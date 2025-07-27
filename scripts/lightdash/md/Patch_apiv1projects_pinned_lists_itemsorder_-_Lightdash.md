# Patch apiv1projects pinned lists itemsorder - Lightdash

**Source:** https://docs.lightdash.com/api-reference/content/patch-apiv1projects-pinned-lists-itemsorder

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Content
Patch apiv1projects pinned lists itemsorder
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

PATCH
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
/
order
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
#### Body
application/json · object[]
the new order of the pinned items
the new order of the pinned items
data
object
required
From T, pick a set of properties whose keys are in the union K
Show child attributes
type
enum<string>
required
Available options: 
`chart`, 
`dashboard`, 
`space`
#### Response
200
200 default
application/json
Success
results
object[]
required
  * Option 1
  * Option 2
  * Option 3


Show child attributes
status
enum<string>
required
Available options: 
Get apiv1projects pinned lists itemsPost apiv2content move
Assistant
Responses are generated using AI and may contain mistakes.


