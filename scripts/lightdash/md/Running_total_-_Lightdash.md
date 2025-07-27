# Running total - Lightdash

**Source:** https://docs.lightdash.com/guides/table-calculations/table-calculation-sql-templates/running-total

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Table calculation SQL templates
Running total
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
  * Here’s the SQL you can copy-paste to calculate a running total


Here’s an example of a running total: And here’s the SQL used in the table calculation:
Copy
Ask AI
```
SUM(${orders.total_order_amount}) OVER (
  ORDER BY
    ${orders.order_date_month}
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW


```

In general, the SQL used for calculating running totals has two bits (with an optional third bit):
  * `column_I_want_to_sum` - this is the column with the values you want to add up
  * `column_I_want_to_order_by` - this is the column you want to order your running total over
  * `optional_other_column_I_want_to_order_by` - this column is optional and you can add as many more `order by` columns as you need. For your running total to only go up an increment of one row, you’ll need to add every dimension in your results table to the `ORDER BY` bit in your SQL. And, the order of these will need to be the same as the ordering you’ve added to the columns in your results table.


###  Here’s the SQL you can copy-paste to calculate a running total
Copy
Ask AI
```
SUM(${table.column_I_want_to_sum}) OVER (
  ORDER BY
    ${table.column_I_want_to_order_by},
    ${table.optional_other_column_I_want_to_order_by}
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW


```

**💎 Level up your SQL** :
  * You can specify if you want to order your columns in ascending order (1, 2, 3, 4) or descending order (4, 3, 2, 1) using the key words `ASC` and `DESC` in your `ORDER BY` clause. By default, a column will be ordered in ascending order - so if you want it ordered ascending, you don’t need to add anything.


Copy
Ask AI
```
SUM(${table.column_I_want_to_sum}) OVER (
  ORDER BY
    ${table.column_I_want_to_order_by} ASC,
    ${table.optional_other_column_I_want_to_order_by} DESC
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW


```

Rank in columnRolling window
Assistant
Responses are generated using AI and may contain mistakes.


