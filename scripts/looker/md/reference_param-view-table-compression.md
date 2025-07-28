# table_compression  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-table-compression

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Dialect support for table_compression




Send feedback 
#  table_compression
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialect support for table_compression


## Usage
```
view: my_view {
  derived_table: {
    table_compression: GZIP
    ...
  }
}

```

Hierarchy `table_compression` |  Default Value `GZIP`Accepts `GZIP` or `SNAPPY`Special Rules `table_compression` is supported only on specific dialects  
---|---  
## Definition
The `table_compression` parameter specifies the compression that a persistent derived table (PDT) will have in an Athena database, either `GZIP` or `SNAPPY`.
See the Amazon Athena documentation for details.
> See the Dialect support for `table_compression` section for the list of dialects that support `table_compression`.
> The `table_compression` parameter works only with tables that are persistent, such as PDTs and aggregate tables. `table_compression` is not supported for derived tables without a persistence strategy.
## Examples
Create a `customer_order_facts` PDT on an Amazon Athena database with SNAPPY compression:
```
view: customer_order_facts {
  derived_table: {
    explore_source: order {
      column: customer_id { field: order.customer_id }
      column: date { field: order.order_time }
      column: city { field: users.city }
      column: age_tier { field: users.age_tier }
      derived_column: num_orders {
        sql: COUNT(order.customer_id) ;;
      }
    }
    table_format: ORC
    table_compression: SNAPPY
    datagroup_trigger: daily_datagroup
  }
}


```

## Dialect support for `table_compression`
The ability to use `table_compression` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `table_compression`:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena | Yes  
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
PrestoDB  
PrestoSQL  
SAP HANA  
SAP HANA 2+  
SingleStore  
SingleStore 7+  
Snowflake  
Teradata  
Trino  
Vector  
Vertica  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


