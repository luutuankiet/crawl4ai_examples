# Get apiv1projects datacatalogmetricstree - Lightdash

**Source:** https://docs.lightdash.com/api-reference/catalog/get-apiv1projects-datacatalogmetricstree

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Catalog
Get apiv1projects datacatalogmetricstree
##### API


##### Reference
  * Projects
  * My Account
  * User attributes
  * SSH Keypairs
  * SQL runner
  * Spotlight
  * Spaces
  * Roles & Permissions
  * Integrations
  * Share links
  * Schedulers
  * Exploring
  * Charts
  * Content
  * Organizations
  * Notifications
  * Metrics Explorer
  * User Groups
  * API Reference
  * Git Integration
  * Dashboards
  * Exports
  * Comments
  * Catalog
    * Get apiv1projects datacatalog
    * Get apiv1projects datacatalog metadata
    * Get apiv1projects datacatalog analytics
    * Get apiv1projects datacatalog analytics 1
    * Get apiv1projects datacatalogmetrics
    * Get apiv1projects datacatalogmetrics 
    * Get apiv1projects datacatalogmetrics with time dimensions
    * Get apiv1projects datacatalog segment dimensions
    * POST
Post apiv1projects datacatalog categories
    * Delete apiv1projects datacatalog categories
    * PATCH
Patch apiv1projects datacatalog icon
    * Get apiv1projects datacatalogmetricstree
    * POST
Post apiv1projects datacatalogmetricstreeedges
    * Delete apiv1projects datacatalogmetricstreeedges 
    * Get apiv1projects datacatalogmetricshas


200
default
Copy
Ask AI
```
{
  "results": {
    "edges": [
      {
        "projectUuid": "<string>",
        "createdByUserUuid": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "target": {
          "name": "<string>",
          "tableName": "<string>",
          "catalogSearchUuid": "<string>"
        },
        "source": {
          "name": "<string>",
          "tableName": "<string>",
          "catalogSearchUuid": "<string>"
        }
      }
    ]
  },
  "status": "ok"
}
```

GET
/
api
/
v1
/
projects
/
{projectUuid}
/
dataCatalog
/
metrics
/
tree
Try it
200
default
Copy
Ask AI
```
{
  "results": {
    "edges": [
      {
        "projectUuid": "<string>",
        "createdByUserUuid": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "target": {
          "name": "<string>",
          "tableName": "<string>",
          "catalogSearchUuid": "<string>"
        },
        "source": {
          "name": "<string>",
          "tableName": "<string>",
          "catalogSearchUuid": "<string>"
        }
      }
    ]
  },
  "status": "ok"
}
```

#### Path Parameters
projectUuid
string
required
#### Query Parameters
metricUuids
string[]
required
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Patch apiv1projects datacatalog iconPost apiv1projects datacatalogmetricstreeedges
Assistant
Responses are generated using AI and may contain mistakes.


