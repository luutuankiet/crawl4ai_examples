# Get All Board sections  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Board/all_board_sections

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Get All Board sections
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Get information about all board sections.
## Request
GET /board_sections 
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
sorts
string 
Fields to sort by.
## Response
### 200: Board section
Datatype
Description
(array)
can
_lock_
object 
Operations the current user is able to perform on this object
created_at
_lock_
string 
Time at which this section was created.
deleted_at
string 
Time at which this section was deleted.
description
string 
Description of the content found in this section.
board_id
string 
Id reference to parent board
board_items
Expand BoardItem definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
content_created_by
_lock_
string 
Name of user who created the content this item is based on
content_favorite_id
_lock_
string 
Content favorite id associated with the item this content is based on
content_metadata_id
_lock_
string 
Content metadata id associated with the item this content is based on
content_updated_at
_lock_
string 
Last time the content that this item is based on was updated
custom_description
string 
Custom description entered by the user, if present
custom_title
string 
Custom title entered by the user, if present
custom_url
string 
Custom url entered by the user, if present
dashboard_id
string 
Dashboard to base this item on
description
_lock_
string 
The actual description for display
favorite_count
_lock_
integer 
Number of times content has been favorited, if present
board_section_id
string 
Associated Board Section
id
_lock_
string 
Unique Id
image_url
_lock_
string 
The actual image_url for display
location
_lock_
string 
The container folder name of the content
look_id
string 
Look to base this item on
lookml_dashboard_id
string 
LookML Dashboard to base this item on
order
integer 
An arbitrary integer representing the sort order within the section
title
_lock_
string 
The actual title for display
url
_lock_
string 
Relative url for the associated content
use_custom_description
boolean 
Whether the custom description should be used instead of the content description, if the item is associated with content
use_custom_title
boolean 
Whether the custom title should be used instead of the content title, if the item is associated with content
use_custom_url
boolean 
Whether the custom url should be used instead of the content url, if the item is associated with content
view_count
_lock_
integer 
Number of times content has been viewed, if present
custom_image_data_base64
string 
(Write-Only) base64 encoded image data
custom_image_url
_lock_
string 
Custom image_url entered by the user, if present
use_custom_image
boolean 
Whether the custom image should be used instead of the content image, if the item is associated with content
id
_lock_
string 
Unique Id
item_order
string[] 
visible_item_order
string[] 
title
string 
Name of row
updated_at
_lock_
string 
Time at which this section was last updated.
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


