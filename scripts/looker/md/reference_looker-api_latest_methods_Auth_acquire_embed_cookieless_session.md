# Create Acquire cookieless embed session  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/acquire_embed_cookieless_session

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Acquire a cookieless embed session.




Was this helpful?
Send feedback 
#  Create Acquire cookieless embed session
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Acquire a cookieless embed session.


Version 4.0.25.10 (latest) 
### Acquire a cookieless embed session.
The acquire session endpoint negates the need for signing the embed url and passing it as a parameter to the embed login. This endpoint accepts an embed user definition and creates or updates it. This is similar behavior to the embed SSO login as they both can create and update embed user data.
The endpoint also accepts an optional `session_reference_token`. If present and the session has not expired and the credentials match the credentials for the embed session, a new authentication token will be generated. This allows the embed session to attach a new embedded IFRAME to the embed session. Note that the session is NOT extended in this scenario. In other words the session_length parameter is ignored.
**IMPORTANT:** If the `session_reference_token` is provided and the session has NOT expired, the embed user is NOT updated. This is done for performance reasons and to support the embed SSO usecase where the first IFRAME created on a page uses a signed url and subsequently created IFRAMEs do not.
If the `session_reference_token` is provided but the session has expired, the token will be ignored and a new embed session will be created. Note that the embed user definition will be updated in this scenario.
If the credentials do not match the credentials associated with an existing session_reference_token, a 404 will be returned.
The endpoint returns the following:
  * Authentication token - a token that is passed to `/embed/login` endpoint that creates or attaches to the embed session. This token can be used once and has a lifetime of 30 seconds.
  * Session reference token - a token that lives for the length of the session. This token is used to generate new api and navigation tokens OR create new embed IFRAMEs.
  * Api token - lives for 10 minutes. The Looker client will ask for this token once it is loaded into the iframe.
  * Navigation token - lives for 10 minutes. The Looker client will ask for this token once it is loaded into the iframe.


**NOTE** : Calls to this endpoint require Embedding to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.
## Request
POST /embed/cookieless_session/acquire 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
EmbedCookielessSessionAcquire
Embed user details
Expand EmbedCookielessSessionAcquire definition... 
session_length
integer 
Number of seconds the signed embed session will be valid after the embed session is started. Defaults to 300 seconds. Maximum session length accepted is 2592000 seconds (30 days).
force_logout_login
boolean 
When true, the embed session will purge any residual Looker login state (such as in browser cookies) before creating a new login state with the given embed user info. Defaults to true.
external_user_id
string 
A value from an external system that uniquely identifies the embed user. Since the user_ids of Looker embed users may change with every embed session, external_user_id provides a way to assign a known, stable user identifier across multiple embed sessions. When the same external user id value is used for a new embed session, any existing session is terminated and existing access grants are replaced with the access grants associated with the new embed session.
first_name
string 
First name of the embed user. Defaults to 'Embed' if not specified
last_name
string 
Last name of the embed user. Defaults to 'User' if not specified
user_timezone
string 
Sets the user timezone for the embed user session, if the User Specific Timezones setting is enabled in the Looker admin settings. A value of `null` forces the embed user to use the Looker Application Default Timezone. You MUST omit this property from the request if the User Specific Timezones setting is disabled. Timezone values are validated against the IANA Timezone standard and can be seen in the Application Time Zone dropdown list on the Looker General Settings admin page.
permissions
string[] 
models
string[] 
group_ids
string[] 
external_group_id
string 
A unique value identifying an embed-exclusive group. Multiple embed users using the same `external_group_id` value will be able to share Looker content with each other. Content and embed users associated with the `external_group_id` will not be accessible to normal Looker users or embed users not associated with this `external_group_id`.
user_attributes
object 
A dictionary of name-value pairs associating a Looker user attribute name with a value.
embed_domain
string 
The domain of the server embedding the Looker IFRAME. This is an alternative to specifying the domain in the embedded domain allow list in the Looker embed admin page.
session_reference_token
string 
Token referencing the embed session and is used to generate new authentication, navigation and api tokens.
## Response
200: Embed cookieless acquire session response400: Bad Request403: Permission Denied404: Not Found More
409: Resource Already Exists422: Validation Error429: Too Many Requests
Datatype
Description
(object)
EmbedCookielessSessionAcquireResponse
authentication_token
string 
One time token used to create or to attach to an embedded session in the Looker application server.
authentication_token_ttl
integer 
Authentication token time to live in seconds.
navigation_token
string 
Token used to load and navigate between Looker pages.
navigation_token_ttl
integer 
Navigation token time to live in seconds.
api_token
string 
Token to used to call Looker APIs. 
api_token_ttl
integer 
Api token time to live in seconds.
session_reference_token
string 
Token referencing the actual embed session. It is used to generate new api, navigation and authentication tokens. api and navigation tokens are short lived and must be refreshed regularly. A new authentication token must be acquired for each IFRAME that is created. The session_reference_token should be kept secure, ideally in the embed hosts application server. 
session_reference_token_ttl
integer 
Session reference token time to live in seconds. Note that this is the same as actual embed session. The session is expired when the value is set to zero. It is important to note that the generate token endpoint does NOT return an error when the embed session has expired. If an embedding application needs to monitor expiration of embed sessions, check this property for a value of zero.
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


