# Creating a treemap chart with the Chart Config Editor  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/treemap

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Prerequisites
    * Writing the JSON snippet
    * Creating a treemap chart




Was this helpful?
Send feedback 
#  Creating a treemap chart with the Chart Config Editor
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Prerequisites
    * Writing the JSON snippet
    * Creating a treemap chart


A treemap chart displays categorical and hierarchical data as a set of rectangles, where the size of each rectangle is determined by a numeric measure.
Using the Chart Config Editor, you can create treemap charts by starting from a column chart in Looker. For best results, use a pivoted dimension, an unpivoted dimension, and a measure to create a treemap chart.
For example, you can create a treemap chart that shows the **Order Item Count** over several different **Category** values, pivoted by **Seasonal Collection**. Each season is represented by a color-coded rectangle, which contains smaller rectangles that represent the category. The size of each rectangle corresponds to the **Order Item Count** .
## Prerequisites
To access the Chart Config Editor, you must have the `can_override_vis_config` permission.
### Writing the JSON snippet
To create a treemap chart, start from the following JSON snippet:
```
{
chart:{
type:'treemap',
}
}

```

### Creating a treemap chart
To create a treemap chart, follow these steps:
  1. View a column chart in an Explore, or edit a column chart in a Look or dashboard.
For this example, we recommend starting from a column chart with two dimensions and one measure. One dimension should be pivoted. The pivoted values define the top level categories used to render the treemap. Your starting chart might look something like this example:
  2. Open the **Edit** menu in the visualization.
  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.
  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.
  5. To let Looker properly format your JSON, click **< > (Format code)**.
  6. To test your changes, click **Preview**.
  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.


Once you've customized your visualization, you can save it.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


