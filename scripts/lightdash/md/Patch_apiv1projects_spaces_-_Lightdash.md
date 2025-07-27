# Patch apiv1projects spaces - Lightdash

**Source:** https://docs.lightdash.com/api-reference/roles-&-permissions/patch-apiv1projects-spaces

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Roles & Permissions
Patch apiv1projects spaces
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
    * PATCH
Patch apiv1projects spaces
    * POST
Post apiv1projects spaces
    * POST
Post apiv1projects spaces share
    * Delete apiv1projects spaces share
    * POST
Post apiv1projects spaces groupshare
    * Delete apiv1projects spaces groupshare
    * Get apiv1projects access
    * POST
Post apiv1projects access
    * Get apiv1projects user
    * Delete apiv1projects access
    * PATCH
Patch apiv1projects access
    * PATCH
Patch apiv1orgusers
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
    "breadcrumbs": [

        "uuid": "<string>",
        "name": "<string>"


    "path": "<string>",
    "parentSpaceUuid": "<string>",
    "childSpaces": [

        "name": "<string>",
        "projectUuid": "<string>",
        "organizationUuid": "<string>",
        "uuid": "<string>",
        "access": [
          "<string>"

        "isPrivate": true,
        "pinnedListUuid": "<string>",
        "pinnedListOrder": 123,
        "slug": "<string>",
        "parentSpaceUuid": "<string>",
        "path": "<string>",
        "chartCount": 123,
        "dashboardCount": 123


    "slug": "<string>",
    "pinnedListOrder": 123,
    "pinnedListUuid": "<string>",
    "groupsAccess": [

        "spaceRole": "viewer",
        "groupName": "<string>",
        "groupUuid": "<string>"


    "access": [

        "inheritedFrom": "organization",
        "inheritedRole": "member",
        "projectRole": "viewer",
        "hasDirectAccess": true,
        "role": "viewer",
        "email": "<string>",
        "lastName": "<string>",
        "firstName": "<string>",
        "userUuid": "<string>"


    "dashboards": [

        "description": "<string>",
        "name": "<string>",
        "projectUuid": "<string>",
        "organizationUuid": "<string>",
        "uuid": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "spaceUuid": "<string>",
        "pinnedListUuid": "<string>",
        "pinnedListOrder": 123,
        "updatedByUser": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"

        "views": 123,
        "firstViewedAt": "<string>",
        "validationErrors": [

            "createdAt": "2023-11-07T05:31:56Z",
            "validationId": 123,
            "error": "<string>"




    "projectUuid": "<string>",
    "queries": [

        "description": "<string>",
        "name": "<string>",
        "projectUuid": "<string>",
        "organizationUuid": "<string>",
        "uuid": "<string>",
        "spaceUuid": "<string>",
        "pinnedListUuid": "<string>",
        "slug": "<string>",
        "spaceName": "<string>",
        "dashboardUuid": "<string>",
        "dashboardName": "<string>",
        "source": "dbt_explore",
        "chartKind": "line",
        "chartType": "cartesian",
        "updatedAt": "2023-11-07T05:31:56Z",
        "pinnedListOrder": 123,
        "updatedByUser": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"

        "firstViewedAt": "2023-11-07T05:31:56Z",
        "views": 123,
        "validationErrors": [

            "createdAt": "2023-11-07T05:31:56Z",
            "validationId": 123,
            "error": "<string>"




    "isPrivate": true,
    "name": "<string>",
    "uuid": "<string>",
    "organizationUuid": "<string>"

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
spaces
/
{spaceUuid}
Try it
200
default
Copy
Ask AI
```

  "results": {
    "breadcrumbs": [

        "uuid": "<string>",
        "name": "<string>"


    "path": "<string>",
    "parentSpaceUuid": "<string>",
    "childSpaces": [

        "name": "<string>",
        "projectUuid": "<string>",
        "organizationUuid": "<string>",
        "uuid": "<string>",
        "access": [
          "<string>"

        "isPrivate": true,
        "pinnedListUuid": "<string>",
        "pinnedListOrder": 123,
        "slug": "<string>",
        "parentSpaceUuid": "<string>",
        "path": "<string>",
        "chartCount": 123,
        "dashboardCount": 123


    "slug": "<string>",
    "pinnedListOrder": 123,
    "pinnedListUuid": "<string>",
    "groupsAccess": [

        "spaceRole": "viewer",
        "groupName": "<string>",
        "groupUuid": "<string>"


    "access": [

        "inheritedFrom": "organization",
        "inheritedRole": "member",
        "projectRole": "viewer",
        "hasDirectAccess": true,
        "role": "viewer",
        "email": "<string>",
        "lastName": "<string>",
        "firstName": "<string>",
        "userUuid": "<string>"


    "dashboards": [

        "description": "<string>",
        "name": "<string>",
        "projectUuid": "<string>",
        "organizationUuid": "<string>",
        "uuid": "<string>",
        "updatedAt": "2023-11-07T05:31:56Z",
        "spaceUuid": "<string>",
        "pinnedListUuid": "<string>",
        "pinnedListOrder": 123,
        "updatedByUser": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"

        "views": 123,
        "firstViewedAt": "<string>",
        "validationErrors": [

            "createdAt": "2023-11-07T05:31:56Z",
            "validationId": 123,
            "error": "<string>"




    "projectUuid": "<string>",
    "queries": [

        "description": "<string>",
        "name": "<string>",
        "projectUuid": "<string>",
        "organizationUuid": "<string>",
        "uuid": "<string>",
        "spaceUuid": "<string>",
        "pinnedListUuid": "<string>",
        "slug": "<string>",
        "spaceName": "<string>",
        "dashboardUuid": "<string>",
        "dashboardName": "<string>",
        "source": "dbt_explore",
        "chartKind": "line",
        "chartType": "cartesian",
        "updatedAt": "2023-11-07T05:31:56Z",
        "pinnedListOrder": 123,
        "updatedByUser": {
          "userUuid": "<string>",
          "firstName": "<string>",
          "lastName": "<string>"

        "firstViewedAt": "2023-11-07T05:31:56Z",
        "views": 123,
        "validationErrors": [

            "createdAt": "2023-11-07T05:31:56Z",
            "validationId": 123,
            "error": "<string>"




    "isPrivate": true,
    "name": "<string>",
    "uuid": "<string>",
    "organizationUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
projectUuid
string
required
The uuid of the space's parent project
spaceUuid
string
required
The uuid of the space to update
#### Body
application/json
name
string
required
isPrivate
boolean
#### Response
200
200 default
application/json
Updated
results
object
required
Show child attributes
status
enum<string>
required
Available options: 
Delete apiv1projects spacesPost apiv1projects spaces
Assistant
Responses are generated using AI and may contain mistakes.


