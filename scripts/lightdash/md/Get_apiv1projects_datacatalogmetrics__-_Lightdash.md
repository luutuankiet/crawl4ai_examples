# Get apiv1projects datacatalogmetrics  - Lightdash

**Source:** https://docs.lightdash.com/api-reference/catalog/get-apiv1projects-datacatalogmetrics-

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Catalog
Get apiv1projects datacatalogmetrics 
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
{tableName}
/
{metricName}
Try it
200
default
Copy
Ask AI
```

  "results": {
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
tableName
string
required
metricName
string
required
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Get apiv1projects datacatalogmetricsGet apiv1projects datacatalogmetrics with time dimensions
Assistant
Responses are generated using AI and may contain mistakes.


