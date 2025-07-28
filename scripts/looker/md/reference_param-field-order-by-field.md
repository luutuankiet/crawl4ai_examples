# order_by_field  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-order-by-field

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  order_by_field
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: view_name {
  dimension: field_name {
    order_by_field: field_name
  }
}

```

Hierarchy `order_by_field` |  Possible Field Types Dimension, Dimension Group, MeasureAccepts A field name  
---|---  
> Using `order_by_field` incorrectly can cause inconsistent, confusing behavior for users.
## Definition
The `order_by_field` parameter lets you use the sort order from a dimension, dimension group, or measure on another field of the same type, rather than using the default sort order. Fields that are referenced by the `order_by_field` parameter must match the field type of the parent field. A dimension cannot reference a field of `type: measure`, and vice versa.
For example, you have a table that contains both a `status_id` and a `status_name` column. When a user sorts by **Status Name** in the UI, you want the names to appear in the order of the status ID, and not the alphabetical order of the names.
> There should be a 1:1 relationship between a dimension or dimension group and the field referenced by the `order_by_field` parameter, so that the grouping characteristics of both fields are exactly the same. If you do not ensure this, sorting can appear to be random to users.
If there is one and only one `status_id` for each `status_name`, you could write:
```
dimension: status_name {
  sql: ${TABLE}.status_name ;;
  order_by_field: status_id
}

```

With measures, `order_by_field` lets you use the sort order from a measure on another measure.
This can be helpful in cases where you want to sort a non-numeric measure type, such as a `string`, by a numeric measure type.
In this example, a string of cities is ordered by a `count` measure:
```
measure: user_cities {
  type: string
  order_by_field: count
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


