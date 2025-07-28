# relationship  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-join-relationship

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Definition
    * many_to_one (default value)




Send feedback 
#  relationship
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Definition
    * many_to_one (default value)


## Usage
```
explore: view_name {
  join: view_name_2 {
    relationship: one_to_one
  }
}

```

Hierarchy `relationship` |  Default Value `many_to_one`Accepts A relationship (`many_to_one`, `many_to_many`, `one_to_many`, `one_to_one`)   
---|---  
## Definition
`relationship` lets you describe the `join` relationship between joined views. It's important to properly define the type of relationship in order for Looker to calculate accurate measures.
To understand the relationship that is being defined, consider this example:
```
explore: order {
  join: user {
    sql_on: ${order.user_id} = ${user.id} ;;
    relationship: many_to_one
  }
  join: user_facts {
    sql_on: ${user.id} = ${user_facts.user_id} ;;
    relationship: one_to_one
  }
}

```

When a view is joined directly to an Explore, like the `user` view in this example, the relationship is _from_ the Explore _to_ the joined view. We're saying here that there could be _many_ orders for _one_ user.
When a view is joined to an Explore through another view — such as how `user_facts` joins through `user` to `order` in this example — the relationship being defined is _from_ the intermediate view (`user`) _to_ the final view (`user_facts`). In this example we're saying there is _one_ user for _one_ user fact record.
The possible values for `relationship` are described in these sections of this page:
  * `many_to_one` (default value)


### one_to_one
If one row in the Explore can only match one row in the joined view, the relationship is `one_to_one`. For example, a `user` Explore with a `user_facts` joined view would be `one_to_one`, since both tables have one row per user.
> A `one_to_one` relationship requires that there be no null values in the primary keys of the tables. If there are null values in one or both of the primary keys of the tables, the relationship is either `many_to_many` or `many_to_one`.
### many_to_one (default value)
If many rows in the Explore can match one row in the joined view, the relationship is `many_to_one`. For example, an `order` Explore with a `user` joined view would be `many_to_one`, because there may be multiple orders per user.
### one_to_many
If one row in the Explore can match many rows in the joined view, the relationship is `one_to_many`. For example, an `order` Explore with an `item` joined view would be `one_to_many`, because one order can contain multiple items..
### many_to_many
If many rows in the Explore can match many rows in the joined view, the relationship is `many_to_many`. For example, a `student` Explore with a `class` joined view _could_ be `many_to_many` if a student has multiple classes and a class has multiple students. In practice, `many-to-many` relationships are often avoided in SQL database design, so most models do not have a need for `many_to_many`.
## Examples
Declare the `user` to `dna` relationship as `one_to_one`:
```
explore: user {
  join: dna {
    sql_on: ${user.dna_id} = ${dna.id} ;;
    relationship: one_to_one
  }
}

```

Declare the `order` to `user` relationship as `many_to_one`:
```
explore: order {
  join: user {
    sql_on: ${order.user_id} = ${user.id} ;;
    relationship: many_to_one
  }
}

```

Declare the `order` to `item` relationship as `one_to_many`:
```
explore: order {
  join: item {
    sql_on: ${order.order_id} = ${item.order_id} ;;
    relationship: one_to_many
  }
}

```

Declare the `student` to `class` relationship as `many_to_many`:
```
explore: student {
  join: class {
    sql_on: ${student.student_id} = ${class.student_id} ;;
    relationship: many_to_many
  }
}

```

Declare the `user` to `user_type` relationship as `many_to_one`:
```
explore: order {
  join: user {
    sql_on: ${order.user_id} = ${user.id} ;;
    relationship: many_to_one
  }
  join: user_type {
    sql_on: ${user.type_id} = ${user_type.id} ;;
    relationship: many_to_one
  }
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


