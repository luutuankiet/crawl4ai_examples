# Get apiv1schedulers list - Lightdash

**Source:** https://docs.lightdash.com/api-reference/schedulers/get-apiv1schedulers-list

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Schedulers
Get apiv1schedulers list
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
    * Get apiv1schedulers logs
    * Get apiv1schedulers list
    * Get apiv1schedulers
    * Delete apiv1schedulers
    * PATCH
Patch apiv1schedulers
    * PATCH
Patch apiv1schedulers enabled
    * Get apiv1schedulers jobs
    * Get apiv1schedulersjob status
    * POST
Post apiv1schedulerssend
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

        "includeLinks": true,
        "notificationFrequency": "always",
        "enabled": true,
        "thresholds": [

            "value": 123,
            "fieldId": "<string>",
            "operator": "greaterThan"


        "options": {
          "limit": 123,
          "formatted": true

        "dashboardName": "<string>",
        "dashboardUuid": null,
        "savedChartName": "<string>",
        "savedChartUuid": "<string>",
        "timezone": "<string>",
        "cron": "<string>",
        "format": "csv",
        "createdByName": "<string>",
        "createdBy": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "createdAt": "2023-11-07T05:31:56Z",
        "message": "<string>",
        "name": "<string>",
        "schedulerUuid": "<string>",
        "targets": [

            "channel": "<string>",
            "schedulerUuid": "<string>",
            "updatedAt": "2023-11-07T05:31:56Z",
            "createdAt": "2023-11-07T05:31:56Z",
            "schedulerSlackTargetUuid": "<string>"





  "status": "ok"

```

GET
/
api
/
v1
/
schedulers
/
{projectUuid}
/
list
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

        "includeLinks": true,
        "notificationFrequency": "always",
        "enabled": true,
        "thresholds": [

            "value": 123,
            "fieldId": "<string>",
            "operator": "greaterThan"


        "options": {
          "limit": 123,
          "formatted": true

        "dashboardName": "<string>",
        "dashboardUuid": null,
        "savedChartName": "<string>",
        "savedChartUuid": "<string>",
        "timezone": "<string>",
        "cron": "<string>",
        "format": "csv",
        "createdByName": "<string>",
        "createdBy": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "createdAt": "2023-11-07T05:31:56Z",
        "message": "<string>",
        "name": "<string>",
        "schedulerUuid": "<string>",
        "targets": [

            "channel": "<string>",
            "schedulerUuid": "<string>",
            "updatedAt": "2023-11-07T05:31:56Z",
            "createdAt": "2023-11-07T05:31:56Z",
            "schedulerSlackTargetUuid": "<string>"





  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Query Parameters
pageSize
number
number of items per page
page
number
page number
searchQuery
string
search query to filter schedulers by name
sortBy
enum<string>
column to sort by
Available options: 
`name`
sortDirection
enum<string>
sort direction (asc or desc)
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
Get apiv1schedulers logsGet apiv1schedulers
Assistant
Responses are generated using AI and may contain mistakes.


