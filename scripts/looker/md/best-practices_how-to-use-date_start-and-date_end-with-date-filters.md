# Using date_start and date_end with date filters  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-use-date_start-and-date_end-with-date-filters

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Use case examples
    * Monthly partitioned columns (in BigQuery)
    * Log files are in UTC when querying in American time zones (in BigQuery)
    * Trailing N-day window functions (in BigQuery)
    * Table partitioned by date via string with format 'YYYY-MM-DD' (in Presto)




Was this helpful?
Send feedback 
#  Using date_start and date_end with date filters
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Use case examples
    * Monthly partitioned columns (in BigQuery)
    * Log files are in UTC when querying in American time zones (in BigQuery)
    * Trailing N-day window functions (in BigQuery)
    * Table partitioned by date via string with format 'YYYY-MM-DD' (in Presto)


You can use templated filters to refer to dates by selecting the beginning and end dates in a date filter — `{% date_start date_filter %}` and `{% date_end date_filter %}`, respectively. This page will walk you through some use cases examples and the steps to accomplish them. 
## Syntax notes
  * BigQuery allows greater control when working with table wildcard functions like `TABLE_DATE_RANGE` and `TABLE_QUERY`, so using `{% table_date_range prefix date_filter %}` is insufficient for specifying date filters. 
  * Hadoop allows working with date-partitioned columns, no matter the type (`string`, `date`) or format (`YYYY-MM-DD`) of the column. 


## Usage notes
  * When there is no value specified for `date_filter`, both `{% date_start date_filter %}` and `{% date_end date_filter %}` will evaluate to `NULL`. 
  * In the case of an open-ended `date_filter` (such as `before 2016-01-01` or `after 2016-01-01`), then one of `{% date_start date_filter %}` or `{% date_end date_filter %}` filters will be `NULL`. 
To make sure neither of these two cases result in invalid SQL, you can use `IFNULL` or `COALESCE` in the LookML. 


## Use case examples
### Monthly partitioned columns (in BigQuery)
In some BigQuery datasets, tables are organized by month, and the table ID has the year and month combination as a suffix. An example of this is in the following dataset, which has many tables with names like `pagecounts_201601`, `pagecounts_201602`, `pagecounts_201603`. 
#### Example 1: LookML that depends on `always_filter`
The following derived table uses `TABLE_QUERY([dataset], [expr])` to get the right set of tables to query: 
```
view: pagecounts {
  derived_table: {
    sql: SELECT * FROM
    TABLE_QUERY([fh-bigquery:wikipedia],
    "length(table_id) = 17 AND
    table_id >= CONCAT( 'pagecounts_' , STRFTIME_UTC_USEC({% date_start date_filter %},'%Y%m') ) AND
    table_id <= CONCAT('pagecounts_' , STRFTIME_UTC_USEC({% date_end date_filter %},'%Y%m') )";
    )
    ;;
  }
  filter: date_filter {
    type: date
  }
}

```

**Some notes on the code in the expression:**
  * `table_id` refers to the name of the table in the dataset. 
  * `length(table_id) = 17` makes sure it ignores the other tables with names like `pagecounts_201407_en_top64k`. 
  * `STRFTIME_UTC_USEC({% date_start date_filter %},'%Y%m')` will output just the `YYYYmm` part of the beginning date. 


`NULL` will be substituted for the `date_filter` parts. Getting around this requires an `always_filter` on the Explore: 
```
explore: pagecounts {
  always_filter: {
    filters: [date_filter: "2 months ago"]
  }
}

```

Note that this will still fail for filters for dates from before the earliest date in the dataset because `{% date_start date_filter %}` will evaluate to `NULL`. 
#### Example 2: LookML that does not depend on `always_filter`
It is also possible to use `COALESCE` or `IFNULL` to encode a default set of tables to query. In the following example, the past two months are used: 
  * The lower bound: `COALESCE({% date_start date_filter %},DATE_ADD(CURRENT_TIMESTAMP(),-2,'MONTH'))`
  * The upper bound: `COALESCE({% date_end date_filter %},CURRENT_TIMESTAMP())`

```
view: pagecounts {
  derived_table: {
    sql: SELECT * FROM
    TABLE_QUERY([fh-bigquery:wikipedia],
    "length(table_id) = 17 AND
    table_id >= CONCAT( 'pagecounts_'; , STRFTIME_UTC_USEC(COALESCE({% date_start date_filter %},DATE_ADD(CURRENT_TIMESTAMP(),-2,'MONTH')),'%Y%m') ) AND
    table_id <= CONCAT( 'pagecounts_' , STRFTIME_UTC_USEC(COALESCE({% date_end date_filter %},CURRENT_TIMESTAMP()),'%Y%m') )"
    )
    ;;
  }
  filter: date_filter {
    type: date
  }
}

```

### Log files are in UTC when querying in American time zones (in BigQuery)
Sometimes your Looker log files are stored in UTC, even though you are querying in Eastern or Pacific time zones. This issue can cause a problem where the log files have already rolled to "tomorrow's" date in the local timezone of the query, resulting in some missed data. 
The solution is to add an extra day to the end date of the date filter, to make sure that if it is past midnight UTC, those log entries are picked up. 
The following examples use the public `[githubarchive:day]` dataset, which has a daily partition of GitHub information. 
#### Example 1: LookML that depends on `always_filter`
```
view: githubarchive {
  derived_table: {
    sql: SELECT * FROM
    TABLE_DATE_RANGE([githubarchive:day.],
    {% date_start date_filter %},
    DATE_ADD({% date_end date_filter %},1,"DAY")
    )
    ;;
  }

  filter: date_filter {
    type: date
  }
}

```

Because this SQL will fail if `NULL` is substituted for the dates, it is necessary to add an `always_filter` to the Explore: 
```
explore: githubarchive {
  always_filter: {
    filters: [date_filter: "2 days ago"]
  }
}

```

#### Example 2: LookML that does not depend on `always_filter`
In this example, the default date range is encoded in the LookML. Because `COALESCE` was returning an `unknown` type, I ultimately had to use `IFNULL` to make the SQL work. 
  * The lower bound: `IFNULL({% date_start date_filter %},CURRENT_DATE())`
  * The upper bound: `IFNULL({% date_end date_filter %},CURRENT_DATE())` + 1 day 

```
view: githubarchive {
  derived_table: {
    sql: SELECT * FROM
    TABLE_DATE_RANGE([githubarchive:day.],
    IFNULL({% date_start date_filter %},CURRENT_TIMESTAMP()),
    DATE_ADD(IFNULL({% date_end date_filter %},CURRENT_TIMESTAMP()),1,"DAY")
    )
    ;;
  }
  filter: date_filter {
    type: date
  }
}

```

### Trailing N-day window functions (in BigQuery)
When performing certain analyses, calculations are expected in some aggregate form over a historical timeframe. To perform this operation in SQL, one will typically implement a window function that reaches back `n` number of rows for a table unique by date. However, there is a catch-22 when using a date-partitioned table — one must first dictate the set of tables that the query will run against, even as the query really needs extra historical tables for computation. 
**The solution:** Allow the start date to be earlier than the dates provided in the date filter. Here is an example reaching back an additional week: 
```
view: githubarchive {
  derived_table: {
    sql:  SELECT y._date,
                y.foo,
                y.bar
            FROM (
              SELECT _date,
                    SUM(foo) OVER (ORDER BY _date RANGE BETWEEN x PRECEDING AND CURRENT ROW),
                    COUNT(DISTINCT(bar)) OVER (ORDER BY _date RANGE BETWEEN x PRECEDING AND CURRENT ROW)
                FROM (
                    SELECT _date,
                          foo,
                          bar
                      FROM TABLE_DATE_RANGE([something:something_else.], DATE_ADD(IFNULL({% date_start date_filter %},CURRENT_TIMESTAMP()), -7, "DAY"), IFNULL({% date_end date_filter %},CURRENT_TIMESTAMP()))
                      ) x
            ) y
          WHERE {% condition date_filter %} y._date {% endcondition %};;
  }
  filter: date_filter {
    type: date
  }
}

```

The extra `SELECT` statement is needed because it is supplying a `WHERE` constraint to trim the resultset back down to the date range the user originally specified in the query. 
### Table partitioned by date via string with format 'YYYY-MM-DD' (in Presto)
It is a common pattern in Hadoop tables to use partitioned columns to speed up search times for columns that are commonly searched on, especially dates. The format of the date columns can be arbitrary, though `YYYY-MM-DD` and `YYYYMMDD` are most common. The type of the date column can be string, date, or number. 
In this example, a Hive table `table_part_by_yyyy_mm_dd` has a partitioned column `dt`, a string formatted `YYYY-MM-DD`, that is being searched by Presto. 
When the generator is first run, the LookML looks like this: 
```
view: table_part_by_yyyy_mm_dd {
  sql_table_name: hive.taxi. table_part_by_yyyy_mm_dd ;;
  suggestions: no
  dimension: dt {
    type: string
    sql: ${TABLE}.dt ;;
  }
}

```

Some notes on the code in the expressions in both of the following examples: 
  * The output of `date_start` and `date_end` is `type: timestamp`. 
  * `date_format( <expr>, '%Y-%m-%d')` is used to convert the timestamp to a string and to the right format. 
  * The `coalesce` is to handle the case of NULLs if someone types in a filter like `before 2010-01-01` or `after 2012-12-31`. 
  * This is Presto dialect code, so Hive will have some differences in the format string (`yyyy-MM-dd`) and `date_format` can't take a NULL value, so the `coalesce` would have to move in there with some sort of default value. 


#### Example 1: LookML that uses a common table expression to filter the table
This example uses a derived table to filter the table.
```
view: table_part_by_yyyy_mm_dd {
  # sql_table_name: hive.taxi. table_part_by_yyyy_mm_dd
  suggestions: no
  derived_table: {
    sql: SELECT * FROM hive.taxi. table_part_by_yyyy_mm_dd
      WHERE ( coalesce( dt >= date_format({% date_start date_filter %}, '%Y-%m-%d'), TRUE) )
      AND ( coalesce( dt <= date_format({% date_end date_filter %}, '%Y-%m-%d'), TRUE) )
      ;;
  }
  filter: date_filter {
    type: date
  }
  dimension: dt {
    type: string
    sql: ${TABLE}.dt ;;
  }
}

```

Usually, partitioned tables take too long for full table scans (and consume too many cluster resources), so it is a good idea to put a default filter on the Explore for this view as well: 
```
explore: table_part_by_yyyy_mm_dd {
  always_filter: {
    filters: [date_filter: "2013-01"]
  }
}

```

#### Example 2: LookML that filters directly in the predicate
This example does the predicate filtering directly on the table, without a subquery or common table expression. 
```
view: table_part_by_yyyy_mm_dd {
  sql_table_name: hive.taxi.table_part_by_yyyy_mm_dd ;;
  filter: date_filter {
    type: date
    sql: ( coalesce( ${dt} >= date_format({% date_start date_filter %}, '%Y-%m-%d'), TRUE) )
    AND ( coalesce( ${dt} <= date_format({% date_end date_filter %}, '%Y-%m-%'), TRUE) );;
  }
  dimension: dt {
    type: string
    sql: ${TABLE}.dt ;;
  }
}

```

We can validate that the table partitions are actually being used by checking the output of `EXPLAIN` in SQL Runner for a query generated by this LookML (you can access to it by clicking to the SQL section in the Data tab of the Explore page), you will see something like this: 
```
output[table_part_by_yyyy_mm_dd.count] => [count:bigint]
table_part_by_yyyy_mm_dd.count := count
  TopN[500 by (count DESC_NULLS_LAST)] => [count:bigint]
  Aggregate(FINAL) => [count:bigint]
  count := "count"("count_4")
  RemoteExchange[GATHER] => count_4:bigint
  Aggregate(PARTIAL) => [count_4:bigint]
  count_4 := "count"(*)
  Filter[(COALESCE(("dt" >= CAST('2013-04-01' AS VARCHAR)), true) AND COALESCE(("dt" <= CAST('2016-08-01' AS VARCHAR)), true))] => [dt:varchar]
  TableScan[hive:hive:taxi: table_part_by_yyyy_mm_dd, originalConstraint = (COALESCE(("dt" >= CAST('2013-04-01' AS VARCHAR)), true) AND COALESCE(("dt" <= CAST('2016-08-01' AS VARCHAR)), true))] => [dt:varchar]
  LAYOUT: hive dt := HiveColumnHandle{clientId=hive, name=dt, hiveType=string, hiveColumnIndex=-1, partitionKey=true}
  :: [[2013-04-01, 2013-12-31]]

```

The `partitionKey=true` along with the range of partition keys listed indicate that it is only scanning those partitioned columns. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


