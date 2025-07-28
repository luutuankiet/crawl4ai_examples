# Get schemas for a connection  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Metadata/connection_schemas

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get the list of schemas and tables for a connection




Was this helpful?
Send feedback 
#  Get schemas for a connection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get the list of schemas and tables for a connection


Version 4.0.25.10 (latest) 
### Get the list of schemas and tables for a connection
## Request
GET /connections/{connection_name}/schemas 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
connection_name
string 
Name of connection
query
HTTP Query 
Expand HTTP Query definition... 
database
string 
For dialects that support multiple databases, optionally identify which to use
cache
boolean 
True to use fetch from cache, false to load fresh
fields
string 
Requested fields.
## Response
200: Schemas for connection400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(array)
name
_lock_
string 
Schema name
is_default
_lock_
boolean 
True if this is the default schema
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


