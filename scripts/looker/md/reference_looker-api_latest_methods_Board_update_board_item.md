# Update Board Item  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Board/update_board_item

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  Update Board Item
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
### Update a board item definition.
## Request
PATCH /board_items/{board_item_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
board_item_id
string 
Id of board item
body
HTTP Body 
Expand HTTP Body definition... 
body
Board Item
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
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
### 200: Board Item
Datatype
Description
(object)
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


