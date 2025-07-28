# System Activity pages  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/system-activity-pages

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  System Activity pages
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
System Activity is an internal LookML model that connects to Looker's underlying application database. System Activity Explores and dashboards that are built upon this model show information about your Looker instance, which includes the following:
  * All Looks and dashboards that are saved on your instance
  * User and historical query information
  * Instance performance statistics


Both the granularity and retention of System Activity data are subject to system constraints. System Activity is designed for collecting high-volume data, and aggregating it can be used to supplement your business logs.
> This data can be useful for supplementing monitoring and auditing activities, but is not intended to replace your current compliance strategy.
> The text in filters run by users is accessible in System Activity and can be viewed by any user who has permission to view the System Activity model.
> **Take action** : Modify who has view access to the System Activity models. Looker admins have access to System Activity by default. A Looker admin can grant access to System Activity to a non-admin user by giving the user the `see_system_activity` permission.
System Activity includes the following elements:
  * System Activity dashboards: Looker-created dashboards showing usage and performance information about the Looker instance. You can download, schedule, set alerts on, and drill into metrics and elements just like on any other dashboard. Data in the System Activity dashboards is updated and cached every 12 hours.
  * System Activity Explores: Using System Activity Explores, you can create your own Looks and dashboards to monitor and analyze your Looker instance. See the System Activity Explores page for a list of Explores and their cache rules.
  * System Activity for Looker reports: If the Looker reports feature is enabled on your Looker instance, System Activity dashboards and Explores include information about the Looker reports that are saved on your Looker instance.
  * Elite System Activity: An optional analytical store that increases System Activity performance and storage limits. Elite System Activity is a paid feature on Looker (original), and is a standard feature on the **Enterprise** and **Embed** editions of Looker (Google Cloud core).
  * Read replica option: For customer-hosted instances only, this method increases System Activity performance and provides longer System Activity data retention.
  * Understanding PDT log actions: Use the **PDT Event Log** Explore to view and understand PDT log actions and their corresponding action data.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


