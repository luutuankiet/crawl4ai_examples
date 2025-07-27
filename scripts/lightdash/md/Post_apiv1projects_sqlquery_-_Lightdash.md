# Post apiv1projects sqlquery - Lightdash

**Source:** https://docs.lightdash.com/api-reference/exploring/post-apiv1projects-sqlquery

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Exploring
Post apiv1projects sqlquery
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
    * POST
Post apiv1projects explores rununderlyingdataquery
deprecated
    * POST
Post apiv1projects explores runquery
deprecated
    * POST
Post apiv1projects sqlquery
deprecated
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
    "rows": [


    "fields": {}

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
sqlQuery
Try it
200
default
Copy
Ask AI
```

  "results": {
    "rows": [


    "fields": {}

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
The uuid of the project to run the query against
#### Body
application/json
The query to run
sql
string
required
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
Post apiv1projects explores runqueryPost apiv1saved results
Assistant
Responses are generated using AI and may contain mistakes.


