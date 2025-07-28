# Apache Spark  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-apache-spark

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Creating the Looker connection to your database
  * Feature support
    * Apache Spark 3+




Was this helpful?
Send feedback 
#  Apache Spark
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Creating the Looker connection to your database
  * Feature support
    * Apache Spark 3+


This page contains information about connecting Looker to Apache Spark 3.
Looker connects to Apache Spark 3+ through a JDBC connection to the Spark Thrift Server.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Name** : The name of the connection. This is how the connection will be referred to in the LookML model.
  * **Dialect** : Select **Apache Spark 3+**.
  * **Host** : The Thrift server host.
  * **Port** The Thrift server port (10000 by default).
  * **Database** : The default schema/database that will be modeled. When no database is specified for a table, this will be assumed.
  * **Username** : The user that Looker will authenticate as.
  * **Password** : The optional password for Looker user.
  * **Enable PDTs** : Use this toggle to enable persistent derived tables. When PDTs are enabled, the **Connection** window reveals additional PDT settings and the **PDT Overrides** section.
  * **Temp Database** : A temporary schema/database for storing PDTs. It must be created beforehand, with a statement such as `CREATE SCHEMA looker_scratch;`.
  * **Additional JDBC parameters** : Add any additional Hive JDBC parameters here, such as: 
    * `;spark.sql.inMemoryColumnarStorage.compressed=true`
    * `;auth=noSasl`
  * **SSL** : Leave this unchecked.
  * **Database Time Zone** : The time zone of data stored in Spark. Usually it can be left blank or set to UTC.
  * **Query Time Zone** : The time zone to display data queried in Looker.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Feature support
For Looker to support some features, your database dialect must also support them.
### Apache Spark 3+
Apache Spark 3+ supports the following features as of Looker 25.10:
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
List type | Yes  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes  
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
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
## Next steps
After you have created the connection, set authentication options.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


