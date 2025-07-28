# sql_always_where  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-sql-always-where

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * If you use raw SQL, you might need to use always_join
    * Only use one sql_always_where per Explore
  * Things to know
    * There is a similar parameter for the SQL HAVING clause
    * If you want filters a user can change, but not remove, consider always_filter
    * If you want user specific filters that can't be changed, consider access_filter
    * When an Explore includes sql_always_where, the default value of full_suggestions switches to yes




Was this helpful?
Send feedback 
#  sql_always_where
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * If you use raw SQL, you might need to use always_join
    * Only use one sql_always_where per Explore
  * Things to know
    * There is a similar parameter for the SQL HAVING clause
    * If you want filters a user can change, but not remove, consider always_filter
    * If you want user specific filters that can't be changed, consider access_filter
    * When an Explore includes sql_always_where, the default value of full_suggestions switches to yes


## Usage
```
explore: explore_name {
  sql_always_where: ${created_date} >= '2017-01-01' ;;
}

```

Hierarchy `sql_always_where` |  Default Value NoneAccepts A SQL `WHERE` condition using dimension name(s) and/or SQL column name(s)Special Rules If you are referencing a SQL column name in `sql_always_where` that is part of a joined view rather than part of the Explore, it's important to use the `always_join` parameter -- or reference a field name instead   
---|---  
## Definition
`sql_always_where` lets you apply a query restriction that users cannot change. The restriction will be inserted into the `WHERE` clause of the underlying SQL that Looker generates, for all queries on the Explore where `sql_always_where` is used. In addition to queries run by human users, the restriction will apply to dashboards, scheduled Looks, and embedded information that relies on that Explore.
The condition can be written in pure SQL, using your database's actual table and column names. It can also use Looker references like:
  * `${view_name.SQL_TABLE_NAME}`, which references a different Looker view or a derived table. Note that `SQL_TABLE_NAME` in this reference is a literal string; you do not need to replace it with anything.
  * `${view_name.field_name}`, which references a Looker field. Using this method is better than referring to SQL columns directly because Looker can automatically include any necessary joins.


A `sql_always_where` condition is not displayed to the user, unless they look at the underlying SQL of any queries that they create.
## Examples
Prevent users from looking at orders before 2012-01-01:
```
# Using Looker references
explore: order {
  sql_always_where: ${created_date} >= '2012-01-01' ;;
}

# Using raw SQL
explore: order {
  sql_always_where: DATE(created_time) >= '2012-01-01' ;;
}

```

Prevent users from looking at customer information for Altostrat Corporation:
```
explore: customer {
  sql_always_where: ${name} <> 'Altostrat Corporation' ;;
}

```

Prevent users from looking at orders from Altostrat Corporation:
```
explore: order {
  sql_always_where: ${customer.name} <> 'Altostrat Corporation' ;;
  join: customer {
    sql_on: ${order.customer_id} = ${customer.id} ;;
  }
}

```

## Common challenges
### If you use raw SQL, you might need to use `always_join`
If you are referencing a SQL column name in `sql_always_where` that is part of a joined view, instead of the Explore, it's important to use the `always_join` parameter. Consider this example:
```
explore: order {
  sql_always_where: customer.name <> 'Altostrat Corporation' ;;
  join: customer {
    sql_on: ${order.customer_id} = ${customer.id} ;;
  }
}

```

In this case `sql_always_where` is referencing a column from the joined `customer` view, instead of the `order` Explore. Since `sql_always_where` will be applied to every query, it's important that `customer` is also joined in every query.
When Looker generates SQL for a query, it attempts to create the cleanest SQL possible, and will only use the joins that are necessary for the fields a user selects. In this case, Looker would only join `customer` if a user selected a customer field. By using `always_join`, you can force the join to occur no matter what.
If, instead of `sql_always_where: customer.name <> 'Altostrat Corporation'` you used `sql_always_where: ${customer.name} <> 'Altostrat Corporation'`, Looker would be smart enough to make the `customer` join without requiring you to use `always_join`. For this reason, we encourage you to use Looker field references instead of raw SQL references when possible.
### Only use one `sql_always_where` per Explore
You should only have one `sql_always_where` in an `explore` definition. Put all the desired behavior into a single `sql_always_where` by using `AND` and `OR` as needed.
## Things to know
### There is a similar parameter for the SQL HAVING clause
There is a very similar parameter to `sql_always_where` called `sql_always_having` that works in the same way, but applies conditions to the `HAVING` clause instead of the `WHERE` clause.
### If you want filters a user can change, but not remove, consider `always_filter`
If you want to force users to use a specific set of filters, but where the default value can be changed, try `always_filter` instead.
### If you want user specific filters that can't be changed, consider `access_filter`
If you want an Explore to have filters that are specific to each user, and cannot be changed in any way, you can use `access_filter`.
### When an Explore includes `sql_always_where`, the default value of `full_suggestions` switches to `yes`
When an Explore includes the `sql_always_where` parameter, the default value of `full_suggestions` switches to `yes`. This causes the suggestions query to run using the Explore logic, which means that `sql_always_where` will be applied to narrow the suggestions that come back, limiting the list of suggestions to only the data that the user is intended to have access to.
If you manually set `full_suggestions` to `no`, the filter suggestion query won't run.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


