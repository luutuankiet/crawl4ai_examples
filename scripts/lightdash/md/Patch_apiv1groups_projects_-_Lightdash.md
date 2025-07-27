# Patch apiv1groups projects - Lightdash

**Source:** https://docs.lightdash.com/api-reference/user-groups/patch-apiv1groups-projects

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
User Groups
Patch apiv1groups projects
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
    "role": "viewer",
    "groupUuid": "<string>",
    "projectUuid": "<string>"

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
/
projects
/
{projectUuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "role": "viewer",
    "groupUuid": "<string>",
    "projectUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
groupUuid
string
required
projectUuid
string
required
#### Body
application/json
From T, pick a set of properties whose keys are in the union K
role
enum<string>
required
Available options: 
`viewer`, 
`interactive_viewer`, 
`editor`, 
`developer`, 
`admin`
#### Response
200
200 default
application/json
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Delete apiv1groups projectsGet apiv1githubinstall
Assistant
Responses are generated using AI and may contain mistakes.


