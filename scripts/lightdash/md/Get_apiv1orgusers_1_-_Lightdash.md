# Get apiv1orgusers 1 - Lightdash

**Source:** https://docs.lightdash.com/api-reference/organizations/get-apiv1orgusers-1

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Organizations
Get apiv1orgusers 1
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
    * Get apiv1org
    * Put apiv1org
    * PATCH
Patch apiv1org
    * Delete apiv1org
    * Get apiv1orgprojects
    * POST
Post apiv1orgprojects
    * Get apiv1orgusers
    * Get apiv1orgusers 1
    * Get apiv1orgusersemail
    * Delete apiv1orguser
    * Get apiv1orgallowedemaildomains
    * PATCH
Patch apiv1orgallowedemaildomains
    * Get apiv1orggroups
    * POST
Post apiv1orggroups
    * Get apiv1orgcolor palettes
    * POST
Post apiv1orgcolor palettes
    * Delete apiv1orgcolor palettes
    * PATCH
Patch apiv1orgcolor palettes
    * POST
Post apiv1orgcolor palettes active
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

GET
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
string<uuid>
required
the uuid of the user
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
Get apiv1orgusersGet apiv1orgusersemail
Assistant
Responses are generated using AI and may contain mistakes.


