# Get Integration  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Integration/integration

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get information about a Integration.




Send feedback 
#  Get Integration
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get information about a Integration.


Version 4.0.25.10 (latest) 
### Get information about a Integration.
## Request
GET /integrations/{integration_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
integration_id
string 
Id of integration
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
### 200: Integration
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
ID of the integration.
integration_hub_id
_lock_
string 
ID of the integration hub.
label
_lock_
string 
Label for the integration.
description
_lock_
string 
Description of the integration.
enabled
boolean 
Whether the integration is available to users.
params
IntegrationParam[] 
Expand IntegrationParam definition... 
name
string 
Name of the parameter.
label
_lock_
string 
Label of the parameter.
description
_lock_
string 
Short description of the parameter.
required
_lock_
boolean 
Whether the parameter is required to be set to use the destination. If unspecified, this defaults to false.
has_value
_lock_
boolean 
Whether the parameter has a value set.
value
string 
The current value of the parameter. Always null if the value is sensitive. When writing, null values will be ignored. Set the value to an empty string to clear it.
user_attribute_name
string 
When present, the param's value comes from this user attribute instead of the 'value' parameter. Set to null to use the 'value'.
sensitive
_lock_
boolean 
Whether the parameter contains sensitive data like API credentials. If unspecified, this defaults to true.
per_user
_lock_
boolean 
When true, this parameter must be assigned to a user attribute in the admin panel (instead of a constant value), and that value may be updated by the user as part of the integration flow.
delegate_oauth_url
_lock_
string 
When present, the param represents the oauth url the user will be taken to.
supported_formats
string[] 
supported_action_types
string[] 
supported_formattings
string[] 
supported_visualization_formattings
string[] 
supported_download_settings
string[] 
icon_url
_lock_
string 
URL to an icon for the integration.
uses_oauth
_lock_
boolean 
Whether the integration uses oauth.
required_fields
IntegrationRequiredField[] 
Expand IntegrationRequiredField definition... 
tag
_lock_
string 
Matches a field that has this tag.
any_tag
string[] 
all_tags
string[] 
privacy_link
_lock_
string 
Link to privacy policy for destination
delegate_oauth
_lock_
boolean 
Whether the integration uses delegate oauth, which allows federation between an integration installation scope specific entity (like org, group, and team, etc.) and Looker.
installed_delegate_oauth_targets
string[] 
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
## Examples
### Kotlin
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
---  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


