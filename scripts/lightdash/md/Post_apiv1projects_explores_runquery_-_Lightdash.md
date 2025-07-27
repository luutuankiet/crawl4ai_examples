# Post apiv1projects explores runquery - Lightdash

**Source:** https://docs.lightdash.com/api-reference/exploring/post-apiv1projects-explores-runquery

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Exploring
Post apiv1projects explores runquery
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
    * POST
Post apiv1projects explores rununderlyingdataquery
deprecated
    * POST
Post apiv1projects explores runquery
deprecated
    * POST
Post apiv1projects sqlquery
deprecated
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
    "fields": {},
    "rows": [
      "<any>"

    "cacheMetadata": {
      "cacheHit": true,
      "cacheKey": "<string>",
      "cacheExpiresAt": "2023-11-07T05:31:56Z",
      "cacheUpdatedTime": "2023-11-07T05:31:56Z"

    "metricQuery": {
      "metadata": {
        "hasADateDimension": {
          "name": "<string>",
          "label": "<string>",
          "table": "<string>"


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
explores
/
{exploreId}
/
runQuery
Try it
200
default
Copy
Ask AI
```

  "results": {
    "fields": {},
    "rows": [
      "<any>"

    "cacheMetadata": {
      "cacheHit": true,
      "cacheKey": "<string>",
      "cacheExpiresAt": "2023-11-07T05:31:56Z",
      "cacheUpdatedTime": "2023-11-07T05:31:56Z"

    "metricQuery": {
      "metadata": {
        "hasADateDimension": {
          "name": "<string>",
          "label": "<string>",
          "table": "<string>"


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


  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
The uuid of the project
exploreId
string
required
table name
#### Body
application/json
metricQuery for the chart to run
tableCalculations
object[]
required
Show child attributes
limit
number
required
sorts
object[]
required
Show child attributes
filters
object
required
Show child attributes
metrics
string[]
required
dimensions
string[]
required
exploreName
string
required
metricOverrides
object
Show child attributes
timezone
string
metadata
object
Show child attributes
dateZoom
object
Show child attributes
customDimensions
object[]
  * Option 1
  * Option 2


Show child attributes
csvLimit
number
additionalMetrics
object[]
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
Post apiv1projects explores rununderlyingdataqueryPost apiv1projects sqlquery
Assistant
Responses are generated using AI and may contain mistakes.


