# Post apiv1orgprojects - Lightdash

**Source:** https://docs.lightdash.com/api-reference/organizations/post-apiv1orgprojects

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Organizations
Post apiv1orgprojects
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
    * Get apiv1org
    * Put apiv1org
    * PATCH
Patch apiv1org
    * Delete apiv1org
    * Get apiv1orgprojects
    * POST
Post apiv1orgprojects
    * Get apiv1orgusers
    * Get apiv1orgusers 1
    * Get apiv1orgusersemail
    * Delete apiv1orguser
    * Get apiv1orgallowedemaildomains
    * PATCH
Patch apiv1orgallowedemaildomains
    * Get apiv1orggroups
    * POST
Post apiv1orggroups
    * Get apiv1orgcolor palettes
    * POST
Post apiv1orgcolor palettes
    * Delete apiv1orgcolor palettes
    * PATCH
Patch apiv1orgcolor palettes
    * POST
Post apiv1orgcolor palettes active
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
    "hasContentCopy": true,
    "project": {
      "createdByUserUuid": "<string>",
      "schedulerTimezone": "<string>",
      "dbtVersion": "v1.4",
      "upstreamProjectUuid": "<string>",
      "pinnedListUuid": "<string>",
      "warehouseConnection": {
        "type": "snowflake",
        "authenticationType": "password",
        "token": "<string>",
        "role": "<string>",
        "account": "<string>",
        "requireUserCredentials": true,
        "database": "<string>",
        "warehouse": "<string>",
        "schema": "<string>",
        "threads": 123,
        "clientSessionKeepAlive": true,
        "queryTag": "<string>",
        "accessUrl": "<string>",
        "startOfWeek": 0,
        "quotedIdentifiersIgnoreCase": true,
        "override": true

      "dbtConnection": {
        "type": "dbt",
        "target": "<string>",
        "environment": [

            "value": "<string>",
            "key": "<string>"


        "selector": "<string>",
        "profiles_dir": "<string>",
        "project_dir": "<string>"

      "type": "DEFAULT",
      "name": "<string>",
      "projectUuid": "<string>",
      "organizationUuid": "<string>"


  "status": "ok"

```

POST
/
api
/
v1
/
org
/
projects
Try it
200
default
Copy
Ask AI
```

  "results": {
    "hasContentCopy": true,
    "project": {
      "createdByUserUuid": "<string>",
      "schedulerTimezone": "<string>",
      "dbtVersion": "v1.4",
      "upstreamProjectUuid": "<string>",
      "pinnedListUuid": "<string>",
      "warehouseConnection": {
        "type": "snowflake",
        "authenticationType": "password",
        "token": "<string>",
        "role": "<string>",
        "account": "<string>",
        "requireUserCredentials": true,
        "database": "<string>",
        "warehouse": "<string>",
        "schema": "<string>",
        "threads": 123,
        "clientSessionKeepAlive": true,
        "queryTag": "<string>",
        "accessUrl": "<string>",
        "startOfWeek": 0,
        "quotedIdentifiersIgnoreCase": true,
        "override": true

      "dbtConnection": {
        "type": "dbt",
        "target": "<string>",
        "environment": [

            "value": "<string>",
            "key": "<string>"


        "selector": "<string>",
        "profiles_dir": "<string>",
        "project_dir": "<string>"

      "type": "DEFAULT",
      "name": "<string>",
      "projectUuid": "<string>",
      "organizationUuid": "<string>"


  "status": "ok"

```

#### Body
application/json
From T, pick a set of properties whose keys are in the union K
name
string
required
type
enum<string>
required
Available options: 
`DEFAULT`, 
`PREVIEW`
dbtConnection
object
required
  * Option 1
  * Option 2
  * Option 3
  * Option 4
  * Option 5
  * Option 6
  * Option 7


Show child attributes
dbtVersion
Option 1 · enum<string> Option 2 · enum<string>
required
Available options: 
`v1.4`, 
`v1.5`, 
`v1.6`, 
`v1.7`, 
`v1.8`, 
`v1.9`, 
`v1.10`
pinnedListUuid
string
upstreamProjectUuid
string
copyWarehouseConnectionFromUpstreamProject
boolean
tableConfiguration
enum<string>
Available options: 
`prod`, 
`all`
copyContent
boolean
warehouseConnection
object
  * Option 1
  * Option 2
  * Option 3
  * Option 4
  * Option 5
  * Option 6


Show child attributes
#### Response
200
200 default
application/json
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Get apiv1orgprojectsGet apiv1orgusers
Assistant
Responses are generated using AI and may contain mistakes.


