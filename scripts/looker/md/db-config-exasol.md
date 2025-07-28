# Exasol  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-exasol

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Create a Looker user
  * Persistent derived tables
  * Enable symmetric aggregates
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Exasol
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Create a Looker user
  * Persistent derived tables
  * Enable symmetric aggregates
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
The Exasol JDBC drivers support encrypted connections. If you're interested, see Exasol's documentation.
## Create a Looker user
First, create a designated Looker user and give it the ability to create sessions:
```
CREATE USER LOOKER IDENTIFIED BY "<password>";
GRANT CREATE SESSION TO LOOKER;

```

Give the Looker user the appropriate `SELECT` permissions for the schema or tables that you plan to access from Looker:
```
GRANT SELECT ON <tables that will be used by LOOKER>;

```

Alternatively, you can grant all privileges:
```
GRANT ALL PRIVILEGES ON SCHEMA <YOUR_SCHEMA> TO LOOKER;

```

Alternatively, if you do not want to have to re-run `GRANT` statements on newly created tables in the future:
```
GRANT SELECT ANY TABLE TO LOOKER;

```

## Persistent derived tables
If you want to enable PDTs for your Looker connection to Exasol, run this command:
```
CREATE SCHEMA LOOKER_SCRATCH;
ALTER SCHEMA LOOKER_SCRATCH CHANGE OWNER LOOKER;

```

Alternatively, you can grant all privileges:
```
GRANT ALL PRIVILEGES ON SCHEMA LOOKER_SCRATCH TO LOOKER;

```

## Enable symmetric aggregates
To allow Exasol to take advantage of symmetric aggregates, create the `hexstring2dec` function:
```
OPENSCHEMAYOUR_SCHEMA>;

createorreplacefunctionhexstring2dec(hexstringinvarchar(32))returndecimal(36,0)
is
possmallint;
current_hexstringchar(1);
current_hexstring_decsmallint;
hexstring_lengthsmallint;
resdecimal(36,0);
begin
ifhexstringisnullthen
returnnull;
endif;
hexstring_length:=length(hexstring);
res:=0;
pos:=1;
whilepos=hexstring_length
do
current_hexstring:=substr(hexstring,pos,1);
ifcurrent_hexstringin('A','B','C','D','E','F')then
current_hexstring_dec:=ascii(current_hexstring)-ascii('A')+10;
else
current_hexstring_dec:=to_number(current_hexstring);
endif;
res:=(res*16)+current_hexstring_dec;
pos:=pos+1;
endwhile;
returnres;
endhexstring2dec;
/

GRANTEXECUTEONFUNCTIONhexstring2dec;

```

## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Exasol** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
Exasol supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views | Yes  
Query killing | Yes  
SQL-based pivots | Yes  
Timezones  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes  
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
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


