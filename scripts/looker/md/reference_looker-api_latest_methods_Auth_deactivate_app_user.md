# Deactivate OAuth App User  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/deactivate_app_user

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Deactivate an app for a user




Was this helpful?
Send feedback 
#  Deactivate OAuth App User
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Deactivate an app for a user


Version 4.0.25.10 (latest) 
### Deactivate an app for a user
Deactivate a user for a given oauth client app. All tokens issued to the app for this user will be invalid immediately. Before the user can use the app with their Looker account, the user will have to read and accept an account use disclosure statement for the app.
Admin users can deactivate other users, but non-admin users can only deactivate themselves.
As with most REST DELETE operations, this endpoint does not return an error if the indicated resource (app or user) does not exist or has already been deactivated.
## Request
DELETE /oauth_client_apps/{client_guid}/users/{user_id} 
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
204: Successfully deleted.400: Bad Request404: Not Found429: Too Many Requests More
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
documentation_url
_lock_
string 
Documentation link
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


