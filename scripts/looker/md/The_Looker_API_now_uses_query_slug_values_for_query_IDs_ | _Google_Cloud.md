# The Looker API now uses query slug values for query IDs  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/api-update-query-slug

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * What do I need to do?
  * How do I find the slug value for a query?
  * How can I tell if we use any of the updated API endpoints?




Was this helpful?
Send feedback 
#  The Looker API now uses query slug values for query IDs
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * What do I need to do?
  * How do I find the slug value for a query?
  * How can I tell if we use any of the updated API endpoints?


The following Looker application API methods don't use a numeric `query_id` value or, in the case of the Query APIs, a numeric `id` value. The following methods use the query slug value instead.
  * Look APIs:
  * Dashboard APIs:
    * Search Dashboard Elements
    * Update DashboardElement
    * Get All DashboardElements
    * Create DashboardElement
  * Render Task APIs:
    * Create Look Render Task
    * Create Query Render Task
    * Create Dashboard Render Task
    * Create Dashboard Element Render Task
  * Scheduled Plan APIs:
    * Scheduled Plans for Space
    * Get All Scheduled Plans
    * Scheduled Plans for Look
    * Scheduled Plans for Dashboard
    * Scheduled Plans for LookML Dashboard
  * Query APIs:
    * Get All Running Queries


## What do I need to do?
The `query_id` field or, in the case of the Query APIs, the `id` field, is a string data type. The `query_id` or `id` fields now return a query slug value in the API response. That query slug value can then be used in any API requests.
For example, if you were to create a query with the **Create Query** API, the `id` would be the query slug in the response. You could then use that `id` to make a subsequent request.
If you have hard-coded numeric query ID values for any of the listed API methods, **you need to update your scripts to use query slug values**!
## How do I find the slug value for a query?
You can find the slug value for a query in the following ways:
  * For an Explore, you can find the slug in the Explore's URL following the `qid=` variable in the URL.
  * You can find the slug value that is associated with a numeric query ID using System Activity.
    1. From the Looker **Explore menu** , select the **System Activity > History** Explore.
    2. From the **Query** view, select the **ID** and **Link** dimensions.
    3. Optionally, add a filter on the **ID** dimension, and enter the query's numeric query ID in the **Query ID** filter field.
    4. Click **Run**.
    5. Click the `[Query]` link next to the numeric query ID in the Explore results to open an Explore based on that numeric query ID.
    6. You can then use the slug in the Explore's URL, which follows the `qid=` variable in the URL.


## How can I tell if we use any of the updated API endpoints?
You can view a list of the API calls that were made to your Looker instance using the API Usage System Activity Explore.
  1. From the Looker **Explore** menu, select the **System Activity** Explore, and then select the **API Usage** view.
  2. Select the **Created Date > Date** and **Endpoint** dimensions and the **Total Usage** measure.
  3. Add a filter on the **Endpoint** dimension, and, in the filter field, include any of the updated endpoints listed at the beginning of this document that you want to search for.
  4. Click **Run**. Looker will display usage information for those endpoints.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


