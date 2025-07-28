# Create SQL Runner Query  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/create_sql_query

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Create a SQL Runner Query




Was this helpful?
Send feedback 
#  Create SQL Runner Query
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create a SQL Runner Query


Version 4.0.25.10 (latest) 
### Create a SQL Runner Query
Either the `connection_name` or `model_name` parameter MUST be provided.
## Request
POST /sql_queries 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
SQL Runner Query
Expand SqlQueryCreate definition... 
connection_name
string 
Name of the db connection on which to run this query
connection_id
string 
(DEPRECATED) Use `connection_name` instead
model_name
string 
Name of LookML Model (this or `connection_id` required)
sql
string 
SQL query
vis_config
object 
Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.
## Response
200: SQL Runner Query400: Bad Request404: Not Found409: Resource Already Exists More
422: Validation Error429: Too Many Requests
Datatype
Description
(object)
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
Expand Dialect definition... 
name
_lock_
string 
The name of the dialect
label
_lock_
string 
The human-readable label of the connection
supports_cost_estimate
_lock_
boolean 
Whether the dialect supports query cost estimates
cost_estimate_style
_lock_
string 
How the dialect handles cost estimation
persistent_table_indexes
_lock_
string 
PDT index columns
persistent_table_sortkeys
_lock_
string 
PDT sortkey columns
persistent_table_distkey
_lock_
string 
PDT distkey column
supports_streaming
_lock_
boolean 
Supports streaming results
automatically_run_sql_runner_snippets
_lock_
boolean 
Should SQL Runner snippets automatically be run
connection_tests
string[] 
supports_inducer
_lock_
boolean 
Is supported with the inducer (i.e. generate from sql)
supports_multiple_databases
_lock_
boolean 
Can multiple databases be accessed from a connection using this dialect
supports_persistent_derived_tables
_lock_
boolean 
Whether the dialect supports allowing Looker to build persistent derived tables
has_ssl_support
_lock_
boolean 
Does the database have client SSL support settable through the JDBC string explicitly?
snippets
Expand Snippet definition... 
name
_lock_
string 
Name of the snippet
label
_lock_
string 
Label of the snippet
sql
_lock_
string 
SQL text of the snippet
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
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


