# DataVirtuality  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-datavirtuality

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Installing the DataVirtuality JDBC driver
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  DataVirtuality
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Installing the DataVirtuality JDBC driver
  * Creating the Looker connection to your database


To use Looker with DataVirtuality, you will need to configure a DataVirtuality driver. These instructions describe that process, assuming use of a startup script similar to the examples provided on the looker-open-source GitHub page.
You will need to acquire a DataVirtuality driver JAR, include it as part of the startup process, and add an option to tell Looker to access it.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Installing the DataVirtuality JDBC driver
Follow the steps on the Unpackaged JDBC drivers documentation page using the following values:
**driver symbol** : `datavirtuality`
**driver entry** :
```
- name: datavirtuality
  dir_name: datavirtuality
  module_path: com.datavirtuality.dv.jdbc.Driver

```

## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **DataVirtuality** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
DataVirtuality supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates | Yes  
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
Aggregate awareness  
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


