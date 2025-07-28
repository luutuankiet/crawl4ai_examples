# Update Digest_emails  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_digest_emails_enabled

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Update the setting for enabling/disabling digest emails




Was this helpful?
Send feedback 
#  Update Digest_emails
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Update the setting for enabling/disabling digest emails


Version 4.0.25.10 (latest) 
### Update the setting for enabling/disabling digest emails
## Request
PATCH /digest_emails_enabled 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Digest_emails
Expand DigestEmails definition... 
is_enabled
boolean 
Whether or not digest emails are enabled
## Response
200: Digest_emails400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(object)
is_enabled
boolean 
Whether or not digest emails are enabled
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


