# ScheduledPlan  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/ScheduledPlan

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  ScheduledPlan
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
name
string 
Name of this scheduled plan
user_id
string 
User Id which owns this scheduled plan
run_as_recipient
boolean 
Whether schedule is run as recipient (only applicable for email recipients)
enabled
boolean 
Whether the ScheduledPlan is enabled
look_id
string 
Id of a look
dashboard_id
string 
Id of a dashboard
lookml_dashboard_id
string 
Id of a LookML dashboard
filters_string
string 
Query string to run look or dashboard with
dashboard_filters
string 
(DEPRECATED) Alias for filters_string field
require_results
boolean 
Delivery should occur if running the dashboard or look returns results
require_no_results
boolean 
Delivery should occur if the dashboard look does not return results
require_change
boolean 
Delivery should occur if data have changed since the last run
send_all_results
boolean 
Will run an unlimited query and send all results.
crontab
string 
Vixie-Style crontab specification when to run
datagroup
string 
Name of a datagroup; if specified will run when datagroup triggered (can't be used with cron string)
timezone
string 
Timezone for interpreting the specified crontab (default is Looker instance timezone)
scheduled_plan_destination
ScheduledPlanDestination[] 
Expand ScheduledPlanDestination definition... 
id
_lock_
string 
Unique Id
scheduled_plan_id
string 
Id of a scheduled plan you own
format
string 
The data format to send to the given destination. Supported formats vary by destination, but include: "txt", "csv", "inline_json", "json", "json_detail", "xlsx", "html", "wysiwyg_pdf", "assembled_pdf", "wysiwyg_png"
apply_formatting
boolean 
Are values formatted? (containing currency symbols, digit separators, etc.
apply_vis
boolean 
Whether visualization options are applied to the results.
address
string 
Address for recipient. For email e.g. 'user@example.com'. For webhooks e.g. 'https://example.domain/path'. For Amazon S3 e.g. 's3://bucket-name/path/'. For SFTP e.g. 'sftp://host-name/path/'. 
looker_recipient
_lock_
boolean 
Whether the recipient is a Looker user on the current instance (only applicable for email recipients)
type
string 
Type of the address ('email', 'webhook', 's3', or 'sftp')
parameters
string 
JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username.
secret_parameters
string 
(Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password.
message
string 
Optional message to be included in scheduled emails
run_once
boolean 
Whether the plan in question should only be run once (usually for testing)
include_links
boolean 
Whether links back to Looker should be included in this ScheduledPlan
custom_url_base
string 
Custom url domain for the scheduled entity
custom_url_params
string 
Custom url path and parameters for the scheduled entity
custom_url_label
string 
Custom url label for the scheduled entity
show_custom_url
boolean 
Whether to show custom link back instead of standard looker link
pdf_paper_size
string 
The size of paper the PDF should be formatted to fit. Valid values are: "letter", "legal", "tabloid", "a0", "a1", "a2", "a3", "a4", "a5".
pdf_landscape
boolean 
Whether the PDF should be formatted for landscape orientation
embed
boolean 
Whether this schedule is in an embed context or not
color_theme
string 
Color scheme of the dashboard if applicable
long_tables
boolean 
Whether or not to expand table vis to full length
inline_table_width
integer 
The pixel width at which we render the inline table visualizations
query_id
string 
Query id
id
_lock_
string 
Unique Id
created_at
_lock_
string 
Date and time when ScheduledPlan was created
updated_at
_lock_
string 
Date and time when ScheduledPlan was last updated
title
_lock_
string 
Title
user
_lock_
User who owns this ScheduledPlan
Expand UserPublic definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
first_name
_lock_
string 
First Name
last_name
_lock_
string 
Last Name
display_name
_lock_
string 
Full name for display (available only if both first_name and last_name are set)
avatar_url
_lock_
string 
URL for the avatar image (may be generic)
url
_lock_
string 
Link to get this item
next_run_at
_lock_
string 
When the ScheduledPlan will next run (null if running once)
last_run_at
_lock_
string 
When the ScheduledPlan was last run
can
_lock_
object 
Operations the current user is able to perform on this object
## Related Methods
  * ScheduledPlan/update_scheduled_plan
  * ScheduledPlan/scheduled_plan
  * ScheduledPlan/create_scheduled_plan
  * ScheduledPlan/scheduled_plan_run_once
  * ScheduledPlan/scheduled_plan_run_once_by_id


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


