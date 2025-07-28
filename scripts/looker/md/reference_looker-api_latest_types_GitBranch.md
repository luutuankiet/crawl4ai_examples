# GitBranch  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/GitBranch

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  GitBranch
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
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
## Related Methods
  * Project/create_git_branch
  * Project/update_git_branch
  * Project/find_git_branch


## Related Types


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


