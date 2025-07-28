# LookMLValidatorErrorItem  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LookMLValidatorErrorItem

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  LookMLValidatorErrorItem
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
lookml_error
_lock_
LookMLValidatorError
Details of the LookML that failed validation
Expand LookMLValidatorError definition... 
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
LookML model that contains the error
explore
_lock_
string 
LookML Explore that contains the error
field_name
_lock_
string 
LookML field that caused the error
message
_lock_
string 
Message returned by the LookML validator
severity
_lock_
string 
Severity of the error (warning, error, fatal, info, success)
line_number
_lock_
string 
Line number of the error in the LookML file
lookml_url
_lock_
string 
URL to the LookML that caused the error
file_path
_lock_
string 
IDE folder path to the LookML file that caused the error
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


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


