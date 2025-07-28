# Using the Explore query tracker and Performance panel to monitor query performance  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/query-tracker

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Explore query tracker
  * Explore Performance panel
  * Query phases
    * Query Initialization phase
    * Running Query phase
    * Processing Results phase




Was this helpful?
Send feedback 
#  Using the Explore query tracker and Performance panel to monitor query performance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Explore query tracker
  * Explore Performance panel
  * Query phases
    * Query Initialization phase
    * Running Query phase
    * Processing Results phase


The Explore query tracker and the Explore **Performance** panel provide step-by-step performance data for an Explore query. This data can help identify key entry points for troubleshooting and resolving performance issues with queries and provide recommendations for improvements.
## Explore query tracker
The Explore query tracker displays the progress of an Explore query through the three phases of the query while the query is running.
If a query is taking a long time to execute, the query tracker can indicate which phase of the query is causing the performance issue. This is useful for identifying where performance problems may occur, and where optimization efforts can be the most effective.
The query tracker is displayed when an Explore is running, as long as either the Explore **Visualization** panel or the Explore **Data** panel is open.
## Explore **Performance** panel
To see the Explore **Performance** panel, click the **See performance details** link, which is available on any Explore query that has been run.
The **Performance** panel shows the time that the query spent in each of the three query phases and includes links to performance documentation and the **Query History** System Activity dashboard, which shows current and historical performance data for the query and the Explore that was used to create the query.
## Query phases
When a Looker Explore runs a database query, the query is executed in three phases, as follows:
  * The query initialization phase
  * The running query phase
  * The processing results phase


### Query Initialization phase
During the **Query Initialization** phase, Looker is performing all of the tasks that are required before the query is sent to your database. The **Query Initialization** phase includes the following tasks:
  * Compiling the LookML model
  * Checking to see if any persistent derived tables (PDTs) will need to be built
  * Generating the query SQL
  * Acquiring the database connection


The Understanding query performance metrics documentation page describes how to use the **Query Performance Metrics** Explore in System Activity to view detailed breakdowns of a query. The **Query initialization** phase of the query tracker includes the events that are described in the **Asynchronous worker phase** , **Initialization phase** , and **Connection handling phase** of the **Query Performance Metrics** Explore.
### Running Query phase
The **Running Query** phase is when Looker contacts and queries your database and returns the results of the query. Performance issues during this phase could indicate issue with the external database, such as PDTs that take a long time to rebuild and may need to be optimized, or external database tables that may need optimization. The **Running Query** phase includes the following tasks:
  * Building any PDTs in the database that are required for the Explore query
  * Running the requested query on the database


The Understanding query performance metrics documentation page describes how to use the **Query Performance Metrics** Explore in System Activity to view detailed breakdowns of a query. The **Running query** phase of the query tracker includes the events that are described in the of the **Query Performance Metrics** Explore.
Possible steps to take if you experience performance issues during this phase include the following:
  * Build Explores using `many_to_one` joins whenever possible. Joining views from the most granular level to the highest level of detail (`many_to_one`) typically provides the best query performance.
  * Maximize caching to sync with your ETL policies wherever possible to reduce database query traffic. By default, Looker caches queries for one hour. You can control the caching policy and sync Looker data refreshes with your ETL process by applying datagroups within Explores using the `persist_with` parameter. Maximizing caching enables Looker to integrate more closely with the backend data pipeline, so cache usage can be maximized without the risk of analyzing stale data. Named caching policies can be applied to an entire model or to individual Explores and persistent derived tables (PDTs).
  * Use Looker's aggregate awareness feature to create roll-ups or summary tables that Looker can use for queries whenever possible, especially for common queries of large databases. You can also use aggregate awareness to drastically improve the performance of entire dashboards. See the Aggregate awareness tutorial for additional information.
  * Use PDTs for faster queries. Convert Explores with many complex or unperformant joins, or dimensions with subqueries or subselects, into PDTs so that the views are pre-joined and ready prior to runtime.
  * If your database dialect supports incremental PDTs, configure incremental PDTs to reduce the time Looker spends rebuilding PDT tables.
  * Avoid joining views into Explores on concatenated primary keys that are defined in Looker. Instead, join on the base fields that make up the concatenated primary key from the view. Alternatively, recreate the view as a PDT with the concatenated primary key predefined in the table's SQL definition, rather than in a view's LookML.
  * Use the Explain in SQL Runner tool for benchmarking. `EXPLAIN` produces an overview of your database's query execution plan for a given SQL query, letting you detect query components that can be optimized. Learn more in the How to optimize SQL with `EXPLAIN` Community post.
  * Declare indexes. You can look at the indexes of each table directly in Looker from SQL Runner by clicking the gear icon in a table and then selecting **Show Indexes**.`indexes`, `sort keys`, and `distribution`, can be applied appropriately.


### Processing Results phase
During the **Processing Results** phase, Looker processes and renders the results of the query. The **Processing Results** phase includes the following tasks:
  * Streaming query results to the cache
  * Resolving table calculations
  * Formatting the results of the Liquid templating language
  * Merging queries together
  * Calculating totals and subtotals


The Understanding query performance metrics documentation page describes how to use the **Query Performance Metrics** Explore in System Activity to view detailed breakdowns of a query. The **Processing Results** phase of the query tracker includes the events that are described in the of the **Query Performance Metrics** Explore.
Possible steps to take if you experience performance issues during this phase include:
  * Use features such as merge results, custom fields, and table calculations sparingly. These features are intended to be used as proofs of concept to help design your model. It is best practice to hardcode any frequently used calculations and functions in LookML, which will generate SQL to be processed on your database. Excessive calculations can compete for Java memory on the Looker instance, causing the Looker instance to respond more slowly.
  * Limit the number of views that you include within a model when a large number of view files are present. Including all views in a single model can slow performance. When a large number of views are present within a project, consider including only the view files that are needed within each model. Consider using strategic naming conventions for view file names to enable inclusion of groups of views within a model. An example is outlined in the `includes` parameter documentation.
  * Avoid returning a large number of data points by default within dashboard tiles and Looks. Queries that return thousands of data points will consume more memory. Ensure that data is limited wherever possible by applying frontend  filters to dashboards, Looks, and Explores, and on the LookML level with `required filters`, `conditionally_filter` and `sql_always_where` parameters.
  * Download or deliver queries using the **All Results** option sparingly, as some queries can be very large and overwhelm the Looker server when they're processed.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


