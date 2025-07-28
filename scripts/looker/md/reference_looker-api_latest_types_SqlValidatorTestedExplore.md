# SqlValidatorTestedExplore  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/SqlValidatorTestedExplore

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  SqlValidatorTestedExplore
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
model
_lock_
string 
LookML model that was tested
explore
_lock_
string 
LookML Explore that was tested
status
_lock_
string 
Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)
skip_reason
_lock_
string 
Reason the validation was skipped
error_count
_lock_
integer 
Total number of failed validations
errors
SqlValidatorErrorItem[] 
Expand SqlValidatorErrorItem definition... 
sql_error
_lock_
Details of the LookML that failed validation
Expand SqlValidatorError definition... 
type
_lock_
string 
A URI reference that identifies the problem type
title
_lock_
string 
Overview of the error
detail
_lock_
string 
Detail of the error
status
_lock_
string 
The HTTP status code for the problem
instance
_lock_
string 
URI reference that identifies the specific occurrence of the problem
model
_lock_
string 
LookML model that contains the Explore that failed SQL validation
explore
_lock_
string 
LookML Explore that failed SQL validation
message
_lock_
string 
Message returned by the SQL validation
explore_url
_lock_
string 
URL to the Explore
lookml_url
_lock_
string 
URL to the LookML that caused the error
dimension
_lock_
string 
LookML dimension that caused the error
line_number
_lock_
string 
Line of the error in the LookML file
generic_error
_lock_
Error that occurred when attempting to run validation
Expand GenericError definition... 
type
_lock_
string 
A URI reference that identifies the problem type
title
_lock_
string 
Overview of the error
detail
_lock_
string 
Detail of the error
status
_lock_
string 
The HTTP status code for the problem
instance
_lock_
string 
URI reference that identifies the specific occurrence of the problem
## Related Types


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


