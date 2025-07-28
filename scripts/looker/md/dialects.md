# Looker dialects  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/dialects

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Support levels and JDBC installation
  * Database configuration instructions




Was this helpful?
Send feedback 
#  Looker dialects
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Support levels and JDBC installation
  * Database configuration instructions


Looker supports a wide range of SQL database dialects and continues to improve the feature implementations for existing dialect options as well as add new dialects. Because our modeling layer, LookML, builds on top of the in-database features available, some dialects allow for a more powerful implementation than others.
## Support levels and JDBC installation
Looker has two support levels for dialects based on a dialect's built-in feature set and the level of demand by Looker users:
  * **Supported** : A dialect that is fully supported by Looker. Looker is committed to improving this dialect implementation and will fix issues based on severity and demand. Looker runs exhaustive tests against this dialect at least weekly to ensure quality.
  * **Integration** : A dialect that is partially supported. Looker is able to connect to this dialect, but there are no commitments to improve implementation, fix issues, or regularly run tests against the dialect.


For the dialects whose value of **JDBC Driver Included?** is **No** , the needed JDBC JAR file is not bundled with the Looker JAR files. For customer-hosted installations of Looker, you must configure the driver for use with Looker as described on the Unpackaged JDBC drivers documentation page.
Looker (original) supports the following SQL dialects as of Looker 25.10:
Dialect | Support Level | JDBC Driver Included?  
---|---|---  
Actian Avalanche | Supported  
Amazon Athena | Supported | Yes  
Amazon Aurora MySQL | Supported | Yes  
Amazon Redshift | Supported | Yes  
Amazon Redshift 2.1+ | Supported | Yes  
Amazon Redshift Serverless 2.1+ | Supported | Yes  
Apache Druid | Supported | Yes  
Apache Druid 0.13+ | Supported | Yes  
Apache Druid 0.18+ | Supported | Yes  
Apache Hive 2.3+ | Integration | Yes  
Apache Hive 3.1.2+ | Supported | Yes  
Apache Spark 3+ | Supported | Yes  
ClickHouse | Supported | Yes  
Cloudera Impala 3.1+ | Supported | Yes  
Cloudera Impala 3.1+ with Native Driver | Supported  
Cloudera Impala with Native Driver | Supported  
DataVirtuality | Supported  
Databricks | Supported | Yes  
Denodo 7 | Supported | Yes  
Denodo 8 | Supported | Yes  
Dremio | Supported | Yes  
Dremio 11+ | Supported | Yes  
Exasol | Supported | Yes  
Firebolt | Supported | Yes  
Google BigQuery Legacy SQL | Supported | Yes  
Google BigQuery Standard SQL | Supported | Yes  
Google Cloud PostgreSQL | Supported | Yes  
Google Cloud SQL | Supported | Yes  
Google Spanner | Supported | Yes  
Greenplum | Supported | Yes  
HyperSQL | Integration | Yes  
IBM Netezza | Supported | Yes  
MariaDB | Supported | Yes  
Microsoft Azure PostgreSQL | Supported | Yes  
Microsoft Azure SQL Database | Supported | Yes  
Microsoft Azure Synapse Analytics | Supported | Yes  
Microsoft SQL Server 2008+ | Integration | Yes  
Microsoft SQL Server 2012+ | Integration | Yes  
Microsoft SQL Server 2016 | Supported | Yes  
Microsoft SQL Server 2017+ | Supported | Yes  
MongoBI | Supported  
MySQL | Supported | Yes  
MySQL 8.0.12+ | Supported | Yes  
Oracle | Supported | Yes  
Oracle ADWC | Integration | Yes  
PostgreSQL 9.5+ | Supported | Yes  
PostgreSQL pre-9.5 | Integration | Yes  
PrestoDB | Supported | Yes  
PrestoSQL | Supported | Yes  
SAP HANA | Supported | Yes  
SAP HANA 2+ | Supported | Yes  
SingleStore | Supported | Yes  
SingleStore 7+ | Supported | Yes  
Snowflake | Supported | Yes  
Teradata | Supported  
Trino | Supported | Yes  
Vector | Supported  
Vertica | Supported | Yes  
## Database configuration instructions
Instructions are available for these SQL dialects:
  * AlloyDB for PostgreSQL
  * Amazon Aurora MySQL
  * Amazon Aurora PostgreSQL
  * Amazon RDS for MySQL
  * Amazon RDS for PostgreSQL
  * Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+
  * Apache Hive 2.3+ and 3.1.2+

| 
  * Denodo 7 and Denodo 8
  * Google BigQuery Legacy SQL
  * Google BigQuery Standard SQL
  * Google Cloud SQL for PostgreSQL
  * Google Cloud SQL for MySQL
  * Microsoft Azure Synapse Analytics
  * Microsoft Azure SQL Database
  * Microsoft Azure PostgreSQL
  * Microsoft SQL Server (MSSQL)

| 
  * MongoDB Connector for BI
  * SingleStore (Formerly MemSQL)

  
---|---|---  
Looker does not support new connections for the following dialects. Existing connections will continue to function as expected. For Looker instances with existing connections to these dialects, the following links to documentation are provided for reference:


Looker also connects with the following dialects. Reach out to your Looker contact for assistance.
  * IBM Netezza


## Next steps
After you configure your database to work with Looker, you're ready to connect Looker to your database.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


