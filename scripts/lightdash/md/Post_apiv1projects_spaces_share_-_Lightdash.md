# Post apiv1projects spaces share - Lightdash

**Source:** https://docs.lightdash.com/api-reference/roles-&-permissions/post-apiv1projects-spaces-share

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Roles & Permissions
Post apiv1projects spaces share
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

POST
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
#### Body
application/json
spaceRole
enum<string>
required
Available options: 
`viewer`, 
`editor`, 
`admin`
userUuid
string
required
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
Post apiv1projects spacesDelete apiv1projects spaces share
Assistant
Responses are generated using AI and may contain mistakes.


