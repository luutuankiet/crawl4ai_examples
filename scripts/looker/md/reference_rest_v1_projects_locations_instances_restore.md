# Method: projects.locations.instances.restore  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/restore

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  Method: projects.locations.instances.restore
Stay organized with collections  Save and categorize content based on your preferences. 
  * Path parameters
  * Request body
    * JSON representation
  * Authorization scopes
  * IAM Permissions


Restore Looker instance.
### HTTP request
`POST https://looker.googleapis.com/v1/{name=projects/*/locations/*/instances/*}:restore`
The URL uses gRPC Transcoding syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Required. Instance being restored Format: projects/{project}/locations/{location}/instances/{instance}  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "backup": string
}
```
  
Fields  
---  
`backup` |  `string` Required. Backup being used to restore the instance Format: projects/{project}/locations/{location}/instances/{instance}/backups/{backup}  
### Response body
If successful, the response body contains an instance of .
### Authorization scopes
Requires the following OAuth scope:
  * `https://www.googleapis.com/auth/cloud-platform`


For more information, see the Authentication Overview.
### IAM Permissions
Requires the following IAM permission on the `name` resource:
  * `looker.googleapis.com/looker.instances.update`


For more information, see the IAM documentation.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


