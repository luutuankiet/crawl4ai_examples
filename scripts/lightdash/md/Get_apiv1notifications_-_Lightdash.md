# Get apiv1notifications - Lightdash

**Source:** https://docs.lightdash.com/api-reference/notifications/get-apiv1notifications

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Notifications
Get apiv1notifications
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
    * Get apiv1notifications
    * PATCH
Patch apiv1notifications
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

  "results": [

      "url": "<string>",
      "message": "<string>",
      "resourceUuid": "<string>",
      "viewed": true,
      "createdAt": "2023-11-07T05:31:56Z",
      "notificationId": "<string>",
      "metadata": {
        "dashboardUuid": "<string>",
        "dashboardName": "<string>",
        "dashboardTileUuid": "<string>",
        "dashboardTileName": "<string>"

      "resourceType": "dashboardComments"


  "status": "ok"

```

GET
/
api
/
v1
/
notifications
Try it
200
default
Copy
Ask AI
```

  "results": [

      "url": "<string>",
      "message": "<string>",
      "resourceUuid": "<string>",
      "viewed": true,
      "createdAt": "2023-11-07T05:31:56Z",
      "notificationId": "<string>",
      "metadata": {
        "dashboardUuid": "<string>",
        "dashboardName": "<string>",
        "dashboardTileUuid": "<string>",
        "dashboardTileName": "<string>"

      "resourceType": "dashboardComments"


  "status": "ok"

```

#### Query Parameters
type
enum<string>
required
Available options: 
`dashboardComments`
#### Response
200
200 default
application/json
Success
results
object[]
required
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1orgcolor palettes activePatch apiv1notifications
Assistant
Responses are generated using AI and may contain mistakes.


