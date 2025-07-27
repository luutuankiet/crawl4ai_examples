# Post apiv1saved calculate total - Lightdash

**Source:** https://docs.lightdash.com/api-reference/charts/post-apiv1saved-calculate-total

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Charts
Post apiv1saved calculate total
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
{
  "results": {},
  "status": "ok"
}
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
calculate-total
Try it
200
default
Copy
Ask AI
```
{
  "results": {},
  "status": "ok"
}
```

#### Path Parameters
chartUuid
string
required
chartUuid for the chart to run
#### Body
application/json
invalidateCache
boolean
dashboardFilters
any
This AnyType is an alias for any The goal is to make it easier to identify any type in the codebase without having to eslint-disable all the time These are only used on legacy `any` types, don't use it for new types. This is added on a separate file to avoid circular dependencies.
#### Response
200
200 default
application/json
Success
results
object
required
Construct a type with a set of properties K of type T
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1saved rollbackPost apiv1saved promote
Assistant
Responses are generated using AI and may contain mistakes.


