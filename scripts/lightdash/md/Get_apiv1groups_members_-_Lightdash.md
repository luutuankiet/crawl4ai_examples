# Get apiv1groups members - Lightdash

**Source:** https://docs.lightdash.com/api-reference/user-groups/get-apiv1groups-members

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
User Groups
Get apiv1groups members
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
  * Notifications
  * Metrics Explorer
  * User Groups
    * Get apiv1groups
    * Delete apiv1groups
    * PATCH
Patch apiv1groups
    * Put apiv1groups members
    * Delete apiv1groups members
    * Get apiv1groups members
    * POST
Post apiv1groups projects
    * Delete apiv1groups projects
    * PATCH
Patch apiv1groups projects
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
  "results": [
    {
      "lastName": "<string>",
      "firstName": "<string>",
      "email": "<string>",
      "userUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
  ],
  "status": "ok"
}
```

GET
/
api
/
v1
/
groups
/
{groupUuid}
/
members
Try it
200
default
Copy
Ask AI
```
{
  "results": [
    {
      "lastName": "<string>",
      "firstName": "<string>",
      "email": "<string>",
      "userUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
  ],
  "status": "ok"
}
```

#### Path Parameters
groupUuid
string
required
the UUID for the group to view the members of
#### Response
200
200 default
application/json
results
object[]
required
Show child attributes
status
enum<string>
required
Available options: 
Delete apiv1groups membersPost apiv1groups projects
Assistant
Responses are generated using AI and may contain mistakes.


