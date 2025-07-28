# Create a Continuous Integration run  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/create_ci_run

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Creates a CI Run.




Was this helpful?
Send feedback 
#  Create a Continuous Integration run
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Creates a CI Run.


Version 4.0.25.10 (latest) 
### Creates a CI Run.
## Request
POST /projects/{project_id}/ci/run 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
project_id
string 
Project Id
body
HTTP Body 
Expand HTTP Body definition... 
body
Options for creating a CI run
Expand CreateCIRunRequest definition... 
suite_id
string 
ID of the CI suite
branch
string 
Branch that the CI run should validate. Omit to test production.
commit
string 
Commit that the CI run should validate. Omit to test production.
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields
## Response
400: Bad Request404: Not Found409: Resource Already Exists422: Validation Error More
429: Too Many Requests
Datatype
Description
(object)
run_id
_lock_
string 
ID of the CI run
status
_lock_
string 
Status of the CI run (unknown, failed, passed, skipped, errored, cancelled, queued, running)
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


