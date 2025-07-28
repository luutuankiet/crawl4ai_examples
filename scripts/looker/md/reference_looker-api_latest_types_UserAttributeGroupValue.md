# UserAttributeGroupValue  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/UserAttributeGroupValue

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  UserAttributeGroupValue
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id of this group-attribute relation
group_id
_lock_
string 
Id of group
user_attribute_id
_lock_
string 
Id of user attribute
value_is_hidden
_lock_
boolean 
If true, the "value" field will be null, because the attribute settings block access to this value
rank
_lock_
integer 
Precedence for resolving value for user
value
_lock_
string 
Value of user attribute for group
## Related Methods
  * Group/update_user_attribute_group_value


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


