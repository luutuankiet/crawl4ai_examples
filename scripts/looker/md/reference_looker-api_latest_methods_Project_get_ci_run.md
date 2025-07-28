# Fetch Continuous Integration run  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/get_ci_run

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Fetches a CI Run.




Was this helpful?
Send feedback 
#  Fetch Continuous Integration run
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Fetches a CI Run.


Version 4.0.25.10 (latest) 
### Fetches a CI Run.
## Request
GET /projects/{project_id}/ci/runs/{run_id} 
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
run_id
string 
Run Id
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields
## Response
400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
run
_lock_
Continuous Integration run results
Expand CIRun definition... 
run_id
_lock_
string 
ID of the CI run
created_at
_lock_
string 
Time and date that the CI run was initiated
started_at
_lock_
string 
Time and date that the CI run began executing
finished_at
_lock_
string 
Time and date that the CI run completed
status_url
_lock_
string 
Git provider URL where you can view the commit status. This is the status URL that you specify when you create a CI suite
status
_lock_
string 
Status of the CI run (unknown, failed, passed, skipped, errored, cancelled, queued, running)
git_service
_lock_
string 
Git service for CI run (e.g. GitHub)
git_state
_lock_
Git state information for the CI run
Expand CIGitState definition... 
branch
_lock_
string 
Git branch that the CI run validates
repository
_lock_
string 
Git repository that contains the Git branch being validated
commit_ref
_lock_
string 
Git commit that the CI run validates
target
_lock_
string 
For incremental runs, the Git branch that the CI run compares against during validation
result
_lock_
Results of the CI run
Expand CIRunResult definition... 
sql_result
_lock_
Results of the SQL validation
sql_error
_lock_
Errors that occurred when attempting SQL validation
assert_result
_lock_
AssertValidatorResult
Results of the assert validation
assert_error
_lock_
Errors that occurred when attempting assert validation
content_result
_lock_
ContentValidatorResult
Results of the content validation
content_error
_lock_
Errors that occurred when attempting content validation
lookml_result
_lock_
LookMLValidatorResult
Results of the LookML validation
lookml_error
_lock_
Errors that occurred when attempting LookML validation
generic_error
_lock_
Errors that occurred when attempting validation
schedule
_lock_
Schedule for CI run
Expand CIScheduleTrigger definition... 
enabled
_lock_
boolean 
Whether the CI run schedule is active
day
_lock_
string 
For scheduled runs, day of the week that the CI run is scheduled
hour
_lock_
string 
For schedules runs, the hour of the day (24 hour format) that the CI run is scheduled
frequency
_lock_
string 
For scheduled runs, how often the CI run is scheduled to run (hourly, daily, weekly)
target_branch
_lock_
string 
Git branch that the CI run compares against during validation, used for incremental runs
title
_lock_
string 
Name of the CI suite
trigger
_lock_
string 
Trigger for CI run (unknown, manual, schedule, change_request)
change_request
_lock_
Details of the change request, if the CI run was triggered by a change request
Expand CIChangeRequest definition... 
change_request_number
_lock_
integer 
Numeric identifier of the change request
change_request_url
_lock_
string 
URL of the change request
change_request_name
_lock_
string 
Name of the change request
change_request_commits_url
_lock_
string 
For PR-triggered CI runs, the URL to the change request commit that triggered the run.
suite_id
_lock_
string 
ID of the CI suite
username
_lock_
string 
Username of the user who triggered the CI run, if the CI run was manually triggered
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


