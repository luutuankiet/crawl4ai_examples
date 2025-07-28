# Looker and Looker Studio shared terms and concepts  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-and-studio-shared-terms-glossary

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Connection, connector
  * Content access; roles, permissions
  * Cross-filtering dashboards, chart cross-filtering
  * Dashboard, report
  * Dashboard filter, filter properties
  * Dashboard filter controls, filter controls
  * Data access, credentials
  * Linked filters, filter inheritance
  * Measure, metric
  * Merged results, blended data
  * Report, report
  * Parameter, parameter
  * Table calculations, calculated fields




Was this helpful?
Send feedback 
#  Looker and Looker Studio shared terms and concepts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Connection, connector
  * Content access; roles, permissions
  * Cross-filtering dashboards, chart cross-filtering
  * Dashboard, report
  * Dashboard filter, filter properties
  * Dashboard filter controls, filter controls
  * Data access, credentials
  * Linked filters, filter inheritance
  * Measure, metric
  * Merged results, blended data
  * Report, report
  * Parameter, parameter
  * Table calculations, calculated fields


This page lists the terms and concepts that are similar between the Looker and Looker Studio products as well as in the Looker and Looker Studio user documentation. This page also highlights the similarities, differences, and nuances of those terms and concepts.
The following Looker and Looker Studio terms and concepts are outlined on this page, with the Looker term or concept appearing first:
  * Connection, connector
  * Content access; roles, permissions
  * Cross-filtering dashboards, chart cross-filtering
  * Dashboard, report
  * Dashboard filter, filter properties
  * Dashboard filter control, filter controls
  * Data access, credentials
  * Linked filters, filter inheritance
  * Measure, metric
  * Merged results, blended data
  * Report, report
  * Parameter, parameter
  * Table calculations, calculated fields


Each term or concept is identified with one of the following labels:
  * Same (Same) — The Looker and Looker Studio term or concept share the same meaning and function in both applications.
  * Similar (Similar) — The Looker and Looker Studio term or concept have a _similar_ function, but differ in nuanced ways.
  * Different (Different) — The Looker and Looker Studio term or concept have _different_ meanings and functions in each application.


See the Connecting to Looker Studio documentation page to learn more about connecting Looker and Looker Studio.
## Connection, connector
Similar
**Looker term** : Connection
In the **Admin** section of Looker, you establish the database connection from which a model will retrieve data.
**Looker Studio term** : Connector
The mechanism by which Looker Studio accesses a specific data platform, system, or product. Connectors let Looker Studio query your underlying data. Connecting to your data creates a _data source_ in Looker Studio.
Data sources represent a particular instance of a connector: for example, a connection to a specific BigQuery table or query, a Google Analytics property, or a Google Sheet. Data sources let you configure the fields and options that are provided by the connector that is used to create that connection instance. In addition, the data source gives you a secure way to share information and insights with report viewers who may not be able to directly access the underlying data.
### Similarities
Connecting to data in Looker and Looker Studio is **similar** in the following ways:
  * Looker and Looker Studio can retrieve data from external sources of data.
  * Looker and Looker Studio can connect to multiple sources of data, such as multiple databases for a Looker instance or multiple data sources for Looker Studio.


### Differences
Connecting to data in Looker and Looker Studio is **different** in the following ways:
  * In **Looker** , data models retrieve their data from the database that only a Looker admin connects to the Looker instance through a database connection. Only Looker admins can enable connectors to allow users to interact with data from a Looker Explore in another application.
  * In **Looker Studio** , any user with the permissions to add data sources can use a connector to connect to the specific kind of data that they want to visualize in Looker Studio. Connectors can be used to connect to more than just databases.


## Content access; roles, permissions
Similar
**Looker** term: Content access
Content access lets admins limit what users can view and interact with in Looker. Content access controls whether a user or group can view or make changes to a board, or to a folder and its contents.
**Looker Studio** term: Roles, permissions
Access to Looker Studio assets (reports and data sources) is based on the Google Cloud Identity and Access Management (IAM) system.
With IAM, you can manage access to Looker Studio assets by assigning users to a predefined role. A role is a collection of permissions that allows users to perform certain actions while preventing them from performing other actions.
### Similarities
Content access management in Looker and Looker Studio is **similar** in the following ways:
  * Users are granted roles that let them perform specific actions on specific types of content.
  * **Looker (Google Cloud core)** and **Looker Studio** roles are based on IAM roles.


### Differences
Content access management in Looker and Looker Studio is **different** in the following ways:
  * **Looker** uses a system of roles and content access that is unique to the Looker instance. A Looker admin grants users roles that are a combination of permissions to perform certain actions and a set of data models upon which those actions can be performed. Content access levels grant users the ability to view or edit collections of Explores, Looks, and dashboards that are contained within boards and folders.
  * **Looker (Google Cloud core)** uses both Looker roles and IAM roles. Within a Looker (Google Cloud core) instance, content and feature access is managed identically to Looker. Administrative functions that are performed in the Google Cloud console are managed using IAM roles.
  * **Looker Studio** users are granted IAM roles with permissions that enable them to perform certain actions in specific types of content, called assets, such as reports or data sources. Roles and permissions don't grant users the ability to see the asset's underlying data.
  * **Looker Studio Pro** users are additionally granted team workspace roles to govern access to the assets that are contained in a workspace.


**Custom roles** are handled differently in Looker and Looker Studio in the following ways:
  * **Looker** allows the creation of custom roles.
  * **Looker (Google Cloud core)** allows the creation of custom roles, both for IAM roles for tasks performed in the Google Cloud console, and for Looker roles within the Looker (Google Cloud core) instance.
  * **Looker Studio** and **Looker Studio Pro** _don't_ support custom roles.


## Cross-filtering dashboards, chart cross-filtering
Similar
**Looker term** : Cross-filtering dashboards
Cross-filtering makes it easier and more intuitive for dashboard viewers to interact with a dashboard's data and understand how one metric affects another. With cross-filtering, dashboard viewers can select a data point in one dashboard tile to filter all dashboard tiles on that value.
Dashboard editors can create multiple cross-filters at one time, and cross-filters can be used in conjunction with standard dashboard filters. For cross-filtering to be turned on successfully, all dashboard tiles must be created from the same Explore.
Some visualization types don't support cross-filters.
**Looker Studio term** : Chart cross-filtering
Cross-filtering lets report viewers interact with one chart and apply that interaction as a filter to other charts in the report. When cross-filtering is turned on for a chart, report viewers can filter the report by interacting with that chart in two ways:
  * Click one or more dimension values in the chart.
  * Select an area by clicking and dragging your mouse across a time series, a line chart, or an area chart.


Cross-filtering works in the same way as other controls. For example, a pie chart that is based on a **Country** dimension lets report viewers filter a report in the same way as a drop-down list control that is based on the **Country** dimension. Brushing a time series acts in the same way as a date range control.
Report editors can restrict cross-filtering to groups, just like other controls.
Some visualization types don't support cross-filters.
## Dashboard, report
Similar
**Looker term** : Dashboard
A dashboard is a collection of one or more saved queries, displayed as visualization or as text tiles together on one page. Looker offers two types of dashboard experience: user-defined dashboards and LookML dashboards.
  * User-defined dashboards are created by adding content through Looker's user interface, rather than using LookML. This is the most common type of dashboard in Looker.
  * LookML dashboards are written entirely using LookML.


**Looker Studio term** : Report
A report is a Looker Studio asset that presents information and insights that are derived from your data.
Reports let you visualize your data, gain insights, and share those insights with others. You can share reports with other people and let them only view the data, or you can give them edit access so that they can change the report structure. Reports can consist of multiple pages, charts, and other components, such as controls, text areas, shapes, and images.
Reports derive their data from one or more data sources.
### Similarities
Both dashboards in **Looker** and reports in **Looker Studio** let users visualize data from at least one model or data source, respectively. Both are composed of modular elements — in **Looker** they are called _tiles_ , and in **Looker Studio** they are called _components_.
### Differences
Dashboards in **Looker** and reports in **Looker Studio** handle user access differently — for **Looker** , see content access; for **Looker Studio** , see credentials.
Although the appearance both dashboards and reports can be customized with custom themes and different types of elements, each type of report component — controls, charts, or all report components — can be uniquely stylized.
Users create report components and create dashboard tiles using different methods. Report components are added to a report from the report panels. Dashboard tiles can be created as Explore or Looks and then later saved to a dashboard or they can be created directly in the dashboard. LookML dashboards are created by LookML developers and stored as version-controlled files.
## Dashboard filter, filter properties
Similar
**Looker term** : Dashboard filters
Dashboard filters let dashboard viewers narrow a dashboard's results to only the data that the viewer is interested in. Dashboard filters can apply to all tiles on a dashboard or to only one dashboard tile.
Dashboard editors have several options for altering the way dashboard filters are displayed to viewers. Dashboard editors can adjust the appearance of individual filter controls or of the entire filter bar.
**Looker Studio term** : Filter properties
Filter properties (or just filters, for short) refine or reduce the data that is shown to report viewers.
Filters can be applied to a chart, a control, a page, or an entire report.
Only report editors can change or interact with filter properties. Report viewers cannot change filter properties unless a report editor adds a filter control.
### Similarities
Dashboard filters in Looker and filter properties in Looker Studio are **similar** in the following ways:
  * Dashboard filters in **Looker** and filter properties in **Looker Studio** filter results that the users see on dashboards and reports.
  * Dashboard filters in **Looker** and filter properties in **Looker Studio** can be applied to entire dashboards (in Looker) or reports (in Looker Studio), or to individual dashboard tiles (in Looker) or charts (in Looker Studio).


### Differences
Dashboard filters in Looker and filter properties in Looker Studio are **different** in the following ways:
  * Dashboard filters in **Looker** can be changed by users who have the appropriate folder access level and Looker permissions to edit the dashboard. Filter properties in **Looker Studio** can only be changed by report editors. Report viewers cannot change filter properties unless a report editor adds a filter control to the report.
  * Dashboard filters in **Looker** can only be applied to entire dashboards or to individual tiles. Filter properties in **Looker Studio** can be applied to individual report pages and controls, in addition to entire reports.


## Dashboard filter controls, filter controls
Similar
**Looker term** : Dashboard filter controls
Dashboard filter controls let dashboard editors customize the appearance of filters for dashboard viewers. The filter control types that are available in the Control drop-down as editors create a dashboard filter depend on the LookML data type that is assigned to the field you're filtering on.
Dashboard filter control types include button groups, checkboxes, radio buttons, sliders, and date range control, among other options.
**Looker Studio term** : Filter controls
Filter controls, or controls, let report viewers filter or change the data that is displayed in a report's components. Controls also provide a way to gather user input and use it in calculated fields and in connectors that support parameters, such as BigQuery and community connectors.
With controls, report viewers can perform the following actions:
  * Filter the data by specific dimension values.
  * Set the timeframe of the report.
  * Set parameter values that can then be used in calculated fields or passed back to the connector.
  * Change the underlying dataset that is used by a data source.


Filter control types include drop-down lists, input boxes, sliders, and checkboxes, among other options.
Report editors can limit the scope of a control by grouping it with one or more charts. Once grouped, the control only affects the charts that are in the group.
### Similarities
Dashboard filter controls in Looker and filter controls in Looker Studio are **similar** in the following ways:
  * Dashboard filter controls in **Looker** and filter controls in **Looker Studio** are configured by dashboard editors (in Looker) and report editors (in Looker Studio) to let viewers filter and limit data.
  * Dashboard filter controls in **Looker** and filter controls in **Looker Studio** can be set on multiple specific dashboard tiles (in Looker) and charts (in Looker Studio) at once. In Looker Studio, this is called a _group_.
  * The types of dashboard filter controls in **Looker** and filter controls in **Looker Studio** that can be applied are dependent on the data type of the underlying filter field.


### Differences
Dashboard filter controls in Looker and filter controls in Looker Studio are **different** in the following ways:
  * When configured, filter controls in **Looker Studio** can change the underlying dataset that is used by a data source. Filter controls in **Looker Studio** can also apply to calculated fields, and to connectors that support parameters such as BigQuery and community connectors.


## Data access, credentials
Similar
**Looker term** : Data access, access level
Data access controls which data a user or group is allowed to view. This type of access can be restricted or granted either at the user level or at the data level. Data access is primarily managed using model sets.
**Looker Studio term** : Credentials
Credentials determine who can see the data from a data source. When a Looker Studio data source is created, its creator chooses how Looker Studio will control access to the data provided by the data source. Credentials tell Looker Studio whether to grant the user the ability to access the data source's data with the credentials of the data source's owner or whether the user will have to provide their own credentials. In the latter case, if a user does not have access to the data from its original source, they won't be able to view that data in any Looker Studio assets.
### Similiarities
Data access management in Looker and Looker Studio is **similar** in the following ways:
  * Users can access the underlying data for various types of content.
  * In **Looker** , data models form the basis of all Looker content, including Explores, Looks, and dashboards.
  * In **Looker Studio** , credentials control a user's ability to interact with the underlying data from a specific Looker Studio data source.


### Differences
Data access management in Looker and Looker Studio is **different** in the following ways:
  * In **Looker** , users can access the underlying data for any model sets to which they have been granted specific permissions to perform actions.
  * In **Looker Studio** , if a data source is created requiring Looker Studio's credentials, the user must have access to the data from wherever that data originated.


## Dimension
Same
**Looker term** : Dimension
A dimension is a field that represents an attribute, a fact, or a value, which can be selected from the field picker within an Explore and can be used to filter a query. Common dimensions include such attributes as dates, names, and IDs, and they often correspond to columns in your underlying data table. A dimension can also be created within a view file.
**Looker Studio term** : Dimension
A dimension is a set of values by which you can group your data.
Dimensions are categories of information. The values contained in those categories are typically names, attributes, or other characteristics of that data. Dimensions contain unaggregated data. Dimensions appear as green fields in the data source editor and the report **Properties** panel.
## Linked filters, filter inheritance
Similar
**Looker term** : Linked filters
Dashboard editors can link filters so that the filter value options for one filter are narrowed based on the filter value or values that are selected for a different filter on the same dashboard.
When dashboard editors are linking filters, any filter can be used as the "parent" filter (the filter that narrows the options of another filter), but the "child" filter (the filter to be narrowed) can only use a field of `type: string`, commonly used for words or phrases, or `type: zipcode`, commonly used for zip codes.
If there is only one filter on the dashboard, the ability to link filters is disabled.
**Looker Studio term** : Filter inheritance
Filters can be inherited, meaning that filters on higher level components apply to the components beneath them. The order of inheritance is report level > page level > chart or control level.
In order for a lower-level (child) component to inherit filters from a higher-level (parent) component, the dimensions and metrics that are used in the parent's filters must exist in the child component's data source. If they don't, then inheritance is turned off for the child component.
Report editors can turn off inheritance by using the toggle in the Filter section of the Setup tab in the Properties panel for a selected component. For example, you can tell a chart not to inherit a page level filter property, or you can tell a page not to inherit the report level property.
### Similarities
Linked filters in Looker and filter inheritance in Looker Studio are **similar** in the following way:
  * Both linked filters in **Looker** and filter inheritance in **Looker Studio** hierarchically impact lower-level filters and components, so that the filter value options for child filters are narrowed based on the filter value or values that are selected for a parent filter.


### Differences
Linked filters in Looker and filter inheritance in Looker Studio are **different** in the following ways:
  * Linked filters in **Looker** must be set up by a dashboard editor. Filter inheritance in **Looker Studio** is enabled by default and must be disabled by a report editor.
  * Linked filters in **Looker** affect the dashboard globally; wherever a linked filter is applied, the link must be obeyed.
  * Filter inheritance in **Looker Studio** can be disabled for individual components. For example, you can configure a chart that doesn't inherit a page level filter property, or a page that doesn't inherit the report level property.


## Measure, metric
Similar
**Looker term** : Measure
A measure is a field in an Explore that represents measurable information about your data, such as sums and counts. A measure is declared in the LookML of a view file using aggregate functions such as `SUM()` and `COUNT()`. Although typically measures are of an aggregate type, they can also be a non-aggregate type such as `type: number`. Measure aggregates are grouped by dimensions in a Looker Explore.
**Looker Studio term** : Metric
A metric is a specific aggregation that is applied to a set of values.
Metrics are aggregations that come from the underlying dataset or that are the result of implicitly or explicitly applying an aggregation function, such as `COUNT()`, `SUM()`, or `AVG()`. The metric itself has no defined set of values, so you can't group by it as you can with a dimension.
### Similarities
Measures in Looker and metrics in Looker Studio are **similar** in the following ways:
  * Measures in **Looker** and metrics in **Looker Studio** represent the measurable information about your data.
  * Users can create measures or metrics by applying aggregation functions to existing dimensions or measures. **Looker** refers to these user-generated measures as _custom measures_ , which are created in Looker Explores. **Looker Studio** refers to these user-generated aggregation functions as _calculated fields_.


### Differences
Measures in Looker and metrics in Looker Studio are **different** in the following ways:
  * Measures in **Looker** are declared in a model's view file or as custom measures in an Explore.
  * Metrics in **Looker Studio** represent aggregations that are derived directly from the underlying dataset.


## Merged results, blended data
Similar
**Looker term** : Merged results
The **Merged Results** feature lets you combine data from different Explores (even from different models, projects, or connections). Using merged results, you can create a query from an Explore and then add queries from other Explores to display the merged results in a single table. The **Merged Results** feature performs similarly to a left join in SQL: it's as if the added query is being left-joined into the primary query.
**Looker Studio term** : Blended data
Blended data is data that is derived by joining fields from different data sources, or multiple instances of the same data source.
Blending data lets you plot information from distinct data sets in a single chart, making it easier to see the interrelationships between that data.
### Similarities
Merged results in Looker and blends (blended data) in Looker Studio are **similar** in the following ways:
  * Both merged results in **Looker** and blends in **Looker Studio** let you combine data from multiple sources within a single query.
  * Both merged results in **Looker** and blends in **Looker Studio** use concepts that are similar to SQL joins to match and combine data that is based on common fields (like an ID dimension), which lets you relate records from various sources for analysis and visualization.
  * Neither merged results in **Looker** nor blends in **Looker Studio** can be saved as a standalone, reusable object: 
    * Merged results in **Looker** can't be saved as Looks, but they can be saved to multiple dashboards.
    * Blends in **Looker Studio** are embedded within the report where they're defined (although they will be copied into a new report if you make a copy of that report).


### Differences
Merged results in Looker and blends in Looker Studio are **different** in the following ways:
  * Merge logic: 
    * In **Looker** , merged results require that you designate a primary query and that you specify one or more fields that have exactly matching values within the primary and other queries. There is also no limit to the number of secondary queries in a merged result.
    * In **Looker Studio** , blends combine data directly from up to five different tables within a single data source or across data sources, using a process that is similar to SQL joins. You can choose the type of join in the blend editor in the Looker Studio UI. Metrics are treated as unaggregated dimensions in the blended table, which allows for reaggregating data (for example, calculating the average of averages) in Looker Studio.
  * In **Looker** , merged results combine the results of separate queries where aggregation is typically defined within the LookML model for the Explore and therefore applied before the merge takes place. Table calculations from the source queries are displayed as standard dimensions in the merged results.
  * In **Looker Studio** , blends inherit data freshness or credentials settings directly from their underlying data sources. In Looker, you can clear the cache and retrieve fresh results from your database by using the **Clear Cache & Refresh** option.


## Report, report
Both Looker reports and Looker Studio reports are types of content that are designed to use visualizations to present information and insights that are derived from data, but each report differs in how it is managed and accessed.
**Looker term** : Report
A Looker report is a type of Looker content, akin to a dashboard, Look, or Explore, with which you can visualize and analyze data. Unlike a Looker dashboard, a report requires no underlying modeling but instead uses connectors to connect to data sources. Looker reports are organized using Looker's folder-based content management system.
**Looker Studio term** : Report
A Looker Studio report is an asset that presents information and insights that are derived from one or more data sources. Looker Studio reports are organized using Looker Studio's content management system.
### Similarities
Looker reports and Looker Studio reports are **similar** in the following ways:
  * **Creation capabilities:** Both types of reports can be created, viewed, and edited.
  * **Report structure:** Both can contain multiple pages, charts, and other components such as controls (for example, date range controls, filter controls), text areas, shapes, and images.
  * **Data handling:**
    * **Data sources:** Both types of reports derive their data from one or more data sources.
    * **Embedded data sources:** Both types of reports utilize embedded data sources.
    * **Looker connector:** Both types of reports can connect to Looker Explore data using the Looker connector.
    * **Connectors:** Both types of reports use many of the same connectors to create data sources. To see the list of connectors that are supported in Looker reports, see the Feature availability in Looker reports documentation page. To see the available Looker Studio connectors, navigate to the Connect Gallery.
    * **Connector management** : Users with administrator permissions can manage the individual data connectors that are available to create data sources.
    * **Data blending:** Both types of reports support blending data from up to five data sources.
  * **Version history:** The ability to view the version history of a report is available for both types of reports.
  * **Content Management:**
    * **Storage and organization** : Both types of reports appear in their respective environment's organizational structure and can be accessed using a search function. 
      * Looker reports live exclusively within Looker folders, with access managed through Looker 's existing content management system and permissions. Looker reports appear in folders under a **Reports** heading. They can also be found using Looker 's search functionality (requires Looker 25.4 or later).
      * Users can find and view Looker Studio reports in Looker Studio from the search bar, from a user's "Owned by me" space or "Sandbox", or from a Looker Studio Pro "Team workspace".
    * **Permissions and access:** Both types of reports operate using data credentials, which determine who can see the data that is provided by a data source. Depending on how the Looker Studio administrator has configured some data source settings, Looker Studio reports can use one of three types of data credentials: Owner's, Viewer's, or Service Account credentials. Looker reports connectors can use only Owner's or Viewer's credentials.
    * **Report management:** Both types of reports can be copied. Users with the appropriate permissions can move a report in accordance with their organizational structure. Deleting a Looker report moves it to the Looker instance's **Trash** folder. Deleting a Looker Studio report moves it to the Looker Studio **Trash** , where it can be permanently deleted.


### Differences
Looker reports and Looker Studio reports are **different** in the following ways:
  * **Content management:**
    * **Sharing reports:** Users can share both types of reports, but the ability to do so for Looker reports is managed through access to the Looker folders where the reports are stored. Users with access to a folder can access and share the reports within it at the folder level. Looker Studio reports can be shared by users who have a Looker Studio role that grants them the ability to share reports. They can be shared from within the report directly to specific users or Google Groups or shared using link-based sharing or embedding options managed from the Looker Studio interface.
    * **Report management** : Although users can perform tasks on or with both types of reports, Looker reports require users to have Looker permissions and content access and Looker Studio reports require users to have Looker Studio permissions.
  * **Data sources:**
    * Looker Studio reports support both embedded data sources, which are used in a single report, and reusable data sources, can be used across multiple reports. For more information about the difference between embedded and reusable data sources, see the About data sources documentation page.
    * Looker reports support embedded data sources only. Anyone who can edit the report can also edit the data source as well as modify the report.
  * **Gemini in Looker features:**
    * Gemini in Looker features are not available in Looker reports.
    * Looker Studio Pro users can perform some tasks with Gemini assistance in Looker Studio reports.
  * **Content recovery:**
    * Deleted Looker reports are moved to the Looker instance's **Trash** folder. For Looker instances 25.4 or later, these reports can be viewed in and restored from the Trash.
    * Deleted Looker Studio reports go to Looker Studio's own **Trash** , which has a separate mechanism for viewing, restoring, or permanently deleting content.
  * **Administrative and instance-level features:**
    * Administrative tasks for Looker reports, such as managing allowed connectors, monitoring usage through System Activity, and localization settings, are deeply integrated with the Looker instance's admin panel and settings (generally requiring Looker 25.4 or later for these report-specific admin features).
    * Looker reports must be enabled by a Looker admin on the **Reports Setup** page in the **Reports** section of the Looker instance's Admin panel.
    * Administration for Looker Studio reports, especially for Pro features, may involve the Looker Studio Enterprise admin panel or Google Cloud project configurations rather than the Looker instance admin settings.


## Parameter, parameter
Different
**Looker term** : Parameter
In Looker, a LookML parameter is a named element that consists of a key-value pair that defines specific attributes or settings for LookML objects such as models, Explores, views, dimensions, measures, and filters. The values that you specify for LookML parameters control the appearance, behavior, and interaction between LookML objects within your data model. For example, the `label` parameter defines a user-friendly name for a field when users interact with it in Looker's Explore UI, while the `sql` parameter defines the underlying SQL logic for a dimension or a measure.
In addition to these general parameters in LookML, Looker has a specific parameter called `parameter` that creates a filter-only field that can be used to filter Explores, Looks, and dashboards. This filter-only field cannot be added to a result set.
**Looker Studio term** : Parameter
Parameters in Looker Studio let you interact with user-provided data to make reports more interactive. You can also use parameters to create report templates. Parameters act like variables in a programming language. Parameters serve three primary uses:
  * You can use parameters in calculated fields to display results based on user input.
  * You can pass parameters back to the custom SQL query in a BigQuery data source.
  * You can pass parameters back to a community connector.


### Similarities
The `parameter` parameter in Looker and parameters in Looker Studio are **similar** in the following ways:
  * Both the filter-only field that is created by the `parameter` parameter in **Looker** and parameters in **Looker Studio** act like variables to make reports (in Looker Studio) and Explores, Looks, and dashboards (in Looker) more interactive.
  * Both parameters in **Looker** and parameters in **Looker Studio** can be set with default or allowed values or to accept user input.


### Differences
The `parameter` parameter in Looker and parameters in Looker Studio are **different** in the following ways:
  * Parameters in **Looker** are defined in LookML, while parameters in **Looker Studio** can be created within data sources or directly in reports, or passed to a custom SQL query in the BigQuery connector.
  * Parameters in **Looker** create a filter-only field that is used for filtering data in Explores, Looks, and dashboards. Parameters in **Looker Studio** can be used more broadly to interact with user-provided data, as to create calculated fields that include input from people using your report or to pass values back to the SQL query used by your data source.


## Table calculations, calculated fields
Similar
**Looker term** : Table calculation
Table calculations in Looker are similar to spreadsheet formulas and are performed on the results of a query, after the query has executed.
**Looker Studio term** : Calculated fields
Calculated fields let you create new metrics and dimensions that are derived from your data. Calculated fields let you extend and transform the information that flows from your data sources and see the results in reports.
There are two kinds of calculated fields:
  * Calculated fields that are created in a data source
  * Calculated fields that are created in specific charts of a report


### Similarities
Table calculations in Looker and calculated fields in Looker Studio are **similar** in the following way:
  * Both table calculations in **Looker** and calculated fields in **Looker Studio** let users create ad hoc metrics that are based on existing data.


### Differences
Table calculations in Looker and calculated fields in Looker Studio are **different** in the following ways:
  * Table calculations in **Looker** operate on the _results_ of a query, not on the underlying database. Calculated fields in **Looker Studio** operate directly on the data fields that are available in the data source.
  * Table calculations in **Looker** are created directly within an Explore after the query has run. Calculated fields in **Looker Studio** can be created within the data source (making the field available to all reports that use that data source) or directly within a specific chart.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


