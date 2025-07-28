# cancel_grouping_fields  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-cancel-grouping-fields

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * cancel_grouping_fields requires fully scoped field names
    * cancel_grouping_fields is triggered when any specified field is chosen, it doesn't require all fields to be chosen
  * Things to know
    * cancel_grouping_fields is not required for Looker to work properly. It is for query improvement on large tables




Was this helpful?
Send feedback 
#  cancel_grouping_fields
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * cancel_grouping_fields requires fully scoped field names
    * cancel_grouping_fields is triggered when any specified field is chosen, it doesn't require all fields to be chosen
  * Things to know
    * cancel_grouping_fields is not required for Looker to work properly. It is for query improvement on large tables


## Usage
```
explore: explore_name {
  cancel_grouping_fields: [
    fully_scoped_field,
    fully_scoped_field,
    ...
  ]
}

```

Hierarchy `cancel_grouping_fields` |  Default Value NoneAccepts Square brackets containing a comma-separated list of fully scoped field namesSpecial Rules
  * Each field must be fully specified using `view_name.field_name` syntax
  * Will not function correctly if measures are included in the query
  * Cannot be used with `relationship: one_to_many` or `relationship: many_to_many`

  
---|---  
## Definition
`cancel_grouping_fields` lets you stop Looker from adding a `GROUP BY` clause to the SQL that it generates. If any of the fields that you specify are included by the user, Looker will not group. This functionality is typically used to improve query performance on very large tables. Except in rare and unique circumstances, you should only include fields that are unique to each row in the table, such as the primary key.
Since Looker measures represent SQL aggregate functions, which require a `GROUP BY` clause to work, you should note that `cancel_grouping_fields` will not work with any query that includes measures. Furthermore `cancel_grouping_fields` does not work when `relationship: one_to_many` or `relationship: many_to_many` is used.
Finally, note that the fields you list must be fully scoped. In other words, they should be written as `view_name.field_name`, and not simply as `field_name`.
## Examples
Do not group the results if the user chooses **Order ID** in the field picker:
```
explore: order {
  cancel_grouping_fields: [order.id]
}

```

Do not group the results if the user chooses **Order ID** or **Order Hash** in the field picker:
```
explore: order {
  cancel_grouping_fields: [order.id, order.hash]
}

```

Do not group the results if the user chooses **Person ID** or **DNA ID** in the field picker:
```
explore: person {
  cancel_grouping_fields: [person.id, dna.id]
  join: dna {
    sql_on: ${person.dna_id} = ${dna.id} ;;
    relationship: one_to_one
  }
}

```

## Common challenges
###  `cancel_grouping_fields` requires fully scoped field names
Most parameters in Looker will assume a view name, based on the place that the parameter is used, if you write a field name by itself. `cancel_grouping_fields` does not work this way and requires you to write both the view name and field name.
For example, you might think this would work, and that `id` would be interpreted as the **Order ID** that appears in the field picker:
```
explore: order {
  cancel_grouping_fields: [id]
}

```

However, this is not the case, and you will receive an error. Instead you must write:
```
explore: order {
  cancel_grouping_fields: [order.id]
}

```

###  `cancel_grouping_fields` is triggered when _any_ specified field is chosen, it doesn't require _all_ fields to be chosen
If you specify more than one field in `cancel_grouping_fields`, grouping will be cancelled if a user selects _any_ field in the list. The user is not required to select _all_ the fields in the list. For this reason, multi-column primary keys don't work with `cancel_grouping_fields`.
## Things to know
###  `cancel_grouping_fields` is not required for Looker to work properly. It is for query improvement on large tables
When writing SQL by hand, most people will not include a `GROUP BY` clause unless it is absolutely necessary. Looker also avoids unnecessary `GROUP BY` clauses in some cases. If one of the dimensions in your query has been defined as the primary key (by using the `primary_key` parameter) of the Explore you're using, the `GROUP BY` clause will be dropped.
However, there are some cases when another dimension — which is not the primary key — still defines a unique row. In these cases Looker may generate an unnecessary `GROUP BY`, because grouping by dimensions is a fundamental part of how Looker works. In the majority of cases, this won't cause any problems. Results will show up the way you expect them and will be speedy.
However, on some very large tables, unnecessary `GROUP BY` clauses can lengthen query times. This is the ideal situation in which to use `cancel_grouping_fields`.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


