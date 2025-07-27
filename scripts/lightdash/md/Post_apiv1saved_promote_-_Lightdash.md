# Post apiv1saved promote - Lightdash

**Source:** https://docs.lightdash.com/api-reference/charts/post-apiv1saved-promote

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Charts
Post apiv1saved promote
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
    * POST
Post apiv1saved results
deprecated
    * POST
Post apiv1saved chart and results
deprecated
    * Get apiv1saved history
    * Get apiv1saved version
    * POST
Post apiv1saved version results
deprecated
    * POST
Post apiv1saved rollback
    * POST
Post apiv1saved calculate total
    * POST
Post apiv1saved promote
    * Get apiv1saved promotediff
    * POST
Post apiv1saved downloadcsv
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


  "status": "ok"

```

POST
/
api
/
v1
/
saved
/
{chartUuid}
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


  "status": "ok"

```

#### Path Parameters
chartUuid
string
required
chartUuid for the chart to run
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
Post apiv1saved calculate totalGet apiv1saved promotediff
Assistant
Responses are generated using AI and may contain mistakes.


