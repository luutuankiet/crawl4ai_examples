# Create Model Set  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Role/create_model_set

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Create Model Set
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Create a model set with the specified information. Model sets are used by Roles.
## Request
POST /model_sets 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
ModelSet
Expand ModelSet definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
all_access
_lock_
boolean 
built_in
_lock_
boolean 
id
_lock_
string 
Unique Id
models
string[] 
name
string 
Name of ModelSet
url
_lock_
string 
Link to get this item
## Response
### 200: Newly created ModelSet
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
all_access
_lock_
boolean 
built_in
_lock_
boolean 
id
_lock_
string 
Unique Id
models
string[] 
name
string 
Name of ModelSet
url
_lock_
string 
Link to get this item
### 400: Bad Request
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
### 409: Resource Already Exists
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
### 422: Validation Error
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


