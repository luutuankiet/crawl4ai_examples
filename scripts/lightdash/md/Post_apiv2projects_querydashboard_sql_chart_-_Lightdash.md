# Post apiv2projects querydashboard sql chart - Lightdash

**Source:** https://docs.lightdash.com/api-reference/v2/post-apiv2projects-querydashboard-sql-chart

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Post apiv2projects querydashboard sql chart
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
    "appliedDashboardFilters": {
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
dashboard-sql-chart
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
    "appliedDashboardFilters": {
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




  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Body
application/json
  * Option 1
  * Option 2


savedSqlUuid
string
required
dashboardSorts
object[]
required
Show child attributes
dashboardFilters
object
required
Show child attributes
tileUuid
string
required
dashboardUuid
string
required
parameters
object
Construct a type with a set of properties K of type T
Show child attributes
invalidateCache
boolean
context
enum<string>
Available options: 
`dashboardView`, 
`autorefreshedDashboard`, 
`exploreView`, 
`filterAutocomplete`, 
`chartView`, 
`chartHistory`, 
`sqlChartView`, 
`sqlRunner`, 
`viewUnderlyingData`, 
`alert`, 
`scheduledDelivery`, 
`csvDownload`, 
`gsheets`, 
`scheduledGsheetsChart`, 
`scheduledGsheetsDashboard`, 
`scheduledChart`, 
`scheduledDashboard`, 
`calculateTotal`, 
`calculateSubtotal`, 
`embed`, 
`ai`, 
`api`, 
`cli`, 
`metricsExplorer`
limit
number
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
Post apiv2projects querysql chartGet apiv2projects query results
Assistant
Responses are generated using AI and may contain mistakes.


