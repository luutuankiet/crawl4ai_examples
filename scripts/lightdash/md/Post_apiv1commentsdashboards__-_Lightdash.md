# Post apiv1commentsdashboards  - Lightdash

**Source:** https://docs.lightdash.com/api-reference/comments/post-apiv1commentsdashboards-

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Comments
Post apiv1commentsdashboards 
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
    * POST
Post apiv1commentsdashboards 
    * Get apiv1commentsdashboards
    * Delete apiv1commentsdashboards 
    * PATCH
Patch apiv1commentsdashboards 
  * Catalog


200
default
Copy
Ask AI
```

  "results": "<string>",
  "status": "ok"

```

POST
/
api
/
v1
/
comments
/
dashboards
/
{dashboardUuid}
/
{dashboardTileUuid}
Try it
200
default
Copy
Ask AI
```

  "results": "<string>",
  "status": "ok"

```

#### Path Parameters
dashboardUuid
string
required
the uuid of the dashboard
dashboardTileUuid
string
required
the uuid of the dashboard tile
#### Body
application/json
the comment to create
text
string
required
mentions
string[]
required
textHtml
string
required
replyTo
string
#### Response
200
200 default
application/json
Success
results
string
required
status
enum<string>
required
Available options: 
Get apiv1csvGet apiv1commentsdashboards
Assistant
Responses are generated using AI and may contain mistakes.


