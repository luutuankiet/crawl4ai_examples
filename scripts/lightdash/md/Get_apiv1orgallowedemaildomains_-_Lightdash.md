# Get apiv1orgallowedemaildomains - Lightdash

**Source:** https://docs.lightdash.com/api-reference/organizations/get-apiv1orgallowedemaildomains

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Organizations
Get apiv1orgallowedemaildomains
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
    "projects": [

        "role": "editor",
        "projectUuid": "<string>"


    "role": "editor",
    "emailDomains": [
      "<string>"

    "organizationUuid": "<string>"

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
allowedEmailDomains
Try it
200
default
Copy
Ask AI
```

  "results": {
    "projects": [

        "role": "editor",
        "projectUuid": "<string>"


    "role": "editor",
    "emailDomains": [
      "<string>"

    "organizationUuid": "<string>"

  "status": "ok"

```

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
Delete apiv1orguserPatch apiv1orgallowedemaildomains
Assistant
Responses are generated using AI and may contain mistakes.


