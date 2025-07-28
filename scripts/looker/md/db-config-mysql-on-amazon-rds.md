# Amazon RDS for MySQL  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-mysql-on-amazon-rds

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Modifying an existing replica
    * Users and security
    * RDS and temporary tables
    * Create database and grant permissions
  * Creating a new replica
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Amazon RDS for MySQL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Modifying an existing replica
    * Users and security
    * RDS and temporary tables
    * Create database and grant permissions
  * Creating a new replica
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
If you're interested in using SSL encryption, see the MySQL RDS documentation.
## Options
For performance reasons, it is common to use read-only replica databases — also called read replicas — with Looker. This frees up the production database to perform its primary function without any queries potentially slowing it down.
This document describes how to either:
  * Modify an existing replica database to work with Looker
  * Create a new read replica database and configure it to work with Looker


## Modifying an existing replica
### Users and security
Change `<some_password_here>` to a unique, secure password:
```
CREATE USER looker;
SET PASSWORD FOR looker = PASSWORD ('<some_password_here>');
GRANT SELECT ON database_name.* TO 'looker'@'%';

```

### RDS and temporary tables
RDS read replicas, by default, have a read-only flag enabled that prevents Looker from writing to temporary tables. Looker never actually changes existing data, but MySQL still requires write access to use temp tables. This can be solved by changing the flag in RDS. From the RDS FAQ:
**Q: Can my read replicas only accept database read operations?**
Read replicas are designed to serve read traffic. However, there may be use cases where advanced users wish to complete Data Definition Language (DDL) SQL statements against a read replica. Examples might include adding a database index to a read replica that is used for business reporting without adding the same index to the corresponding source DB instance. 
Amazon RDS for MySQL can be configured to permit DDL SQL statements against a read replica. If you wish to enable operations other than reads for a given read replica, modify the active DB Parameter Group for the read replica setting the `read_only` parameter to `0`. 
Amazon RDS for PostgreSQL does not currently support the execution of DDL SQL statements against a read replica. 
If you alter the DB Parameter Group, you will need to restart the read replica for the changes to take effect.
### Create database and grant permissions
Create a temp database and give the `looker` user the rights to write to it. The `CREATE TEMPORARY` statement in MySQL needs to be associated with a DB for permission purposes.
```
CREATE SCHEMA looker_tmp;
GRANT
  SELECT,
  INDEX,
  INSERT,
  UPDATE,
  DELETE,
  CREATE,
  DROP,
  ALTER,
  CREATE TEMPORARY TABLES
ON looker_tmp.* TO 'looker'@'%';

```

## Creating a new replica
Note that AWS RDS can only create read replicas with database instances that have **Backup Retention** activated.
### Pre-AWS steps
#### Step 1
`mysql` into the database that will be the primary database instance:
```
mysql -h hostname.uid.region.rds.amazonaws.com -P 3306 -u root -p

```

#### Step 2
Create a user named `looker` (replace `<some_password_here>` with a unique, secure password):
```
CREATE USER looker IDENTIFIED BY '<some_password_here>';

```

#### Step 3
Create a temporary database and grant read privileges to Looker for other databases and tables. Looker generally doesn't write to the `looker_tmp` database but uses it to execute `CREATE TEMPORARY TABLE` commands.
```
CREATE SCHEMA looker_tmp;
GRANT
  SELECT,
  INDEX,
  INSERT,
  UPDATE,
  DELETE,
  CREATE,
  DROP,
  ALTER,
  CREATE TEMPORARY TABLES
ON looker_tmp.* TO 'looker'@'%';

GRANT
  SELECT,
  SHOW DATABASES
ON *.* TO 'looker'@'%';

```

#### Step 4
Flush privileges:
```
FLUSH PRIVILEGES;

```

### AWS steps
#### Step 1
Log in and go to the AWS dashboard. In the **Database** section, select **RDS**.
#### Step 2
On your RDS dashboard, select the database instance you want to specify as the primary database. Select **Instance Actions** , and then select **Create Read Replica**.
#### Step 3
In the **Create Read Replica DB Instance** pop-up, configure the read replica database and select **Yes, Create Read Replica**.
#### Step 4
While you're waiting for the read replica database to be created, you can set up the **DB Parameter Group** , which will contain the engine configuration values that are applied to the read replica database instance. Select the **DB Parameter Groups** page in the sidebar, and then select the **Create DB Parameter Group** button.
#### Step 5
Select the **DB Parameter Group Family** and **DB Parameter Group Name** , and enter a **DB Parameter Group Description**. Then select **Yes, Create**.
#### Step 6
Select the magnifying glass icon on the row that contains the read replica database parameter group, _or_ select that row and select **Edit Parameters**.
#### Step 7
In the **Filters** field under **Parameters** , search for "read_only". Change the parameter value to a `0`. Then select **Save Changes**.
#### Step 8
When the read replica creation has finished, select it from the list of database instances, select the **Instance Action** button, and select **Modify** in the instance action.
#### Step 9
In the **Modify DB Instance** pop-up, change the DB instance **Parameter Group** to the new read replica parameter group. Then check the **Apply Immediately** box, select **Continue** , and select **Modify DB Instance**.
#### Step 10
Using the MySQL client, connect to the read replica database instance as `looker` and test to see if data is accessible.
## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


