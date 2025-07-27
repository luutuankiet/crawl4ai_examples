# Get apiv1projects pinned lists items - Lightdash

**Source:** https://docs.lightdash.com/api-reference/content/get-apiv1projects-pinned-lists-items

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Content
Get apiv1projects pinned lists items
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
    * Get apiv1projects pinned lists items
    * PATCH
Patch apiv1projects pinned lists itemsorder
    * POST
Post apiv2content move
    * POST
Post apiv2contentbulk action move
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

  "results": [

      "category": "mostPopular",
      "data": {
        "description": "<string>",
        "name": "<string>",
        "uuid": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "spaceUuid": "<string>",
        "pinnedListUuid": "<string>",
        "pinnedListOrder": 123,
        "updatedByUser": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"

        "views": 123,
        "firstViewedAt": "<string>",
        "validationErrors": [

            "createdAt": "2023-11-07T05:31:56Z",
            "validationId": 123,
            "error": "<string>"



      "type": "dashboard"


  "status": "ok"

```

GET
/
api
/
v1
/
projects
/
{projectUuid}
/
pinned-lists
/
{pinnedListUuid}
/
items
Try it
200
default
Copy
Ask AI
```

  "results": [

      "category": "mostPopular",
      "data": {
        "description": "<string>",
        "name": "<string>",
        "uuid": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "spaceUuid": "<string>",
        "pinnedListUuid": "<string>",
        "pinnedListOrder": 123,
        "updatedByUser": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"

        "views": 123,
        "firstViewedAt": "<string>",
        "validationErrors": [

            "createdAt": "2023-11-07T05:31:56Z",
            "validationId": 123,
            "error": "<string>"



      "type": "dashboard"


  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
project uuid
pinnedListUuid
string
required
the list uuid for the pinned items
#### Response
200
200 default
application/json
Success
The response is of type `object`.
Post apiv1saved downloadcsvPatch apiv1projects pinned lists itemsorder
Assistant
Responses are generated using AI and may contain mistakes.


