# Get apiv1projects datacatalog metadata - Lightdash

**Source:** https://docs.lightdash.com/api-reference/catalog/get-apiv1projects-datacatalog-metadata

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Catalog
Get apiv1projects datacatalog metadata
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

  "results": {
    "fieldType": "metric",
    "tableLabel": "<string>",
    "joinedTables": [
      "<string>"

    "fields": [

        "description": "<string>",
        "name": "<string>",
        "label": "<string>",
        "fieldType": "metric",
        "tableLabel": "<string>",
        "requiredAttributes": {},
        "icon": {
          "unicode": "<string>"

        "chartUsage": 123,
        "categories": [

            "name": "<string>",
            "color": "<string>",
            "tagUuid": "<string>",
            "yamlReference": "<string>"


        "tags": [
          "<string>"

        "tableGroupLabel": "<string>",
        "tableName": "<string>",
        "basicType": "<string>",
        "type": "field",
        "catalogSearchUuid": "<string>"


    "source": "<string>",
    "modelName": "<string>",
    "label": "<string>",
    "description": "<string>",
    "name": "<string>"

  "status": "ok"

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
metadata
Try it
200
default
Copy
Ask AI
```

  "results": {
    "fieldType": "metric",
    "tableLabel": "<string>",
    "joinedTables": [
      "<string>"

    "fields": [

        "description": "<string>",
        "name": "<string>",
        "label": "<string>",
        "fieldType": "metric",
        "tableLabel": "<string>",
        "requiredAttributes": {},
        "icon": {
          "unicode": "<string>"

        "chartUsage": 123,
        "categories": [

            "name": "<string>",
            "color": "<string>",
            "tagUuid": "<string>",
            "yamlReference": "<string>"


        "tags": [
          "<string>"

        "tableGroupLabel": "<string>",
        "tableName": "<string>",
        "basicType": "<string>",
        "type": "field",
        "catalogSearchUuid": "<string>"


    "source": "<string>",
    "modelName": "<string>",
    "label": "<string>",
    "description": "<string>",
    "name": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
table
string
required
Table name to get metadata for
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Get apiv1projects datacatalogGet apiv1projects datacatalog analytics
Assistant
Responses are generated using AI and may contain mistakes.


