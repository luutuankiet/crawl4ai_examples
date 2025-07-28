# Denodo 7 and Denodo 8  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-denodo

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Configuring Denodo 7 or Denodo 8 for Looker
    * Import a custom function
    * Grant the database user appropriate permissions
  * Creating the Looker connection to your database
  * Feature support




Was this helpful?
Send feedback 
#  Denodo 7 and Denodo 8
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Configuring Denodo 7 or Denodo 8 for Looker
    * Import a custom function
    * Grant the database user appropriate permissions
  * Creating the Looker connection to your database
  * Feature support


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Configuring Denodo 7 or Denodo 8 for Looker
Preparing Denodo 7 or Denodo 8 for Looker requires a few steps:
### Import a custom function
To support symmetric aggregates, a custom function (BASE64_TO_BASE10) has to be added to the Denodo VDP Server. For instructions, see Denodo's Knowledge Base article on Connecting Looker to Denodo.
### Grant the database user appropriate permissions
Looker will require `SELECT` access to any tables or databases that you would like to query with Looker. Ensure that the database user account that you are using to connect to Looker can access these tables.
## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (You may have to click the back arrow if the **Explore** or **Develop** menu is displayed.)
  2. In the **Admin** menu, select **Connections** , and then click **Add Connection**.
  3. Select **Denodo 7** or **Denodo 8** from the **Dialect** drop-down menu.
  4. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  5. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  6. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
### Denodo 7
Denodo 7 supports the following features as of Looker 25.10:
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
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes | Yes  
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
Milliseconds  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
### Denodo 8
Denodo 8 supports the following features as of Looker 25.10:
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
Timezones  
SSL | Yes  
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes | Yes  
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
Milliseconds  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


