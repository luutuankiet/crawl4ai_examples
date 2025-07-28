# Update LookML Model  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/update_lookml_model

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Update LookML Model
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Update a lookml model using the specified configuration.
## Request
PATCH /lookml_models/{lookml_model_name} 
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
body
HTTP Body 
Expand HTTP Body definition... 
body
LookML Model
Expand LookmlModel definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
allowed_db_connection_names
string[] 
explores
LookmlModelNavExplore[] 
has_content
_lock_
boolean 
Does this model declaration have have lookml content?
label
_lock_
string 
UI-friendly name for this model
name
string 
Name of the model. Also used as the unique identifier
project_name
string 
Name of project containing the model
unlimited_db_connections
boolean 
Is this model allowed to use all current and future connections
## Response
### 200: LookML Model
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
allowed_db_connection_names
string[] 
explores
LookmlModelNavExplore[] 
Expand LookmlModelNavExplore definition... 
name
_lock_
string 
Name of the explore
description
_lock_
string 
Description for the explore
label
_lock_
string 
Label for the explore
hidden
_lock_
boolean 
Is this explore marked as hidden
group_label
_lock_
string 
Label used to group explores in the navigation menus
has_content
_lock_
boolean 
Does this model declaration have have lookml content?
label
_lock_
string 
UI-friendly name for this model
name
string 
Name of the model. Also used as the unique identifier
project_name
string 
Name of project containing the model
unlimited_db_connections
boolean 
Is this model allowed to use all current and future connections
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


