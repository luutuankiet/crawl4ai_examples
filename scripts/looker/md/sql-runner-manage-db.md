# Managing database functions with SQL Runner  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-runner-manage-db

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Modifying database schema and data
  * Examining an execution plan using EXPLAIN
  * Getting information about your database
    * Getting database connection information
    * BigQuery gear menu options
    * Searching your database
    * Getting table information




Was this helpful?
Send feedback 
#  Managing database functions with SQL Runner
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Modifying database schema and data
  * Examining an execution plan using EXPLAIN
  * Getting information about your database
    * Getting database connection information
    * BigQuery gear menu options
    * Searching your database
    * Getting table information


SQL Runner provides a way to directly access your database and use that access in a variety of ways. Using SQL Runner, you can navigate the tables in your schema, use an ad hoc Explore from a SQL query, run prewritten descriptive queries on your data, see your SQL Runner history, download results, share queries, add to a LookML Project as a derived table, and perform other useful tasks.
This page describes how to modify your database schema and data using SQL Runner, view your database's execution plan for a query with the EXAMINE statement, and how to use SQL Runner to get information about your database. See these other documentation pages for information on:
  * SQL Runner basics
  * Using SQL Runner to create queries and Explores
  * Using SQL Runner to create derived tables


## Modifying database schema and data
In addition to running queries on your database, the **Database** tab in SQL Runner lets you execute Data Definition Language (DDL) and Data Manipulation Language (DML) statements on your database. You can use SQL Runner to make schema changes (such as create, drop, and alter) and data changes (such as insert, update, and delete). SQL dialects have varying support for DDL and DML statements, so see the documentation for your database to find out which statements are supported.
To execute a DDL or DML statement on your database in SQL Runner, follow these steps:
  1. Navigate to SQL Runner.
  2. In SQL Runner, click the **Database** tab.
  3. Enter the DDL or DML statement in the SQL Runner **Query** box. (See the documentation for your database dialect for the support and syntax of DDL and DML statements.)
  4. Click **Run** to execute the statement on your database.


If the statement is successfully executed on your database, the SQL **Results** box will show a confirmation.
## Examining an execution plan using `EXPLAIN`
In addition to running SQL queries against your database, you can use SQL Runner to run an `EXPLAIN` function for a query. The `EXPLAIN` function, which is supported by most SQL dialects, returns the database's execution plan for a query.
  1. From an Explore, run a query and click the **SQL** tab of the **Data** area to view the query's SQL command.
  2. In the **SQL** tab of the Explore, click the **Explain in SQL Runner** button.
Looker will open SQL Runner and load the query within an `EXPLAIN` function.
  3. In SQL Runner, click **Run** to execute the `EXPLAIN` function.
  4. View the output of the `EXPLAIN` function.


The exact information and format of the `EXPLAIN` response will depend on your specific dialect, so you should see the documentation for your dialect for specifics.
In the preceding MySQL example, the `EXPLAIN` function returns a list of the steps taken by the database to complete the query. This may be useful for queries that seem slow to execute, since you may find that your database is scanning an entire table in a query, when perhaps the table could use an index to improve performance.
For a step-by-step example of using `EXPLAIN` in SQL Runner to optimize SQL, see the How to Optimize SQL with EXPLAIN  Community post.
## Getting information about your database
The **Database** tab in SQL Runner has a bunch of tools to give you insight into your database.
### Getting database connection information
When you choose a connection in SQL Runner, Looker displays the database dialect for that connection at the right of the **SQL QUERY** banner. If you navigated to SQL Runner by choosing **Open in SQL Runner** or **Explain in SQL Runner** , then Looker preselects the appropriate connection for you and displays the connection's database dialect.
Click the connection gear menu to get more options for the database connection:
  * Select the **Show Processes** option to display information about queries and processes currently running on the connection.
  * Select the **Refresh Schemas & Tables** option to repopulate the SQL Runner left navigation pane with the schemas and tables in the database.


### BigQuery gear menu options
When you choose a BigQuery connection that supports multiple databases, Looker displays dialect-specific options in the gear menu. The menu item switches between **Show available projects** and **Search public projects** , depending on which option is selected.
  * Select **Refresh Schemas & Tables** to repopulate the SQL Runner left navigation pane with the schemas and tables that are in the database.
  * When available projects are displayed, there is a gear menu option to **Search public projects**. Select this option to search for public datasets that are not visible in the information schema.
  * When public projects are displayed, there is a gear menu option to **Show available projects**. Select this option to revert the display back to connection-specific BigQuery projects and tables in the SQL Runner left navigation pane.


### Searching your database
SQL Runner displays a search box under the selected **Schema** (or **Dataset** , for Google BigQuery connections).
The SQL Runner search browses the names of all tables and table columns that contain the string in the search box. In the following figure, 'airport_name' is a column and 'airport_remarks' is a table.
Click on one of the search results to navigate to that item in SQL Runner.
### Getting table information
> By default, SQL Runner preloads all table information when you select a connection and a schema. For connections that have many tables or very large tables, an admin can disable this behavior by deselecting the **SQL Runner Precache** option in the Connections page.
SQL Runner's left-hand navigation panel lets you navigate the schemas and tables in your connections. Select a connection and a schema to see all the tables in that schema. Click on a table name to see the fields in that table.
SQL Runner has some prewritten queries to help you understand your data. In order to use these queries, click the gear that appears next to the name of a table or table column and select the query you want to run. Looker generates the SQL automatically in the **SQL Query** section, and the query will be run.
> The available queries will vary by database dialect.
#### Table information
Looker displays the following options when you click the gear next to a table name:
  * **Explore Table** : Opens a new browser tab to a Looker Explore of the table.
  * **Describe** : Displays the column names in the underlying table as well as their data types.
  * **Show Indexes** : Displays information about how the table is indexed.
  * **Select 10** : Returns a query of the first ten rows in the table. This is a good way to get a sense of what the data actually looks like.
  * **Count** : Returns a simple `count(*)` query to get the total row count of the table.


#### Column information
Click a table name to see the columns in the table. Looker displays the following options when you click the gear next to a column name:
  * **Most Common Values** : Returns a query of the most common values for that table column, along with a count of the number of times that value is found in the column.
  * **Approximate Count Distinct** : Displays an approximate count of the number of distinct values found in the column.


##### Getting column data type information
You can use SQL Runner to get column data type information by performing the following steps:
  1. In SQL Runner, select the database connection from the **Connection** drop-down.
  2. Select the schema from the **Schema** drop-down. (For BigQuery connections, select **Project** and **Dataset**.)
  3. SQL Runner displays the list of tables in that schema on your database. Click on a table to see the columns in that table.
  4. Each column name has an icon to represent the data type. Hover over a column name to see the type of data in that column.


#### Editing the prebuilt SQL queries
You can edit any SQL query in the **Query** area, including the preset SQL queries chosen from the table and field gear menus.
For example, you can use the SQL Runner **Count** query to load in a basic count command for a database, then edit the SQL query. So if you think the `id` column in the `public.users` table could be a primary key, you can validate that there are no duplicate values by editing the count query like this:
```
SELECTid,COUNT(*)
FROMpublic.users
GROUPBY1
ORDERBY2DESC
LIMIT10

```

Because the query is sorted by the count before the results are limited to 10 rows, the results will include the highest count values. If this query returns a count of 1 for each `id` value, then `id` would likely be the primary key in this table. However, this query specifies only the rows in the table at query runtime. Since future insertions to the database may disqualify `id` as a primary key, we recommend implementing restrictions on your database to ensure that your primary keys are unique.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


