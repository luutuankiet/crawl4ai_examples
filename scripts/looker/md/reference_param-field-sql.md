# sql (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-sql

Skip to main content 
  * Español – América Latina

Console  Sign in




Send feedback 
#  sql (for fields)
Stay organized with collections  Save and categorize content based on your preferences. 
> This page refers to the `sql` parameter that is part of a field.
> `sql` can also be used as part of a derived table, as described on the `sql` (for derived tables) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    sql: ${revenue_in_dollars} - ${inventory_item.cost_in_dollars} ;;
  }
}

```

Hierarchy `sql` |  Possible Field Types Dimension, Dimension Group, Filter, MeasureAccepts A SQL expressionSpecial Rules A SQL expression that varies according to the `type` of the field (as described in detail on this documentation page)   
---|---  
## Definition
The `sql` parameter takes several types of SQL expressions that will define a dimension, measure, or filter. The expression you need to write varies based on the type of field you are creating. More details about dimension and filter types can be found on the Dimension, filter, and parameter types documentation page, while more details about measure types can be found on the Measure types documentation page. See also the Incorporating SQL and referring to LookML objects documentation page.
###  `sql` for Dimensions
The `sql` block for dimensions can generally take any valid SQL that would go into a single column of a `SELECT` statement. These statements generally rely on Looker's substitution operator, which has several forms:
  * `${TABLE}.column_name` references a column in the table that is connected to the view you're working on.
  * `${dimension_name}` references a dimension within the view you're working on.
  * `${view_name.dimension_name}` references a dimension from another view.
  * `${view_name.SQL_TABLE_NAME}` references another view or derived table. (Note that `SQL_TABLE_NAME` in this reference is a literal string; you do not need to replace it with anything.)


If `sql` is left unspecified, then Looker assumes that there is a column in the underlying table with the same name as the field. For example, selecting a field called `city` without a `sql` parameter would be equivalent to specifying `sql: ${TABLE}.city`.
> The `sql` parameter of a dimension cannot include any aggregations. This means it cannot contain SQL aggregations or references to LookML measures. If you want to create a field with `sql` that includes a SQL aggregation or that references a LookML measure, use a `sql` parameter in a _measure_, not in a dimension.
A very simple dimension that takes the value directly from a column called `revenue` could look like:
```
dimension: revenue_in_cents {
  sql: ${TABLE}.revenue ;;
  type: number
}

```

A dimension that relies on another dimension in the same view could look like this:
```
dimension: revenue_in_dollars {
  sql: ${revenue_in_cents} / 100 ;;
  type: number
}

```

A dimension that relies on another dimension in a _different_ view could look like this:
```
dimension: profit_in_dollars {
  sql: ${revenue_in_dollars} - ${inventory_item.cost_in_dollars} ;;
  type: number
}

```

A dimension that relies on another dimension in a derived table could look like this:
```
dimension: average_margin {
  sql: (SELECT avg(${gross_margin} FROM ${order_facts.SQL_TABLE_NAME})) ;;
  type: number
}

```

More advanced SQL users can perform relatively advanced calculations, including correlated sub-queries (note: not all database dialect support correlated subqueries):
```
dimension: user_order_sequence_number {
  type: number
  sql:
    (
      SELECT COUNT(*)
      FROM orders AS o
      WHERE o.id <= ${TABLE}.id
        AND o.user_id = ${TABLE}.user_id
    ) ;;
}

```

For further details, refer to the documentation for a specific dimension type.
####  `sql` for Dimension Groups
The `sql` parameter for a `dimension_group` takes any valid SQL expression that contains data in a timestamp, datetime, date, epoch, or yyyymmdd format.
###  `sql` for Measures
The `sql` block for measures typically takes one of two forms:
  * The SQL over which an aggregate function (such as `COUNT`, `SUM`, `AVG`) will be performed, again using Looker's substitution operator as described in the SQL for Dimensions section
  * A value based on several other measures


For example, to calculate the total revenue in dollars, we might use:
```
measure: total_revenue_in_dollars {
  sql: ${revenue_in_dollars} ;;
  type: sum
}

```

To calculate our total profit, we might use:
```
measure: total_revenue_in_dollars {
  sql: ${total_revenue_in_dollars} - ${inventory_item.total_cost_in_dollars} ;;
  type: number
}

```

For further details, see the documentation for a specific measure type.
For a `count` measure type, you can leave off the `sql` parameter.
For other types of measures, if `sql` is left unspecified then Looker assumes that there is a column in the underlying table with the same name as the field. Since a measure should have a name indicating that it is an aggregate of an underlying set of values, in practice you should always include a `sql` parameter.
### SQL math challenges
There are two frequent challenges that come up with division in the `sql` parameter.
First, if you are using division in your calculation, you want to protect against the possibility of dividing by zero, which will cause a SQL error. To do so, use the SQL `NULLIF` function. For example, this example means "if the denominator is zero, treat it like NULL instead":
```
measure: active_users_percent {
  sql: ${active_users} / NULLIF(${users}, 0) ;;
  type: number
}

```

Another issue is the way that SQL handles integer math. If you divide 5 by 2, most people expect the result to be 2.5. However, many SQL dialects will return the result as just 2, because when it divides two integers it also gives the result as an integer. To address this, you can multiply the numerator by a decimal number to force SQL into returning a decimal result. For example:
```
measure: active_users_percent {
  sql: 100.00 * ${active_users} / NULLIF(${users}, 0) ;;
  type: number
}

```

### Liquid variables with `sql`
You can also use Liquid variables with the `sql` parameter. Liquid variables let you access data such as the values in a field, data about the field, and filters applied to the field.
For example, this dimension masks a customer password according to a Looker user attribute:
```
dimension: customer_password {
  sql:
    {% if _user_attributes['pw_access'] == 'yes' %}
      ${password}
    {% else %}
      "Password Hidden"
    {% endif %} ;;
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


