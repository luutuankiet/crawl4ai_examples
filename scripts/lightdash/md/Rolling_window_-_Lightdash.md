# Rolling window - Lightdash

**Source:** https://docs.lightdash.com/guides/table-calculations/table-calculation-sql-templates/rolling-window

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Table calculation SQL templates
Rolling window
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
  * Here’s the SQL you can copy-paste to calculate rolling windows


Here’s an example of a rolling window: And here’s the SQL used in the table calculation:
Copy
Ask AI
```
SUM(${dbt_orders.count_distinct_order_id}) OVER (
  ORDER BY
    ${dbt_orders.order_date_week}
  ROWS BETWEEN 3 PRECEDING AND CURRENT ROW

  SUM(${dbt_orders.count_distinct_user_id}) OVER (
    ORDER BY
dbt_orders.order_date_week}
    ROWS BETWEEN 3 PRECEDING AND CURRENT ROW


```

The SQL used for calculating rolling windows has at least two bits, with an optional third:
  * `first_column_I_want_to_sum` is the column with the values you want to add up (sometimes this is an average)
  * `column_I_want_to_order_by` is the column you want to order by when defining your lookback window
  * `N` is the number of previous rows you want to include in your calculation (don’t forget the current row is included, so for a four week lookback window, we’ll use N=3)
  * `second_column_I_want_to_sum` is optional, another column with values you want to add up to compare to your first column, like when calculating averages (which is how we use it in this example)


###  Here’s the SQL you can copy-paste to calculate rolling windows
Make sure you swap out the columns AND choose a number value for `N`.
Copy
Ask AI
```
SUM(${table.column_I_want_to_sum}) OVER (
  ORDER BY
    ${table.column_I_want_to_order_by}
  ROWS BETWEENPRECEDING AND CURRENT ROW

  SUM(${table.second_column_I_want_to_sum}) OVER (
    ORDER BY
table.column_I_want_to_order_by}
    ROWS BETWEENPRECEDING AND CURRENT ROW


```

Assistant
Responses are generated using AI and may contain mistakes.


