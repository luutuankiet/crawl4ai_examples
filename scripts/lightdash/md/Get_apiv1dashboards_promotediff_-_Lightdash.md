# Get apiv1dashboards promotediff - Lightdash

**Source:** https://docs.lightdash.com/api-reference/dashboards/get-apiv1dashboards-promotediff

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Dashboards
Get apiv1dashboards promotediff
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

GET
/
api
/
v1
/
dashboards
/
{dashboardUuid}
/
promoteDiff
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
dashboardUuid
string
required
dashboardUuid for the dashboard to check diff
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
Post apiv1dashboards promoteGet apiv1csv
Assistant
Responses are generated using AI and may contain mistakes.


