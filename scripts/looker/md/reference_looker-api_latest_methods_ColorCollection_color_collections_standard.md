# Get all Standard Color Collections  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collections_standard

Skip to main content 



Console  Sign in
  * On this page
  * Get an array of all existing Standard Color Collections




Send feedback 
#  Get all Standard Color Collections
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get an array of all existing Standard Color Collections


Version 4.0.25.10 (latest) 
### Get an array of all existing **Standard** Color Collections
Get a **single** color collection by id with ColorCollection
Get all **custom** color collections with ColorCollection
**Note** : Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.
## Request
GET /color_collections/standard 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
### 200: ColorCollections
Datatype
Description
(array)
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


