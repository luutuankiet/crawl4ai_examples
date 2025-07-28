# Get an artifact value  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Artifact/artifact_value

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get an artifact value
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Return the value of an artifact
The MIME type for the API response is set to the `content_type` of the value
**Note** : The artifact storage API can only be used by Looker-built extensions.
## Request
GET /artifact/{namespace}/value 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
namespace
string 
Artifact storage namespace
query
HTTP Query 
Expand HTTP Query definition... 
key
string 
Artifact storage key. Namespace + Key must be unique
## Response
### 200: Artifact value
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


