# Considerations when building performant Looker dashboards  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/considerations-when-building-performant-dashboards

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Considerations when building performant Looker dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
One of the best ways to empower users to explore data is by providing them with curated views by building effective Looker dashboards. If you want to create a great performance experience for your users, consider the tips on this page as you design your dashboards. 
Looker dashboards load in the browser. To build for optimal performance, keep the following facts in mind. 
The most important element of dashboard performance is the underlying SQL query performance. Each dashboard element, when not returned from cache, runs a SQL query that takes time to execute on the underlying database. See the **Optimize Query Performance** section of the Optimize Looker performance Best Practices page for more details regarding building performant queries.
Some components are more memory-intensive than they are SQL-related — these can cause slow performance in dashboards: 
  * **Data volume has the greatest impact on performance.** The more data that is returned in an individual element, the more memory resources will be consumed. Looks and dashboard elements that are returned with many thousands of data points will use more memory. 
  * **Limit the number of dashboard elements.** There is no hard and fast rule about the number, since the design of a single element impacts its memory consumption based on a few factors (covered later on this page). However, avoid creating dashboards with 25 or more queries. Keep dashboard performance slick by creating navigation links between dashboards or by creating links to custom URLs to create a curated navigation from dashboard to dashboard. You can also try concatenating similar measures into the same single value visualization to avoid many single tile visualizations. 
  * **Use dashboard settings strategically.** If your dashboard uses autorefresh, make sure it refreshes no faster than your ETL process. In general, you should avoid setting the autorefresh faster than 15 minutes. Don't use run on load if the dashboard is meant to be filtered. Use required filters to prevent users from running dashboards without the necessary filters. 
  * **Leverage caching.** It's best practice to use  datagroups to sync all Looker content (dashboards, Looks, schedules) with your ETL process. This helps avoid unnecessary querying when the data is not up to date. 
  * **Post-query processing features, such asmerged results, custom fields, and table calculations, consume memory.** The more post-query processing features used, the more memory is consumed. If you are using the same table calculations, merged results, or custom fields across multiple Looks and dashboards, consider hard-coding them into your LookML model wherever possible. In general, don't add more than four merged results tiles to a dashboard. 
  * **Pivoted dimensions consume memory.** The more dimensions that are pivoted in a Look or dashboard tile, the more memory is consumed when the dashboard is loaded. As mentioned in the first bullet point, this is because more data is used as more data is returned. If the dimension you are pivoting has high cardinality (many unique values), there will be a column for each value. Filter at the dashboard or Look level to allow the user to select the dimension values that they are most interested in comparing, as opposed to showing everything at once. 
  * **Having many columns and rows consumes more memory.** For browser performance, 50 or fewer columns is recommended. Again, as discussed in the first bullet point, Looks returning a high volume of rows and many columns can slow performance. Filter at the dashboard or Look level to reduce the number of results within an element. 
  * Leverage shared filters with a single query to render a single query result across multiple tiles. This should reduce the total number of queries run from the dashboard by leveraging one query to power multiple dashboard elements. 
  * **deliver queries using the **All Results** option sparingly, as some queries can be very large and overwhelm the Looker server when processed. **

**
Make sure that you test dashboard performance after you add elements. As you are building, continue to navigate to the dashboard and refresh the page to determine how performance is impacted as you add additional Looks. 
Once you are satisfied with your new Looker dashboard, be sure to utilize folder permissioning to ensure that the dashboard cannot inadvertently be changed. Leverage user groups to manage content access and permissions in bulk, instead of on an individual-user basis. 
If you're having performance issues, reach out to Looker Support directly — our team is always ready to investigate and lend a hand! 
**
**
Was this helpful?
Send feedback  ****
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.
**


