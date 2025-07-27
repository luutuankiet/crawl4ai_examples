# Post apiv1projects dashboards - Lightdash

**Source:** https://docs.lightdash.com/api-reference/projects/post-apiv1projects-dashboards

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Projects
Post apiv1projects dashboards
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


201
default
Copy
Ask AI
```

  "results": {
    "config": {
      "isDateZoomDisabled": true

    "slug": "<string>",
    "access": [

        "inheritedFrom": "organization",
        "inheritedRole": "member",
        "projectRole": "viewer",
        "hasDirectAccess": true,
        "role": "viewer",
        "email": "<string>",
        "lastName": "<string>",
        "firstName": "<string>",
        "userUuid": "<string>"


    "isPrivate": true,
    "tabs": [

        "order": 123,
        "name": "<string>",
        "uuid": "<string>"


    "pinnedListOrder": 123,
    "pinnedListUuid": "<string>",
    "firstViewedAt": "2023-11-07T05:31:56Z",
    "views": 123,
    "spaceName": "<string>",
    "spaceUuid": "<string>",
    "updatedByUser": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "filters": {
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


      "dimensions": [

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



    "tiles": [

        "uuid": "<string>",
        "type": "saved_chart",
        "x": 123,
        "y": 123,
        "h": 123,
        "w": 123,
        "tabUuid": "<string>",
        "properties": {
          "chartSlug": "<string>",
          "lastVersionChartKind": "line",
          "chartName": "<string>",
          "belongsToDashboard": true,
          "savedChartUuid": "<string>",
          "hideTitle": true,
          "title": "<string>"



    "updatedAt": "2023-11-07T05:31:56Z",
    "description": "<string>",
    "name": "<string>",
    "uuid": "<string>",
    "dashboardVersionId": 123,
    "projectUuid": "<string>",
    "organizationUuid": "<string>"

  "status": "ok"

```

POST
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
Try it
201
default
Copy
Ask AI
```

  "results": {
    "config": {
      "isDateZoomDisabled": true

    "slug": "<string>",
    "access": [

        "inheritedFrom": "organization",
        "inheritedRole": "member",
        "projectRole": "viewer",
        "hasDirectAccess": true,
        "role": "viewer",
        "email": "<string>",
        "lastName": "<string>",
        "firstName": "<string>",
        "userUuid": "<string>"


    "isPrivate": true,
    "tabs": [

        "order": 123,
        "name": "<string>",
        "uuid": "<string>"


    "pinnedListOrder": 123,
    "pinnedListUuid": "<string>",
    "firstViewedAt": "2023-11-07T05:31:56Z",
    "views": 123,
    "spaceName": "<string>",
    "spaceUuid": "<string>",
    "updatedByUser": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "filters": {
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


      "dimensions": [

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



    "tiles": [

        "uuid": "<string>",
        "type": "saved_chart",
        "x": 123,
        "y": 123,
        "h": 123,
        "w": 123,
        "tabUuid": "<string>",
        "properties": {
          "chartSlug": "<string>",
          "lastVersionChartKind": "line",
          "chartName": "<string>",
          "belongsToDashboard": true,
          "savedChartUuid": "<string>",
          "hideTitle": true,
          "title": "<string>"



    "updatedAt": "2023-11-07T05:31:56Z",
    "description": "<string>",
    "name": "<string>",
    "uuid": "<string>",
    "dashboardVersionId": 123,
    "projectUuid": "<string>",
    "organizationUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Query Parameters
duplicateFrom
string
#### Body
application/json
  * Option 1
  * Option 2


dashboardDesc
string
required
dashboardName
string
required
#### Response
201
201 default
application/json
Created
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Get apiv1projects dashboardsPatch apiv1projects dashboards
Assistant
Responses are generated using AI and may contain mistakes.


