# case_sensitive (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-case-sensitive

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * case_sensitive is not supported by some SQL dialects




Was this helpful?
Send feedback 
#  case_sensitive (for fields)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * case_sensitive is not supported by some SQL dialects


> This page refers to the `case_sensitive` parameter that is part of a dimension or filter.
> `case_sensitive` can also be used as part of a model, described on the `case_sensitive` (for models) parameter documentation page.
> `case_sensitive` can also be used as part of an Explore, described on the `case_sensitive` (for Explores) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    case_sensitive:  no
  }
}

```

Hierarchy `case_sensitive` |  Possible Field Types Dimension, FilterAccepts A Boolean (yes or no)  
---|---  
## Definition
When a `dimension` or `filter` field is used as a filter, you can change its case-sensitivity by using the `case_sensitive` parameter. The `case_sensitive` parameter works with most dialects, although some dialects do not have the necessary SQL functions.
By default, `case_sensitivity` is on and filters are case-sensitive. However, some dialects do not support this parameter, as described in the `case_sensitive` is not supported by some SQL dialects section on this page.
## Examples
Stop filters on the `name` dimension from being case-sensitive:
```
dimension: name {
  sql: ${TABLE}.name ;;
  case_sensitive: no
}

```

## Common challenges
###  `case_sensitive` is not supported by some SQL dialects
By default, `case_sensitivity` is on and filters are case-sensitive. If your SQL dialect doesn't support the `case_sensitive` parameter, case sensitivity will vary according to your database setup, which will _usually_ not be case-sensitive.
For Looker to support `case_sensitive` in your Looker project, your database dialect must also support it. The following table shows which dialects support `case_sensitive` in the latest release of Looker:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL  
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
Google Cloud SQL  
Google Spanner | Yes  
Greenplum | Yes  
HyperSQL  
IBM Netezza | Yes  
MariaDB  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database  
Microsoft Azure Synapse Analytics  
Microsoft SQL Server 2008+  
Microsoft SQL Server 2012+  
Microsoft SQL Server 2016  
Microsoft SQL Server 2017+  
MongoBI | Yes  
MySQL  
MySQL 8.0.12+  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore  
SingleStore 7+  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


