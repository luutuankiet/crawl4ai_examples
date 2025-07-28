# Elite System Activity  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/elite-system-activity

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Refresh intervals




Was this helpful?
Send feedback 
#  Elite System Activity
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Refresh intervals


## Benefits
Elite System Activity includes an analytical store for System Activity data that provides the following benefits:
  * System Activity Explores and dashboards remain the same, so the process of viewing System Activity data is no different.
  * More System Activity data can be stored. System Activity data can be retained for up to 1 year.
  * System Activity queries are offloaded from the Looker instance, which improves System Activity query performance and may improve Looker's performance. Elite System Activity also removes the concurrent query limit on System Activity Explores and dashboards along with the forced 12-hour caching policy for System Activity Explores and dashboards.


## Refresh intervals
The following tables refresh every 10 minutes:
  * `event`
  * `event_attribute`
  * `history`
  * `pdt_event_log`
  * `query`
  * `query_api_client_context`
  * `query_metrics`
  * `sql_text`


The `user` table refreshes once an hour.
The following tables refresh every 24 hours:
  * `access_token`
  * `api_usage`
  * `compliance_user_permissions`
  * `content_metadata`
  * `content_usage`
  * `dashboard`
  * `dashboard_element`
  * `dashboard_layout`
  * `dashboard_layout_component`
  * `db_connection`
  * `field_usage`
  * `group`
  * `group_group`
  * `group_user`
  * `look`
  * `merge_query`
  * `merge_query_source_query`
  * `model_set`
  * `node`
  * `permission_set`
  * `result_maker`
  * `role`
  * `role_group`
  * `role_user`
  * `scheduled_job`
  * `scheduled_job_stage`
  * `scheduled_plan`
  * `scheduled_plan_destination`
  * `session`
  * `slug`
  * `space`
  * `space_user`
  * `sql_query`
  * `user_attribute`
  * `user_facts`
  * `user_facts_role`


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


