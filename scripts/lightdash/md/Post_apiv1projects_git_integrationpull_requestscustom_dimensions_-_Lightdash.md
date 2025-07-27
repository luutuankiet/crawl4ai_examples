# Post apiv1projects git integrationpull requestscustom dimensions - Lightdash

**Source:** https://docs.lightdash.com/api-reference/git-integration/post-apiv1projects-git-integrationpull-requestscustom-dimensions

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Git Integration
Post apiv1projects git integrationpull requestscustom dimensions
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
  * API Reference
  * Git Integration
    * POST
Post apiv1projects git integrationpull requestscustom metrics
    * POST
Post apiv1projects git integrationpull requestscustom dimensions
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
    "prUrl": "<string>",
    "prTitle": "<string>"

  "status": "ok"

```

POST
/
api
/
v1
/
projects
/
{projectUuid}
/
git-integration
/
pull-requests
/
custom-dimensions
Try it
200
default
Copy
Ask AI
```

  "results": {
    "prUrl": "<string>",
    "prTitle": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
#### Body
application/json
customDimensions
object[]
required
  * Option 1
  * Option 2


Show child attributes
quoteChar
enum<string>
Available options: 
#### Response
200
200 default
application/json
Success
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1projects git integrationpull requestscustom metricsPost apiv1dashboards promote
Assistant
Responses are generated using AI and may contain mistakes.


