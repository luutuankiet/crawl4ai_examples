# Creating a Sankey chart with the Chart Config Editor  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sankey

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Prerequisites
    * Writing the JSON snippet
  * Creating a Sankey chart
  * Limitations and requirements




Was this helpful?
Send feedback 
#  Creating a Sankey chart with the Chart Config Editor
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Prerequisites
    * Writing the JSON snippet
  * Creating a Sankey chart
  * Limitations and requirements


A Sankey chart emphasizes flow from one state to another. In Looker, each dimension value is represented as a state, and the size of the flow is determined by a numeric measure value.
Using the Chart Config Editor, you can create Sankey charts by starting from a column chart in Looker. For best results, use at least two dimensions and exactly one measure to create a Sankey chart.
For example, you can create a Sankey chart that shows the **Order Item Count** measure values over several **Seasonal Collection** dimension values, which flow into **Category** dimension values. Each dimension value is represented by a color-coded rectangle. The width of each line where it meets each rectangle corresponds to the value of the **Order Item Count** measure for that dimension. 
## Prerequisites
To access the Chart Config Editor, you must have the `can_override_vis_config` permission.
### Writing the JSON snippet
To create a Sankey chart, start from the following JSON snippet:
```
{
chart:{
type:'sankey'
}
}

```

## Creating a Sankey chart
To create a Sankey chart, follow these steps:
  1. View a column chart in an Explore, or edit a column chart in a Look or dashboard.
For this example, we recommend starting from a column chart with two dimensions and one measure. Your starting chart might look something like this example:
  2. Open the **Edit** menu in the visualization.
  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.
  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.
  5. To let Looker properly format your JSON, click **< > (Format code)**.
  6. To test your changes, click **Preview**.
  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.


Once you've customized your visualization, you can save it.
## Limitations and requirements
  * Sankey charts require at least two dimensions and exactly one measure.
  * Sankey charts can display a maximum of 50 rows of data.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


