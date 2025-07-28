# Get Mobile_Settings  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/mobile_settings

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get all mobile settings.




Was this helpful?
Send feedback 
#  Get Mobile_Settings
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get all mobile settings.


Version 4.0.25.10 (latest) 
### Get all mobile settings.
## Request
GET /mobile/settings 
Datatype
Description
Request
HTTP Request 
## Response
200: Mobile_Settings400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
mobile_force_authentication
_lock_
boolean 
Specifies whether the force authentication option is enabled for mobile
mobile_app_integration
_lock_
boolean 
Specifies whether mobile access for this instance is enabled.
mobile_feature_flags
MobileFeatureFlags[] 
Expand MobileFeatureFlags definition... 
feature_flag_name
_lock_
string 
Specifies the name of feature flag.
feature_flag_state
_lock_
boolean 
Specifies the state of feature flag
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


