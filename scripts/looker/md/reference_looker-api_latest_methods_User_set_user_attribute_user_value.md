# Set User Attribute User Value  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/set_user_attribute_user_value

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Store a custom value for a user attribute in a user's account settings.




Was this helpful?
Send feedback 
#  Set User Attribute User Value
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Store a custom value for a user attribute in a user's account settings.


Version 4.0.25.10 (latest) 
### Store a custom value for a user attribute in a user's account settings.
Per-user user attribute values take precedence over group or default values.
## Request
PATCH /users/{user_id}/attribute_values/{user_attribute_id} 
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
user_attribute_id
string 
Id of user attribute
body
HTTP Body 
Expand HTTP Body definition... 
body
UserAttributeWithValue
New attribute value for user.
Expand UserAttributeWithValue definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
name
_lock_
string 
Name of user attribute
label
_lock_
string 
Human-friendly label for user attribute
rank
_lock_
integer 
Precedence for setting value on user (lowest wins)
value
string 
Value of attribute for user
user_id
_lock_
string 
Id of User
user_can_edit
_lock_
boolean 
Can the user set this value
value_is_hidden
_lock_
boolean 
If true, the "value" field will be null, because the attribute settings block access to this value
user_attribute_id
_lock_
string 
Id of User Attribute
source
_lock_
string 
How user got this value for this attribute
hidden_value_domain_whitelist
_lock_
string 
If this user attribute is hidden, allowed list of destinations to which it may be sent.
## Response
200: User attribute value.400: Bad Request403: Permission Denied404: Not Found More
422: Validation Error429: Too Many Requests
Datatype
Description
(object)
UserAttributeWithValue
can
_lock_
object 
Operations the current user is able to perform on this object
name
_lock_
string 
Name of user attribute
label
_lock_
string 
Human-friendly label for user attribute
rank
_lock_
integer 
Precedence for setting value on user (lowest wins)
value
string 
Value of attribute for user
user_id
_lock_
string 
Id of User
user_can_edit
_lock_
boolean 
Can the user set this value
value_is_hidden
_lock_
boolean 
If true, the "value" field will be null, because the attribute settings block access to this value
user_attribute_id
_lock_
string 
Id of User Attribute
source
_lock_
string 
How user got this value for this attribute
hidden_value_domain_whitelist
_lock_
string 
If this user attribute is hidden, allowed list of destinations to which it may be sent.
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


