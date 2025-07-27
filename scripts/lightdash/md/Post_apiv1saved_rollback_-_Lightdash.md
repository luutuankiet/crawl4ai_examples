# Post apiv1saved rollback - Lightdash

**Source:** https://docs.lightdash.com/api-reference/charts/post-apiv1saved-rollback

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Charts
Post apiv1saved rollback
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
    * POST
Post apiv1saved results
deprecated
    * POST
Post apiv1saved chart and results
deprecated
    * Get apiv1saved history
    * Get apiv1saved version
    * POST
Post apiv1saved version results
deprecated
    * POST
Post apiv1saved rollback
    * POST
Post apiv1saved calculate total
    * POST
Post apiv1saved promote
    * Get apiv1saved promotediff
    * POST
Post apiv1saved downloadcsv
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

  "results": "<any>",
  "status": "ok"

```

POST
/
api
/
v1
/
saved
/
{chartUuid}
/
rollback
/
{versionUuid}
Try it
200
default
Copy
Ask AI
```

  "results": "<any>",
  "status": "ok"

```

#### Path Parameters
chartUuid
string
required
chartUuid for the chart to run
versionUuid
string
required
versionUuid for the chart version
#### Response
200
200 default
application/json
Success
status
enum<string>
required
Available options: 
results
any
Post apiv1saved version resultsPost apiv1saved calculate total
Assistant
Responses are generated using AI and may contain mistakes.


