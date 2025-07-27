# Get apiv1saved history - Lightdash

**Source:** https://docs.lightdash.com/api-reference/charts/get-apiv1saved-history

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Charts
Get apiv1saved history
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
    "history": [

        "createdAt": "2023-11-07T05:31:56Z",
        "chartUuid": "<string>",
        "versionUuid": "<string>",
        "createdBy": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"




  "status": "ok"

```

GET
/
api
/
v1
/
saved
/
{chartUuid}
/
history
Try it
200
default
Copy
Ask AI
```

  "results": {
    "history": [

        "createdAt": "2023-11-07T05:31:56Z",
        "chartUuid": "<string>",
        "versionUuid": "<string>",
        "createdBy": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"




  "status": "ok"

```

#### Path Parameters
chartUuid
string
required
chartUuid for the chart
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Post apiv1saved chart and resultsGet apiv1saved version
Assistant
Responses are generated using AI and may contain mistakes.


