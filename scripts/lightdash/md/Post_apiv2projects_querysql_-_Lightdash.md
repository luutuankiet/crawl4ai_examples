# Post apiv2projects querysql - Lightdash

**Source:** https://docs.lightdash.com/api-reference/v2/post-apiv2projects-querysql

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Post apiv2projects querysql
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

    "queryUuid": "<string>"

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
sql
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

    "queryUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Body
application/json
sql
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
pivotConfiguration
object
Show child attributes
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
Post apiv2projects queryunderlying dataPost apiv2projects querysql chart
Assistant
Responses are generated using AI and may contain mistakes.


