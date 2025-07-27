# Post apiv1share - Lightdash

**Source:** https://docs.lightdash.com/api-reference/share-links/post-apiv1share

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Share links
Post apiv1share
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


201
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

POST
/
api
/
v1
/
share
Try it
201
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

#### Body
application/json
a full URL used to generate a short url id
path
string
required
The URL path of the full URL
params
string
required
#### Response
201
201 default
application/json
Created
results
object
required
A ShareUrl maps a short shareable id to a full URL in the Lightdash UI. This allows very long URLs to be represented by short ids.
Show child attributes
status
enum<string>
required
Available options: 
Get apiv1shareGet apiv1schedulers logs
Assistant
Responses are generated using AI and may contain mistakes.


