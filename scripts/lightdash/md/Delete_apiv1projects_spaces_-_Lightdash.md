# Delete apiv1projects spaces - Lightdash

**Source:** https://docs.lightdash.com/api-reference/spaces/delete-apiv1projects-spaces

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Spaces
Delete apiv1projects spaces
##### API


##### Reference
  * Projects
  * My Account
  * User attributes
  * SSH Keypairs
  * SQL runner
  * Spotlight
  * Spaces
    * Get apiv1projects spaces
    * Delete apiv1projects spaces
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


204
default
Copy
Ask AI
```

  "results": "<any>",
  "status": "ok"

```

DELETE
/
api
/
v1
/
projects
/
{projectUuid}
/
spaces
/
{spaceUuid}
Try it
204
default
Copy
Ask AI
```

  "results": "<any>",
  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
The uuid of the space's parent project
spaceUuid
string
required
The uuid of the space to delete
#### Response
204
204 default
application/json
Deleted
status
enum<string>
required
Available options: 
results
any
Get apiv1projects spacesPatch apiv1projects spaces
Assistant
Responses are generated using AI and may contain mistakes.


