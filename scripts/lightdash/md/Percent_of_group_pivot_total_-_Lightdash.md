# Percent of group/pivot total - Lightdash

**Source:** https://docs.lightdash.com/guides/table-calculations/table-calculation-sql-templates/percent-of-group-pivot-total

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Table calculation SQL templates
Percent of group/pivot total
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
  * Here’s the SQL you can copy-paste to calculate the percent of the group/pivot total
  * Make sure to add percent formatting to your calculation


Here’s an example of a percent of the total group/pivot: And here’s the SQL used in the table calculation:
Copy
Ask AI
```
${orders.total_order_amount} /
  SUM(${orders.total_order_amount}) OVER (
    PARTITION BY
orders.status}


```

In general, the SQL used for calculating the percent of the total has two important columns:
  * `column_i_want_to_see_the_percent_of_total` - this is the column that you want to see the percent total of. In our example above, that was the `sum of profit`.
  * `column_i_want_to_group_by` - this is the column that you want the total to be grouped by. In our example above, that was the `order date - week`.


###  Here’s the SQL you can copy-paste to calculate the percent of the group/pivot total
Copy
Ask AI
```
${table.column_i_want_to_see_the_percent_of_total} /
  SUM(${table.column_i_want_to_see_the_percent_of_total}) OVER (
    PARTITION BY
table.column_i_want_to_group_by}


```

###  Make sure to add percent formatting to your calculation
In the `format` tab, make sure to update the format to `percent` so that your table calculation is shown as a percentage value (instead of a number).
Percent of column totalRank in column
Assistant
Responses are generated using AI and may contain mistakes.


