# Custom Tooltips - Lightdash

**Source:** https://docs.lightdash.com/references/custom-tooltip

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Reference
Custom Tooltips
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference
    * Creating Dashboards
    * Filters reference
    * Using custom fields


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


By default, tooltips will show the x-axis value, the y-axis field name, and the y-axis value, like this: You can customize tooltips to show additional metrics or table calculations from your results table. You can even include notes, links, or custom formatting for additional context. To use this feature, go to **Configure chart > Display > Custom Tooltip**.
HTML is allowed in the Custom tooltip code, but Javascript is disabled.
You can also select variables from your chart, from any of the axes, even on grouped charts. Start typing the name of the field, and we’ll autocomplete with the right variable. Here is an example code block for a custom tooltip:
Copy
Ask AI
```
<strong>💰 Profit this month:</strong>
 ${dbt_orders_sum_of_profit}
<br>
<strong>🛒 Average basket this month:</strong>
 ${dbt_orders_average_of_basket_total}
<br>
<strong>💳 Total Orders this month:</strong>
 ${dbt_orders_count_distinct_order_id}
<h3>Additional resources:</h3>
Check out the <a href="https://analytics.lightdash.cloud/projects/21eef0b9/dashboards/e2b82df2/view">Sales Dashboard</a> and the Notion doc about <a href="https://notion.so">Orders and Revenue KPIs</a>.

```

The above code will look like this in the tooltip: Custom tooltips will show up on saved charts, dashboards, and the code will be included in dashboards as code downloads.
If you need to show some data that is not included in the chart (eg: a dynamic URL, or an ID) , you can even create a table calculation, and include it on on the chart as an extra axis to use this variable on the tooltip.
Using custom fieldsCustom Charts
Assistant
Responses are generated using AI and may contain mistakes.


