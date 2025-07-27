# Post apiv1projects metricsexplorer runmetrictotal - Lightdash

**Source:** https://docs.lightdash.com/api-reference/metrics-explorer/post-apiv1projects-metricsexplorer-runmetrictotal

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Metrics Explorer
Post apiv1projects metricsexplorer runmetrictotal
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


    "comparisonValue": 123,
    "value": 123

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
runMetricTotal
Try it
200
default
Copy
Ask AI
```

  "results": {
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


    "comparisonValue": 123,
    "value": 123

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
explore
string
required
metric
string
required
#### Query Parameters
timeFrame
enum<string>
required
Available options: 
`RAW`, 
`YEAR`, 
`QUARTER`, 
`MONTH`, 
`WEEK`, 
`DAY`, 
`HOUR`, 
`MINUTE`, 
`SECOND`, 
`MILLISECOND`, 
`DAY_OF_WEEK_INDEX`, 
`DAY_OF_MONTH_NUM`, 
`DAY_OF_YEAR_NUM`, 
`WEEK_NUM`, 
`MONTH_NUM`, 
`QUARTER_NUM`, 
`YEAR_NUM`, 
`DAY_OF_WEEK_NAME`, 
`MONTH_NAME`, 
`QUARTER_NAME`, 
`HOUR_OF_DAY_NUM`, 
`MINUTE_OF_HOUR_NUM`
granularity
enum<string>
required
Available options: 
`RAW`, 
`YEAR`, 
`QUARTER`, 
`MONTH`, 
`WEEK`, 
`DAY`, 
`HOUR`, 
`MINUTE`, 
`SECOND`, 
`MILLISECOND`, 
`DAY_OF_WEEK_INDEX`, 
`DAY_OF_MONTH_NUM`, 
`DAY_OF_YEAR_NUM`, 
`WEEK_NUM`, 
`MONTH_NUM`, 
`QUARTER_NUM`, 
`YEAR_NUM`, 
`DAY_OF_WEEK_NAME`, 
`MONTH_NAME`, 
`QUARTER_NAME`, 
`HOUR_OF_DAY_NUM`, 
`MINUTE_OF_HOUR_NUM`
startDate
string
required
endDate
string
required
#### Body
application/json
comparisonType
enum<string>
Available options: 
`none`, 
`previous_period`
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
Post apiv1projects metricsexplorer runmetricexplorerqueryGet apiv1groups
Assistant
Responses are generated using AI and may contain mistakes.


