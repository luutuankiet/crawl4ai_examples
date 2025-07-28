# Looker filter expressions  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/filter-expressions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to know about filter expressions
  * Filter expressions for each filter type
  * String
    * Including special characters in string filters
  * Date and Time
    * Basic structure of date and time filters
  * Location
    * Supported units of measurement
  * User Attribute Values




Was this helpful?
Send feedback 
#  Looker filter expressions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to know about filter expressions
  * Filter expressions for each filter type
  * String
    * Including special characters in string filters
  * Date and Time
    * Basic structure of date and time filters
  * Location
    * Supported units of measurement
  * User Attribute Values


Filter expressions are an advanced way to filter Looker queries. You can use filter expressions in the following ways:
  * In the Explore section of Looker, you can add a filter, choose the **matches (advanced)** option, and then enter one of the expressions that are listed on this page for the filter type as the filter value.
  * In LookML elements that take a `filter` parameter.


This page lists the values that you can enter for a filter that uses the **matches (advanced)** condition option in a Looker Explore. Depending on the filter type and your input for the filter value, Looker may convert the **matches (advanced)** option to a filter condition that may be more appropriate.
## Things to know about filter expressions
Keep the following notes in mind when working with Looker filter expressions:
  * The filter expressions on this page are also supported for some filter types in Looker Studio when the Looker connector references a Looker Explore as a data source and the filter employs a **Matches (advanced)** condition. The **Matches (advanced)** condition behaves somewhat differently in Looker Studio than it does in a Looker Explore. Looker may convert the **matches (advanced)** condition to a more appropriate condition, based on the user's input. However, Looker Studio uses the **Matches (advanced)** option as a catch-all condition when the user's input is inappropriate for the other filter conditions that Looker Studio supports, but Looker Studio doesn't convert the condition.
  * In Explores, basic filters use some phrases that differ in meaning from the filter expressions that are documented on this page.
  * When using filter expressions in LookML, place the expression in quotation marks (see the `filters` documentation page for proper use). This is especially important for logical values like `NULL`. When using filter expressions in the Explore section of Looker, you don't need to place the expression in quotation marks.
  * Filter expressions aren't supported with access grants. See the `access_grant` documentation page for more information.


## Filter expressions for each filter type
Enter the following examples as filter values in Looker Explore filters that use the **matches (advanced)** condition option. Filter expressions are supported for the following filter types:
  * Date and time


## String
Example | Description  
---|---  
`FOO` | is equal to "FOO", exactly  
`FOO,BAR` | is equal to either "FOO" or "BAR", exactly  
`%FOO%` | contains "FOO", matches "buffoon" and "fast food"  
`FOO%` | starts with "FOO", matches "foolish" and "food" but not "buffoon" or "fast food"  
`%FOO` | ends with "FOO", matches "buffoo" and "fast foo" but not "buffoon" or "fast food"  
`F%OD` | starts with an "F" and ends with "OD", matches "fast food"  
`EMPTY` | string is empty (has zero characters) or is null (no value)  
`NULL` | value is null (when it is used as part of a LookML filter expression, place `NULL` in quotes, as shown on the `filters` documentation page)  
`-FOO` | is not equal to "FOO" (is any value except "FOO"), matches "pizza", "trash", "fun" but not "foo"  
`-FOO,-BAR` | is not equal to either "FOO" or "BAR", matches any value except "FOO" and "BAR"  
`-%FOO%` | doesn't contain "FOO", does not match "buffoon" or "fast food"  
`-FOO%` | doesn't start with "FOO", does not match "foolish" or "food"  
`-%FOO` | doesn't end with "FOO", does not match "buffoo" or "fast foo"  
`-EMPTY` | string is not empty (has at least one character)  
`-NULL` | value of column is not null (when it is used as part of a LookML filter expression, place `-NULL` in quotes, as shown on the `filters` documentation page)  
`FOO%,BAR` | starts with "FOO" or is "BAR" exactly, matches "food" and matches "bar" but not "barfood"  
`FOO%,-FOOD` | starts with "FOO" but is not "FOOD"  
`_UF` | has any single character followed by "UF", matches "buffoon"  
### Including special characters in string filters
Note these rules for including special characters in string filters:
  * To include `"`, `%`, or `_`, prefix with the escape character, `^`. For example: `^"`, `^%`, and `^_`
  * To include a leading `-`, escape it as `^-`. This is only necessary if the `-` is the leading character; you don't need to escape `-` if it is inside the string.
  * To include `^`, escape it as `^^`.
  * To include a comma in a regular UI string filter, prefix the comma with a backslash character, `\`. For example: `Santa Cruz\, CA`.
  * To include a comma with the **matches (advanced)** option in a filter, prefix the comma with the escape character, `^`. For example: `Santa Cruz^, CA`.
  * To include a comma in a filter expression in LookML, prefix with the escape character, `^`. For example: 

```
  field: filtered_count {
      type: count
      filters: [city: "Santa Cruz^, CA"]
    }

```

## Date and Time
Looker date filtering allows for English phrases to be used instead of SQL date functions.
### Basic structure of date and time filters
For the following examples:
  * **`{n}`**is an integer.
  * **`{interval}`**is a time increment such as hours, days, weeks, or months.
The phrasing you use determines whether the `{interval}` will include partial time periods or only complete time periods. For example, the expression `3 days` includes the current, partial day as well as the prior two days. The expression `3 days ago for 3 days` includes the previous three complete days and excludes the current, partial day. See the Relative Dates section for more information.
  * **`{time}`**can specify a time formatted as either YYYY-MM-DD HH:MM:SS or YYYY/MM/DD HH:MM:SS, or a date formatted as either YYYY-MM-DD or YYYY/MM/DD. When using the form YYYY-MM-DD, be sure to include both digits for the month and day, for example, 2016-01. Truncating a month or day to a single digit is interpreted as an offset, not a date. For example, 2016-1 is interpreted as 2016 minus one year, or 2015.


These are all the possible combinations of date filters:
Combination | Example | Notes  
---|---|---  
`this {interval}` | `this month` | You can use `this week`, `this month`, `this quarter`, or `this year`. Note that `this day` isn't supported. If you want to get data from the current day, you can use `today`.  
`{n} {interval}` | `3 days`  
`{n} {interval} ago` | `3 days ago`  
`{n} {interval} ago for {n} {interval}` | `3 months ago for 2 days`  
`before {n} {interval} ago` | `before 3 days ago`  
`before {time}` | `before 2018-01-01 12:00:00` |  `before` is not inclusive of the time you specify. The expression `before 2018-01-01` will return data from all dates before 2018-01-01, but it won't return data from 2018-01-01.  
`after {time}` | `after 2018-10-05` |  `after` is inclusive of the time you specify. So, the expression `after 2018-10-05` will return data from 2018-10-05 and all dates later than 2018-10-05.  
`{time} to {time}` |  `2018-05-18 12:00:00 to``2018-05-18 14:00:00` | The initial time value is inclusive but the latter time value is not. So the expression `2018-05-18 12:00:00 to 2018-05-18 14:00:00` will return data with the time "2018-05-18 12:00:00" through "2018-05-18 13:59:59".  
`this {interval} to {interval}` | `this year to second` | The beginning of each interval is used. For example, the expression `this year to second` returns data from the beginning of the year the query is run through to the beginning of the second the query is run. `this week to day` returns data from the beginning of the week the query is run through to the beginning of the day the query is run.  
`{time} for {n} {interval}` | `2018-01-01 12:00:00 for 3 days`  
`today` | `today`  
`yesterday` | `yesterday`  
`tomorrow` | `tomorrow`  
`{day of week}` | `Monday` | Specifying a day of week with a **Dimension Group Date** field returns the most recent date that matches the specified day of week. For example, the expression `Dimension Group Date matches (advanced) Monday` returns the most recent Monday.`{day of week}` with the `before` and `after` keywords in this context. For example, the expression `Dimension Group Date matches (advanced) after Monday` returns the most recent Monday and everything after the most recent Monday. The expression `Dimension Group Date matches (advanced) before Monday` returns every day before the most recent Monday, but it doesn't return the most recent Monday.**Dimension Group Day of Week** field returns every day that matches the specified day of week. So the expression `Dimension Group Day of Week matches (advanced) Monday` returns every Monday.  
`next {week, month, quarter, fiscal quarter, year, fiscal year}` | `next week` | The `next` keyword is unique in that it requires one of the intervals listed previously and won't work with other intervals.  
`{n} {interval} from now` | `3 days from now`  
`{n} {interval} from now for {n} {interval}` | `3 days from now for 2 weeks`  
Date filters can also be combined together:
  * **To get OR logic:** Type multiple conditions into the same filter, separated by commas. For example, `today, 7 days ago` means "today or 7 days ago".
  * **To get AND logic:** Type your conditions, one by one, into multiple date or time filters. For example, you could put `after 2014-01-01` into a **Created Date** filter, then put `before 2 days ago` into a **Created Time** filter. This would mean "January 1st, 2014 and after, and before 2 days ago".


### Absolute dates
Absolute date filters use the specific date values to generate query results. These are useful when creating queries for specific date ranges.
Example | Description  
---|---  
`2018/05/29` | sometime on 2018/05/29  
`2018/05/10 for 3 days` | from 2018/05/10 00:00:00 through 2018/05/12 23:59:59  
`after 2018/05/10` | 2018/05/10 00:00:00 and after  
`before 2018/05/10` | before 2018/05/10 00:00:00  
`2018/05` | within the entire month of 2018/05  
`2018/05 for 2 months` | within the entire months of 2018/05 and 2018/06  
`2018/05/10 05:00 for 5 hours` | from 2018/05/10 05:00:00 through 2018/05/10 09:59:59  
`2018/05/10 for 5 months` | from 2018/05/10 00:00:00 through 2018/10/09 23:59:59  
`2018` | entire year of 2018 (2018/01/01 00:00:00 through 2018/12/31 23:59:59)  
`FY2018` | entire fiscal year starting in 2018 (if your Looker developers have specified that your fiscal year starts in April then this is 2018/04/01 00:00 through 2019/03/31 23:59)  
`FY2018-Q1` | first quarter of the fiscal year starting in 2018 (if your Looker developers have specified that your fiscal year starts in April then this is 2018/04/01 00:00:00 through 2018/06/30 23:59:59)  
### Relative dates
Relative date filters allow you to create queries with rolling date values relative to the current date. These are useful when creating queries that update each time you run the query.
For all of the following examples, assume today is **Friday, 2018/05/18 18:30:02**. In Looker, weeks start on Monday unless you change that setting with `week_start_day`.
#### Seconds
Example | Description  
---|---  
`1 second` | the current second (2018/05/18 18:30:02)  
`60 seconds` | 60 seconds ago for 60 seconds (2018/05/18 18:29:02 through 2018/05/18 18:30:01)  
`60 seconds ago for 1 second` | 60 seconds ago for 1 second (2018/05/18 18:29:02)  
#### Minutes
Example | Description  
---|---  
`1 minute` | the current minute (2018/05/18 18:30:00 through 18:30:59)  
`60 minutes` | 60 minutes ago for 60 minutes (2018/05/18 17:31:00 through 2018/05/18 18:30:59)   
`60 minutes ago for 1 minute` | 60 minutes ago for 1 minute (2018/05/18 17:30:00 through 2018/05/18 17:30:59)  
#### Hours
Example | Description  
---|---  
`1 hour` | the current hour (2018/05/18 18:00 through 2018/05/18 18:59)  
`24 hours` | the same hour of day that was 24 hours ago for 24 hours (2018/05/17 19:00 through 2018/05/18 18:59)   
`24 hours ago for 1 hour` | the same hour of day that was 24 hours ago for 1 hour (2018/05/17 18:00 until 2018/05/17 18:59)  
#### Days
Example | Description  
---|---  
`today` | the current day (2018/05/18 00:00 through 2018/05/18 23:59)  
`2 days` | all of yesterday and today (2018/05/17 00:00 through 2018/05/18 23:59)  
`1 day ago` | just yesterday (2018/05/17 00:00 until 2018/05/17 23:59)  
`7 days ago for 7 days` | the last complete 7 days (2018/05/11 00:00 until 2018/05/17 23:59)  
`today for 7 days` | the current day, starting at midnight, for 7 days into the future (2018/05/18 00:00 until 2018/05/24 23:59)  
`last 3 days` | 2 days ago through the end of the current day (2018/05/16 00:00 until 2018/05/18 23:59)  
`7 days from now` | 7 days in the future (2018/05/18 00:00 until 2018/05/25 23:59)  
#### Weeks
Example | Description  
---|---  
`1 week` | top of the current week going forward (2018/05/14 00:00 through 2018/05/20 23:59)  
`this week` | top of the current week going forward (2018/05/14 00:00 through 2018/05/20 23:59)  
`before this week` | anytime until the top of this week (before 2018/05/14 00:00)  
`after this week` | anytime after the top of this week (2018/05/14 00:00 and later)  
`next week` | the following Monday going forward 1 week (2018/05/21 00:00 through 2018/05/27 23:59)  
`2 weeks` | a week ago Monday going forward (2018/05/07 00:00 through 2018/05/20 23:59)  
`last week` | synonym for "1 week ago"  
`1 week ago` | a week ago Monday going forward 1 week (2018/05/07 00:00 through 2018/05/13 23:59)  
#### Months
Example | Description  
---|---  
`1 month` | the current month (2018/05/01 00:00 through 2018/05/31 23:59)  
`this month` | synonym for "0 months ago" (2018/05/01 00:00 through 2018/05/31 23:59)  
`2 months` | the past two months (2018/04/01 00:00 through 2018/05/31 23:59)  
`last month` | all of 2018/04  
`2 months ago` | all of 2018/03  
`before 2 months ago` | all time before 2018/03/01  
`next month` | all of 2018/06  
`2 months from now` | all of 2018/07  
`6 months from now for 3 months` | 2018/11 through 2019/01  
#### Quarters
Example | Description  
---|---  
`1 quarter` | the current quarter (2018/04/01 00:00 through 2018/06/30 23:59)  
`this quarter` | synonym for "0 quarters ago" (2018/04/01 00:00 through 2018/06/30 23:59)  
`2 quarters` | the past two quarters (2018/01/01 00:00 through 2018/06/30 23:59)  
`last quarter` | all of Q1 (2018/01/01 00:00 through 2018/03/31 23:59)  
`2 quarters ago` | all of Q4 of last year (2017/010/01 00:00 through 2017/12/31 23:59)  
`before 2 quarters ago` | all time before Q4 of last year  
`next quarter` | all of the following quarter (2018/07/01 00:00 through 2018/09/30 23:59)  
`2018-07-01 for 1 quarter` | all of Q3 (2018/07/01 00:00 through 2018/09/30 23:59)  
`2018-Q4` | all of Q4 (2018/10/01 00:00 through 2018/12/31 23:59)  
#### Years
Example | Description  
---|---  
`1 year` | all of the current year (2018/01/01 00:00 through 2018/12/31 23:59)  
`this year` | all of the current year (2018/01/01 00:00 through 2018/12/31 23:59)  
`next year` | all of the following year (2019/01/01 00:00 through 2019/12/31 23:59)  
`2 years` | the past two years (2017/01/01 00:00 through 2018/12/31 23:59)  
`last year` | all of 2017  
`2 years ago` | all of 2016  
`before 2 years ago` | all time before 2016/01/01 (does not include any days between 2016/01/01 and 2016/05/18)  
## Boolean
Filtering on true or false type values in Looker requires you to know what type of true or false value you're interacting with.
Example | Description  
---|---  
`yes` or `Yes` | field evaluates to true`type: yesno` dimensions use lowercase, for `filters` parameters (like those used in a measure or used in an `always_filter`) use uppercase  
`no` or `No` | field evaluates to false`type: yesno` dimensions use lowercase, for `filters` parameters (like those used in a measure or used in an `always_filter`) use uppercase  
`TRUE` | field contains true (for fields that contain Boolean database values)  
`FALSE` | field contains false (for fields that contain Boolean database values)  
## Number
Filters on numbers support both natural language expressions (for example, `3 to 10`) and relational operators (for example, `>20`). Looker supports the `OR` operator to express multiple filter ranges (for example, `3 to 10 OR 30 to 100`). The `AND` operator can be used to express numeric ranges with relational operators (for example, `>=3 AND <=10`) to specify a range. Filters on numbers can also use algebraic interval notation to filter numeric fields.
Example | Description  
---|---  
is exactly 5  
`NOT 5` | is any value but exactly 5  
`1, 3, 5, 7` | is one of the values 1, 3, 5, or 7, exactly  
`NOT 66, 99, 4` | is not one of the values 66, 99, or 4, exactly  
` >1 AND <100, NOT 2` | is greater than 1 and less than 100, is not 2  
`NOT >1, 2, <100` | is less than or equal to 1, is not 2, and is greater than or equal to 100 (Looker recognizes that this is an impossible condition, and will instead write the SQL `IS NULL`)  
`5, NOT 6, NOT 7` | is 5, is not 6 or 7  
`5.5 to 10` | is 5.5 or greater but also 10 or less  
`NOT 3 to 80.44` | is less than 3 or greater than 80.44  
`1 to` | is 1 or greater  
`to 10` | is 10 or less  
`>10 AND <=20 OR 90` | is greater than 10 and less than or equal to 20, or is 90 exactly  
`>=50 AND <=100 OR >=500 AND <=1000` | is between 50 and 100, inclusive, or between 500 and 1000, inclusive  
`NULL` | has no data in it (when it is used as part of a LookML filter expression, place `NULL` in quotes, as shown on the `filters` documentation page)  
`NOT NULL` | has some data in it (when it is used as part of a LookML filter expression, place `NOT NULL` in quotes, as shown on the `filters` documentation page)  
`(1, 7)` | interpreted as **1 < x < 7** where the endpoints aren't included. While this notation resembles an ordered pair, in this context it refers to the interval upon which you are working.  
`[5, 90]` | interpreted as **5 <= x <= 90** where the endpoints are included  
`(12, 20]` | interpreted as **12 < x <= 20** where **12** is not included, but **20** is included  
`[12, 20)` | interpreted as **12 <= x < 20** where **12** is included, but **20** is not included  
`(500, inf)` | interpreted as **x > 500** where **500** is not included and infinity is always expressed as being "open" (not included). `inf` may be omitted and `(500, inf)` may be written as **(500,)**  
`(-inf, 10]` | interpreted as **x <= 10** where **10** is included and infinity is always expressed as being "open" (not included). `inf` may be omitted and `(-inf, 10]` may be written as **(,10]**  
`[0,9],[20,29]` | the numbers between 0 and 9 inclusive or 20 to 29 inclusive  
`[0,10],20` | 0 to 10 inclusive or 20  
`NOT (3,12)` | interpreted as **x < 3** and **x > 12**  
## Location
Location filter expressions are based on latitude and longitude, but can accept some natural language to define boxes and circles within which to limit a search.
Example | Description  
---|---  
`36.97, -122.03` | location is exactly at latitude 36.97, longitude 122.03  
`40 miles from 36.97, -122.03` | location is within 40 miles of latitude 36.97, longitude -122.03  
`inside box from 72.33, -173.14 to 14.39, -61.70` | location is within a box whose northwest corner is at latitude 72.33, longitude -173.14, and whose southeast corner is at latitude 14.39, longitude -61.70  
`NOT NULL (works the same as -NULL)` | location has both a non-null latitude and a non-null longitude (when it is used as part of a LookML filter expression, place `NOT NULL` in quotes, as shown on the `filters` documentation page)  
`-NULL (works the same as NOT NULL)` | location has both a non-null latitude and a non-null longitude (when it is used as part of a LookML filter expression, place `-NULL` in quotes, as shown on the `filters` documentation page)  
`NULL` | location has a null latitude, or a null longitude, or both are null (when it is used as part of a LookML filter expression, place `NULL` in quotes, as shown on the `filters` documentation page)  
### Supported units of measurement
To filter in an area around a certain location, you can use these units:
  * Meters
  * Feet
  * Kilometers
  * Miles


Singular units of measurement aren't supported. For example, filtering for a one-mile radius should be written `within 1 miles of 36.97, -122.03`.
## User Attribute Values
To use the value of a user attribute in a filter expression, reference the user attribute with the `_user_attributes` Liquid variable using the syntax that is required by your database dialect:
```
{{ _user_attributes['name_of_attribute'] }}

```

For example, suppose you need to apply an `sf_` prefix to the value of the `salesforce_username` user attribute because that is how the values are stored in your database. To add the prefix to the user attribute value, you can add a **matches (advanced)** filter on the relevant field and use the `_user_attributes` Liquid variable in the filter expression as follows:
```

sf_{{_user_attributes['salesforce_username']}}


```

You can use the same pattern to insert user attributes into LookML dashboard filters and dashboard element filters.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


