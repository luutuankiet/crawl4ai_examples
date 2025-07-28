# Validate Theme  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Theme/validate_theme

Skip to main content 


  * Español – América Latina

Console  Sign in


Send feedback 
#  Validate Theme
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Validate a theme with the specified information
Validates all values set for the theme, returning any errors encountered, or 200 OK if valid
See Create Theme for constraints
**Note** : Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or https://console.cloud.google.com/support/cases/ to update your license for this feature.
## Request
POST /themes/validate 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Theme
Expand Theme definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
begin_at
string 
Timestamp for when this theme becomes active. Null=always
end_at
string 
Timestamp for when this theme expires. Null=never
id
_lock_
string 
Unique Id
name
string 
Name of theme. Can only be alphanumeric and underscores.
settings
Hash of name/value pairs for theme settings. These names get validated.
## Response
### 200: Theme validation results
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
### 204: No errors detected with the theme
Datatype
Description
(string)
string 
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
## Examples
### Kotlin
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
---  
### TypeScript
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
### Python
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


