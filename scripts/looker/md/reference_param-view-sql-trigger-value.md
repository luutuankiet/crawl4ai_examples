# sql_trigger_value  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-sql-trigger-value

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Examples
  * Common challenges
    * sql_trigger_value requires that you have set up persistent derived tables
    * sql_trigger_value works differently between Development Mode and Production Mode




Was this helpful?
Send feedback 
#  sql_trigger_value
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Examples
  * Common challenges
    * sql_trigger_value requires that you have set up persistent derived tables
    * sql_trigger_value works differently between Development Mode and Production Mode


## Usage
```
view: my_view {
  derived_table: {
    sql_trigger_value: SELECT CURDATE() ;;
    ...
  }
}

```

Hierarchy `sql_trigger_value` |  Default Value NoneAccepts A SQL statement that results in one row and one column   
---|---  
## Definition
> Consider instead using a `datagroup` and `datagroup_trigger`, described on the Caching queries documentation page.
`sql_trigger_value` lets you trigger the regeneration of a persistent derived table based on a SQL statement that you provide. If the result of the SQL statement is different from the previous value, the PDT is regenerated.
The `sql_trigger_value` parameter will only consider the first row and column in the SQL you write. Therefore, we strongly recommend that you write your query to return just one value (one row and one column). This removes any confusion for future developers and protects non-streaming SQL dialects from loading large result sets into memory.
By default, every five minutes Looker runs the SQL query that you write, as long as another persistent derived table is not in the process of being built. If the results of the SQL query change, Looker will re-generate the derived table. You can change this schedule as desired by using the **PDT And Datagroup Maintenance Schedule** setting in Looker's admin settings.
For example, suppose you were running MySQL and used:
```
    sql_trigger_value: SELECT CURDATE() ;;

```

The results would be like:
sql_trigger_value Run Time | sql_trigger_value Result  
---|---  
2015-01-01 00:00 | 2015-01-01  
2015-01-01 00:05 | 2015-01-01  
2015-01-01 00:10 | 2015-01-01  
... | ...  
2015-01-01 23:55 | 2015-01-01  
2015-01-02 00:00 | 2015-01-02  
2015-01-02 00:05 | 2015-01-02  
You can see that the value of this SQL query will change once per day at midnight, so the derived table will be regenerated at these times.
> Looker does not perform time zone conversion for `sql_trigger_value`. When you use `sql_trigger_value` to trigger a PDT rebuild at midnight or at a specific time of day, the trigger will occur in the time zone your database is configured for.
If your admin has given you the `develop` permission, you can force a derived table to regenerate before its `sql_trigger_value` query has changed. Select the **Rebuild Derived Tables & Run** option from the **Explore actions** gear menu after running a query.
See the Derived tables in Looker documentation page for further details about the **Rebuild Derived Tables & Run** option.
## Examples
Create a PDT on MySQL that rebuilds once per day at midnight:
```
view: clean_events {
  derived_table: {
    sql:
      SELECT *
      FROM events
      WHERE type NOT IN ('test', 'staff') ;;
    sql_trigger_value: SELECT CURDATE() ;;
  }
}

```

The following sections show the SQL to use for various PDT rebuilding strategies on different dialects:
### Google BigQuery
Desired Regeneration Schedule | SQL to Use  
---|---  
Once per day at midnight Pacific Time | ```
SELECT FORMAT_TIMESTAMP('%F', CURRENT_TIMESTAMP(), 'America/Los_Angeles')
```
  
Once per day at a specific hour |  ```
SELECT FLOOR(((TIMESTAMP_DIFF(CURRENT_TIMESTAMP(),'1970-01-01 00:00:00',SECOND)) - 60*60*3)/(60*60*24))
```
_Replace the "3" with the hour of day you would like the regeneration to occur_  
Twice per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 4am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4 and 18 with the hours of day you would like the regeneration to occur_  
Three times per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 9
    THEN 'between 4am and 9am'
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 9 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 9am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4, 9, and 18 with the hours of day you would like the regeneration to occur_  
Every hour | ```
SELECT EXTRACT(HOUR FROM CURRENT_TIMESTAMP())
```
  
Every 2 hours |  ```
SELECT FLOOR((TIMESTAMP_DIFF(CURRENT_TIMESTAMP(),'1970-01-01 00:00:00',SECOND)) / (2*60*60))
```
_You can replace the "2" with the number of hours you would like between each regeneration_  
Never update data | ```
SELECT 1
```
  
### MySQL
Desired Regeneration Schedule | SQL to Use  
---|---  
Once per day at midnight | ```
SELECT CURDATE()
```
  
Once per day at a specific hour Coordinated Universal Time (UTC) |  ```
SELECT FLOOR((UNIX_TIMESTAMP(NOW()) - 60*60*3)/(60*60*24))
```
_Replace the "3" with the hour of day you would like the regeneration to occur_  
Twice per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 4am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4 and 18 with the hours of day you would like the regeneration to occur_  
Three times per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 9
    THEN 'between 4am and 9am'
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 9 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 9am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4, 9, and 18 with the hours of day you would like the regeneration to occur_  
When a particular table is updated | ```
SELECT COUNT(*) FROM table
```
  
Every hour | ```
SELECT HOUR(CURTIME())
```
  
Every 2 hours Coordinated Universal Time (UTC) |  ```
SELECT FLOOR(UNIX_TIMESTAMP() / (2*60*60))
```
_You can replace the "2" with the number of hours you would like between each regeneration_  
Never update data | ```
SELECT 1
```
  
### Amazon Redshift
Desired Regeneration Schedule | SQL to Use  
---|---  
Once per day at midnight | ```
SELECT CURRENT_DATE
```
  
Once per day at a specific hour |  ```
SELECT FLOOR((EXTRACT(epoch from GETDATE()) - 60*60*3)/(60*60*24))
```
_Replace the "3" with the hour of day you would like the regeneration to occur_  
Twice per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 4am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4 and 18 with the hours of day you would like the regeneration to occur_  
Three times per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 9
    THEN 'between 4am and 9am'
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 9 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 9am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4, 9, and 18 with the hours of day you would like the regeneration to occur_  
When a particular table is updated | ```
SELECT COUNT(*) FROM table
```
  
Every hour | ```
SELECT DATE_PART('hour', GETDATE())
```
  
Every 2 hours |  ```
SELECT FLOOR(EXTRACT(epoch from GETDATE()) / (2*60*60))
```
_You can replace the "2" with the number of hours you would like between each regeneration_  
Never update data | ```
SELECT 1
```
  
### PostgreSQL
Desired Regeneration Schedule | SQL to Use  
---|---  
Once per day at midnight | ```
SELECT CURRENT_DATE
```
  
Once per day at a specific hour |  ```
SELECT FLOOR((EXTRACT(epoch from NOW()) - 60*60*3)/(60*60*24))
```
_Replace the "3" with the hour of day you would like the regeneration to occur_  
Twice per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 4am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4 and 18 with the hours of day you would like the regeneration to occur_  
Three times per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 9
    THEN 'between 4am and 9am'
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 9 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 9am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4, 9, and 18 with the hours of day you would like the regeneration to occur_  
When a particular table is updated | ```
SELECT COUNT(*) FROM table
```
  
Every hour | ```
SELECT DATE_PART('hour', NOW())
```
  
Every 2 hours |  ```
SELECT FLOOR(EXTRACT(epoch from NOW()) / (2*60*60))
```
_You can replace the "2" with the number of hours you would like between each regeneration_  
Never update data | ```
SELECT 1
```
  
### Snowflake
Desired Regeneration Schedule | SQL to Use  
---|---  
Once per day at midnight | ```
SELECT CURRENT_DATE()
```
  
Once per day at a specific hour Coordinated Universal Time (UTC) |  ```
SELECT FLOOR((DATE_PART('EPOCH_SECOND', CURRENT_TIMESTAMP) - 60*60*3)/(60*60*24))
```
_Replace the "3" with the hour of day you would like the regeneration to occur_  
Twice per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 4am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4 and 18 with the hours of day you would like the regeneration to occur_  
Three times per day at specific hours |  ```
SELECT CASE
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 4 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 9
    THEN 'between 4am and 9am'
  WHEN EXTRACT(HOUR FROM CURRENT_TIMESTAMP) > 9 AND EXTRACT(HOUR FROM CURRENT_TIMESTAMP) < 18
    THEN 'between 9am and 6pm'
  ELSE 'between 6pm and 4am'
END
```
_Replace 4, 9, and 18 with the hours of day you would like the regeneration to occur_  
When a particular table is updated | ```
SELECT COUNT(*) FROM table
```
  
Every hour | ```
SELECT HOUR(CURRENT_TIME())
```
  
Every 2 hours Coordinated Universal Time (UTC) |  ```
SELECT FLOOR(DATE_PART('EPOCH_SECOND', CURRENT_TIMESTAMP) / (2*60*60))
```
_You can replace the "2" with the number of hours you would like between each regeneration_  
Never update data | ```
SELECT 1
```
  
## Common challenges
###  `sql_trigger_value` requires that you have set up persistent derived tables
Using `sql_trigger_value` will cause LookML validation errors unless you have enabled persistence for derived tables in your database connection settings. Most customers _do_ set up persistent derived tables when they initially configure a database connection. The most common exception to this rule is for customers that connect Looker to a PostgreSQL read-only, hot-swap secondary.
###  `sql_trigger_value` works differently between Development Mode and Production Mode
`sql_trigger_value` should work as expected in Production Mode. In Development Mode, all derived tables are treated as if `persist_for: 24 hours` has been used, no matter what setting you have implemented. See the Persisted tables in Development Mode section of the Derived tables in Looker documentation page for more information.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


