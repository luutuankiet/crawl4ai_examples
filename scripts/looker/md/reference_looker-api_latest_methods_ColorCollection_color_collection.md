# Get Color Collection by ID  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collection

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get Color Collection by ID
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Get a Color Collection by ID
Use this to retrieve a specific Color Collection. Get a **single** color collection by id with ColorCollection
Get all **standard** color collections with ColorCollection
Get all **custom** color collections with ColorCollection
**Note** : Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.
## Request
GET /color_collections/{collection_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
collection_id
string 
Id of Color Collection
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
### 200: ColorCollection
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


