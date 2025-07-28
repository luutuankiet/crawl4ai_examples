# Dremio  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-dremio

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Dremio
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Creating the Looker connection to your database


The Looker dialect testing of Dremio runs against Dremio version 1.4.9 Enterprise Edition.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next. Use the default values in all the other fields, or leave them blank.
     * **Name** : Assign a unique name to the connection. The name is how LookML refers to this connection.
     * **Dialect** : Select **Dremio 11+** or **Dremio**.
     * **Host** : Enter the IP address or hostname of the server where Dremio is running.
     * **Port** : The default port is `31010`.
     * **Database** : The default value is `DREMIO`.
     * **Username** : Enter the username that Looker uses to access Dremio.
     * **Password** : Enter the password that is associated with the username that you entered.
  3. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
Looker will run `SELECT 1 FROM (VALUES(1))` to verify a basic connection and query test. It will not validate that the user can access any of the Dremio sources or underlying tables.
  4. To save these settings, click **Connect**.


## Debugging
Connect your web browser to `dremio_host:9047` on the server. From the SQL Editor, run `SELECT 1 FROM (VALUES(1))` to verify that Dremio is installed correctly and that queries are able to execute.
## Feature support
For Looker to support some features, your database dialect must also support them.
Dremio supports the following features as of Looker 25.10:
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
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Dremio 11+ supports the following features as of Looker 25.10:
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
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
## Next steps
After you have completed the database connection, configure authentication options.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


