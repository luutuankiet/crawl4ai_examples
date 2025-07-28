# Getting the relationship parameter right  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-use-the-relationship-parameter-correctly

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Getting the relationship parameter right
Stay organized with collections  Save and categorize content based on your preferences. 
> This page is written for anyone attempting to use LookML to build an Explore in Looker. The page will be easier to understand if you are proficient in SQL, specifically if you understand the difference between inner and outer joins. For a concise explanation of how inner and outer joins differ, see this w3schools article on **SQL Joins**. 
Looker has the ability to be a powerful SQL engine for your company. Abstract modeling in LookML allows data and IT teams to build general rules that are always true, freeing business analysts to build queries in the wild that are always correct even if the data team never anticipated a need for them. The core driver of this ability is the symmetric aggregates algorithm, which solves an industry-wide issue with SQL joins. However, two things must be done correctly to take advantage of the algorithm: primary keys must be accurate in every view that contains a measure (typically all of them), and `relationship` parameters must be correct in every join. 
## Primary keys
In many ways, understanding the primary key of a table is essentially the same as understanding what the table is and what might be done with it. The only thing that needs to be true is that the column (or set of concatenated columns) that you choose as the primary key must have no repeated values. 
## The `relationship` parameter
Now that you've verified your primary keys, you can determine the correct value for the join's `relationship` parameter. The purpose of the `relationship` parameter is to tell Looker whether to invoke symmetric aggregates when the join is written into a SQL query. A possible approach here would be to tell Looker to always invoke them, which would always produce accurate results. However, this comes at a performance cost so it is best use symmetric aggregates judiciously. 
The process to determine the correct value is slightly different between inner and outer joins. 
### Inner joins
As an example, suppose you have a table of orders with a primary key of `order_id`: 
order_id | amount | customer_id  
---|---|---  
1 | $25.00 | 1  
2 | $50.00 | 1  
3 | $75.00 | 2  
4 | $35.00 | 3  
Suppose that you also have a table of customers with a primary key of `customer_id`: 
customer_id | first_name | last_name | visits  
---|---|---|---  
1 | Amelia | Earhart | 2  
2 | Bessie | Coleman | 2  
3 | Wilbur | Wright | 4  
You can join these tables on the `customer_id` field, which is present in both tables. This join would be represented in LookML like this:
```
explore: orders {
  join: customers {
    type: inner
    sql_on: ${orders.customer_id} = ${customers.customer_id} ;;
    relationship: many_to_one
  }
}

```

The result of this LookML join can be represented as a single joined table, as follows: 
order_id | amount | customer_id | customer_id | first_name | last_name | visits  
---|---|---|---|---|---|---  
1 | $25.00 | 1 | 1 | Amelia | Earhart | 2  
2 | $50.00 | 1 | 1 | Amelia | Earhart | 2  
3 | $75.00 | 2 | 2 | Bessie | Coleman | 2  
4 | $35.00 | 3 | 3 | Wilbur | Wright | 4  
The `many_to_one` relationship here is referring to the number of times one value of the join field (`customer_id`) is represented in each table. In the `orders` table (the left table), a single customer ID is represented many times (in this case, this is the customer with the ID of `1`, which is present in multiple rows). 
In the `customers` table (the right table), every customer ID is only represented once since `customer_id` is the primary key of that table. Therefore, records in the `orders` table could have many matches for a single value in the `customers` table. If `customer_id` wasn't unique in every row of the `customers` table, then the relationship would be `many_to_many`. 
You can follow these steps to determine the correct relationship value programmatically by checking primary keys: 
  1. Start by writing `many_to_many` as the relationship. As long as your primary keys are correct, this will always produce accurate results because Looker will always trigger the symmetric aggregation algorithm and enforce accuracy. However, since the algorithm complicates queries and adds run time, it is beneficial to try and change one or both sides to `one` instead of `many`.
  2. Take a look at the field or fields that are in your `sql_on` clause from the left table. If the field or fields form the primary key of the left table, you can change the left side of the `relationship` parameter to `one`. If not, it typically must remain `many`. (For information about a special case, see the **Things to consider** section later on this page.)
  3. Next, look at the field or fields representing your right table in the `sql_on` clause. If the field or fields form the primary key of the right table, you can change the right side to `one`.


It's best practice to write your `sql_on` phrase starting with the left table, which is represented on the left side of the equal sign, and the right table, which is on the right side. The order of the conditions in the `sql_on` parameter does not matter, unless the order is relevant to your database's SQL dialect. Even though the `sql_on` parameter does not require that you order the fields this way, arranging the `sql_on` conditions so that the left and right sides of the equal sign match how the `relationship` parameter is read from left to right can help you to determine the relationship. Ordering the fields this way can also help make it easier to discern, at a glance, which existing table in the Explore you are joining the new table to. 
### Outer joins
For outer joins, you also need to take into consideration that a fanout might occur when null records are added during the join. This is particularly important because left outer joins are the default in Looker. While null records do not affect sums or averages, they do affect the way Looker runs a measure of `type: count`. If this is done incorrectly, the null records will be counted (which is undesirable). 
In a full outer join, null records can be added to either table if its join key is missing values that exist in the other table. This is illustrated in the following example, which involves an `orders` table: 
order_id | amount | customer_id  
---|---|---  
1 | $25.00 | 1  
2 | $50.00 | 1  
3 | $75.00 | 2  
4 | $35.00 | 3  
For the example, suppose that you also have the following `customers` table: 
customer_id | first_name | last_name | visits  
---|---|---|---  
1 | Amelia | Earhart | 2  
2 | Bessie | Coleman | 2  
3 | Wilbur | Wright | 4  
4 | Charles | Yeager | 3  
Once these tables have been joined, the joined table can be represented as follows: 
order_id | amount | customer_id | customer_id | first_name | last_name | visits  
---|---|---|---|---|---|---  
1 | $25.00 | 1 | 1 | Amelia | Earhart | 2  
2 | $50.00 | 1 | 1 | Amelia | Earhart | 2  
3 | $75.00 | 2 | 2 | Bessie | Coleman | 2  
4 | $35.00 | 3 | 3 | Wilbur | Wright | 4  
null | null | null | 4 | Charles | Yeager | 3  
Just like in an inner join, the relationship between the tables' primary keys is `many_to_one`. However, the added null record forces the need for symmetric aggregates on the left table as well. Therefore, you must change the `relationship` parameter to `many_to_many`, because performing this join disrupts counts on the left table. 
If this example had been a left outer join, the null row would not have been added and the extra customer record would have been dropped. In that case, the relationship would still be `many_to_one`. This is the Looker default because it is assumed that the base table defines the analysis. In this case you are analyzing orders, not customers. If the customer table were on the left, the situation would be different. 
### Multi-level joins
In some Explores, the base table joins to one or more views that, in turn, need to join to one or more additional views. In the example here, that would mean a table would be joined to the customer table. In these situations, it is best to only look at the individual join being written when evaluating the `relationship` parameter. Looker will understand when a downstream fanout affects a query even though the affected view isn't in the join that actually created the fanout. 
## How does Looker help me?
There are mechanisms in Looker to help ensure that the relationship value is correct. One is a check for primary key uniqueness. Whenever there is a fanout and symmetric aggregates are needed to compute a measure, Looker checks the leveraged primary key for uniqueness. If it is not unique, an error will appear at query run time (however, there is no LookML Validator error for this). 
Also, if there is no way for Looker to handle a fanout (usually because no primary key is indicated), no measures will appear in the Explore from that view. To correct this, simply designate a field as the primary key to allow your measures to get into the Explore. 
## Things to consider
### Dialect support for symmetric aggregates
Looker can connect with some dialects that don't support symmetric aggregates. You can view a list of dialects and their support for symmetric aggregates on the `symmetric_aggregates` documentation page. 
### Special case
The **Inner join** section earlier on this page states that, to determine the correct relationship value, you should look at the field or fields that are in your `sql_on` clause from the left table: “If the field or fields form the primary key of the left table, you can change the left side of the `relationship` parameter to `one`. If not, it typically must remain as a `many`.” This is true unless your table contains multiple columns that have no repeated records in them. In this case, you can treat any such column as if it were a primary key when formulating your relationship, even if it is not the column designated `primary_key: yes`. 
It can be handy to make sure that there is some sort of software rule in place that ensures that the statement in the previous paragraph will always remain true for the column you designate. If so, go ahead and treat it as such and make note of its special property in the view file for others to reference in the future (complete with SQL Runner link to prove it). Be aware, though, that Looker will confirm the truth of implied uniqueness when a field is designated as the primary key, but it will not do the same for other fields. It will simply not invoke the symmetric aggregates algorithm. 
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


