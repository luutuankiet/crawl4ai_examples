# Create Group  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Group/create_group

Skip to main content 


  * Español – América Latina

Console  Sign in
  * On this page
  * Creates a new group (admin only).




Send feedback 
#  Create Group
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * Creates a new group (admin only).


Version 4.0.25.10 (latest) 
### Creates a new group (admin only).
## Request
POST /groups 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Group
Expand Group definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
can_add_to_content_metadata
boolean 
Group can be used in content access controls
contains_current_user
_lock_
boolean 
Currently logged in user is group member
external_group_id
_lock_
string 
External Id group if embed group
externally_managed
_lock_
boolean 
Group membership controlled outside of Looker
id
_lock_
string 
Unique Id
include_by_default
_lock_
boolean 
New users are added to this group by default
name
string 
Name of group
user_count
_lock_
integer 
Number of users included in this group
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
### 200: Group
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
can_add_to_content_metadata
boolean 
Group can be used in content access controls
contains_current_user
_lock_
boolean 
Currently logged in user is group member
external_group_id
_lock_
string 
External Id group if embed group
externally_managed
_lock_
boolean 
Group membership controlled outside of Looker
id
_lock_
string 
Unique Id
include_by_default
_lock_
boolean 
New users are added to this group by default
name
string 
Name of group
user_count
_lock_
integer 
Number of users included in this group
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
### 409: Resource Already Exists
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


