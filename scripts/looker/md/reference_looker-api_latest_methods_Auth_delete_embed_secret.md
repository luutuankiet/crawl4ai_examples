# Delete Embed Secret  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/delete_embed_secret

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Delete Embed Secret
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Delete an embed secret.
**NOTE** : Calls to this endpoint require Embedding to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.
## Request
DELETE /embed_config/secrets/{embed_secret_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
embed_secret_id
string 
Id of Embed Secret
## Response
### 204: Successfully deleted.
Datatype
Description
(string)
string 
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


