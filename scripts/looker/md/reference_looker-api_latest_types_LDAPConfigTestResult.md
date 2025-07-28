# LDAPConfigTestResult  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPConfigTestResult

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Send feedback 
#  LDAPConfigTestResult
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
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
## Related Methods
  * Auth/test_ldap_config_connection
  * Auth/test_ldap_config_auth
  * Auth/test_ldap_config_user_info
  * Auth/test_ldap_config_user_auth


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


