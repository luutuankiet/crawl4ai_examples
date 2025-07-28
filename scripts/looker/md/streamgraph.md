# Creating a streamgraph chart with the Chart Config Editor  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/streamgraph

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Prerequisites
    * Writing the JSON snippet
    * Creating a streamgraph chart




Was this helpful?
Send feedback 
#  Creating a streamgraph chart with the Chart Config Editor
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Prerequisites
    * Writing the JSON snippet
    * Creating a streamgraph chart


A streamgraph chart is a type of stacked area chart that is useful for displaying compound volume across different categories or over time.
Using the Chart Config Editor, you can create streamgraph charts by starting from an area chart in Looker. Streamgraph charts require two dimensions and one measure.
For example, the following streamgraph chart shows the **Total Sale Price** over several different **Category** values, plotted over **Order Created Month**. Categories are stacked on top of one another to show how much each category contributes to the total, as well as how the total changes over time.
## Prerequisites
To access the Chart Config Editor, you must have the `can_override_vis_config` permission.
### Writing the JSON snippet
To create a streamgraph chart, start from the following JSON snippet:
```
{
chart:{
type:'streamgraph',
}
}

```

### Creating a streamgraph chart
To create a streamgraph chart, follow these steps:
  1. View an area chart in an Explore, or edit an area chart in a Look or dashboard.
For this example, we recommend starting from an area chart with two dimensions and one measure. One dimension should be pivoted. Your starting chart might look something like this example:
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


