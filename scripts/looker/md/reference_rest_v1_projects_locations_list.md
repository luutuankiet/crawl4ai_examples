# Method: projects.locations.list  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/rest/v1/projects.locations/list

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Query parameters
  * Authorization scopes
Try it! 



Send feedback 
#  Method: projects.locations.list
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


Lists information about the supported locations for this service.
### HTTP request
`GET https://looker.googleapis.com/v1/{name=projects/*}/locations`
The URL uses gRPC Transcoding syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The resource that owns the locations collection, if applicable.  
### Query parameters
Parameters  
---  
`filter` |  `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in AIP-160.  
`pageSize` |  `integer` The maximum number of results to return. If not set, the service selects a default.  
`pageToken` |  `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page.  
`extraLocationTypes[]` |  `string` Optional. A list of extra location types that should be used as conditions for controlling the visibility of the locations.  
### Request body
The request body must be empty.
### Response body
The response message for `Locations.ListLocations`.
If successful, the response body contains data with the following structure:
JSON representation  
---  
```
{
  "locations": [
    {
      object ()
    }
  ],
  "nextPageToken": string
}
```
  
Fields  
---  
`locations[]` |  `object ()` A list of locations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
### Authorization scopes
Requires the following OAuth scope:
  * `https://www.googleapis.com/auth/cloud-platform`


For more information, see the Authentication Overview.
### IAM Permissions
Requires the following IAM permission on the `name` resource:
  * `looker.locations.list`


For more information, see the IAM documentation.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


