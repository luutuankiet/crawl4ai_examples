# Get OIDC Auth Credential  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/user_credentials_oidc

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get OIDC Auth Credential
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### OpenID Connect (OIDC) authentication login information for the specified user.
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
GET /users/{user_id}/credentials_oidc 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
user_id
string 
Id of user
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
### 200: OIDC Auth Credential
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Timestamp for the creation of this credential
email
_lock_
string 
EMail address
is_disabled
_lock_
boolean 
Has this credential been disabled?
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
oidc_user_id
_lock_
string 
OIDC OP's Unique ID for this user
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
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


