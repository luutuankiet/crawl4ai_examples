# Percent of column total - Lightdash

**Source:** https://docs.lightdash.com/guides/table-calculations/table-calculation-sql-templates/percent-of-total-column

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Table calculation SQL templates
Percent of column total
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
      * Percent change from previous
      * Percent of previous value
      * Percent of column total
      * Percent of group/pivot total
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
  * Here’s the SQL you can copy-paste to calculate the percent of the column total
  * Make sure to add percent formatting to your calculation


Here’s an example of a percent of the total column: And here’s the SQL used in the table calculation:
Copy
Ask AI
```
${orders.total_order_amount} / SUM(${orders.total_order_amount}) OVER()

```

In general, the SQL used for calculating the percent of the total has just one important column:
  * `column_i_want_to_see_the_percent_of_total` - this is the column that you want to see each value’s percent of the total values in that column


###  Here’s the SQL you can copy-paste to calculate the percent of the column total
Copy
Ask AI
```
${table.column_i_want_to_see_the_percent_of_total} /
  SUM(${table.column_i_want_to_see_the_percent_of_total}) OVER()

```

###  Make sure to add percent formatting to your calculation
In the `format` tab, make sure to update the format to `percent` so that your table calculation is shown as a percentage value (instead of a number).
Percent of previous valuePercent of group/pivot total
Assistant
Responses are generated using AI and may contain mistakes.


