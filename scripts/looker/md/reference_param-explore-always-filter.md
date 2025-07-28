# always_filter  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-always-filter

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * Users can't remove a filter specified by always_filter
    * Setting a blank default value
    * The always_filter parameter overrides a default_value filter setting
  * Things to know
    * always_filter affects existing Looks and dashboard tiles
    * If you want filters that users can't change, consider sql_always_where
    * If you want user-specific filters that users can't change, consider access_filter




Was this helpful?
Send feedback 
#  always_filter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Common challenges
    * Users can't remove a filter specified by always_filter
    * Setting a blank default value
    * The always_filter parameter overrides a default_value filter setting
  * Things to know
    * always_filter affects existing Looks and dashboard tiles
    * If you want filters that users can't change, consider sql_always_where
    * If you want user-specific filters that users can't change, consider access_filter


## Usage
```
explore: explore_name {
  always_filter:  {
    filters:  [field_name: "filter expression", field_name: "filter expression", ...]
  }
}

```

Hierarchy `always_filter` |  Default Value NoneAccepts A field name and a Looker filter expression  
---|---  
## Definition
`always_filter` lets you require users to include a certain set of filters that you define. You also define a default value for the filters. Although users may change your default value for their query, they cannot remove the filter entirely.
The field referenced in the `filters` subparameter can be a dimension, measure, filter, or parameter. If you need to reference a dimension or measure that is part of a joined view rather than part of this Explore, use `view_name.field_name`. For example:
```
explore: order {
  always_filter: {
    filters: [id: "123", customer.id: "789"]
  }
  join: customer {
    sql_on: ${order.customer_id} = ${customer.id} ;;
  }
}

```

Here the `id` filter refers to the `id` field from `order`. The `customer.id` filter refers to the `id` field from `customer`. This example also demonstrates that you can require multiple filters.
In the `value` subparameter, specify default values using Looker filter expressions.
## Examples
Force the user to use an **Order ID** filter (with a default value of "123"):
```
explore: order {
  always_filter: {
    filters: [id: "123"]
  }
}

```

Force the user to use an **Order Created Date** filter (with a default value of the previous seven days):
```
explore: order {
  always_filter: {
    filters: [created_date: "7 days"]
  }
}

```

Force the user to use an **Order ID** filter (default value of "123"), an **Order City** filter (default value of "Chicago"), and a **Customer Age** filter (default value of greater than or equal to 18):
```
explore: order {
  always_filter: {
    filters: [id: "123", city: "Chicago", customer.age: ">=18"]
  }
  join: customer {
    sql_on: ${order.customer_id} = ${customer.id} ;;
  }
}

```

## Common challenges
### Users can't remove a filter specified by `always_filter`
Although users may change the condition or the default value for their query, they cannot remove a filter that has been added by `always_filter`. If you want to pre-load filters for an Explore in a way that lets users completely remove the filters, consider creating a query that includes suggested filters and then sharing the query with users so they can use the query and its filters as a starting point.
### Setting a blank default value
If you want to create a required filter with a **blank** default value, you can do so by specifying `"-EMPTY"` in the filter values:
```
always_filter: {
  filters: [products.category: "-EMPTY"]
}

```

### The `always_filter` parameter overrides a `default_value` filter setting
`always_filter` overrides the `default_value` setting for the field. If you declare a value with `always_filter`, that value will be the default in the Explore. If you don't declare a value with `always_filter`, then "is any value" is the filter default in the Explore.
## Things to know
###  `always_filter` affects existing Looks and dashboard tiles
Adding `always_filter` to an existing `explore` definition adds the set of filters with the default values to any Looks, Explores, or dashboard tiles based on that `explore`, including previously saved Looks and dashboard tiles that are based on the `explore`.
### If you want filters that users can't change, consider `sql_always_where`
If you want an Explore to have filters that are the same for everyone and that cannot be changed in any way, you can use `sql_always_where`.
### If you want user-specific filters that users can't change, consider `access_filter`
If you want an Explore to have filters that are specific to each user and that cannot be changed in any way, you can use `access_filter`.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


