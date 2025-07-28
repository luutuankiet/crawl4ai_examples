# sql_where  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-join-sql-where

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  sql_where
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
See more code actions.
Light code theme
Dark code theme
```
explore: view_name_1 {
  join: view_name_2 {
    sql_where: ${view_name_1.id}  100 ;;
  }
}

```

Hierarchy `sql_where` |  Default Value NoneAccepts A SQL `WHERE` clause  
---|---  
## Definition
`sql_where` lets you apply a query restriction that users cannot change. The restriction will be inserted into the `WHERE` clause of the underlying SQL that Looker generates if and only if the join is used in the query. In addition to queries run by human users, the restriction will apply to dashboards, scheduled Looks, and embedded information that relies on that Explore.
The condition can be written in pure SQL, using your database's actual table and column names. It can also use Looker field references like `${view_name.field_name}`, which is the preferred method, because Looker can be smarter about automatically including necessary joins. A `sql_where` condition is not displayed to the user, unless they look at the underlying SQL of any queries that they create.
## Example
For example, you can specify that if the join to users is used, that only users younger than 50 should be included:
```
explore: orders_users_under_50 {
  view_name: orders

  join: users {
    sql_on: ${users.id} = ${orders.user_id} ;;
    sql_where: ${users.age} < 50 ;;
    type: left_outer
  }
}

```

If the user selects `Orders.Count` and `Users.Count`, the SQL that Looker would generate from this LookML is:
```
SELECT
COUNT(orders.id)ASorders_count,
COUNT(DISTINCTusers.id,1000)ASusers_count
FROMthelook2.ordersASorders
LEFTJOINthelook2.usersASusersONusers.id=orders.user_id

WHEREusers.age50
LIMIT500

```

## Things to consider
### Parentheses are required if you are using `OR` logic
If you use OR logic with `sql_where`, it's very important to place parentheses around the SQL condition. For example, instead of writing this:
```
sql_where: region = 'Northeast' OR company = 'Altostrat' ;;

```

You would write this:
```
sql_where: (region = 'Northeast' OR company = 'Altostrat') ;;

```

If you forgot to add the parentheses in this example, and a user added their own filter, the generated `WHERE` clause could have the form:
```
WHERE
user_filter='something'AND
region='Northeast'OR
company='Altostrat'

```

In this situation, the filter that the user applied may not work. No matter what, rows with `company = 'Altostrat'` will show up, because the AND condition is evaluated first. Without parentheses, only part of the `sql_where` condition combines with the user's filter. If parentheses were added, the `WHERE` clause would look like this instead:
```
WHERE
user_filter='something'AND
(region='Northeast'ORcompany='Altostrat')

```

Now the user's filter will be applied for every row.
### Join order is important for `sql_where` dependencies
In general, Looker implements joins in the correct order, regardless of the order in which the joins are defined in the LookML. The exception to this is with `sql_where`. If you reference a field from another join in your `sql_where` statement, the join you are referencing must be defined before your `sql_where` statement in the LookML.
For example, here is a `sql_where` statement that references the `inventory_items.id` field before `inventory_items` has been joined in:
```
explore: orders {
  hidden: yes
  join: order_items {
    sql_on: ${order_items.order_id} = ${orders.id} ;;
    sql_where: ${inventory_items.id} IS NOT NULL ;;
  }
  join: inventory_items {
    sql_on: ${inventory_items.id}=${order_items.inventory_item_id} ;;
  }
}

```

If you run a query in this Explore, Looker will return an error that the `inventory_items.id` field cannot be found.
However, you can solve this problem by reordering your joins so that the join referenced in the `sql_where` statement is defined before the `sql_where` statement, like this:
```
explore: orders {
  hidden: yes
  join: inventory_items {
    sql_on: ${inventory_items.id}=${order_items.inventory_item_id} ;;
  }
join: order_items {
    sql_on: ${order_items.order_id} = ${orders.id} ;;
    sql_where: ${inventory_items.id} IS NOT NULL ;;
  }
}

```

This will prevent the error because the `inventory_items` join is defined before the `inventory_items.id` field is referenced in the `sql_where` statement of the `order_items` join.
### The `sql_where` query restriction is applied only if the join is used
The query restriction specified in `sql_where` will be inserted into the `WHERE` clause of the underlying SQL that Looker generates if and only if the join is used in the query. If you want to have a where clause applied even if the join wouldn't have been used, use `sql_always_where` instead.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


