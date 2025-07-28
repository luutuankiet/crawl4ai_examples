# MySQL, MariaDB, and SingleStore  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialects that use these instructions
  * Encrypting network traffic
  * Users and security
    * MySQL 5.7.X and earlier, MariaDB, and SingleStore:
  * Temp schema setup for persistent derived tables
  * Alternative setup for regular derived tables
  * Setting the max_allowed_packet variable
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  MySQL, MariaDB, and SingleStore
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialects that use these instructions
  * Encrypting network traffic
  * Users and security
    * MySQL 5.7.X and earlier, MariaDB, and SingleStore:
  * Temp schema setup for persistent derived tables
  * Alternative setup for regular derived tables
  * Setting the max_allowed_packet variable
  * Creating the Looker connection to your database


## Dialects that use these instructions
MySQL, MariaDB, and SingleStore (formerly MemSQL) share the database setup requirements described on this page.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
If you're interested in using SSL encryption, see this MySQL documentation page.
## Users and security
To create and grant the required access to the Looker user, follow the instructions in the section appropriate to your database dialect and version:
### MySQL 8.0.X:
In MySQL 8.0.X, the default authentication plugin is `caching_sha2_password`. Looker uses the `mysql_native_password` plugin to attempt to authenticate to MySQL databases through the JDBC driver. For this version of MySQL to work properly, you must take the following additional steps:
  1. Configure the MySQL database to use the `mysql_native_password` plugin. This can be done in multiple ways, and will depend on how your MySQL 8 database is deployed and what type of access you have to the configuration:
     * Start the process with the flag `--default-auth=mysql_native_password`
     * Set the property in the `my.cnf` configuration file:
```
[mysqld]
default-authentication-plugin=mysql_native_password

```

     * If your database instance is hosted through AWS RDS, set the `default_authentication_plugin` parameter through an RDS Parameter Group that is applied to this database instance.
  2. Run the following commands, replacing `some_password_here` with a unique, secure password:
```
CREATE USER looker IDENTIFIED WITH mysql_native_password BY 'some_password_here';
GRANT SELECT ON database_name.* TO 'looker'@'%';

```



### MySQL 5.7.X and earlier, MariaDB, and SingleStore:
Run the following commands, replacing `some_password_here` with a unique, secure password:
```
CREATEUSERlooker;
SETPASSWORDFORlooker=PASSWORD('some_password_here');
GRANTSELECTONdatabase_name.*TO'looker'@'%';

```

## Temp schema setup for persistent derived tables
These database dialects support the creation of persistent derived tables (PDTs). This feature can be very useful, and we recommend enabling it when possible.
To enable PDTs, you need to configure a temp schema. The following commands show an example of creating a temp database and granting the required privileges to the `looker` user.
> You can specify the name of the temp database in the **Temp Database** field when creating your database connection. If you don't specify a temp database name, Looker generates a scratch database named `looker_tmp`. The following commands use `looker_tmp`, but if you specified a different temp database name, use your temp database name instead of `looker_tmp`.
```
CREATESCHEMAlooker_tmp;
GRANT
SELECT,
INDEX,
INSERT,
UPDATE,
DELETE,
CREATE,
DROP,
ALTER,
CREATETEMPORARYTABLES
ONlooker_tmp.*TO'looker'@'%';

```

For SingleStore, or if your database uses GTID-based replication, you must use the `create_process` LookML parameter to use PDTs, because GTID does not support `CREATE TABLE AS SELECT` statements.
## Alternative setup for regular derived tables
If you do not want to allow the creation of persistent derived tables, you can still use regular derived tables. To use regular derived tables, you still need to add certain permissions to a schema called `looker_tmp`. However, the `looker_tmp` schema does not actually need to exist in your database!
```
GRANT
SELECT,
INDEX,
INSERT,
DROP,
CREATETEMPORARYTABLES
ONlooker_tmp.*TO'looker'@'%';
-- Note that the looker_tmp schema does not need to actually exist,
-- even though these permission grants are still needed

```

## Setting the `max_allowed_packet` variable
For MySQL, set the MySQL `max_allowed_packet` variable to its maximum value, 1073741824, to prevent "SQLException: Packet for query is too large" errors.
## Creating the Looker connection to your database
After completing the database configuration, you can connect to the database from Looker. Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select your database dialect name: **MySQL** , **MySQL 8.0.12+** , **MariaDB** , **SingleStore** , or **SingleStore 7+**.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
MySQL supports the following features as of Looker 25.10:
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
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive  
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
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
MySQL 8.0.12+ supports the following features as of Looker 25.10:
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
Case sensitive  
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
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
MariaDB supports the following features as of Looker 25.10:
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
SQL-based pivots  
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive  
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
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
SingleStore supports the following features as of Looker 25.10:
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
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive  
Location type | Yes  
List type | Yes  
Percentile  
Distinct percentile  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
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
SingleStore 7+ supports the following features as of Looker 25.10:
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
Case sensitive  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
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


