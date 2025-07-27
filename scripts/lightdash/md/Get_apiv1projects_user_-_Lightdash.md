# Get apiv1projects user - Lightdash

**Source:** https://docs.lightdash.com/api-reference/roles-&-permissions/get-apiv1projects-user

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Roles & Permissions
Get apiv1projects user
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

  "results": {
    "lastName": "<string>",
    "firstName": "<string>",
    "email": "<string>",
    "role": "viewer",
    "projectUuid": "<string>",
    "userUuid": "<string>"

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
user
/
{userUuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "lastName": "<string>",
    "firstName": "<string>",
    "email": "<string>",
    "role": "viewer",
    "projectUuid": "<string>",
    "userUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
userUuid
string
required
#### Response
200
200 default
application/json
Success
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1projects accessDelete apiv1projects access
Assistant
Responses are generated using AI and may contain mistakes.


