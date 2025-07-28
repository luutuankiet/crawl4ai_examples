# Database connection pooling  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-connection-pooling

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialect support for database connection pooling




Was this helpful?
Send feedback 
#  Database connection pooling
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialect support for database connection pooling


Connection pooling enables the use of preconfigured connection pools on PostgreSQL and Snowflake database dialects.
If your dialect supports it, database connection pooling enables Looker to use pools of connections through the JDBC driver. Database connection pooling enables faster query performance; a new query does not need to create a new database connection but can instead use an existing connection from the connection pool. The connection pooling capability ensures that a connection is cleaned up after a query execution and is available for reuse after the query execution ends.
You can enable connection pooling using the **Database Connection Pooling** option when you create or edit a database connection in Looker.
Looker will use connection pooling on your connection if all of the following are true:
  * You are using one of the dialects that support database connection pooling.
  * The **Database Connection Pooling** option is enabled on the Looker connection.
  * You have configured connection pools on your database.


Here are some things to consider when you're using connection pools:
  * Multiple users share a connection pool if their user attribute values are identical. Users who have unique or differing values in their set of user attributes will use unique connection pools when connecting to the database.
  * The maximum number of connections that can be made to connection pools across all database nodes is limited by the value in the **Max connections per node** field in the database's **Connection** page.
  * If the number of concurrent queries being issued to a connection pool exceeds the maximum number of connections, queries are queued in Looker until prior queries are executed.
  * Unique JDBC connection strings create unique connection pools. For example, unique database usernames or database group names that dictate role-based access control to the database will create unique JDBC connection strings, which then create unique connection pools. For example, a finance group in a company may have a database role that grants them access to all tables in the database, but the sales and marketing team may have a database role that grants them access to only a subset of the database tables. In this case, each group would have a unique JDBC connection string and a unique connection pool. A third group might be a set of embedded analytics customers who have their own access rights to the database. The embedded analytics customers would also have a unique JDBC string and a unique connection pool, so they would also have a unique set of connections that are not in use by the finance or sales and marketing groups.
  * The `WHERE` clause in a SQL query does not cause new connection pools. The `WHERE` clause has no impact on the JDBC connection string, so a new connection pool is not created. For example, unique access filters modify the SQL `WHERE` clause in a query, not the JDBC connection string, so unique access filters won't create new connection pools.
  * When multiple connection pools are created, the maximum number of connections is fragmented into multiple pools, with each pool containing a subset of available connections. This occurs because the total number of connections cannot exceed the maximum connections value.


## Dialect support for database connection pooling
The ability to use database connection pooling depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support database connection pooling:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena  
Amazon Aurora MySQL  
Amazon Redshift  
Amazon Redshift 2.1+  
Amazon Redshift Serverless 2.1+  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+  
Apache Hive 3.1.2+  
Apache Spark 3+  
ClickHouse  
Cloudera Impala 3.1+  
Cloudera Impala 3.1+ with Native Driver  
Cloudera Impala with Native Driver  
DataVirtuality  
Databricks  
Denodo 7  
Denodo 8  
Dremio  
Dremio 11+  
Exasol  
Firebolt  
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL  
Google Spanner  
Greenplum | Yes  
HyperSQL  
IBM Netezza  
MariaDB  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database  
Microsoft Azure Synapse Analytics  
Microsoft SQL Server 2008+  
Microsoft SQL Server 2012+  
Microsoft SQL Server 2016  
Microsoft SQL Server 2017+  
MongoBI  
MySQL  
MySQL 8.0.12+  
Oracle  
Oracle ADWC  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB  
PrestoSQL  
SAP HANA  
SAP HANA 2+  
SingleStore  
SingleStore 7+  
Snowflake | Yes  
Teradata  
Trino  
Vector  
Vertica  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


