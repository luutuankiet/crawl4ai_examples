# Delete Support Access Allowlist Entry  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/delete_support_access_allowlist_entry

Skip to main content 



Console 
  * On this page
  * Delete Support Access Allowlist User




Was this helpful?
Send feedback 
#  Delete Support Access Allowlist Entry
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Delete Support Access Allowlist User


Version 4.0.25.10 (latest) 
### Delete Support Access Allowlist User
Deletes the specified Allowlist Entry Id
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
DELETE /support_access/allowlist/{entry_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
entry_id
string 
Id of Allowlist Entry
## Response
204: Entry successfully deleted.400: Bad Request403: Permission Denied404: Not Found More
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


