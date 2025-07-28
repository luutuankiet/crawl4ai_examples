# Delete Repository Credential  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/delete_repository_credential

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Repository Credential for a remote dependency




Send feedback 
#  Delete Repository Credential
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Repository Credential for a remote dependency


Version 4.0.25.10 (latest) 
### Repository Credential for a remote dependency
Admin required.
`root_project_id` is required. `credential_id` is required.
## Request
DELETE /projects/{root_project_id}/credential/{credential_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
root_project_id
string 
Root Project Id
credential_id
string 
Credential Id
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


