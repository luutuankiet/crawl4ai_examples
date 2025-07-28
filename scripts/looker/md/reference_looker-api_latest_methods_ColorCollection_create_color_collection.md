# Create ColorCollection  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/create_color_collection

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Create a custom color collection with the specified information




Send feedback 
#  Create ColorCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create a custom color collection with the specified information


Version 4.0.25.10 (latest) 
### Create a custom color collection with the specified information
Creates a new custom color collection object, returning the details, including the created id.
**Update** an existing color collection with Update Color Collection
**Permanently delete** an existing custom color collection with Delete Color Collection
**Note** : Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.
## Request
POST /color_collections 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
ColorCollection
Expand ColorCollection definition... 
id
_lock_
string 
Unique Id
label
string 
Label of color collection
categoricalPalettes
sequentialPalettes
ContinuousPalette[] 
divergingPalettes
ContinuousPalette[] 
## Response
200: ColorCollection400: Bad Request403: Permission Denied404: Not Found409: Resource Already Exists422: Validation Error429: Too Many Requests More
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


