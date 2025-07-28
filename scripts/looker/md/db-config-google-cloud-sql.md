# Google Cloud SQL for MySQL  |  Looker

**Source:** https://cloud.google.com/looker/docs/db-config-google-cloud-sql

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Users and security
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Google Cloud SQL for MySQL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Users and security
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Users and security
To perform actions on your database, Looker needs to have a user account on your database.
To configure a database user for Looker to use, perform the following steps on your database:
  1. Create a database user.
```
CREATEUSERUSERNAME;
SETPASSWORDFORUSERNAME=PASSWORD('PASSWORD');

```

  2. Grant `SELECT` privileges to the database user on the database that you want Looker to query. Replace `database_name` with the name of your database.
```
GRANTSELECTONDATABASE_NAME.*TOUSERNAME;

```



Once you create the database user, you can enter the database user account credentials in the **Username** and **Password** fields of the Looker UI when you create the Looker connection to your database.
## Creating the Looker connection to your database
To create the connection from Looker to your database, follow these steps:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select **Google Cloud SQL**.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
     * **Host** : The database hostname that is used to connect to the Google Cloud SQL for MySQL database. For an SSH tunnel, use `localhost`.
     * **Port** : The port used that is to connect to the Google Cloud SQL for MySQL database.
     * **Database** : The name of the Google Cloud SQL for MySQL database instance.
     * **Username** : The username of the account that Looker will use to sign in to Google Cloud SQL for MySQL.
     * **Password** : The password of the account that Looker will use to sign in to Google Cloud SQL for MySQL.
     * **Additional JDBC parameters** : Additional JDBC parameters (optional).
     * **SSL** : If checked, enables an SSL connection; however, SSL connections to Google Cloud SQL for MySQL are not supported by default.
     * **Verify SSL** : If checked, SSL verification is enforced. However, SSL connections to Google Cloud are not supported by default.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## PDT support
Google Cloud SQL for MySQL does not support `CREATE TABLE AS SELECT` statements, so you must use the `create_process` LookML parameter to define PDTs.
## Feature support
For Looker to support some features, your database dialect must also support them.
Google Cloud SQL supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables  
Stable views  
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
Aggregate awareness  
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
## Next steps
After you have created your database connection, set authentication options.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


