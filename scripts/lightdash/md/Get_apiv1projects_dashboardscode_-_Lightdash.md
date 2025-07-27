# Get apiv1projects dashboardscode - Lightdash

**Source:** https://docs.lightdash.com/api-reference/projects/get-apiv1projects-dashboardscode

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Projects
Get apiv1projects dashboardscode
##### API


##### Reference
  * Projects
    * Get apiv1snowflakessois authenticated
    * Get apiv1projects validate
    * POST
Post apiv1projects validate
    * Delete apiv1projects validate
    * Get apiv1analyticsuser activity
    * POST
Post apiv1analyticsuser activity download
    * Get apiv1projects spaces
    * POST
Post apiv1projects rename
    * POST
Post apiv1projects renamechart
    * Get apiv1projects renamechart fields
    * Get apiv1projects
    * Get apiv1projects charts
    * Get apiv1projects chart summaries
deprecated
    * Get apiv1projects groupaccesses
    * POST
Post apiv1projects calculate total
    * POST
Post apiv1projects calculate subtotals
    * Get apiv1projects user credentials
    * PATCH
Patch apiv1projects user credentials
    * Get apiv1projects custom metrics
    * PATCH
Patch apiv1projects metadata
    * Get apiv1projects dashboards
    * POST
Post apiv1projects dashboards
    * PATCH
Patch apiv1projects dashboards
    * POST
Post apiv1projects createpreview
    * PATCH
Patch apiv1projects schedulersettings
    * Get apiv1projects tags
    * POST
Post apiv1projects tags
    * Delete apiv1projects tags
    * PATCH
Patch apiv1projects tags
    * Put apiv1projects tagsyaml
    * Get apiv1projects chartscode
    * Get apiv1projects dashboardscode
    * POST
Post apiv1projects charts code
    * POST
Post apiv1projects dashboards code
    * POST
Post apiv1projects dbt cloudwebhook
    * POST
Post apiv1projects refresh
    * Get apiv1projects explores
    * Put apiv1projects explores
    * Get apiv1projects explores 1
    * POST
Post apiv1projects explores compilequery
    * POST
Post apiv1projects explores downloadcsv
    * Get apiv1bigqueryssodatasets
    * Get apiv1bigqueryssois authenticated
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


200
default
Copy
Ask AI
```

  "results": {
    "offset": 123,
    "total": 123,
    "missingIds": [
      "<string>"

    "languageMap": [

        "dashboard": {}


    "dashboards": [

        "description": "<string>",
        "name": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "slug": "<string>",
        "tabs": [

            "order": 123,
            "name": "<string>",
            "uuid": "<string>"


        "filters": {
          "metrics": [

              "values": [
                "<any>"

              "operator": "isNull",
              "id": "<string>",
              "target": {
                "fallbackType": "string",
                "isSqlColumn": true,
                "tableName": "<string>",
                "fieldId": "<string>"

              "settings": "<any>",
              "disabled": true,
              "required": true,
              "singleValue": true,
              "label": "<string>",
              "tileTargets": {}


          "tableCalculations": [

              "values": [
                "<any>"

              "operator": "isNull",
              "id": "<string>",
              "target": {
                "fallbackType": "string",
                "isSqlColumn": true,
                "tableName": "<string>",
                "fieldId": "<string>"

              "settings": "<any>",
              "disabled": true,
              "required": true,
              "singleValue": true,
              "label": "<string>",
              "tileTargets": {}


          "dimensions": [

              "label": "<string>",
              "target": {
                "fallbackType": "string",
                "isSqlColumn": true,
                "tableName": "<string>",
                "fieldId": "<string>"

              "settings": "<any>",
              "disabled": true,
              "required": true,
              "operator": "isNull",
              "values": [
                "<any>"

              "tileTargets": {},
              "singleValue": true



        "downloadedAt": "2023-11-07T05:31:56Z",
        "spaceSlug": "<string>",
        "version": 123,
        "tiles": [

            "type": "saved_chart",
: 123,
: 123,
: 123,
: 123,
            "tabUuid": "<string>",
            "properties": {
              "title": "<string>",
              "hideTitle": true,
              "chartSlug": "<string>",
              "chartName": "<string>"

            "tileSlug": "<string>",
            "uuid": "<string>"





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
dashboards
/
code
Try it
200
default
Copy
Ask AI
```

  "results": {
    "offset": 123,
    "total": 123,
    "missingIds": [
      "<string>"

    "languageMap": [

        "dashboard": {}


    "dashboards": [

        "description": "<string>",
        "name": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "slug": "<string>",
        "tabs": [

            "order": 123,
            "name": "<string>",
            "uuid": "<string>"


        "filters": {
          "metrics": [

              "values": [
                "<any>"

              "operator": "isNull",
              "id": "<string>",
              "target": {
                "fallbackType": "string",
                "isSqlColumn": true,
                "tableName": "<string>",
                "fieldId": "<string>"

              "settings": "<any>",
              "disabled": true,
              "required": true,
              "singleValue": true,
              "label": "<string>",
              "tileTargets": {}


          "tableCalculations": [

              "values": [
                "<any>"

              "operator": "isNull",
              "id": "<string>",
              "target": {
                "fallbackType": "string",
                "isSqlColumn": true,
                "tableName": "<string>",
                "fieldId": "<string>"

              "settings": "<any>",
              "disabled": true,
              "required": true,
              "singleValue": true,
              "label": "<string>",
              "tileTargets": {}


          "dimensions": [

              "label": "<string>",
              "target": {
                "fallbackType": "string",
                "isSqlColumn": true,
                "tableName": "<string>",
                "fieldId": "<string>"

              "settings": "<any>",
              "disabled": true,
              "required": true,
              "operator": "isNull",
              "values": [
                "<any>"

              "tileTargets": {},
              "singleValue": true



        "downloadedAt": "2023-11-07T05:31:56Z",
        "spaceSlug": "<string>",
        "version": 123,
        "tiles": [

            "type": "saved_chart",
: 123,
: 123,
: 123,
: 123,
            "tabUuid": "<string>",
            "properties": {
              "title": "<string>",
              "hideTitle": true,
              "chartSlug": "<string>",
              "chartName": "<string>"

            "tileSlug": "<string>",
            "uuid": "<string>"





  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Query Parameters
ids
string[]
offset
number
languageMap
boolean
#### Response
200
200 default
application/json
Success
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Get apiv1projects chartscodePost apiv1projects charts code
Assistant
Responses are generated using AI and may contain mistakes.


