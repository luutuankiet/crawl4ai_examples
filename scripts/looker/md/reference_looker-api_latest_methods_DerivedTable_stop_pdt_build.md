# Stop a PDT materialization  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/stop_pdt_build

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  Stop a PDT materialization
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Stop a PDT materialization
## Request
GET /derived_table/{materialization_id}/stop 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
materialization_id
string 
The materialization id to stop.
query
HTTP Query 
Expand HTTP Query definition... 
source
string 
The source of this request.
## Response
200: Derived Table400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
materialization_id
_lock_
string 
The ID of the enqueued materialization task
resp_text
_lock_
string 
Detailed response in text format
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


