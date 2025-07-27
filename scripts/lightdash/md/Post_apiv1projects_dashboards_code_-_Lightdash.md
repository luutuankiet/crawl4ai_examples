# Post apiv1projects dashboards code - Lightdash

**Source:** https://docs.lightdash.com/api-reference/projects/post-apiv1projects-dashboards-code

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Projects
Post apiv1projects dashboards code
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
    "charts": [

        "data": {
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
          "dashboardUuid": "<string>",
          "dashboardName": "<string>",
          "updatedByUser": {
            "userUuid": "<string>",
            "firstName": "<string>",
            "lastName": "<string>"

          "tableName": "<string>",
          "metricQuery": {
            "metadata": {
              "hasADateDimension": {
                "name": "<string>",
                "label": "<string>",
                "table": "<string>"


            "timezone": "<string>",
            "metricOverrides": {},
            "customDimensions": [

                "id": "<string>",
                "name": "<string>",
                "table": "<string>",
                "type": "bin",
                "dimensionId": "<string>",
                "binType": "fixed_number",
                "binNumber": 123,
                "binWidth": 123,
                "customRange": [

                    "to": 123,
                    "from": 123




            "additionalMetrics": [

                "label": "<string>",
                "type": "percentile",
                "description": "<string>",
                "sql": "<string>",
                "hidden": true,
                "round": 123,
                "compact": "thousands",
                "format": "km",
                "table": "<string>",
                "name": "<string>",
                "index": 123,
                "filters": [

                    "values": [
                      "<any>"

                    "operator": "isNull",
                    "id": "<string>",
                    "target": {
                      "fieldRef": "<string>"

                    "settings": "<any>",
                    "disabled": true,
                    "required": true


                "baseDimensionName": "<string>",
                "uuid": "<string>",
                "percentile": 123,
                "formatOptions": {
                  "type": "default",
                  "round": 123,
                  "separator": "default",
                  "currency": "<string>",
                  "compact": "thousands",
                  "prefix": "<string>",
                  "suffix": "<string>",
                  "timeInterval": "RAW",
                  "custom": "<string>"



            "tableCalculations": [

                "type": "number",
                "format": {
                  "type": "default",
                  "round": 123,
                  "separator": "default",
                  "currency": "<string>",
                  "compact": "thousands",
                  "prefix": "<string>",
                  "suffix": "<string>",
                  "timeInterval": "RAW",
                  "custom": "<string>"

                "sql": "<string>",
                "displayName": "<string>",
                "name": "<string>",
                "index": 123


            "limit": 123,
            "sorts": [

                "descending": true,
                "fieldId": "<string>"


            "filters": {
              "tableCalculations": {
                "or": [
                  "<any>"

                "id": "<string>"

              "metrics": {
                "or": [
                  "<any>"

                "id": "<string>"

              "dimensions": {
                "or": [
                  "<any>"

                "id": "<string>"


            "metrics": [
              "<string>"

            "dimensions": [
              "<string>"

            "exploreName": "<string>"

          "pivotConfig": {
            "columns": [
              "<string>"


          "chartConfig": {
            "config": {
              "comparisonLabel": "<string>",
              "flipColors": true,
              "comparisonFormat": "raw",
              "showComparison": true,
              "showBigNumberLabel": true,
              "selectedField": "<string>",
              "style": "thousands",
              "label": "<string>"

            "type": "big_number"

          "tableConfig": {
            "columnOrder": [
              "<string>"


          "parameters": {},
          "colorPalette": [
            "<string>"

          "oldUuid": "<string>",
          "spacePath": "<string>",
          "spaceSlug": "<string>"

        "action": "no changes"


    "dashboards": [

        "data": {
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
: 123,
: 123,
: 123,
: 123,
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

          "spacePath": "<string>",
          "spaceSlug": "<string>"

        "action": "no changes"


    "spaces": [

        "data": {
          "name": "<string>",
          "projectUuid": "<string>",
          "organizationUuid": "<string>",
          "uuid": "<string>",
          "access": [
            "<string>"

          "isPrivate": true,
          "pinnedListUuid": "<string>",
          "pinnedListOrder": 123,
          "slug": "<string>",
          "parentSpaceUuid": "<string>",
          "path": "<string>",
          "chartCount": 123,
          "dashboardCount": 123

        "action": "no changes"



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
/
{slug}
/
code
Try it
200
default
Copy
Ask AI
```

  "results": {
    "charts": [

        "data": {
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
          "dashboardUuid": "<string>",
          "dashboardName": "<string>",
          "updatedByUser": {
            "userUuid": "<string>",
            "firstName": "<string>",
            "lastName": "<string>"

          "tableName": "<string>",
          "metricQuery": {
            "metadata": {
              "hasADateDimension": {
                "name": "<string>",
                "label": "<string>",
                "table": "<string>"


            "timezone": "<string>",
            "metricOverrides": {},
            "customDimensions": [

                "id": "<string>",
                "name": "<string>",
                "table": "<string>",
                "type": "bin",
                "dimensionId": "<string>",
                "binType": "fixed_number",
                "binNumber": 123,
                "binWidth": 123,
                "customRange": [

                    "to": 123,
                    "from": 123




            "additionalMetrics": [

                "label": "<string>",
                "type": "percentile",
                "description": "<string>",
                "sql": "<string>",
                "hidden": true,
                "round": 123,
                "compact": "thousands",
                "format": "km",
                "table": "<string>",
                "name": "<string>",
                "index": 123,
                "filters": [

                    "values": [
                      "<any>"

                    "operator": "isNull",
                    "id": "<string>",
                    "target": {
                      "fieldRef": "<string>"

                    "settings": "<any>",
                    "disabled": true,
                    "required": true


                "baseDimensionName": "<string>",
                "uuid": "<string>",
                "percentile": 123,
                "formatOptions": {
                  "type": "default",
                  "round": 123,
                  "separator": "default",
                  "currency": "<string>",
                  "compact": "thousands",
                  "prefix": "<string>",
                  "suffix": "<string>",
                  "timeInterval": "RAW",
                  "custom": "<string>"



            "tableCalculations": [

                "type": "number",
                "format": {
                  "type": "default",
                  "round": 123,
                  "separator": "default",
                  "currency": "<string>",
                  "compact": "thousands",
                  "prefix": "<string>",
                  "suffix": "<string>",
                  "timeInterval": "RAW",
                  "custom": "<string>"

                "sql": "<string>",
                "displayName": "<string>",
                "name": "<string>",
                "index": 123


            "limit": 123,
            "sorts": [

                "descending": true,
                "fieldId": "<string>"


            "filters": {
              "tableCalculations": {
                "or": [
                  "<any>"

                "id": "<string>"

              "metrics": {
                "or": [
                  "<any>"

                "id": "<string>"

              "dimensions": {
                "or": [
                  "<any>"

                "id": "<string>"


            "metrics": [
              "<string>"

            "dimensions": [
              "<string>"

            "exploreName": "<string>"

          "pivotConfig": {
            "columns": [
              "<string>"


          "chartConfig": {
            "config": {
              "comparisonLabel": "<string>",
              "flipColors": true,
              "comparisonFormat": "raw",
              "showComparison": true,
              "showBigNumberLabel": true,
              "selectedField": "<string>",
              "style": "thousands",
              "label": "<string>"

            "type": "big_number"

          "tableConfig": {
            "columnOrder": [
              "<string>"


          "parameters": {},
          "colorPalette": [
            "<string>"

          "oldUuid": "<string>",
          "spacePath": "<string>",
          "spaceSlug": "<string>"

        "action": "no changes"


    "dashboards": [

        "data": {
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
: 123,
: 123,
: 123,
: 123,
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

          "spacePath": "<string>",
          "spaceSlug": "<string>"

        "action": "no changes"


    "spaces": [

        "data": {
          "name": "<string>",
          "projectUuid": "<string>",
          "organizationUuid": "<string>",
          "uuid": "<string>",
          "access": [
            "<string>"

          "isPrivate": true,
          "pinnedListUuid": "<string>",
          "pinnedListOrder": 123,
          "slug": "<string>",
          "parentSpaceUuid": "<string>",
          "path": "<string>",
          "chartCount": 123,
          "dashboardCount": 123

        "action": "no changes"



  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
slug
string
required
#### Body
application/json
From T, pick a set of properties whose keys are in the union K
name
string
required
updatedAt
string<date-time>
required
slug
string
required
tabs
object[]
required
Show child attributes
version
number
required
spaceSlug
string
required
tiles
any
required
This AnyType is an alias for any The goal is to make it easier to identify any type in the codebase without having to eslint-disable all the time These are only used on legacy `any` types, don't use it for new types. This is added on a separate file to avoid circular dependencies.
filters
any
required
This AnyType is an alias for any The goal is to make it easier to identify any type in the codebase without having to eslint-disable all the time These are only used on legacy `any` types, don't use it for new types. This is added on a separate file to avoid circular dependencies.
downloadedAt
string<date-time>
description
string | null
skipSpaceCreate
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
Post apiv1projects charts codePost apiv1projects dbt cloudwebhook
Assistant
Responses are generated using AI and may contain mistakes.


