# Update Session Config  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/update_session_config

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Update Session Config
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Update session config.
## Request
PATCH /session_config 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Session Config
Expand SessionConfig definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
allow_persistent_sessions
boolean 
Allow users to have persistent sessions when they login
session_minutes
integer 
Number of minutes for user sessions. Must be between 5 and 43200
unlimited_sessions_per_user
boolean 
Allow users to have an unbounded number of concurrent sessions (otherwise, users will be limited to only one session at a time).
use_inactivity_based_logout
boolean 
Enforce session logout for sessions that are inactive for 15 minutes.
track_session_location
boolean 
Track location of session when user logs in.
## Response
### 200: Session Config
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
allow_persistent_sessions
boolean 
Allow users to have persistent sessions when they login
session_minutes
integer 
Number of minutes for user sessions. Must be between 5 and 43200
unlimited_sessions_per_user
boolean 
Allow users to have an unbounded number of concurrent sessions (otherwise, users will be limited to only one session at a time).
use_inactivity_based_logout
boolean 
Enforce session logout for sessions that are inactive for 15 minutes.
track_session_location
boolean 
Track location of session when user logs in.
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
### 422: Validation Error
Datatype
Description
(object)
message
_lock_
string 
Error details
errors
ValidationErrorDetail[] 
Expand ValidationErrorDetail definition... 
field
_lock_
string 
Field with error
code
_lock_
string 
Error code
message
_lock_
string 
Error info message
documentation_url
_lock_
string 
Documentation link
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


