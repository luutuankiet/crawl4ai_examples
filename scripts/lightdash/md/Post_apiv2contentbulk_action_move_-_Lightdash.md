# Post apiv2contentbulk action move - Lightdash

**Source:** https://docs.lightdash.com/api-reference/content/post-apiv2contentbulk-action-move

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Content
Post apiv2contentbulk action move
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

  "results": "<any>",
  "status": "ok"

```

POST
/
api
/
v2
/
content
/
bulk-action
/
{projectUuid}
/
move
Try it
200
default
Copy
Ask AI
```

  "results": "<any>",
  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Body
application/json
action
object
required
Show child attributes
content
object[]
required
  * Option 1
  * Option 2
  * Option 3


Show child attributes
#### Response
200
200 default
application/json
Success
status
enum<string>
required
Available options: 
results
any
Post apiv2content moveGet apiv1org
Assistant
Responses are generated using AI and may contain mistakes.


