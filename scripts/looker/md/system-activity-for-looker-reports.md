# Monitoring Looker reports with System Activity  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/system-activity-for-looker-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
    * Required roles and permissions
    * Key considerations and limitations
  * System Activity dashboards
    * User Activity dashboard
    * Content Activity dashboard
  * System Activity Explores




Was this helpful?
Send feedback 
#  Monitoring Looker reports with System Activity
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
    * Required roles and permissions
    * Key considerations and limitations
  * System Activity dashboards
    * User Activity dashboard
    * Content Activity dashboard
  * System Activity Explores


System Activity is an internal LookML model that connects to Looker's underlying application database. System Activity Explores and dashboards that are built upon this model show information about your Looker instance, which includes the following:
  * All Looks and dashboards that are saved on your instance
  * User and historical query information
  * Instance performance statistics


Both the granularity and retention of System Activity data are subject to system constraints. System Activity is designed for collecting high-volume data, and aggregating it can be used to supplement your business logs.
When the Looker reports feature is enabled on your Looker instance, System Activity dashboards and Explores also include information about the Looker reports that are saved on your Looker instance. This information includes individual report usage data, as well as details about users who have created or accessed reports.
## Before you begin
Understand the required roles and permissions and the key considerations and limitations of using System Activity.
### Required roles and permissions
To access System Activity Explores and dashboards, you must have the `see_system_activity` permission, or you must have the Admin Looker role. Looker admins have access to System Activity by default.
### Key considerations and limitations
Be aware of the following considerations and limitations when using System Activity:
  * System Activity doesn't provide information about reports on private IP Looker (Google Cloud core) instances.
  * The text in filters that are run by users is accessible in System Activity and can be viewed by any user who has permission to view the System Activity model.
  * Looker admins can modify who has view access to the System Activity model. Looker admins have access to System Activity by default. A Looker admin can grant access to System Activity to a non-admin user by giving the user the `see_system_activity` permission.
  * System Activity dashboards and Explores are restricted in the number of concurrent queries that can be run. This restriction may increase loading times for System Activity Explores.
  * Time-based data in System Activity is stored in the Looker System time zone. See the Using time zone settings for more information.
  * It is not possible to query System Activity data using SQL Runner, as permissions for Looker's internal database are limited.
  * By default, System Activity data is stored in Looker's internal database. Most tables are truncated on a regular schedule to comply with storage limits. For example, the History table is truncated to the past 90 days of data. Some tables have more stringent data retention policies. To increase data retention, consider using Elite System Activity.


## System Activity dashboards
The **System Activity** section of the Looker **Admin** menu displays built-in dashboards that show usage and performance information about your Looker instance. You can download, schedule, set alerts on, and drill into metrics and elements just like on any other dashboard. Data in the System Activity dashboards is updated and cached every 12 hours.
When the Looker reports feature is enabled on your instance, the following System Activity dashboards also display information about Looker reports on your instance, as well as information about report creators and users:
  * User Activity dashboard
  * Content Activity dashboard


### User Activity dashboard
The **User Activity** dashboard shows information about your users and their usage of your Looker instance.
If the Looker reports feature is enabled on your instance, the **User Activity** dashboard includes additional details about report usage on your Looker instance.
In the **About Your Users** section of the **User Activity** dashboard, the **Top Report Builders** tile shows the users that created the most new reports in the last seven days.
### Content Activity dashboard
The **Content Activity** dashboard shows information about the dashboards, Looks, Explores, and reports that are being viewed and scheduled on your Looker instance.
If the Looker reports feature is enabled on your instance, the **Content Activity** dashboard includes the following additional details about reports, report usage, and report users and creators on your Looker instance:
  * The **Content Usage** section of the **Content Activity** dashboard includes the following additional tiles: 
    * **Total Reports** tile: Shows the total number of reports on your instance that have not been deleted.
    * **Reports Usage** tile: Shows the percentage of reports that have and that have not been used over the last 30 days.
  * In the **Popular Content and Explores** section of the **Content Activity** dashboard, the **Popular Content** tile includes details about reports. The **Content Type** field, which is used in the **Popular Content** tile, includes a `report` value. This lets you see information about reports, including the report's title, view total, embed total, API total, favorites total, and schedule total over the last 30 days.


## System Activity Explores
Looker admins and users who have been granted the `see_system_activity` permission have access to Looker's System Activity Explores in the **Explore** menu.
When you have enabled the Looker reports feature on your Looker instance, in addition to the standard System Activity Explores, you can use the **Report** Explore to analyze data about report usage.
The **Report** Explore includes details about Looker reports, including information about report creation date and last updated date, whether reports have been moved to trash, and details about report users and creators. The cache duration for the **Report** Explore is 12 hours.
See Using the System Activity Explores for some examples of common uses for System Activity Explores.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


