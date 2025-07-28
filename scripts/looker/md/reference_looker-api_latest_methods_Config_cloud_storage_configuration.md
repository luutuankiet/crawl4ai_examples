# Get Cloud Storage  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/cloud_storage_configuration

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Send feedback 
#  Get Cloud Storage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Get the current Cloud Storage Configuration.
## Request
GET /cloud_storage 
Datatype
Description
Request
HTTP Request 
## Response
200: Current Cloud Storage Configuration400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
type
string 
Type of backup: looker-s3 or custom-s3
custom_s3_bucket
string 
Name of bucket for custom-s3 backups
custom_s3_bucket_region
string 
Name of region where the bucket is located
custom_s3_key
string 
(Write-Only) AWS S3 key used for custom-s3 backups
custom_s3_secret
string 
(Write-Only) AWS S3 secret used for custom-s3 backups
url
_lock_
string 
Link to get this item
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
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


