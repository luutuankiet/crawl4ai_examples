# SQL Runner basics  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-runner-basics

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Navigating to SQL Runner
  * Basic SQL Runner usage
  * SQL Runner visualizations
  * Supported database dialects for SQL Runner features




Was this helpful?
Send feedback 
#  SQL Runner basics
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Navigating to SQL Runner
  * Basic SQL Runner usage
  * SQL Runner visualizations
  * Supported database dialects for SQL Runner features


SQL Runner provides a way to directly access your database and to leverage that access in a variety of ways. Using SQL Runner, you can easily navigate the tables in your schema, use an ad hoc Explore from a SQL query, run prewritten descriptive queries on your data, see your SQL Runner history, download results, share queries, add to a LookML project as a derived table, and perform other useful tasks.
This page describes how to navigate to SQL Runner and shows which database dialects support SQL Runner features. See these other documentation pages for information on:
  * Using SQL Runner to create queries and Explores
  * Using SQL Runner to create derived tables
  * Managing database functions with SQL Runner


## Navigating to SQL Runner
If you have the permissions to see LookML and to use SQL Runner, you can navigate to SQL Runner in two ways:
  * In the **Develop** menu, select **SQL Runner**.


  * From an Explore, click **SQL** on the Data bar to see the SQL. Then click **Open in SQL Runner** to see the query in SQL Runner, or click **Explain in SQL Runner** to open SQL Runner and request the database's execution plan for the query.


## Basic SQL Runner usage
This section describes how to use SQL Runner to directly access tables in your schema, run a SQL query on your data, and see query results.
  1. Select the **Connection** that you want to query.
  2. Select the **Schema** that you want to query. For Google BigQuery connections, select the **Project** (if your BigQuery connection supports multiple databases) and the **Dataset**.
  3. Select a table to show its columns in the Results area.
  4. Optionally, select the ⊝ icon to collapse the left panel. If the panel is collapsed, select the ⊕ icon to expand the panel.
  5. Check the database SQL dialect used for the query. The dialect is displayed on the right side of the **Query** bar.
  6. Write a SQL command in the text box below the **Query** bar.
  7. Select **Run** to execute the SQL query.
  8. View the information that is returned by the database in the **Results** area.


## SQL Runner visualizations
If your Looker admin has enabled the **SQL Runner Vis** Labs feature, you can create visualizations directly in SQL Runner.
For more information, see the Using SQL Runner to create queries and Explores documentation page.
## Supported database dialects for SQL Runner features
For Looker to support SQL Runner features in your Looker project, your database dialect must also support them. The following tables show which dialects support each SQL Runner feature.
These dialects support SQL Runner Show Processes:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+  
Apache Hive 3.1.2+  
Apache Spark 3+  
ClickHouse | Yes  
Cloudera Impala 3.1+  
Cloudera Impala 3.1+ with Native Driver  
Cloudera Impala with Native Driver  
DataVirtuality  
Databricks  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio  
Dremio 11+  
Exasol  
Firebolt | Yes  
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL  
IBM Netezza  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics  
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
Snowflake  
Teradata  
Trino | Yes  
Vector  
Vertica | Yes  
These dialects support SQL Runner Describe Table:
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
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza  
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
These dialects support SQL Runner Show Indexes:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+ | Yes  
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
Firebolt | Yes  
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB  
PrestoSQL  
SAP HANA  
SAP HANA 2+  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake  
Teradata | Yes  
Trino  
Vector | Yes  
Vertica  
These dialects support SQL Runner Select 10:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
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
HyperSQL | Yes  
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
These dialects support SQL Runner Count:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
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
HyperSQL | Yes  
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
These dialects support SQL Explain:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality  
Databricks | Yes  
Denodo 7  
Denodo 8  
Dremio  
Dremio 11+  
Exasol  
Firebolt | Yes  
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+  
Microsoft SQL Server 2012+  
Microsoft SQL Server 2016  
Microsoft SQL Server 2017+  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle  
Oracle ADWC  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA  
SAP HANA 2+  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector  
Vertica | Yes  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


