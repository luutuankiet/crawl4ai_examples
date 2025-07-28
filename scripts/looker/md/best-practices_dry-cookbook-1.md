# Maximizing code reusability with DRY LookML: Define fields once, use substitution operators everywhere  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/dry-cookbook-1

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Example: Referencing the underlying database column only once for a dimension




Send feedback 
#  Maximizing code reusability with DRY LookML: Define fields once, use substitution operators everywhere
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Example: Referencing the underlying database column only once for a dimension


LookML field definitions can change over time. For example, a database column name may change, or you may need to change the definition of a LookML field for other reasons.
If you use the syntax `{TABLE}.field_name` to reference a database column directly in multiple places, you must update each reference manually. Any fields that reference that dimension can break if you forget to update them, and Looker will display an error:
To make your LookML projects more efficient and easier to maintain, you can define fields in one place and use the substitution operator (`$`) to reference those fields everywhere else.
This page provides an example of using the substitution operator (with the syntax `${field_name}`) to reference a single dimension in the definitions of multiple LookML fields.
## Ingredients
  * Substitution operators
  * The LookML `dimension` parameter
  * The LookML `sql` parameter
  * The LookML `sql_table_name` parameter


## Prerequisites
  * A configured LookML model
  * Permissions to develop LookML


## Example: Referencing the underlying database column only once for a dimension
Define a database table column in a LookML project once using the syntax `${TABLE}.field_name` in the dimension's `sql` parameter. Then reference the dimension using the syntax `${field_name}` or `${view_name.field_name}` elsewhere in your project. This lets you maintain the LookML definition of the database column in one place (the original `${TABLE}.field_name` dimension), which is helpful if you need to reference it in multiple places in your project.
As an example, you can use the syntax `${TABLE}.sale_price` to define a base dimension called `sale_price` in a view called `order_items`:
```

  dimension: sale_price {
    type: number
    value_format_name: usd
    sql: ${TABLE}.sale_price ;;
    description: "The price at which an item is set to sell."
  }


```

When you define other fields that reference the `sale_price` dimension, can use the syntax `${sale_price}` within the `order_items` view (or use the syntax `${order_items.sale_price}` to reference the `sale_price` dimension in other views).
```

dimension: profit {
  type: number
  value_format_name: usd
  sql: ${sale_price} - ${inventory_items.cost} ;;
  description: "The difference between an item's sale price and an item's cost."
}

dimension: item_gross_margin {
  type: number
  value_format_name: percent_2
  sql: 1.0 * ${profit}/NULLIF(${sale_price},0) ;;
}

measure: total_sale_price {
  type: sum
  value_format_name: usd
  sql: ${sale_price} ;;
}


```

In this example, if the column name for the dimension `sale_price` changes, you will only need to update the `${TABLE}.sale_price` reference once, in the definition of the base `sale_price` dimension. This change will then propagate automatically to the `profit`, `item_gross_margin`, and `total_sale_price` fields, as well as all other fields that reference the `sale_price` dimension.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


