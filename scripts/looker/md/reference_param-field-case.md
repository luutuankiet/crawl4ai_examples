# case  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-case

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Definition
    * Choosing the sort order of labels with alpha_sort




Send feedback 
#  case
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Definition
    * Choosing the sort order of labels with alpha_sort


## Usage
```
view: view_name {
  dimension: field_name {
    case: {
      when: {
        sql: SQL condition ;;
        label: "value"
      }
      # Possibly more when statements
      else: "value"
    }
    alpha_sort:  yes
  }
}

```

Hierarchy `case` |  Possible Field Types DimensionAccepts A SQL condition and a stringSpecial Rules Use an `alpha_sort` parameter if you want the values alphabeticalized  
---|---  
## Definition
`case` lets you bucket results with case logic. While you can write raw SQL `CASE` statements instead, using `case` will create a drop-down menu for your users in the Looker UI. A SQL `CASE` statement will not create such a menu.
The general form of `case` is:
```
dimension: status {
  case: {
    when: {
      sql: condition ;;
      label: "Label of Condition"
    }
    # possibly more when statements
    else: "Label If No Condition Met"
  }
}

```

These parameters work as follows:
  * `when` — You may use as many `when` statements as you would like to represent each condition for which you want to supply a label. The `when` statements are evaluated in order from the first one listed to the last one listed, and the first `when` statement that is evaluated to true will assign the associated label.
  * `sql` — The `sql` parameter accepts a SQL condition that evaluates to true or false.
  * `label` — If the SQL condition is true, this is the label that will be assigned. The assigned label has a data type of `string`. The value of each `label` in a `case` statement must be unique. If you use the same `label` value for multiple SQL conditions, only the last SQL condition in the `case` statement is assigned the `label` value. See Examples on this page.
  * `else` — If none of your conditions are met, this is the label that will be used.


### Choosing the sort order of labels with `alpha_sort`
Typically, `case` values appear in the order you write them. If you prefer an alphabetical sort, you can use `alpha_sort: yes` like this:
```
dimension: status {
  alpha_sort: yes
  case: { ... }
}

```

## Examples
Assign several human-readable labels to different status numbers:
```
dimension: status {
  case: {
    when: {
      sql: ${TABLE}.status = 0 ;;
      label: "pending"
    }
    when: {
      sql: ${TABLE}.status = 1 ;;
      label: "complete"
    }
    when: {
      sql: ${TABLE}.status = 2 ;;
      label: "returned"
    }
    else: "unknown"
  }
}

```

When the same condition is repeated and evaluates to different labels, LookML uses the first condition that evaluates to true. In the following example, `${TABLE}.status = 0` evaluates to `pending` and not `returned`, since the `pending` condition is evaluated first.
```
dimension: status {
  case: {
    when: {
      sql: ${TABLE}.status = 0 ;;
      label: "pending"
    }
    when: {
      sql: ${TABLE}.status = 1 ;;
      label: "complete"
    }
    when: {
      sql: ${TABLE}.status = 0 ;;
      label: "returned"
    }
    else: "unknown"
  }
}

```

When multiple conditions evaluate to the same label, LookML uses only the first condition. In the following example, Looker will use `${TABLE}.status = 0` instead of `${TABLE}.status = 2` to generate the SQL `CASE` statement that evaluates to `pending`. When `${TABLE}.status = 2`, the `CASE` statement evaluates to `unknown`.
```
view: orders
dimension: status {
  case: {
    when: {
      sql: ${TABLE}.status = 0 ;;
      label: "pending"
    }
    when: {
      sql: ${TABLE}.status = 1 ;;
      label: "complete"
    }
    when: {
      sql: ${TABLE}.status = 2 ;;
      label: "pending"
    }
    else: "unknown"
  }
}

```

## Things to know
When a dimension contains a `case` parameter that references another field, that additional field may be added to the underlying SQL of a query that the dimension is used in. If the referenced field is not present in the query's visualization, and the visualization is a table chart with manually rearranged columns, the column order in some downloaded formats may be affected.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


