# Alert Notifications  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Alert/alert_notifications

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  Alert Notifications
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
# Alert Notifications. 
The endpoint returns all the alert notifications received by the user on email in the past 7 days. It also returns whether the notifications have been read by the user.
## Request
GET /alert_notifications 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
limit
integer 
(Optional) Number of results to return (used with `offset`).
offset
integer 
(Optional) Number of results to skip before returning any (used with `limit`).
## Response
200: It shows all the alert notifications received by the user on email.400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
AlertNotifications[] 
notification_id
_lock_
string 
ID of the notification
alert_condition_id
_lock_
string 
ID of the alert
user_id
_lock_
string 
ID of the user
is_read
boolean 
Read state of the notification
field_value
_lock_
number 
The value of the field on which the alert condition is set
threshold_value
_lock_
number 
The value of the threshold which triggers the alert notification
ran_at
_lock_
string 
The time at which the alert query ran
alert
_lock_
It contains the details needed for mobile alerts payload
Expand MobilePayload definition... 
title
_lock_
string 
Title of the alert
alert_id
_lock_
string 
ID of the alert
investigative_content_id
_lock_
string 
ID of the investigative content
dashboard_name
_lock_
string 
Name of the dashboard on which the alert has been set
dashboard_id
_lock_
string 
ID of the dashboard on which the alert has been set
query_slug
_lock_
string 
Slug of the query which runs the alert queries.
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


