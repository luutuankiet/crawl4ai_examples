# Put apiv1groups members - Lightdash

**Source:** https://docs.lightdash.com/api-reference/user-groups/put-apiv1groups-members

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
User Groups
Put apiv1groups members
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

  "results": "<any>",
  "status": "ok"

```

PUT
/
api
/
v1
/
groups
/
{groupUuid}
/
members
/
{userUuid}
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
groupUuid
string
required
the UUID for the group to add the user to
userUuid
string
required
the UUID for the user to add to the group
#### Response
200
200 default
application/json
status
enum<string>
required
Available options: 
results
any
Patch apiv1groupsDelete apiv1groups members
Assistant
Responses are generated using AI and may contain mistakes.


