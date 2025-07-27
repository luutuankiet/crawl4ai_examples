# Get apiv1orggroups - Lightdash

**Source:** https://docs.lightdash.com/api-reference/organizations/get-apiv1orggroups

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Organizations
Get apiv1orggroups
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
{
  "results": {
    "pagination": {
      "page": 123,
      "pageSize": 123,
      "totalResults": 123,
      "totalPageCount": 123
    },
    "data": [
      {
        "organizationUuid": "<string>",
        "updatedByUserUuid": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "createdByUserUuid": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "name": "<string>",
        "uuid": "<string>"
      }
    ]
  },
  "status": "ok"
}
```

GET
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
{
  "results": {
    "pagination": {
      "page": 123,
      "pageSize": 123,
      "totalResults": 123,
      "totalPageCount": 123
    },
    "data": [
      {
        "organizationUuid": "<string>",
        "updatedByUserUuid": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "createdByUserUuid": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "name": "<string>",
        "uuid": "<string>"
      }
    ]
  },
  "status": "ok"
}
```

#### Query Parameters
page
number
pageSize
number
includeMembers
number
number of members to include
searchQuery
string
#### Response
200
200 default
application/json
The response is of type `object`.
Patch apiv1orgallowedemaildomainsPost apiv1orggroups
Assistant
Responses are generated using AI and may contain mistakes.


