# Admin settings - Queries  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-database-queries

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Basic query information
  * The Details button
  * Query timeouts and queueing




Was this helpful?
Send feedback 
#  Admin settings - Queries
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Basic query information
  * The Details button
  * Query timeouts and queueing


The **Queries** page in the **Database** section of the **Admin** menu lists information about the last 50 queries that Looker submitted to your database. For information about queries that are older than the most recent 50 queries, see the **Usage** section of Looker.
If you have enabled the Enhanced Query Admin Labs feature, the **Queries** page displays the following tabs:
  * **Recent** : Displays queries that were run in the last hour. From this tab, Looker admins can cancel running queries.
  * **Complete** : Displays the most recent 500 queries.


If you haven't enabled the **Enhanced Query Admin** Labs feature, the **Queries** page lists the last 50 queries on a single page.
## Basic query information
Column | Definition  
---|---  
Time | The start time of the query, displayed in your application time zone.  
Status | The status of the query, which can include: 
  * **Cache** : Looker returned the results from its cache instead of running a duplicate query against the database.
  * **Complete** : The query was completed successfully.
  * **Error** : The query wasn't completed successfully because an error occurred, the details of which can be found by clicking the Details button.
  * **Cancelled** : The query was cancelled by Looker or the user.
  * **Waiting for PDT** : The query needs to wait for a persistent derived table to be built before it can be executed.
  * **Building PDT** : A persistent derived table is in the process of being built.
  * **Queued** : The query is waiting to be executed because too many queries are already in progress (queries can be limited by Looker in your connection setup or your database).
  * **Running** : The query is in the process of being run.
  * **Unknown** : Looker wasn't able to determine what happened with this query.

  
Connection | The Looker connection under which this query was run.  
User | The user who ran this query, if that can be determined. Some queries are not executed by a specific user, such as when Looker creates a persistent derived table or when an unknown user accesses a public Look.  
Source | The source of the query in Looker, such as the Explore page or SQL Runner. If possible, a link to the saved Look, or the query ID along with the name of the model and Explore, is also displayed. Some queries don't have additional information, such as those that are run in SQL Runner. Queries that are issued from the Open SQL Interface have a **Source** value of `Sql_interface`.  
Runtime | The time it took to run the query. This includes the construction of the query, any time the query spent in the queue, transit to and from the database, and database execution of the query.  
Details Button | See The Details Button subsection on this page for additional details.  
## The Details button
Clicking the **Details** button to the right of any query will bring up additional information about that query. The **Query Details** menu includes the following:
  * An **Info** section that includes details about the query (see the following table).
  * A **SQL** section that shows the raw SQL that was executed against the database. **Context Comments** will not appear in the **Query Details** information. To prevent comments from affecting query caching, Looker adds the context comments to outgoing SQL commands right before the SQL is sent to the database.
  * A **SQL Interface query** section that appears when a query has been issued through the Open SQL Interface. This section displays the SQL query that was sent to Looker from the external BI tool and can aid in troubleshooting and reproducing issues.
  * An **Open in SQL Runner** link that will open the query in SQL Runner.


The **Info** section includes the following information:
Section | Definition  
---|---  
History ID | The history ID of the query, if available.  
Status | The status of the query, as described in the basic query information table.  
Message | If the query contains a PDT, the PDT generation comment appears in this field. If the query does not contain a PDT, the field does not appear.  
Connection | The Looker connection under which this query was run.  
User | The user who ran this query, if that can be determined. Some queries are not executed by a specific user, such as when Looker creates a persistent derived table or when an unknown user accesses a public Look.  
Source | The source of the query in Looker, such as the **Explore** page or SQL Runner. If possible, additional information is displayed, such as a link to the saved Look, the query ID, model name, Explore name, or the fields that were selected.  
Start Time | The start time of the query, displayed in your application time zone.  
End Time | The finish time of the query, displayed in your application time zone.  
Runtime | The length of time it took to run the query.  
## Query killing
When you close the browser tab in which a query is running, Looker will automatically stop the query. Looker admins can also stop a running query from the **Queries** page. (Users with the `see_queries` permission can view the **Queries** page, but only Looker admins can stop a running query.) Any query that is still running shows a **Stop** button to the right of the query. Click **Stop** to stop the query.
For Looker to kill queries, your database dialect must support query killing. The following list shows which dialects support query killing in the latest release of Looker:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | Yes  
Greenplum | Yes  
HyperSQL  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
## Query timeouts and queueing
Looker kills queries that have been waiting in queue for too long. This operation is called a _timeout_. Several timeouts may apply to your query:
  * **Connection pool timeout and maximum concurrent queries** : To prevent overloading of your database with concurrent queries, Looker holds excess concurrent queries in the Looker query queue, and will kill queries that remain in queue for too long. By default, 75 maximum concurrent queries are allowed per connection. Additional queries beyond the connection limit will be timed out after 0 seconds. To change these defaults, configure the Max connections, **Max concurrent queries for this connection**, and **Connection pool timeout** settings on a connection's **Connections Settings** page.
  * **Per-user query limit and timeout** : To prevent any single user from filling up the Looker query queue, each user has a maximum number of allowed concurrent queries and a corresponding queue timeout. By default, each user can run a maximum of 15 concurrent queries, and the timeout is 600 seconds for queries that are queued because of this limit. These settings apply to both users who log in to Looker using the regular authentication process, and to users who log in using API user credentials. To change these defaults, configure the Max concurrent queries per user for this connection settings on a connection's **Connections Settings** page. If your Looker instance is customer-hosted, you can change these defaults by configuring the `--per-user-query-limit` and `--per-user-query-timeout` startup options.
  * **Scheduler query limit and timeout** : To prevent overloading of the Looker scheduler process, a Looker instance can run a maximum of 10 concurrent scheduled queries, and the timeout for queries in the scheduler queue is 1,200 seconds. If your Looker instance is customer-hosted, you can change these defaults by configuring the `--scheduler-query-limit` and `--scheduler-query-timeout` startup options.
  * **Renderer query limit and timeout** : To prevent overloading of the Looker renderer process, a Looker instance can render a maximum of 2 concurrent image-based downloads, such as PDF and PNG formats. If your Looker instance is customer-hosted, you can change this default by configuring the `--concurrent-render-jobs` startup option.


* **Webhook timeout** : Looker will attempt data delivery to a webhook for a maximum of 30 minutes. If Looker cannot communicate with the webhook destination in 30 minutes, the query will time out. This timeout is not configurable.
  * **Proxy timeout** : Customer-hosted instances often use proxies with a default timeout of 60 seconds. We recommend that this timeout be increased to 60 minutes. See the Running Looker behind a proxy server or load balancer Looker Community post for more information.
  * **Database timeout** : Most databases have rules for queueing and timeouts that are independent of Looker's queues and timeouts. For example, a query may have left the Looker queue, but it can still be queued on your database. Check the documentation for your database for more information on customizing database query timeouts.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


