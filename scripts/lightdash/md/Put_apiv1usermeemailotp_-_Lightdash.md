# Put apiv1usermeemailotp - Lightdash

**Source:** https://docs.lightdash.com/api-reference/my-account/put-apiv1usermeemailotp

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
My Account
Put apiv1usermeemailotp
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
    "otp": {
      "numberOfAttempts": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "isMaxAttempts": true,
      "isExpired": true,
      "expiresAt": "2023-11-07T05:31:56Z"

    "isVerified": true,
    "email": "<string>"

  "status": "ok"

```

PUT
/
api
/
v1
/
user
/
me
/
email
/
otp
Try it
200
default
Copy
Ask AI
```

  "results": {
    "otp": {
      "numberOfAttempts": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "isMaxAttempts": true,
      "isExpired": true,
      "expiresAt": "2023-11-07T05:31:56Z"

    "isVerified": true,
    "email": "<string>"

  "status": "ok"

```

#### Response
200
200 default
application/json
Shows the current verification status of an email address
results
object
required
Verification status of an email address
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1userGet apiv1usermeemailstatus
Assistant
Responses are generated using AI and may contain mistakes.


