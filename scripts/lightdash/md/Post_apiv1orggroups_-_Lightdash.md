# Post apiv1orggroups - Lightdash

**Source:** https://docs.lightdash.com/api-reference/organizations/post-apiv1orggroups

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Organizations
Post apiv1orggroups
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
    "organizationUuid": "<string>",
    "updatedByUserUuid": "<string>",
    "updatedAt": "2023-11-07T05:31:56Z",
    "createdByUserUuid": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "name": "<string>",
    "uuid": "<string>",
    "memberUuids": [
      "<string>"

    "members": [

        "lastName": "<string>",
        "firstName": "<string>",
        "email": "<string>",
        "userUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"



  "status": "ok"

```

POST
/
api
/
v1
/
org
/
groups
Try it
200
default
Copy
Ask AI
```

  "results": {
    "organizationUuid": "<string>",
    "updatedByUserUuid": "<string>",
    "updatedAt": "2023-11-07T05:31:56Z",
    "createdByUserUuid": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "name": "<string>",
    "uuid": "<string>",
    "memberUuids": [
      "<string>"

    "members": [

        "lastName": "<string>",
        "firstName": "<string>",
        "email": "<string>",
        "userUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"



  "status": "ok"

```

#### Body
application/json
the new group details
the new group details From T, pick a set of properties whose keys are in the union K
name
string
required
A friendly name for the group
members
object[]
Show child attributes
#### Response
200
200 default
application/json
results
object
required
Details for a group including a list of the group's members.
Show child attributes
status
enum<string>
required
Available options: 
Get apiv1orggroupsGet apiv1orgcolor palettes
Assistant
Responses are generated using AI and may contain mistakes.


