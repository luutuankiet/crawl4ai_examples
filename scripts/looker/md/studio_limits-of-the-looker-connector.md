# Overview of Looker connector requirements, limits, feature support, and troubleshooting  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/limits-of-the-looker-connector

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Looker instance requirements
  * Limits of the Looker connector
  * Support of Looker Studio features
  * Report a problem




Was this helpful?
Send feedback 
#  Overview of Looker connector requirements, limits, feature support, and troubleshooting
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Looker instance requirements
  * Limits of the Looker connector
  * Support of Looker Studio features
  * Report a problem


This page covers the following topics about the Looker connector in Looker Studio:
  * Required configurations for each type of Looker instance
  * Limits of the Looker connector
  * Unsupported or partially supported Looker Studio features
  * Troubleshooting guidance
  * How to report a problem to the Support team


## Looker instance requirements
To set up a Looker data source by using the Looker connector in Looker Studio, first verify that your Looker instance meets the following requirements:
  * The instance must be Looker-hosted. **The Looker Studio connector is not available for customer-hosted Looker instances.**
  * The **Looker Studio** BI connector must be enabled in the **Platform** section of the Looker instance's **Admin** panel.
  * Looker (original) instances that have the **Enable IP Allowlist** setting enabled may require additional configuration. Contact Support for assistance.
  * Looker (original) instances must meet the following version requirements:
Hosting provider |  Minimum Looker version   
---|---  
AWS, Azure | 23.4  
Google Cloud | 22.16  
  * The Looker connector can connect to a Looker (Google Cloud core) private IP (private services access) instance that is on the same network as Looker Studio from Looker Studio Pro or Looker reports using the Looker instance ID. For more information, see the Connecting to a private IP instance from Looker Studio Pro or Looker reports documentation page.
  * The Looker connector, when used with Looker Studio Pro or Looker reports, can't connect to a Looker (Google Cloud core) instance that is inside of a VPC Service Controls perimeter.
  * Some tasks that are performed on reports that are built with the Looker connector require additional permissions, which are granted within Looker. For more information, see Overview of Looker connector permissions.


## Limits of the Looker connector
The Looker connector exhibits the following limitations, which may restrict the types of Looker instances and models that you can connect to:
  * The Looker connector cannot connect to customer-hosted Looker instances.
  * Exceptionally large Looker models (generally those that have more than 100 Explores) may cause long delays or timeouts during the data source creation process.
  * There is a 5-minute query timeout. Results from queries that are run on Looker data sources are limited to a maximum of 5,000 rows.
  * Data downloads are limited to 5,000 rows.


## Support of Looker Studio features
Looker data sources may not support or may only partially support the following Looker Studio features:
  * Number of fields: You can include up to 100 dimensions and up to 100 metrics in a table visualization.
  * Data downloads, schedules, alerts, and exports: 
    * Downloads, schedules, alerts, and data exports aren't supported for reports that are built using Looker data from a Looker (Google Cloud core) instance that uses a private IP network connection or that is configured to use a Virtual Private Cloud (VPC) IP address. To learn more about Looker (Google Cloud core) instance networking, see the Looker (Google Cloud core) networking options documentation.
    * Downloads, schedules, alerts, and data exports aren't supported for reports that are built using Looker data from a Looker (original) instance that is configured to use an IP allowlist.
  * Calculated fields: Available in Preview, data sources that are created with the Looker connector support some Looker Studio functions for calculated fields. These functions can be applied on dimensions only. 
#### Supported functions for calculated fields
Name | Type | Description | Syntax  
---|---|---|---  
`ABS` | Arithmetic | Returns the absolute value of number. Learn more. | `ABS(X)`  
`ACOS` | Arithmetic | Returns the inverse of the cosine of X. Learn more. | `ACOS(X)`  
`ASIN` | Arithmetic | Returns the inverse of the sine of X. Learn more. | `ASIN(X)`  
`ATAN` | Arithmetic | Returns the inverse of the tangent of X. Learn more. | `ATAN(X)`  
`AVG` | Aggregation | Returns the average of all values of X. Learn more. | `AVG(X)`  
`CASE (Simple)` | Conditional | Compares `input_expression` to `expression_to_match` of each successive WHEN clause and returns the first `result` where this comparison returns `true`. Learn more. | ```
    CASE input_expression
    WHEN expression_to_match THEN result
    [WHEN expression_to_match THEN result]
    [...]
    [ELSE result]
    END
```
  
`CASE` | Conditional | Evaluates the `condition` of each successive WHEN clause and returns the first `result` where the `condition` is true; any remaining WHEN and ELSE clauses are not evaluated. If all conditions are false or NULL, returns `else_result` if present; if not present, returns `NULL`. Learn more. | ```
    CASE
    WHEN condition THEN result
    [WHEN condition THEN result]
    [...]
    [ELSE else_result]
    END
```
  
`CAST` | Miscellaneous | Cast field or expression into TYPE. Aggregated fields are not allowed inside CAST.`TYPE` can be `NUMBER`, `TEXT`, or `DATETIME`. Learn more. | `CAST(_field_expression_ AS _TYPE_)`  
`CEIL` | Arithmetic | Returns the nearest integer greater than X. For example, if the value of X is v, `CEIL(X)` is greater than or equal to v. Learn more. | `CEIL(X)`  
`COALESCE` | Conditional | Returns the first non-missing value found in a list of fields. Learn more. | `COALESCE(field_expression[,field_expression, ...])`  
`CONCAT` | Text | Returns a text that is the concatenation of X and Y. Learn more. | `CONCAT(X, Y)`  
`CONTAINS_TEXT` | Text | Returns true if _X_ contains text, otherwise returns false. Case-sensitive. Learn more. | `CONTAINS_TEXT(X, text)`  
`COS` | Arithmetic | Returns the cosine of X. Learn more. | `COS(X)`  
`COUNT_DISTINCT` | Aggregation | Returns the number of unique values of X. Learn more. | `COUNT_DISTINCT(X)`  
`CURRENT_DATE` | Date | Returns the current date as of the default timezone. Learn more. | `CURRENT_DATE()`  
`CURRENT_DATETIME` | Date | Returns the current date and time as of the default timezone. Learn more. | `CURRENT_DATETIME()`  
`DATE` | Date | Constructs a `Date` field or value from numbers or from a `Date & Time` field or expression. Learn more. | `DATE(year, month, day)`  
`DATE_DIFF` | Date | Returns the difference in days between X and Y (X - Y). Learn more. | `DATE_DIFF(X, Y)`  
`DATE_FROM_UNIX_DATE` | Date | Interprets an integer as the number of days since 1970-01-01. Learn more. | `DATE_FROM_UNIX_DATE(integer)`  
`DATETIME` | Date | Constructs a Date & Time field or value from numbers. Learn more. | `DATETIME(year, month, day, hour, minute, second)`  
`DATETIME_ADD` | Date | Adds a specified time interval to a date. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. Learn more. | `DATETIME_ADD(datetime_expression, INTERVAL integer part)`  
`DATETIME_DIFF` | Date | Returns the number of part boundaries between two dates. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. Learn more. | `DATETIME_DIFF(date_expression, date_expression, part)`  
`DATETIME_SUB` | Date | Subtracts a specified time interval from a date. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. Learn more. | `DATETIME_SUB(datetime_expression, INTERVAL integer part)`  
`DATETIME_TRUNC` | Date | Truncates a date to the specified granularity. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. Learn more. | `DATETIME_TRUNC(date_expression, part)`  
`DAY` | Date | Returns the day of a Date or Date & Time. Learn more. | `Day(date_expression)`  
`EXTRACT` | Date | Returns part of a date or date & time. Accepted `part` values include `DAY`, `MONTH`, `YEAR`. Learn more. | `EXTRACT(part FROM date_expression)`  
`FLOOR` | Arithmetic | Returns the nearest integer less than X. For example, if the value X is v, `FLOOR(X)` is equal to or less than v. Learn more. | `FLOOR(X)`  
`HOUR` | Date | Returns the hour of a date and time. Learn more. | `HOUR(datetime_expression)`  
Conditional | If `condition` is true, returns `true_result`, else returns `false_result`. `false_result` is not evaluated if `condition` is true. `true_result` is not evaluated if `condition` is false or NULL. Learn more. | `IF(condition, true_result, false_result)`  
`IFNULL` | Conditional | Returns a result if the input is null, otherwise, returns the input. Learn more. | `IFNULL(input_expression, null_result)`  
`LEFT_TEXT ` | Text | Returns a number of characters from the beginning of _X_. The number of characters is specified by _length_. Learn more. | `LEFT_TEXT(X, length)`  
`LENGTH` | Text | Returns the number of characters in _X_. Learn more. | `LENGTH(X)`  
`LOG` | Arithmetic | Returns the logarithm to base 2 of X. Learn more. | `LOG(X)`  
`LOG10` | Arithmetic | Returns the logarithm to base 10 of X. Learn more. | `LOG10(X)`  
`LOWER` | Text | Converts X to lowercase. Learn more. | `LOWER(X)`  
`MAX` | Aggregation | Returns the maximum value of X. Learn more. | `MAX(X)`  
`MEDIAN` | Aggregation | Returns the median of all values of X. Learn more. | `MEDIAN(X)`  
`MIN` | Aggregation | Returns the minimum value of X. Learn more. | `MIN(X)`  
`MINUTE` | Date | Returns the minutes component of a given date and time. Learn more. | `MINUTE(datetime_expression)`  
`MONTH` | Date | Returns the month from a `Date & Time` value. Learn more. | `MONTH(date_expression)`  
`NULLIF` | Conditional | Returns `NULL` if the input matches an expression, otherwise returns the input. Learn more. | `NULLIF(input_expression, expression_to_match)`  
`POWER` | Arithmetic | Returns result of raising X to the power Y. Learn more. | `POWER(X, Y)`  
`REPLACE` | Text | Returns a copy of _X_ with all occurrences of _Y_ in _X_ replaced by _Z_. Learn more. | `REPLACE(X, Y, Z)`  
`RIGHT_TEXT ` | Text | Returns a number of characters from the end of _X_. The number of characters is specified by _length_. Learn more. | `RIGHT_TEXT(X, length)`  
`ROUND` | Arithmetic | Returns `X` rounded to `Y` precision digits. Learn more. | `ROUND(X, Y)`  
`SECOND` | Date | Returns the seconds component of a given date and time. Learn more. | `SECOND(datetime_expression)`  
`SIN` | Arithmetic | Returns the sine of X. Learn more. | `SIN(X)`  
`SQRT` | Arithmetic | Returns the square root of X. Note that X must be non-negative. Learn more. | `SQRT(X)`  
`SUBSTR` | Text | Returns a text that is a substring of _X_. The substring begins at _start index_ and is _length_ characters long. Learn more. | `SUBSTR(X, start index, length)`  
`SUM` | Aggregation | Returns the sum of all values of X. Learn more. | `SUM(X)`  
`TAN` | Arithmetic | Returns the tangent of X. Learn more. | `TAN(X)`  
`TODAY` | Date | Returns the current date as of the default timezone. Learn more. | `TODAY()`  
`UNIX_DATE` | Date | Returns the number of days since 1970-01-01. Learn more. | `UNIX_DATE(date_expression)`  
`UPPER` | Text | Converts _X_ to uppercase. Learn more. | `UPPER(X)`  
`YEAR` | Date | Returns the year of a given date. Learn more. | `YEAR(Date)`  


## Troubleshooting
Issue | Resolution  
---|---  
Looker Studio displays the following error message: "_Authorization Required_" | Authorize the Looker connector to link any necessary accounts, as described in the View and interact with Looker data on a Looker Studio documentation.  
Looker Studio displays an HTTP 400 error | 
  * Confirm that the **Looker Studio** BI connector is enabled in the Looker instance.
  * Confirm that account linking was successful.

  
Looker Studio displays the following error message: "_Cannot connect to a Looker instance_" | 
  * Confirm that the Looker instance URL is correct and that there are no trailing spaces.
  * The Looker connector is valid only for specific configurations and versions of Looker instances.
  * Looker (original) instances that have the **Enable Allowlist** feature enabled may require special setup — Contact Support.
  * Confirm that the API Host URL in the Looker instance is configured properly.

  
Looker Studio displays the following error message: "_No Explores found_" | Select a different Looker model.  
Existing report charts are broken | 
  * Confirm that the Looker Studio connector is enabled in the Looker instance.
  * Looker instances that have the **Enable Allowlist** feature enabled may require special setup — Contact Support.
  * Confirm that the API endpoint for the Looker instance is configured properly.

  
Looker Studio displays an error when trying to fetch Explore data |  Contact Support or visit the Looker Studio Community.   
Charts don't render on a downloaded report | Ask your Looker admin to grant you `download_with_limit` or `download_without_limit` permissions on the data source's (that is, the Looker Explore's) underlying LookML models. This permission is available only for Looker Studio Pro users.  
Charts don't render in the exported file | Ask your Looker admin to grant you `download_with_limit` or `download_without_limit` permissions on the data source's (that is, the Looker Explore's) underlying LookML models. This permission is available only for Looker Studio Pro users.  
Charts don't render in the scheduled report delivery | If you own the report delivery, you have insufficient Looker permissions to view at least one of the models that are referenced in the delivered report. Ask your Looker admin to grant you `schedule_look_emails` permissions on the data source's underlying LookML models. This permission is available only for Looker Studio Pro users.  
Looker Studio displays the following error when downloading a report: "_Due to lack of permissions, some charts using Looker models will not download. Ask your Looker admin to grant permissions._" | Ask your Looker admin to grant you `download_with_limit` or `download_without_limit` permissions on the report's underlying LookML models. This permission is available only for Looker Studio Pro users.  
Looker Studio displays the following error when scheduling a report delivery: "_Due to lack of permissions, some charts using Looker data will be missing from your scheduled report. Ask your Looker Admin to grant permissions._" | Ask your Looker admin to grant you `schedule_look_emails` permissions on the report's underlying LookML models. This permission is available only for Looker Studio Pro users.  
Looker Studio displays the following error on the list of report schedules: "_Some Looker data may be missing from your report deliveries. Ask your Looker admin to grant permissions to deliver all data in this report._" | Ask your Looker admin to grant you `schedule_look_emails` permissions on the report's underlying LookML models. This permission is available only for Looker Studio Pro users.  
## Report a problem
Report problems with the Looker connector to the Support team.
If you're a Looker Studio Pro customer and experience problems that are related to Looker Studio features other than the Looker connector, contact Cloud Customer Care.
If you're using the free version of Looker Studio, post your question or issue in the Looker Studio Community.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


