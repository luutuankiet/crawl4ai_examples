# Method: projects.locations.operations.list  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/rest/v1/projects.locations.operations/list

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Query parameters
  * Authorization scopes
Try it! 



Was this helpful?
Send feedback 
#  Method: projects.locations.operations.list
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Query parameters
  * Authorization scopes


  * Path parameters
  * Query parameters
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions


Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.
### HTTP request
`GET https://looker.googleapis.com/v1/{name=projects/*/locations/*}/operations`
The URL uses gRPC Transcoding syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation's parent resource.  
### Query parameters
Parameters  
---  
`filter` |  `string` The standard list filter.  
`pageSize` |  `integer` The standard list page size.  
`pageToken` |  `string` The standard list page token.  
### Request body
The request body must be empty.
### Response body
The response message for `Operations.ListOperations`.
If successful, the response body contains data with the following structure:
JSON representation  
---  
```
{
  "operations": [
    {
      object ()
    }
  ],
  "nextPageToken": string
}
```
  
Fields  
---  
`operations[]` |  `object ()` A list of operations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
### Authorization scopes
Requires the following OAuth scope:
  * `https://www.googleapis.com/auth/cloud-platform`


For more information, see the Authentication Overview.
### IAM Permissions
Requires the following IAM permission on the `name` resource:
  * `looker.operations.list`


For more information, see the IAM documentation.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


