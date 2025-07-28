# Oracle  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-oracle

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Creating a Looker user
  * Ensuring Looker can see all tables
  * Setting up main database objects
  * Setting up symmetric aggregates
  * Setting up persistent derived tables
  * Setting up query killing
    * Standard Oracle deployments
    * Amazon RDS deployments
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Oracle
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Creating a Looker user
  * Ensuring Looker can see all tables
  * Setting up main database objects
  * Setting up symmetric aggregates
  * Setting up persistent derived tables
  * Setting up query killing
    * Standard Oracle deployments
    * Amazon RDS deployments
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
If you're interested in using SSL encryption, see the Oracle documentation.
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

## Ensuring Looker can see all tables
Looker may not be able to identify tables (especially empty tables) without first collecting statistics in Oracle. If tables you need do not appear in generated LookML or SQL Runner, try executing:
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
sess.username='LOOKER';

CREATEORREPLACESYNONYMLOOKER.LOOKER_SQLFORLOOKER_SQL;

GRANTSELECTONLOOKER.LOOKER_SQLTOLOOKER;

-- Pay special attention to the following comments:
-- the following view will be different for clustered Oracle deployments
CREATEORREPLACEVIEWLOOKER_SESSION
AS
SELECT
SID,
USERNAME,
TYPE,
STATUS,
SQL_ID,
-- If using a single node Oracle deployment
"SERIAL#",
-- If using a clustered Oracle deployment, like Oracle Real Application Clusters
(SERIAL#||','||INST_ID)AS"SERIAL#",
AUDSID
-- If using a single node Oracle deployment
FROMV$SESSION
-- If using a clustered Oracle deployment, like Oracle Real Application Clusters
FROMGV$SESSION
WHERE
USERNAME='LOOKER';

CREATEORREPLACESYNONYMLOOKER.LOOKER_SESSIONFORLOOKER_SESSION;

GRANTSELECTONLOOKER.LOOKER_SESSIONTOLOOKER;

```

## Setting up symmetric aggregates
Your Oracle DBA must set up the `LOOKER_HASH` function to enable symmetric aggregates. The `LOOKER_HASH` function is a synonym for the Oracle `dbms_crypto.hash` function. The DBA must also create the associated synonym and privileges. The following commands assume that the Looker user's name is `LOOKER`:
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
Follow these instructions to configure query killing for either a standard Oracle deployment or an Amazon RDS deployment.
### Standard Oracle deployments
To set up query killing in standard Oracle deployments, the Oracle DBA must create the `LOOKER_KILL_QUERY` procedure as a synonym of `ALTER SYSTEM KILL SESSION`. To do this, execute the following command:
```
CREATEORREPLACEPROCEDURELOOKER_KILL_QUERY(p_sidinvarchar2,
p_serial#invarchar2)
IS
cursor_namepls_integerdefaultdbms_sql.open_cursor;
ignorepls_integer;

BEGIN
SELECT
COUNT(*)INTOignore
-- If using a single node Oracle deployment
FROMV$SESSION
-- If using a clustered Oracle deployment, like Oracle Real Application Clusters
FROMGV$SESSION
WHERE
username=USER
ANDsid=p_sid
-- If using a single node Oracle deployment
ANDserial#=p_serial#;
-- If using a clustered Oracle deployment, like Oracle Real Application Clusters
AND(SERIAL#||','||INST_ID)=p_serial#;

IF(ignore=1)
THEN
dbms_sql.parse(cursor_name,
'ALTER SYSTEM KILL SESSION '''
||p_sid||','||p_serial#||'''',
dbms_sql.native);
ignore:=dbms_sql.execute(cursor_name);
ELSE
raise_application_error(-20001,
'You do not own session '''||
p_sid||','||p_serial#||
'''');
ENDIF;
END;

```

The DBA will also need to run these related commands:
```
CREATEORREPLACESYNONYMLOOKER.LOOKER_KILL_QUERYFORSYS.LOOKER_KILL_QUERY;
GRANTEXECUTEONSYS.LOOKER_KILL_QUERYTOLOOKER;

```

> Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.
### Amazon RDS deployments
In Amazon RDS Oracle deployments, the `rdsadmin.rdsadmin_util.kill` procedure is used to kill queries. To use this procedure, the Looker database user must have the `DBA` role assigned.
> Because DBA is an elevated database role, you might consider skipping this step and forgoing query killing in Looker.
To give the Looker database user query killing abilities, run the following command:
```
GRANTDBATOLOOKER;

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. The following settings are specific to Oracle:
  * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : Oracle.
  * **Use TNS** : Enable Transparent Network Substrate (TNS) connections.
  * **Host** : Hostname or TNS alias.
  * **Port** : Database port.
  * **Database** : Database name (if not using TNS).
  * **Service Name** : Service name (if using TNS).
  * **Username** : Database username or **Temp Database** if PDTs are enabled.
  * **Password** : Database user password.
  * **Enable PDTs** : Use this toggle to enable persistent derived tables. When PDTs are enabled, the **Connection** window reveals additional PDT settings and the **PDT Overrides** section.
  * **Temp Database** : In Oracle _a user is a schema_ , so this should be specified as the name of the database user. For this example, you would use the temp schema value `LOOKER`.
  * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the Connecting Looker to your database documentation page.
  * **Additional JDBC parameters** : Leave this blank, since Oracle does not support additional JDBC parameters.
  * **Maintenance Schedule** : A `cron` expression that indicates when Looker should check datagroups and persistent derived tables. Read more about this setting in the Maintenance Schedule documentation.
  * **SSL** : Check to use SSL connections.
  * **Verify SSL** : Ignore this field. Oracle will use the default Java Truststore to verify SSL.
  * **Max connections per node** : This setting can be left at the default value initially. Read more about this setting in the Max connections per node section of the **Connecting Looker to your database** documentation page.
  * **Connection Pool Timeout** : This setting can be left at the default value initially. Read more about this setting in the Connection Pool Timeout section of the **Connecting Looker to your database** documentation page.
  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, uncheck this option. Read more about this setting in the SQL Runner Precache section of the **Connecting Looker to your database** documentation page.
  * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the Using time zone settings documentation page for more information.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
## Feature support
For Looker to support some features, your database dialect must also support them.
Oracle supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views | Yes  
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
SQL Runner Show Indexes | Yes  
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


