# measure  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-measure

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Subparameters for measure
  * Things to know
    * Measures in joined views
    * Measures based on other measures




Was this helpful?
Send feedback 
#  measure
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Subparameters for measure
  * Things to know
    * Measures in joined views
    * Measures based on other measures


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: view_name {
  measure:  field_name { ... }
}

```

Hierarchy `measure` |  Accepts A Looker identifier to name the measure  
---|---  
## Definition
The `measure` parameter declares a new measure (aggregation) and specifies a name for that measure.
There are several criteria for a measure's name:
  * It must be unique within any given view.
  * It must consist of characters `a` through `z` (no capital letters), `0` through `9`, or `_`.
  * It must start with a letter.


There are many types of measures, as discussed further on the Measure types documentation page.
## Subparameters for `measure`
See the Field parameters reference page for a list of subparameters that are available for LookML fields.
## Examples
Create measures named `product_count` and `total_value` in a view named `products`:
```
view: products {
  measure: product_count {
    type: count
  }
  measure: total_value {
    sql: ${value} ;;
    type: sum
  }
}

```

## Things to know
### Measures in joined views
To have measures (aggregations) come through joins, you must define primary keys in all the views that are involved in the join.
You can do this by adding the `primary_key` parameter to the primary key field definition in each view:
```
dimension: id {
  type: number
  primary_key: yes
}

```

> To correctly handle joined measures, Looker relies on you specifying a primary key where the values are completely unique, non-NULL values. If your data does not contain a primary key, consider whether the concatenation of several fields would result in a primary key of completely unique, non-NULL values. If your primary key is not unique or contains NULL values and your query includes data that reveals those issues, then Looker returns an error as described in the Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum Best Practices page.
### Measures based on other measures
It is possible to define a measure that is based on another measure. The new measure must be of `type: number` to avoid nested-aggregation errors. See the documentation on `type: number` for measures for an example and explanation.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


