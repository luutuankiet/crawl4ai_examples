# explore_source  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-explore-source

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Defining a native derived table
  * Creating filters for Development Mode
  * Passing filters into a native derived table
    * Using bind_all_filters
    * Using bind_filters
  * Things to consider
    * Use only one explore_source parameter
    * Use include statements to enable referencing fields




Was this helpful?
Send feedback 
#  explore_source
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Defining a native derived table
  * Creating filters for Development Mode
  * Passing filters into a native derived table
    * Using bind_all_filters
    * Using bind_filters
  * Things to consider
    * Use only one explore_source parameter
    * Use include statements to enable referencing fields


> This page refers to the `explore_source` parameter that is a subparameter of `derived_table`.
> `explore_source` can also be a subparameter of `test`, described on the `test` parameter documentation page.
## Usage
```
derived_table: customer_order_facts {
  explore_source:  orders {
    column:  customer_id {
      field:  orders.customer_id
    }
    column:  order_amount {
      field:  orders.sale_price
    }
    column:  item_qty {
      field:  orders.number_items
    }
    derived_column:  average_item_priceorder_amount / item_qty  ;;
    }
    timezone:  "America/Los_Angeles"
  }
}

```

Hierarchy `explore_source` |  Default Value NoneAccepts The identifier of the Explore from which the native derived table is derived, plus subparameters defining the native derived table.   
---|---  
## Definition
There are two ways to make a derived table, which you can use as if it were a normal table in your database — native derived tables, which are defined using LookML parameters, and SQL-based derived tables, which are defined using SQL query statements.
The `explore_source` parameter is used for native derived tables. In this parameter you define which columns will be included in a native derived table, any filters to be applied to the native derived table, whether to limit or sort the native derived table rows, and whether to convert the native derived table's time-based fields to a different time zone.
## Defining a native derived table
You can use a variety of parameters in a native derived table, many of which are optional. The syntax for defining a native derived table is as follows:
```
explore_source: identifier {
  bind_all_filters: yes
  column: identifier {
    field: field_name
  }
  derived_column: identifier {
    sql: SQL expression ;;
  }
  expression_custom_filter: [custom filter expression]
  filters: [field_name_1: "string", field_name_2: "string", ...]
  limit: number
  sorts: [field_name_1: asc | desc, field_name_2: asc | desc, ...]
  timezone: "string"
}

```

The following table provides information about each parameter that you can use to define a native derived table:
Parameter Name | Description | Example  
---|---|---  
`bind_filters` |  Passes a filter from the Explore query into the native derived table subquery. To set up this parameter, use the `from_field` subparameter to specify a field defined in the native derived table view or accessible in the Explore to which the native derived table is joined. At runtime, any filters on the `from_field` in the Explore will be passed into the `to_field` in the native derived table subquery. See the Using `bind_filters` section for an example. `bind_filters`, note the following: 
  * The runtime filter must be in a view joined to the same Explore as the native derived table.
  * The native derived table cannot be made into a persistent derived table (PDT).

**•** The `explore_source` parameter can have the `bind_all_filters` subparameter _or_ the `bind_filters` subparameter, but not both.  | ```
bind_filters: {
  to_field: users.created_date
  from_field: user_dt.filter_date
}
```
  
`bind_all_filters` | Passes all filters from the Explore query into the native derived table subquery. To set up this parameter, specify `bind_all_filters: yes` in the `explore_source` of the native derived table. See the Using `bind_filters` section for an example. `bind_all_filters: yes`, note the following: 
  * The runtime filter must be in a view joined to the same Explore as the native derived table.
  * The native derived table cannot be made in to a PDT.
  * The native derived table can be joined only into the Explore specified in the native derived table's `explore_source` parameter. This is because `bind_all_filters` needs to map the Explore's filtered fields to the fields in the native derived table.
  * The `explore_source` parameter can have the `bind_all_filters` subparameter _or_ the `bind_filters` subparameter, but not both.

| `bind_all_filters: yes`  
`column` | Specifies a column to include in the `explore_source`. Has a `field` subparameter. | ```
column: cust_id {
  field: orders.customer_id
}
```
  
`derived_column` | Specifies a column in the `explore_source` with an expression in the namespace of the inner columns. Aggregate SQL expressions won't work here, since there is no SQL grouping at this step. SQL window functions can be very useful in this parameter. Has a `sql` subparameter. | ```
derived_column: average_order {
  sql: order_amount / item_qty ;;
}
```
  
`dev_filters` |  Added 21.12  Specifies filters that Looker applies only to development versions of the derived table. This is useful for LookML developers when they test derived tables in Development Mode. The `dev_filters` parameter lets Looker build smaller, filtered versions of the table so that a LookML developer can iterate and test the table without waiting for the full table to build after each change. Looker applies the `dev_filters` only to the development versions of the derived table, not to the production version of the table that is queried by your users. See the Derived tables in Looker documentation page for more information on working with derived tables in Development Mode and the Creating filters for Development Mode section on this page for an example. | `dev_filters: [orders.created_date: "90 days", orders.products: "sweaters"]`  
`expression_custom_filter` | Optionally specifies a custom filter expression on an `explore_source` query. | `expression_custom_filter: ${orders.status} = "pending" ;;`  
`filters` |  Optionally adds a filter to an `explore_source` query. Enclose in square brackets; include the field name to filter, using `view_name.field_name` format, followed by `:` and the value(s) on which the field should be filtered. Filters are added to the `WHERE` clause of the SQL generated by the native derived table. | `filters: [products.department: "sweaters"]`  
`limit` |  Optionally, specifies the row limit of the query. | `limit: 10`  
`sorts` |  Optionally, specifies a sort for this `explore_source`. Enclose in square brackets; include the field name to sort, using `view_name.field_name` format, followed by `:` and `asc` or `desc` to indicate whether the field should be sorted in ascending or descending. You can sort on multiple fields by adding multiple field name and keyword pairs separated by commas. | `sorts: [products.brand: asc, products.name: asc]`  
`timezone` |  Sets the time zone for the `explore_source` query. For non-persistent derived tables, set the time zone to `"query_timezone"` to automatically use the time zone of the currently running query. If a time zone is not specified, the `explore_source` query won't perform any time zone conversion but will use the database time zone instead. See the `timezone` values page for a list of the supported time zones.autosuggests the time zone value when you type the `timezone` parameter in the IDE. The IDE also displays the list of supported time zone values in the Quick Help panel. | `timezone: "America/Los_Angeles"`  
## Examples
The following definitions provide basic examples of native derived tables.
Create a `user_order_facts` native derived table:
```
view: user_order_facts {
  derived_table: {
    explore_source: order_items {
      column: user_id {
        field: order_items.user_id
      }
      column: lifetime_number_of_orders {
        field: order_items.order_count
      }
      column: lifetime_customer_value {
        field: order_items.total_revenue
      }
    }
  }
  # Define the view's fields as desired
  dimension: user_id {
    hidden: yes
  }
  dimension: lifetime_number_of_orders {
    type: number
  }
  dimension: lifetime_customer_value {
    type: number
  }
}

```

You can add filters to create a `user_90_day_facts` native derived table:
```
view: user_90_day_facts {
  derived_table: {
    explore_source: order_items {
      column: user_id {
        field: order_items.user_id
      }
      column: number_of_orders_90_day {
        field: order_items.order_count
      }
      column: customer_value_90_day {
        field: order_items.total_revenue
      }
      filters: [order_items.created_date: "90 days"]
    }
  }
  # Add define view's fields as desired
  dimension: user_id {
    hidden: yes
  }
  dimension: number_of_orders_90_day {
    type: number
  }
  dimension: customer_value_90_day {
    type: number
  }
}

```

## Creating filters for Development Mode
There are situations when the native derived table you're creating takes a long time to generate, which can be time-consuming if you are testing lots of changes in Development Mode. For these cases, you can use `dev_filters` to create smaller development versions of a native derived table:
```
view: e_faa_pdt {
  derived_table: {
  ...
    datagroup_trigger: e_faa_shared_datagroup
    explore_source: flights {
      dev_filters: [flights.event_date: "90 days"]
      filters: [flights.event_date: "2 years", flights.airport_name: "Yucca Valley Airport"]
      column: id {}
      column: airport_name {}
      column: event_date {}
    }
  }
...
}

```

This example includes a `dev_filters` parameter that filters the data to the last 90 days and a `filters` parameter that filters the data to the last 2 years and to the Yucca Valley Airport. The `dev_filters` parameter acts in conjunction with the `filters` parameter so that all filters are applied to the development version of the table. If both `dev_filters` and `filters` specify filters for the same column, the `dev_filters` take precedence for the development version of the table. In this example, the development version of the table will filter the data to the last 90 days for the Yucca Valley Airport.
> If a native derived table has the `dev_filters` parameter, the development table cannot be used as the production version, since the development version has an abbreviated dataset. If this is the case, after you've finished developing the table and before you deploy your changes, you can comment out the `dev_filters` parameter and then query the table in Development Mode. Looker will then build a full version of the table that can be used for production when you deploy your changes. See the Derived tables in Looker documentation page for more details about using development tables in production. 
> `dev_filters` parameter and you query it in Development Mode, Looker _can_ use the production table to answer your Development Mode query. This statement is true unless you change the definition of the table and then query the table in Development Mode, at which point Looker will build a development table to answer the query.
## Passing filters into a native derived table
When you include a native derived table in an Explore, you can take runtime filters from the Explore and apply them to the native derived table query. You do this by adding either the `bind_all_filters` or the `bind_filters` parameter to the `explore_source` of the native derived table.
When passing runtime filters from an Explore to a native derived table subquery, the runtime filter must be in a view joined to the same Explore as the native derived table. Also, because the native derived table must regenerate at runtime in order to incorporate the runtime filters from the Explore, the native derived table can't be a persistent derived table (PDT).
### Using `bind_all_filters`
The easiest way to pass filters from an Explore to a native derived table subquery is to specify `bind_all_filters: yes` in the native derived table's `explore_source` parameter. This will pass _all_ of an Explore's runtime filters into the native derived table subquery.
A native derived table with `bind_all_filters: yes` must be joined into the same Explore that is specified in the native derived table's `explore_source` parameter. If you want to use the native derived table in a different Explore, use the `bind_filters` parameter instead, as described in the Using `bind_filters` section.
Here is the LookML for a native derived table with `bind_all_filters: yes`:
```

view: top_10_simple_item_names {
  view_label: "Top 10s"
  derived_table: {
    explore_source: order_items {
      column: total_sale_price {
        field: order_items.total_sale_price
      }
      column: item_name {
        field: products.item_name
      }
      derived_column: rank {
        sql: RANK() OVER (ORDER BY total_sale_price DESC) ;;
      }
      bind_all_filters: yes
      sorts: [order_items.total_sale_price: desc]
      timezone: "query_timezone"
      limit: 10
    }
  }
  dimension: item_name {
    group_label: "Simple Example"
  }
  dimension: rank {
    type: number
    group_label: "Simple Example"
  }
  dimension: item_name_ranked {
    group_label: "Simple Example"
    order_by_field: rank
    type: string
    sql: ${rank} || ') ' || ${item_name} ;;
  }
}

```

In the native derived table's view, the `explore_source` is `order_items`. The following is the LookML for the `order_items` Explore where the native derived table is joined into the Explore:
```
explore: order_items {
  ...
  join: top_10_simple_item_names {
    type: inner
    relationship: many_to_one
    sql_on: ${products.item_name} = ${top_10_simple_item_names.item_name} ;;
  }
}

```

To see this example in action, check out the [Analytic Block] – Pivot by Top X – Introducing `bind_all_filters: yes` Community post.
### Using `bind_filters`
The `bind_filters` subparameter of `explore_source` passes a specific filter from the Explore query into the native derived table subquery:
  * The `to_field` is the field in the native derived table to which the filter is applied. The `to_field` must be a field from the underlying `explore_source`.
  * The `from_field` specifies the field in the Explore from which to get the filter, if the user specifies a filter at runtime.


At runtime, any filters on the `from_field` in the Explore will be passed into the `to_field` in the native derived table subquery.
The following LookML shows a native derived table with `bind_filters`. With this setup, Looker will take any filter that is applied to the `filtered_lookml_dt.filter_date` field in the Explore and apply the filter to the `users.created_date` field in the native derived table.
```
derived_table: {
  explore_source: order_items {
    bind_filters: {
      to_field: users.created_date
      from_field: filtered_lookml_dt.filter_date
    . . .
    }
  }
}

```

## Things to consider
### Use only one `explore_source` parameter
Each native derived table accepts only one `explore_source` parameter. Subsequent `explore_source` parameters won't raise LookML validation errors, but they will override previous `explore_source` parameters.
To create columns from fields in different views, first join together the different views in the same Explore. Then use that Explore for `explore_source`.
### Use `include` statements to enable referencing fields
When creating a native derived table, you must include the file containing the Explore's definition. The best way to do that is to define the Explore in a separate Explore file, as described in the documentation for Creating Explore Files.
If you create a separate Explore file:
  * The native derived table's view file should include the Explore's file. For example:
    * `include: "/explores/order_items.explore.lkml"`
  * The Explore's file should include the view files that it needs. For example:
    * `include: "/views/order_items.view.lkml"`
    * `include: "/views/users.view.lkml"`
  * The model should include the Explore's file. For example:
    * `include: "/explores/order_items.explore.lkml"`


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


