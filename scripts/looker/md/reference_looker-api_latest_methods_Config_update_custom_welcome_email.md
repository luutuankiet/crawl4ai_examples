# Update Custom Welcome Email Content  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_custom_welcome_email

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Update Custom Welcome Email Content
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Update custom welcome email setting and values. Optionally send a test email with the new content to the currently logged in user.
## Request
PATCH /custom_welcome_email 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
Custom Welcome Email setting and value to save
Expand CustomWelcomeEmail definition... 
enabled
boolean 
If true, custom email content will replace the default body of welcome emails
content
string 
The HTML to use as custom content for welcome emails. Script elements and other potentially dangerous markup will be removed.
subject
string 
The text to appear in the email subject line. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.
header
string 
The text to appear in the header line of the email body. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.
query
HTTP Query 
Expand HTTP Query definition... 
send_test_welcome_email
boolean 
If true a test email with the content from the request will be sent to the current user after saving
## Response
### 200: Custom Welcome Email
Datatype
Description
(object)
enabled
boolean 
If true, custom email content will replace the default body of welcome emails
content
string 
The HTML to use as custom content for welcome emails. Script elements and other potentially dangerous markup will be removed.
subject
string 
The text to appear in the email subject line. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.
header
string 
The text to appear in the header line of the email body. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.
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


