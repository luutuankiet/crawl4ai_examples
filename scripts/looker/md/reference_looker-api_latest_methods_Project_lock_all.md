# Lock All  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/lock_all

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  Lock All
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
See more code actions.
Light code theme
Dark code theme
```
  ### Generate Lockfile for All LookML Dependencies

  Git must have been configured, must be in dev mode and deploy permission required

  Install_all is a two step process
  1. For each remote_dependency in a project the dependency manager will resolve any ambiguous ref.
  2. The project will then write out a lockfile including each remote_dependency with its resolved ref.

```

## Request
POST /projects/{project_id}/manifest/lock_all 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
project_id
string 
Id of project
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields
## Response
200: Project Dependency Manager204: Returns 204 if dependencies successfully installed, otherwise 400 with an error message400: Bad Request404: Not Found More
422: Validation Error429: Too Many Requests
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


