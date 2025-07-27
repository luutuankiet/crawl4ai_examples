# SQL Runner - Lightdash

**Source:** https://docs.lightdash.com/references/sql-runner

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
SQL Runner
SQL Runner
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference
    * Lightdash CLI reference
    * Feature Maturity Levels
    * SQL Runner


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Getting started with the SQL Runner
  * Saved charts in the SQL Runner


A query built in the SQL runner can be:
  * used to power a single saved chart
  * turned into a virtual view so it becomes a reusable table
  * written back to dbt as a model

Only users with `developer or admin access` can use the SQL runner.
##  Getting started with the SQL Runner
The SQL Runner can be accessed from the `New` —> `Query using SQL Runner` option in your navigation bar. Once you’re in the SQL Runner, you’ll see four key components:
  1. A list of tables in your data warehouse that Lightdash has access to (based on your data warehouse connection in Lightdash).
  2. The schema of a selected table.
  3. The SQL query builder.
  4. The results from your latest SQL query.

To build a query in the SQL Runner, just write your query in the SQL query builder, then hit `Run query` to see the results. You can access your **Query history** from your session by clicking on the `SQL Query history` button beside `Run query`. Once you’ve run your query, you can either:
  1. **Build and save a Chart**
  2. **Create a Virtual View so your query becomes a reusable table in Lightdash**
  3. **Write-back to dbt so your query is saved as a governed model.**
  4. Click the link icon in the top-right to share your query draft with a coworker (or save it yourself to return to later).


##  Saved charts in the SQL Runner
Once you’ve run your query, you can build a chart by clicking on the `chart` tab in the SQL Runner. The charts in the SQL Runner are built from the data that you generated in your query. The chart builder automatically aggregates the data from your query results using the aggregation type that you choose. Depending on the column type, the aggregation options are:
  * count (which is a distinct count and will ignore duplicates)
  * any (which will count and include duplicates)
  * sum
  * average
  * max
  * min

Once you’ve configured your chart, you can save it, add it to a space, and add it to a dashboard by hitting `save chart`. SQL runner charts on a dashbaord can be filtered in the UI. See the filter documentation for more information.
Feature Maturity LevelsVirtual Views
Assistant
Responses are generated using AI and may contain mistakes.


