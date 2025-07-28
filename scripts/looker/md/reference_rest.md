# Looker (Google Cloud core) API

**Source:** https://cloud.google.com/looker/docs/reference/rest

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Service: looker.googleapis.com
    * Discovery document
    * Service endpoint
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.backups
  * REST Resource: v1.projects.locations.operations




Was this helpful?
Send feedback 
#  Looker (Google Cloud core) API
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Service: looker.googleapis.com
    * Discovery document
    * Service endpoint
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.backups
  * REST Resource: v1.projects.locations.operations


  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.backups
  * REST Resource: v1.projects.locations.operations


## Service: looker.googleapis.com
To call this service, we recommend that you use the Google-provided client libraries. If your application needs to use your own libraries to call this service, use the following information when you make the API requests.
### Discovery document
A Discovery Document is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:
  * https://looker.googleapis.com/$discovery/rest?version=v1


### Service endpoint
A service endpoint is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:
  * `https://looker.googleapis.com`


## REST Resource: v1.projects.locations
Methods  
---  
`GET /v1/{name=projects/*/locations/*}`  
`GET /v1/{name=projects/*}/locations`  
## REST Resource: v1.projects.locations.instances
Methods  
---  
|  `POST /v1/{parent=projects/*/locations/*}/instances`  
|  `DELETE /v1/{name=projects/*/locations/*/instances/*}`  
|  `POST /v1/{name=projects/*/locations/*/instances/*}:export`  
`GET /v1/{name=projects/*/locations/*/instances/*}`  
|  `POST /v1/{name=projects/*/locations/*/instances/*}:import`  
`GET /v1/{parent=projects/*/locations/*}/instances`  
|  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`  
|  `POST /v1/{name=projects/*/locations/*/instances/*}:restart`  
|  `POST /v1/{name=projects/*/locations/*/instances/*}:restore`  
## REST Resource: v1.projects.locations.instances.backups
Methods  
---  
|  `POST /v1/{parent=projects/*/locations/*/instances/*}/backups`  
|  `DELETE /v1/{name=projects/*/locations/*/instances/*/backups/*}`  
`GET /v1/{name=projects/*/locations/*/instances/*/backups/*}`  
`GET /v1/{parent=projects/*/locations/*/instances/*}/backups`  
## REST Resource: v1.projects.locations.operations
Methods  
---  
|  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`  
|  `DELETE /v1/{name=projects/*/locations/*/operations/*}`  
`GET /v1/{name=projects/*/locations/*/operations/*}`  
`GET /v1/{name=projects/*/locations/*}/operations`  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


