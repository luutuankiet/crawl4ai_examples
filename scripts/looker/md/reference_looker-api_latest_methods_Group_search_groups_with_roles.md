# Search Groups with Roles  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Group/search_groups_with_roles

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Search groups include roles




Was this helpful?
Send feedback 
#  Search Groups with Roles
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Search groups include roles


Version 4.0.25.10 (latest) 
### Search groups include roles
Returns all group records that match the given search criteria, and attaches any associated roles.
If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match _all_ search param criteria will be returned.
If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.
String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example="dan%" will match "danger" and "Danzig" but not "David" example="D_m%" will match "Damage" and "dump"
Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.
Most search params can accept "IS NULL" and "NOT NULL" as special expressions to match or exclude (respectively) rows where the column is null.
Boolean search params accept only "true" and "false" as values.
## Request
GET /groups/search/with_roles 
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
limit
integer 
Number of results to return (used with `offset`).
offset
integer 
Number of results to skip before returning any (used with `limit`).
sorts
string 
Fields to sort by.
filter_or
boolean 
Combine given search criteria in a boolean OR expression
id
string 
Match group id.
name
string 
Match group name.
external_group_id
string 
Match group external_group_id.
externally_managed
boolean 
Match group externally_managed.
externally_orphaned
boolean 
Match group externally_orphaned.
## Response
400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
can
_lock_
object 
Operations the current user is able to perform on this object
can_add_to_content_metadata
boolean 
Group can be used in content access controls
contains_current_user
_lock_
boolean 
Currently logged in user is group member
external_group_id
_lock_
string 
External Id group if embed group
externally_managed
_lock_
boolean 
Group membership controlled outside of Looker
id
_lock_
string 
Unique Id
include_by_default
_lock_
boolean 
New users are added to this group by default
name
string 
Name of group
user_count
_lock_
integer 
Number of users included in this group
roles
Expand Role definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
name
string 
Name of Role
permission_set
_lock_
(Read only) Permission set
Expand PermissionSet definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
all_access
_lock_
boolean 
built_in
_lock_
boolean 
id
_lock_
string 
Unique Id
name
string 
Name of PermissionSet
permissions
string[] 
url
_lock_
string 
Link to get this item
permission_set_id
string 
(Write-Only) Id of permission set
model_set
_lock_
(Read only) Model set
Expand ModelSet definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
all_access
_lock_
boolean 
built_in
_lock_
boolean 
id
_lock_
string 
Unique Id
models
string[] 
name
string 
Name of ModelSet
url
_lock_
string 
Link to get this item
model_set_id
string 
(Write-Only) Id of model set
url
_lock_
string 
Link to get this item
users_url
_lock_
string 
Link to get list of users with this role
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


