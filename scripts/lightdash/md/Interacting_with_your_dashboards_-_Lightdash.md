# Interacting with your dashboards - Lightdash

**Source:** https://docs.lightdash.com/guides/interactive-dashboards

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Guides
Interacting with your dashboards
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
    * Interacting with your dashboards
    * Using the Slack integration
    * Scheduled deliveries
    * Chart Version History
    * Formatting your fields
    * How to promote content
    * Table calculation SQL templates
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Viewing the underlying data for a point on a chart
  * Using a chart to filter your dashboard (a.k.a. cross-filtering)
  * You can see which tiles had the filter applied by hovering over the dashboard filter applied text on your chart tile.
  * Drill into a metric in a chart or your results table using Drill into


##  Viewing the underlying data for a point on a chart
You can click on any point on a chart and view the records which make up that data point. For example, I can find out what the underlying data is for the $4,334.0 in my `What are the sales stats per partner, per month?` chart, by clicking on the bar for that month, and then clicking `View underlying data` in the action menu. I’d see all of the rows in the underlying table that make up that total. After viewing the underlying data, I can also:
  * Export this data as a CSV
  * Explore from this underlying data, which will take me to a new chart with the underlying data as the starting point


##  Using a chart to filter your dashboard (a.k.a. cross-filtering)
When you click on the value in a chart (e.g. a bar in your bar chart), you can choose to filter on that value and update all of the other relevant charts in the dashboard. This type of chart-to-dashboard filtering is sometimes called `cross-filtering`.
###  You can see which tiles had the filter applied by hovering over the `dashboard filter applied` text on your chart tile.
Once you’ve clicked on your filter, all of the tiles in your dashboard with the filter field will be filtered to the value you selected. You can see which tiles had the filter applied by hovering over the tile and then on the funnel icon to see the filter that was applied.
##  Date Zoom
When viewing a dashboard, you can change the date granularity (to Week, Year, etc.) of the **charts with date dimensions** by clicking on the `Date Zoom` button. This is helpful if you want to zoom in to look more closely at something, or zoom out to identify a trend. You’re able to quickly view your results at different time granularities without editing the chart. Here’s a quick video showing Date Zoom in action: When the date granularity of a chart is changed, you can hover over the indicator to see the date dimension that was affected: Any chart with results that have at least one date Dimension will be affected by Date Zoom (even if the date dimension is not explicitly shown on the chart).
If you have more than one date dimension in your results, Date Zoom will be applied to the first date dimension it scans - this is normally the left-most column in your results.
You’re only temporarily changing the dates in the tiles on your dashboard. If you refresh the dashboard, the affected tiles will go back to their default saved state. If you want to restrict access to this feature you can remove Date Zoom functionality from a dashboard by heading to edit mode, and hitting the ‘x’ on the Date Zoom dropdown.
##  Drill into a metric in a chart or your results table using `Drill into`
You can drill into a Metric in your chart or results table to better understand a point in your chart. Selecting `Drill into` lets you group your Metric by a Dimension, like revenue segmented by (or grouped by) product type. Note that `Drill into` only works for Metrics, not for Dimensions or Table Calculations.
##### Here’s an example of Drill into
I have a chart with **Sum of basket total** (a Metric) per Partner, per month. As you can see, there’s a high spike in sales for one of the partners in the month of May. I want to understand why this spike happened. To do this, I click on the data point in my chart, then click `Drill into` in the action menu: I then select the Dimension I want to segment my metric by (or “drill into”). In this example, I’m interested to see what Shipping country the orders were coming from, so I select **Shipping country** : Once I’ve selected the Dimension I want to group by, I click `Open in new tab` and see a chart with my Metric, grouped by `Shipping country`. Now I can uncover where this spike in sales is coming from 
Assistant
Responses are generated using AI and may contain mistakes.


