# Get apiv1schedulers jobs - Lightdash

**Source:** https://docs.lightdash.com/api-reference/schedulers/get-apiv1schedulers-jobs

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Schedulers
Get apiv1schedulers jobs
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
    * Get apiv1schedulers logs
    * Get apiv1schedulers list
    * Get apiv1schedulers
    * Delete apiv1schedulers
    * PATCH
Patch apiv1schedulers
    * PATCH
Patch apiv1schedulers enabled
    * Get apiv1schedulers jobs
    * Get apiv1schedulersjob status
    * POST
Post apiv1schedulerssend
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

  "results": [

      "id": "<string>",
      "date": "2023-11-07T05:31:56Z"


  "status": "ok"

```

GET
/
api
/
v1
/
schedulers
/
{schedulerUuid}
/
jobs
Try it
200
default
Copy
Ask AI
```

  "results": [

      "id": "<string>",
      "date": "2023-11-07T05:31:56Z"


  "status": "ok"

```

#### Path Parameters
schedulerUuid
string
required
The uuid of the scheduler to update
#### Response
200
200 default
application/json
Success
results
object[]
required
Show child attributes
status
enum<string>
required
Available options: 
Patch apiv1schedulers enabledGet apiv1schedulersjob status
Assistant
Responses are generated using AI and may contain mistakes.


