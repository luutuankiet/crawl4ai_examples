# Add Support Access Allowlist Users  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/add_support_access_allowlist_entries

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Add Support Access Allowlist Users
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Add Support Access Allowlist Users
Adds a list of emails to the Allowlist, using the provided reason
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
POST /support_access/allowlist 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
SupportAccessAddEntries
Request params.
Expand SupportAccessAddEntries definition... 
emails
string[] 
reason
string 
Reason for adding emails to the Allowlist
## Response
### 200: Support Access Allowlist Entries
Datatype
Description
(array)
SupportAccessAllowlistEntry[] 
id
_lock_
string 
Unique ID
email
string 
Email address
full_name
_lock_
string 
Full name of allowlisted user
reason
string 
Reason the Email is included in the Allowlist
created_date
_lock_
string 
Date the Email was added to the Allowlist
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
### 422: Validation Error
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


