# Post apiv2projects queryunderlying data - Lightdash

**Source:** https://docs.lightdash.com/api-reference/v2/post-apiv2projects-queryunderlying-data

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Post apiv2projects queryunderlying data
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
  *     * Get apiv2projects query
    * POST
Post apiv2projects query cancel
    * POST
Post apiv2projects querymetric query
    * POST
Post apiv2projects querychart
    * POST
Post apiv2projects querydashboard chart
    * POST
Post apiv2projects queryunderlying data
    * POST
Post apiv2projects querysql
    * POST
Post apiv2projects querysql chart
    * POST
Post apiv2projects querydashboard sql chart
    * Get apiv2projects query results
    * POST
Post apiv2projects query download
    * Get apiv2projects parameters
    * Put apiv2projects parameters
    * Get apiv2feature flag
    * Get apiv2content


200
default
Copy
Ask AI
```

  "results": {
    "parameterReferences": [
      "<string>"

    "cacheMetadata": {
      "cacheHit": true,
      "cacheKey": "<string>",
      "cacheExpiresAt": "2023-11-07T05:31:56Z",
      "cacheUpdatedTime": "2023-11-07T05:31:56Z"

    "queryUuid": "<string>",
    "warnings": [

        "tables": [
          "<string>"

        "fields": [
          "<string>"

        "message": "<string>"


    "fields": {},
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


  "status": "ok"

```

POST
/
api
/
v2
/
projects
/
{projectUuid}
/
query
/
underlying-data
Try it
200
default
Copy
Ask AI
```

  "results": {
    "parameterReferences": [
      "<string>"

    "cacheMetadata": {
      "cacheHit": true,
      "cacheKey": "<string>",
      "cacheExpiresAt": "2023-11-07T05:31:56Z",
      "cacheUpdatedTime": "2023-11-07T05:31:56Z"

    "queryUuid": "<string>",
    "warnings": [

        "tables": [
          "<string>"

        "fields": [
          "<string>"

        "message": "<string>"


    "fields": {},
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


  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Body
application/json
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Post apiv2projects querydashboard chartPost apiv2projects querysql
Assistant
Responses are generated using AI and may contain mistakes.


