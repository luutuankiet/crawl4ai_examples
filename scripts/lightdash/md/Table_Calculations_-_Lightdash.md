# Table Calculations - Lightdash

**Source:** https://docs.lightdash.com/references/table-calculations

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Reference
Table Calculations
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


On this page
  * When to use table calculations
  * Creating table calculations
  * Using Quick Calculations
  * Using Custom Table Calculations
  * Table calculation SQL templates


You add table calculations in the Explore view and they appear as green columns in your results table (remember, dimensions are blue, and metrics are orange). Table calculations are built using raw SQL. That means you can use table calculations to build mathematical, True/False, text, and date-based calculations (basically, anything you can do in SQL, you can do in table calculations).
##  When to use table calculations
Typically, in your Lightdash project, you’ll have one or more Tables that you’ve pre-defined in your dbt project (this is probably done by the data analysts/engineers/analytics engineers). But sometimes, you’ll need particular logic which hasn’t been defined as a dimension or metric in your dbt project - maybe because you have a new kind of question or use case. This is when you might need a table calculation. Watch out: table calculations can be easier to create than regular metrics/dimensions, but they are not as easy to manage. If you find yourself creating the same table calculation over and over again when you’re using a Table, then it might be worth adding it in as a more permanent metric in your dbt project! You can read more about adding metrics to your dbt project here.
##  Creating table calculations
Before you create a table calculation, you need to add some dimensions and/or metrics to your results table. Table calculations can only be built using the dimensions + metrics that you’ve included in your results table. So, to create a table calculation, first, you need to add the dimensions and/or metrics for your table calculation to your results table.
###  Using Quick Calculations
Quick calculations are shortcuts to the most common table calculations, these are only available to metrics in the contextual menu in the results table. To learn more about what these calculations are doing, check out the docs here. Once the table calculation is generated you can edit it to modify the SQL query or update the format.
###  Using Custom Table Calculations
Once you’ve got some data in your results table, you can create a table calculation by clicking on the `+ Table calculation` in the `Results` tab of the Explore view:
##### Write the SQL for your table calculation in the pop-up box
Your table calculation is defined using raw SQL that you write up in this pop up box. If you’re not sure what to write here, you can check out some of our table calculation SQL templates. To reference the metrics and dimensions in your results table, you can either use the autocomplete, or you can manually write the full field name using the format `${table_name.field_name}`.
##### Update the format of your table calculation (if needed)
If needed, you can update the format of your table calculation to things like percent formatting using the `format` tab. Format types | Description | Raw value | How it might look like in Lightdash  
---|---|---|---  
Default | Default format for the table calculation result | 0.75 | 0.75  
Percent | Converts numbers into a percentage | 0.75 | 75%  
Currency | Adds currency symbol and default locale format | 1234.1234 | $ 1234.12  
Number | Formats number with prefix and suffix | 123.1234 | Speed: 123.12 km/h  
##### To delete or edit your table calculation, just click on the gear icon by the field name
If you need to edit or delete a table calculation, you can just click on the toggle beside the field and do what you need to do!
##  Table calculation SQL templates
I’m not sure about you, but I definitely rely on copy-pasting old SQL code to write 90% of my new SQL queries. So, we thought it might be useful to give you some snippets of SQL code to help you get started with your most common table calculations. You can check out our table calculation SQL templates here.
Filters referenceUsing custom fields
Assistant
Responses are generated using AI and may contain mistakes.


