# Post apiv1dashboards promote - Lightdash

**Source:** https://docs.lightdash.com/api-reference/dashboards/post-apiv1dashboards-promote

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Dashboards
Post apiv1dashboards promote
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
    * POST
Post apiv1dashboards promote
    * Get apiv1dashboards promotediff
  * Exports
  * Comments
  * Catalog


200
default
Copy
Ask AI
```

  "results": {
    "description": "<string>",
    "name": "<string>",
    "projectUuid": "<string>",
    "organizationUuid": "<string>",
    "uuid": "<string>",
    "updatedAt": "2023-11-07T05:31:56Z",
    "spaceUuid": "<string>",
    "pinnedListUuid": "<string>",
    "pinnedListOrder": 123,
    "slug": "<string>",
    "spaceName": "<string>",
    "updatedByUser": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "views": 123,
    "firstViewedAt": "<string>",
    "dashboardVersionId": 123,
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



    "tabs": [

        "order": 123,
        "name": "<string>",
        "uuid": "<string>"


    "config": {
      "isDateZoomDisabled": true


  "status": "ok"

```

POST
/
api
/
v1
/
dashboards
/
{dashboardUuid}
/
promote
Try it
200
default
Copy
Ask AI
```

  "results": {
    "description": "<string>",
    "name": "<string>",
    "projectUuid": "<string>",
    "organizationUuid": "<string>",
    "uuid": "<string>",
    "updatedAt": "2023-11-07T05:31:56Z",
    "spaceUuid": "<string>",
    "pinnedListUuid": "<string>",
    "pinnedListOrder": 123,
    "slug": "<string>",
    "spaceName": "<string>",
    "updatedByUser": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "views": 123,
    "firstViewedAt": "<string>",
    "dashboardVersionId": 123,
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



    "tabs": [

        "order": 123,
        "name": "<string>",
        "uuid": "<string>"


    "config": {
      "isDateZoomDisabled": true


  "status": "ok"

```

#### Path Parameters
dashboardUuid
string
required
dashboardUuid for the dashboard to run
#### Response
200
200 default
application/json
Success
results
object
required
From T, pick a set of properties whose keys are in the union K
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1projects git integrationpull requestscustom dimensionsGet apiv1dashboards promotediff
Assistant
Responses are generated using AI and may contain mistakes.


