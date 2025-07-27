# Post apiv1gdriveupload gsheet - Lightdash

**Source:** https://docs.lightdash.com/api-reference/integrations/post-apiv1gdriveupload-gsheet

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Integrations
Post apiv1gdriveupload gsheet
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
    * Get apiv1slackchannels
    * Put apiv1slackcustom settings
    * Get apiv1slackis authenticated
    * Get apiv1slack
    * Delete apiv1slack
    * Get apiv1slackimage
    * Get apiv1slackinstall
    * Get apiv1gdriveget access token
    * POST
Post apiv1gdriveupload gsheet
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
    "jobId": "<string>"

  "status": "ok"

```

POST
/
api
/
v1
/
gdrive
/
upload-gsheet
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

#### Body
application/json
columnOrder
string[]
required
showTableNames
boolean
required
metricQuery
object
required
Show child attributes
exploreId
string
required
projectUuid
string
required
pivotConfig
object
Show child attributes
hiddenFields
string[]
customLabels
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
Get apiv1gdriveget access tokenGet apiv1share
Assistant
Responses are generated using AI and may contain mistakes.


