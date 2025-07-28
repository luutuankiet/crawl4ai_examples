# Apache Druid  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-apache-druid

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Configuring your Apache Druid cluster
    * Turning off COUNT DISTINCT approximation (optional)
  * Creating the Looker connection to your database
  * Feature support
    * Apache Druid 0.13+ (Apache Druide 0.13.x - 0.17.x)
    * Apache Druid 0.18+




Was this helpful?
Send feedback 
#  Apache Druid
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Configuring your Apache Druid cluster
    * Turning off COUNT DISTINCT approximation (optional)
  * Creating the Looker connection to your database
  * Feature support
    * Apache Druid 0.13+ (Apache Druide 0.13.x - 0.17.x)
    * Apache Druid 0.18+


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Configuring your Apache Druid cluster
`<DRUID_BASE_DIR>` refers to the base directory in which the Apache Druid cluster is installed on a server.
### Enabling SQL
To enable SQL on your Druid database, add this line to the `broker/runtime.properties` configuration file:
`<DRUID_BASE_DIR>/conf/druid/broker/runtime.properties`
```
druid.sql.enable=true

```

### Turning off `COUNT DISTINCT` approximation (optional)
By default, Druid approximates `COUNT DISTINCT`. For precise results, add this line to the `broker/runtime.properties` configuration file:
`<DRUID_BASE_DIR>/conf/druid/broker/runtime.properties`
```
`druid.sql.planner.useApproximateCountDistinct=false`

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Name** : The name of the connection.
  * **Dialect** : **Apache Druid** , **Apache Druid 0.13+** (Apache Druide 0.13.x - 0.17.x), or **Apache Druid 0.18+**.
  * **Host** : DNS or IP address of the cluster Broker. You can find this in your `broker/runtime.properties` file.
  * **Port** : The port of the Broker. The default port is 8082. If your cluster is secured by SSL, the default port is 8182.
  * **Database** : The name of your database. The default is `druid`.
  * **Username** : The database username if your Apache Druid cluster is configured to use Druid Basic Security. If it is not, then you can specify any string.
  * **Password** : The user password. If your cluster is not configured to use Druid Basic Security, then you can specify any string.
  * **Schema** : The default schema to use when there is no schema specified. Entering a schema is optional. 
  * **Additional JDBC parameters** : Semicolon delimited Avatica JDBC parameters.
    * These properties can be set as connection properties: 
      * `useApproximateCountDistinct`
      * `useApproximateTopN`
      * `useFallback`
      * `sqlTimeZone`
Example: `none   useApproximateCountDistinct=false;truststore=/path/to/truststore.jks;truststore_password=changeit`
  * **Maintenance Schedule** : A `cron` expression that indicates when Looker should check datagroups and persistent derived tables. Read more about this setting in the Maintenance Schedule documentation.
  * **SSL** : Check if your Apache Druid cluster is configured to use Druid TLS.
  * **Verify SSL** : Check to enforce strict hostname verification.
  * **Max connections per node** : The default is 25. This setting can be left at the default value initially. See the Connecting Looker to your database documentation page for more information.
  * **Connection Pool Timeout** : The default is 120 seconds.
  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting in the SQL Runner Precache documentation.
  * **Database Time Zone** : Database timezone. Supported in Apache Druid 0.13+ and Apache Druid 0.18+.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
Looker runs a `SELECT 1` query to verify a basic connection and perform a query test. It does not validate that the catalog and schema combination exist or that the user has the required access to that schema.
If you have any issues, check out our Testing Connections documentation.
To save these settings, click **Connect**.
Test the connection in SQL Runner. Navigate to SQL Runner, select your connection and schema, then check if you can see your database tables.
## Feature support
For Looker to support some features, your database dialect must also support them.
### Apache Druid
Apache Druid supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates  
Derived tables | Yes  
Persistent SQL derived tables  
Persistent native derived tables  
Stable views  
Query killing  
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
SQL Runner Describe Table  
SQL Runner Show Indexes  
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
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
### Apache Druid 0.13+ (Apache Druide 0.13.x - 0.17.x)
Apache Druid 0.13+ supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates  
Derived tables | Yes  
Persistent SQL derived tables  
Persistent native derived tables  
Stable views  
Query killing  
SQL-based pivots  
Timezones | Yes  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table  
SQL Runner Show Indexes  
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
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
### Apache Druid 0.18+
Apache Druid 0.18+ supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates  
Derived tables | Yes  
Persistent SQL derived tables  
Persistent native derived tables  
Stable views  
Query killing  
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
SQL Explain | Yes  
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


