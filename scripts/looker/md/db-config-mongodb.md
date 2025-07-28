# MongoDB Connector for BI  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-mongodb

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * MongoDB Atlas
    * Configuring the MongoDB Connector for BI
    * Adding the Looker server to the Atlas IP access list
    * Enabling the MongoDB Connector for BI
  * MongoDB on the same server
    * Installing the Mongo Connector for BI
    * Encrypting network traffic
    * Setting up the Looker user and permissions
  * Installing the MongoBI JDBC driver files
    * Allowing use of regular derived tables (recommended)
  * Creating the Looker connection to your database
  * Using SQL functions and operators with MongoDB Connector for BI




Was this helpful?
Send feedback 
#  MongoDB Connector for BI
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * MongoDB Atlas
    * Configuring the MongoDB Connector for BI
    * Adding the Looker server to the Atlas IP access list
    * Enabling the MongoDB Connector for BI
  * MongoDB on the same server
    * Installing the Mongo Connector for BI
    * Encrypting network traffic
    * Setting up the Looker user and permissions
  * Installing the MongoBI JDBC driver files
    * Allowing use of regular derived tables (recommended)
  * Creating the Looker connection to your database
  * Using SQL functions and operators with MongoDB Connector for BI


Looker can access MongoDB using the MongoDB Connector for BI using two options:
  * Using the MongoDB Connector for BI in MongoDB Atlas.
  * Using a MongoDB Connector for BI installed on the same server as the MongoDB database.


## MongoDB Atlas
Your MongoDB Atlas must use an M10+ cluster. For Looker to use a MongoDB database running on MongoDB Atlas, you must use the MongoDB Connector for BI (MongoBI). Enabling the BI Connector for Atlas requires that MongoDB Atlas use a M10+ cluster.
You must also create a user account that has read permissions for the desired database.
### Configuring the MongoDB Connector for BI
Before creating a connection in Looker, your MongoDB or Atlas administrator needs to set up the MongoDB Connector for BI using the following steps, which are explained on this page:
  * Add the Looker server to the Atlas IP access list
  * Enable the MongoDB Connector for BI
  * Allow use of regular derived tables (recommended)


### Adding the Looker server to the Atlas IP access list
Atlas only allows client connections from entries in the project's IP access list. Add the Looker IP address to the Atlas project's IP access list:
  1. Get the Looker IP address.
  2. Follow the Atlas IP access list setup instructions to add the Looker IP address to the Atlas IP access list.


### Enabling the MongoDB Connector for BI
Enable the MongoDB Connector for BI:
  1. Verify that you are on a M10+ cluster.
  2. In Atlas, open the Connect page for the cluster. Make a note of the hostname, port, and user. You'll need to use that information when configuring the connection in Looker.


## MongoDB on the same server
Before creating a connection in Looker, your MongoDB administrator should set up MongoDB and the Mongo Connector for BI using the following steps, which are explained on this page:
  * Installing the Mongo Connector for BI
  * Encrypting network traffic
  * Setting up the Looker user and permissions
  * Allowing use of regular derived tables (recommended)


### Installing the Mongo Connector for BI
Install the MongoDB Connector for BI on the same server as the MongoDB database, as explained on the Install BI Connector On Premises  MongoDB documentation page.
### Encrypting network traffic
The MongoDB Connector for BI requires using SSL encryption between MongoDB's server and the Looker application. Follow the SSL setup instructions on the Configure SSL for BI Connector MongoDB documentation page.
### Setting up the Looker user and permissions
In the MongoDB shell, enter the `use` command to switch to the database that Looker will connect to. Then, create a user for Looker with `db.createUser()` with the role `readWrite`:
```
use looker_database

db.createUser({ user: looker,
                pwd: `some_password_here`,
                roles: [ "readWrite" ]
              })

```

## Installing the MongoBI JDBC driver files
For both MongoDB Connector for BI options, Looker requires configuring JDBC driver files by doing the following steps:
Download these two JAR files:
  * mysql connector java 5.1.47


Follow the steps on the Unpackaged JDBC drivers documentation page using the following values:
**driver symbol** : `mongobi`
**driver entry** :
```
- name: mongobi
  dir_name: mongobi
  module_path: com.mysql.jdbc.Driver
  override_jdbc_url_subprotocol: mysql

```

**If you are on Looker 6.2 or earlier** :
```
- name: maria15x
  dir_name: mongobi
  module_path: com.mysql.jdbc.Driver
  override_jdbc_url_subprotocol: mysql

```

For the step to put the driver in your dialect's directory, the paths to these files will look like this:
  * `looker/custom_jdbc_drivers/mongobi/mongosql-auth-1.0.0-rc0.jar`
  * `looker/custom_jdbc_drivers/mongobi/mysql-connector-java-5.1.47.jar`


### Allowing use of regular derived tables (recommended)
Derived tables are important tools in Looker that enable you to expand the sophistication of your analyses. They can also play a valuable role in enhancing query performance. At a high level, the Looker derived table capability provides a way to create new tables that don't already exist in your database.
The MongoDB Connector for BI supports temporary regular derived tables but does not support persistent derived tables.
Since regular derived tables are temporary, they don't need to be stored. Thus, you don't need to create a schema for them. However, you need to grant the `dbOwner` role to `looker_tmp` schema, even if that schema does not exist.
Follow the Modify MongoDB Users section on this MongoDB documentation page about configuring database users to add the `dbOwner` role on `looker_tmp` for the user Looker will use to connect.
```
db.grantRolesToUser("looker", [ {role: "dbOwner", db: "looker_tmp"} ])

```

## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **MongoBI** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Using SQL functions and operators with MongoDB Connector for BI
When developing using a MongoDB Connector for BI connection, you can use the SQL functions and operators listed in the MongoDB documentation.
## Feature support
For Looker to support some features, your database dialect must also support them.
MongoBI supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates  
Derived tables | Yes  
Persistent SQL derived tables  
Persistent native derived tables  
Stable views  
Query killing | Yes  
SQL-based pivots  
Timezones  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
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
Aggregate awareness  
Incremental PDTs  
Milliseconds  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
In addition:
  * MongoDB does not support millisecond and microsecond timeframes for dimension groups.
  * MongoDB does not support millisecond, millisecondX, and microsecond types for dimensions.
  * Looker treats all timestamps accessed from MongoBI as being in the coordinated universal time (UTC) time zone.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


