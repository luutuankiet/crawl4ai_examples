# Test LDAP User Info  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/test_ldap_config_user_info

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Test the user authentication settings for an LDAP configuration without authenticating the user.




Was this helpful?
Send feedback 
#  Test LDAP User Info
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Test the user authentication settings for an LDAP configuration without authenticating the user.


Version 4.0.25.10 (latest) 
### Test the user authentication settings for an LDAP configuration without authenticating the user.
This test will let you easily test the mapping for user properties and roles for any user withoutneeding to authenticate as that user.
This test accepts a full LDAP configuration along with a username and attempts to find the full infofor the user from the LDAP server without actually authenticating the user. So, user password is notrequired.The configuration is validated before attempting to contact the server.
**test_ldap_user** is required.
The active LDAP settings are not modified.
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
PUT /ldap_config/test_user_info 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
LDAP Config
Expand LDAPConfig definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
alternate_email_login_allowed
boolean 
Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.
auth_password
string 
(Write-Only) Password for the LDAP account used to access the LDAP server
auth_requires_role
boolean 
Users will not be allowed to login at all unless a role for them is found in LDAP if set to true
auth_username
string 
Distinguished name of LDAP account used to access the LDAP server
connection_host
string 
LDAP server hostname
connection_port
string 
LDAP host port
connection_tls
boolean 
Use Transport Layer Security
connection_tls_no_verify
boolean 
Do not verify peer when using TLS
default_new_user_group_ids
string[] 
default_new_user_groups
default_new_user_role_ids
string[] 
default_new_user_roles
enabled
boolean 
Enable/Disable LDAP authentication for the server
force_no_page
boolean 
Don't attempt to do LDAP search result paging (RFC 2696) even if the LDAP server claims to support it.
groups
groups_base_dn
string 
Base dn for finding groups in LDAP searches
groups_finder_type
string 
Identifier for a strategy for how Looker will search for groups in the LDAP server
groups_member_attribute
string 
LDAP Group attribute that signifies the members of the groups. Most commonly 'member'
groups_objectclasses
string 
Optional comma-separated list of supported LDAP objectclass for groups when doing groups searches
groups_user_attribute
string 
LDAP Group attribute that signifies the user in a group. Most commonly 'dn'
groups_with_role_ids
has_auth_password
_lock_
boolean 
(Read-only) Has the password been set for the LDAP account used to access the LDAP server
merge_new_users_by_email
boolean 
Merge first-time ldap login to existing user account by email addresses. When a user logs in for the first time via ldap this option will connect this user into their existing account by finding the account with a matching email address. Otherwise a new user account will be created for the user.
modified_at
_lock_
string 
When this config was last modified
modified_by
_lock_
string 
User id of user who last modified this config
set_roles_from_groups
boolean 
Set user roles in Looker based on groups from LDAP
test_ldap_password
string 
(Write-Only) Test LDAP user password. For ldap tests only.
test_ldap_user
string 
(Write-Only) Test LDAP user login id. For ldap tests only.
user_attribute_map_email
string 
Name of user record attributes used to indicate email address field
user_attribute_map_first_name
string 
Name of user record attributes used to indicate first name
user_attribute_map_last_name
string 
Name of user record attributes used to indicate last name
user_attribute_map_ldap_id
string 
Name of user record attributes used to indicate unique record id
user_attributes
LDAPUserAttributeRead[] 
user_attributes_with_ids
LDAPUserAttributeWrite[] 
user_bind_base_dn
string 
Distinguished name of LDAP node used as the base for user searches
user_custom_filter
string 
(Optional) Custom RFC-2254 filter clause for use in finding user during login. Combined via 'and' with the other generated filter clauses.
user_id_attribute_names
string 
Name(s) of user record attributes used for matching user login id (comma separated list)
user_objectclass
string 
(Optional) Name of user record objectclass used for finding user during login id
allow_normal_group_membership
boolean 
Allow LDAP auth'd users to be members of non-reflected Looker groups. If 'false', user will be removed from non-reflected groups on login.
allow_roles_from_normal_groups
boolean 
LDAP auth'd users will be able to inherit roles from non-reflected Looker groups.
allow_direct_roles
boolean 
Allows roles to be directly assigned to LDAP auth'd users.
url
_lock_
string 
Link to get this item
## Response
200: Result info.400: Bad Request403: Permission Denied404: Not Found More
422: Validation Error429: Too Many Requests
Datatype
Description
(object)
LDAPConfigTestResult
details
_lock_
string 
Additional details for error cases
issues
LDAPConfigTestIssue[] 
Expand LDAPConfigTestIssue definition... 
severity
_lock_
string 
Severity of the issue. Error or Warning
message
_lock_
string 
Message describing the issue
message
_lock_
string 
Short human readable test about the result
status
_lock_
string 
Test status code: always 'success' or 'error'
trace
_lock_
string 
A more detailed trace of incremental results during auth tests
user
_lock_
User details from LDAP server for auth tests
Expand LDAPUser definition... 
all_emails
string[] 
attributes
_lock_
object 
Dictionary of user's attributes (name/value)
email
_lock_
string 
Primary email address
first_name
_lock_
string 
First name
groups
string[] 
last_name
_lock_
string 
Last Name
ldap_dn
_lock_
string 
LDAP's distinguished name for the user record
ldap_id
_lock_
string 
LDAP's Unique ID for the user
roles
string[] 
url
_lock_
string 
Link to ldap config
url
_lock_
string 
Link to ldap config
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


