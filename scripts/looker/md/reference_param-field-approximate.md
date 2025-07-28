# approximate  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-approximate

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialect support for approximate




Was this helpful?
Send feedback 
#  approximate
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialect support for approximate


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: view_name {
  measure: field_name {
    approximate: yes 
  }
}

```

Hierarchy `approximate` |  Possible Field Types MeasureAccepts A Boolean (yes or no)  
---|---  
## Definition
> See the Dialect support for `approximate` section on this page for the list of dialects that support `indexes`.
The `approximate` parameter lets you use approximate counting with measures of `type: count` and `type: count_distinct`. With large datasets, approximate counts can be _much_ faster than exact counts and are typically within a few percent of the actual value. Please check your SQL dialect's documentation to understand the speed and accuracy tradeoffs of this method.
```
measure: apx_unique_count {
  type: count_distinct
  approximate: yes   # default value is no
  sql: ${id} ;;
}

```

-
Turning on `approximate` with a measure of `type: count` might seem unnecessary, because the approximate counting feature applies only to distinct counts. However, there are some situations when Looker automatically turns measures of `type: count` into a distinct count of a primary key to provide accurate results for joined views. In those situations, approximate counting may be useful.
## Dialect support for `approximate`
The ability to use `approximate` depends on the database dialect your Looker connection is using. In the latest version of Looker, the following dialects support `approximate`:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena | Yes  
Amazon Aurora MySQL  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+  
Apache Hive 3.1.2+  
Apache Spark 3+  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality  
Databricks  
Denodo 7  
Denodo 8  
Dremio  
Dremio 11+  
Exasol  
Firebolt  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL  
Google Cloud SQL  
Google Spanner  
Greenplum  
HyperSQL  
IBM Netezza  
MariaDB  
Microsoft Azure PostgreSQL  
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
PostgreSQL 9.5+  
PostgreSQL pre-9.5  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA  
SAP HANA 2+  
SingleStore  
SingleStore 7+  
Snowflake  
Teradata  
Trino | Yes  
Vector  
Vertica  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


