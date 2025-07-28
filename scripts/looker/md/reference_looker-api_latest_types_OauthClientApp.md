# OauthClientApp  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/OauthClientApp

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  OauthClientApp
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
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
## Related Methods
  * Auth/register_oauth_client_app
  * Auth/update_oauth_client_app


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


