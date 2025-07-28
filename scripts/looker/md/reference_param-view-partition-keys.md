# partition_keys  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-partition-keys

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialect support for partition_keys




Was this helpful?
Send feedback 
#  partition_keys
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialect support for partition_keys


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: view_name {
  derived_table: {
    partition_keys: [ "created_date" ]
    ...
  }
}

```

Hierarchy `partition_keys` - or - `partition_keys` |  Default Value `None`Accepts One or more partitioned column namesSpecial Rules `partition_keys` is supported only on specific dialects  
---|---  
## Definition
The `partition_keys` parameter supports database dialects that have the ability to partition columns. When a query is run that is filtered on a partitioned column, the database will scan only those partitions that include the filtered data, rather than scanning the entire table. Because a smaller subsection of the table is being scanned, this can significantly reduce the time and cost of querying large tables when the appropriate partition and filter are specified.
> The `partition_keys` parameter works only with tables that are persistent, such as PDTs and aggregate tables. `partition_keys` is not supported for derived tables without a persistence strategy.
> In addition, the `partition_keys` parameter is not supported for derived tables that are defined using `create_process` or `sql_create`.
When you create a persistent derived table (PDT) or an aggregate table, if your underlying database table uses partitioning, Looker can use that partitioning.
> See the Dialect support for `partition_keys` section for the list of dialects that support `partition_keys`.
To add a partitioned column to a PDT or an aggregate table, use `partition_keys` and supply the names of the corresponding columns that are partitioned in the database table.
## Examples
Create a `customer_day_facts` PDT on a BigQuery database with a partition key on the `date` column:
```
view: customer_order_facts {
  derived_table: {
    explore_source: order {
      column: customer_id { field: order.customer_id }
      column: date { field: order.order_time }
      derived_column: num_orders {
        sql: COUNT(order.customer_id) ;;
      }
    }
    partition_keys: [ "date" ]
    datagroup_trigger: daily_datagroup
  }
}

```

Create a `customer_day_facts` SQL-based derived table on a Presto database with partition keys on the `date` and `state` columns:
```
view: customer_day_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        DATE(order_time) AS date,
        COUNT(*) AS num_orders
      FROM
        order
      GROUP BY
        customer_id ;;
    partition_keys: [ "date", "state" ]
    datagroup_trigger: daily_datagroup
  }
}

```

## Dialect support for `partition_keys`
The ability to use `partition_keys` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `partition_keys`:
> In BigQuery, partitioning can be used on only one table column, which must be a date/time column — so a Looker PDT based on a BigQuery table can use partitioning on only one date/time column.
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
Databricks | Yes  
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


