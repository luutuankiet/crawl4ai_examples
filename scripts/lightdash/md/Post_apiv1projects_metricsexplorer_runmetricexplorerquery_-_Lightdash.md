# Post apiv1projects metricsexplorer runmetricexplorerquery - Lightdash

**Source:** https://docs.lightdash.com/api-reference/metrics-explorer/post-apiv1projects-metricsexplorer-runmetricexplorerquery

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Metrics Explorer
Post apiv1projects metricsexplorer runmetricexplorerquery
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
    * POST
Post apiv1projects metricsexplorer runmetricexplorerquery
    * POST
Post apiv1projects metricsexplorer runmetrictotal
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
    "hasFilteredSeries": true,
    "results": [

        "compareMetric": {
          "label": "<string>",
          "value": 123

        "metric": {
          "label": "<string>",
          "value": 123

        "segment": "<string>",
        "date": "2023-11-07T05:31:56Z",
        "dateValue": 123


    "fields": {},
    "segmentDimension": {
      "fieldType": "dimension",
      "type": "string",
      "name": "<string>",
      "label": "<string>",
      "table": "<string>",
      "tableLabel": "<string>",
      "sql": "<string>",
      "description": "<string>",
      "source": {
        "content": "<string>",
        "highlight": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "range": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "path": "<string>"

      "hidden": true,
      "compact": "thousands",
      "round": 123,
      "format": "km",
      "groupLabel": "<string>",
      "groups": [
        "<string>"

      "urls": [

          "label": "<string>",
          "url": "<string>"


      "index": 123,
      "tags": [
        "<string>"

      "parameterReferences": [
        "<string>"

      "group": "<string>",
      "requiredAttributes": {},
      "timeInterval": "RAW",
      "timeIntervalBaseDimensionName": "<string>",
      "isAdditionalDimension": true,
      "colors": {},
      "isIntervalBase": true,
      "aiHint": "<string>"

    "compareMetric": {
      "fieldType": "metric",
      "type": "percentile",
      "name": "<string>",
      "label": "<string>",
      "table": "<string>",
      "tableLabel": "<string>",
      "sql": "<string>",
      "description": "<string>",
      "source": {
        "content": "<string>",
        "highlight": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "range": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "path": "<string>"

      "hidden": true,
      "compact": "thousands",
      "round": 123,
      "format": "km",
      "groupLabel": "<string>",
      "groups": [
        "<string>"

      "urls": [

          "label": "<string>",
          "url": "<string>"


      "index": 123,
      "tags": [
        "<string>"

      "parameterReferences": [
        "<string>"

      "showUnderlyingValues": [
        "<string>"

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

      "dimensionReference": "<string>",
      "requiredAttributes": {},
      "defaultTimeDimension": {
        "interval": "RAW",
        "field": "<string>"

      "spotlight": {
        "categories": [
          "<string>"

        "visibility": "show"

      "aiHint": "<string>",
      "tablesRequiredAttributes": {},
      "tablesReferences": [
        "<string>"

      "compiledSql": "<string>",
      "availableTimeDimensions": [

          "fieldType": "dimension",
          "type": "date",
          "name": "<string>",
          "label": "<string>",
          "table": "<string>",
          "tableLabel": "<string>",
          "sql": "<string>",
          "description": "<string>",
          "source": {
            "content": "<string>",
            "highlight": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "range": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "path": "<string>"

          "hidden": true,
          "compact": "thousands",
          "round": 123,
          "format": "km",
          "groupLabel": "<string>",
          "groups": [
            "<string>"

          "urls": [

              "label": "<string>",
              "url": "<string>"


          "index": 123,
          "tags": [
            "<string>"

          "parameterReferences": [
            "<string>"

          "group": "<string>",
          "requiredAttributes": {},
          "timeInterval": "RAW",
          "timeIntervalBaseDimensionName": "<string>",
          "isAdditionalDimension": true,
          "colors": {},
          "isIntervalBase": true,
          "aiHint": "<string>",
          "tablesRequiredAttributes": {},
          "tablesReferences": [
            "<string>"

          "compiledSql": "<string>"


      "timeDimension": {
        "interval": "RAW",
        "field": "<string>",
        "table": "<string>"


    "metric": {
      "fieldType": "metric",
      "type": "percentile",
      "name": "<string>",
      "label": "<string>",
      "table": "<string>",
      "tableLabel": "<string>",
      "sql": "<string>",
      "description": "<string>",
      "source": {
        "content": "<string>",
        "highlight": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "range": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "path": "<string>"

      "hidden": true,
      "compact": "thousands",
      "round": 123,
      "format": "km",
      "groupLabel": "<string>",
      "groups": [
        "<string>"

      "urls": [

          "label": "<string>",
          "url": "<string>"


      "index": 123,
      "tags": [
        "<string>"

      "parameterReferences": [
        "<string>"

      "showUnderlyingValues": [
        "<string>"

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

      "dimensionReference": "<string>",
      "requiredAttributes": {},
      "defaultTimeDimension": {
        "interval": "RAW",
        "field": "<string>"

      "spotlight": {
        "categories": [
          "<string>"

        "visibility": "show"

      "aiHint": "<string>",
      "tablesRequiredAttributes": {},
      "tablesReferences": [
        "<string>"

      "compiledSql": "<string>",
      "availableTimeDimensions": [

          "fieldType": "dimension",
          "type": "date",
          "name": "<string>",
          "label": "<string>",
          "table": "<string>",
          "tableLabel": "<string>",
          "sql": "<string>",
          "description": "<string>",
          "source": {
            "content": "<string>",
            "highlight": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "range": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "path": "<string>"

          "hidden": true,
          "compact": "thousands",
          "round": 123,
          "format": "km",
          "groupLabel": "<string>",
          "groups": [
            "<string>"

          "urls": [

              "label": "<string>",
              "url": "<string>"


          "index": 123,
          "tags": [
            "<string>"

          "parameterReferences": [
            "<string>"

          "group": "<string>",
          "requiredAttributes": {},
          "timeInterval": "RAW",
          "timeIntervalBaseDimensionName": "<string>",
          "isAdditionalDimension": true,
          "colors": {},
          "isIntervalBase": true,
          "aiHint": "<string>",
          "tablesRequiredAttributes": {},
          "tablesReferences": [
            "<string>"

          "compiledSql": "<string>"


      "timeDimension": {
        "interval": "RAW",
        "field": "<string>",
        "table": "<string>"



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
metricsExplorer
/
{explore}
/
{metric}
/
runMetricExplorerQuery
Try it
200
default
Copy
Ask AI
```

  "results": {
    "hasFilteredSeries": true,
    "results": [

        "compareMetric": {
          "label": "<string>",
          "value": 123

        "metric": {
          "label": "<string>",
          "value": 123

        "segment": "<string>",
        "date": "2023-11-07T05:31:56Z",
        "dateValue": 123


    "fields": {},
    "segmentDimension": {
      "fieldType": "dimension",
      "type": "string",
      "name": "<string>",
      "label": "<string>",
      "table": "<string>",
      "tableLabel": "<string>",
      "sql": "<string>",
      "description": "<string>",
      "source": {
        "content": "<string>",
        "highlight": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "range": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "path": "<string>"

      "hidden": true,
      "compact": "thousands",
      "round": 123,
      "format": "km",
      "groupLabel": "<string>",
      "groups": [
        "<string>"

      "urls": [

          "label": "<string>",
          "url": "<string>"


      "index": 123,
      "tags": [
        "<string>"

      "parameterReferences": [
        "<string>"

      "group": "<string>",
      "requiredAttributes": {},
      "timeInterval": "RAW",
      "timeIntervalBaseDimensionName": "<string>",
      "isAdditionalDimension": true,
      "colors": {},
      "isIntervalBase": true,
      "aiHint": "<string>"

    "compareMetric": {
      "fieldType": "metric",
      "type": "percentile",
      "name": "<string>",
      "label": "<string>",
      "table": "<string>",
      "tableLabel": "<string>",
      "sql": "<string>",
      "description": "<string>",
      "source": {
        "content": "<string>",
        "highlight": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "range": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "path": "<string>"

      "hidden": true,
      "compact": "thousands",
      "round": 123,
      "format": "km",
      "groupLabel": "<string>",
      "groups": [
        "<string>"

      "urls": [

          "label": "<string>",
          "url": "<string>"


      "index": 123,
      "tags": [
        "<string>"

      "parameterReferences": [
        "<string>"

      "showUnderlyingValues": [
        "<string>"

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

      "dimensionReference": "<string>",
      "requiredAttributes": {},
      "defaultTimeDimension": {
        "interval": "RAW",
        "field": "<string>"

      "spotlight": {
        "categories": [
          "<string>"

        "visibility": "show"

      "aiHint": "<string>",
      "tablesRequiredAttributes": {},
      "tablesReferences": [
        "<string>"

      "compiledSql": "<string>",
      "availableTimeDimensions": [

          "fieldType": "dimension",
          "type": "date",
          "name": "<string>",
          "label": "<string>",
          "table": "<string>",
          "tableLabel": "<string>",
          "sql": "<string>",
          "description": "<string>",
          "source": {
            "content": "<string>",
            "highlight": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "range": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "path": "<string>"

          "hidden": true,
          "compact": "thousands",
          "round": 123,
          "format": "km",
          "groupLabel": "<string>",
          "groups": [
            "<string>"

          "urls": [

              "label": "<string>",
              "url": "<string>"


          "index": 123,
          "tags": [
            "<string>"

          "parameterReferences": [
            "<string>"

          "group": "<string>",
          "requiredAttributes": {},
          "timeInterval": "RAW",
          "timeIntervalBaseDimensionName": "<string>",
          "isAdditionalDimension": true,
          "colors": {},
          "isIntervalBase": true,
          "aiHint": "<string>",
          "tablesRequiredAttributes": {},
          "tablesReferences": [
            "<string>"

          "compiledSql": "<string>"


      "timeDimension": {
        "interval": "RAW",
        "field": "<string>",
        "table": "<string>"


    "metric": {
      "fieldType": "metric",
      "type": "percentile",
      "name": "<string>",
      "label": "<string>",
      "table": "<string>",
      "tableLabel": "<string>",
      "sql": "<string>",
      "description": "<string>",
      "source": {
        "content": "<string>",
        "highlight": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "range": {
          "end": {
            "character": 123,
            "line": 123

          "start": {
            "character": 123,
            "line": 123


        "path": "<string>"

      "hidden": true,
      "compact": "thousands",
      "round": 123,
      "format": "km",
      "groupLabel": "<string>",
      "groups": [
        "<string>"

      "urls": [

          "label": "<string>",
          "url": "<string>"


      "index": 123,
      "tags": [
        "<string>"

      "parameterReferences": [
        "<string>"

      "showUnderlyingValues": [
        "<string>"

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

      "dimensionReference": "<string>",
      "requiredAttributes": {},
      "defaultTimeDimension": {
        "interval": "RAW",
        "field": "<string>"

      "spotlight": {
        "categories": [
          "<string>"

        "visibility": "show"

      "aiHint": "<string>",
      "tablesRequiredAttributes": {},
      "tablesReferences": [
        "<string>"

      "compiledSql": "<string>",
      "availableTimeDimensions": [

          "fieldType": "dimension",
          "type": "date",
          "name": "<string>",
          "label": "<string>",
          "table": "<string>",
          "tableLabel": "<string>",
          "sql": "<string>",
          "description": "<string>",
          "source": {
            "content": "<string>",
            "highlight": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "range": {
              "end": {
                "character": 123,
                "line": 123

              "start": {
                "character": 123,
                "line": 123


            "path": "<string>"

          "hidden": true,
          "compact": "thousands",
          "round": 123,
          "format": "km",
          "groupLabel": "<string>",
          "groups": [
            "<string>"

          "urls": [

              "label": "<string>",
              "url": "<string>"


          "index": 123,
          "tags": [
            "<string>"

          "parameterReferences": [
            "<string>"

          "group": "<string>",
          "requiredAttributes": {},
          "timeInterval": "RAW",
          "timeIntervalBaseDimensionName": "<string>",
          "isAdditionalDimension": true,
          "colors": {},
          "isIntervalBase": true,
          "aiHint": "<string>",
          "tablesRequiredAttributes": {},
          "tablesReferences": [
            "<string>"

          "compiledSql": "<string>"


      "timeDimension": {
        "interval": "RAW",
        "field": "<string>",
        "table": "<string>"



  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
The project UUID
explore
string
required
The explore name
metric
string
required
The metric name
#### Query Parameters
startDate
string
required
endDate
string
required
#### Body
application/json
query
object
required
  * Option 1
  * Option 2
  * Option 3


Show child attributes
filter
object
Show child attributes
timeDimensionOverride
object
Show child attributes
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
Patch apiv1notificationsPost apiv1projects metricsexplorer runmetrictotal
Assistant
Responses are generated using AI and may contain mistakes.


