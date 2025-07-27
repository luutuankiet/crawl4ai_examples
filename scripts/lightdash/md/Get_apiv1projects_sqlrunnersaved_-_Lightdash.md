# Get apiv1projects sqlrunnersaved - Lightdash

**Source:** https://docs.lightdash.com/api-reference/sql-runner/get-apiv1projects-sqlrunnersaved

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
SQL runner
Get apiv1projects sqlrunnersaved
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
    "lastViewedAt": "2023-11-07T05:31:56Z",
    "firstViewedAt": "2023-11-07T05:31:56Z",
    "views": 123,
    "organization": {
      "organizationUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"

    "project": {
      "projectUuid": "<string>"

    "dashboard": {
      "name": "<string>",
      "uuid": "<string>"

    "space": {
      "name": "<string>",
      "uuid": "<string>",
      "isPrivate": true,
      "userAccess": {
        "inheritedFrom": "organization",
        "inheritedRole": "member",
        "projectRole": "viewer",
        "hasDirectAccess": true,
        "role": "viewer",
        "email": "<string>",
        "lastName": "<string>",
        "firstName": "<string>",
        "userUuid": "<string>"


    "lastUpdatedBy": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "lastUpdatedAt": "2023-11-07T05:31:56Z",
    "createdBy": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "createdAt": "2023-11-07T05:31:56Z",
    "chartKind": "line",
    "config": {
      "type": "vertical_bar",
      "metadata": {
        "version": 123

      "display": {
        "stack": true,
        "legend": {
          "align": "start",
          "position": "top"

        "series": {},
        "yAxis": [

            "format": "km",
            "position": "<string>",
            "label": "<string>"


        "xAxis": {
          "type": "time",
          "label": "<string>"


      "fieldConfig": {
        "sortBy": [

            "direction": "ASC",
            "reference": "<string>"


        "groupBy": [

            "reference": "<string>"


        "y": [

            "aggregation": "sum",
            "reference": "<string>"


        "x": {
          "type": "time",
          "reference": "<string>"



    "limit": 123,
    "sql": "<string>",
    "slug": "<string>",
    "description": "<string>",
    "name": "<string>",
    "savedSqlUuid": "<string>"

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
    "lastViewedAt": "2023-11-07T05:31:56Z",
    "firstViewedAt": "2023-11-07T05:31:56Z",
    "views": 123,
    "organization": {
      "organizationUuid": "3c90c3cc-0d44-4b50-8888-8dd25736052a"

    "project": {
      "projectUuid": "<string>"

    "dashboard": {
      "name": "<string>",
      "uuid": "<string>"

    "space": {
      "name": "<string>",
      "uuid": "<string>",
      "isPrivate": true,
      "userAccess": {
        "inheritedFrom": "organization",
        "inheritedRole": "member",
        "projectRole": "viewer",
        "hasDirectAccess": true,
        "role": "viewer",
        "email": "<string>",
        "lastName": "<string>",
        "firstName": "<string>",
        "userUuid": "<string>"


    "lastUpdatedBy": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "lastUpdatedAt": "2023-11-07T05:31:56Z",
    "createdBy": {
      "userUuid": "<string>",
      "firstName": "<string>",
      "lastName": "<string>"

    "createdAt": "2023-11-07T05:31:56Z",
    "chartKind": "line",
    "config": {
      "type": "vertical_bar",
      "metadata": {
        "version": 123

      "display": {
        "stack": true,
        "legend": {
          "align": "start",
          "position": "top"

        "series": {},
        "yAxis": [

            "format": "km",
            "position": "<string>",
            "label": "<string>"


        "xAxis": {
          "type": "time",
          "label": "<string>"


      "fieldConfig": {
        "sortBy": [

            "direction": "ASC",
            "reference": "<string>"


        "groupBy": [

            "reference": "<string>"


        "y": [

            "aggregation": "sum",
            "reference": "<string>"


        "x": {
          "type": "time",
          "reference": "<string>"



    "limit": 123,
    "sql": "<string>",
    "slug": "<string>",
    "description": "<string>",
    "name": "<string>",
    "savedSqlUuid": "<string>"

  "status": "ok"

```

#### Path Parameters
uuid
string
required
the uuid for the saved sql chart
projectUuid
string
required
the uuid for the project
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
Get apiv1projects sqlrunnerresultsDelete apiv1projects sqlrunnersaved
Assistant
Responses are generated using AI and may contain mistakes.


