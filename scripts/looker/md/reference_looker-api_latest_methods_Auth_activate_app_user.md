# Activate OAuth App User  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/activate_app_user

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Activate an app for a user




Was this helpful?
Send feedback 
#  Activate OAuth App User
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Activate an app for a user


Version 4.0.25.10 (latest) 
### Activate an app for a user
Activates a user for a given oauth client app. This indicates the user has been informed that the app will have access to the user's looker data, and that the user has accepted and allowed the app to use their Looker account.
Activating a user for an app that the user is already activated with returns a success response.
## Request
POST /oauth_client_apps/{client_guid}/users/{user_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
client_guid
string 
The unique id of this application
user_id
string 
The id of the user to enable use of this app
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: OAuth Client App400: Bad Request404: Not Found422: Validation Error More
429: Too Many Requests
Datatype
Description
(string)
string 
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


