# Setting alerts based on time series data  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-set-alerts-based-on-time-series-data

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Setting alerts based on time series data
Stay organized with collections  Save and categorize content based on your preferences. 
You can create an alert to send an email or a Slack notification whenever the results from a query-based or Look-linked dashboard tile meet or exceed a specified threshold. Setting an alert based on time series data differs from setting an alert based on other data types. 
For time series data, the alert condition is based on comparing specific rows in the series rather than being based on the complete result set. Working this way with time series data lets users perform additional operations that compare data from two rows in the series using additional alert condition options that are not available to other data types, such as **changes by** , **increases by** , and **decreases by**. 
When using these comparison conditions with time series data, the alert query compares the latest row of data with its previous row. To keep track of where you are in the time series — in order to base alert conditions only on data that wasn't there the previous time the alert query was run — Looker must persist the value of the latest time series data every time it runs the alert query. 
This page describes two important cases to consider when you choose alert conditions that use time series data: 
  1. The alert conditions tell Looker to check the data for updates less frequently than the data is updated.
     * For example, the time series interval is hourly (the data is aggregated by the hour), but an alert is set for a daily frequency. 
  2. The alert conditions tell Looker to check the data for updates more frequently than the data is updated.
     * For example, the time series interval is daily (the data is aggregated by day), but an alert is set for an hourly frequency. 

Both cases depend on the relationship between the shortest interval between the time series rows (time series interval) and how often the alert query is run (frequency). The frequency is the amount of time between scheduled alert queries, and is set by the alert creator. 
> Ideally, the time series interval and frequency are the same; however, that is not always the case. If an ETL job is configured to load hourly data every night, or a query fails for some reason, it's important to understand how alert queries work when these intervals are not synchronized. 
## Alert checking
Alert queries will check the latest row of time series data to determine whether either of the following is true: 
  * If the current time series value is more recent than the most recent time series value from the previous alert check
  * If the current time series value is the most recent time series value in the time series, even if it has the same time series value as from the previous alert check


The first time an alert query is run, Looker will no longer evaluate the entire result set. Instead, Looker will consider those results as historical data and only look for changes that occur after the alert is created and the initial alert query is run. 
## Case 1: The time series interval is shorter than the frequency
In this example, a user wants to check daily whether the hourly sales are greater than the goal: 
**Time series interval = hourly Frequency = daily**
This approach involves checking hourly data with a frequency that is greater than an hour. The alert will check every new time series row that wasn't checked in the previous alert interval. In the case where you have hourly data and a daily alert check, the alert will check 24 rows every day. Each row is checked against the specified alert condition, and if _any_ row fulfills the condition, an email will be sent. 
### Run 5/25/19 9:00 AM
Time series value | Measure value  
---|---  
5/25/19 8:00 AM | 200 | < alert check  
5/25/19 9:00 AM | 250 | < alert check  
### Run 5/25/19 11:00 AM
Time series value | Measure value  
---|---  
5/25/19 8:00 AM | 200  
5/25/19 9:00 AM | 250 | < previous alert  
5/25/19 10:00 AM | 300 | < alert check  
5/25/19 11:00 AM | 300 | < alert check  
### Run 5/25/19 12:00 PM (no new data)
Time series value | Measure value  
---|---  
5/25/19 8:00 AM | 200  
5/25/19 9:00 AM | 250  
5/25/19 10:00 AM | 300 | < previous alert  
5/25/19 11:00 AM | 300 | < alert check  
## Case 2: The time series interval is longer than the frequency
In this example, a user wants to check hourly whether today's cumulative sales totals are greater than the goal: 
**Time series interval = daily Frequency = hourly**
This approach involves checking data that is aggregated by **date** many times throughout the day. Let's say that you've set up an alert to notify you if the daily sales total equals or exceeds 200. The sales total is increasing during each alert check as it accumulates throughout the day, so Looker continually rechecks the latest time series value against the value that triggered the previous alert. 
### Run 5/25/19 9:00 AM
Time series value | Measure value  
---|---  
5/24/19 | 200 | < previous alert  
5/25/19 | 50 | < alert check (no notification)  
### Run 5/25/19 10:00 AM
Time series value | Measure value  
---|---  
5/24/19 | 200 | < previous alert  
5/25/19 | 100 | < alert check (no notification)  
### Run 5/25/19 11:00 AM
Time series value | Measure value  
---|---  
5/24/19 | 200 | < previous alert  
5/25/19 | 150 | < alert check (no notification)  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


