# Post apiv1userwarehousecredentials - Lightdash

**Source:** https://docs.lightdash.com/api-reference/my-account/post-apiv1userwarehousecredentials

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
My Account
Post apiv1userwarehousecredentials
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
    "credentials": {
      "user": "<string>",
      "type": "postgres"

    "updatedAt": "2023-11-07T05:31:56Z",
    "createdAt": "2023-11-07T05:31:56Z",
    "name": "<string>",
    "userUuid": "<string>",
    "uuid": "<string>"

  "status": "ok"

```

POST
/
api
/
v1
/
user
/
warehouseCredentials
Try it
200
default
Copy
Ask AI
```

  "results": {
    "credentials": {
      "user": "<string>",
      "type": "postgres"

    "updatedAt": "2023-11-07T05:31:56Z",
    "createdAt": "2023-11-07T05:31:56Z",
    "name": "<string>",
    "userUuid": "<string>",
    "uuid": "<string>"

  "status": "ok"

```

#### Body
application/json
credentials
object
required
From T, pick a set of properties whose keys are in the union K
  * Option 1
  * Option 2
  * Option 3
  * Option 4
  * Option 5
  * Option 6


Show child attributes
name
string
required
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
Get apiv1userwarehousecredentialsDelete apiv1userwarehousecredentials
Assistant
Responses are generated using AI and may contain mistakes.


