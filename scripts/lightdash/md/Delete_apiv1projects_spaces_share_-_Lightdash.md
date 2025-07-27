# Delete apiv1projects spaces share - Lightdash

**Source:** https://docs.lightdash.com/api-reference/roles-&-permissions/delete-apiv1projects-spaces-share

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Roles & Permissions
Delete apiv1projects spaces share
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
share
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
projectUuid
string
required
The uuid of the space's parent project
spaceUuid
string
required
The uuid of the space to update
userUuid
string
required
The uuid of the user to revoke access from
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
Post apiv1projects spaces sharePost apiv1projects spaces groupshare
Assistant
Responses are generated using AI and may contain mistakes.


