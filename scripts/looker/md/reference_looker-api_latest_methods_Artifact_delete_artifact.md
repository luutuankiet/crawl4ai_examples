# Delete one or more artifacts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Artifact/delete_artifact

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Delete one or more artifacts
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Delete one or more artifacts
To avoid rate limiting on deletion requests, multiple artifacts can be deleted at the same time by using a comma-delimited list of artifact keys.
**Note** : The artifact storage API can only be used by Looker-built extensions.
## Request
DELETE /artifact/{namespace} 
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
Comma-delimited list of keys. Wildcards not allowed.
## Response
### 204: The artifact is deleted.
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


