# SamlConfig  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/SamlConfig

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  SamlConfig
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
enabled
boolean 
Enable/Disable Saml authentication for the server
idp_cert
string 
Identity Provider Certificate (provided by IdP)
idp_url
string 
Identity Provider Url (provided by IdP)
idp_issuer
string 
Identity Provider Issuer (provided by IdP)
idp_audience
string 
Identity Provider Audience (set in IdP config). Optional in Looker. Set this only if you want Looker to validate the audience value returned by the IdP.
allowed_clock_drift
integer 
Count of seconds of clock drift to allow when validating timestamps of assertions.
user_attribute_map_email
string 
Name of user record attributes used to indicate email address field
user_attribute_map_first_name
string 
Name of user record attributes used to indicate first name
user_attribute_map_last_name
string 
Name of user record attributes used to indicate last name
new_user_migration_types
string 
Merge first-time saml login to existing user account by email addresses. When a user logs in for the first time via saml this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'
alternate_email_login_allowed
boolean 
Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.
test_slug
_lock_
string 
Slug to identify configurations that are created in order to run a Saml config test
modified_at
_lock_
string 
When this config was last modified
modified_by
_lock_
string 
User id of user who last modified this config
default_new_user_roles
Expand Role definition... 
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
Name of Role
permission_set
_lock_
(Read only) Permission set
Expand PermissionSet definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
all_access
_lock_
boolean 
built_in
_lock_
boolean 
id
_lock_
string 
Unique Id
name
string 
Name of PermissionSet
permissions
string[] 
url
_lock_
string 
Link to get this item
permission_set_id
string 
(Write-Only) Id of permission set
model_set
_lock_
(Read only) Model set
Expand ModelSet definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
all_access
_lock_
boolean 
built_in
_lock_
boolean 
id
_lock_
string 
Unique Id
models
string[] 
name
string 
Name of ModelSet
url
_lock_
string 
Link to get this item
model_set_id
string 
(Write-Only) Id of model set
url
_lock_
string 
Link to get this item
users_url
_lock_
string 
Link to get list of users with this role
default_new_user_groups
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
default_new_user_role_ids
string[] 
default_new_user_group_ids
string[] 
set_roles_from_groups
boolean 
Set user roles in Looker based on groups from Saml
groups_attribute
string 
Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'
groups
Expand SamlGroupRead definition... 
id
_lock_
string 
Unique Id
looker_group_id
_lock_
string 
Unique Id of group in Looker
looker_group_name
_lock_
string 
Name of group in Looker
name
_lock_
string 
Name of group in Saml
roles
Expand Role definition... 
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
Name of Role
permission_set
_lock_
(Read only) Permission set
permission_set_id
string 
(Write-Only) Id of permission set
model_set
_lock_
(Read only) Model set
model_set_id
string 
(Write-Only) Id of model set
url
_lock_
string 
Link to get this item
users_url
_lock_
string 
Link to get list of users with this role
url
_lock_
string 
Link to saml config
groups_with_role_ids
Expand SamlGroupWrite definition... 
id
string 
Unique Id
looker_group_id
_lock_
string 
Unique Id of group in Looker
looker_group_name
string 
Name of group in Looker
name
string 
Name of group in Saml
role_ids
string[] 
url
_lock_
string 
Link to saml config
auth_requires_role
boolean 
Users will not be allowed to login at all unless a role for them is found in Saml if set to true
user_attributes
SamlUserAttributeRead[] 
Expand SamlUserAttributeRead definition... 
name
_lock_
string 
Name of User Attribute in Saml
required
_lock_
boolean 
Required to be in Saml assertion for login to be allowed to succeed
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
Link to saml config
user_attributes_with_ids
SamlUserAttributeWrite[] 
Expand SamlUserAttributeWrite definition... 
name
string 
Name of User Attribute in Saml
required
boolean 
Required to be in Saml assertion for login to be allowed to succeed
user_attribute_ids
string[] 
url
_lock_
string 
Link to saml config
groups_finder_type
string 
Identifier for a strategy for how Looker will find groups in the SAML response. One of ['grouped_attribute_values', 'individual_attributes']
groups_member_value
string 
Value for group attribute used to indicate membership. Used when 'groups_finder_type' is set to 'individual_attributes'
bypass_login_page
boolean 
Bypass the login page when user authentication is required. Redirect to IdP immediately instead.
allow_normal_group_membership
boolean 
Allow SAML auth'd users to be members of non-reflected Looker groups. If 'false', user will be removed from non-reflected groups on login.
allow_roles_from_normal_groups
boolean 
SAML auth'd users will inherit roles from non-reflected Looker groups.
allow_direct_roles
boolean 
Allows roles to be directly assigned to SAML auth'd users.
url
_lock_
string 
Link to get this item
## Related Methods
  * Auth/update_saml_config
  * Auth/create_saml_test_config


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


