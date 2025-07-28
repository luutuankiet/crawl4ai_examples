# Get an alert  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Alert/get_alert

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get an alert
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Get an alert by a given alert ID
## Request
GET /alerts/{alert_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
alert_id
string 
ID of an alert
## Response
### 200: Alert
Datatype
Description
(object)
applied_dashboard_filters
AlertAppliedDashboardFilter[] 
Expand AlertAppliedDashboardFilter definition... 
filter_title
string 
Field Title. Refer to `DashboardFilter.title` in [DashboardFilter](#!/types/DashboardFilter). Example `Name`
field_name
string 
Field Name. Refer to `DashboardFilter.dimension` in [DashboardFilter](#!/types/DashboardFilter). Example `distribution_centers.name`
filter_value
string 
Field Value. [Filter Expressions](https://cloud.google.com/looker/docs/reference/filter-expressions). Example `Los Angeles CA`
filter_description
_lock_
string 
Human Readable Filter Description. This may be null or auto-generated. Example `is Los Angeles CA`
comparison_type
string 
This property informs the check what kind of comparison we are performing. Only certain condition types are valid for time series alerts. For details, refer to [Setting Alert Conditions](https://cloud.google.com/looker/docs/sharing-and-publishing/creating-alerts#setting_alert_conditions) Valid values are: "EQUAL_TO", "GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO", "LESS_THAN", "LESS_THAN_OR_EQUAL_TO", "INCREASES_BY", "DECREASES_BY", "CHANGES_BY".
cron
string 
Vixie-Style crontab specification when to run. At minimum, it has to be longer than 15 minute intervals
custom_url_base
string 
Domain for the custom url selected by the alert creator from the admin defined domain allowlist
custom_url_params
string 
Parameters and path for the custom url defined by the alert creator
custom_url_label
string 
Label for the custom url defined by the alert creator
show_custom_url
boolean 
Boolean to determine if the custom url should be used
custom_title
string 
An optional, user-defined title for the alert
dashboard_element_id
string 
ID of the dashboard element associated with the alert. Refer to [dashboard_element()](#!/Dashboard/DashboardElement)
description
string 
An optional description for the alert. This supplements the title
destinations
AlertDestination[] 
Expand AlertDestination definition... 
destination_type
string 
Type of destination that the alert will be sent to Valid values are: "EMAIL", "ACTION_HUB".
email_address
string 
Email address for the 'email' type
action_hub_integration_id
string 
Action hub integration id for the 'action_hub' type. [Integration](#!/types/Integration)
action_hub_form_params_json
string 
Action hub form params json for the 'action_hub' type [IntegrationParam](#!/types/IntegrationParam)
field
The field the alert threshold is compared against when determining when to send notifications
Expand AlertField definition... 
title
string 
Field's title. Usually auto-generated to reflect field name and its filters
name
string 
Field's name. Has the format `.` Refer to [docs](https://cloud.google.com/looker/docs/sharing-and-publishing/creating-alerts) for more details
filter
AlertFieldFilter[] 
Expand AlertFieldFilter definition... 
field_name
string 
Field Name. Has format ` 
field_value
Field Value. Depends on the type of field - numeric or string. For [location](https://cloud.google.com/looker/docs/reference/field-reference/dimension-type-reference#location) type, it's a list of floats. Example `[1.0, 56.0]`
filter_value
string 
Filter Value. Usually null except for [location](https://cloud.google.com/looker/docs/reference/field-reference/dimension-type-reference#location) type. It'll be a string of lat,long ie `'1.0,56.0'`
followed
_lock_
boolean 
Whether or not the user follows this alert.
followable
_lock_
boolean 
Whether or not the alert is followable
id
_lock_
string 
ID of the alert
is_disabled
boolean 
Whether or not the alert is disabled
disabled_reason
string 
Reason for disabling alert
is_public
boolean 
Whether or not the alert is public
investigative_content_type
string 
The type of the investigative content Valid values are: "dashboard".
investigative_content_id
string 
The ID of the investigative content. For dashboards, this will be the dashboard ID
investigative_content_title
_lock_
string 
The title of the investigative content.
lookml_dashboard_id
string 
ID of the LookML dashboard associated with the alert
lookml_link_id
string 
ID of the LookML dashboard element associated with the alert
owner_id
string 
User id of alert owner
owner_display_name
_lock_
string 
Alert owner's display name
threshold
number 
Value of the alert threshold
time_series_condition_state
(Write-Only) (Optional) Only used when first creating time series alerts. It's used to pick a starting time reference from which alerts will be evaluated again. Without it, alerts be run against all time series data. Refer to [docs](https://cloud.google.com/looker/docs/sharing-and-publishing/creating-alerts) for details. Example `{ latest_time_series_id: '2020-09-17', previous_time_series_id: '2020-09-16' }`.
Expand AlertConditionState definition... 
previous_time_series_id
string 
(Write-Only) The second latest time string the alert has seen.
latest_time_series_id
string 
(Write-Only) Latest time string the alert has seen.
### 400: Bad Request
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
### 404: Not Found
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
### 429: Too Many Requests
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


