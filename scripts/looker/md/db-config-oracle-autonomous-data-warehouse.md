# Oracle Autonomous Data Warehouse on Cloud  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-oracle-autonomous-data-warehouse

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Setting up the Looker host for connections
  * Creating a Looker user
  * Ensuring that Looker can see all tables
  * Setting up main database objects
  * Setting up symmetric aggregates
  * Setting up persistent derived tables
  * Setting up query killing
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Oracle Autonomous Data Warehouse on Cloud
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Setting up the Looker host for connections
  * Creating a Looker user
  * Ensuring that Looker can see all tables
  * Setting up main database objects
  * Setting up symmetric aggregates
  * Setting up persistent derived tables
  * Setting up query killing
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Setting up the Looker host for connections
All Oracle ADWC connections require SSL and certificate authentication. In order for Looker to connect to your Oracle ADWC instance, it is necessary to download your Oracle wallet files and install them on the Looker server. If you are a customer-hosted Looker user, you will need a system administrator with access to the Looker server to do this. If you are a Looker-hosted user, reach out to Looker Support.
To install your Oracle wallet on the Looker server:
  1. Download your Oracle wallet to your **local** computer. You will have a zip file named something like `Wallet_databasename.zip`.
  2. On the Looker server, make a directory to hold the wallet zip file:
```
mkdir /home/looker/looker/credentials

```

  3. Copy the wallet zip file from your local computer to the Looker server. This example uses `scp` and places the file in `/home/looker/looker/credentials`:
```
scp Wallet_databasename.zip username@remotehost:/home/looker/looker/credentials

```

  4. Unzip the wallet zip file. This example uses the command `unzip`:
```
cd /home/looker/looker/credentials
unzip Wallet_databasename.zip

```

  5. Verify the contents of the wallet with the `ls` command. These are the files you should have:
```
 ls

 cwallet.sso  keystore.jks      sqlnet.ora    truststore.jks
 ewallet.p12  ojdbc.properties  tnsnames.ora

```

Looker connects to Oracle ADWC using Oracle Wallets with the JDBC Thin Driver 18.3. For this, you will need the Transparent Network Substrate (TNS) Alias of the Oracle ADWC Service level for your database and the PATH to your Oracle wallet files.
  6. To get the TNS Alias of your database, run this command:
```
cat tnsnames.ora

```

There will be three TNS aliases to choose from: `dbname_high`, `dbname_medium`, and `dbname_low`. These aliases correspond to different levels of service. The protocol, host, port, service name, and SSL information is included in this file. For this example, we will use `dbname_medium`.


## Creating a Looker user
First, create a designated Looker user:
```
-- connect / as sysdba;
CREATEUSERLOOKERIDENTIFIEDBYpassword>
DEFAULTTABLESPACEUSERS
TEMPORARYTABLESPACETEMP;

```

Next, give the new Looker user the ability to create sessions:
```
GRANTCREATESESSIONTOLOOKER;

```

Finally, give the Looker user the appropriate `SELECT` permissions for the data tables that you plan to access from Looker. If you want to access additional tables in the future, you will need to grant `SELECT` on those new tables as well.
```
GRANTSELECTON-- <all tables that will be used by looker>;

```

## Ensuring that Looker can see all tables
Looker may not be able to identify tables (especially empty tables) without first collecting statistics in Oracle. If tables you need don't appear in generated LookML or SQL Runner, execute this command:
```
EXECDBMS_STATS.GATHER_DATABASE_STATS;

```

For alternative methods, consult your Oracle documentation.
## Setting up main database objects
Your Oracle DBA must set up the following objects and permissions on Oracle. The following commands create `LOOKER_SESSION` and `LOOKER_SQL` as synonyms for `V$SESSION` and `V$SQL`.
Run the following commands as the root user to complete this setup. These examples assume that the Looker user's name is `LOOKER`.
```
CREATEORREPLACEVIEWLOOKER_SQL
AS
SELECT
sql.SQL_ID,
sql.SQL_TEXT
FROM
V$SQLsql,
v$sessionsess
WHERE
sess.SQL_ADDRESS=sql.ADDRESSAND
sess.username=&apos;LOOKER&apos;;

CREATEORREPLACESYNONYMLOOKER.LOOKER_SQLFORLOOKER_SQL;

GRANTSELECTONLOOKER.LOOKER_SQLTOLOOKER;

-- Pay special attention to the comments:
-- the following view will be different for clustered Oracle deployments
CREATEORREPLACEVIEWLOOKER_SESSION
AS
SELECT
SID,
USERNAME,
TYPE,
STATUS,
SQL_ID,
-- If using a single node Oracle ADWC deployment
"SERIAL#",
-- If using a clustered Oracle ADWC deployment
(SERIAL#||','||INST_ID)AS"SERIAL#",
AUDSID
-- If using a single node Oracle ADWC deployment
FROMV$SESSION
-- If using a clustered Oracle ADWC deployment
FROMGV$SESSION
WHERE
USERNAME=&apos;LOOKER&apos;;

CREATEORREPLACESYNONYMLOOKER.LOOKER_SESSIONFORLOOKER_SESSION;

GRANTSELECTONLOOKER.LOOKER_SESSIONTOLOOKER;

```

## Setting up symmetric aggregates
Your Oracle DBA must set up the `LOOKER_HASH` function to enable symmetric aggregates. The `LOOKER_HASH` function is a synonym for the Oracle `dbms_crypto.hash` function. The DBA must also create the associated synonym and privileges. The following example assumes that the Looker user's name is `LOOKER`:
```
CREATEORREPLACEFUNCTIONLOOKER_HASH(bytesraw,precnumber)
RETURNrawAS
BEGIN
return(dbms_crypto.HASH(bytes,prec));
END;

CREATEORREPLACESYNONYMLOOKER.LOOKER_HASHFORLOOKER_HASH;

GRANTEXECUTEONLOOKER.LOOKER_HASHTOLOOKER;

GRANTEXECUTEONSYS.LOOKER_HASHTOLOOKER;

```

> Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.
## Setting up persistent derived tables
To enable persistent derived tables, give the Looker user the `UNLIMITED TABLESPACE` and `CREATE TABLE` permissions. The following commands assume that the Looker user's name is `LOOKER`:
```
GRANTUNLIMITEDTABLESPACETOLOOKER;
GRANTCREATETABLETOLOOKER;

```

## Setting up query killing
To set up query killing, the Oracle DBA must create the `LOOKER_KILL_QUERY` procedure as a synonym of `ALTER SYSTEM KILL SESSION`. To do this, execute the following command:
```
CREATEORREPLACEPROCEDURELOOKER_KILL_QUERY(p_sidinvarchar2,
p_serial#invarchar2)
IS
cursor_namepls_integerdefaultdbms_sql.open_cursor;
ignorepls_integer;

BEGIN
SELECT
COUNT(*)INTOIGNORE
-- If using a single node Oracle ADWC deployment
FROMV$SESSION
-- If using a clustered Oracle ADWC deployment
FROMGV$SESSION
WHERE
username=USER
ANDsid=p_sid
-- If using a single node Oracle ADWC deployment
ANDserial#=p_serial#;
-- If using a clustered Oracle ADWC deployment
AND(SERIAL#||','||INST_ID)=p_serial#;

IF(ignore=1)
THEN
dbms_sql.parse(cursor_name,
apos;ALTERSYSTEMKILLSESSIONapos;&apos;&apos;
||p_sid||apos;,&apos;||p_serial#||apos;&apos;&apos;&apos;,
dbms_sql.native);
ignore:=dbms_sql.execute(cursor_name);
ELSE
raise_application_error(-20001,
apos;Youdonotownsessionapos;&apos;&apos;||
p_sid||apos;,&apos;||p_serial#||
apos;&apos;&apos;&apos;);
ENDIF;
END;

```

The DBA will also need to run these related commands:
```
CREATEORREPLACESYNONYMLOOKER.LOOKER_KILL_QUERYFORSYS.LOOKER_KILL_QUERY;
GRANTEXECUTEONSYS.LOOKER_KILL_QUERYTOLOOKER;

```

> Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.
## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. The following settings are specific to Oracle ADWC:
     * **Dialect** : **Oracle ADWC**.
     * **Use TNS** : Enable Transparent Network Substrate (TNS) connections.
     * **Host** : Hostname or TNS alias. For this example, `dbname_medium`.
     * **Port** : Leave as default; Looker will find the port from the `tnsnames.ora` file.
     * **Service Name** : Leave blank; Looker will find the service name from the `tnsnames.ora` file.
     * **Username** : Database username or **Temp Database** if PDTs are enabled.
     * **Password** : Database user password.
     * **Enable PDTs** : Use this toggle to enable persistent derived tables. When PDTs are enabled, the **Connection** window reveals additional PDT settings and the **PDT Overrides** section.
     * **Temp Database** : In Oracle, _a user is a schema_ , so this should be specified as the name of the database user. For this example, you would use the temp schema value `LOOKER`.
     * **Additional JDBC Parameters** : The **PATH** to your Oracle wallet on the Looker server. For this example, it's `/home/looker/looker/credentials`.
     * On a Looker-hosted legacy deployment, this value will be `/home/lookerops/looker/credentials`.
     * On a Looker-hosted deployment in next-generation hosting, this value will be `/app/credentials`.
     * **SSL and Verify SSL** : You can ignore these fields; Looker will always use SSL with Oracle ADWC.
  3. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information. When you click **Test** , Looker will build a JDBC string like this:
`jdbc:oracle:thin:@dbname_medium?TNS_ADMIN=/home/looker/looker/credentials`
  4. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
Oracle ADWC supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Integration  
Looker (Google Cloud core)  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views  
Query killing | Yes  
SQL-based pivots | Yes  
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC additional params  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


