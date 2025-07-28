# Get Support Access Allowlist Users  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/get_support_access_allowlist_entries

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get Support Access Allowlist Users




Was this helpful?
Send feedback 
#  Get Support Access Allowlist Users
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get Support Access Allowlist Users


Version 4.0.25.10 (latest) 
### Get Support Access Allowlist Users
Returns the users that have been added to the Support Access Allowlist
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
GET /support_access/allowlist 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: Support Access Allowlist Entries400: Bad Request403: Permission Denied404: Not Found More
429: Too Many Requests
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


