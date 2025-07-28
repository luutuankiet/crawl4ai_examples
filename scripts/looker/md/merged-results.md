# Merging results from different Explores  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/merged-results

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Understanding merged results
    * What if one query doesn't have a matching data value?
    * What if one query has multiple rows for the same value?
  * Merging queries
    * Creating the primary query
  * Adding the next source query
    * Checking the merge rules and running the merge
    * Using and modifying the merged results
  * Editing merged results
    * Editing the source queries
    * Editing the merge rules
    * Switching the primary query
  * Saving your merged results to a dashboard
  * Merging queries in embedded Looks, dashboards, and Explores




Was this helpful?
Send feedback 
#  Merging results from different Explores
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Understanding merged results
    * What if one query doesn't have a matching data value?
    * What if one query has multiple rows for the same value?
  * Merging queries
    * Creating the primary query
  * Adding the next source query
    * Checking the merge rules and running the merge
    * Using and modifying the merged results
  * Editing merged results
    * Editing the source queries
    * Editing the merge rules
    * Switching the primary query
  * Saving your merged results to a dashboard
  * Merging queries in embedded Looks, dashboards, and Explores


> **Merged Results** is a post-query processing feature that, if not used thoughtfully, can overtax Looker instance resources and cause your Looker instance to respond more slowly for all users. Best practice is to define functions and logic in LookML instead, which generates SQL that is processed by your database. View the Optimize Looker performance Best Practices page for more information about optimizing Looker performance.
Explores in Looker are designed by your Looker developers to combine the data from your database tables in the most effective way by using defined relationships between data fields and tables. Because of this, it is best to use a single Explore to examine your data.
However, there may be times when your Looker developers haven't created the relationships you need or have encountered technical limitations. In these cases, **Merged Results** lets you combine results from different Explores (even from different models or projects) to create data tables on which to Explore and create visualizations. You can use **Merged Results** as a proof of concept to further develop and define your LookML projects and models.
## Understanding merged results
When you merge queries, you start out by creating a single query from a single Explore, and then you combine other queries with that first query.
By default, that first query is considered the _primary_ query. This is an important concept because when Looker matches the data to create the merged results, it matches each added query to the primary query (not to any other added query). So, whenever you add a query, you need to include a dimension that can be matched to a dimension in the primary query.
For example, consider the following queries.
The primary query returns the following results: 
Products Category | Products Count  
---|---  
Active | 5  
Jeans | 9  
Formalwear | 3  
The secondary query returns the following results: 
Products Category | Items in Inventory Count  
---|---  
Active | 11  
Jeans | 16  
Formalwear | 6  
If you merge these queries on the **Products Category** field, Looker produces the following merged results:
Products Category | Products Count | Items in Inventory Count  
---|---|---  
Active | 5 | 11  
Jeans | 9 | 16  
Formalwear | 3 | 6  
Merged results do not perform an actual SQL join. But, for those who are familiar with SQL joins, the **Merged Results** feature combines the results of multiple Explores in a similar way as would a _left join_. The results of the added query are combined with the results of the primary query as if they are being left joined into the primary query.
You don't have to be familiar with the idea of a left join to understand how merged results work. In practical terms, here's why it matters which query is the primary query:
  * **How field names appear:** For matching fields, the primary query's field names are used in the merged results, as shown in the previous example.
  * **How merged results handle a query without a matching value:** The next section, What if one query doesn't have a matching data value?, discusses how Looker handles merging data when only some of the queries have specific value(s) in the matching dimension(s).
You can also reference the Why are there nulls in my secondary merge results query? Best Practices page for more troubleshooting tips for missing or null merged results values.
  * **How merged results handle a query having multiple matching values:** The section What if one query has multiple rows for the same value? later on this page discusses how Looker handles merging data when some of the queries have multiple rows with a specific value (or combination of values) in the matching dimension(s).


### What if one query doesn't have a matching data value?
Another reason the primary query is important is because of the way null values are handled in the matched dimensions:
  * If a row exists in the primary query but not in the additional query, then the added query's fields will be NULL for that row.
  * If a row exists in the added query but not in the primary query, then the row will not show in the results at all.


To illustrate these examples, consider the following example queries.
The primary query returns the following results: 
Products Category | Products Department | Products Count  
---|---|---  
Active | Kids | 522  
Active | Adults | 545  
Dresses | Adults | 878  
Formalwear | Adults | 349  
The secondary query returns the following results: 
Products Category | Products Brand Name | Items in Inventory Count  
---|---|---  
Active | Brand 1 | 223  
Dresses | Brand 2 | 80  
Dresses | Brand 3 | 3  
Jeans | Brand 3 | 8  
Jeans | Brand 2 | 19  
If you merge these queries on the **Products Category** field, Looker produces the following merged results:
Products Category | Products Department | Products Brand Name | Products Count | Items in Inventory Count  
---|---|---|---|---  
Active | Adults | Brand 1 | 545 | 223  
Active | Kids | Brand 1 | 522 | 223  
Dresses | Adults | Brand 2 | 878 | 80  
Dresses | Adults | Brand 3 | 878 | 3  
Formalwear | Adults | ∅ | 349 | ∅  
The primary query has a row for **Formalwear** , so the merged results will show this row. The added query does not have a **Formalwear** row, so any of the fields from the added query will show NULL (∅) for **Formalwear**.
The added query has two rows for **Jeans** , but the primary query does not. So this row is not shown in the merged results at all.
In this example, if you switch the primary query to make the added query the new primary query, Looker instead produces the following merged results:
Products Category | Products Brand Name | Products Department | Items in Inventory Count | Products Count  
---|---|---|---|---  
Active | Brand 1 | Adults | 223 | 545  
Active | Brand 1 | Kids | 223 | 522  
Dresses | Brand 2 | Adults | 80 | 878  
Dresses | Brand 3 | Adults | 3 | 878  
Jeans | Brand 2 | ∅ | 19 | ∅  
Jeans | Brand 3 | ∅ | 8 | ∅  
Looker no longer displays the **Formalwear** rows because they do not exist in our new primary query. However, Looker now displays the **Jeans** rows, and those rows show NULL for the dimensions and measures that are only in the query that is _added_ to the primary query.
You can also reference the Why are there nulls in my secondary merge results query? Best Practices page for more troubleshooting tips for missing or null merged results values.
### What if one query has multiple rows for the same value?
Finally, designating the desired primary query is also important because of the way multiple rows with matching values are handled. If the added query has two or more rows with values that match a row in the primary query, the primary query row will be duplicated that number of times.
In the following example, the _added_ query has two rows for **Dresses**. In the merged results, the **Dresses** values from the primary query appear twice, once for each of the **Dresses** rows from the added query.
The primary query returns the following results: 
Products Category | Products Department | Products Count  
---|---|---  
Active | Kids | 522  
Active | Adults | 545  
Dresses | Adults | 878  
Formalwear | Adults | 349  
The secondary query returns the following results: 
Products Category | Products Brand Name | Items in Inventory Count  
---|---|---  
Active | Brand 1 | 223  
Dresses | Brand 2 | 80  
Dresses | Brand 3 | 3  
Jeans | Brand 3 | 8  
Jeans | Brand 2 | 19  
The merged results query, merging on the **Products Category** field, returns the following results:
Products Category | Products Department | Products Brand Name | Products Count | Items in Inventory Count  
---|---|---|---|---  
Active | Adults | Brand 1 | 545 | 223  
Active | Kids | Brand 1 | 522 | 223  
Dresses | Adults | Brand 2 | 878 | 80  
Dresses | Adults | Brand 3 | 878 | 3  
Formalwear | Adults | ∅ | 349 | ∅  
Note that if you switch the primary query in this case, you would still have two **Dresses** rows, since the newly designated primary query has two rows for **Dresses**. The takeaway is that, when you merge queries, the results may have more rows than the primary query has — but there will never be _fewer_ rows.
## Merging queries
To merge the results from multiple queries, follow these steps:
  1. Create the first source query, called the _primary query_.
  2. Add the next source query.
  3. Check the merge rules for those queries and run the merge.
  4. Optionally, you can:
     * Sort, pivot, and create visualizations for the results.
     * Reuse and share the results using the URL.
     * Modify the results by editing the source queries or adding source queries.


### Creating the primary query
To merge the results from multiple queries, start by preparing the _primary_ query by following these steps:
  1. Select an Explore from the **Explore** menu.
  2. Select the dimensions and measures of interest from the field picker. Do not pivot any dimensions during this step.
This is all you need to start merging results. However, you can also use some advanced exploring techniques to further refine your query. You can:
  3. Optionally, add filters for the data.
  4. Optionally, include table calculations to create ad hoc metrics.
  5. Optionally, click **Run** to see the results of your primary query and to test your filters and table calculations.


## Adding the next source query
Once you've created your primary Explore, add another source query by following these steps:
  1. In your Explore, click the gear icon.
  2. Select **Merge Results**. This will open the **Choose an Explore** window.
  3. In the **Choose an Explore** window, click on the name of an Explore where you will create your next query.
Looker opens the Explore in the **Edit Query** window, where you can build the new query to be merged into your primary query.
> To merge queries, Looker finds dimensions in the queries whose values can be matched. Be sure that your queries contain at least one common dimension whose values can be matched exactly. For example, if both queries have a **Date** dimension, but one query uses "2017-10-01" as a value and the other query uses "October 2017" as a value, Looker can't use that dimension to merge the queries.
  4. Select the dimensions and measures of interest from the field picker. Be sure to include at least one dimension that will exactly match a dimension in the primary query. Do not pivot any dimensions during this step.
  5. Optionally, include filters to narrow the data.
  6. Optionally, incorporate table calculations to create new fields based on the query fields.
  7. Optionally, click **Run** to see the results of the source query and to test your filters and table calculations.
  8. Click **Save** to merge the query into your primary query.


### Checking the merge rules and running the merge
Looker automatically finds the best dimensions to use for matching the queries and displays these matches in the **Merge Rules** section. Looker displays which fields will be used for each merge.
  1. Review the dimensions that Looker used to match the queries. (See Editing merge rules for information on changing these rules.)
  2. Click **Run** to see the merged query results.


Note that any table calculations from the source queries are displayed as standard dimensions in the merged results.
### Using and modifying the merged results
You can use the merged results to:
  * Examine and sort the data, including drilling into the data. If you drill into the dimension used to merge the two Explores, however, Looker displays only drill fields from the primary Explore.
  * View totals. Looker calculates totals on each of the component queries and uses those totals in the merged results. Therefore, totals may appear too high, because what you are seeing are totals calculated before the results were merged. One way to avoid this is to align the filters on each query.
  * Create visualizations.
  * Pivot dimensions in the merged results by selecting **Pivot** from the gear menu in the dimension's column of the data table. Note that you can't pivot dimensions in the source queries.


To reuse the merged results, you can:
  * Share the results using the browser URL.
  * Bookmark the URL in your browser to run the same merged query again in the future. You can't save the merged results as a Look.
  * Save the merged results as a tile on a dashboard (see Saving your merged results to a dashboard).


If you want to modify the merged results, you can:
  * Merge queries from additional Explores by clicking the **Add Query** button and following the same steps.
  * Edit the source queries or configure the way the queries are merged. See Editing merged results for more information.
  * Create filters by adding those filters in the source queries, either when creating and merging the queries, or by editing the queries from the **Merged Results** page. Note that you can't add a filter directly to the merged results.


If you want to clear the cache and retrieve fresh results from your database, select the **Clear Cache & Refresh** option from the gear menu at the top right of the **Merged Results** window.
To download your merged results query, you can save the query to a dashboard and then download the dashboard as a PDF or as a collection of CSV files.
## Editing merged results
Once you have your merged results, you can make the following changes to your merged results:
  * Editing the source queries
  * Editing the merge rules
  * Switching the primary query


### Editing the source queries
From the **Merged Results** window, you can go back and edit the source queries by clicking on the query name in the left pane, or by selecting **Edit** from the query's gear menu. These options take you back to the **Edit Query** screen.
You can add or remove fields, add table calculations, or change the source query's filters. Click **Save** to return to your merged results.
The query's gear menu also has these options:
  * **Rename** : Specify a different name to display for the query in the **Merged Results** window.
  * **Make Primary** : Make the query the base for the merged results. See Understanding merged results to understand the role of the primary query.
  * **Delete** : Remove the query from the merged results. (If you want to add the query back into the merged results after you've deleted it, you can use the **Back** button in your browser.)


### Editing the merge rules
When you add a query, Looker automatically finds dimensions that it can use to match the added query to the primary query. Each added query must have at least one dimension whose values exactly match up to a dimension in the primary query. Looker displays these matches in the **Merge Rules** section, showing which fields will be used to merge the queries.
You can use the Merge Rules section to change or add which fields Looker uses to merge the queries.
  1. Use the drop-down menu to see other dimension options for matching the data.
  2. If there are additional dimensions that could be used for matching, Looker displays **+ Add dimension**. Click **+ Add dimension** to configure an additional set of dimensions to use in the query merge.
  3. Click on the **X** if you don't want to match the data between the two dimensions.


### Switching the primary query
When merging queries, you start out by creating a single query from a single Explore and then you add other queries by combining them with that first query. By default, that first query is considered the _primary_ query, but you can designate any query as the primary query by selecting **Make Primary** from the query's gear menu.
Each added query must have at least one dimension whose values can be matched exactly to a dimension in the primary query.
When you switch the primary query, the merged results are likely to change. See Understanding merged results to understand the role of the primary query.
## Saving your merged results to a dashboard
Once you've added your merged results query to a dashboard, you can add or apply dashboard filters to your merged results tile, rearrange the tile, edit the tile, or add new tiles to your dashboard. You can't download the data from a tile based on merged results, but you can download the dashboard as a PDF or as a collection of CSV files.
> Any dashboard filters applied to a merged results tile will be turned off if the merged query is changed in any way. You can reinstate the filters by turning them back on again in the filter configuration window.
## Merging queries in embedded Looks, dashboards, and Explores
You can merge queries within embedded Looks, dashboards, and Explores, if you have the appropriate permissions. To merge the query of an embedded Look with another query:
  1. Hover over the Look's title to reveal the Look's gear menu and click on the gear menu.
  2. Select **Merge Results** , then follow the steps for merging queries.


To merge an embedded dashboard tile's query:
  1. Hover over the dashboard tile to review the drop-down menu for the dashboard tile.
  2. From the drop-down menu, choose **Explore From Here**. Looker opens the Explore for that tile's query.
  3. Click on the Explore's gear menu and select **Merge Results**.
  4. Follow the steps for merging queries.


## Notes
  * The **Merged Results** feature has a limit of 5,000 rows of data for each of the merged queries. If you include queries that return more than 5,000 rows of data, only the first 5,000 rows that are returned are included in the merged results.
  * All the primary query's fields are displayed in the merged results, using the primary query's names for the fields. This means that if the primary query and an added query use different names for a matching dimension, only the primary query's dimension name will be displayed in the results.


## Conclusion
Whenever possible, you should use the data from a single Explore because your Looker developers have carefully considered how the data from different database tables should be combined. When needed, though, merging results is a powerful technique that lets you combine data from multiple Explores and databases.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


