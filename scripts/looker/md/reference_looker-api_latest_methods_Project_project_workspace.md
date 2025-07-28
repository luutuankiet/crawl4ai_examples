# Get Project Workspace  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/project_workspace

Skip to main content 


  * Español – América Latina

Console  Sign in
  * On this page
  * Get Project Workspace




Send feedback 
#  Get Project Workspace
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get Project Workspace


Version 4.0.25.10 (latest) 
### Get Project Workspace
Returns information about the state of the project files in the currently selected workspace
## Request
GET /projects/{project_id}/current_workspace 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
project_id
string 
Project Id
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields
## Response
### 200: Project Workspace
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
project_id
_lock_
string 
The id of the project
workspace_id
_lock_
string 
The id of the local workspace containing the project files
git_status
_lock_
string 
The status of the local git directory
git_head
_lock_
string 
Git head revision name
dependency_status
_lock_
string 
Status of the dependencies in your project. Valid values are: "lock_optional", "lock_required", "lock_error", "install_none".
git_branch
_lock_
GitBranch
Expand GitBranch definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
name
string 
The short name on the local. Updating `name` results in `git checkout `
remote
_lock_
string 
The name of the remote
remote_name
_lock_
string 
The short name on the remote
error
_lock_
string 
Name of error
message
_lock_
string 
Message describing an error if present
owner_name
_lock_
string 
Name of the owner of a personal branch
readonly
_lock_
boolean 
Whether or not this branch is readonly
personal
_lock_
boolean 
Whether or not this branch is a personal branch - readonly for all developers except the owner
is_local
_lock_
boolean 
Whether or not a local ref exists for the branch
is_remote
_lock_
boolean 
Whether or not a remote ref exists for the branch
is_production
_lock_
boolean 
Whether or not this is the production branch
ahead_count
_lock_
integer 
Number of commits the local branch is ahead of the remote
behind_count
_lock_
integer 
Number of commits the local branch is behind the remote
commit_at
_lock_
integer 
UNIX timestamp at which this branch was last committed.
ref
string 
The resolved ref of this branch. Updating `ref` results in `git reset --hard ``.
remote_ref
_lock_
string 
The resolved ref of this branch remote.
lookml_type
_lock_
string 
The lookml syntax used by all files in this project
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


