# Delete User Login Lockout  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/delete_user_login_lockout

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Removes login lockout for the associated user.




Was this helpful?
Send feedback 
#  Delete User Login Lockout
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Removes login lockout for the associated user.


Version 4.0.25.10 (latest) 
### Removes login lockout for the associated user.
## Request
DELETE /user_login_lockout/{key} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
key
string 
The key associated with the locked user
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


