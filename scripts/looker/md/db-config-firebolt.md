# Firebolt  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-firebolt

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Create a Looker user
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Firebolt
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Create a Looker user
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Create a Looker user
In Firebolt, create a user email and password for Looker to use to connect to your Firebolt instance.
## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
     * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
     * **Dialect** : Specify the dialect **Firebolt**.
     * **Host** : Specify the endpoint: `api.app.firebolt.io`
     * **Port** : Specify the database port. The default is 443.
     * **Database** : Specify the database name.
     * **Username** : Enter the database user email.
     * **Password** : Enter the database user password.
     * **Additional JDBC parameters** : Add any additional Firebolt JDBC parameters
     * **SSL** : Check to use SSL connections.
     * **Verify SSL** : Check to enforce strict SSL certificate verification.
     * **Max connections per node** : This setting can be left at the default value initially. See the Connecting Looker to your database documentation page for more information.
     * **Connection Pool Timeout** : Can be left at the default value initially. Read more about this setting on the Connecting Looker to your database documentation page.
     * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting on the Connecting Looker to your database documentation page.
     * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the Using time zone settings documentation page for more information.
  3. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  4. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
Firebolt supports the following features as of Looker 25.10:
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
SQL-based pivots | Yes  
Timezones  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
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
Aggregate awareness  
Incremental PDTs  
Milliseconds  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


