# Looker–Power BI Connector  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/powerbi-connector

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Setting up Power BI Desktop to connect to Looker
    * Enable the connector on your Looker instance
    * Download and save the connector file
    * Setting up Power BI Desktop for a custom connector
  * Connecting to Looker data from Power BI Desktop
  * Viewing Looker elements in Power BI Desktop
  * Creating queries with Looker dimensions and measures
  * Filtering queries with Looker filters and parameters
  * Monitoring the Looker–Power BI Connector
  * Power BI service
    * Publishing a report with Power BI service using row-level security
  * Things to consider
    * Query row limits
    * Supported dimension group timeframes
    * Known limitations
  * Looker–Power BI Connector changelog




Was this helpful?
Send feedback 
#  Looker–Power BI Connector
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Setting up Power BI Desktop to connect to Looker
    * Enable the connector on your Looker instance
    * Download and save the connector file
    * Setting up Power BI Desktop for a custom connector
  * Connecting to Looker data from Power BI Desktop
  * Viewing Looker elements in Power BI Desktop
  * Creating queries with Looker dimensions and measures
  * Filtering queries with Looker filters and parameters
  * Monitoring the Looker–Power BI Connector
  * Power BI service
    * Publishing a report with Power BI service using row-level security
  * Things to consider
    * Query row limits
    * Supported dimension group timeframes
    * Known limitations
  * Looker–Power BI Connector changelog


The Looker–Power BI Connector lets you use Microsoft Power BI Desktop to connect to data from a Looker Explore.
## Setting up Power BI Desktop to connect to Looker
The general steps to use the Looker–Power BI Connector are as follows:
  1. Verify the requirements.
  2. Enable the connector on your Looker instance.
  3. Download and save the connector file: Each user who wants to access the Looker–Power BI Connector must download the `looker_1.4.2.mez` file and save it in a specific directory on their computer.
  4. Set up Power BI Desktop for a custom connector: Each Power BI user must configure their Power BI Desktop security settings to use a non-certified custom connector.


The sections on this page describe these steps in detail.
After you complete the steps to connect Looker with Power BI Desktop, you can connect to Looker data from Power BI and publish reports in Power BI. You can optionally use Power BI service (Power BI online) to interact with your Looker reports in a web browser. You can also publish reports with Power BI service using row-level security.
### Requirements
To set up the Looker–Power BI Connector, you need the following:
  * Microsoft Power BI Desktop installed on your computer.
  * A Looker instance that meets the following requirements: 
    * The instance must be hosted by Looker. (Looker (Google Cloud core) instances are hosted by Looker and support the Looker–Power BI Connector.)
    * The instance must be running Looker 23.10 or later.
  * A Looker user account on the Looker instance with the `explore` permission, which is required to access Explores in Looker. If you want to work with queries with more than 5,000 rows, you also need the `download_without_limit` permission (see Query row limits for information on downloading limits).


### Enable the connector on your Looker instance
The Looker instance you want to use with the Looker–Power BI Connector must be enabled for the **Microsoft Power BI** connector:
  * For Looker (Google Cloud core) instances, BI connectors are enabled by default.
  * For Looker (original) instances, BI connectors are disabled by default.


Your Looker admin can enable BI connectors on the BI Connectors panel in the **Platform** section of the Looker **Admin** menu.
### Download and save the connector file
To download the connector file, follow these steps on the computer with Microsoft Power BI Desktop installed:
  1. To download the connector file, click the following link: `looker_1.4.2.mez`
  2. When the download is completed, move the `looker_1.4.2.mez` file to the directory **[Documents]\Microsoft Power BI Desktop\Custom Connectors**. (Create the folders on your computer if they don't already exist.)


### Setting up Power BI Desktop for a custom connector
To set up the Looker–Power BI Connector on the Power BI Desktop side, follow the Custom connectors instructions on the Microsoft Power BI website.
As it says in the instructions, under **Data Extensions** , you will select the option **(Not Recommended) Allow any extension to load without validation or warning**. Select **OK** , and then restart the Power BI Desktop.
## Connecting to Looker data from Power BI Desktop
Once you have downloaded the `looker_1.4.2.mez` connector file and set up your Power BI Desktop application for a custom connector, you can use Power BI Desktop to connect to data from your Looker instance:
  1. From the Power BI Desktop toolbar, select **Get Data > More...**
  2. In the **Get Data** dialog, enter **Looker** in the search field.
  3. In the search results, click the **Looker** entry, and then click **Connect**.
  4. In the **Connecting to a third-party service** dialog, click **Continue**.
  5. Power BI Desktop will display a Looker sign-in dialog. In the **Host** field, type in the URL of your instance. For example: `example.cloud.looker.com`.
  6. Optionally, click **Advanced Options** to expand the section and use the **Show Hidden Fields** drop-down to include fields that are configured in LookML as hidden:
     * **FALSE** (default): Hidden fields are suppressed.
     * **TRUE** : Hidden fields are shown.
  7. Select the **DirectQuery** option to create a live connection to your data on Looker.
  8. Click **OK**.
  9. In the **Looker** dialog, click **Sign in**.
  10. In the Looker login screen, sign in to your Looker instance.
  11. Power BI Desktop will return to the Looker sign-in dialog, with a message that says that you are signed in. Click **Connect**.
  12. Power BI Desktop will display a list of the Looker models that you have access to, each represented as a folder. Click the Looker model that you want to access, and then select the checkbox next to the Looker Explore that you want to load in Power BI Desktop. To see a model, you must have Looker user access or group access to a model set that contains the model. To access Explores, you must have the Looker `explore` permission.
  13. Click **Load**.


Power BI Desktop will populate its **Data** pane with the fields from your selected Explore. You can then use the Looker data from the Explore to create reports in Power BI Desktop. See Viewing Looker elements in Power BI Desktop for information on how Looker elements are displayed by the Looker–Power BI Connector.
Field names will appear in a single list in the format `ViewName.FieldName`.
## Viewing Looker elements in Power BI Desktop
After you connect to Looker data from Power BI Desktop, Power BI Desktop will populate its **Data** pane with the fields from your selected Explore.
The Looker–Power BI Connector uses the following format to display Looker fields in Power BI Desktop:
`ViewName.FieldType.FieldName`
  * The `ViewName` value is the LookML view where the field is defined.
  * The `FieldType` value can be one of the following types that are supported by the Looker–Power BI Connector:
    * `dim`: Dimension, a field that represents an attribute, a fact, or a value, such as dates, names, and IDs. Dimensions often correspond to columns in your underlying data table. In LookML, dimensions are defined with the `dimension` parameter.
    * `mea`: Measure, a field that represents measurable information about your data, such as sums, counts, averages, minimums, and maximums. In LookML, measures are defined with the `measure` parameter.
    * `fil`: Filter, a filter-only field that is used only to create a filter in an Explore query; filter fields are not included in a query's result set. In LookML, filters are defined with the `filter` parameter.
    * `par`: Parameter, a field that is used only to create a filter in an Explore query; parameter fields are not included in a query's result set. A parameter can create interactive query results, labels, URLs, and more when it is defined with the `{% parameter parameter_name %}` and `parameter_name._parameter_value` Liquid variables. In LookML, parameters are defined with the `parameter` parameter.
  * The `FieldName` value is the name of the field as it is displayed in the Looker Explore.


Power BI Desktop displays Looker elements just as they are displayed in the Looker Explore, with the same capitalization and word spacing. For example, if a Looker Explore displays a LookML dimension as `Created Date` from a view displayed as `Order Items`, Power BI Desktop will display this field as `Order Items.dim.Created Date`.
## Creating queries with Looker dimensions and measures
The Looker–Power BI Connector lets you use Looker dimensions and measures to create queries in Power BI Desktop.
To create a query in Power BI Desktop using Looker dimensions and measures, follow these steps:
  1. Connect to Looker data from Power BI Desktop, and wait for Power BI to populate its **Data** pane with the fields from your selected Looker Explore.
  2. In the Power BI **Data** pane, select the checkbox for each Looker dimension or measure that you want to include in the query.


As you select each dimension or measure, Power BI will update the query that is displayed in the report canvas.
## Filtering queries with Looker filters and parameters
The Looker–Power BI Connector lets you use LookML parameters and filter-only fields from a Looker Explore to add filters to your Power BI report.
To filter a report in Power BI Desktop using Looker parameters and filter-only fields, follow these steps:
  1. If you haven't already, connect to Looker data from Power BI Desktop and wait for Power BI to populate its **Data** pane with the fields from your selected Looker Explore.
  2. In the Power BI **Data** pane, drag the name of a parameter or a filter-only field into one of the **Add data fields here** boxes in **Filters** pane, either for **Filters on this page** or for **Filters on all pages**. See the Power BI documentation for details on adding filters to a report in Power BI.


Note the following about using Looker parameters and filter-only fields in Power BI:
  * For filter-only fields that are configured in LookML with the `suggestions` parameter or the `suggest_dimension` parameter, Power BI will fetch the suggestion values and display them in the **Basic filtering** options in the **Filters** pane.
  * For parameters that are configured in LookML with the `allowed_value` attribute, Power BI will fetch all of the allowed values that are configured in LookML for the parameter and display them in the **Basic filtering** options in the **Filters** pane.


## Monitoring the Looker–Power BI Connector
A Looker admin can view Looker–Power BI Connector usage using the **Query API Client Properties** group of fields in the System Activity History Explore. An entry is created in the **History** Explore every time a new query is run.
In the **Query API Client Properties** group of fields, the **API Client Name** shows a `Power BI` value to identify Looker–Power BI Connector entries.
The following is an example of a System Activity URL that shows Power BI usage. Replace `<instance_name.looker.com>` with your instance URL.
```
https://<instance_name.looker.com>/explore/system__activity/history?fields=query_api_client_context.name,user.name,history.created_date,history.created_time_of_day&f[query_api_client_context.name]=Power+BI&sorts=history.created_time_of_day+desc&limit=5000

```

## Power BI service
After you connect to Looker data from Power BI and publish reports in Power BI, you can optionally use Power BI service (Power BI online) to interact with your Looker reports in a web browser.
You can also publish reports with Power BI service using row-level security.
### Publishing a report with Power BI service using row-level security
After you have published reports in Power BI Desktop using the Looker–Power BI Connector, you can optionally use Power BI service to interact with the reports from a web browser.
Power BI Desktop lets you use row-level security (RLS) to restrict data access for certain users. See the Power BI documentation for the procedures for defining roles and rules and validating the roles within Power BI Desktop.
Once you define the roles in Power BI Desktop, you can use the roles and rules online with Power BI service.
To publish a report with Power BI service using row-level security, follow these steps:
  1. In Power BI Desktop, open your report and select the **Home** menu from the top of the window.
  2. Select the **Publish** option from the **Home** menu.
  3. Select a workspace from the drop-down menu, and then click **Select**. Power BI Desktop shows a success message that includes a link to open the report in Power BI.
  4. Click the link to open Power BI.
  5. In Power BI service, go to **Workspaces** and select the workspace where you published the report.
  6. Find the listing for your report's dataset (not the report itself).
  7. In the dataset's listing, click the three-dot **More options** menu, and then select **Security**.


Power BI will show the **Row-Level Security** window. From here, you can select the role that you created in Power BI Desktop and add people or groups who belong to the role and validate your roles in Power BI service.
Now you can share the report with anyone you want, and they will see only the data that they are allowed to see, based on the roles that you created.
## Things to consider
### Query row limits
Queries from the Looker–Power BI Connector will automatically include a `LIMIT 5000` statement unless the Looker user account has the `download_without_limit` permission. If the Looker user account has `download_without_limit`, queries from the Looker–Power BI Connector have no imposed query row limit.
### Explore filters
If the Looker Explore is defined with `always_filter` or `conditionally_filter` LookML parameters, the filters will be applied to queries in the Looker–Power BI Connector, even though the filters won't be visible in Power BI.
### Supported dimension group timeframes
For the `dimension_group` of `type: time`, only the `date` and `time` timeframes are supported with the Looker–Power BI Connector. Other timeframes will be hidden.
### Known limitations
The following are known limitations with the Looker–Power BI Connector:
  * Numeric dimensions and measures both render as measures (see Dimension and measure fields for a description of dimensions and measures). To use a numeric dimension as a dimension, you must first change it to **Not Summarized** in Power BI Desktop.
  * To ensure optimal performance and functionality, use DirectQuery Mode whenever possible. When using the Power BI Import Mode with the Looker–Power BI Connector, be aware of the following limitations: 
    * Import Mode reports that attempt to access larger models may experience performance degradation.
    * If the Get Data process does not resolve or times out, switch to DirectQuery Mode to improve performance and reliability.
    * Don't use filter-only fields and parameter fields if you are using Import Mode, since these fields are disabled in Import Mode.
    * Import Mode does not allow Looker to correctly evaluate measures within the Explore. This limitation can impact the accuracy and functionality of your reports.
  * Power BI attempts to apply its own aggregations on Looker measures, this sometimes will lead to inconsistent results (especially if you are using matrix visuals) or lead to aggregations not working due to a lack of equivalent mapping. 
    * Use only the following supported measures types in your Power BI reports: `average`, `count`, `count-distinct`, `max`, `min`, `sum`.
    * Querying for standard deviation and variance is not supported.
    * Querying for the first or last string alphabetically using the Power BI first/last aggregators is not supported.
    * In Power BI, the query for median is performed by pulling all values in the dataset and then calculating the median locally. This can be very slow on larger datasets and may time out.
  * Because of the inconsistencies with Power Query and Looker filter expressions, be aware of the following advanced filters limitations: 
    * All text filters are supported.
    * Multiple text filters are not supported.
    * All number filters are supported.
    * Multiple number filters are supported only in the following cases: 
      * INEQUALITY AND INEQUALITY (for example, is less than AND is greater than).
      * INEQUALITY OR INEQUALITY (for example, is less than OR is greater than).
      * is OR is.
    * Only the following date/datetime filters are supported: `is`, `is not`, `is on or after`, `is before`.
    * Multiple date and datetimefilters are supported only in the following cases: 
      * `is on or after AND is before`
      * `is or is`
    * The following table functions are not foldable: 
      * `Table.Distinct`
      * `Table.Join`
      * `Table.NestedJoin`
      * `Table.Skip`


## Looker–Power BI Connector changelog
The following sections show the updates in each version of the Looker–Power BI Connector:
  * Version 1.4.2
  * Version 1.4.0
  * Version 1.3.1
  * Version 1.3.0
  * Version 1.2.0


### Version 1.4.2
Version 1.4.2 of the Looker–Power BI Connector has the following updates:
  * The **Disable Preview Optimization** connection setting has been removed.
  * The **Show Hidden Fields** connection option has moved under the **Advanced Options** section.
  * The Beta flag has been removed; the connector no longer appears as beta in Power BI.


Version 1.4.2 of the Looker–Power BI Connector has the following bug fixes:
  * Fixed the regression error where Boolean slicers and date slicers failed in Power BI.
  * Fixed `is-not` filter not working for `dates` filter.


### Version 1.4.0
Click to expand section
Version 1.4.0 of the Looker–Power BI Connector has the following updates:
  * Added support for Import Mode
  * Enabled data preview
  * Improved behavior when performing `SELECT *` queries
  * Improved Looker cache hit rate
  * Improved performance of filter suggestions retrieval


Version 1.4.0 of the Looker–Power BI Connector has the following bug fixes:
  * Fixed bug where Looker wouldn't detect that values had been passed for filter and parameter fields
  * Fixed bug where parameter suggested values would sometimes be missing from slicers
  * Fixed bug where Liquid variables would be ignored by LookML statements
  * Fixed bug where count distinct measure values would be inconsistent in Power BI matrix views


### Version 1.3.1
Click to expand section
Version 1.3.1 of the Looker–Power BI Connector has the following updates:
  * Added option to show hidden fields


Version 1.3.1 of the Looker–Power BI Connector has the following bug fix:
  * Fixed bug where a visual would fail if a filter exists on both the visual and report


### Version 1.3.0
Click to expand section
Version 1.3.0 of the Looker–Power BI Connector has the following updates:
  * Simplified datetime formatting
  * Improved detection on unsupported text expressions
  * Improved error message reporting


Version 1.3.0 of the Looker–Power BI Connector has the following bug fix:
  * Improved support for escape characters in filter values


### Version 1.2.0
Click to expand section
Version 1.2.0 of the Looker–Power BI Connector has the following updates:
  * Parameter and filter-only fields are now supported
  * Advanced filters support for filter-only fields of type text, number, date and datetime
  * Basic filter support for filter-only field utilizing Looker suggested values


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


