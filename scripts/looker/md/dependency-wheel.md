# Creating a dependency wheel chart with the Chart Config Editor  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/dependency-wheel

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Prerequisites
    * Writing the JSON snippet
  * Creating a dependency wheel chart
  * Limitations and requirements




Was this helpful?
Send feedback 
#  Creating a dependency wheel chart with the Chart Config Editor
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Prerequisites
    * Writing the JSON snippet
  * Creating a dependency wheel chart
  * Limitations and requirements


A dependency wheel chart is similar to a Sankey chart, but a dependency wheel displays flow between states around a circle rather than in a linear direction. In Looker, each dimension value is represented as a state, and the size of the flow is determined by a numeric measure value.
Using the Chart Config Editor, you can create dependency wheel charts by starting from a column chart in Looker. 
Dependency wheel charts require at least two dimensions and exactly one measure.
For example, you can create a dependency wheel chart that shows the **Order Item Count** measure values over several **Seasonal Collection** dimension values, which flow into **Category** dimension values. Each dimension value is represented by a color-coded arc on the outside of the circle. The width of a line connecting two arcs corresponds to the values of the **Order Item Count** measure for that dimension pair. The higher the value, the wider the line. 
## Prerequisites
To access the Chart Config Editor, you must have the `can_override_vis_config` permission.
### Writing the JSON snippet
To create a dependency wheel chart, start from the following JSON snippet:
```
{
chart:{
type:'dependencywheel'
}
}

```

## Creating a dependency wheel chart
To create a dependency wheel chart, follow these steps:
  1. View a column chart in an Explore, or edit a column chart in a Look or dashboard.
Start from a column chart with at least two dimensions and exactly one measure. Your starting chart might look something like this example:
  2. Open the **Edit** menu in the visualization.
  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.
  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.
  5. To let Looker properly format your JSON, click **< > (Format code)**.
  6. To test your changes, click **Preview**.
  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.


Once you've customized your visualization, you can save it.
## Limitations and requirements
When you're using dependency wheel charts, keep the following limitations and requirements in mind:
  * Dependency wheel charts require at least two dimensions and exactly one measure.
  * Dependency wheel charts can display a maximum of 50 rows of data.
  * Dependency wheel charts don't support pivoted dimensions.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


