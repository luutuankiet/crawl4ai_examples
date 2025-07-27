# Post apiv1saved downloadcsv - Lightdash

**Source:** https://docs.lightdash.com/api-reference/charts/post-apiv1saved-downloadcsv

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Charts
Post apiv1saved downloadcsv
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

  "results": {
    "jobId": "<string>"

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
downloadCsv
Try it
200
default
Copy
Ask AI
```

  "results": {
    "jobId": "<string>"

  "status": "ok"

```

#### Path Parameters
chartUuid
string
required
#### Body
application/json
onlyRaw
boolean
required
dashboardFilters
any
required
This AnyType is an alias for any The goal is to make it easier to identify any type in the codebase without having to eslint-disable all the time These are only used on legacy `any` types, don't use it for new types. This is added on a separate file to avoid circular dependencies.
csvLimit
number | null
tileUuid
string
#### Response
200
200 default
application/json
Success
results
object
required
status
enum<string>
required
Available options: 
Get apiv1saved promotediffGet apiv1projects pinned lists items
Assistant
Responses are generated using AI and may contain mistakes.


