# Fetch Remote Data Action Form  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/DataAction/fetch_remote_data_action_form

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  Fetch Remote Data Action Form
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
For some data actions, the remote server may supply a form requesting further user input. This endpoint takes a data action, asks the remote server to generate a form for it, and returns that form to you for presentation to the user.
## Request
POST /data_actions/form 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
object 
Data Action Request
## Response
200: Data Action Form400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(object)
state
_lock_
User state
Expand DataActionUserState definition... 
data
_lock_
string 
User state data
refresh_time
_lock_
integer 
Time in seconds until the state needs to be refreshed
fields
DataActionFormField[] 
Expand DataActionFormField definition... 
name
_lock_
string 
Name
label
_lock_
string 
Human-readable label
description
_lock_
string 
Description of field
type
_lock_
string 
Type of field.
default
_lock_
string 
Default value of the field.
oauth_url
_lock_
string 
The URL for an oauth link, if type is 'oauth_link'.
interactive
_lock_
boolean 
Whether or not a field supports interactive forms.
required
_lock_
boolean 
Whether or not the field is required. This is a user-interface hint. A user interface displaying this form should not submit it without a value for this field. The action server must also perform this validation.
options
DataActionFormSelectOption[] 
Expand DataActionFormSelectOption definition... 
name
_lock_
string 
Name
label
_lock_
string 
Human-readable label
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


