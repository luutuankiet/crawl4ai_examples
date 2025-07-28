# Get namespaces and counts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Artifact/artifact_namespaces

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Send feedback 
#  Get namespaces and counts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Get all artifact namespaces and the count of artifacts in each namespace
**Note** : The artifact storage API can only be used by Looker-built extensions.
## Request
GET /artifact/namespaces 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Comma-delimited names of fields to return in responses. Omit for all fields
limit
integer 
Number of results to return. (used with offset)
offset
integer 
Number of results to skip before returning any. (used with limit)
## Response
200: Artifact store namespace counts400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(array)
ArtifactNamespace[] 
namespace
_lock_
string 
Artifact storage namespace.
count
_lock_
integer 
The number of artifacts stored in the namespace.
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


