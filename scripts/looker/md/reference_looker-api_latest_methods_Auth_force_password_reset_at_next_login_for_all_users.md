# Force password reset  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/force_password_reset_at_next_login_for_all_users

Skip to main content 



Console 
  * On this page
  * Force all credentials_email users to reset their login passwords upon their next login.




Send feedback 
#  Force password reset
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Force all credentials_email users to reset their login passwords upon their next login.


Version 4.0.25.10 (latest) 
### Force all credentials_email users to reset their login passwords upon their next login.
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
PUT /password_config/force_password_reset_at_next_login_for_all_users 
Datatype
Description
Request
HTTP Request 
## Response
200: Password Config400: Bad Request403: Permission Denied404: Not Found More
422: Validation Error429: Too Many Requests
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


