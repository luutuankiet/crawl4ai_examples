# Test integration  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Integration/test_integration

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Test integration
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Tests the integration to make sure all the settings are working.
## Request
POST /integrations/{integration_id}/test 
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
## Response
### 200: Test Result
Datatype
Description
(object)
IntegrationTestResult
success
_lock_
boolean 
Whether or not the test was successful
message
_lock_
string 
A message representing the results of the test.
delegate_oauth_result
DelegateOauthTest[] 
Expand DelegateOauthTest definition... 
name
_lock_
string 
Delegate Oauth Connection Name
installation_target_id
_lock_
string 
The ID of the installation target. For Slack, this would be workspace id.
installation_id
_lock_
string 
Installation ID
success
_lock_
boolean 
Whether or not the test was successful
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
## Examples
### Ruby
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/test_integrations.rb   
---  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


