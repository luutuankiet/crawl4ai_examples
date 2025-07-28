# Creating native derived tables  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/creating-ndts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Using an Explore to begin defining your native derived tables
  * Defining a native derived table in LookML
  * Using include statements to enable referencing fields
  * Defining native derived table columns
    * Specifying the column names
    * Implied column names
    * Creating derived columns for calculated values
  * Adding filters to a native derived table
    * Using templated filters
  * Sorting and limiting native derived tables
  * Converting native derived tables to different time zones




Was this helpful?
Send feedback 
#  Creating native derived tables
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using an Explore to begin defining your native derived tables
  * Defining a native derived table in LookML
  * Using include statements to enable referencing fields
  * Defining native derived table columns
    * Specifying the column names
    * Implied column names
    * Creating derived columns for calculated values
  * Adding filters to a native derived table
    * Using templated filters
  * Sorting and limiting native derived tables
  * Converting native derived tables to different time zones


A derived table is a query whose results are used as if the derived table were a physical table in the database. A _native derived table_ is based on a query that you define using LookML terms. This is different from a _SQL-based derived table_, which is based on a query that you define with SQL terms. Compared to SQL-based derived tables, native derived tables are much easier to read and understand as you model your data. See the Native derived tables and SQL-based derived tables section of the Derived tables in Looker documentation page for more information.
Both native and SQL-based derived tables are defined in LookML using the `derived_table` parameter at the view level. However, with native derived tables, you do not need to create a SQL query. Instead, you use the `explore_source` parameter to specify the Explore on which to base the derived table, the desired columns, and other desired characteristics.
> You can also have Looker create the derived table LookML from a SQL Runner query, as described on the Using SQL Runner to create derived tables documentation page.
## Using an Explore to begin defining your native derived tables
Starting with an Explore, Looker can generate LookML for all or most of your derived table. Just create an Explore and select all the fields you want to include in your derived table. Then, to generate the native derived table LookML, follow these steps:
  1. Select the **Explore Actions** gear menu and select **Get LookML**.
  2. Click the **Derived Table** tab to see the LookML for creating a native derived table for the Explore.
  3. Copy the LookML.


Now that you have copied the generated LookML, paste it into a view file:
  1. In Development Mode, navigate to your project files.
  2. Click the **+** at the top of the project file list in the Looker IDE and select **Create View**. Alternatively, you can click a folder's menu and select **Create View** from the menu to create the file inside the folder.
  3. Set the view name to something meaningful.
  4. Optionally, change column names, specify derived columns, and add filters.


> When you use a measure of `type: count` in an Explore, the visualization labels the resulting values with the view name rather than the word _Count_. To avoid confusion, pluralize your view name. You can change the view name by either selecting **Show Full Field Name** under **Series** in the visualization settings or by using the `view_label` parameter with a pluralized version of your view name.
## Defining a native derived table in LookML
Whether you use derived tables declared in SQL or native LookML, the output of a `derived_table`'s query is a table with a set of columns. When the derived table is expressed in SQL, the output column names are implied by the SQL query. For example, the following SQL query will have the output columns `user_id`, `lifetime_number_of_orders`, and `lifetime_customer_value`:
```
SELECT
user_id
,COUNT(DISTINCTorder_id)aslifetime_number_of_orders
,SUM(sale_price)aslifetime_customer_value
FROMorder_items
GROUPBY1

```

In Looker, a query is based on an Explore, includes measure and dimension fields, adds any applicable filters, and may also specify a sort order. A native derived table contains all these elements plus the output names for the columns.
The following simple example produces a derived table with three columns: `user_id`, `lifetime_customer_value`, and `lifetime_number_of_orders`. You don't need to manually write the query in SQL — instead, Looker creates the query for you by using the specified Explore `order_items` and some of that Explore's fields (`order_items.user_id`, `order_items.total_revenue`, and `order_items.order_count`).
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

## Using `include` statements to enable referencing fields
In the native derived table's view file, you use the `explore_source` parameter to point to an Explore and to define the columns and other characteristics for the native derived table.
In the native derived table's view file, you're not required to use the `include` parameter to point to the file that contains the Explore's definition. If you don't have the `include` statement, the Looker IDE won't autosuggest field names or verify your field references as you build the native derived table. Instead, you can use the LookML Validator to verify the fields that you are referencing in your native derived table.
However, if you want to enable the autosuggest and immediate field verification in the Looker IDE, or if you have a complex LookML project that has multiple Explores of the same name or potential for circular references, you can use the `include` parameter to point to the location of the Explore's definition.
Explores are often defined within a model file, but, in the case of native derived tables, it's cleaner to create a separate file for the Explore. LookML Explore files have the `.explore.lkml` file extension, as described in the documentation for Creating Explore Files. That way, in your native derived table view file you can include a single Explore file and not the entire model file.
If you do want to create a separate Explore file and use the `include` parameter to point to the Explore file in your native derived table's view file, make sure that your LookML files meet the following requirements:
  * The native derived table's view file should include the Explore's file. For example: 
    * `include: "/explores/order_items.explore.lkml"`
  * The Explore's file should include the view files that it needs. For example: 
    * `include: "/views/order_items.view.lkml"`
    * `include: "/views/users.view.lkml"`
  * The model should include the Explore's file. For example: 
    * `include: "/explores/order_items.explore.lkml"`


## Defining native derived table columns
As shown in the preceding example, you use `column` to specify the output columns of the derived table.
### Specifying the column names
For the `user_id` column, the column name matches the name of the specified field in the original Explore.
Frequently, you will want a different column name in the output table than the name of the fields in the original Explore. The preceding example produced a lifetime value calculation by user using the `order_items` Explore. In the output table, `total_revenue` is really a customer's `lifetime_customer_value`.
The `column` declaration supports declaring an output name that is different from the input field. For example, the following code instructs Looker to "make an output column named `lifetime_value` from field `order_items.total_revenue`":
```
column: lifetime_value {
  field: order_items.total_revenue
}

```

### Implied column names
If the `field` parameter is left out of a column declaration, it is assumed to be `<explore_name>.<field_name>`. For example, if you have specified `explore_source: order_items`, then
```
column: user_id {
  field: order_items.user_id
}

```

is equivalent to
```
column: user_id {}

```

### Creating derived columns for calculated values
You can add `derived_column` parameters to specify columns that don't exist in the `explore_source` parameter's Explore. Each `derived_column` parameter has a `sql` parameter specifying how to construct the value.
Your `sql` calculation can use any columns that you have specified using `column` parameters. Derived columns cannot include aggregate functions, but they can include calculations that can be performed on a single row of the table.
The following example produces the same derived table as the earlier example, except that it adds a calculated `average_customer_order` column, which is calculated from the `lifetime_customer_value` and `lifetime_number_of_orders` columns in the native derived table.
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
      derived_column: average_customer_order {
        sql:  lifetime_customer_value / lifetime_number_of_orders ;;
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
  dimension: average_customer_order {
    type: number
  }
}

```

#### Using SQL window functions
Some database dialects support window functions, especially to create sequence numbers, primary keys, running and cumulative totals, and other useful multi-row calculations. After the primary query has been executed, any `derived_column` declarations are executed in a separate pass.
If your database dialect supports window functions, then you can use them in your native derived table. Create a `derived_column` parameter with a `sql` parameter that contain the desired window function. When referring to values, you should use the column name as defined in your native derived table.
The following example creates a native derived table that includes the `user_id`, `order_id`, and `created_time` columns. Then, using a derived column with a `SQL ROW_NUMBER()` window function, it calculates a column that contains the sequence number of a customer's order.
```
view: user_order_sequences {
  derived_table: {
    explore_source: order_items {
      column: user_id {
        field: order_items.user_id
      }
      column: order_id {
        field: order_items.order_id
      }
      column: created_time {
        field: order_items.created_time
      }
      derived_column: user_sequence {
        sql: ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_time) ;;
      }
    }
  }
  dimension: order_id {
    hidden: yes
  }
  dimension: user_sequence {
    type: number
  }
}

```

## Adding filters to a native derived table
Suppose you wanted to build a derived table of a customer's value over the past 90 days. You want the same calculations as you performed in the previous example, but you only want to include purchases from the last 90 days.
You would just add a filter to the `derived_table` that filters for transactions in the last 90 days. The `filters` parameter for a derived table uses the same syntax as you use to create a filtered measure.
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

Filters will be added to the `WHERE` clause when Looker writes the SQL for the derived table.
In addition, you can use the `dev_filters` subparameter of `explore_source` with a native derived table. The `dev_filters` parameter lets you specify filters that Looker applies only to development versions of the derived table, which means that you can build smaller, filtered versions of the table to iterate and test without waiting for the full table to build after each change.
The `dev_filters` parameter acts in conjunction with the `filters` parameter so that all filters are applied to the development version of the table. If both `dev_filters` and `filters` specify filters for the same column, `dev_filters` takes precedence for the development version of the table.
See Working faster in Development Mode for more information.
### Using templated filters
You can use `bind_filters` to include templated filters:
```
bind_filters: {
  to_field: users.created_date
  from_field: filtered_lookml_dt.filter_date
}

```

This is essentially the same as using the following code in a `sql` block:
```
{% condition filtered_lookml_dt.filter_date %} users.created_date {% endcondition %}

```

The `to_field` is the field to which the filter is applied. The `to_field` must be a field from the underlying `explore_source`.
The `from_field` specifies the field from which to get the filter, if there is a filter at runtime.
In the preceding `bind_filters` example, Looker will take any filter applied to the `filtered_lookml_dt.filter_date` field and apply the filter to the `users.created_date` field.
You can also use the `bind_all_filters` subparameter of `explore_source` to pass all runtime filters from an Explore to a native derived table subquery. See the `explore_source` parameter documentation page for more information.
## Sorting and limiting native derived tables
You can also sort and limit the derived tables, if desired:
```
sorts: [order_items.count: desc]
limit: 10

```

Remember, an Explore may display the rows in a different order than the underlying sort.
## Converting native derived tables to different time zones
You can specify the time zone for your native derived table using the `timezone` subparameter:
```
timezone: "America/Los_Angeles"

```

When you use the `timezone` subparameter, all time-based data in the native derived table will be converted to the time zone you specify. See the `timezone` values documentation page for a list of the supported time zones.
If you don't specify a time zone in your native derived table definition, the native derived table will not perform any time zone conversion on time-based data, and instead time-based data will default to your database time zone.
If the native derived table is not persistent, you can set the time zone value to `"query_timezone"` to automatically use the time zone of the currently running query.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


