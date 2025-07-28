# filter  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-filter

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Subparameters for filter
  * Examples
    * Creating a user-specified filter
    * Defining a dynamic derived table with a templated filter
    * Using the sql parameter with filter
    * Using filter to define a dynamic derived table and a user-defined filter
    * Using filter to filter by a hidden field




Was this helpful?
Send feedback 
#  filter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Subparameters for filter
  * Examples
    * Creating a user-specified filter
    * Defining a dynamic derived table with a templated filter
    * Using the sql parameter with filter
    * Using filter to define a dynamic derived table and a user-defined filter
    * Using filter to filter by a hidden field


## Usage
```
view: view_name {
  filter: filter_name { ... }
}

```

Hierarchy `filter` |  Default Value NoneAccepts A Looker identifier to name the filterSpecial Rules Filter names may not be shared with any other filter, `dimension`, or `measure` within the same `view`  
---|---  
## Definition
The `filter` parameter declares a filter-only field and a name for that filter. A user can add filter-only fields as filters when exploring, but they cannot add them to their result set. These filter-only fields are made useful using templated filters, which are an advanced LookML topic. You can also refer to the Using `filter` to filter by a hidden field example.
The filter name must:
  * Be unique within any given view
  * Consist of characters `a` through `z` (no capital letters), `0` through `9`, or `_`
  * Start with a letter


There are many types of filter fields, as discussed further on the Dimension, filter, and parameter types documentation page.
## Subparameters for `filter`
See the Field parameters reference page for a list of subparameters that are available for LookML fields.
## Examples
Here are some examples for using the `filter` parameter.
### Creating a user-specified filter
Create a filter that lets the user specify the `order_region`:
```
filter: order_region {
  type: string
}

```

### Defining a dynamic derived table with a templated filter
As shown on the Templated filters and Liquid parameters documentation page, define a derived table to calculate the lifetime spending for customers in a region that is specified by the user. This example uses the `filter` created in the previous example as part of a templated filter. The `filter` input is used in the `WHERE` clause with Liquid variables:
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        SUM(sale_price) AS lifetime_spend
      FROM
        order
      WHERE
        {% condition order_region %} order.region {% endcondition %}
      GROUP BY 1
    ;;
  }

  filter: order_region {
    type: string
  }
}

```

### Using the `sql` parameter with `filter`
You can also use the `sql` parameter with `filter`, which applies to the SQL `WHERE` clause whenever the filter has a value. This allows for a dynamic `WHERE` clause, based on the user filter input.
The following example creates a filter that allows only user names that exist in the dataset:
```
filter: user_enabled {
  type: string
  suggest_dimension: user_name
  sql: EXISTS (SELECT user_id FROM users WHERE {% condition %} user_name {% endcondition %} and state = 'enabled') ;;
}

```

In the previous example, if the complete list of user names in the dataset is "Zach", "Erin", and "Brett", the filter results in the following `WHERE` clause:
```
WHEREEXISTS(SELECTuser_idFROMusersWHEREuser_namein('Zach','Erin','Brett')andstate='enabled')

```

See the Using `filter` to filter by a hidden field section on this page for an example of how to use the `sql` parameter with `filter`.
### Using `filter` to define a dynamic derived table and a user-defined filter
Using the earlier example that defines a derived table with a dynamic region value, you can use the `sql` parameter with a templated filter to dynamically build a `WHERE` clause that applies to both the derived table and the main Looker-generated query:
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        SUM(sale_price) AS lifetime_spend
      FROM
        order
      WHERE
        {% condition order_region %} order.region {% endcondition %}
      GROUP BY 1
    ;;
  }
  filter: order_region {
    type: string
    sql: {% condition order_region %} ${region} {% endcondition %} ;;
  }
  dimension: region {
    type: string
    sql: ${TABLE}.region ;;
  }

```

In the previous example, the user provides input to the filter `order_region`, which in turn provides the value to the `region` dimension. The `region` dimension then provides the value of the `WHERE` clause in the derived table SQL and, because of the `sql` parameter in the `filter` definition, the value for the `WHERE` clause in a Looker-generated query.
### Using `filter` to filter by a hidden field
You can use `filter` to create a dimension that users can filter on, while also preventing users from selecting the dimension in a query.
  1. First, hide the dimension in question using `hidden: yes`. This means that the dimension won't be available for users to select from an Explore field picker.
```
  dimension: field_to_hide {
    type: string
    hidden: yes
    sql: ${TABLE}.field_to_hide ;;
  }

```

  2. Now, make a `filter` field to link to the `field_to_hide` dimension.
```
filter: filter_on_field_to_hide {
  type: string
  sql: {% condition filter_on_field_to_hide %} ${field_to_hide} {% endcondition %} ;;
}

```



As discussed in the Using the `sql` parameter with `filter` example, the `sql` parameter of the `filter` field applies SQL directly to the `WHERE` clause of the query. In this case, the `sql` takes the filter condition specified in the `filter_on_field_to_hide` filter and applies it to the `${field_to_hide}` dimension.
This way, users can filter a query by `field_to_hide` with the `filter_on_field_to_hide` filter, while the `field_to_hide` dimension remains hidden.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


