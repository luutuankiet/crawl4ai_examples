# symmetric_aggregates  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to consider
    * Create joins carefully when symmetric aggregates are off
    * Not all database dialects support median and percentile measure types with symmetric aggregates
  * Dialect support for symmetric aggregates




Was this helpful?
Send feedback 
#  symmetric_aggregates
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to consider
    * Create joins carefully when symmetric aggregates are off
    * Not all database dialects support median and percentile measure types with symmetric aggregates
  * Dialect support for symmetric aggregates


## Usage
See more code actions.
Light code theme
Dark code theme
```
explore: explore_name {
  symmetric_aggregates: yes
}

```

Hierarchy `symmetric_aggregates` |  Default Value `yes`Accepts A Boolean (`yes` or `no`)   
---|---  
## Definition
The `symmetric_aggregates` parameter determines whether or not symmetric aggregates will be applied within a given Explore. When `symmetric_aggregates` is on, aggregate functions return correct results, even when joins result in a fanout. Symmetric aggregates are described in more detail on the Understanding symmetric aggregates Best Practices page, and the fanout problem they solve is explained in The problem of SQL fanouts Community post.
By default, symmetric aggregates are turned on for every Explore within Looker. This means that if your SQL dialect supports symmetric aggregates, you need to include the `symmetric_aggregates` parameter only if you'd like to disable that functionality for an Explore.
## Examples
Turn on symmetric aggregates for the `product` Explore:
```
explore: product {
  symmetric_aggregates: yes  # the default value, could be excluded
}

```

Turn off symmetric aggregates for the `customer` Explore:
```
explore: customer {
  symmetric_aggregates: no
}

```

## Things to consider
### Create joins carefully when symmetric aggregates are off
Symmetric aggregates protect certain calculations from giving incorrect results when a join results in a fanout. Therefore, if your dialect does not support symmetric aggregates, or if you choose to turn them off, you will need to be careful when you execute joins in Looker. This problem and the workarounds for it are described in great detail in the Community post The problem of SQL fanouts.
### Not all database dialects support median and percentile measure types with symmetric aggregates
When symmetric aggregates are enabled, Looker automatically converts the `percentile` and `median` measure types to `percentile_distinct` and `median_distinct` when a join involves a fanout. Not all database dialects that support symmetric aggregates support the `percentile_distinct` and `median_distinct` measure types. You can see whether your database dialect supports the `percentile_distinct` and `median_distinct` measure types on the Measure types documentation page.
If you receive an error similar to `SQL dialect doesn't support Symmetric Aggregates with percentiles, field ignored.`, this indicates that your database dialect does not support the `percentile_distinct` and `median_distinct` measure types. To work around this, change the measure type to `type: number` and then specify the aggregate function with `sql: median(${dimension})`. This disables symmetric aggregates, however.
## Dialect support for symmetric aggregates
The ability to use symmetric aggregates depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support aggregate awareness:
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
Apache Hive 2.3+  
Apache Hive 3.1.2+  
Apache Spark 3+ | Yes  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio  
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
MongoBI  
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


