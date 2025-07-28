# UserLoginLockout  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/UserLoginLockout

Skip to main content 


  * Español – América Latina

Console 


Send feedback 
#  UserLoginLockout
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
key
_lock_
string 
Hash of user's client id
auth_type
_lock_
string 
Authentication method for login failures
ip
_lock_
string 
IP address of most recent failed attempt
user_id
_lock_
string 
User ID
remote_id
_lock_
string 
Remote ID of user if using LDAP
full_name
_lock_
string 
User's name
email
_lock_
string 
Email address associated with the user's account
fail_count
_lock_
integer 
Number of failures that triggered the lockout
lockout_at
_lock_
string 
Time when lockout was triggered
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


