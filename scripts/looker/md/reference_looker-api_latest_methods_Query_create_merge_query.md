# Create Merge Query  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/create_merge_query

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Create Merge Query
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Create Merge Query
Creates a new merge query object.
A merge query takes the results of one or more queries and combines (merges) the results according to field mapping definitions. The result is similar to a SQL left outer join.
A merge query can merge results of queries from different SQL databases.
The order that queries are defined in the source_queries array property is significant. The first query in the array defines the primary key into which the results of subsequent queries will be merged.
Like model/view query objects, merge queries are immutable and have structural identity - if you make a request to create a new merge query that is identical to an existing merge query, the existing merge query will be returned instead of creating a duplicate. Conversely, any change to the contents of a merge query will produce a new object with a new id.
## Request
POST /merge_queries 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Merge Query
Expand MergeQuery definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
column_limit
string 
Column Limit
dynamic_fields
string 
Dynamic Fields
id
_lock_
string 
Unique Id
pivots
string[] 
result_maker_id
_lock_
string 
Unique to get results
sorts
string[] 
source_queries
MergeQuerySourceQuery[] 
total
boolean 
Total
vis_config
object 
Visualization Config
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields
## Response
### 200: Merge Query
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
column_limit
string 
Column Limit
dynamic_fields
string 
Dynamic Fields
id
_lock_
string 
Unique Id
pivots
string[] 
result_maker_id
_lock_
string 
Unique to get results
sorts
string[] 
source_queries
MergeQuerySourceQuery[] 
Expand MergeQuerySourceQuery definition... 
merge_fields
Expand MergeFields definition... 
field_name
string 
Field name to map onto in the merged results
source_field_name
string 
Field name from the source query
name
string 
Display name
query_id
string 
Id of the query to merge
query_slug
string 
Slug of the query to merge
total
boolean 
Total
vis_config
object 
Visualization Config
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
## Examples
### TypeScript
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts   
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


