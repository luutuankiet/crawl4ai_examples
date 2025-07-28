# Method: projects.locations.get  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/rest/v1/projects.locations/get

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Authorization scopes
Try it! 



Send feedback 
#  Method: projects.locations.get
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * Authorization scopes


  * Path parameters
  * Authorization scopes
  * IAM Permissions


Gets information about a location.
### HTTP request
`GET https://looker.googleapis.com/v1/{name=projects/*/locations/*}`
The URL uses gRPC Transcoding syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Resource name for the location.  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of .
### Authorization scopes
Requires the following OAuth scope:
  * `https://www.googleapis.com/auth/cloud-platform`


For more information, see the Authentication Overview.
### IAM Permissions
Requires the following IAM permission on the `name` resource:
  * `looker.locations.get`


For more information, see the IAM documentation.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


