# case_sensitive (for models)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-case-sensitive

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * case_sensitive is not supported by some SQL dialects
  * Things to know
    * You can create a case-sensitive search in MySQL




Was this helpful?
Send feedback 
#  case_sensitive (for models)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * case_sensitive is not supported by some SQL dialects
  * Things to know
    * You can create a case-sensitive search in MySQL


> This page refers to the `case_sensitive` parameter that is part of a model.
> `case_sensitive` can also be used as part of an Explore, described on the `case_sensitive` (for Explores) documentation page.
> `case_sensitive` can also be used as part of a dimension or filter field, described on the `case_sensitive` (for fields) documentation page.
## Usage
```
case_sensitive: yes

```

Hierarchy `case_sensitive` |  Default Value `yes`, if the database dialect supports the parameterAccepts A Boolean (`yes` or `no`)   
---|---  
## Definition
`case_sensitive` determines whether filters will be treated as case-sensitive for a given model. All filters related to the model are impacted, including those added in the Explore UI, the Dashboard UI, a filter field, or a measure's `filters` parameter.
`case_sensitive` works by adjusting the `WHERE` clause of the SQL that Looker generates. When `case_sensitive: yes`, filters are expressed with `=` or `LIKE`, such as:
```
WHEREname='bob'
WHEREnameLIKE'%bob%'

```

When `case_sensitive: no`, filters are expressed with `ILIKE` (or equivalent), such as:
```
WHEREnameILIKE'bob'

```

Most SQL dialects support `case_sensitive`. However, if your SQL dialect doesn't support the `case_sensitive` parameter, case sensitivity will vary according to your database setup, which will _usually_ not be case-sensitive. Dialect support is listed in `case_sensitive` is not supported by some SQL dialects.
## Examples
Make all filters case-sensitive for a model:
```
connection: "connection_name"
include: "filename_or_pattern"
case_sensitive: yes
explore: explore_name {...}

```

Make all filters not case-sensitive for a model:
```
connection: "connection_name"
include: "filename_or_pattern"
case_sensitive: no

```

## Common challenges
###  `case_sensitive` is not supported by some SQL dialects
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
DataVirtuality provides a semantic data layer connecting to various database dialects. If Looker supports `case_sensitive` for the underlying dialects, then Looker supports `case_sensitive` for DataVirtuality connecting to those dialects.
## Things to know
### You can create a case-sensitive search in MySQL
It is possible to create a case-sensitive search in MySQL without using the `case_sensitive` parameter. In MySQL, certain data types, called binary strings, store text as a series of numbers. The capitalization of the text makes a difference in the numbers that are used. Therefore, if you convert your text to a binary string, you can make searches that are case-sensitive. For example:
```
dimension: will_NOT_be_case_sensitive {
  sql: ${TABLE}.something ;;
}
dimension: will_be_case_sensitive {
  sql: CAST(${TABLE}.something AS BINARY) ;;
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


