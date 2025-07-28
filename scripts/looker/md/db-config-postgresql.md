# PostgreSQL  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-postgresql

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialects that use these instructions
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
    * Self-hosted Postgres
    * Postgres on Amazon RDS
  * Setting the search_path
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  PostgreSQL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialects that use these instructions
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
    * Self-hosted Postgres
    * Postgres on Amazon RDS
  * Setting the search_path
  * Creating the Looker connection to your database


## Dialects that use these instructions
The following dialects share database setup requirements as described on this page:
  * PostgreSQL
  * Google Cloud SQL for PostgreSQL
  * Microsoft Azure PostgreSQL
  * AlloyDB for PostgreSQL
  * Amazon Aurora PostgreSQL
  * Amazon RDS for PostgreSQL


For Google Cloud SQL for PostgreSQL, Looker (Google Cloud core) offers Application Default Credentials (ADC) as a method of authentication. See the Looker (Google Cloud core) documentation for more information.
For AlloyDB for PostgreSQL, Amazon RDS for PostgreSQL, and Amazon Aurora PostgreSQL, Looker has integration support. To create a connection for these dialects, select **PostgreSQL 9.5+** from the **Dialect** drop-down on the **New Connection** page.
For PostgreSQL on Heroku, see the Heroku documentation.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
If you're interested in using SSL encryption, see the PostgreSQL documentation.
## Users and security
To perform actions on your database, Looker needs to have a user account on your database.
If you're on a Looker (Google Cloud core) instance and you want to use ADC, use the impersonated service account username that you added to your Cloud SQL database. The service account username will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. If your service account username ends with `.gserviceaccount.com`, remove the `.gserviceaccount.com` portion of the username. After it's truncated, the username would look like `service-<project number>@gcp-sa-looker.iam`.
To configure a database user for Looker to use, perform the following steps on your database:
  1. Create a database user and password.
```
CREATEUSERUSERNAMEWITHENCRYPTEDPASSWORD'PASSWORD';

```

  2. Grant permissions to the database user so that Looker can perform actions on your database:
```
GRANTCONNECTONDATABASEDATABASE_NAMEtoUSERNAME;
\cDATABASE_NAME
GRANTSELECTONALLSEQUENCESINSCHEMApublicTOUSERNAME;
GRANTSELECTONALLTABLESINSCHEMApublicTOUSERNAME;

```

  3. If you're using a schema other than `public`, run this command to grant usage permissions to Looker:
```
GRANTUSAGEONSCHEMASCHEMA_NAMETOUSERNAME;

```

  4. To make sure that future tables that you add to the public schema are also available to the Looker user, run these commands:
```
ALTERDEFAULTPRIVILEGESINSCHEMApublicGRANTSELECTONtablesTOUSERNAME;
ALTERDEFAULTPRIVILEGESINSCHEMApublicGRANTSELECTONsequencesTOUSERNAME;

```



Depending on your setup, the preceding commands may need to be altered. If another user or role is creating tables that the Looker user needs future permissions for, you must specify a _target_ role or user to apply the Looker user's permission grants to:
```
ALTERDEFAULTPRIVILEGESFORUSERANOTHER_USERNAMEINSCHEMASCHEMA_NAMEGRANTSELECTONtablesTOUSERNAME;
ALTERDEFAULTPRIVILEGESFORROLETARGET_ROLEINSCHEMASCHEMA_NAMEGRANTSELECTONsequencesTOUSERNAME;

```

For example, if a `web_app` user creates tables and you want the `looker` user to be able to use those tables, you must run a `GRANT` statement to give the `looker` user permissions on tables that are created by the `web_app` user. The target role or user in this case is the `web_app` user, meaning you want to alter privileges on tables that are created by `web_app` so that the `looker` user can have permissions to read the tables. Here is an example:
```
ALTERDEFAULTPRIVILEGESFORUSERweb_appINSCHEMApublicGRANTSELECTONtablesTOlooker;

```

See `ALTER DEFAULT PRIVILEGES` on PostgreSQL's website for more information.
## Temp schema setup
### Self-hosted Postgres
Create a schema owned by the Looker user:
```
CREATESCHEMASCHEMA_NAMEAUTHORIZATIONUSERNAME;

```

### Postgres on Amazon RDS
Create a scratch schema:
```
CREATESCHEMASCHEMA_NAME;

```

Change the ownership of the scratch schema to the Looker user:
```
ALTERSCHEMASCHEMA_NAMEOWNERTOUSERNAME;

```

## Setting the `search_path`
Before connecting Looker to your database, you should set an appropriate `search_path`, which the Looker SQL Runner can use to retrieve certain metadata from your database:
```
ALTERUSERUSERNAMESETsearch_pathTO'$user',SCHEMA_NAME,SCHEMA_NAME_2,SCHEMA_NAME_3
^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^
includeacomma-separatedlistof
allschemasyou'llusewithLooker

```

## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select your database dialect name. For the AlloyDB for PostgreSQL dialect, select **PostgreSQL 9.5+**.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
PostgreSQL 9.5+ supports the following features as of Looker 25.10:
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
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile | Yes  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling | Yes  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Google Cloud PostgreSQL supports the following features as of Looker 25.10:
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
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile | Yes  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling | Yes  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Microsoft Azure PostgreSQL supports the following features as of Looker 25.10:
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
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile | Yes  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling | Yes  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


