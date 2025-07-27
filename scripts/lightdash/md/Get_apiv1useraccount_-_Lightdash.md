# Get apiv1useraccount - Lightdash

**Source:** https://docs.lightdash.com/api-reference/my-account/get-apiv1useraccount

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
My Account
Get apiv1useraccount
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
    "organization": {
      "name": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "organizationUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"

    "authentication": {
      "source": "<string>",
      "type": "session"

    "user": {
      "id": "<string>",
      "type": "registered",
      "email": "<string>",
      "isActive": true


  "status": "ok"

```

GET
/
api
/
v1
/
user
/
account
Try it
200
default
Copy
Ask AI
```

  "results": {
    "organization": {
      "name": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "organizationUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"

    "authentication": {
      "source": "<string>",
      "type": "session"

    "user": {
      "id": "<string>",
      "type": "registered",
      "email": "<string>",
      "isActive": true


  "status": "ok"

```

#### Response
200
200 default
application/json
Success
results
object
required
From T, pick a set of properties whose keys are in the union K
Show child attributes
status
enum<string>
required
Available options: 
Patch apiv1usermepersonal access tokens rotateGet apiv1orgattributes
Assistant
Responses are generated using AI and may contain mistakes.


