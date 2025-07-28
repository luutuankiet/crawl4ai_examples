# Get Email/Password Credential  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/user_credentials_email

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Email/password login information for the specified user.




Was this helpful?
Send feedback 
#  Get Email/Password Credential
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Email/password login information for the specified user.


Version 4.0.25.10 (latest) 
### Email/password login information for the specified user.
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
GET /users/{user_id}/credentials_email 
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
200: Email/Password Credential400: Bad Request403: Permission Denied404: Not Found More
429: Too Many Requests
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
string 
EMail address used for user login
forced_password_reset_at_next_login
boolean 
Force the user to change their password upon their next login
user_id
_lock_
string 
Unique Id of the user
is_disabled
_lock_
boolean 
Has this credential been disabled?
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
password_reset_url
_lock_
string 
Url with one-time use secret token that the user can use to reset password
account_setup_url
_lock_
string 
Url with one-time use secret token that the user can use to setup account
password_reset_url_expired
_lock_
boolean 
Is password_reset_url expired or not present?
account_setup_url_expired
_lock_
boolean 
Is account_setup_url expired or not present?
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
user_url
_lock_
string 
Link to get this user
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
documentation_url
_lock_
string 
Documentation link
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


