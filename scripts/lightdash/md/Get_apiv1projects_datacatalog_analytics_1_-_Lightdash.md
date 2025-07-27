# Get apiv1projects datacatalog analytics 1 - Lightdash

**Source:** https://docs.lightdash.com/api-reference/catalog/get-apiv1projects-datacatalog-analytics-1

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Catalog
Get apiv1projects datacatalog analytics 1
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
    "charts": [
      {
        "name": "<string>",
        "uuid": "<string>",
        "spaceUuid": "<string>",
        "spaceName": "<string>",
        "dashboardUuid": "<string>",
        "dashboardName": "<string>",
        "chartKind": "line"
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
{table}
/
analytics
/
{field}
Try it
200
default
Copy
Ask AI
```
{
  "results": {
    "charts": [
      {
        "name": "<string>",
        "uuid": "<string>",
        "spaceUuid": "<string>",
        "spaceName": "<string>",
        "dashboardUuid": "<string>",
        "dashboardName": "<string>",
        "chartKind": "line"
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
table
string
required
Table where this field belongs
field
string
required
Field name to get analytics for
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Get apiv1projects datacatalog analyticsGet apiv1projects datacatalogmetrics
Assistant
Responses are generated using AI and may contain mistakes.


