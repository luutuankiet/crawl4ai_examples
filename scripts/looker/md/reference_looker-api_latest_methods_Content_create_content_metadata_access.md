# Create Content Metadata Access  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/create_content_metadata_access

Skip to main content 


  * Español – América Latina

Console  Sign in
  * On this page
  * Create content metadata access.




Send feedback 
#  Create Content Metadata Access
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create content metadata access.


Version 4.0.25.10 (latest) 
### Create content metadata access.
## Request
POST /content_metadata_access 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
ContentMetaGroupUser
Content Metadata Access
Expand ContentMetaGroupUser definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
content_metadata_id
_lock_
string 
Id of associated Content Metadata
permission_type
_lock_
string 
Type of permission: "view" or "edit" Valid values are: "view", "edit".
group_id
_lock_
string 
ID of associated group
user_id
_lock_
string 
ID of associated user
query
HTTP Query 
Expand HTTP Query definition... 
send_boards_notification_email
boolean 
Optionally sends notification email when granting access to a board.
## Response
### 200: Content Metadata Access
Datatype
Description
(object)
ContentMetaGroupUser
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
content_metadata_id
_lock_
string 
Id of associated Content Metadata
permission_type
_lock_
string 
Type of permission: "view" or "edit" Valid values are: "view", "edit".
group_id
_lock_
string 
ID of associated group
user_id
_lock_
string 
ID of associated user
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


