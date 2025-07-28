# About filter properties  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/about-filter-properties

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How filters work
    * What you can filter
  * Filters and data sources
  * Filter inheritance
  * Multiple filters on a component
  * Limitations of filters
  * Related resources




Was this helpful?
Send feedback 
#  About filter properties
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How filters work
    * What you can filter
  * Filters and data sources
  * Filter inheritance
  * Multiple filters on a component
  * Limitations of filters
  * Related resources


_Filter properties_ (or _filters_ , for short) refine or reduce the data that is shown to report viewers. As a report editor, filter properties let you focus on the data that best communicates the story that you want to tell, making your reports more relevant to your audience.
You can apply a filter to a chart, control, page, or the entire report using the **Data** tab. Filter properties are sometimes referred to as _editor filters_ , because report viewers can't change them. Filter properties can be changed only by report editors.
> Learn how to add filter controls, which can be used by report viewers.
## How filters work
There are two types of filters:
  * **Include filters** retrieve only the records that _match_ the conditions.
  * **Exclude filters** retrieve only the records that _don't_ _match_ the conditions.


Note that filters do not transform your data in any way. They simply reduce the amount of data that is displayed in the report.
Filter conditions consist of one or more _clauses_. Multiple clauses can be joined with "OR" logic (true if any conditions are met), "AND" logic (true if all conditions are met), or both.
You can apply filters to dimensions or metrics, or both.
When defining filters on charts, pages, or reports that use **Equal to (=)** or **In** conditions, report editors can select from a list of possible filter values that are provided from the underlying data. To see filter value suggestions, enable **Show suggested values while typing** in the filter editor. Filter suggestions are supported for all data connectors.
### What you can filter
You can apply filters to the following components:
  * **Charts**. For example, you can display a pie chart of new versus returning users in your biggest markets with a filter that includes _Country_ **IN** " `United States,Canada,Mexico,Japan` ".
  * **Filter controls**. For example, you can let your viewers select from a list of best selling products on `Quantity Sold Greater than (>) 100`.
  * **Groups**. For example, you can group two sets of charts and filter on **Device Category** to show website traffic in one set, and on the other to show mobile traffic.
  * **Pages**. Page-level filters apply to every chart on that page. For example, you can dedicate page 1 of your Google Analytics report to mobile app traffic, and page 2 to desktop traffic by filtering on the **Device Category** dimension.
  * **Reports**. Every chart in the report is subject to the filter. For example, you can create a report that focuses on your best customers by setting the report-level filter property to `Lifetime Value Greater than or equal to 10,000`.


## Filters and data sources
Just like charts, filter properties are associated with a data source. If you create the filter by adding it to a component, that data source is the one in use by the component. If you create the filter using the filter manager, you can select any of the data sources currently added to the report.
> Reusing a filter on a component that uses a different data source can render the filter invalid. That's because the dimensions and/or metrics used by the filter may not exist in the new data source.
> The same thing can happen if you copy a chart or control to a report that uses a different data source, or if you simply change the data source in use by a filter by editing it in the filter manager.
> Invalid filters display an error on the chart or control, and a warning icon on the filter. You can fix this by editing the filter and selecting new dimensions or metrics, or by deleting the filter.
## Filter inheritance
Filters can be _inherited_ , which means that filters on higher-level components apply to the components beneath them. The order of inheritance is as follows:
**Report level > page level > chart/control level**
For a lower-level ( _child_ ) component to inherit filters from a higher-level ( _parent_ ) component, the dimensions and metrics that are used in the parent's filters must exist in the child component's data source. If they don't, then inheritance is turned off for the child component.
You can explicitly turn off inheritance by using the toggle in the **Filter** section of the **Setup** panel for a selected component. For example, you can tell a chart not to inherit a page level filter property, or you can tell a page not to inherit the report-level property.
## Multiple filters on a component
A component can have multiple filters. When this is the case, each filter is treated like an AND clause. This means that only the data rows that meet all the conditions in the filter are affected.
When viewing a report, you can view the filters that are applied to the current page or to individual components. To view applied filters, follow these steps:
  1. If you are editing the report, switch to viewing the report.
  2. Open the **Applied filters** panel using one of the following methods: 
     * Click the three dot menu on a report and then select **View applied filters.**
     * Click the **View applied filters button** at the top of a chart.
  3. By default, the **Applied filters** panel shows the filters that are applied to the current page. To see filters for another page or for individual components, click the context selector and select a page or component.
  4. By default, the **Active controls** section displays all the filters for which you can edit the values. To edit a filter value, click on the filter in the report.
  5. If a report editor has enabled viewing advanced applied filters for a report, you can also see filters whose values you cannot edit. Click **Advanced View** to display any applied report and model filters, page filters, group filters, and chart filters.


## Limitations of filters
  * Report-level filters only apply to components that use the default data source. If you include charts that use a different data source, you'll need to create a chart-level filter for that chart.
  * A single component can have a maximum of 75 filter clauses.
  * A single filter can have a maximum of 10 OR clauses. If you need more OR clauses, consider changing the comparison operator to **In**.
  * Because of the way metrics and dimensions are aggregated, they cannot be mixed in an OR clause.
  * If you change a field in a data source from a metric to dimension or from a dimension to a metric, any filters that use that field are disabled.


## Related resources
  * Regular expressions in Looker Studio
  * google / RE2 / Syntax


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


