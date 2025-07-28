# allow_approximate_optimization  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-allow-approximate-optimization

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Dialect support for distinct counts with aggregate awareness




Send feedback 
#  allow_approximate_optimization
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * Dialect support for distinct counts with aggregate awareness


## Usage
```
view: view_name {
  measure: field_name {
    allow_approximate_optimization: yes 
  }
}

```

Hierarchy `allow_approximate_optimization` |  Possible Field Types MeasureDefault Value `no`Accepts A Boolean (yes or no)  
---|---  
## Definition
For dialects that support HyperLogLog sketches, Looker can leverage the HyperLogLog algorithm to approximate distinct counts for aggregate tables.
The `allow_approximate_optimization: yes` statement enables Looker to store HyperLogLog sketches in aggregate tables, which means that Looker can use approximations for distinct counts for aggregate awareness.
See the Dialect support for distinct counts with aggregate awareness section on this page for the list of dialects that support distinct counts for aggregate tables using HyperLogLog sketches.
In general, distinct counts can't be supported with aggregate awareness because you can't get accurate data if you try to aggregate distinct counts. For example, if you are counting the distinct users on a website, there may be a user who came to the website twice, three weeks apart. If you tried to apply a weekly aggregate table to get a monthly count of distinct users on your website, that user would be counted twice in your monthly distinct count query, and the data would be incorrect.
One workaround for this is to create an aggregate table that exactly matches an Explore query, as described on the Aggregate awareness documentation page. When the Explore query and an aggregate table query are the same, distinct count measures do provide accurate data, so they can be used for aggregate awareness.
The other option is to use approximations for distinct counts. The HyperLogLog algorithm is known to have about a 2% potential error. The `allow_approximate_optimization` parameter requires your Looker developers to acknowledge that it's okay to use approximate data for the measure so that the measure may be calculated approximately from aggregate tables.
With aggregate awareness, there are two cases where distinct counts come into play:
  * The first case is with measures of `type: count_distinct`.
  * The second case is with measures of `type: count` that are actually being rendered by Looker as `count_distinct` measure types. As discussed on the Aggregate awareness documentation page, Looker renders `count` measures as `count_distinct` to avoid fanout miscalculations in Explores that join multiple database tables.


In both of these cases, if your dialect supports HyperLogLog sketches, you can add the `allow_approximate_optimization: yes` statement to measures to enable approximate values. You can then include these measures in aggregate tables.
> Even for measures defined with `allow_approximate_optimization: yes`, Looker will return exact data when possible. For example, if the dimensions in an Explore query are a perfect match of the dimensions in an aggregate table, Looker can provide exact data for distinct counts, without having to approximate. In this case, you will see in the Explore's SQL tab that distinct count measures are being used for aggregate awareness without employing the HyperLogLog algorithm.
## Example
The `apx_unique_count` measure shown in this example is set for `allow_approximate_optimization: yes`, which means that the measure can be used in an `aggregate_table`.
```
measure: apx_unique_count {
  type: count_distinct
    allow_approximate_optimization: yes   # default value is no
  sql: ${id} ;;
}

```

## Dialect support for distinct counts with aggregate awareness
Looker can use distinct counts for aggregate awareness with database dialects that support HyperLogLog sketches. In the latest release of Looker, the following SQL dialects are supported for distinct counts with aggregate awareness:
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
Snowflake | Yes  
Teradata  
Trino | Yes  
Vector  
Vertica  
> Check your SQL dialect's documentation to understand the speed and accuracy tradeoffs of this method.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


