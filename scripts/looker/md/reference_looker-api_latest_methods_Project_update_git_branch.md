# Update Project Git Branch  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/update_git_branch

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Checkout and/or reset --hard an existing Git Branch




Was this helpful?
Send feedback 
#  Update Project Git Branch
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Checkout and/or reset --hard an existing Git Branch


Version 4.0.25.10 (latest) 
### Checkout and/or reset --hard an existing Git Branch
Only allowed in development mode
  * Call `update_session` to select the 'dev' workspace.


Checkout an existing branch if name field is different from the name of the currently checked out branch.
Optionally specify a branch name, tag name or commit SHA to which the branch should be reset. **DANGER** hard reset will be force pushed to the remote. Unsaved changes and commits may be permanently lost.
## Request
PUT /projects/{project_id}/git_branch 
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
body
HTTP Body 
Expand HTTP Body definition... 
body
Git Branch
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
## Response
200: Git Branch400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(object)
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
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/validateBranch.ts   
---  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


