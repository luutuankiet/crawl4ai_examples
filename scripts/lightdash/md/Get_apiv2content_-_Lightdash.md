# Get apiv2content - Lightdash

**Source:** https://docs.lightdash.com/api-reference/v2/get-apiv2content

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Get apiv2content
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
    "pagination": {
      "page": 123,
      "pageSize": 123,
      "totalResults": 123,
      "totalPageCount": 123

    "data": [

        "contentType": "chart",
        "uuid": "<string>",
        "slug": "<string>",
        "name": "<string>",
        "description": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "createdBy": {
          "lastName": "<string>",
          "firstName": "<string>",
          "uuid": "<string>"

        "lastUpdatedAt": "2023-11-07T05:31:56Z",
        "lastUpdatedBy": {
          "lastName": "<string>",
          "firstName": "<string>",
          "uuid": "<string>"

        "project": {
          "name": "<string>",
          "uuid": "<string>"

        "organization": {
          "name": "<string>",
          "uuid": "<string>"

        "space": {
          "name": "<string>",
          "uuid": "<string>"

        "pinnedList": {
          "uuid": "<string>"

        "views": 123,
        "firstViewedAt": "2023-11-07T05:31:56Z",
        "source": "dbt_explore",
        "chartKind": "line",
        "dashboard": {
          "name": "<string>",
          "uuid": "<string>"




  "status": "ok"

```

GET
/
api
/
v2
/
content
Try it
200
default
Copy
Ask AI
```

  "results": {
    "pagination": {
      "page": 123,
      "pageSize": 123,
      "totalResults": 123,
      "totalPageCount": 123

    "data": [

        "contentType": "chart",
        "uuid": "<string>",
        "slug": "<string>",
        "name": "<string>",
        "description": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "createdBy": {
          "lastName": "<string>",
          "firstName": "<string>",
          "uuid": "<string>"

        "lastUpdatedAt": "2023-11-07T05:31:56Z",
        "lastUpdatedBy": {
          "lastName": "<string>",
          "firstName": "<string>",
          "uuid": "<string>"

        "project": {
          "name": "<string>",
          "uuid": "<string>"

        "organization": {
          "name": "<string>",
          "uuid": "<string>"

        "space": {
          "name": "<string>",
          "uuid": "<string>"

        "pinnedList": {
          "uuid": "<string>"

        "views": 123,
        "firstViewedAt": "2023-11-07T05:31:56Z",
        "source": "dbt_explore",
        "chartKind": "line",
        "dashboard": {
          "name": "<string>",
          "uuid": "<string>"




  "status": "ok"

```

#### Query Parameters
projectUuids
string[]
spaceUuids
string[]
parentSpaceUuid
string
contentTypes
enum<string>[]
Show child attributes
pageSize
number
page
number
search
string
sortBy
enum<string>
Available options: 
`name`, 
`space_name`, 
`last_updated_at`
sortDirection
enum<string>
Available options: 
`asc`, 
`desc`
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
Get apiv2feature flag
Assistant
Responses are generated using AI and may contain mistakes.


