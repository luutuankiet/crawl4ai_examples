# Incremental PDTs  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/incremental-pdts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Defining an incremental PDT
  * Interaction of increment parameters and persistence strategy
  * Testing an incremental PDT in Development Mode
  * Troubleshooting incremental PDTs
    * Incremental PDT fails to build after schema change
  * Supported database dialects for incremental PDTs




Was this helpful?
Send feedback 
#  Incremental PDTs
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Defining an incremental PDT
  * Interaction of increment parameters and persistence strategy
  * Testing an incremental PDT in Development Mode
  * Troubleshooting incremental PDTs
    * Incremental PDT fails to build after schema change
  * Supported database dialects for incremental PDTs


In Looker, persistent derived tables (PDTs) are written to the scratch schema of your database. Looker persists and rebuilds a PDT based on its persistence strategy. When a PDT is triggered to rebuild, by default Looker rebuilds the entire table.
An incremental PDT is a PDT that Looker builds by appending fresh data to the table instead of rebuilding the table in its entirety:
If your dialect supports incremental PDTs, you can make the following types of PDTs into incremental PDTs:
  * LookML-based (native) PDTs
  * SQL-based PDTs


The first time you run a query on an incremental PDT, Looker builds the entire PDT to get the initial data. If the table is large, the initial build may take a significant amount of time, as would building any large table. Once the initial table is built, subsequent builds will be incremental and will take less time, if the incremental PDT is set up strategically.
Note the following for incremental PDTs:
  * Incremental PDTs are supported only for PDTs that use a trigger-based persistence strategy (`datagroup_trigger`, `sql_trigger_value`, or `interval_trigger`). Incremental PDTs are not supported for PDTs that use the `persist_for` persistence strategy.
  * For SQL-based PDTs, the table query must be defined using the `sql` parameter to be used as an incremental PDT. SQL-based PDTs that are defined with the `sql_create` parameter or the `create_process` parameter cannot be incrementally built. As you can see in Example 1 on this page, Looker uses an INSERT or a MERGE command to create the increments for an incremental PDT. The derived table cannot be defined using custom Data Definition Language (DDL) statements, since Looker wouldn't be able to determine which DDL statements would be required to create an accurate increment.
  * The incremental PDT's source table must be optimized for time-based queries. Specifically, the time-based column that is used for the increment key must have an optimization strategy, such as partitioning, sortkeys, indexes, or whatever optimization strategy is supported for your dialect. Source table optimization is strongly recommended because each time the incremental table is updated, Looker queries the source table to determine the latest values of the time-based column that is used for the increment key. If the source table is not optimized for these queries, Looker's query for the latest values may be slow and expensive.


## Defining an incremental PDT
You can use the following parameters to make a PDT into an incremental PDT:
  * `increment_key` (required to make the PDT an incremental PDT): Defines the time period for which new records should be queried.
  * `{% incrementcondition %}` Liquid filter (required to make a SQL-based PDT an incremental PDT; not applicable to LookML-based PDTs): Connects the increment key to the database time column that the increment key is based on. See the `increment_key` documentation page for more information.
  * `increment_offset` (optional): An integer that defines the number of previous time periods (at the increment key's granularity) that are rebuilt for each incremental build. The `increment_offset` parameter is useful in the case of late-arriving data, where previous time periods may have new data that wasn't included when the corresponding increment was originally built and appended to the PDT.


See the `increment_key` parameter documentation page for examples that show how to create incremental PDTs from persistent native derived tables, persistent SQL-based derived tables, and aggregate tables.
Here is a simple example of a view file that defines an incremental LookML-based PDT:
```
view: flights_lookml_incremental_pdt {
  derived_table: {
    indexes: ["id"]
    increment_key: "departure_date"
    increment_offset: 3
    datagroup_trigger: flights_default_datagroup
    distribution_style: all
    explore_source: flights {
      column: id {}
      column: carrier {}
      column: departure_date {}
    }
  }

  dimension: id {
    type: number
  }
  dimension: carrier {
    type: string
  }
   dimension: departure_date {
    type: date
  }
}

```

This table will build in its entirety the first time a query is run on it. After that, the PDT will be rebuilt in increments of one day (`increment_key: departure_date`), going back three days (`increment_offset: 3`).
The increment key is based on the `departure_date` dimension, which is actually the `date` timeframe from the `departure` dimension group. (See the `dimension_group` parameter documentation page for an overview of how dimension groups work.) The dimension group and timeframe are both defined in the `flights` view, which is the `explore_source` for this PDT. Here is how the `departure` dimension group is defined in the `flights` view file:
```
...
  dimension_group: departure {
    type: time
    timeframes: [
      raw,
      date,
      week,
      month,
      year
    ]
    sql: ${TABLE}.dep_time ;;
  }
...


```

## Interaction of increment parameters and persistence strategy
A PDT's `increment_key` and `increment_offset` settings are independent of the PDT's persistence strategy:
  * The incremental PDT's persistence strategy determines only when the PDT increments. The PDT builder doesn't modify the incremental PDT unless the table's persistence strategy is triggered, or unless the PDT is manually triggered with the **Rebuild Derived Tables & Run** option in an Explore.
  * When the PDT increments, the PDT builder will determine when the latest data was previously added to the table, in terms of the most current time increment (the time period that is defined by the `increment_key` parameter). Based on that, the PDT builder will truncate the data to the beginning of the most recent time increment in the table, then build the latest increment from there.
  * If the PDT has an `increment_offset` parameter, the PDT builder will also rebuild the number of previous time periods specified in the `increment_offset` parameter. The previous time periods go back starting from the beginning of the most current time increment (the time period that is defined by the `increment_key` parameter).


The following example scenarios illustrate how incremental PDTs are updated, by showing the interaction of `increment_key`, `increment_offset`, and persistence strategy.
### Example 1
This example uses a PDT with these properties:
  * **Increment key** : date
  * **Increment offset** : 3
  * **Persistence strategy** : triggered once a month on the first day of the month


Here is how this table will be updated:
  * A monthly persistence strategy means that the table is automatically built once a month. This means that on June 1st, for example, the last row in the table will have been added on May 1st.
  * Because this PDT has an increment key based on date, the PDT builder will truncate May 1st back to the beginning of the day and rebuild the data for May 1st and up to the current day, June 1st.
  * Additionally, this PDT has an increment offset of `3`. So the PDT builder also rebuilds the data from the previous three time periods (days) before May 1st. The result is that data is rebuilt for April 28th, 29th, 30th, and up to the present day of June 1st.


In SQL terms, here is the command that the PDT builder will run on June 1st to determine the rows from the existing PDT that should be rebuilt:
```
## Example SQL for BigQuery:
SELECT FORMAT_TIMESTAMP('%F %T',TIMESTAMP_ADD(MAX(pdt_name),INTERVAL -3 DAY))

## Example SQL for other dialects:
SELECT CAST(DATE_ADD(MAX(pdt_name),INTERVAL -3 DAY) AS CHAR)


```

And here is the SQL command that the PDT builder will run on June 1st to build the latest increment:
```
## Example SQL for BigQuery:

MERGE INTO [pdt_name] USING (SELECT [columns]
   WHERE created_at >= TIMESTAMP('4/28/21 12:00:00 AM'))
   AS tmp_name ON FALSE
WHEN NOT MATCHED BY SOURCE AND created_date >= TIMESTAMP('4/28/21 12:00:00 AM')
   THEN DELETE
WHEN NOT MATCHED THEN INSERT [columns]

## Example SQL for other dialects:

START TRANSACTION;
DELETE FROM [pdt_name]
   WHERE created_date >= TIMESTAMP('4/28/21 12:00:00 AM');
INSERT INTO [pdt_name]
   SELECT [columns]
   FROM [source_table]
   WHERE created_at >= TIMESTAMP('4/28/21 12:00:00 AM');
COMMIT;


```

### Example 2
This example uses a PDT with these properties:
  * **Persistence strategy** : triggered once a day
  * **Increment key** : month
  * **Increment offset** : 0


Here is how this table will be updated on June 1st:
  * The daily persistence strategy means that the table is automatically built once a day. On June 1st, the last row in the table will have been added on May 31st.
  * Because the increment key is based on the month, the PDT builder will truncate from May 31st back to the beginning of the month and rebuild the data for all of May and up to the current day, including June 1st.
  * Because this PDT has no increment offset, no previous time periods are rebuilt.


Here is how this table will be updated on June 2nd:
  * On June 2nd, the last row on the table will have been added on June 1st.
  * Because the PDT builder will truncate back to the beginning of the month of June, then rebuild the data starting with June 1st and up to the current day, the data is rebuilt for only June 1st and June 2nd.
  * Because this PDT has no increment offset, no previous time periods are rebuilt.


### Example 3
This example uses a PDT with these properties:
  * **Increment key** : month
  * **Increment offset** : 3
  * **Persistence strategy** : triggered once a day


> This scenario illustrates a poor setup for an incremental PDT, since it's a daily triggering PDT with a three-month offset. This means that at least three months of data will be rebuilt every day, which would be a very inefficient use of an incremental PDT. However, it is an interesting scenario to examine as a way of understanding of how incremental PDTs work.
Here is how this table will be updated on June 1st:
  * The daily persistence strategy means that the table is automatically built once a day. On June 1st, for example, the last row in the table will have been added on May 31st.
  * Because the increment key is based on the month, the PDT builder will truncate from May 31st back to the beginning of the month and rebuild the data for all of May and up to the current day, including June 1st.
  * Additionally, this PDT has an increment offset of `3`. This means that the PDT builder also rebuilds the data from the previous three time periods (months) before May. The result is that data is rebuilt from February, March, April, and up to the current day, June 1st.


Here is how this table will be updated on June 2nd:
  * On June 2nd, the last row in the table will have been added on June 1st.
  * The PDT builder will truncate the month back to June 1st and rebuild the data for the month of June, including June 2nd.
  * In addition, because of the increment offset, the PDT builder will rebuild the data from the previous three months before June. The result is that data is rebuilt from March, April, May, and up to the current day, June 2nd.


## Testing an incremental PDT in Development Mode
Before deploying a new incremental PDT to your production environment, you can test the PDT to be sure it builds and increments. To test an incremental PDT in Development Mode:
  1. Create an Explore for the PDT:
     * In an associated model file, use the `include` parameter to include the PDT's view file in the model file.
     * In the same model file, use the `explore` parameter to create an Explore for the incremental PDT's view.
```
 include: "/views/e_faa_pdt.view"
 explore: e_faa_pdt {}

```

  2. Open the Explore for the PDT. To do this, select the **See file actions** button and then select an Explore name.


  1. In the Explore, select some dimensions or measures and click **Run**. Looker will then build the entire PDT. If this is the first query you have run on the incremental PDT, the PDT builder will build the entire PDT to get the initial data. If the table is large, the initial build may take a significant amount of time, as would building any large table.
  2. You can verify that the initial PDT was built in the following ways:
     * If you have the `see_logs` permission, you can verify that the table was built by looking in the PDT Event Log. If you don't see the PDT create events in the PDT Event Log, check the status information at the top of the PDT Event Log Explore. If it says "from cache," you can select **Clear Cache & Refresh** to get more recent information.
     * Otherwise, you can look at the comments in the **SQL** tab of the Explore's **Data** bar. The **SQL** tab shows the query and the actions that will be taken when you run the query in the Explore. For example, if the comments in the **SQL** tab say `-- generate derived table e_incremental_pdt`, that is the action that will be taken when you click **Run**.
  3. Once you create the initial build of the PDT, prompt an incremental build of the PDT by using the **Rebuild Derived Tables & Run** option from the Explore.
  4. You can use the same methods as before to verify that the PDT builds incrementally:
     * If you have the `see_logs` permission, you can use the PDT Event Log to see `create increment complete` events for the incremental PDT. If you don't see this event in the PDT Event Log and the query status says "from cache," select **Clear Cache & Refresh** to get more recent information.
     * Look at the comments in the **SQL** tab of the Explore's **Data** bar. In this case, the comments will indicate that the PDT was incremented. For example: `-- increment persistent derived table e_incremental_pdt to generation 2`
  5. Once you've verified the PDT is built and incrementing correctly, if you don't want to keep the dedicated Explore for the PDT, you can remove or comment out the PDT's `explore` and `include` parameters from your model file.


After the PDT is built in Development Mode, the same table will be used for production once you deploy your changes, unless you make further changes to the table's definition. See the Persisted tables in Development Mode section of the **Derived tables in Looker** documentation page for more information.
## Troubleshooting incremental PDTs
This section describes some common issues that you may encounter while using incremental PDTs, as well as steps to troubleshoot and resolve those issues.
### Incremental PDT fails to build after schema change
If your incremental PDT is a SQL-based derived table, and the `sql` parameter includes a wildcard like `SELECT *`, then changes to your underlying database schema (such as column addition, column removal, or column data type change) may cause the PDT to fail with the following error:
```
SQL Error in incremental PDT: Query execution failed

```

To resolve this issue, edit the `SELECT` statement in the `sql` parameter to instead select individual columns. For example, if your select clause is `SELECT *`, change it to `SELECT column1, column2, ...`.
If your schema changes and you want to rebuild your incremental PDT from scratch, use the API call `start_pdt_build`, and include the `full_force_incremental` parameter.
## Supported database dialects for incremental PDTs
For Looker to support incremental PDTs in your Looker project, your database dialect must support Data Definition Language (DDL) commands that enable deleting and inserting rows.
The following table shows which dialects support incremental PDTs in the latest release of Looker (for Databricks, Incremental PDTs are supported only on Databricks version 12.1 and higher):
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
Databricks | Yes  
Denodo 7  
Denodo 8  
Dremio  
Dremio 11+  
Exasol  
Firebolt  
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL  
Google Spanner  
Greenplum | Yes  
HyperSQL  
IBM Netezza  
MariaDB  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+  
Microsoft SQL Server 2012+  
Microsoft SQL Server 2016  
Microsoft SQL Server 2017+  
MongoBI  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle  
Oracle ADWC  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB  
PrestoSQL  
SAP HANA  
SAP HANA 2+  
SingleStore  
SingleStore 7+  
Snowflake | Yes  
Teradata  
Trino  
Vector  
Vertica | Yes  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


