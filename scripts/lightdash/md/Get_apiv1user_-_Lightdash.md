# Get apiv1user - Lightdash

**Source:** https://docs.lightdash.com/api-reference/my-account/get-apiv1user

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
My Account
Get apiv1user
##### API


##### Reference
  * Projects
  * My Account
    * Get apiv1user
    * POST
Post apiv1user
    * Put apiv1usermeemailotp
    * Get apiv1usermeemailstatus
    * Get apiv1usermeallowedorganizations
    * POST
Post apiv1usermejoinorganization
    * Delete apiv1userme
    * Get apiv1userwarehousecredentials
    * POST
Post apiv1userwarehousecredentials
    * Delete apiv1userwarehousecredentials
    * PATCH
Patch apiv1userwarehousecredentials
    * Get apiv1userlogin options
    * Get apiv1usermepersonal access tokens
    * POST
Post apiv1usermepersonal access tokens
    * Delete apiv1usermepersonal access tokens
    * PATCH
Patch apiv1usermepersonal access tokens rotate
    * Get apiv1useraccount
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
  * Catalog


200
default
Copy
Ask AI
```

  "results": {
    "userUuid": "<string>",
    "firstName": "<string>",
    "lastName": "<string>",
    "organizationUuid": "<string>",
    "organizationName": "<string>",
    "organizationCreatedAt": "2023-11-07T05:31:56Z",
    "userId": 123,
    "role": "member",
    "isTrackingAnonymized": true,
    "isMarketingOptedIn": true,
    "isSetupComplete": true,
    "email": "<string>",
    "isActive": true,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "isPending": true

  "status": "ok"

```

GET
/
api
/
v1
/
user
Try it
200
default
Copy
Ask AI
```

  "results": {
    "userUuid": "<string>",
    "firstName": "<string>",
    "lastName": "<string>",
    "organizationUuid": "<string>",
    "organizationName": "<string>",
    "organizationCreatedAt": "2023-11-07T05:31:56Z",
    "userId": 123,
    "role": "member",
    "isTrackingAnonymized": true,
    "isMarketingOptedIn": true,
    "isSetupComplete": true,
    "email": "<string>",
    "isActive": true,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "isPending": true

  "status": "ok"

```

#### Response
200
200 default
application/json
Shows the authenticated user
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Get apiv1bigqueryssois authenticatedPost apiv1user
Assistant
Responses are generated using AI and may contain mistakes.


