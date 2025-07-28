# DataActionForm  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/DataActionForm

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  DataActionForm
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
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
## Related Methods
  * DataAction/fetch_remote_data_action_form
  * Integration/fetch_integration_form


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


