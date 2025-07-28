# SQL concepts for joins  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-experts-joins

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  SQL concepts for joins
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Just as in SQL, a join in LookML is used to combine rows from two or more tables, based on a related column between them.
In LookML an Explore — as defined by the `explore` LookML parameter — is used to define how a user can query the data. An Explore consists of at least one view or a set of views joined together. The main view in the Explore is always included in the query. The joined views are normally only included if they are needed to satisfy the query.
A LookML view corresponds to a SQL table (or another element that has the structure of a table) in the database, or to a derived table. The view defines what fields or columns are available in the database, and how they should be accessed.
The following example is a definition for the `orders` Explore.
See more code actions.
Light code theme
Dark code theme
```
explore: orders {
  join: users {
    type: left_outer
    sql_on: ${orders.user_id} = ${users.id} ;;
    relationship: many_to_one
  }
}

```

The `orders` view, which is the main view in the Explore, is being joined to the `users` view with a `SQL LEFT OUTER JOIN`, as indicated by the `type: left_outer` LookML parameter. The `SQL ON` clause, which is defined by the `sql_on` LookML parameter, does not use `table_alias.column` but instead refers `to ${view_name.field_name}`. This is so that if the table name or the column name changes in the database, that change only has to be made in one place.
The `relationship` parameter is important. Joins can cause fanout problems where rows are duplicated. By specifying that many orders will join to only one user, Looker recognizes that fanouts won't occur from this join, so special handling is not needed. However, `one_to_many` relationships can trigger a fanout.
The automatic generation of views and Explores defaults to a left outer join. In the previous example, however, it is very likely that every order will have exactly one user, so the join in this example can be an inner join.
To view the generated SQL of an Explore, you can run the Explore in the UI and then select the **SQL** tab in the **Data** panel.
For example, if you open the **Orders** Explore, which was defined previously, and then select the **User ID** and **Count** fields, the generated SQL will look like the following:
```
SELECT
    `user_id` AS `orders.user_id`,
    COUNT(*) AS `orders.count`
FROM
    `thelook`.`orders` AS `orders`
GROUP BY
    1
ORDER BY
    2 DESC
LIMIT 500

```

In this example, the users table is not referenced at all. It is only brought in if it is needed.
If you remove the **User ID** dimension and add in the **ID** dimension from the **Users** view, the SQL will look like the following:
```
SELECT
    `users`.`id` AS `users.id`,
    COUNT(*) AS `orders.count`
FROM
    `thelook`.`orders` AS `orders`
    INNER JOIN `thelook`.`users` AS `users` ON `orders`.`user_id` = `users`.`id`
GROUP BY
    1
ORDER BY
    2 DESC
LIMIT 500

```

In this case, since there is a selection from the **Users** view, the join is included.
The following example shows LookML in the `orders` Explore file, which was defined previously, and adds a join to the `order_items` view:
```
explore: orders {
  join: users {
    type: inner
    sql_on: ${orders.user_id} = ${users.id} ;;
    relationship: many_to_one
  }
  join: order_items {
    type: inner
    sql_on: ${orders.id} = ${order_items.order_id} ;;
    relationship: one_to_many
  }
}

```

Now if you open the **Orders** Explore in the UI, you will see the **Order Items** view. If you select the **Total Sale Price** measure from the **Order Items** view along with the **Count** from **Orders** and **ID** from **Users** , Looker generates the following SQL:
```
SELECT
    `users`.`id` AS `users.id`,
    COUNT(DISTINCT orders.id ) AS `orders.count`,
    COALESCE(SUM(`order_items`.`sale_price`), 0) AS `order_items.total_sale_price`
FROM
    `thelook`.`orders` AS `orders`
    INNER JOIN `thelook`.`users` AS `users` ON `orders`.`user_id` = `users`.`id`
    INNER JOIN `thelook`.`order_items` AS `order_items` ON `orders`.`id` = `order_items`.`order_id`
GROUP BY
    1
ORDER BY
    2 DESC
LIMIT 500

```

In this example, `COUNT(*) AS orders.count` became `COUNT(DISTINCT orders.id ) AS orders.count`. Looker detected that there was a possible fanout situation and automatically added the `SQL DISTINCT` keyword to the `SQL COUNT` function.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


