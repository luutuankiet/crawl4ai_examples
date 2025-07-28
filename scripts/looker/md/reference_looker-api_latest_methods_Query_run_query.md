# Run Query  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/run_query

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Run a saved query.




Was this helpful?
Send feedback 
#  Run Query
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Run a saved query.


Version 4.0.25.10 (latest) 
### Run a saved query.
This runs a previously saved query. You can use this on a query that was generated in the Looker UI or one that you have explicitly created using the API. You can also use a query 'id' from a saved 'Look'.
The 'result_format' parameter specifies the desired structure and format of the response.
Supported formats:
result_format | Description  
---|---  
json | Plain json  
json_bi | (_RECOMMENDED_) Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query. See JsonBi type for schema  
json_detail | (_LEGACY_) Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query  
csv | Comma separated values with a header  
txt | Tab separated values with a header  
html | Simple html  
md | Simple markdown  
xlsx | MS Excel spreadsheet  
sql | Returns the generated SQL rather than running the query  
png | A PNG image of the visualization of the query  
jpg | A JPG image of the visualization of the query  
## Request
GET /queries/{query_id}/run/{result_format} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
query_id
string 
Id of query
result_format
string 
Format of result
query
HTTP Query 
Expand HTTP Query definition... 
limit
integer 
Row limit (may override the limit in the saved query).
apply_formatting
boolean 
Apply model-specified formatting to each result.
apply_vis
boolean 
Apply visualization options to results.
cache
boolean 
Get results from cache if available.
image_width
integer 
Render width for image formats.
image_height
integer 
Render height for image formats.
generate_drill_links
boolean 
Generate drill links (only applicable to 'json_detail' format.
force_production
boolean 
Force use of production models even if the user is in development mode. Note that this flag being false does not guarantee development models will be used.
cache_only
boolean 
Retrieve any results from cache even if the results have expired.
path_prefix
string 
Prefix to use for drill links (url encoded).
rebuild_pdts
boolean 
Rebuild PDTS used in query.
server_table_calcs
boolean 
Perform table calculations on query results
source
string 
Specifies the source of this call.
enable_oauth_error_response
boolean 
Return a specialized OAuth error response if a database OAuth error occurs.
## Response
400: Bad Request403: Database OAuth Error404: Not Found422: Validation Error More
429: Too Many Requests
Datatype
Description
(string)
string 
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
## Examples
More
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-write-to-bigquery/main.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


