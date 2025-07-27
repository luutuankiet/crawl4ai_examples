# Patch apiv1projects sqlrunnersaved - Lightdash

**Source:** https://docs.lightdash.com/api-reference/sql-runner/patch-apiv1projects-sqlrunnersaved

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
SQL runner
Patch apiv1projects sqlrunnersaved
##### API


##### Reference
  * Projects
  * My Account
  * User attributes
  * SSH Keypairs
  * SQL runner
    * Get apiv1projects sqlrunnertables
    * Get apiv1projects sqlrunnerfields
    * POST
Post apiv1projects sqlrunnerrun
    * POST
Post apiv1projects sqlrunnerrunpivotquery
    * Get apiv1projects sqlrunnerresults
    * Get apiv1projects sqlrunnersaved
    * Delete apiv1projects sqlrunnersaved
    * PATCH
Patch apiv1projects sqlrunnersaved
    * Get apiv1projects sqlrunnersavedslug
    * Get apiv1projects sqlrunnersavedslug results job
    * Get apiv1projects sqlrunnersaved results job
    * POST
Post apiv1projects sqlrunnersaved
    * POST
Post apiv1projects sqlrunnerrefresh catalog
    * POST
Post apiv1projects sqlrunnervirtual view
    * Put apiv1projects sqlrunnervirtual view
    * Delete apiv1projects sqlrunnervirtual view
    * POST
Post apiv1projects sqlrunnerpreview
    * POST
Post apiv1projects sqlrunnerpull request
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
    "savedSqlVersionUuid": "<string>",
    "savedSqlUuid": "<string>"

  "status": "ok"

```

PATCH
/
api
/
v1
/
projects
/
{projectUuid}
/
sqlRunner
/
saved
/
{uuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "savedSqlVersionUuid": "<string>",
    "savedSqlUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
the uuid for the project
uuid
string
required
the uuid for the saved sql chart
#### Body
application/json
the sql chart details to update
versionedData
object
Show child attributes
unversionedData
object
Show child attributes
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
Delete apiv1projects sqlrunnersavedGet apiv1projects sqlrunnersavedslug
Assistant
Responses are generated using AI and may contain mistakes.


