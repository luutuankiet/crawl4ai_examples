# Get All Running Queries  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/all_running_queries

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get All Running Queries
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Get information about all running queries.
## Request
GET /running_queries 
Datatype
Description
Request
HTTP Request 
## Response
### 200: Running Queries.
Datatype
Description
(array)
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
user
_lock_
User who initiated the query
Expand UserPublic definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
first_name
_lock_
string 
First Name
last_name
_lock_
string 
Last Name
display_name
_lock_
string 
Full name for display (available only if both first_name and last_name are set)
avatar_url
_lock_
string 
URL for the avatar image (may be generic)
url
_lock_
string 
Link to get this item
query
_lock_
Query that was run
Expand Query definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
model
string 
Model
view
string 
Explore Name
fields
string[] 
pivots
string[] 
fill_fields
string[] 
filters
object 
Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.
filter_expression
string 
Filter Expression
sorts
string[] 
limit
string 
Row limit. To download unlimited results, set the limit to -1 (negative one).
column_limit
string 
Column Limit
total
boolean 
Total
row_total
string 
Raw Total
subtotals
string[] 
vis_config
object 
Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.
filter_config
object 
The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.
visible_ui_sections
string 
Visible UI Sections
slug
_lock_
string 
Slug
dynamic_fields
string 
Dynamic Fields
client_id
string 
Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.
share_url
_lock_
string 
Share Url
expanded_share_url
_lock_
string 
Expanded Share Url
url
_lock_
string 
Expanded Url
query_timezone
string 
Query Timezone
has_table_calculations
_lock_
boolean 
Has Table Calculations
sql_query
_lock_
SQL Query that was run
Expand SqlQuery definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
slug
_lock_
string 
The identifier of the SQL query
last_runtime
_lock_
number 
Number of seconds this query took to run the most recent time it was run
run_count
_lock_
integer 
Number of times this query has been run
browser_limit
_lock_
integer 
Maximum number of rows this query will display on the SQL Runner page
sql
_lock_
string 
SQL query text
last_run_at
_lock_
string 
The most recent time this query was run
connection
_lock_
Connection this query uses
Expand DBConnectionBase definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
name
_lock_
string 
Name of the connection. Also used as the unique identifier
dialect
_lock_
(Read-only) SQL Dialect details
snippets
pdts_enabled
_lock_
boolean 
True if PDTs are enabled on this connection
model_name
_lock_
string 
Model name this query uses
creator
_lock_
User who created this SQL query
Expand UserPublic definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
first_name
_lock_
string 
First Name
last_name
_lock_
string 
Last Name
display_name
_lock_
string 
Full name for display (available only if both first_name and last_name are set)
avatar_url
_lock_
string 
URL for the avatar image (may be generic)
url
_lock_
string 
Link to get this item
explore_url
_lock_
string 
Explore page URL for this SQL query
plaintext
_lock_
boolean 
Should this query be rendered as plain text
vis_config
object 
Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.
result_maker_id
string 
ID of the ResultMakerLookup entry.
look
_lock_
Look of query that was run
Expand LookBasic definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
content_metadata_id
_lock_
string 
Id of content metadata
id
_lock_
string 
Unique Id
title
_lock_
string 
Look Title
user_id
string 
User Id
created_at
_lock_
string 
Date/Time Query was initiated
completed_at
_lock_
string 
Date/Time Query was completed
query_id
_lock_
string 
Query Id
source
_lock_
string 
Source (look, dashboard, queryrunner, explore, etc.)
node_id
_lock_
string 
Node Id
slug
_lock_
string 
Slug
query_task_id
_lock_
string 
ID of a Query Task
cache_key
_lock_
string 
Cache Key
connection_name
_lock_
string 
Connection
dialect
_lock_
string 
Dialect
connection_id
_lock_
string 
Connection ID
message
_lock_
string 
Additional Information(Error message or verbose status)
status
_lock_
string 
Status description
runtime
_lock_
number 
Number of seconds elapsed running the Query
sql
_lock_
string 
SQL text of the query as run
sql_interface_sql
_lock_
string 
SQL text of the SQL Interface query as run
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
## Examples
### Python
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/kill_queries.py   
---  
### Ruby
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/kill_all_running_queries.rb   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/stream_to_s3.rb   
### Swift
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


