# Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/yearweek

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Syntax
  * Related resources




Was this helpful?
Send feedback 
  * On this page
  * Syntax
  * Related resources


#  YEARWEEK
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the year and week number of a given date.
## Sample usage
`YEARWEEK(Date)`
## Syntax
The following syntaxe turns the year and week number from a Date value.
`YEARWEEK( date_expression )`
The following syntax returns the year and week number from a compatibility mode Date value.
`YEARWEEK( X [, format_string ])`
### Parameters
  * `date_expression` - a Date or Date & Time field or expression.
  * - a field or expression that evaluates to Text, Number, or compatibility mode Date.
  * `format_string` - format for . Optional if is correctly configured as a semantic date field.


#### Format strings for compatibility mode dates
Supported date functions accept the following input formats if `X` is a Text field or expression, or compatibility mode Date:
  * `BASIC`: %Y/%m/%d-%H:%M:%S
  * `DEFAULT_DASH`: %Y-%m-%d [%H:%M:%S]
  * `DEFAULT_SLASH`: %Y/%m/%d [%H:%M:%S]
  * `DEFAULT_DECIMAL`: %Y%m%d [%H:%M:%S]
  * `RFC_1123`: for example, Sat, 24 May 2008 20:09:47 GMT
  * `RFC_3339`: for example, 2008-05-24T20:09:47Z
  * `DECIMAL_DATE`: same as `DEFAULT_DECIMAL`


Any valid strptime format is accepted.
Supported time functions accept the following input format if `X` is a Number field or expression:
  * `SECONDS`: seconds since Epoch
  * `MILLIS`: milliseconds since Epoch
  * `MICROS`: microseconds since Epoch
  * `NANOS`: nanoseconds since Epoch
  * `JULIAN_DATE`: days since Epoch


## Examples
Example formula | Input | Output  
---|---|---  
` YEARWEEK(Date) ` |  Jan 1, 2019  |  201901   
` YEARWEEK(Date as Text, 'BASIC') ` |  2019/01/01-09:40:45  |  201901   
` YEARWEEK(Date as Number, 'SECONDS') ` |  1561784874  |  201926   
` YEARWEEK(Date as lots of Numbers, 'MILLIS') ` |  1562004058620  |  201927   
## Notes
This function works with both compatibility mode dates and upgraded Date and Date & Time data types.
## Related resources
  * About calculated fields
  * Looker Studio function list


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


