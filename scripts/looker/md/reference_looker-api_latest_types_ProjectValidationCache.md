# ProjectValidationCache  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/ProjectValidationCache

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  ProjectValidationCache
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
errors
Expand ProjectError definition... 
code
_lock_
string 
A stable token that uniquely identifies this class of error, ignoring parameter values. Error message text may vary due to parameters or localization, but error codes do not. For example, a "File not found" error will have the same error code regardless of the filename in question or the user's display language
severity
_lock_
string 
Severity: fatal, error, warning, info, success
kind
_lock_
string 
Error classification: syntax, deprecation, model_configuration, etc
message
_lock_
string 
Error message which may contain information such as dashboard or model names that may be considered sensitive in some use cases. Avoid storing or sending this message outside of Looker
field_name
_lock_
string 
The field associated with this error
file_path
_lock_
string 
Name of the file containing this error
line_number
_lock_
integer 
Line number in the file of this error
model_id
_lock_
string 
The model associated with this error
explore
_lock_
string 
The explore associated with this error
help_url
_lock_
string 
A link to Looker documentation about this error
params
_lock_
object 
Error parameters
sanitized_message
_lock_
string 
A version of the error message that does not contain potentially sensitive information. Suitable for situations in which messages are stored or sent to consumers outside of Looker, such as external logs. Sanitized messages will display "(?)" where sensitive information would appear in the corresponding non-sanitized message
project_digest
_lock_
string 
A hash value computed from the project's current state
models_not_validated
ModelsNotValidated[] 
Expand ModelsNotValidated definition... 
name
_lock_
string 
Model name
project_file_id
_lock_
string 
Project file
computation_time
_lock_
number 
Duration of project validation in seconds
stale
_lock_
boolean 
If true, the cached project validation results are no longer accurate because the project has changed since the cached results were calculated
## Related Methods
  * Project/project_validation_results


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


