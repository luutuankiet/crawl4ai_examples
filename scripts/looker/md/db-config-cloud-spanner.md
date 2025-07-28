# Google Spanner  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-cloud-spanner

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Getting the connection credentials
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Google Spanner
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Getting the connection credentials
  * Creating the Looker connection to your database


This page explains how to set up a connection in Looker to Google Spanner.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Getting the connection credentials
  1. Log in to the Google Cloud console.
  2. Select the appropriate project.
  3. From the menu, select **IAM & Admin** and then **Service accounts**.
  4. Select **Create service account** and fill in the dialog box as follows:
     * **Service account name** : Enter `looker-spanner-service` or something similar.
     * **Role** : Select **Cloud Spanner** and then **Cloud Spanner Database Reader**.
     * **Furnish a new private key** : Select the **Furnish a new private key** checkbox, and select **JSON** under **Key type**.
  5. Click **Create** and keep track of the following:
     * The email address associated with the service account
     * The name and location of the JSON credential file that was downloaded


## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Dialect** : **Google Spanner**.
  * **Name** : The name of the connection.
  * **Project Name** : The project ID for the Google project that contains the Spanner database.
  * **Instance Name** : The name of the instance that contains the Spanner database.
  * **Database** : The name of the Spanner database.
  * **Schema** : Leave this blank.
  * **Max connections per node** : The maximum number of total connections to the Spanner database across all users. The default is 30. This setting can be left at the default value initially. See the Connecting Looker to your database documentation page for more information.
  * **Connection Pool Timeout** : The number of seconds a query will wait before timing out because of a full connection pool.
  * **Additional JDBC parameters** : Any additional JDBC driver parameters.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Feature support
For Looker to support some features, your database dialect must also support them.
Google Spanner supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables  
Persistent native derived tables  
Stable views  
Query killing | Yes  
SQL-based pivots  
Timezones | Yes  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table  
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
Milliseconds  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
## References
  * Documented Spanner limits
  * Google Spanner IAM documentation


## Next steps
After you have connected your database to Looker, configure sign-in options for your users.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


