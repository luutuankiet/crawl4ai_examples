# Search Looks  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/search_looks

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  Search Looks
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
### Search Looks
Returns an **array of Look objects** that match the specified search criteria.
If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match _all_ search param criteria will be returned.
If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.
String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example="dan%" will match "danger" and "Danzig" but not "David" example="D_m%" will match "Damage" and "dump"
Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.
Most search params can accept "IS NULL" and "NOT NULL" as special expressions to match or exclude (respectively) rows where the column is null.
Boolean search params accept only "true" and "false" as values.
Get a **single look** by id with look(id)
## Request
GET /looks/search 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
id
string 
Match look id.
title
string 
Match Look title.
description
string 
Match Look description.
content_favorite_id
string 
Select looks with a particular content favorite id
folder_id
string 
Select looks in a particular folder.
user_id
string 
Select looks created by a particular user.
view_count
string 
Select looks with particular view_count value
deleted
boolean 
Select soft-deleted looks
query_id
string 
Select looks that reference a particular query by query_id
curate
boolean 
Exclude items that exist only in personal spaces other than the users
last_viewed_at
string 
Select looks based on when they were last viewed
fields
string 
Requested fields.
page
integer 
DEPRECATED. Use limit and offset instead. Return only page N of paginated results
per_page
integer 
DEPRECATED. Use limit and offset instead. Return N rows of data per page
limit
integer 
Number of results to return. (used with offset and takes priority over page and per_page)
offset
integer 
Number of results to skip before returning any. (used with limit and takes priority over page and per_page)
sorts
string 
One or more fields to sort results by. Sortable fields: [:title, :user_id, :id, :created_at, :space_id, :folder_id, :description, :updated_at, :last_updater_id, :view_count, :favorite_count, :content_favorite_id, :deleted, :deleted_at, :last_viewed_at, :last_accessed_at, :query_id]
filter_or
boolean 
Combine given search criteria in a boolean OR expression
## Response
400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
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
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_look.py   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py   
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestAsync.kt   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestAsync.kt   
https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
---  
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts   
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


