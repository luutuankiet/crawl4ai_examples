# Get User by Id  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/user

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get User by Id
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Get information about the user with a specific id.
If the caller is an admin or the caller is the user being specified, then full user information will be returned. Otherwise, a minimal 'public' variant of the user information will be returned. This contains The user name and avatar url, but no sensitive information.
## Request
GET /users/{user_id} 
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
### 200: Specified user.
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
avatar_url
_lock_
string 
URL for the avatar image (may be generic)
avatar_url_without_sizing
_lock_
string 
URL for the avatar image (may be generic), does not specify size
credentials_api3
Expand CredentialsApi3 definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
client_id
_lock_
string 
API key client_id
created_at
_lock_
string 
Timestamp for the creation of this credential
is_disabled
_lock_
boolean 
Has this credential been disabled?
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
credentials_email
_lock_
Email/Password login credentials
Expand CredentialsEmail definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Timestamp for the creation of this credential
email
string 
EMail address used for user login
forced_password_reset_at_next_login
boolean 
Force the user to change their password upon their next login
user_id
_lock_
string 
Unique Id of the user
is_disabled
_lock_
boolean 
Has this credential been disabled?
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
password_reset_url
_lock_
string 
Url with one-time use secret token that the user can use to reset password
account_setup_url
_lock_
string 
Url with one-time use secret token that the user can use to setup account
password_reset_url_expired
_lock_
boolean 
Is password_reset_url expired or not present?
account_setup_url_expired
_lock_
boolean 
Is account_setup_url expired or not present?
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
user_url
_lock_
string 
Link to get this user
credentials_embed
CredentialsEmbed[] 
Expand CredentialsEmbed definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Timestamp for the creation of this credential
external_group_id
_lock_
string 
Embedder's id for a group to which this user was added during the most recent login
external_user_id
_lock_
string 
Embedder's unique id for the user
id
_lock_
string 
Unique Id
is_disabled
_lock_
boolean 
Has this credential been disabled?
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
credentials_google
_lock_
Google auth credentials
Expand CredentialsGoogle definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Timestamp for the creation of this credential
domain
_lock_
string 
Google domain
email
_lock_
string 
EMail address
google_user_id
_lock_
string 
Google's Unique ID for this user
is_disabled
_lock_
boolean 
Has this credential been disabled?
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
credentials_ldap
_lock_
LDAP credentials
Expand CredentialsLDAP definition... 
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
credentials_looker_openid
_lock_
CredentialsLookerOpenid
LookerOpenID credentials. Used for login by Looker Analysts
Expand CredentialsLookerOpenid definition... 
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
EMail address used for user login
is_disabled
_lock_
boolean 
Has this credential been disabled?
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
logged_in_ip
_lock_
string 
IP address of client for most recent login using credential
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
user_url
_lock_
string 
Link to get this user
credentials_oidc
_lock_
OpenID Connect auth credentials
Expand CredentialsOIDC definition... 
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
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
oidc_user_id
_lock_
string 
OIDC OP's Unique ID for this user
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
credentials_saml
_lock_
Saml auth credentials
Expand CredentialsSaml definition... 
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
logged_in_at
_lock_
string 
Timestamp for most recent login using credential
saml_user_id
_lock_
string 
Saml IdP's Unique ID for this user
type
_lock_
string 
Short name for the type of this kind of credential
url
_lock_
string 
Link to get this item
credentials_totp
_lock_
Two-factor credentials
Expand CredentialsTotp definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Timestamp for the creation of this credential
is_disabled
_lock_
boolean 
Has this credential been disabled?
type
_lock_
string 
Short name for the type of this kind of credential
verified
_lock_
boolean 
User has verified
url
_lock_
string 
Link to get this item
display_name
_lock_
string 
Full name for display (available only if both first_name and last_name are set)
email
_lock_
string 
EMail address
embed_group_space_id
_lock_
string 
(DEPRECATED) (Embed only) ID of user's group space based on the external_group_id optionally specified during embed user login
first_name
string 
First name
group_ids
string[] 
home_folder_id
string 
ID string for user's home folder
id
_lock_
string 
Unique Id
is_disabled
boolean 
Account has been disabled
last_name
string 
Last name
locale
string 
User's preferred locale. User locale takes precedence over Looker's system-wide default locale. Locale determines language of display strings and date and numeric formatting in API responses. Locale string must be a 2 letter language code or a combination of language code and region code: 'en' or 'en-US', for example.
looker_versions
string[] 
models_dir_validated
boolean 
User's dev workspace has been checked for presence of applicable production projects
personal_folder_id
_lock_
string 
ID of user's personal folder
presumed_looker_employee
_lock_
boolean 
(DEPRECATED) User is identified as an employee of Looker
role_ids
string[] 
sessions
Expand Session definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
ip_address
_lock_
string 
IP address of user when this session was initiated
browser
_lock_
string 
User's browser type
operating_system
_lock_
string 
User's Operating System
city
_lock_
string 
City component of user location (derived from IP address)
state
_lock_
string 
State component of user location (derived from IP address)
country
_lock_
string 
Country component of user location (derived from IP address)
credentials_type
_lock_
string 
Type of credentials used for logging in this session
extended_at
_lock_
string 
Time when this session was last extended by the user
extended_count
_lock_
integer 
Number of times this session was extended
sudo_user_id
_lock_
string 
Actual user in the case when this session represents one user sudo'ing as another
created_at
_lock_
string 
Time when this session was initiated
expires_at
_lock_
string 
Time when this session will expire
url
_lock_
string 
Link to get this item
ui_state
object 
Per user dictionary of undocumented state information owned by the Looker UI.
verified_looker_employee
_lock_
boolean 
User is identified as an employee of Looker who has been verified via Looker corporate authentication
roles_externally_managed
_lock_
boolean 
User's roles are managed by an external directory like SAML or LDAP and can not be changed directly.
allow_direct_roles
_lock_
boolean 
User can be directly assigned a role.
allow_normal_group_membership
_lock_
boolean 
User can be a direct member of a normal Looker group.
allow_roles_from_normal_groups
_lock_
boolean 
User can inherit roles from a normal Looker group.
embed_group_folder_id
_lock_
string 
(Embed only) ID of user's group folder based on the external_group_id optionally specified during embed user login
is_iam_admin
_lock_
boolean 
User is an IAM Admin - only available in Looker (Google Cloud core)
url
_lock_
string 
Link to get this item
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
## Examples
### Ruby
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/disable_users.rb   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/disable_users.rb   
### Kotlin
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
---  
### TypeScript
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
### Python
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
### Swift
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/methodsTests.swift   
---  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


