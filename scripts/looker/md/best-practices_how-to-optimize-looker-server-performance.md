# Optimize Looker performance  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-server-performance

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Optimize query performance
  * Optimize Looker server performance




Was this helpful?
Send feedback 
#  Optimize Looker performance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Optimize query performance
  * Optimize Looker server performance


> _These best practices reflect recommendations shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations, but you should use your best judgment when implementing._
## Optimize query performance
You can ensure that queries are built and executed optimally against your database with the following frontend and backend tips: 
  * Build Explores using `many_to_one` joins whenever possible. Joining views from the most granular level to the highest level of detail (`many_to_one`) typically provides the best query performance. 
  * Maximize caching to sync with your ETL policies wherever possible to reduce database query traffic. By default, Looker caches queries for one hour. You can control the caching policy and sync Looker data refreshes with your ETL process by applying datagroups within Explores, using the `persist_with` parameter. This enables Looker to integrate more closely with the backend data pipeline, so cache usage can be maximized without the risk of analyzing stale data. Named caching policies can be applied to an entire model and/or to individual Explores and persistent derived tables (PDTs). 
  * Use Looker's aggregate awareness functionality to create roll-ups or summary tables that Looker can use for queries whenever possible, especially for common queries of large databases. You can also leverage aggregate awareness to drastically improve the performance of entire dashboards. See the Aggregate awareness tutorial for additional information. 
  * Use PDTs for faster queries. Convert Explores with many complex or unperformant joins, or dimensions with subqueries or subselects, into PDTs so that the views are pre-joined and ready prior to runtime. 
  * If your database dialect supports incremental PDTs, configure incremental PDTs to reduce the time Looker spends rebuilding PDT tables. 
  * Avoid joining views into Explores on concatenated primary keys that are defined in Looker. Instead, join on the base fields that make up the concatenated primary key from the view. Alternatively, recreate the view as a PDT with the concatenated primary key predefined in the table's SQL definition, rather than in a view's LookML. 
  * Leverage the Explain in SQL Runner tool for benchmarking. `EXPLAIN` produces an overview of your database's query execution plan for a given SQL query, letting you detect query components that can be optimized. Learn more in the How to optimize SQL with `EXPLAIN` Community post. 
  * Declare indexes. You can look at the indexes of each table directly in Looker from SQL Runner by clicking the gear icon in a table and then selecting **Show Indexes**.`indexes`, `sort keys`, and `distribution`, can be applied appropriately. 
  * Increase memory, cores, and I/O (input/output) of databases with insufficient hardware or necessary provisioned resources (such as AWS) for processing large datasets, to increase query performance. 


## Optimize Looker server performance
You can also take measures to ensure that the Looker server and application are performing optimally: 
  * Limit the number of elements within an individual dashboard. There is no precise rule for defining the number, because the design of each element impacts memory consumption based on a variety of factors; however, dashboards with 25 or more tiles tend to be problematic when it comes to performance. 
  * Use the dashboard auto refresh feature strategically. If a dashboard uses auto refresh, make sure it refreshes no faster than the ETL processes running behind the scenes. 
  * Use pivots strategically, and avoid over-using pivots within dashboard tiles and Looks. Queries with pivoted dimensions will consume more memory. The more dimensions that are pivoted, the more memory is consumed when content (an Explore, a Look, or a dashboard) is loaded. 
  * Use features, such as merge results, custom fields, and table calculations, sparingly. These features are intended to be used as proofs of concept to help design your model. It is best practice to hardcode any frequently used calculations and functions in LookML, which will generate SQL to be processed on your database. Excessive calculations can compete for Java memory on the Looker instance, causing the Looker instance to respond more slowly. 
  * Limit the number of views included within a model when a large number of view files are present. Including all views in a single model can slow performance. When a large number of views are present within a project, consider including only the view files needed within each model. Consider using strategic naming conventions for view file names, to enable easy inclusion of groups of views within a model. An example is outlined in the `includes` parameter documentation. 
  * Avoid returning a large number of data points by default within dashboard tiles and Looks. Queries that return thousands of data points will consume more memory. Ensure that data is limited wherever possible by applying frontend  filters to dashboards, Looks and Explores, and on the LookML level with `required filters`, `conditionally_filter` and `sql_always_where` parameters. 
  * Download or deliver queries using the **All Results** option sparingly, as some queries can be very large and overwhelm the Looker server when processed. 


For more help identifying the source of performance issues, check out the Performance overview Best Practices page. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


