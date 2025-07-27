# Admin settings: Content guardrails  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Limit users from adding new Merged Results queries to dashboards
  * Limit users from executing existing Merged Results queries
  * Limit the automatic dashboard refresh option
  * Set a minimum refresh interval for autorefreshing dashboards and tiles globally




Was this helpful?
Send feedback 
#  Admin settings: Content guardrails
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Limit users from adding new Merged Results queries to dashboards
  * Limit users from executing existing Merged Results queries
  * Limit the automatic dashboard refresh option
  * Set a minimum refresh interval for autorefreshing dashboards and tiles globally


The **Content guardrails** page lets Looker admins:
  * Disable or set limits on merged results queries.
Merged results queries are calculated post-query processing. Excessive calculations can compete for Java memory on the Looker instance, causing the Looker instance to respond more slowly.
  * Limit the use of the dashboard autorefresh option.
Looker dashboards can also be configured to autorefresh, which refreshes the displayed data at automatic intervals. Each time a dashboard tile refreshes its data, the system generates and sends a query to the database. When a dashboard refreshes, the system generates queries for each tile on the dashboard. Frequent dashboard refreshes, especially on large dashboards, can significantly strain database systems and cause performance issues. Similarly, when multiple users access a dashboard with autorefresh enabled, performance might be impeded.


For more information and recommendations about building performant dashboards, see Considerations when building performant Looker dashboards.
The **Content guardrails** page has the following options:
  * Limit users from adding new Merged Results queries to dashboards
  * Limit users from executing existing Merged Results queries
  * Limit the automatic dashboard refresh option
  * Set a minimum refresh interval for autorefreshing dashboards and tiles globally


## Limit users from adding new Merged Results queries to dashboards
When you enable this option, Looker prevents users from saving new Merged Results queries to dashboards. Dashboards with existing Merged Results queries remain functional.
## Limit users from executing existing Merged Results queries
When you enable this option, Looker stops executing Merged Results queries and reports an error instead. Existing dashboards with Merged Results queries will report `No Results` and show an error for the corresponding elements. If Looker encounters these errors, Looker won't complete scheduled deliveries of dashboards that have Merged Results queries.
## Limit the automatic dashboard refresh option
When this option is enabled, only Looker admins can configure dashboards to autorefresh.
## Set a minimum refresh interval for autorefreshing dashboards and tiles globally
The **Limit the minimum refresh interval for auto-refreshing dashboards and tiles globally** field lets you set a minimum time interval for the dashboard autorefresh option. This setting applies to all dashboards in the Looker instance.
Any dashboards that are configured to autorefresh more frequently than the time interval in this field won't autorefresh any more frequently than the value that's configured in this field.
As an example, if you have a dashboard that is configured to autorefresh more frequently that your database ETL process occurs, then any time the dashboard refreshes before the next ETL occurs, the dashboard won't retrieve any new data. To prevent these unnecessary queries, you could use this field to set the minimum dashboard refresh time to match the time between your database ETL processes, so that when the dashboard refreshes, it will be retrieving new data.
To set a minimum time for dashboard autorefresh, select a time interval (seconds, minutes, hours, or days). Then, enter the number of the selected time interval that constitutes the minimum time between dashboard autorefreshes. After you enter the minimum time interval, click **Save**.
Set this field to **0** or leave it blank to enable unlimited dashboard autorefresh times.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


