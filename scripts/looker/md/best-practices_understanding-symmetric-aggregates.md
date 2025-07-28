# Understanding symmetric aggregates  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Why symmetric aggregates are needed
  * How symmetric aggregates work
  * Why symmetric aggregates look complicated




Was this helpful?
Send feedback 
#  Understanding symmetric aggregates
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Why symmetric aggregates are needed
  * How symmetric aggregates work
  * Why symmetric aggregates look complicated


Symmetric aggregates in Looker are a very powerful feature. However, because symmetric aggregates can look a bit intimidating and mostly happen behind the scenes, it can be a bit confusing to encounter them. This page provides the following information about symmetric aggregates: 
  * Why symmetric aggregates are needed
  * How symmetric aggregates work
  * Why symmetric aggregates look complicated


## Why symmetric aggregates are needed
SQL, the language of data analysis, is extremely powerful. But with great power comes great responsibility, and analysts have a responsibility to avoid accidentally calculating incorrect aggregates, such as sums, averages, and counts. 
It is surprisingly easy to perform these calculations incorrectly, and these types of incorrect calculations can be a source of great frustration for analysts. The following example illustrates how you can go wrong. 
Imagine you have two tables, `orders` and `order_items`. The `order_items` table records one row for each item in an order, so the relationship between the tables is one-to-many. The relationship is one-to-many because one order can have many items, but each item can only be part of one order. See the Getting the relationship parameter right Best Practices page for guidance on determining the correct relationship for a join. 
In this example, suppose the `orders` table looks like this: 
`order_id` | `user_id` | `total` | `order_date`  
---|---|---|---  
1 | 100 | $ 50.36 | 2017-12-01  
2 | 101 | $ 24.12 | 2017-12-02  
3 | 137 | $ 50.36 | 2017-12-02  
In this `orders` table, the sum of the values in the `total` column (`SUM(total)`) equals `124.84`. 
Suppose the `order_items` table contains six rows: 
`order_id` | `item_id` | `quantity` | `unit_price`  
---|---|---|---  
1 | 50 | 1 | $ 23.00  
1 | 63 | 2 | $ 13.68  
2 | 63 | 1 | $ 13.68  
2 | 72 | 1 | $ 5.08  
2 | 79 | 1 | $ 5.36  
3 | 78 | 1 | $ 50.36  
Getting the count of items ordered is easy. The sum of the values in the `quantity` column (`SUM(quantity)`) is `7`. 
Now, suppose you join the `orders` table and the `order_items` table using their shared column, `order_id`. This results in the following table: 
`order_id` | `user_id` | `total` | `order_date` | `item_id` | `quantity` | `unit_price`  
---|---|---|---|---|---|---  
1 | 100 | $ 50.36 | 2017-12-01 | 50 | 1 | $ 23.00  
1 | 100 | $ 50.36 | 2017-12-01 | 63 | 2 | $ 13.68  
2 | 101 | $ 24.12 | 2017-12-02 | 63 | 1 | $ 13.68  
2 | 101 | $ 24.12 | 2017-12-02 | 72 | 1 | $ 5.08  
2 | 101 | $ 24.12 | 2017-12-02 | 79 | 1 | $ 5.36  
3 | 137 | $ 50.36 | 2017-12-02 | 78 | 1 | $ 50.36  
The preceding table provides new information, such as that two items were ordered on December 1 (`2017-12-01` in the `order_date` column) and four items were ordered on December 2 (`2017-12-02`). Some of the previous calculations, such as the `SUM(quantity)` calculations, are still valid. However, you will encounter a problem if you try to calculate the total spent. 
If you use the previous calculation, `SUM(total)`, the total value `50.36` in the new table for rows where the value of `order_id` is `1` will be counted twice, since the order includes two different items (with `item_id` values of `50` and `63`). The total of `24.12` for rows where the `order_id` is `2` will be counted three times, since this order includes three different items. As a result, the result of the calculation `SUM(total)` for this table is `223.44` instead of the correct answer, which is `124.84`. 
While it's easy to avoid this kind of mistake when you are working with two tiny example tables, solving this problem would be far more complicated in real life, with lots of tables and lots of data. This is exactly the kind of miscalculation someone could make without even realizing. _This is the problem symmetric aggregates solve._
## How symmetric aggregates work
Symmetric aggregates prevent analysts — and anyone else who uses Looker — from accidentally miscalculating aggregates such as sums, averages, and counts. Symmetric aggregates help take a huge burden off analysts' shoulders, because analysts can trust that the users won't charge ahead with incorrect data. Symmetric aggregates do this by making sure to count each fact in the calculation the correct number of times as well as by keeping track of what you're calculating. 
In the previous example, the symmetric aggregates function recognizes that `total` is a property of `orders` (not `order_items`), so it needs to count each order's total only once to get the correct answer. The function does this by using a unique primary key that the analyst has defined in Looker. That means that when Looker is doing calculations on the joined table, it recognizes that even though there are two rows where the value of `order_id` is `1`, it shouldn't count the total twice because that total has already been included in the calculation, and that it should only count the total once for the three rows where the value of `order_id` is `2`. 
It's worth noting that symmetric aggregates depend on a _unique_ primary key and the correct join relationship being specified in the model. So, if the results you're getting look wrong, talk to an analyst to make sure that everything is set up correctly. 
## Why symmetric aggregates look complicated
The appearance of symmetric aggregates can be a bit mystifying. Without symmetric aggregates, Looker typically writes nice, well-behaved SQL, such as in the following example: 
```
SELECT
  order_items.order_id AS "order_items.order_id",
  order_items.sale_price AS "order_items.sale_price"
FROM order_items AS order_items

GROUP BY 1,2
ORDER BY 1
LIMIT 500

```

With symmetric aggregates, the SQL Looker writes might look something like the following example: 
```
SELECT
  order_items.order_id AS "order_items.order_id",
  order_items.sale_price AS "order_items.sale_price",
  (COALESCE(CAST( ( SUM(DISTINCT (CAST(FLOOR(COALESCE(users.age ,0)
  *(1000000*1.0)) AS DECIMAL(38,0))) +
  CAST(STRTOL(LEFT(MD5(CONVERT(VARCHAR,users.id )),15),16) AS DECIMAL(38,0))
  * 1.0e8 + CAST(STRTOL(RIGHT(MD5(CONVERT(VARCHAR,users.id )),15),16) AS DECIMAL(38,0)) )
  - SUM(DISTINCT CAST(STRTOL(LEFT(MD5(CONVERT(VARCHAR,users.id )),15),16) AS DECIMAL(38,0))
  * 1.0e8 + CAST(STRTOL(RIGHT(MD5(CONVERT(VARCHAR,users.id )),15),16) AS DECIMAL(38,0))) ) AS DOUBLE PRECISION)
  / CAST((1000000*1.0) AS DOUBLE PRECISION), 0)
  / NULLIF(COUNT(DISTINCT CASE WHEN users.age IS NOT NULL THEN users.id
  ELSE NULL END), 0)) AS "users.average_age
FROM order_items AS order_items
LEFT JOIN users AS users ON order_items.user_id = users.id

GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 500

```

The exact format that symmetric aggregates take depends on the dialect of SQL that Looker is writing, but all formats do the same basic thing: If multiple rows have the same primary key, the symmetric aggregates function only counts them one time. It does this by using the little-known `SUM DISTINCT` and `AVG DISTINCT` functions that are part of the SQL standard. 
To see how this happens, you can take the calculation you did previously and work it through with symmetric aggregates. Of the seven columns in the joined tables, you only need two: the one you are aggregating (`total`) and the unique primary key for orders (`order_id`). 
`order_id` | `total`  
---|---  
1 | $ 50.36  
1 | $ 50.36  
2 | $ 24.12  
2 | $ 24.12  
2 | $ 24.12  
3 | $ 50.26  
Symmetric aggregates take the primary key (`order_id`, in this case) and create a very large number for each, which is guaranteed to be unique and always give the same output for the same input. (It generally does this with a hashing function, the details of which are beyond the scope of this page.) That result would look something like the following: 
`big_unique_number` | `total`  
---|---  
802959190063912 | $ 50.36  
802959190063912 | $ 50.36  
917651724816292 | $ 24.12  
917651724816292 | $ 24.12  
917651724816292 | $ 24.12  
110506994770727 | $ 50.36  
Then, for each row, Looker does this: 
```
SUM(DISTINCT big_unique_number + total) - SUM(DISTINCT big_unique_number)

```

This reliably gives you the correctly aggregated totals, counting each total exactly the right number of times. The Looker symmetric aggregates function isn't fooled by repeated rows or by multiple orders that have the same total. You can try doing the math yourself to get a better feel for how symmetric aggregates works. 
The SQL required to do this isn't the prettiest to look at: With `CAST()`, and `md5()`, and `SUM(DISTINCT)`, and `STRTOL()`, you certainly wouldn't want to write the SQL by hand. But, luckily, you don't have to — Looker can write the SQL for you. 
> _When an aggregation will work properly without the need for symmetric aggregates, Looker detects this automatically and doesn't use the function. Because symmetric aggregates impose some performance costs, Looker's ability to discern when to use, and when to not use, symmetric aggregates further optimizes the SQL that Looker generates and makes it as efficient as possible while still guaranteeing the right answer._
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


