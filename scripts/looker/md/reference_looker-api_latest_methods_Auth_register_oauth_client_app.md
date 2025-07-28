# Register OAuth App  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/register_oauth_client_app

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Register an OAuth2 Client App




Was this helpful?
Send feedback 
#  Register OAuth App
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Register an OAuth2 Client App


Version 4.0.25.10 (latest) 
### Register an OAuth2 Client App
Registers details identifying an external web app or native app as an OAuth2 login client of the Looker instance. The app registration must provide a unique client_guid and redirect_uri that the app will present in OAuth login requests. If the client_guid and redirect_uri parameters in the login request do not match the app details registered with the Looker instance, the request is assumed to be a forgery and is rejected.
## Request
POST /oauth_client_apps/{client_guid} 
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
body
HTTP Body 
Expand HTTP Body definition... 
body
OAuth Client App
Expand OauthClientApp definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
client_guid
_lock_
string 
The globally unique id of this application
redirect_uri
string 
The uri with which this application will receive an auth code by browser redirect.
display_name
string 
The application's display name
description
string 
A description of the application that will be displayed to users
enabled
boolean 
When enabled is true, OAuth2 and API requests will be accepted from this app. When false, all requests from this app will be refused. Setting disabled invalidates existing tokens.
group_id
string 
If set, only Looker users who are members of this group can use this web app with Looker. If group_id is not set, any Looker user may use this app to access this Looker instance
tokens_invalid_before
_lock_
string 
All auth codes, access tokens, and refresh tokens issued for this application prior to this date-time for ALL USERS will be invalid.
activated_users
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: OAuth Client App400: Bad Request404: Not Found409: Resource Already Exists More
422: Validation Error429: Too Many Requests
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
client_guid
_lock_
string 
The globally unique id of this application
redirect_uri
string 
The uri with which this application will receive an auth code by browser redirect.
display_name
string 
The application's display name
description
string 
A description of the application that will be displayed to users
enabled
boolean 
When enabled is true, OAuth2 and API requests will be accepted from this app. When false, all requests from this app will be refused. Setting disabled invalidates existing tokens.
group_id
string 
If set, only Looker users who are members of this group can use this web app with Looker. If group_id is not set, any Looker user may use this app to access this Looker instance
tokens_invalid_before
_lock_
string 
All auth codes, access tokens, and refresh tokens issued for this application prior to this date-time for ALL USERS will be invalid.
activated_users
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
## Examples
More
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen-scripts/scripts/utils.ts   
---  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


