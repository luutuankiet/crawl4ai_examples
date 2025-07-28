# LookmlTestResult  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlTestResult

Skip to main content 


  * Español – América Latina

Console 


Was this helpful?
Send feedback 
#  LookmlTestResult
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
can
_lock_
object 
Operations the current user is able to perform on this object
model_name
_lock_
string 
Name of model containing this test.
test_name
_lock_
string 
Name of this test.
assertions_count
_lock_
integer 
Number of assertions in this test
assertions_failed
_lock_
integer 
Number of assertions passed in this test
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
warnings
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
success
_lock_
boolean 
True if this test passsed without errors.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


