# Treemap reference  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/treemap-reference

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Treemaps in Looker Studio
  * Treemap examples
  * Set up the chart data
    * Date range dimension
    * Default date range filter
    * Chart interactions
  * Style the chart
    * Background and border
    * Reset to report theme
  * Related resources




Was this helpful?
Send feedback 
#  Treemap reference
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Treemaps in Looker Studio
  * Treemap examples
  * Set up the chart data
    * Date range dimension
    * Default date range filter
    * Chart interactions
  * Style the chart
    * Background and border
    * Reset to report theme
  * Related resources


A treemap shows your data organized into dimension hierarchies. For example, you can use a treemap to show the average annual sales of each item in a product category > subcategory > product hierarchy.
## Treemaps in Looker Studio
Data in a treemap is displayed in "branches" (also called "nodes"). Each branch can have zero or more sub-branches, and one parent branch (except for the root, which has no parents). Each branch is displayed as a rectangle, sized and colored according to the values in your data. Sizes and colors are valued relative to all other branches in the graph.
Treemaps are a good hypothesis-generation tool because they can help expose the relative importance of, and the relationship between, different entities.
## Treemap examples
The following treemap displays the number of items sold by an online pet store. The branch labels come from the **Department** and **Item** dimensions.
Here's how the underlying data for this chart is organized:
## Add the chart
Add a new chart or select an existing chart. Then, use the **Properties** panel to configure the chart's **Setup** tab and **Style** tab properties to set up the chart data and style the chart, respectively.
## Set up the chart data
The options in the **Setup** tab of the **Properties** panel determine how the chart's data is organized and displayed.
### Data source
A data source provides the connection between the component and the underlying dataset.
  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the **Edit data source** icon. (You must have at least Viewer permission to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. Learn more about data blending.


### Dimension
Dimensions are data categories. Dimension values (the data that is contained by the dimension) are names, descriptions, or other characteristics of a category.
#### Drill down
This option appears on charts that support it.
Drilling down gives viewers a way to reveal additional levels of detail within a chart. When you turn on the **Drill down** switch, each dimension that you add becomes another level of detail that you can drill into. Learn more about chart drill down.
#### Levels to show
The **Levels to show** option determines the granularity of the chart. For example, the sample chart in the Treemap examples section on this page has **Levels to show** set to **2** , causing it to show two levels of detail (**Department** and **Item**).
Setting **Levels to show** to **1** causes the chart to display only one level of detail (**Department**):
> **What's the difference between drill down and levels to show?**
> **Drill down** lets you focus on a specific level of detail, while **Levels to show** controls how many levels of detail appear in the treemap. For example, here's the result of drilling down into a chart. Note that it now displays only one level of detail, but that level is now the **Item** dimension level.
> See an example of a treemap with drill down turned on (the report is in English only).
### Metric
This option displays the metric data broken down according to the selected dimension. For example, a chart that shows annual sales data could be broken down by a **Sales Region** dimension to show sales by region or by an **Employee ID** dimension to show sales by sales associate.
#### Optional metrics
You can add optional metrics by turning on the **Optional metrics** switch and selecting metrics from the **Add metric** field selector. You can also click metrics from the fields list on the **Data** panel and place them in the **Optional metrics** selector.
#### Metric sliders
Turn on the **Metric sliders** switch to add a metric slider to your chart.
### Filter
Filters restrict the data that is displayed in the component by including or excluding the values that you specify. Learn more about the filter property.
Filter options include the following:
  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.


### Date range dimension
This option appears if your data source has a valid date dimension.
The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.
### Default date range filter
The default date range filter lets you set a timeframe for an individual chart.
Default date range filter options include the following:
  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.


Learn more about working with dates and time.
### Total rows
Treemaps can display from 5 to 5,000 rows of data.
#### Group others
Turn on the **Group others** switch to aggregate the results that are outside of the specified **Number of series** limit into a series that will have the label **Others**. When enabled, **Group others** lets you compare other series against the context of the remaining results.
### Chart interactions
When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. Learn more about cross-filtering.
## Style the chart
The options in the **Style** tab control the overall presentation and appearance of the chart.
### Chart title
Turn on the **Show title** switch to add a title to your chart. Looker Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.
#### Autogenerate
This option is enabled by default. When **Autogenerate** is enabled, Looker Studio generates a title that is based on the chart type and the fields that are used in the chart. The autogenerated title will be updated if you change the chart type or make changes to the fields that are used in the chart.
To add a custom title to your chart, enter it into the **Title** field. This will turn off the **Autogenerate** setting.
#### Title options
When the **Show title** setting is enabled, you can use the following title options:
  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left:** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title above or below the chart.
  * **Right:** Aligns the chart title to the right side of the chart.


### Treemap
These options control the appearance of the treemap:
  * **Max color value:** Sets the color for the highest metric value.
  * **Mid color value:** Sets the color for the median metric value.
  * **Min color value:** Sets the color for the minimum metric value.
  * **Show branch header:** Shows or hides the parent branches.
  * **Branch header color:** Sets the color of the branch header. This setting appears when **Show branch header** is enabled.
  * **Show scale:** Shows or hides the chart scale above the treemap.


### Text
Set the font style, font size, font color, and value format for the text in the chart.
### Background and border
These options control the appearance of the chart background container:
  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.


### Chart header
The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:
  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.


### Reset to report theme
Click **Reset to report theme** to reset the chart settings to the report theme settings.
## Related resources
  * Types of charts in Looker Studio
  * About filter properties


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


