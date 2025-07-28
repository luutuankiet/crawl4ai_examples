# Get All Locales  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/all_locales

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get a list of locales that Looker supports.




Was this helpful?
Send feedback 
#  Get All Locales
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get a list of locales that Looker supports.


Version 4.0.25.10 (latest) 
### Get a list of locales that Looker supports.
## Request
GET /locales 
Datatype
Description
Request
HTTP Request 
## Response
400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
code
_lock_
string 
Code for Locale
native_name
_lock_
string 
Name of Locale in its own language
english_name
_lock_
string 
Name of Locale in English
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


