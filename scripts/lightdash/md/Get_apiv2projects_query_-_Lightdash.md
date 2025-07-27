# Get apiv2projects query - Lightdash

**Source:** https://docs.lightdash.com/api-reference/v2/get-apiv2projects-query

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Get apiv2projects query
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
    "page": 123,
    "pageSize": 123,
    "totalResults": 123,
    "totalPageCount": 123,
    "previousPage": 123,
    "nextPage": 123,
    "pivotDetails": {
      "originalColumns": {},
      "sortBy": [

          "direction": "ASC",
          "reference": "<string>"


      "groupByColumns": [

          "reference": "<string>"


      "valuesColumns": [

          "pivotValues": [

              "value": "<string>",
              "referenceField": "<string>"


          "aggregation": "sum",
          "pivotColumnName": "<string>",
          "referenceField": "<string>"


      "indexColumn": {
        "type": "time",
        "reference": "<string>"

      "totalColumnCount": 123

    "status": "ready",
    "resultsPageExecutionMs": 123,
    "initialQueryExecutionMs": 123,
    "rows": [


    "columns": {},
    "queryUuid": "<string>"

  "status": "ok"

```

GET
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
{queryUuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "page": 123,
    "pageSize": 123,
    "totalResults": 123,
    "totalPageCount": 123,
    "previousPage": 123,
    "nextPage": 123,
    "pivotDetails": {
      "originalColumns": {},
      "sortBy": [

          "direction": "ASC",
          "reference": "<string>"


      "groupByColumns": [

          "reference": "<string>"


      "valuesColumns": [

          "pivotValues": [

              "value": "<string>",
              "referenceField": "<string>"


          "aggregation": "sum",
          "pivotColumnName": "<string>",
          "referenceField": "<string>"


      "indexColumn": {
        "type": "time",
        "reference": "<string>"

      "totalColumnCount": 123

    "status": "ready",
    "resultsPageExecutionMs": 123,
    "initialQueryExecutionMs": 123,
    "rows": [


    "columns": {},
    "queryUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
queryUuid
string
required
#### Query Parameters
page
number
pageSize
number
#### Response
200
200 default
application/json
Success
results
object
required
  * Option 1
  * Option 2
  * Option 3


Show child attributes
status
enum<string>
required
Available options: 
Get apiv1projects datacatalogmetricshasPost apiv2projects query cancel
Assistant
Responses are generated using AI and may contain mistakes.


