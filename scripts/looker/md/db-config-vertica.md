# Vertica  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-vertica

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Database configuration
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Vertica
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Database configuration
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Database configuration
Before you create a connection to Vertica, create a new database user and schema that is exclusive for your Looker applications. The Looker user needs read and write permissions into a separate schema to store PDTs and read-only privileges to other schemas in the Vertica database. This is optional but recommended.
The following is an example of creating a user and schema for Looker:
```
CREATE USER looker Identified BY 'mypassword';
CREATE SCHEMA looker_scratch;
GRANT CREATE ON SCHEMA looker_scratch to looker;

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Name** : Give a name to the connection. This is how the LookML model will reference the connection.
  * **Dialect** : Select **Vertica** from the drop-down of dialects.
  * **Host** : Enter the Vertica server name or IP.
  * **Port** : The default is 5433.
  * **Database** : Enter Vertica's database name.
  * **Username and Password** : Enter the username and password of the user that will connect to Looker.
  * **Schema** : Enter the schema that contains the tables that you want to explore in Looker.
  * **Temp Database** : This is the scratch schema where you want Looker to create any temporal derived tables to improve performance. It is optional but recommended, and should be created beforehand.
  * **Max connections per node** : This setting can be left at the default value initially. See the Connecting Looker to your database documentation page for more information.
  * **Connection Pool Timeout** : This is optional. Use the default value.
  * **Database Time Zone** : The time zone your Vertica database uses to store dates and times. For example, UTC. This is optional.
  * **Query Time Zone** : The time zone you want your queries to display. For example, US Eastern (America – New York). This is optional.
  * **Additional JDBC parameters** : This is optional. Use this field to enable additional database settings. For example, to enable Vertica's native load balancing, use the JDBC connection parameter `ConnectionLoadBalance=1`. To assign a label to identify Looker's sessions, use the JDBC connection parameter `Label=<mylabel>`. You can pass several parameters one after the other using , as shown on this page. For a complete list of available JDBC connection parameters, see Vertica's documentation.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Feature support
For Looker to support some features, your database dialect must also support them.
Vertica supports the following features as of Looker 25.10:
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
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
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
## Next steps
After you have completed the database connection, configure authentication options.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


