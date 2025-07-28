# Using SQL Runner to create derived tables  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-runner-create-derived-tables

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Adding a SQL Runner query to a LookML project
    * Get Derived Table LookML
  * Debugging using SQL Runner
    * SQL Runner error highlighting
    * Using SQL Runner to test derived tables




Was this helpful?
Send feedback 
#  Using SQL Runner to create derived tables
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Adding a SQL Runner query to a LookML project
    * Get Derived Table LookML
  * Debugging using SQL Runner
    * SQL Runner error highlighting
    * Using SQL Runner to test derived tables


SQL Runner provides a way to directly access your database and leverage that access in a variety of ways. Using SQL Runner, you can easily navigate the tables in your schema, use an ad hoc Explore from a SQL query, run prewritten descriptive queries on your data, see your SQL Runner history, download results, share queries, add to a LookML Project as a derived table, and perform other useful tasks.
This page describes how to create a derived table using SQL Runner and how to use SQL Runner to debug derived tables. See these other documentation pages for information on:
  * SQL Runner basics
  * Using SQL Runner to create queries and Explores
  * Managing database functions with SQL Runner


## Adding a SQL Runner query to a LookML project
SQL Runner is a great place to test SQL to use as a derived table in your LookML project. You can even get a SQL query from a different tool, test it in SQL Runner, and then add it to your LookML project.
Once you have created a SQL query in SQL Runner, you can create a derived table from the query by using the **Add to Project** option or the **Get Derived Table LookML** option. Both of these options allow you to take a query in SQL Runner and add them to your LookML project. See the following sections for information.
### Add to Project
Using the **Add to Project** option is the easiest way to add a SQL Runner query to your project:
The **Add to Project** option lets you select a LookML project, and then Looker automatically creates a view file with the query in your selected project. If you would prefer instead to manually create the view file and add the query's LookML yourself, you can use the **Get Derived Table LookML** option.
Follow these steps to use the **Add to Project** option:
  1. Use SQL Runner to create a SQL query that you want to use for a derived table.
  2. Click **Add to Project** from the gear menu in the upper right.
  3. Select the project you want to add this derived table to.
  4. Enter a view name for the derived table.
  5. Click **Add** to add the query as a derived table in your project. Looker will switch to Development Mode if not already in it, create a new view file with the LookML from the SQL Runner query, and then open the IDE file browser to the new view file.
  6. Move the file to suit your project's file organization.
  7. Validate the LookML and deploy your changes to production.


### Get Derived Table LookML
Another way to create a derived table from your SQL Runner query is to use the **Get Derived Table LookML** option from the SQL Runner gear menu. Just like with the **Add to Project** option, Looker will provide the LookML needed to make your SQL query into a derived table. From there, you can copy the LookML to paste into your project yourself, which is useful if you want to replace an existing derived table.
To create a derived table from a SQL Runner query:
  1. Use SQL Runner to create a SQL query that you want to use for a derived table.
  2. Click the gear menu and select **Get Derived Table LookML**.
  3. From the **Get Derived Table LookML** pop-up, click the **add it to your project** link.
  4. Use the drop-down **Project** list to choose the project you would like to add the derived table to.
  5. Enter a name for the new view in the **View Name** field. See the Managing LookML files and folders page for file naming conventions.
  6. Click the **Add** button. Looker will switch to Development Mode if not already in it, create a new view file with the LookML from the SQL Runner query, and then open the IDE file browser to the new view file.
  7. Move the file to suit your project's file organization.
  8. Validate the LookML and deploy your changes to production.


## Debugging using SQL Runner
SQL Runner is also a useful tool for checking SQL errors in the definition of a derived table.
### SQL Runner error highlighting
SQL Runner highlights the location of errors in the SQL command and includes the position of the error in the error message.
The position information provided will vary depending on the database dialect. For example, MySQL provides the line number that contains the error, while Redshift provides the character position of the error. Other database dialects might have one of these or other behaviors.
SQL Runner also highlights the location of the _first_ syntax error in the SQL command by underlining it in red and marking the row with an "x". Hover over the "x" to see more information on the error. After you fix that issue, click **Run** to see if there are any more errors in the query.
### Using SQL Runner to test derived tables
If you see an error coming from a derived table, you can determine the cause of the error by copying the SQL statement into SQL Runner and testing different parts of the SQL to narrow down the location of the error. For more information, see the Using SQL Runner to test derived tables Looker Community post.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-24 UTC.


