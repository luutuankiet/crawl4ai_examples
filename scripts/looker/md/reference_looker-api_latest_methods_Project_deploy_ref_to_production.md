# Deploy Remote Branch or Ref to Production  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/deploy_ref_to_production

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Deploy a Remote Branch or Ref to Production




Was this helpful?
Send feedback 
#  Deploy Remote Branch or Ref to Production
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Deploy a Remote Branch or Ref to Production


Version 4.0.25.10 (latest) 
### Deploy a Remote Branch or Ref to Production
Git must have been configured and deploy permission required.
Deploy is a one/two step process
  1. If this is the first deploy of this project, create the production project with git repository.
  2. Pull the branch or ref into the production project.


Can only specify either a branch or a ref.
## Request
POST /projects/{project_id}/deploy_ref_to_production 
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
branch
string 
Branch to deploy to production
ref
string 
Ref to deploy to production
## Response
204: Returns 204 if project was successfully deployed to production, otherwise 400 with an error message400: Bad Request404: Not Found422: Validation Error More
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


