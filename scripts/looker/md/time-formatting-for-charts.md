# Time formatting for charts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/time-formatting-for-charts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Time label expressions




Was this helpful?
Send feedback 
#  Time formatting for charts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Time label expressions


If your chart has a time dimension on the x-axis, you can change the formatting of the x-axis label by using the **Time Label Format** setting in the **X** tab of the visualization options.
## Time label expressions
You can format time values in Looker charts by using the syntax in the following table.
Format Type | Description | Expression  
---|---|---  
**Time**  
Time | Milliseconds as a decimal number: 000 to 999  
Time | Second as a two-digit number: 00 to 59  
Time | Minute as a two-digit number: 00 to 59  
Time | Hour as a decimal number (24-hour clock): 00 to 23  
Time | Hour as a decimal number (12-hour clock): 01 to 12  
Time | Either AM or PM  
**Date**  
Date | Day of the year as a decimal number: 001 to 366  
Date | Zero-padded day of the month: 01 to 31  
Date | Space-padded day of the month (equivalent to `%_d`): 1 to 31  
Date | Full weekday name: Monday, Tuesday, Wednesday  
Date | Abbreviated weekday name (3-letter): Mon, Tue, Wed  
Date | Weekday as a decimal number (Sunday as the first day of the week): 0 to 6  
**Week**  
Week | Week number of the year (Sunday as the first day of the week) as a two-digit number: 00 to 53 **Note** : `%U` uses the ISO week date standard offset by one day.  
Week | Week number of the year (Monday as the first day of the week) as a two-digit number: 00 to 53 **Note** : `%W` uses the ISO week date standard.  
**Month**  
Month | Two-digit month: 01 through 12 (1-12 format not supported)  
Month | Abbreviated month name: Jan, Feb, Mar   
Month | Full month name: January, February, March   
**Year**  
Year | Two-digit year: 00 to 99  
Year | Four-digit year: 2000, 2001, 2002  
**Combination**  
Combination | Full time, of the form "%H:%M:%S": 23:56:12  
Combination | Full date, of the form "%m/%d/%Y": 01/27/2014  
Combination | Datetime format with the following: "%a %b %e %H:%M:%S %Y": Mon Jan 1 23:56:04 2014  
## Examples
You can combine expressions together to create custom time formats, such as in the examples in the following table.
Input | Time Label Format | Output  
---|---|---  
August 14, 2014 10:31 PM | `%b '%y, %H:%M` | Aug '14, 22:31  
August 14, 2014 10:31 PM | `%B %Y, %I:%M %p` | August 2014, 10:31 PM  
August 14, 2014 10:31 PM | `%x %X` | 08/14/2014 22:31:00  
August 14, 2014 10:31 PM | `%I:%M:%S %p` | 10:31:00 PM  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


