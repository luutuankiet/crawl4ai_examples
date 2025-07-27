# Patch apiv1orgusers - Lightdash

**Source:** https://docs.lightdash.com/api-reference/roles-&-permissions/patch-apiv1orgusers

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Roles & Permissions
Patch apiv1orgusers
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
    "isPending": true,
    "isInviteExpired": true,
    "isActive": true,
    "role": "member",
    "organizationUuid": "<string>",
    "email": "<string>",
    "lastName": "<string>",
    "firstName": "<string>",
    "userUpdatedAt": "2023-11-07T05:31:56Z",
    "userCreatedAt": "2023-11-07T05:31:56Z",
    "userUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"

  "status": "ok"

```

PATCH
/
api
/
v1
/
org
/
users
/
{userUuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "isPending": true,
    "isInviteExpired": true,
    "isActive": true,
    "role": "member",
    "organizationUuid": "<string>",
    "email": "<string>",
    "lastName": "<string>",
    "firstName": "<string>",
    "userUpdatedAt": "2023-11-07T05:31:56Z",
    "userCreatedAt": "2023-11-07T05:31:56Z",
    "userUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"

  "status": "ok"

```

#### Path Parameters
userUuid
string
required
the uuid of the user to update
#### Body
application/json
the new membership profile
role
enum<string>
required
Available options: 
`member`, 
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
Profile for a user's membership in an organization
Show child attributes
status
enum<string>
required
Available options: 
Patch apiv1projects accessGet apiv1slackchannels
Assistant
Responses are generated using AI and may contain mistakes.


