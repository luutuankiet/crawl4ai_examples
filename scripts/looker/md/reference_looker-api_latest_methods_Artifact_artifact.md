# Get one or more artifacts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Artifact/artifact

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get one or more artifacts




Was this helpful?
Send feedback 
#  Get one or more artifacts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get one or more artifacts


Version 4.0.25.10 (latest) 
### Get one or more artifacts
Returns an array of artifacts matching the specified key value(s).
**Note** : The artifact storage API can only be used by Looker-built extensions.
## Request
GET /artifact/{namespace} 
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
fields
string 
Comma-delimited names of fields to return in responses. Omit for all fields
limit
integer 
Number of results to return. (used with offset)
offset
integer 
Number of results to skip before returning any. (used with limit)
tally
boolean 
Return the full count of results in the X-Total-Count response header. (Slight performance hit.)
## Response
200: Created or updated artifacts400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(array)
key
string 
Key of value to store. Namespace + Key must be unique.
value
string 
Value to store.
content_type
string 
MIME type of content. This can only be used to override content that is detected as text/plain. Needed to set application/json content types, which are analyzed as plain text.
version
_lock_
integer 
Version number of the stored value. The version must be provided for any updates to an existing artifact.
namespace
_lock_
string 
Artifact storage namespace.
created_at
_lock_
string 
Timestamp when this artifact was created.
updated_at
_lock_
string 
Timestamp when this artifact was updated.
value_size
_lock_
integer 
Size (in bytes) of the stored value.
created_by_userid
_lock_
string 
User id of the artifact creator.
updated_by_userid
_lock_
string 
User id of the artifact updater.
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


