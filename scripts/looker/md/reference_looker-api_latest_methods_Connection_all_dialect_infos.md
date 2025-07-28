# Get All Dialect Infos  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/all_dialect_infos

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get information about all dialects.




Send feedback 
#  Get All Dialect Infos
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get information about all dialects.


Version 4.0.25.10 (latest) 
### Get information about all dialects.
## Request
GET /dialect_info 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: Dialect Info400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
can
_lock_
object 
Operations the current user is able to perform on this object
default_max_connections
_lock_
string 
Default number max connections
default_port
_lock_
string 
Default port number
default_max_queries
_lock_
string 
Default number max queries
default_max_queries_per_user
_lock_
string 
Default number max queries per user
installed
_lock_
boolean 
Is the supporting driver installed
label
_lock_
string 
The human-readable label of the connection
label_for_database_equivalent
_lock_
string 
What the dialect calls the equivalent of a normal SQL table
label_for_schema_equivalent
_lock_
string 
What the dialect calls the equivalent of a schema-level namespace
name
_lock_
string 
The name of the dialect
supported_driver_name
_lock_
string 
The name of the driver used for this dialect
supported_driver_versions
DialectDriverNamesVersion[] 
Expand DialectDriverNamesVersion definition... 
name
_lock_
string 
Name to be passed to the backend
display_name
_lock_
string 
Name to be displayed in the frontend.
supported_options
_lock_
Option support details
Expand DialectInfoOptions definition... 
additional_params
_lock_
boolean 
Has additional params support
after_connect_statements
_lock_
boolean 
Has support for issuing statements after connecting to the database
analytical_view_dataset
_lock_
boolean 
Has analytical view support
auth
_lock_
boolean 
Has auth support
cost_estimate
_lock_
boolean 
Has configurable cost estimation
disable_context_comment
_lock_
boolean 
Can disable query context comments
host
_lock_
boolean 
Host is required
instance_name
_lock_
boolean 
Instance name is required
max_billing_gigabytes
_lock_
boolean 
Has max billing gigabytes support
oauth_credentials
_lock_
boolean 
Has support for a service account
pdts_for_oauth
_lock_
boolean 
Has OAuth for PDT support
port
_lock_
boolean 
Port can be specified
project_name
_lock_
boolean 
Has project name support
schema
_lock_
boolean 
Schema can be specified
service_account_credentials
_lock_
boolean 
Has support for a service account
ssl
_lock_
boolean 
Has TLS/SSL support
timezone
_lock_
boolean 
Has timezone support
tmp_table
_lock_
boolean 
Has tmp table support
tns
_lock_
boolean 
Has Oracle TNS support
username
_lock_
boolean 
Username can be specified
username_required
_lock_
boolean 
Username is required
supports_connection_pooling
_lock_
boolean 
Has support for connection pooling
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
## Examples
More
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


