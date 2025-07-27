# Get apiv1projects tags - Lightdash

**Source:** https://docs.lightdash.com/api-reference/projects/get-apiv1projects-tags

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Projects
Get apiv1projects tags
##### API


##### Reference
  * Projects
    * Get apiv1snowflakessois authenticated
    * Get apiv1projects validate
    * POST
Post apiv1projects validate
    * Delete apiv1projects validate
    * Get apiv1analyticsuser activity
    * POST
Post apiv1analyticsuser activity download
    * Get apiv1projects spaces
    * POST
Post apiv1projects rename
    * POST
Post apiv1projects renamechart
    * Get apiv1projects renamechart fields
    * Get apiv1projects
    * Get apiv1projects charts
    * Get apiv1projects chart summaries
deprecated
    * Get apiv1projects groupaccesses
    * POST
Post apiv1projects calculate total
    * POST
Post apiv1projects calculate subtotals
    * Get apiv1projects user credentials
    * PATCH
Patch apiv1projects user credentials
    * Get apiv1projects custom metrics
    * PATCH
Patch apiv1projects metadata
    * Get apiv1projects dashboards
    * POST
Post apiv1projects dashboards
    * PATCH
Patch apiv1projects dashboards
    * POST
Post apiv1projects createpreview
    * PATCH
Patch apiv1projects schedulersettings
    * Get apiv1projects tags
    * POST
Post apiv1projects tags
    * Delete apiv1projects tags
    * PATCH
Patch apiv1projects tags
    * Put apiv1projects tagsyaml
    * Get apiv1projects chartscode
    * Get apiv1projects dashboardscode
    * POST
Post apiv1projects charts code
    * POST
Post apiv1projects dashboards code
    * POST
Post apiv1projects dbt cloudwebhook
    * POST
Post apiv1projects refresh
    * Get apiv1projects explores
    * Put apiv1projects explores
    * Get apiv1projects explores 1
    * POST
Post apiv1projects explores compilequery
    * POST
Post apiv1projects explores downloadcsv
    * Get apiv1bigqueryssodatasets
    * Get apiv1bigqueryssois authenticated
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

      "createdBy": {
        "userUuid": "<string>",
        "firstName": "<string>",
        "lastName": "<string>"

      "yamlReference": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "color": "<string>",
      "name": "<string>",
      "projectUuid": "<string>",
      "tagUuid": "<string>"


  "status": "ok"

```

GET
/
api
/
v1
/
projects
/
{projectUuid}
/
tags
Try it
200
default
Copy
Ask AI
```

  "results": [

      "createdBy": {
        "userUuid": "<string>",
        "firstName": "<string>",
        "lastName": "<string>"

      "yamlReference": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "color": "<string>",
      "name": "<string>",
      "projectUuid": "<string>",
      "tagUuid": "<string>"


  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
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
Patch apiv1projects schedulersettingsPost apiv1projects tags
Assistant
Responses are generated using AI and may contain mistakes.


