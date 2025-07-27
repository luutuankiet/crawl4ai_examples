# Get apiv1share - Lightdash

**Source:** https://docs.lightdash.com/api-reference/share-links/get-apiv1share

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Share links
Get apiv1share
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
    * Get apiv1share
    * POST
Post apiv1share
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
    "host": "<string>",
    "url": "<string>",
    "shareUrl": "<string>",
    "organizationUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "createdByUserUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "params": "<string>",
    "path": "<string>",
    "nanoid": "<string>"

  "status": "ok"

```

GET
/
api
/
v1
/
share
/
{nanoId}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "host": "<string>",
    "url": "<string>",
    "shareUrl": "<string>",
    "organizationUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "createdByUserUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "params": "<string>",
    "path": "<string>",
    "nanoid": "<string>"

  "status": "ok"

```

#### Path Parameters
nanoId
string
required
the short id for the share url
#### Response
200
200 default
application/json
results
object
required
A ShareUrl maps a short shareable id to a full URL in the Lightdash UI. This allows very long URLs to be represented by short ids.
Show child attributes
status
enum<string>
required
Available options: 
Post apiv1gdriveupload gsheetPost apiv1share
Assistant
Responses are generated using AI and may contain mistakes.


