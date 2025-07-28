# SQL concepts for derived tables  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-experts-derived-tables

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How Looker generates the SQL for derived tables
  * SQL-based derived tables
  * Native derived tables
  * Persistent derived tables (PDTs)
  * Related resources




Was this helpful?
Send feedback 
#  SQL concepts for derived tables
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How Looker generates the SQL for derived tables
  * SQL-based derived tables
  * Native derived tables
  * Persistent derived tables (PDTs)
  * Related resources


While LookML views are typically based on existing tables within your database, you can also create views that are based on SQL `SELECT` statements. In Looker, this type of view is called a _derived table_. Derived tables are queries whose results are used as if the results were actual tables in the database.
In this guide, you'll learn about the following topics:
  * How Looker generates the SQL for derived tables
  * SQL-based derived tables
  * Native derived tables
  * Persistent derived tables (PDTs)


## How Looker generates the SQL for derived tables
When you query derived tables in LookML, Looker translates your queries into SQL statements as Common Table Expressions (CTEs) or inline views, depending on the dialect. In other words, the generated SQL queries can resemble one of the following examples.
The following example shows how Looker might generate a SQL query that uses a CTE to query a derived table:
```
WITH(
SELECTo.user_idasid
FROMordersASo
INNERJOINorder_itemsASoiONo.id==oi.order_id
ORDERBYSUM(oi.total_sale_price)DESC
GROUPBYo.customer_id
LIMIT100
)AStop_100_users
SELECT...
FROMusersASu
INNERJOINtop_100_usersONu.id==top_100_users.id
WHERE...

```

The following example shows how Looker might generate a SQL query that uses an inline view to query a derived table:
```
SELECT...
FROMusersASu
INNERJOIN(
SELECTo.user_idasid
FROMordersASo
INNERJOINorder_itemsASoiONo.id==oi.order_id
ORDERBYSUM(oi.total_sale_price)DESC
GROUPBYo.customer_id
LIMIT100
)AStop_100_usersONu.id==top_100_users.id
WHERE...

```

## SQL-based derived tables
To create a SQL-based derived table, you define a SQL query directly within the LookML by using the `sql` parameter within the `derived_table` parameter of a view. This lets you define the columns of the derived table by using SQL.
For example, the following sample LookML defines a derived table called `top_100_users` that identifies the top 100 users with the highest total spending across all their orders:
```
view: top_100_users {
  derived_table: {
    sql: SELECT o.user_id as id
         FROM orders AS o
         INNER JOIN order_items AS oi ON o.id == oi.order_id
         ORDER BY SUM(oi.total_sale_price) DESC
         GROUP BY o.customer_id
         LIMIT 100 ;;
  }

  dimension: id {
    type: number
    sql: ${TABLE}.id ;;
  }
}

```

When the `top_100_users` view is referenced in an Explore query, Looker uses this SQL `SELECT` statement in the generated SQL as either a CTE or an inline view, depending on your dialect.
Using SQL to define derived tables can have some limitations. In the example from the SQL-based derived tables section, for example, the following considerations apply:
  * The relationship between the `orders` and `order_items` tables is probably already defined in the LookML model. If the underlying table names in your database change, then the table names must be updated in multiple places, including in the definition of your SQL-based derived table.
  * The SQL in your derived table definition has to be in the correct dialect for the underlying database. If the data is moved to a different database, then the definition of your SQL-based derived table needs to be changed.


For these reasons, native derived tables are often a better choice.
## Native derived tables
In Looker, native derived tables are defined with LookML. In contrast to using SQL-based derived tables, when you define a native derived table, you're leveraging your LookML model in the following ways:
  * If the table name changes in the database, then you only need to update it once in the LookML model. Because your native derived table points to the existing LookML object where the database table is defined, your native derived table will automatically refer to the appropriate table.
  * Likewise, if you move to a different dialect, the LookML for the native derived table will still be valid because Looker generates the SQL that is appropriate to your database connection.


You can define the LookML for the native derived table manually. However, the easiest way to create a native derived table is to have Looker create the derived table from an Explore query. In your Explore, select the fields that you want to use in your derived table, and use the **Get LookML** > **Derived Table** option from the Explore gear menu to get the LookML. Looker generates the LookML that you need to create a derived table from your Explore query, including the relevant field definitions from your LookML model that are necessary to create the columns for your derived table. You can copy the LookML into a view file in your project to create the derived table.
The following example shows a native derived table that identifies the top 100 users with the highest total spending across all their orders:
```
view: top_100_users {
  derived_table: {
    explore_source:  orders {
      column: id {
        field: orders.customer_id
      }
      sorts: [order_items.sum_total_sale_price desc]
      limit: 100
    }
  }
}

```

When you query a native derived table in an Explore, all the details of the SQL query for the native derived table are generated automatically. The definitions of the columns of a LookML view with a native derived table are inferred from the definitions of the underlying Explore, eliminating the need to repeat any definitions.
## Persistent derived tables (PDTs)
In Looker, you can create both temporary derived tables and persistent derived tables. Once you create a SQL-based derived table or a native derived table, you can add persistence so that Looker writes the table into a scratch schema on your database and regenerates it on the schedule that you specify. For more information, see Derived tables in Looker.
## Related resources
  * Derived tables in Looker
  * Creating native derived tables
  * How Looker generates SQL


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


