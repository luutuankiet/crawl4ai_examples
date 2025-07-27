# Patch apiv1groups - Lightdash

**Source:** https://docs.lightdash.com/api-reference/user-groups/patch-apiv1groups

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
User Groups
Patch apiv1groups
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
    * Get apiv1groups
    * Delete apiv1groups
    * PATCH
Patch apiv1groups
    * Put apiv1groups members
    * Delete apiv1groups members
    * Get apiv1groups members
    * POST
Post apiv1groups projects
    * Delete apiv1groups projects
    * PATCH
Patch apiv1groups projects
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
    "organizationUuid": "<string>",
    "updatedByUserUuid": "<string>",
    "updatedAt": "2023-11-07T05:31:56Z",
    "createdByUserUuid": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "name": "<string>",
    "uuid": "<string>"

  "status": "ok"

```

PATCH
/
api
/
v1
/
groups
/
{groupUuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "organizationUuid": "<string>",
    "updatedByUserUuid": "<string>",
    "updatedAt": "2023-11-07T05:31:56Z",
    "createdByUserUuid": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "name": "<string>",
    "uuid": "<string>"

  "status": "ok"

```

#### Path Parameters
groupUuid
string
required
#### Body
application/json
members
object[]
Show child attributes
name
string
#### Response
200
200 default
application/json
results
object
required
  * Option 1
  * Option 2


Show child attributes
status
enum<string>
required
Available options: 
Delete apiv1groupsPut apiv1groups members
Assistant
Responses are generated using AI and may contain mistakes.


