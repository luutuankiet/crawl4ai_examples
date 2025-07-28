# foreign_key  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-join-foreign-key

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  foreign_key
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
explore: view_name_1 {
  join: view_name_2 {
    foreign_key: dimension_name
  }
}

```
Hierarchy `foreign_key` |  Default Value NoneAccepts A Looker dimension nameSpecial Rules
  * This field expects a dimension name, not a column name from the underlying table (although they are sometimes identical)
  * `foreign_key`, `sql_foreign_key`, and `sql_on` may not be used at the same time within the same `join`
  * Exactly one of the dimensions in the joined view must be defined as the view's primary key by using the `primary_key` parameter

  
---|---  
## Definition
`foreign_key` establishes a join relationship between a view and its Explore. Looker matches the dimension referenced by `foreign_key` with the primary key of the joined view. You set the joined view's primary key by turning on `primary_key` for the field that serves as the primary key.
A view can be joined directly to an Explore when using `foreign_key`, or it can be joined through a second view that is already joined to that Explore.
An example of the first case, where a view is joined directly to the Explore, looks like this:
```
explore: order {
  join: customer {
    foreign_key: customer_id
  }
}

```

Assuming that the primary key of `customer` was named `id`, the SQL that Looker generated would be:
```
SELECT...
FROMorder
LEFTJOINcustomer
ONorder.customer_id=customer.id

```

In the second case, a view is joined to an Explore through an intermediate view that is already joined to that Explore. An example of that would be:
```
explore: order_items {
  join: order {
    foreign_key: order_id
  }
  join: customer {
    foreign_key: order.customer_id
  }
}

```

Here, `customer` cannot be joined directly to `order_items`. Instead, it must be joined through `order`. Assuming that the primary keys of both `order` and `customer` were named `id`, the SQL that Looker generated would be:
```
SELECT...
FROMorder_items
LEFTJOINorder
ONorder_items.order_id=order.id
LEFTJOINcustomer
ONorder.customer_id=customer.id

```

To make this work properly, you can see that we used the fully scoped field reference `order.customer_id` when joining `customer`, instead of simply `customer_id`. If we had only used `customer_id`, Looker would have tried to join `customer` directly to `order_items.customer_id` instead of through `order.customer_id`.
## Examples
Join the view named `customer` to the Explore named `order` by matching up the primary key from `customer` with `order.customer_id`:
```
explore: order {
  join: customer {
    foreign_key: customer_id
  }
}

```

Join the view named `customer` to the Explore named `order_items` through the view called `order`. Match up the primary key from `customer` with `order.customer_id`, and the primary key from `order` with `order_items.order_id`:
```
explore: order_items {
  join: order {
    foreign_key: order_id
  }
  join: customer {
    foreign_key: order.customer_id
  }
}

```

Join the views named `order` and `inventory_item` to the Explore named `order_items`. Match up the primary key from `order` with `order_items.order_id`, and the primary key from `inventory_item` with `order_items.inventory_id`:
```
explore: order_items {
  join: order {
    foreign_key: order_id
  }
  join: inventory_item {
    foreign_key: inventory_id
  }
}

```

## Common challenges
###  `foreign_key` must reference a dimension name, not a column name
The `foreign_key` parameter only takes a dimension name, not the column name in your underlying SQL database. Often times the dimension name and column name are identical, which may lead to the false conclusion that column names can be used.
### A primary key must be defined in views joined with `foreign_key`
For `foreign_key` to function properly, one of the dimensions in the joined view must be defined as the primary key of that view. A primary key is defined via the `primary_key` parameter.
Since only a single dimension can be defined as a primary key, you cannot use `foreign_key` with views that have a multi-column primary key. In such a situation you'll need to use `sql_on` instead.
## Things to know
###  `foreign_key` is not the only way to join in Looker
Some join relationships cannot be established with `foreign_key`. For example, the join may not use the primary key of the joined view, or it may require that multiple conditions are part of the join. In these situations, use `sql_on` instead.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


