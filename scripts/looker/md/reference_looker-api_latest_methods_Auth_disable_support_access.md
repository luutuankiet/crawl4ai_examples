# Disable Support Access  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/disable_support_access

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Disable Support Access
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Disable Support Access
Disables Support Access immediately
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
PUT /support_access/disable 
Datatype
Description
Request
HTTP Request 
## Response
### 200: Support Access Status
Datatype
Description
(object)
open
_lock_
boolean 
Whether or not Support Access is open
open_until
_lock_
string 
Time that Support Access will expire
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
### 403: Permission Denied
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


