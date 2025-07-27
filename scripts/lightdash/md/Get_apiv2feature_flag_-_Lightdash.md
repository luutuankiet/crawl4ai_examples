# Get apiv2feature flag - Lightdash

**Source:** https://docs.lightdash.com/api-reference/v2/get-apiv2feature-flag

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Get apiv2feature flag
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
  * Dashboards
  * Exports
  * Comments
  * Catalog
  *     * Get apiv2projects query
    * POST
Post apiv2projects query cancel
    * POST
Post apiv2projects querymetric query
    * POST
Post apiv2projects querychart
    * POST
Post apiv2projects querydashboard chart
    * POST
Post apiv2projects queryunderlying data
    * POST
Post apiv2projects querysql
    * POST
Post apiv2projects querysql chart
    * POST
Post apiv2projects querydashboard sql chart
    * Get apiv2projects query results
    * POST
Post apiv2projects query download
    * Get apiv2projects parameters
    * Put apiv2projects parameters
    * Get apiv2feature flag
    * Get apiv2content


200
default
Copy
Ask AI
```

  "results": {
    "enabled": true,
    "id": "<string>"

  "status": "ok"

```

GET
/
api
/
v2
/
feature-flag
/
{featureFlagId}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "enabled": true,
    "id": "<string>"

  "status": "ok"

```

#### Path Parameters
featureFlagId
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
Put apiv2projects parametersGet apiv2content
Assistant
Responses are generated using AI and may contain mistakes.


