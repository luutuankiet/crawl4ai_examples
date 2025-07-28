# Method: projects.locations.operations.cancel  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/rest/v1/projects.locations.operations/cancel

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Authorization scopes
Try it! 



Was this helpful?
Send feedback 
#  Method: projects.locations.operations.cancel
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Authorization scopes


  * Path parameters
  * Authorization scopes
  * IAM Permissions


Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use `Operations.GetOperation` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a `google.rpc.Status.code` of `1`, corresponding to `Code.CANCELLED`.
### HTTP request
`POST https://looker.googleapis.com/v1/{name=projects/*/locations/*/operations/*}:cancel`
The URL uses gRPC Transcoding syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation resource to be cancelled.  
### Request body
The request body must be empty.
### Response body
If successful, the response body is an empty JSON object.
### Authorization scopes
Requires the following OAuth scope:
  * `https://www.googleapis.com/auth/cloud-platform`


For more information, see the Authentication Overview.
### IAM Permissions
Requires the following IAM permission on the `name` resource:
  * `looker.operations.cancel`


For more information, see the IAM documentation.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


