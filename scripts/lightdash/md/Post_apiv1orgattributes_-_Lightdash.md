# Post apiv1orgattributes - Lightdash

**Source:** https://docs.lightdash.com/api-reference/user-attributes/post-apiv1orgattributes

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
User attributes
Post apiv1orgattributes
##### API


##### Reference
  * Projects
  * My Account
  * User attributes
    * Get apiv1orgattributes
    * POST
Post apiv1orgattributes
    * Put apiv1orgattributes
    * Delete apiv1orgattributes
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
    "attributeDefault": "<string>",
    "groups": [

        "value": "<string>",
        "groupUuid": "<string>"


    "users": [

        "value": "<string>",
        "email": "<string>",
        "userUuid": "<string>"


    "description": "<string>",
    "organizationUuid": "<string>",
    "name": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "uuid": "<string>"

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
attributes
Try it
200
default
Copy
Ask AI
```

  "results": {
    "attributeDefault": "<string>",
    "groups": [

        "value": "<string>",
        "groupUuid": "<string>"


    "users": [

        "value": "<string>",
        "email": "<string>",
        "userUuid": "<string>"


    "description": "<string>",
    "organizationUuid": "<string>",
    "name": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "uuid": "<string>"

  "status": "ok"

```

#### Body
application/json
the user attribute to create
the user attribute to create From T, pick a set of properties whose keys are in the union K
name
string
required
attributeDefault
string | null
required
groups
object[]
required
Show child attributes
users
object[]
required
Show child attributes
description
string
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
Get apiv1orgattributesPut apiv1orgattributes
Assistant
Responses are generated using AI and may contain mistakes.


