# LDAPUserAttributeRead  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPUserAttributeRead

Skip to main content 


  * Español – América Latina

Console  Sign in
  * On this page




Send feedback 
#  LDAPUserAttributeRead
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
name
_lock_
string 
Name of User Attribute in LDAP
required
_lock_
boolean 
Required to be in LDAP assertion for login to be allowed to succeed
user_attributes
Expand UserAttribute definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
name
string 
Name of user attribute
label
string 
Human-friendly label for user attribute
type
string 
Type of user attribute ("string", "number", "datetime", "yesno", "zipcode", "advanced_filter_string", "advanced_filter_number")
default_value
string 
Default value for when no value is set on the user
is_system
_lock_
boolean 
Attribute is a system default
is_permanent
_lock_
boolean 
Attribute is permanent and cannot be deleted
value_is_hidden
boolean 
If true, users will not be able to view values of this attribute
user_can_view
boolean 
Non-admin users can see the values of their attributes and use them in filters
user_can_edit
boolean 
Users can change the value of this attribute for themselves
hidden_value_domain_whitelist
string 
Destinations to which a hidden attribute may be sent. Once set, cannot be edited.
url
_lock_
string 
Link to ldap config
## Related Types


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


