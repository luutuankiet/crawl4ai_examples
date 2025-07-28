# Incorporating SQL and referring to LookML objects  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-and-referring-to-lookml

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Substitution operator ($)
  * Scoping and naming
  * SQL blocks
    * Example SQL blocks for dimensions and measures
    * Example SQL block with a correlated subselect
    * Example SQL block for derived tables
  * LookML field type references
    * Using LookML field type references with date fields
  * LookML constants




Was this helpful?
Send feedback 
#  Incorporating SQL and referring to LookML objects
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Substitution operator ($)
  * Scoping and naming
  * SQL blocks
    * Example SQL blocks for dimensions and measures
    * Example SQL block with a correlated subselect
    * Example SQL block for derived tables
  * LookML field type references
    * Using LookML field type references with date fields
  * LookML constants


To write powerful LookML, you need to be able to reference existing dimensions, measures, views, or derived tables even if they are not in the current scope. You also need to reference columns in the underlying table and use your database dialect's function calls to manipulate those values.
## Substitution operator ($)
The substitution operator, `$`, makes LookML code more reusable and modular, enabling you to reference other views and derived tables, columns in a SQL table, or LookML dimensions and measures. This is good for two reasons. First, you might have already worked out a really tricky dimension or measure, and you won't need to write out all the complexity again. Second, if you change something about a dimension or measure, that change can propagate to everything else that relies on it.
There are several ways that you can use the substitution operator:
`${TABLE}.column_name` references a column in the table that is connected to the view you're working on. For example:
```
dimension: customer_id {
  type: number
  sql: ${TABLE}.customer_id ;;
}

```

`${field_name}` references a dimension or measure within the view you're working on. For example:
```
measure: total_population {
  type: sum
  sql: ${population} ;;
}

```

`${view_name.field_name}` references a dimension or measure from another view. For example:
```
dimension: lifetime_orders {
  type: number
  sql: ${user_order_facts.lifetime_orders} ;;
}

```

`${view_name.SQL_TABLE_NAME}` references another view or derived table. Note that `SQL_TABLE_NAME` in this reference is a literal string; you do not need to replace it with anything. For example:
```
explore: trips {
  view_label: "Long Trips"
  # This will ensure that we only see trips that are longer than average!
  sql_always_where: ${trips.trip_duration}>=(SELECT tripduration FROM ${average_trip_duration.SQL_TABLE_NAME});;
}

```

> `${view_name.SQL_TABLE_NAME}` does not work with the `sql_trigger` parameter used with datagroups.
## Scoping and naming
You can name Explores, views, fields, and sets. These Looker identifiers are written without quotation marks.
LookML fields and sets have _full names_ and _short names_ :
  * Full names are of the form `<view>.<field-name | set-name>`. The left side indicates the scope, which is the view that contains the field or set. The right side specifies the particular field or set name.
  * Short names simply take the form `<field-name | set-name>`, with no separating period. Looker expands short names into full names by using the scope in which they are used.


Following is an example showing many forms of names and scope. This is an unrealistic group of fields, but is shown to demonstrate a variety of possible scoping expressions.
```
view: orders {                   # "orders" becomes the containing scope
  measure: count {               # short name, equivalent to orders.count
    type: count
  }
  dimension: customer_id {       # short name, equivalent to orders.customer_id
    type: number
    sql: ${TABLE}.customer_id ;;
  }
  dimension: customer_address {  # short name, equivalent to orders.customer_address
    sql: ${customer.address} ;;  # full name, references a field defined in the "customer" view
  }
  set: drill_fields {            # short name, equivalent to orders.drill_fields
    fields: [
      count,                     # short name, equivalent to orders.count
      customer.id                # full name, references a field defined in the "customer" view
    ]
  }
}

```

In the `dimension: customer_address` declaration, note that the underlying view for the SQL block (`customer`) is different than the enclosing view scope (`orders`). This can be useful when you need to compare fields between two different views.
When a view (we'll call it "view A") refers to a field defined in a different view (we'll call it "view B"), there are a few things to keep in mind:
  1. The view B file must be included in the same model as view A, using the `include` parameter.
  2. View B must be joined to view A in one or more Explores. See our Working with joins in LookML page to learn about joins.


## SQL dialect
Looker supports many database types, such as MySQL, Postgres, Redshift, BigQuery, and so on. Each database supports a slightly different feature set with differing function names, referred to as the _SQL dialect_.
LookML is designed to work with all SQL dialects, and LookML does not prefer one dialect over the other. However, you will need to include SQL code expressions (known as ) in certain LookML parameters. With these parameters, Looker passes the SQL expression directly to your database, so you must use the SQL dialect that matches your database. For example, if you use a SQL function, it must be a function that your database supports.
## SQL blocks
Some LookML parameters require you to provide raw SQL expressions so that Looker can understand how to retrieve data from your database.
LookML parameters starting with `sql_` expect a SQL expression of some form. Examples are: `sql_always_where`, `sql_on`, and `sql_table_name`. The most common LookML parameter for SQL blocks is `sql`, used in dimension and measure field definitions to specify the SQL expression that defines the dimension or measure.
The code you specify in a SQL block can be as simple as a single field name or as complex as a correlated subselect. The content can be quite complex, accommodating almost any need you might have to express custom query logic in raw SQL. Note that the code you use in SQL blocks must match the SQL dialect used by the database.
### Example SQL blocks for dimensions and measures
Following are examples of SQL blocks for dimensions and measures. The LookML substitution operator ($) can make these `sql` declarations appear deceptively unlike SQL. However, after substitution has occurred, the resulting string is pure SQL, which Looker injects into the `SELECT` clause of the query.
```
dimension: id {
  primary_key: yes
  sql: ${TABLE}.id ;;   # Specify the primary key, id
}
measure: average_cost {
  type: average
  value_format: "0.00"
  sql: ${order_items.cost} ;;   # Specify the field that you want to average
}
dimension: name {
  sql: CONCAT(${first_name}, ' ', ${last_name}) ;;
}
dimension: days_in_inventory {
  type: int
  sql: DATEDIFF(${sold_date}, ${created_date}) ;;
}

```

As shown in the last two dimensions, SQL blocks can use functions supported by the underlying database (such as the MySQL functions `CONCAT` and `DATEDIFF` in this example).
### Example SQL block with a correlated subselect
You can place any SQL statement in a field's SQL block, including a correlated subselect. The following is an example:
```
view: customers {
  dimension: id {
    primary_key: yes
    sql: ${TABLE}.id ;;
  }
  dimension: first_order_id {
    sql: (SELECT MIN(id) FROM orders o WHERE o.customer_id=customers.id) ;;
         # correlated subselect to derive the value for "first_order_id"
  }
}

```

### Example SQL block for derived tables
Derived tables use the SQL block to specify the query that derives the table. The following is an example:
```
view: user_order_facts {
  derived_table: {
    sql:            # Get the number of orders for each user
      SELECT
        user_id
        , COUNT(*) as lifetime_orders
      FROM orders
      GROUP BY 1 ;;
  }
  # later, dimension declarations reference the derived column(s)

  dimension: lifetime_orders {
    type: number
  }
}

```

## LookML field type references
When you reference an existing LookML field within another field, you can instruct Looker to treat the referenced field as a specific data type by using a double colon (`::`) followed by the desired type. For example, if you reference the `orders.created_date` dimension within another field, you can use the syntax `${orders.created_date::date}` to ensure that the `created_date` field will be treated as a date field in the SQL that Looker generates, rather than being cast as a string.
The data type you can use in a reference depends on the data type of the original field you are referencing. For example, if you are referencing a string field, the only data type you can specify is `::string`. Here is the full list of allowed field type references you can use for each type of field:
  * In a reference to a string field, you can use `::string`.
  * In a reference to a number field, you can use `::string` and `::number`.
  * In a reference to a date or time field, you can use `::string`, `::date`, and `::datetime`.`::string` and `::date` return data in the query time zone, while references using `::datetime` return data in the database time zone.
  * In a reference to a yesno field, you can use `::string`, `::number`, and `::boolean`. `::boolean` type are not available for database dialects that do not support the Boolean data type.
  * In a reference to a location field, you can use `::latitude` and `::longitude`.


### Using LookML field type references with date fields
As an example, suppose you have an `enrollment_month` dimension and a `graduation_month` dimension, both of which were created within dimension groups of `type: time`. In this example, the `enrollment_month` dimension is produced by the following dimension group of `type: time`:
```

dimension_group: enrollment {
  type: time
  timeframes: [time, date, week, month, year, raw]
  sql: ${TABLE}.enrollment_date ;;
}


```

Similarly, the `graduation_month` dimension is created by the following dimension group of `type: time`:
```

dimension_group: graduation {
  type: time
  timeframes: [time, date, week, month, year, raw]
  sql: ${TABLE}.graduation_date ;;
}


```

Using the `enrollment_month` and `graduation_month` dimensions, you can calculate how many months or years passed between a student's enrollment and graduation by creating a dimension group of `type: duration`. However, because some date fields are cast as strings in the SQL that Looker generates, setting the `enrollment_month` and `graduation_month` dimensions as the values for `sql_start` and `sql_end` can result in an error.
To avoid an error resulting from these time fields being cast as strings, one option is to create a dimension group of `type: duration`, referencing the `raw` timeframes from the `enrollment` and `graduation` dimension groups in the `sql_start` and `sql_end` parameters:
```

dimension_group: enrolled {
  type: duration
  intervals: [month, year]
  sql_start: ${enrollment_raw} ;;
  sql_end: ${graduation_raw} ;;
}


```

In the Explore UI, this generates a dimension group called **Duration Enrolled** , with individual dimensions **Months Enrolled** and **Years Enrolled**.
A simpler alternative to using the `raw` timeframe in a dimension group of `type: duration` is to specify the `::date` or `::datetime` reference type for the fields referenced in the `sql_start` and `sql_end` parameters.
```

dimension_group: enrolled {
  type: duration
  intervals: [month, year]
  sql_start: ${enrollment_month::date} ;;
  sql_end: ${graduation_month::date} ;;
}


```

The LookML in this example also creates a **Duration Enrolled** dimension group, but using the `::date` reference allows the `enrollment_month` and `graduation_month` dimensions to be used without using a `raw` timeframe or casting them as strings with SQL.
For an additional example of how LookML field type references can be used to create custom dimension groups of `type: duration`, see the `dimension_group` parameter documentation page.
> This syntax is not available with measures of `type: list`, which cannot be referenced as of Looker 6.8.
## LookML constants
The `constant` parameter lets you specify a constant you can use throughout a LookML project. With LookML constants, you can define a value once and reference it in any part of your project where strings are accepted, thus reducing repetition in your LookML code.
Constants must be declared within a project manifest file, and the value for a constant must be a string. For example, you can define a constant `city` with the value `"Okayama"` as follows:
```
constant: city {
  value: "Okayama"
}


```

The `city` constant can then be referenced throughout your project using the syntax `@{city}`. For example, you can use the `city` constant with the `label` parameter in the `users` Explore:
```

explore: users {
  label: "@{city} Users"
}


```

Looker then displays **Okayama Users** in both the **Explore** menu and in the title of the Explore, rather than the default **Users**.
For more information and examples of how you can use LookML constants to write reusable code, see the `constant` parameter documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


