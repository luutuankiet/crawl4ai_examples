# distribution_style  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-distribution-style

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialect support for distribution_style




Was this helpful?
Send feedback 
#  distribution_style
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialect support for distribution_style


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: my_view {
  derived_table: {
    distribution_style: all
    ...
  }
}

```

Hierarchy `distribution_style` - or - `distribution_style` |  Default Value NoneAccepts A distribution style (`all` or `even`) Special Rules `distribution_style` is supported only on specific dialects  
---|---  
## Definition
`distribution_style` lets you specify how the query for a persistent derived table (PDT) or an aggregate table is distributed across the nodes in a database.
> See the Dialect support for `distribution_style` section for the list of dialects that support `distribution_style`.
> The `distribution_style` parameter works only with tables that are persistent, such as PDTs and aggregate tables. `distribution_style` is not supported for derived tables without a persistence strategy.
> In addition, the `distribution_style` parameter is not supported for derived tables that are defined using `create_process` or `sql_create`.
> Lastly, `distribution_style` and `distribution` should not be used at the same time. If you want to distribute the rows of a table to different Redshift nodes based on a column value, use `distribution`. Otherwise, use `distribution_style` to choose a different distribution strategy.
Redshift offers four distribution styles, which are described in the Amazon Redshift documentation on distribution styles:
  * **ALL Distribution:** All rows are fully copied to each node. You can accomplish this type of distribution in Looker by using `distribution_style: all`.
  * **EVEN Distribution:** Rows are distributed to different nodes in a round-robin fashion. You can accomplish this type of distribution in Looker by using `distribution_style: even`.
  * **KEY Distribution:** Rows are distributed to different nodes based on unique values within a particular column. You can accomplish this type of distribution in Looker by using the `distribution` parameter.
  * **AUTO Distribution** Redshift assigns an optimal distribution style based on the size of the table data. Looker does not support this distribution type.


See the Amazon Redshift documentation on distribution styles for choosing the appropriate distribution strategy. If you don't specify a `distribution_style`, and don't use the `distribution` parameter instead, Looker will default to `all`.
## Examples
Create a `customer_order_facts` derived table with a distribution style of `all`:
```
view: customer_order_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        COUNT(*) AS lifetime_orders
      FROM
        order
      GROUP BY 1 ;;
    persist_for: "24 hours"
    distribution_style: all
  }
}

```

## Dialect support for `distribution_style`
The ability to use `distribution_style` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `distribution_style`:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena  
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


