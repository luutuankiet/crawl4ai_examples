# About controls  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/about-controls

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  About controls
Stay organized with collections  Save and categorize content based on your preferences. 
Controls let you interact with the data in the following ways:
  * Filter the data by specific dimension values.
  * Set the timeframe of the report.
  * Set parameter values that can then be used in calculated fields or passed back to the connector.
  * Change the underlying dataset used by a data source.


## Add a control to the report
  1. Edit your report.
  2. In the toolbar, select **Add a control**.
  3. Select the control type, and then position it on your chart.
  4. On the right, configure the chart with the settings in the **Properties** panel. 
    1. To filter the report by selected dimension values, use a dimension for the **Control field**.
    2. To set the value of a parameter, use that parameter as the **Control field**.
    3. To change the appearance of the data control, use the options in the **Style** tab of the properties panel.


## How controls work
Controls serve two main purposes:
  * Controls let you filter or change the data displayed in the report's components.
  * Controls provide a way to gather user input and use it in calculated fields and in connectors that support parameters, such as BigQuery and community connectors.


### Controls as filters
When a control is based on a dimension (you add a dimension from the **Data** panel as the **Control field** ), the control acts as a filter on the data.
For example, a list control based on a Country dimension lets you filter the data by country. An advanced filter based on a Product SKU dimension lets you filter by all or partial product identifiers.
#### More about controls as filters
Controls filter all components on the page based on the same data source as the control itself, or that have matching field IDs. Controls can also filter components if the data sources are different, but are based on the same fixed schema connector, such as Google Ads and Google Analytics, because the internal field IDs are identical between data sources created by those connectors.
Controls can filter other controls. For example, say you have one filter on a Country dimension, and a second filter on a Campaign dimension. Filtering on **Country = France** causes the filter on the Campaign dimension to only show the campaigns that ran in France. Similarly, filtering on **Campaign "ABC"** restricts the filter on the Country dimension to only show the countries where that campaign ran.
Controls can only filter by a single dimension. To create a control that filters by more than one dimension, you have several options:
  * Create multiple filter controls, one for each dimension you want to filter by.
  * Concatenate the dimension data you want to filter by in a calculated field in the data source.
  * Concatenate the dimension data you want to filter by in the underlying data, if possible.


To filter by metric values, you can add a metric slider to individual charts.
### Controls as input
When a control is based on a parameter (you add a parameter from the **Data** panel as the **Control field** ), the control provides input to that parameter. Parameters are like variables that get their value from the an interaction with the report (say, by typing in a value directly, or picking a value from a predefined list).
You can use parameters to make calculated fields more dynamic. For example, you could create a _Sales Target_ parameter and use it as the control field for an Input box to let people enter different sales goal numbers to visualize projected performance. You could then apply conditional formatting rules that highlight the results in eye-catching ways.
You can also pass parameters back to the underlying SQL query used to create a BigQuery data source, or to data sources created using community connectors.
Learn more about parameters.
## Types of controls
The **Add a control** menu is divided into two sections.
The controls in the first section can be used to filter data or to set parameter values, and they include the following options:


The controls in the second section perform specialized functions and can't be used to set parameter values. The second section includes the following options:
  * Date range control
  * Dimension control


> ## A note on case-sensitivity
> In general, the search operators for text dimensions are case-sensitive. However, this can vary by connector, so it's a good idea to test this on your data and provide guidance to your report viewers.
> To create a case-insensitive regular expression, you can prepend it with `(?i)`. Learn more about Regular expressions in Looker Studio.
## Change the control type
You can switch an existing control on the report from one type to another:
  1. Edit your report.
  2. Select the control.
  3. On the right, at the top of the **Properties** panel, open the control drawer .
  4. Select the new control type.


You may need to edit the control's settings to use the new type.
## Make a control appear on every page
You can make a control appear in the same location on every page of your report. Filters or parameters set on one page will carry over to all the pages in the report.
  1. Edit your report.
  2. Select the control.
  3. Select the **Arrange > Make Report-level** menu.


## Related resources
  * About parameters


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


