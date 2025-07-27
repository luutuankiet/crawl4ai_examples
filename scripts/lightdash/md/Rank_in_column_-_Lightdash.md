# Rank in column - Lightdash

**Source:** https://docs.lightdash.com/guides/table-calculations/table-calculation-sql-templates/rank-in-column

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Table calculation SQL templates
Rank in column
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
  * Here’s the SQL you can copy-paste to calculate your rank in column


Here’s an example of a percent change calculation: And here’s the SQL used to generate it:
Copy
Ask AI
```
ROW_NUMBER() OVER (
  PARTITION BY
    ${orders.order_date_month}
  ORDER BY
    ${orders.total_order_amount} DESC


```

In general, the SQL used for calculating the rank in a column has just one important column and one other important parameter:
  * `column_i_want_to_rank` - this is the column that you want to rank
  * `ASC` and `DESC` - if you want to have the **biggest values** with rank = 1, then you need to add `DESC` to your `ORDER BY` clause. If you want the **smallest values** with rank = 1 then you can add `ASC` to your `ORDER BY` clause (this isn’t required, since the ordering is `ASC` by default).


###  Here’s the SQL you can copy-paste to calculate your rank in column
Copy
Ask AI
```
ROW_NUMBER() OVER (
  ORDER BY
    ${table.column_i_want_to_rank} DESC


```

Percent of group/pivot totalRunning total
Assistant
Responses are generated using AI and may contain mistakes.


