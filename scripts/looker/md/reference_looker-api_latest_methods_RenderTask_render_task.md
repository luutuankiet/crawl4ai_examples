# Get Render Task  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/RenderTask/render_task

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get information about a render task.




Was this helpful?
Send feedback 
#  Get Render Task
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get information about a render task.


Version 4.0.25.10 (latest) 
### Get information about a render task.
Returns a render task object. To check the status of a render task, pass the render_task.id to Get Render Task. Once the render task is complete, you can download the resulting document or image using Get Render Task Results.
## Request
GET /render_tasks/{render_task_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
render_task_id
string 
Id of render task
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: Render Task400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Date/Time render task was created
dashboard_filters
_lock_
string 
Filter values to apply to the dashboard queries, in URL query format
dashboard_id
_lock_
string 
Id of dashboard to render
dashboard_style
_lock_
string 
Dashboard layout style: single_column or tiled
finalized_at
_lock_
string 
Date/Time render task was completed
height
_lock_
integer 
Output height in pixels. Flowed layouts may ignore this value.
id
_lock_
string 
Id of this render task
look_id
_lock_
string 
Id of look to render
lookml_dashboard_id
_lock_
string 
Id of lookml dashboard to render
query_id
_lock_
string 
Id of query to render
dashboard_element_id
_lock_
string 
Id of dashboard element to render: UDD dashboard element would be numeric and LookML dashboard element would be model_name::dashboard_title::lookml_link_id
query_runtime
_lock_
number 
Number of seconds elapsed running queries
render_runtime
_lock_
number 
Number of seconds elapsed rendering data
result_format
_lock_
string 
Output format: pdf, png, or jpg
runtime
_lock_
number 
Total seconds elapsed for render task
status
_lock_
string 
Render task status: enqueued_for_query, querying, enqueued_for_render, rendering, success, failure
status_detail
_lock_
string 
Additional information about the current status
user_id
_lock_
string 
The user account permissions in which the render task will execute
width
_lock_
integer 
Output width in pixels
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
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_pdf.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_look.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_tile.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/render_look_png.rb   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/utils.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/KotlinExample.kt   
---  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


