# Create Signed Embed Url  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/create_sso_embed_url

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Create Signed Embed Url
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Create Signed Embed URL
Creates a signed embed URL and cryptographically signs it with an embed secret. This signed URL can then be used to instantiate a Looker embed session in a PBL web application. Do not make any modifications to the returned URL - any change may invalidate the signature and cause the URL to fail to load a Looker embed session.
A signed embed URL can only be **used once**. After the URL has been used to request a page from the Looker server, it is invalid. Future requests using the same URL will fail. This is to prevent 'replay attacks'.
The `target_url` property must be a complete URL of a Looker UI page - scheme, hostname, path and query params. To load a dashboard with id 56 and with a filter of `Date=1 years`, the looker URL would look like `https:/myname.looker.com/dashboards/56?Date=1%20years`. The best way to obtain this `target_url` is to navigate to the desired Looker page in your web browser and use the "Get embed URL" menu option to copy it to your clipboard and paste it into the `target_url` property as a quoted string value in this API request.
Permissions for the embed user are defined by the groups in which the embed user is a member (`group_ids` property) and the lists of models and permissions assigned to the embed user. At a minimum, you must provide values for either the `group_ids` property, or **both** the models and permissions properties. These properties are additive; an embed user can be a member of certain groups AND be granted access to models and permissions.
The embed user's access is the union of permissions granted by the `group_ids`, `models`, and `permissions` properties.
This function does not strictly require all group_ids, user attribute names, or model names to exist at the moment the embed url is created. Unknown group_id, user attribute names or model names will be passed through to the output URL. Because of this, **these parameters are not validated** when the API call is made.
The Get Embed Url dialog can be used to determine and validate the correct permissions for signing an embed url. This dialog also provides the SDK syntax for the API call to make. Alternatively, you can copy the signed URL into the Embed URI Validator text box in `<your looker instance>/admin/embed` to diagnose potential problems.
The `secret_id` parameter is optional. If specified, its value must be the id of an active secret defined in the Looker instance. if not specified, the URL will be signed using the most recent active signing secret. If there is no active secret for signing embed urls, a default secret will be created. This default secret is encrypted using HMAC/SHA-256.
The `embed_domain` parameter is optional. If specified and valid, the domain will be added to the embed domain allowlist if it is missing.
#### Security Note
Protect this signed URL as you would an access token or password credentials - do not write it to disk, do not pass it to a third party, and only pass it through a secure HTTPS encrypted transport.
**NOTE** : Calls to this endpoint require Embedding to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.
## Request
POST /embed/sso_url 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Signed Embed URL parameters
Expand EmbedSsoParams definition... 
target_url
string 
The complete URL of the Looker UI page to display in the embed context. For example, to display the dashboard with id 34, `target_url` would look like: `https://mycompany.looker.com:9999/dashboards/34`. `target_uri` MUST contain a scheme (HTTPS), domain name, and URL path. Port must be included if it is required to reach the Looker server from browser clients. If the Looker instance is behind a load balancer or other proxy, `target_uri` must be the public-facing domain name and port required to reach the Looker instance, not the actual internal network machine name of the Looker instance.
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
secret_id
string 
Id of the embed secret to use to sign this SSO url. If specified, the value must be an id of a valid (active) secret defined in the Looker instance. If not specified, the URL will be signed with the newest active embed secret defined in the Looker instance.
embed_domain
string 
Optional. URL of the domain hosting the signed embed URL. If provided and valid, the embed_domain will be added to the embed domain allowlist if it is not currently in the list
## Response
### 200: Signed Embed URL
Datatype
Description
(object)
url
_lock_
string 
The embed URL. Any modification to this string will make the URL unusable.
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
### 403: Permission Denied
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
### 409: Resource Already Exists
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
### 422: Validation Error
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


