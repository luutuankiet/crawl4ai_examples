# Update Look  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/update_look

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  Update Look
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
### Modify a Look
Use this function to modify parts of a look. Property values given in a call to `update_look` are applied to the existing look, so there's no need to include properties whose values are not changing. It's best to specify only the properties you want to change and leave everything else out of your `update_look` call. **Look properties marked 'read-only' will be ignored.**
When a user deletes a look in the Looker UI, the look data remains in the database but is marked with a deleted flag ("soft-deleted"). Soft-deleted looks can be undeleted (by an admin) if the delete was in error.
To soft-delete a look via the API, use update_look() to change the look's `deleted` property to `true`. You can undelete a look by calling `update_look` to change the look's `deleted` property to `false`.
Soft-deleted looks are excluded from the results of all_looks() and search_looks(), so they essentially disappear from view even though they still reside in the db. You can pass `deleted: true` as a parameter to search_looks() to list soft-deleted looks.
NOTE: delete_look() performs a "hard delete" - the look data is removed from the Looker database and destroyed. There is no "undo" for `delete_look()`.
## Request
PATCH /looks/{look_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
look_id
string 
Id of look
body
HTTP Body 
Expand HTTP Body definition... 
body
Look
Expand LookWithQuery definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
content_metadata_id
_lock_
string 
Id of content metadata
id
_lock_
string 
Unique Id
title
string 
Look Title
user_id
string 
User Id
content_favorite_id
_lock_
string 
Content Favorite Id
created_at
_lock_
string 
Time that the Look was created.
deleted
boolean 
Whether or not a look is 'soft' deleted.
deleted_at
_lock_
string 
Time that the Look was deleted.
deleter_id
_lock_
string 
Id of User that deleted the look.
description
string 
Description
embed_url
_lock_
string 
Embed Url
excel_file_url
_lock_
string 
Excel File Url
favorite_count
_lock_
integer 
Number of times favorited
google_spreadsheet_formula
_lock_
string 
Google Spreadsheet Formula
image_embed_url
_lock_
string 
Image Embed Url
is_run_on_load
boolean 
auto-run query when Look viewed
last_accessed_at
_lock_
string 
Time that the Look was last accessed by any user
last_updater_id
_lock_
string 
Id of User that last updated the look.
last_viewed_at
_lock_
string 
Time last viewed in the Looker web UI
model
_lock_
Model
public
boolean 
Is Public
public_slug
_lock_
string 
Public Slug
public_url
_lock_
string 
Public Url
query_id
string 
Query Id
short_url
_lock_
string 
Short Url
folder
_lock_
Folder of this Look
folder_id
string 
Folder Id
updated_at
_lock_
string 
Time that the Look was updated.
user_name
_lock_
string 
Name of User that created the look.
view_count
_lock_
integer 
Number of times viewed in the Looker web UI
query
_lock_
Query
url
_lock_
string 
Url
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
content_metadata_id
_lock_
string 
Id of content metadata
id
_lock_
string 
Unique Id
title
string 
Look Title
user_id
string 
User Id
content_favorite_id
_lock_
string 
Content Favorite Id
created_at
_lock_
string 
Time that the Look was created.
deleted
boolean 
Whether or not a look is 'soft' deleted.
deleted_at
_lock_
string 
Time that the Look was deleted.
deleter_id
_lock_
string 
Id of User that deleted the look.
description
string 
Description
embed_url
_lock_
string 
Embed Url
excel_file_url
_lock_
string 
Excel File Url
favorite_count
_lock_
integer 
Number of times favorited
google_spreadsheet_formula
_lock_
string 
Google Spreadsheet Formula
image_embed_url
_lock_
string 
Image Embed Url
is_run_on_load
boolean 
auto-run query when Look viewed
last_accessed_at
_lock_
string 
Time that the Look was last accessed by any user
last_updater_id
_lock_
string 
Id of User that last updated the look.
last_viewed_at
_lock_
string 
Time last viewed in the Looker web UI
model
_lock_
Model
Expand LookModel definition... 
id
_lock_
string 
Model Id
label
_lock_
string 
Model Label
public
boolean 
Is Public
public_slug
_lock_
string 
Public Slug
public_url
_lock_
string 
Public Url
query_id
string 
Query Id
short_url
_lock_
string 
Short Url
folder
_lock_
Folder of this Look
Expand FolderBase definition... 
name
string 
Unique Name
parent_id
string 
Id of Parent. If the parent id is null, this is a root-level entry
id
_lock_
string 
Unique Id
content_metadata_id
_lock_
string 
Id of content metadata
created_at
_lock_
string 
Time the folder was created
creator_id
_lock_
string 
User Id of Creator
child_count
_lock_
integer 
Children Count
external_id
_lock_
string 
Embedder's Id if this folder was autogenerated as an embedding shared folder via 'external_group_id' in an SSO embed login
is_embed
_lock_
boolean 
Folder is an embed folder
is_embed_shared_root
_lock_
boolean 
Folder is the root embed shared folder
is_embed_users_root
_lock_
boolean 
Folder is the root embed users folder
is_personal
_lock_
boolean 
Folder is a user's personal folder
is_personal_descendant
_lock_
boolean 
Folder is descendant of a user's personal folder
is_shared_root
_lock_
boolean 
Folder is the root shared folder
is_users_root
_lock_
boolean 
Folder is the root user folder
can
_lock_
object 
Operations the current user is able to perform on this object
folder_id
string 
Folder Id
updated_at
_lock_
string 
Time that the Look was updated.
user_name
_lock_
string 
Name of User that created the look.
view_count
_lock_
integer 
Number of times viewed in the Looker web UI
query
_lock_
Query
Expand Query definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
model
string 
Model
view
string 
Explore Name
fields
string[] 
pivots
string[] 
fill_fields
string[] 
filters
object 
Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.
filter_expression
string 
Filter Expression
sorts
string[] 
limit
string 
Row limit. To download unlimited results, set the limit to -1 (negative one).
column_limit
string 
Column Limit
total
boolean 
Total
row_total
string 
Raw Total
subtotals
string[] 
vis_config
object 
Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.
filter_config
object 
The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.
visible_ui_sections
string 
Visible UI Sections
slug
_lock_
string 
Slug
dynamic_fields
string 
Dynamic Fields
client_id
string 
Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.
share_url
_lock_
string 
Share Url
expanded_share_url
_lock_
string 
Expanded Share Url
url
_lock_
string 
Expanded Url
query_timezone
string 
Query Timezone
has_table_calculations
_lock_
boolean 
Has Table Calculations
url
_lock_
string 
Url
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
## Examples
More
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/update_look.rb   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


