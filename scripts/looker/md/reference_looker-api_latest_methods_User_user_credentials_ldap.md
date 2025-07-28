# Get LDAP Credential  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/user_credentials_ldap

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * LDAP login information for the specified user.




Was this helpful?
Send feedback 
#  Get LDAP Credential
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * LDAP login information for the specified user.


Version 4.0.25.10 (latest) 
### LDAP login information for the specified user.
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
GET /users/{user_id}/credentials_ldap 
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
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: LDAP Credential400: Bad Request403: Permission Denied404: Not Found429: Too Many Requests More
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Timestamp for the creation of this credential
email
_lock_
string 
EMail address
is_disabled
_lock_
boolean 
Has this credential been disabled?
ldap_dn
_lock_
string 
LDAP Distinguished name for this user (as-of the last login)
ldap_id
_lock_
string 
LDAP Unique ID for this user
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
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
documentation_url
_lock_
string 
Documentation link
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


