# Percent change from previous - Lightdash

**Source:** https://docs.lightdash.com/guides/table-calculations/table-calculation-sql-templates/percent-change-from-previous

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Table calculation SQL templates
Percent change from previous
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
  * Here’s the SQL you can copy-paste to calculate the percent change from the previous
  * Make sure to add percent formatting to your calculation


Here’s an example of a percent change calculation: And here’s the SQL that was used to generate it:
Copy
Ask AI
```

  ${orders.total_order_amount} /
    LAG(${orders.total_order_amount}) OVER (
      ORDER BY
orders.order_date_week}



```

In general, the SQL used for calculating the percent change from the previous value has two bits (with an optional third bit):
  * `column_I_want_to_compare` - this is the column with the values you want to compare
  * `column_I_want_to_order_by` - this is the column you want to use to order the values you want to compare
  * `optional_other_column_I_want_to_order_by` - this column is optional and you can add as many more `order by` columns as you need. Normally, you’ll need to add every dimension in your results table to the `ORDER BY` bit in your SQL. And, the order of these will need to be the same as the ordering you’ve added to the columns in your results table.


###  Here’s the SQL you can copy-paste to calculate the percent change from the previous
Copy
Ask AI
```

  ${table.column_i_want_to_compare} /
    LAG(${table.column_i_want_to_compare}) OVER (
      ORDER BY
table.column_I_want_to_order_by},
table.optional_other_column_I_want_to_order_by}



```

###  Make sure to add percent formatting to your calculation
In the `format` tab, make sure to update the format to `percent` so that your table calculation is shown as a percentage value (instead of a number).
OverviewPercent of previous value
Assistant
Responses are generated using AI and may contain mistakes.


