# Get All Timezones  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/all_timezones

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get a list of timezones that Looker supports (e.g. useful for scheduling tasks).




Was this helpful?
Send feedback 
#  Get All Timezones
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get a list of timezones that Looker supports (e.g. useful for scheduling tasks).


Version 4.0.25.10 (latest) 
### Get a list of timezones that Looker supports (e.g. useful for scheduling tasks).
## Request
GET /timezones 
Datatype
Description
Request
HTTP Request 
## Response
200: Timezone400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
value
_lock_
string 
Timezone
label
_lock_
string 
Description of timezone
group
_lock_
string 
Timezone group (e.g Common, Other, etc.)
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
## Examples
More
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


