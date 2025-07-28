# week_start_day  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-week-start-day

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page




Send feedback 
#  week_start_day
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
```
week_start_day: monday

```

Hierarchy `week_start_day` |  Default Value `monday`Accepts A day of the week (`monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, or `sunday`)   
---|---  
## Definition
You can adjust the day that Looker considers to be the start of a week with the `week_start_day` parameter. Using `week_start_day` affects:
  * The way that data appears in your tables
  * The sort order of the tables
  * The operation of filters


The `week_start_day` parameter works with three of the four week-related `timeframes`:
timeframe | Works with `week_start_day`?  
---|---  
`day_of_week_index` | Yes  
`week` | Yes  
`day_of_week` | Yes  
`week_of_year`  
`week_start_day` does not work with `week_of_year` because that timeframe is based on the ISO standard, which uses Monday weeks.
## Examples
Adjust weeks to start on Sunday instead of Monday:
```
week_start_day: sunday

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


