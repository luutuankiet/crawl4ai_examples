# Exploring your content - Lightdash

**Source:** https://docs.lightdash.com/get-started/exploring-data/exploring-your-content

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Quickstart
Exploring your content
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
    * Exploring your content
    * Metrics and dimensions
    * Sharing with your team
    * Creating Dashboards
  * Guides
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
  * Browsing the saved charts and dashboards in your project
  * Using the search bar
  * Search filters
  * Search groups
  * Exploring data in a chart
  * View underlying data
  * Drill into a metric
  * Exploring data in a dashboard
  * Explore from existing charts
  * Exploring from scratch with Tables


##  Browsing the saved charts and dashboards in your project
The easiest way to get started in Lightdash is to check out the saved charts and dashboards that your team’s already made. You can see a list of some of this content on your homepage as soon as you land in Lightdash. You can always get back to your homepage by clicking on the Lightdash icon in the top-left corner of your screen. You can also browse the lists of all of the saved charts, dashboards, and Spaces that you and your teammates have made in your project by clicking on `Browse` in your navbar.
##  Using the search bar
If you already know what you’re looking for, you can use the search bar to search through all the content in your Lightdash project. Just click on the search bar at the top of your screen, or press `Cmd + K` (Mac) or `Ctrl + K` (Windows, Linux) to open the search bar. This global search feature matches content from everywhere in the project. You can search for dashboards, charts, spaces, tables, and fields by their names and descriptions. It is now more powerful, with the ability to filter results and group them for easier navigation.
###  Search filters
Enhance your search experience by applying filters directly in the search bar. Specify what you’re looking for by content type, and narrow down results by dates, either by choosing a range (e.g., “from: January 10, 2024, to: January 20, 2024”) or a single date (“from: January 10, 2024”). You can also filter results by the creator of the content, making it easier to find items created by specific team members.
###  Search groups
Search results are organized into groups, making navigation through the findings simpler. Items within each group are sorted by their relevance to your query, ensuring that the most pertinent results are always easy to find. This organization aids in quickly identifying the exact type of content you’re searching for, whether it be a chart, dashboard, or any other entity within your project.
##  Exploring data in a chart
###  View underlying data
You can click on any point on a chart or any cell in a results table and view the records which make up that data point. For example, I can click on the page views bar in my chart or the value in the results table cell and I’d see all of the rows in the underlying table that make up the 19,120 page views count. I can then export this as a CSV or explore from this underlying data.
##### Specify fields in `view underlying data`
By default, we show all of the dimensions from the Table. If you have fields from a joined table included in your results table, then we’ll also show you all of the fields from the joined Table. If you don’t want all of the fields from your Table shown, then you can specify which fields you want users to see when they click on `show underlying data` for a field. Check out the metric reference docs to see how to do this in your Table’s `.yml` file. By default, when you click `Explore from here` from the `view underlying data` table, you’re brought to an Explore view with no fields selected. If you specify fields in `show underlying data`, then these fields will be automatically added to the results table, so users won’t `Explore from here` into an empty results table.
###  Drill into a metric
You can drill into a metric in your chart or results table to better understand a point in your chart. Selecting `drill by` lets you group your metric by a dimension, like the total revenue segmented by (or grouped by) product type. Note that `drill by` only works for metrics, not for dimensions or table calculations.
##### Here’s an example of how to use drill by
I have a chart with the total number of page views (a metric) over time. You can see, there’s a spike in October, so I want to drill into that data point and see where this traffic is coming from… To do this, I click on the data point in my chart, then click `drill by` in the action menu: I then select the dimension I want to segment my metric by (or “drill by”). In this example, I’m interested in grouping the total page views by the `source` so I can figure out where this traffic is coming from. Once I’ve selected the dimension I want to group by, I click `open in new tab` and see a chart with my metric, grouped by `Source`. Now I can uncover where this spike in web traffic was coming from 
##  Exploring data in a dashboard
Dashboards allow you to arrange multiple charts that are related to each other into a single view. You can interact with dashboards in your project in a few different ways. Learn more about it here.
##  Explore from existing charts
One of the best ways of exploring data is using saved charts and charts in dashboards as the starting point to your data exploration. You can do this in Lightdash using the `Explore from here` button. `Explore from here` gives you a copy of the same chart you can play around with. Any changes you make here **will not affect** the original chart - so you can Explore away without any worry of breaking things! If you’ve never used the Explore View, then checkout this tutorial on using the Explore View in Lightdash.
##  Exploring from scratch with Tables
If you can’t find any relevant saved charts or dashboards that answer your question, you can always explore your Tables from scratch. To start an Explore view from scratch, just click on `Explore` —> `Tables` —> then select the table that you want to explore. If you’ve never used the Explore View, then checkout this tutorial on using the Explore View in Lightdash.
OverviewMetrics and dimensions
Assistant
Responses are generated using AI and may contain mistakes.


