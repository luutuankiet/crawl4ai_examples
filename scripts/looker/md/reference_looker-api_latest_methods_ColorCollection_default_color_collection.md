# Get Default Color Collection  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/default_color_collection

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get the default color collection




Was this helpful?
Send feedback 
#  Get Default Color Collection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get the default color collection


Version 4.0.25.10 (latest) 
### Get the default color collection
Use this to retrieve the default Color Collection.
Set the default color collection with ColorCollection
## Request
GET /color_collections/default 
Datatype
Description
Request
HTTP Request 
## Response
200: ColorCollection400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
id
_lock_
string 
Unique Id
label
string 
Label of color collection
categoricalPalettes
Expand DiscretePalette definition... 
id
_lock_
string 
Unique identity string
label
string 
Label for palette
type
string 
Type of palette
colors
string[] 
sequentialPalettes
ContinuousPalette[] 
Expand ContinuousPalette definition... 
id
_lock_
string 
Unique identity string
label
string 
Label for palette
type
string 
Type of palette
stops
Expand ColorStop definition... 
color
string 
CSS color string
offset
integer 
Offset in continuous palette (0 to 100)
divergingPalettes
ContinuousPalette[] 
Expand ContinuousPalette definition... 
id
_lock_
string 
Unique identity string
label
string 
Label for palette
type
string 
Type of palette
stops
Expand ColorStop definition... 
color
string 
CSS color string
offset
integer 
Offset in continuous palette (0 to 100)
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
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


