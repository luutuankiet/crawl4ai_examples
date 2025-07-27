# Admin settings - Labs  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-general-labs

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling and disabling Labs features
  * Current Labs features
  * Beta features
    * Access Studio in Looker
    * Embedding Looker Reports
    * Accessible Data Table Visualizations
    * Complex Filters UI Configuration for Explores
    * Data history playback (data change over time animation) for visualization
    * Full Screen Visualizations
    * In-page Table Calculations
    * New Explore & Look Saving
    * Prerender Iframes (before data loads) for custom visualizations
    * Smart Single Value Text Size
    * Tiered Support Access
  * Experimental features
    * BI Engine Symmetric Aggregates
    * Custom Vis Reliable Render
    * Enhanced Query Admin
    * Guided analyses in System Activity
    * Reduce Filter Queries
    * Rigorous Dashboard Download Permission Checking




Was this helpful?
Send feedback 
#  Admin settings - Labs
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling and disabling Labs features
  * Current Labs features
  * Beta features
    * Access Studio in Looker
    * Embedding Looker Reports
    * Accessible Data Table Visualizations
    * Complex Filters UI Configuration for Explores
    * Data history playback (data change over time animation) for visualization
    * Full Screen Visualizations
    * In-page Table Calculations
    * New Explore & Look Saving
    * Prerender Iframes (before data loads) for custom visualizations
    * Smart Single Value Text Size
    * Tiered Support Access
  * Experimental features
    * BI Engine Symmetric Aggregates
    * Custom Vis Reliable Render
    * Enhanced Query Admin
    * Guided analyses in System Activity
    * Reduce Filter Queries
    * Rigorous Dashboard Download Permission Checking


## Labs overview
Looker Labs features are new, in-progress features whose details may change over time. Labs features are split into two categories:
  * **Beta:** These features are expected to remain in the product, and errors are expected to be resolved at some point. However, these features may change in detail, and errors may not be fixed with the same speed as with normal features. You can see the list of current beta Labs features in the Beta features section on this page.
  * **Experimental:** These features may or may not remain in the product, and errors may or may not be corrected. These experimental features are intended to show you functionality that could be incorporated into Looker in the future and to get your feedback. You can see the list of current experimental Labs features in the Experimental features section on this page.


You can choose to use these features or leave them disabled. You'll see a list of these features on the **Labs** page in the **General** section of the **Admin** panel. Each feature has a short description underneath it explaining the functionality that it adds to or changes in Looker.
## Enabling and disabling Labs features
To enable or disable a feature, click the switch next to the feature name.
> Use caution when disabling a Labs feature. If users or developers have relied on the feature to create a certain behavior, disabling the feature will break that functionality.
## Current Labs features
Looker supports the following beta and experimental Labs features.
## Beta features
Beta Labs features are expected to remain in the product, and errors are expected to be resolved at some point. However, their details may change, and errors may not be fixed with the same speed as they would be for normal features.
### Access Studio in Looker
Enables the Looker} reports feature, which lets you create, view, and edit Looker Studio reports in your Looker instance, including both governed and ad hoc data. You can share and manage your reports in Looker folders and see your recent reports and the reports that you have marked as favorites from the Looker Home page.
### Embedding Looker Reports
Enables private or signed embedding of Looker reports in iframes. See the Embed Looker reports page for more information about embedding Looker reports.
### Accessible Data Table Visualizations
This Labs feature is disabled by default.
When this feature is enabled, the data table visualization will behave slightly differently in order to be fully accessible for all viewers. Specifically, this feature disallows double-clicking on table cells and unpins the row number column from the left side of the table.
### Complex Filters UI Configuration for Explores
This Labs feature is enabled by default.
When this feature is enabled and a comma is entered into a filter expression, matches (advanced) filters no longer update to simpler filter types until the page is reloaded. This feature resolves a few stability issues with matches (advanced) filters.
### Data history playback (data change over time animation) for visualization
This Labs feature is disabled by default.
If enabled, this Labs feature allows users to explore data changes over time for visualizations within dashboards. See the Viewing dashboards documentation page for more information.
### Full Screen Visualizations
This Labs feature is enabled by default.
When enabled, this feature enables full-screen and expanded views for visualizations within dashboard tiles. See the Viewing dashboards documentation page for more information on view options.
Full-screen and expanded functionality can be turned off on a dashboard in the dashboard's **Settings** menu.
### In-page Table Calculations
This Labs feature is disabled by default.
The **In-page Table Calculations** Labs feature lets users create and edit table calculations directly in an Explore's **Data** section instead of using either the **Create table calculation** or the **Edit table calculation** dialog. Creating and editing table calculations in the **Data** section lets users reference fields and values in an Explore query as they create and edit table calculation expressions.
### New Explore & Look Saving
This Labs feature is disabled by default.
This feature improves the visibility and navigation of **Save** dialogs on the Explore and Look pages. The new experience allows quick navigation of folders, and users can choose to sort existing content by Name, Created Date, or Last Update. It does not change any functionality of these pages.
### Prerender Iframes (before data loads) for custom visualizations
This Labs feature is disabled by default.
This feature reduces the custom visualization loading time by starting to render the iframe even before query data has been loaded.
### SQL Runner Vis
This Labs feature is disabled by default.
This feature adds the ability to visualize ad hoc queries from SQL Runner.
### Smart Single Value Text Size
This Labs feature is disabled by default.
Enabling the **Smart Single Value Text Size** Labs feature automatically resizes the fonts on single value visualizations displayed within dashboard tiles. Fonts are resized to display at least 8-10 value characters within a tile; if the characters in the visualization overflow horizontally or vertically at a given size, the font size will step down. The minimum font size allowed is 14 pixels. Once the minimum font size is reached, any overflowing characters will be truncated with an ellipsis (...). The maximum font size allowed is 104 pixels.
When you're using this Labs features, single value tiles on dashboards may look less consistent, but more characters will fit on smaller tiles.
### Tiered Support Access
This Labs feature is enabled by default.
Enabling the **Tiered Support Access** Labs feature enables enhanced support access, including updated access duration times and access levels. For more information, see the Admin settings - Support Access documentation page. Disabling this Labs feature enables legacy support access.
### Visual Drilling
This Labs feature is enabled by default.
The **Visual Drilling** Labs feature is not supported by dashboards. For dashboards, visual drilling is possible through the use of the `link` parameter without needing to enable the Labs feature.
When **Visual Drilling** is turned off, the drill overlay always displays the data table.
When **Visual Drilling** is enabled, the drill overlays for Looks and Explores consider the underlying data to select the best visualization type, which can be a table visualization or some other visualization type. Or, with **Visual Drilling** enabled, you can use the `link` parameter to customize a drill visualization, as shown on the `link` parameter documentation page and on the More powerful data drilling Best Practices page. When the visualization from a drill is not a table, buttons let the user switch between the default visualization type and a data table.
For more information about visualization types, see the Visualization types documentation page.
## Experimental features
Experimental Labs features may or may not remain in the product, and errors may or may not be corrected. These experimental features are intended to show you functionality that could be incorporated into Looker in the future. We always welcome your feedback.
### BI Engine Symmetric Aggregates
This Labs feature is disabled by default.
When the **BI Engine Symmetric Aggregates** Labs feature is enabled, for queries that use symmetric aggregates, Looker will generate experimental SQL patterns that are designed to execute faster on the Google BigQuery BI Engine. This feature should have no effect on query results, only on execution performance.
### Custom Vis Reliable Render
This Labs feature is disabled by default.
When this Labs feature is enabled, Looker suppresses refresh behavior in custom visualizations to fix partial PNG and PDF renders.
### Enhanced Query Admin
This Labs feature is disabled by default.
When enabled, this feature enhances the **Queries** page in the **Database** section of the **Admin** menu. The enhanced page features tabs for **Recent** and **Complete** queries. These tabs are paginated for improved performance, and display 50 queries per page.
  * The **Recent** tab displays queries run in the last hour. From this tab, Looker admins can cancel running queries.
  * The **Complete** tab displays the most recent 500 queries.


### Guided analyses in System Activity
This Labs feature is disabled by default.
When enabled, the **History** System Activity Explore displays guided analysis options to provide a question-and-answer format for performing analyses.
### Reduce Filter Queries
This Labs feature is disabled by default.
This feature reduces the number of queries that are sent by filters. When **Reduce Filter Queries** is enabled, Looker moves any filter that requests suggestions into a dialog where the filter won't fetch suggestions until a user clicks on it in the dialog.
### Redux DevTools
This Labs feature is disabled by default.
This feature enables Redux DevTools for debugging application state.
### Rigorous Dashboard Download Permission Checking
This Labs feature is disabled by default.
When this feature is enabled, users can download a dashboard only if they have the `download_with_limit` or `download_without_limit` permission on every model that is included in the dashboard.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


