# Update Mobile Device Registration  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/update_mobile_device_registration

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Updates the mobile device registration




Was this helpful?
Send feedback 
#  Update Mobile Device Registration
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Updates the mobile device registration


Version 4.0.25.10 (latest) 
### Updates the mobile device registration
## Request
PATCH /mobile/device/{device_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
device_id
string 
Unique id of the device.
## Response
200: Device registration updated successfully.400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(object)
id
_lock_
string 
Unique ID.
device_token
string 
Specifies the device token
device_type
string 
Specifies type of device. Valid values are: "android", "ios".
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


