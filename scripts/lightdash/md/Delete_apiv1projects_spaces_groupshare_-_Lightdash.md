# Delete apiv1projects spaces groupshare - Lightdash

**Source:** https://docs.lightdash.com/api-reference/roles-&-permissions/delete-apiv1projects-spaces-groupshare

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Roles & Permissions
Delete apiv1projects spaces groupshare
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
    * PATCH
Patch apiv1projects spaces
    * POST
Post apiv1projects spaces
    * POST
Post apiv1projects spaces share
    * Delete apiv1projects spaces share
    * POST
Post apiv1projects spaces groupshare
    * Delete apiv1projects spaces groupshare
    * Get apiv1projects access
    * POST
Post apiv1projects access
    * Get apiv1projects user
    * Delete apiv1projects access
    * PATCH
Patch apiv1projects access
    * PATCH
Patch apiv1orgusers
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
  * Catalog


200
default
Copy
Ask AI
```

  "results": "<any>",
  "status": "ok"

```

DELETE
/
api
/
v1
/
projects
/
{projectUuid}
/
spaces
/
{spaceUuid}
/
group
/
share
/
{groupUuid}
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
The uuid of the space's parent project
spaceUuid
string
required
The uuid of the space to update
groupUuid
string
required
The uuid of the group to revoke access from
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
Post apiv1projects spaces groupshareGet apiv1projects access
Assistant
Responses are generated using AI and may contain mistakes.


