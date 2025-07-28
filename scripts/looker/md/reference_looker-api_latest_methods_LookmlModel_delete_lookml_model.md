# Delete LookML Model  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/delete_lookml_model

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Delete a lookml model.




Was this helpful?
Send feedback 
#  Delete LookML Model
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Delete a lookml model.


Version 4.0.25.10 (latest) 
### Delete a lookml model.
## Request
DELETE /lookml_models/{lookml_model_name} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
lookml_model_name
string 
Name of lookml model.
## Response
204: Successfully deleted.400: Bad Request404: Not Found429: Too Many Requests More
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
documentation_url
_lock_
string 
Documentation link
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


