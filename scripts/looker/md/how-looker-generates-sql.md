# How Looker generates SQL  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/how-looker-generates-sql

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing the query
  * Canonical form of a Looker query
  * Fundamental components of a Looker query
  * An example query and the resulting SQL
  * Running raw SQL in Looker's SQL Runner
  * Examining query components in the expanded URL
  * How Looker structures JOINs
  * SQL blocks specify custom SQL clauses
    * Example SQL blocks for dimensions and measures
    * Example SQL block for derived tables
    * Example SQL block for filtering an Explore




Was this helpful?
Send feedback 
#  How Looker generates SQL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing the query
  * Canonical form of a Looker query
  * Fundamental components of a Looker query
  * An example query and the resulting SQL
  * Running raw SQL in Looker's SQL Runner
  * Examining query components in the expanded URL
  * How Looker structures JOINs
  * SQL blocks specify custom SQL clauses
    * Example SQL blocks for dimensions and measures
    * Example SQL block for derived tables
    * Example SQL block for filtering an Explore


If you come to Looker from a SQL background, you're probably curious about how Looker generates SQL. Fundamentally, Looker is a tool that generates SQL queries and submits them against a database connection. Looker formulates SQL queries based on a LookML project that describes the relationship between tables and columns in the database. By understanding how Looker generates queries, you will better understand how your LookML code translates to efficient SQL queries.
Every LookML parameter controls some aspect of how Looker generates SQL, by altering the structure, content, or behavior of the query. This page describes the principles of how Looker generates SQL, but does not cover all LookML elements in detail. The LookML quick reference documentation page is a good place to start for information on LookML parameters.
## Viewing the query
In a saved Look or in an Explore, you can use the **SQL** tab in the **Data** panel to see what Looker sends to the database to get the data. You also can use the **Open in SQL Runner** and **Explain in SQL Runner** links at the bottom of the **SQL** tab to view your query in SQL Runner or to see the database's explain plan for the query.
For more on SQL Runner, see the SQL Runner basics documentation page. For more information on optimizing a query using SQL Runner, see the How to optimize SQL with EXPLAIN Community post.
## Canonical form of a Looker query
Looker's SQL queries always take the following form.
```
SELECT
dimension>,dimension>,...
measure>,measure>,...
FROMexplore>
LEFTJOINview>ON...
LEFTJOINview>ON...
WHERE(<dimension_filter_expression>)AND(<dimension_filter_expression>)AND...
GROUPBYdimension>,dimension>,dimension>,...
HAVINGmeasure_filter_expression>ANDmeasure_filter_expression>AND...
ORDERBYdimension>|measure>
LIMITlimit>

```

The LookML project defines all the dimensions, measures, Explores, and views that are referenced in the SQL query. Filter expressions are specified in Looker by the user to shape ad hoc queries. Filter expressions can also be declared directly in the LookML to apply to all queries.
## Fundamental components of a Looker query
All Looker queries are represented by these fundamental parameters applied to a LookML project, as seen in the previous example query.
Looker uses the following parameters to generate a complete SQL query:
  * **`model`**: the name of the LookML model to target, which specifies the target database
  * **`explore`**: the name of the Explore to query, which populates the SQL`FROM` clause
  * **Fields** : the **`dimension`**and**`measure`**parameters to include in the query, which populate the SQL`SELECT` clause
  * **`filter`**:Looker filter expressions to apply to zero or more fields, which populate the SQL `WHERE` and `HAVING` clauses
  * **Sort order** : the field to sort by, and the sort order, which populates the SQL `ORDER BY` clause


These parameters are precisely the elements that a user specifies when building a query on the Looker **Explore** page. These same elements show up in all modes of executing queries with Looker, such as in the generated SQL, in the URL that represents the query, and in the Looker API.
What about the views specified by the `LEFT JOIN` clauses? `JOIN` clauses are populated based on the structure of the LookML model, which specifies how views join to Explores. When constructing SQL queries, Looker includes `JOIN` clauses only when required. When users are building a query in Looker, they don't have to specify how tables join together, because this information is encoded in the model -- one of Looker's most powerful benefits to business users.
## An example query and the resulting SQL
Let's build a query in Looker to demonstrate how the query gets generated according to the previous pattern. Consider an ecommerce store that has a database with two tables, **orders** and **users** , to track users and orders.
`orders`  
---  
`id INT`  
`created_at DATETIME`  
`users_id INT`  
`status VARCHAR(255)`  
`traffic_source VARCHAR(15)`  
`users`  
---  
`id INT`  
`email VARCHAR(255)`  
`first_name VARCHAR(255)`  
`last_name VARCHAR(255)`  
`created_at DATETIME`  
`zip INT`  
`country VARCHAR(255)`  
`state VARCHAR(255)`  
`city VARCHAR(255)`  
`age INT`  
`traffic_source VARCHAR(15)`  
Let's find the number of orders (**ORDERS Count**) grouped by state (**USERS State**) and filtered by the creation date of the order (**ORDERS Created Date**) in a Looker Explore.
To see the SQL query that is generated and executed by Looker, click the **SQL** tab in the **Data** panel.
```
SELECTCOALESCE(users.state,' ')AS"_g1",
users.stateAS'users.state',
COUNT(DISTINCTorders.id)AS'orders.count'
FROMorders
LEFTJOINusersONorders.user_id=users.id

WHERE
orders.created_atBETWEEN(CONVERT_TZ(DATE_ADD(CURDATE(),INTERVAL-29day),'America/Los_Angeles','UTC',))AND(CONVERT_TZ(DATE_ADD(DATE_ADD(DATE_ADD(CURDATE(),INTERVAL-29day),INTERVAL30day),INTERVAL-1second),'America/Los_Angeles','UTC'))
GROUPBY1
ORDERBYCOUNT(DISTINCTorders.id)DESC
LIMIT500

```

Note the similarity to the canonical query formula. The Looker SQL exhibits some traits of machine-generated code (for example, `COALESCE(users.state,'') AS "_g1"`), but always fits the formula.
Experiment with more queries in Looker to prove to yourself that the query structure is always the same.
## Running raw SQL in Looker's SQL Runner
Looker includes a feature called SQL Runner where you can run any SQL you like against the database connections you've set up in Looker.
Since every query generated by Looker results in a complete, functional SQL command, you can use the SQL Runner to investigate or play with the query.
Raw SQL queries that are executed in SQL Runner produce the same result set. If the SQL contains any errors, SQL Runner will highlight the location of the first error in the SQL command and will include the position of the error in the error message.
## Examining query components in the expanded URL
After running a query in Looker, you can examine the expanded URL to see the fundamental components of a Looker query. Begin by selecting **Share** from the Explore's gear menu to open the **Share URLs** menu.
The expanded URL provides sufficient information to recreate the query. For example, this expanded URL example provides the following information:
```
https://<Looker instance URL>.cloud.looker.com/explore/e_thelook/events?fields=users.state,users.count
&f[users.created_year]=2020&sorts=users.count+desc&limit=500

```

model | `e_thelook`  
---|---  
explore | `events`  
fields to query and display | `fields=users.state,users.count`  
sort field and order | `sorts=users.count+desc`  
filter fields and values | `f[users.created_year]=2020`  
## How Looker structures JOINs
In the preceding example query, notice that the `orders` Explore appears in the main `FROM` clause and the joined views appear in the `LEFT JOIN` clauses. Looker joins can be written in many different ways, which is explained in more detail on the Working with joins in LookML page.
## SQL blocks specify custom SQL clauses
Not all elements of a Looker query are machine-generated. At some point the data model needs to provide specific detail for Looker to access the underlying tables and compute derived values. In LookML, SQL blocks are snippets of SQL code provided by the data modeler, which Looker uses to synthesize complete SQL expressions.
The most common SQL block parameter is `sql`, used in dimension and measure definitions. The `sql` parameter specifies a SQL clause to reference an underlying column or to perform an aggregate function. In general, all LookML parameters starting with `sql_` expect a SQL expression of some form. For example: `sql_always_where`, `sql_on`, and `sql_table_name`. See the LookML Reference for more information on each parameter.
### Example SQL blocks for dimensions and measures
The following code sample provides are a few examples of SQL blocks for dimensions and measures. The LookML substitution operator ($) makes these `sql` declarations appear deceptively unlike SQL. However, after substitution has occurred, the resulting string is pure SQL, which Looker injects into the `SELECT` clause of the query.
```
dimension: id {
  primary_key: yes
  sql: ${TABLE}.id ;;  # Specify the primary key, id
}
measure: average_cost {
  type: average
  value_format: "0.00"
  sql: ${cost} ;;      # Specify the field that you want to average
                       # The field 'cost' is declared elsewhere
}
dimension: name {
  sql: CONCAT(${first_name}, ' ', ${last_name}) ;;
}
dimension: days_in_inventory {
  type: number
  sql: DATEDIFF(${sold_date}, ${created_date}) ;;
}

```

As shown in the last two dimensions in this example, SQL blocks can use functions that are supported by the underlying database (such as MySQL functions `CONCAT` and `DATEDIFF` in this case). The code you use in SQL blocks must match the SQL dialect used by the database.
### Example SQL block for derived tables
Derived tables also use a SQL block to specify the query that derives the table. This is an example SQL-based derived table:
```
view: user_order_facts {
  derived_table: {
    sql:
      SELECT
        user_id
        , COUNT(*) as lifetime_orders
      FROM orders
      GROUP BY 1 ;;
  }

  # later, dimension declarations reference the derived column(s)…
  dimension: lifetime_orders {
    type: number
  }
}

```

### Example SQL block for filtering an Explore
The `sql_always_where` and `sql_always_having` LookML parameters let you restrict the data available to a query by injecting a SQL block to the SQL WHERE or HAVING clauses. In this example, the LookML substitution operator `${view_name.SQL_TABLE_NAME}` is used to reference a derived table:
```
explore: trips {
  view_label: "Long Trips"
  # This will ensure that we only see trips that are longer than average!
  sql_always_where: ${trips.trip_duration}>=(SELECT tripduration FROM ${average_trip_duration.SQL_TABLE_NAME});;
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


