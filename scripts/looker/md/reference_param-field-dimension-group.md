# dimension_group  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-dimension-group

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  dimension_group
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
view: view_name {
  dimension_group:  field_name { ... }
}

```
Hierarchy `dimension_group` |  Accepts A Looker identifier (to serve as the first part of the name for each dimension created by the dimension group)Special Rules
  * The `type` can be `time` or `duration`
  * Typically used with a `timeframes` or `intervals` parameter
  * Use a `datatype` parameter if the dimension group is not based on a datetime field
  * For dimension groups of `type: time`, use a `convert_tz` parameter if you want to prevent automatic time zone conversion

  
---|---  
## Definition
The `dimension_group` parameter is used to create a set of time-based or duration-based dimensions all at once. You define the dimension group, and the dimension group will create a set of individual dimensions for different intervals or timeframes. For example, you can specify a dimension group of `type: time` based on a timestamp column, and the dimension group will create corresponding dimensions to express the data in time, date, week, hour, quarter, and year.
The form and function of the dimension group are different depending the `type` value of the dimension group:
  * Duration type


## Duration type dimension groups
`type: duration` is used in conjunction with a `dimension_group` to calculate a set of interval-based duration dimensions.
The form of a dimension group of `type: duration` is:
```
dimension_group: dimension_group_name {
  type: duration
  sql_start: SQL expression ;;  # often this is a single database column
  sql_end: SQL expression ;;  # often this is a single database column
  intervals: [interval, interval, …] # see following explanation for valid intervals
}

```

For dimension groups of `type: duration`:
  * The `sql_start` and `sql_end` parameters provide SQL expressions defining the start time and end time for the duration. See the Defining the start and end of a duration section on this page for details.
  * The `intervals` parameter specifies one or more interval units that should be used to measure the time difference. The possible choices are listed in the Interval options section on this page.
  * The duration values are floored to the nearest integer.
  * The `datatype` parameter is optional. If your dimension group is not based on a datetime you may specify an epoch, timestamp, date, or yyyymmdd format instead. For dimension groups of `type: duration`, the `datatype` parameter applies to both the `sql_start` and `sql_end` parameters, so be sure the `sql_start` and `sql_end` are both of the specified data type. The `datatype` parameter is described in greater detail in the Specifying the database `datatype` section on this page.


Although they are not listed here, many of the field-level parameters can be used with dimension groups as well.
As an example, if you have columns for `enrollment_date` and `graduation_date`, you can create a duration dimension group to see how much time students spent in school, calculated in week and year intervals:
```
dimension_group: enrolled {
  type: duration
  intervals: [week, year]
  sql_start: ${TABLE}.enrollment_date ;;
  sql_end: ${TABLE}.graduation_date ;;
}

```

In the Explore UI, this would generate a dimension group called **Duration Enrolled** , with individual dimensions called **Weeks Enrolled** and **Years Enrolled**.
### Interval options
The `intervals` parameter tells the dimension group which interval units it should use to measure the time difference between the `sql_start` time and the `sql_end` time. The `intervals` parameter is supported only for dimension groups of `type: duration`.
If `intervals` is not included, the dimension group will include all possible intervals.
The options for the `intervals` parameter are:
Interval | Description | Example Output  
---|---|---  
`day` | Calculates a time difference in days. | `9 days`  
`hour` | Calculates a time difference in hours. | `171 hours`  
`minute` | Calculates a time difference in minutes. | `10305 minutes`  
`month` | Calculates a time difference in months. | `3 months`  
`quarter` | Calculates a time difference in quarters of the year. | `2 quarters`  
`second` | Calculates a time difference in seconds. | `606770 seconds`  
`week` | Calculates a time difference in weeks. | `6 weeks`  
`year` | Calculates a time difference in years. | `2 years`  
### Defining the start and end of a duration
For dimension groups of `type: duration`, the `sql_start` and `sql_end` parameters provide the start and end information used to calculate a time difference. These fields can take any valid SQL expression that contains data in a timestamp, datetime, date, epoch, or yyyymmdd format. The `sql_start` and `sql_end` fields can be any of the following:
  * A reference to a `raw` timeframe from an existing dimension group of `type: time`
  * A reference to a dimension of `type: date_raw`
  * A SQL expression that is a timestamp, such as a reference to a SQL column that is a timestamp
  * A SQL expression that pulls a time from your database, using the appropriate expression for your dialect
  * A LookML field reference using the `::datetime` or `::date` field type reference


As an example, suppose you have a dimension named `faa_event_date_raw` that contains datetime information:
```
dimension: faa_event_date_raw {
  type: date_raw
  sql: ${TABLE}.event_date ;;
}

```

You can create a dimension group of `type: duration` that calculates the amount of time that has passed since the FAA event date. To do this, you can use the `faa_event_date_raw` dimension as the start time for the calculation, and then for the end time of the calculation you can use your dialect's SQL expression for the current time. This example is for a MySQL database:
```
dimension_group: since_event {
  type: duration
  intervals: [hour, day]
  sql_start: ${faa_event_date_raw} ;;
  sql_end: CURRENT_TIMESTAMP();;
}

```

In the Explore UI, this would generate a dimension group called **Duration Since Event** , with individual dimensions called **Hours Since Event** and **Days Since Event**.
### Referencing intervals from another LookML field
To reference an `interval` value in a `dimension_group` of `type: duration`, use the syntax `${interval_fieldname}`, using the plural version of the `interval` value. For example, in the following LookML example, the `average_days_since_event` measure uses `${days_since_event}` to reference the `day` interval in the `since_event` dimension group:
```

dimension_group: since_event {
  type: duration
  intervals: [hour, day, week, month, quarter, year]
  sql_start: ${faa_event_date_raw} ;;
  sql_end: CURRENT_TIMESTAMP();;
}

measure: average_days_since_event {
  type: average
  sql: ${days_since_event} ;;
}


```

### Using LookML field type references with duration fields
To create a custom duration field, you can specify a `::date` or `::datetime` reference type for the dimensions referenced in the `sql_start` and `sql_end` parameters of a dimension group of `type: duration`. The `view_name.field_name::type` syntax, described on the Incorporating SQL and referring to LookML objects documentation page, lets you create a `::date` or `::datetime` version of a field without casting the references to those dimensions to strings.
For example, suppose you have a `created` dimension group of `type: time` with timeframes of `time`, `date`, `week`, `month`, and `raw`, defined as follows:
```

dimension_group: created {
  type: time
  timeframes: [time, date, week, month, raw]
  sql: ${TABLE}.created_at ;;
}


```

Using the dimensions `created_month` and `created_time`, you can create a dimension group of `type: duration` that calculates the amount of time between a date from the `created_date` field and the first day of the month in which that date occurred, measured in weeks, days, and hours:
```

dimension_group: since_first_of_month {
  type: duration
  intervals: [week, day, hour]
  sql_start: ${created_month::datetime} ;;
  sql_end: ${created_time::datetime} ;;
}


```

In the Explore UI, this creates a dimension group called **Duration Since First of Month** , with individual dimensions **Weeks Since First of Month** , **Days Since First of Month** , and **Hours Since First of Month**. Specifying the `::datetime` reference type for the fields referenced in the `sql_start` and `sql_end` parameters allows the `created_month` and `created_time` dimensions to be treated as timestamps in the generated SQL.
As an example, suppose a user selects the **Created Date** and **Days Since First of Month** dimensions from the field picker. If one of the values returned for **Created Date** is **2019-03-10** , then the value returned for **Days Since First of Month** will be **9 days**.
## Time type dimension groups
`type: time` is used in conjunction with a `dimension_group` and the `timeframes` parameter to create a set of time-based dimensions. For example, you could easily create a date, week, and month dimension based on a single timestamp column.
The form of a dimension group of `type: time` is:
```
dimension_group: dimension_group_name {
  type: time
  timeframes: [timeframe, timeframe, …] # see following explanation for valid timeframes
  sql: SQL expression ;;  # often this is a single database column
  datatype: epoch| timestamp | datetime | date | yyyymmdd # defaults to datetime
  convert_tz: yes | no   # defaults to yes
}

```

For dimension groups of `type: time`:
  * The `timeframes` parameter is optional but is rarely skipped. It specifies one or more timeframes that should be generated by the dimension group. If `timeframes` is not included every timeframe option will be added to the dimension group. The possible choices are listed in the Timeframe options section on this page.
  * The `sql` parameter for `type: time` dimension groups can take any valid SQL expression that contains data in a timestamp, datetime, date, epoch, or yyyymmdd format.
  * The `datatype` parameter is optional. If your dimension group is not based on a datetime, you may specify an epoch, timestamp, date, or yyyymmdd format instead. It is described in greater detail in the Specifying the database `datatype` section on this page.
  * The `convert_tz` parameter is optional and lets you prevent automatic time zone conversion. It is described in greater detail in the Time zone conversions and `convert_tz` section on this page.


Although they are not listed here, many of the field-level parameters can be used with dimension groups as well.
As an example, suppose you had a column named `created_at` that contained datetime information. You want to create a date, week, and month dimension based on this datetime. You could use:
```
dimension_group: created {
  type: time
  timeframes: [date, week, month]
  sql: ${TABLE}.created_at ;;
}

```

In the Explore UI, this would generate three dimensions with the names **Created Date** , **Created Week** , and **Created Month**. Note how the `dimension_group` name is combined with the timeframes to generate the dimension names.
### Timeframe options
The `timeframes` parameter is supported only for dimension groups of `type: time`. For dimension groups of `type: duration`, use the `intervals` parameter instead.
The `timeframes` parameter tells the dimension group which dimensions it should produce and includes the following options:
  * Special timeframes
  * Time timeframes
  * Date timeframes
  * Week timeframes
  * Month timeframes
  * Quarter timeframes
  * Year timeframes
  * `hourX` timeframes
  * `minuteX` timeframes
  * `millisecondX` timeframes


#### Special timeframes
Timeframe | Description | Example Output  
---|---|---  
`raw` |  The raw value from your database, without casting or time zone conversion. `raw` is accessible only within LookML and **won't show up on the Explore page**. The `raw` timeframe returns a timestamp, unlike most other timeframes that return a formatted string. It is primarily used for performing date operations on a field. | `2014-09-03 17:15:00 +0000`  
`yesno` | A `yesno` dimension, returning "Yes" if the datetime has a value, otherwise "No". Unlike other timeframes, when you refer to a `yesno` timeframe dimension from another field, don't include the timeframe in the reference. For example, to refer to a `yesno` timeframe in the `dimension_group: created`, use the syntax `${created}`, not `${created_yesno}`. | `Yes`  
#### Time timeframes
Timeframe | Description | Example Output  
---|---|---  
`time` | Datetime of the underlying field (some SQL dialects show as much precision as your database contains, while others show only to the second) | `2014-09-03 17:15:00`  
`time_of_day` | Time of day | `17:15`  
`hour` | Datetime truncated to the nearest hour | `2014-09-03 17`  
`hour_of_day` | Integer hour of day of the underlying field  
`hourX` | Splits each day into intervals with the specified number of hours. | See Using `hourX`.  
`minute` | Datetime truncated to the nearest minute | `2014-09-03 17:15`  
`minuteX` | Splits each hour into intervals with the specified number of minutes. | See Using `minuteX`.  
`second` | Datetime truncated to the nearest second | `2014-09-03 17:15:00`  
`millisecond` | Datetime truncated to the nearest millisecond (see the Dialect support for milliseconds and microseconds section on this page for information on dialect support). | `2014-09-03 17:15:00.000`  
`millisecondX` | Splits each second into intervals with the specified number of milliseconds (see the Dialect support for milliseconds and microseconds section on this page for information on dialect support). | See Using `millisecondX`.  
`microsecond` | Datetime truncated to the nearest microsecond (see the Dialect support for milliseconds and microseconds section on this page for information on dialect support). | `2014-09-03 17:15:00.000000`  
#### Date timeframes
Timeframe | Description | Example Output  
---|---|---  
`date` | Date of the underlying field | `2017-09-03`  
#### Week timeframes
Timeframe | Description | Example Output  
---|---|---  
`week` | Date of the week starting on a Monday of the underlying datetime | `2017-09-01`  
`day_of_week` | Day of week alone | `Wednesday`  
`day_of_week_index` | Day of week index (0 = Monday, 6 = Sunday)  
#### Month timeframes
Timeframe | Description | Example Output  
---|---|---  
`month` | Year and month of the underlying datetime | `2014-09`  
`month_num` | Integer number of the month of the underlying datetime  
`fiscal_month_num` | Integer number of the fiscal month of the underlying datetime  
`month_name` | Name of the month | `September`  
`day_of_month` | Day of month  
To use the `fiscal_month_num` timeframes, the `fiscal_month_offset` parameter must be set in the model.
#### Quarter timeframes
Timeframe | Description | Example Output  
---|---|---  
`quarter` | Year and quarter of the underlying datetime | `2017-Q3`  
`fiscal_quarter` | Fiscal year and quarter of the underlying datetime | `2017-Q3`  
`quarter_of_year` | Quarter of the year preceded by a "Q"  
`fiscal_quarter_of_year` | Fiscal quarter of the year preceded by a "Q"  
To use the `fiscal_quarter` and `fiscal_quarter_of_year` timeframes, the `fiscal_month_offset` parameter must be set in the model.
#### Year timeframes
Timeframe | Description | Example Output  
---|---|---  
`year` | Integer year of the underlying datetime | `2017`  
`fiscal_year` | Integer fiscal year of the underlying datetime | `FY2017`  
`day_of_year` | Day of year | `143`  
`week_of_year` | Week of the year as a number  
To use the `fiscal_year` timeframe, the `fiscal_month_offset` parameter must be set in the model.
#### Using `hourX`
In `hourX` the `X` is replaced with 2, 3, 4, 6, 8, or 12.
This will split up each day into intervals with the specified number of hours. For example, `hour6` will split each day into 6 hour segments, which will appear as follows:
  * `2014-09-01 00:00:00`
  * `2014-09-01 06:00:00`
  * `2014-09-01 12:00:00`
  * `2014-09-01 18:00:00`


To give an example, a row with a `time` of `2014-09-01 08:03:17` would have a `hour6` of `2014-09-01 06:00:00`.
#### Using `minuteX`
In `minuteX` the `X` is replaced with 2, 3, 4, 5, 6, 10, 12, 15, 20, or 30.
This will split up each hour into intervals with the specified number of minutes. For example, `minute15` will split each hour into 15 minute segments, which will appear as follows:
  * `2014-09-01 01:00:00`
  * `2014-09-01 01:15:00`
  * `2014-09-01 01:30:00`
  * `2014-09-01 01:45:00`


To give an example, a row with a `time` of `2014-09-01 01:17:35` would have a `minute15` of `2014-09-01 01:15:00`.
#### Using `millisecondX`
In `millisecondX` the `X` is replaced with 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, or 500.
This will split up each second into intervals with the specified number of milliseconds. For example, `millisecond250` will split each second into 250 millisecond segments, which will appear as follows:
  * `2014-09-01 01:00:00.000`
  * `2014-09-01 01:00:00.250`
  * `2014-09-01 01:00:00.500`
  * `2014-09-01 01:00:00.750`


To give an example, a row with a `time` of `2014-09-01 01:00:00.333` would have a `millisecond250` of `2014-09-01 01:00:00.250`.
### Time zone conversions and `convert_tz`
In general, time computations (differences, durations, etc.) only work correctly when you operate on time values that are all converted to the same time zone, so it is important to keep time zones in mind when writing LookML.
Looker has various time zone settings that convert time-based data between different time zones. Looker does time zone conversion by default. The `convert_tz` parameter is supported for dimension groups of `type: time`. If you don't want Looker to perform a time zone conversion for a particular dimension or dimension group, you can use the `convert_tz` parameter described on the `convert_tz` parameter documentation page.
### Dialect support for milliseconds and microseconds
Looker supports timeframe precision to microseconds; however, some databases support precision only to the second. If a database encounters a timeframe more precise than it can support, it will round up to seconds.
In the latest release of Looker, the following dialects support milliseconds:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7  
Denodo 8  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL | Yes  
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
In the latest release of Looker, the following dialects support microseconds:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7  
Denodo 8  
Dremio  
Dremio 11+  
Exasol  
Firebolt  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL | Yes  
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
PrestoDB  
PrestoSQL  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino  
Vector | Yes  
Vertica | Yes  
### Specifying the database `datatype`
The `datatype` parameter lets you specify the type of time data in your database table that you are supplying to the dimension group, which can increase query performance.
For dimension groups of `type: time`, the `datatype` parameter applies to the `sql` parameter of the dimension group.
For dimension groups of `type: duration`, the `datatype` parameter applies to both the `sql_start` and `sql_end` parameters, so be sure the `sql_start` and `sql_end` are both of the specified data type.
The `datatype` parameter accepts the following values:
  * **`epoch`**: A SQL epoch field (i.e., an integer representing the number of seconds from the Unix epoch).
  * **`date`**: A SQL date field (i.e., one that does not contain time of day information).
  * **`datetime`**: A SQL datetime field.
  * **`timestamp`**: A SQL timestamp field.
  * **`yyyymmdd`**: A SQL field that contains an integer that represents a date of the form**YYYYMMDD**.


The default value for `datatype` is `timestamp`.
## Examples
Suppose you had a column named `created_at` that contained datetime information. You want to create a date, week, and month dimension based on this datetime. You could use:
```
dimension_group: created {
  type: time
  timeframes: [date, week, month]
  sql: ${TABLE}.created_at ;;
}

```

-
In the Explore UI, this would generate three dimensions with the names **Created Date** , **Created Week** , and **Created Month**. Note how the `dimension_group` name is combined with the timeframes to generate the dimension names.
## Things to consider
### Dimension groups must be referenced by their individual dimensions
Because a dimension group represents a group of dimensions, instead of just one dimension, you cannot refer to it directly in LookML. Instead, you'll need to refer to the dimensions it creates.
For example, consider this dimension group:
```
dimension_group: created {
  type: time
  timeframes: [date, week, month]
  sql: ${TABLE}.created_at ;;
}

```

To refer to one of these dimensions in another LookML field, use the reference `${created_date}`, `${created_week}`, or `${created_month}`. If you try to use just `${created}`, Looker won't know which timeframe you are referring to and an error will result.
For this same reason, you should not use the `primary_key` parameter on a dimension group if you specify more than one `timeframe`.
> **Chat Team Tip** : We are frequently asked about the validation error that can occur if you're using `primary_key` on a `dimension_group` with more than one `timeframe`. For more information, check out the Timeframes and Dimension Groups in Looker  Community post.
### Timestamp data that includes time zone information
Some database dialects have timestamp options that include time zone information. This lets you store timestamp data in a single field that may have multiple time zones. One row of data might be stored in UTC, another row in Eastern time. As an example, see the Snowflake `TIMESTAMP_LTZ, TIMESTAMP_NTZ, TIMESTAMP_TZ` timestamp documentation for information about the Snowflake dialect timestamp options.
In this case, when Looker performs time zone conversions, errors can occur. To avoid this, in the `sql` parameter of the dimension, you should explicitly cast the timestamp data to a timestamp type that does not do time zone conversion. For example, in the Snowflake dialect, you could use the `TO_TIMESTAMP` function to cast the timestamp data.
### It is possible to create individual time or duration dimensions
It is possible to create one dimension for each individual timeframe or duration you want to include, instead of generating all of them in a single `dimension_group`. You can generally avoid creating individual dimensions, unless you want to change Looker's timeframe naming convention, or you have already pre-calculated time columns in your database. For more information, see the Dimension, filter, and parameter types documentation page.
### You can change the first day of the week
By default, weeks in Looker start on Monday. You can change this by using the `week_start_day` parameter at the model level.
Just keep in mind that `week_start_day` does not work with the `week_of_year` timeframe because that timeframe is based on the ISO standard, which uses Monday weeks.
### Custom filters and custom fields don't support all timeframes
The timeframes `day_of_week`, `fiscal_quarter_of_year`, `millisecond`, `millisecondX`, `microsecond`, `month_name`, `quarter_of_year`, and `time_of_day` are not supported in custom filters or custom fields.
### Month, quarter, and year intervals only count complete periods
The `month` interval in a `duration` dimension group only considers a month to have passed if the ending day is greater than or equal to the starting day. For example:
  * The difference in months between September 26 and October 25 of the same year is 0.
  * The difference in months between September 26 and October 26 of the same year is 1.


The `quarter` and `year` intervals follow the same logic.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


