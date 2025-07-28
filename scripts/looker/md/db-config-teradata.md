# Teradata  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-teradata

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Installing the hash_md5 user-defined function (UDF)
  * Installing the Teradata JDBC driver
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Teradata
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Installing the hash_md5 user-defined function (UDF)
  * Installing the Teradata JDBC driver
  * Creating the Looker connection to your database


The procedures that are required to connect Looker to a Teradata database depend on your Looker deployment:
  * For Looker-hosted, Looker (original) instances, contact Looker Support if you want to enable the Teradata driver.
  * For customer-hosted Looker (original) instances, perform the following procedures:
    1. Install the `hash_md5` user-defined function (UDF) on your Teradata server.
    2. Install the Teradata JDBC driver.
    3. Create the Looker connection to your database.
  * For Looker (Google Cloud core) instances, perform the following procedures:
    1. Install the `hash_md5` user-defined function (UDF) on your Teradata server.
    2. Create the Looker connection to your database.


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Installing the `hash_md5` user-defined function (UDF)
Before configuring Looker to work with Teradata, you must install the `hash_md5` user-defined function (UDF) on your Teradata server. You can find instructions for installing the UDF on this Teradata downloads page.
## Installing the Teradata JDBC driver
If you have a Looker (original) instance, you will need to configure a Teradata driver before creating the Looker connection. These instructions describe that process, assuming use of a startup script that is similar to the examples that are provided on the looker-open-source GitHub page.
To install the driver, you will need to acquire two Teradata files, include them as part of the startup process, and add an option to tell Looker to access the driver.
Follow the steps on the Unpackaged JDBC drivers documentation page using the following values:
**driver symbol** : `teradata`
**driver entry** :
```
- name: teradata
  dir_name: teradata
  module_path: com.teradata.jdbc.TeraDriver

```

For the step to put the driver in your dialect's directory, the paths to these files will look like this:
  * `looker/custom_jdbc_drivers/teradata/tdgssconfig.jar`
  * `looker/custom_jdbc_drivers/teradata/terajdbc4.jar`


## Creating the Looker connection to your database
To create the connection from Looker to your database, follow these steps:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Teradata** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
Teradata supports the following features as of Looker 25.10:
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
Timezones  
SSL  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
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


