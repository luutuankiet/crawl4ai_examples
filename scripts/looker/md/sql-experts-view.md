# SQL concepts for views  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-experts-view

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Customizing a view file
    * Using a SQL expression
    * Using Looker's built-in case logic
    * Using Looker's built-in bin or tier logic
  * Related resources




Was this helpful?
Send feedback 
#  SQL concepts for views
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Customizing a view file
    * Using a SQL expression
    * Using Looker's built-in case logic
    * Using Looker's built-in bin or tier logic
  * Related resources


Each view file in your LookML project defines a single _view_ within Looker, which specifies a table to query and which fields — dimensions and measures — from that table will be surfaced in the Looker UI. A view corresponds to either a single table in your database or a single derived table.
In this guide, you'll learn about the following topics:
  * How elements of a LookML view file relate to SQL
  * How to create new dimensions by using raw SQL, built-in LookML case logic, or built-in LookML bin logic


To learn more about using SQL to define and customize derived tables in LookML using SQL, see SQL concepts for derived tables.
## The view
Here is an example of a view file called `users.view`, which includes definitions for the database table that will be queried along with several dimensions and measures:
```
view: users {
  sql_table_name: thelook.users ;;

  dimension: id {
    primary_key: yes
    type: number
    sql: ${TABLE}.id ;;
  }

  dimension: age {
    type: number
    sql: ${TABLE}.age ;;
  }
   measure: average_age {
    type: average
    sql: ${age} ;;  }

  dimension_group: created {
    type: time
    timeframes: [raw, time, date, week, month, quarter, year]
    sql: ${TABLE}.created_at ;;
  }

  measure: count {
    type: count
  }
}

```

The first element of the view definition is the `sql_table_name` parameter, which specifies the table in your database that will be queried by a view. This value is the only place in the entire model where the table name is defined, because all other references to the view will use the table alias `${TABLE}`. If you want to change the database table name, it only needs to be changed in the `sql_table_name` parameter. There are some things to consider when you reference a database table.
Looker uses the `sql_table_name` value to write its SQL FROM clause, followed by the view name, which becomes the table alias. The SQL equivalent would look like this:
```
FROM`thelook`.`users`AS`users`

```

Looker uses the view's defined dimensions and measures to generate its SQL SELECT clause. Each dimension defines the type of dimension — such as string, number, or Boolean — and a `sql` LookML parameter that references the dimension within the view, using the table alias. For a dimension called `age`, see the following example:
```
  dimension: age {
    type: number
    sql: ${TABLE}.age ;;
  }

```

When Looker creates the SQL to send to your database, Looker substitutes the alias for the view into the `${TABLE}`. For the `age` dimension from the previous example, Looker would produce a SELECT clause like the following:
```
SELECT`users`.`age`AS`users.age`

```

Measures are often aggregations that are performed on dimensions. You specify the dimension alias in a measure's `sql` expression. For example, a measure that calculates the average of the `age` dimension may have a `sql` expression with the alias `${age}` in it, as in the following example:
```
  dimension: age {
    type: number
    sql: ${TABLE}.age ;;
  }

  measure: average_age {
    type: average
    sql: ${age} ;;
  }

```

If you rename the `age` dimension, its new alias propagates to any of its dimension alias references.
## Customizing a view file
You can customize the SQL expressions of your view file or use Looker's built-in LookML logic to mimic the logic of a SQL expression.
### Using a SQL expression
Suppose that you want to divide the age data into four cohorts, with users younger than 18 defined as "Youth", users aged 18-35 as "Young Adult", users aged 36-65 as "Older Adult", and users 65 and older as "Senior". To perform this division, you must define a new dimension — say, `dimension: age_cohort` — with a `sql` expression that captures these cohorts. The following LookML dimension definition uses a CASE statement that is appropriate for a MySQL database connection:
```
dimension: age_cohort {
  type: string
  sql:
    CASE
      WHEN ${age} < 18 THEN 'Youth'
      WHEN ${age} < 35 THEN 'Young Adult'
      WHEN ${age} < 65 THEN 'Older Adult'
      ELSE 'Senior'
    END ;;
}

```

Now that you have defined your age cohort as a dimension, you can reuse the CASE logic by including the age cohort dimension in your Explore queries.
When you create an Explore query with the age cohort dimension, you can use the SQL tab of the Explore to view the SQL that Looker generates. With the age cohort dimension, the SQL will look something like this:
```
SELECT
CASE
WHENusers.age18THEN'Youth'
WHENusers.age35THEN'Young Adult'
WHENusers.age65THEN'Older Adult'
ELSE'Senior'
ENDAS`users.age_cohort`,
AVG(`age`)AS`users.average_age`,
COUNT(*)AS`users.count`
FROM
`thelook`.`users`AS`users`
GROUPBY
1
ORDERBY
2DESC
LIMIT500

```

### Using Looker's built-in case logic
You can achieve the same effect as a SQL CASE statement with an expression that is database-independent. The LookML `case` parameter lets you define the cohort buckets that are made up of `when` statements that use `sql` expressions to capture specific conditions and strings for labeling the results.
The following is an example of the same new `age_cohort` dimension that is written with the `case` LookML parameter:
```
  dimension: age_cohort {
    case: {
      when: {
        sql: ${age} < 18 ;;
        label: "Youth"
      }
      when: {
        sql: ${age} < 35 ;;
        label: "Young Adult"
      }
      when: {
        sql: ${age} < 65 ;;
        label: "Middle-aged Adult"
      }
      else: "Older Adult"
    }
  }

```

At runtime, Looker builds the correct SQL CASE syntax for your database. In addition, Looker builds another expression to handle sorting the groups, so the resulting labels won't just be sorted alphanumerically (unless you define the sort order as alphanumeric). Looker builds a resulting SQL query that resembles the following:
```
SELECT
CASE
WHENusers.age18THEN'0'
WHENusers.age35THEN'1'
WHENusers.age65THEN'2'
ELSE'3'
ENDAS`users.age_cohort__sort_`,
CASE
WHENusers.age18THEN'Youth'
WHENusers.age35THEN'Young Adult'
WHENusers.age65THEN'Older Adult'
ELSE'Senior'
ENDAS`users.age_cohort`,
AVG(`age`)AS`users.average_age`,
COUNT(*)AS`users.count`
FROM
`thelook`.`users`AS`users`
GROUPBY
1,
2
ORDERBY
1
LIMIT500

```

### Using Looker's built-in bin or tier logic
Another method for specifying how numeric values should be grouped uses Looker's built-in `bin` or `tier` parameter types. The `type:bin` is used in conjunction with the `bins` parameter — likewise, the `type: tier` is used in conjunction with the `tiers` parameter — to separate a numeric dimension into a set of number ranges. The trade-off is that you cannot define labels for each bin.
The following LookML example uses the `bins` parameter in a dimension to define the minimum value in each set:
```
  dimension: age_cohort {
    type: bin
    bins: [18,36,65]
    style: integer
    sql: ${age} ;;
  }

```

You can use the `tiers` parameter in a dimension exactly the same way. For example:
```
  dimension: age_cohort {
    type: tier
    tiers: [18,36,65]
    style: integer
    sql: ${age} ;;
  }

```

Looker then generates something like the following SQL statement:
```
SELECT
CASE
WHENusers.age18THEN'0'
WHENusers.age=18ANDusers.age36THEN'1'
WHENusers.age=36ANDusers.age65THEN'2'
WHENusers.age=65THEN'3'
ELSE'4'
ENDAS`users.age_cohort__sort_`,
CASE
WHENusers.age18THEN'Below 18'
WHENusers.age=18ANDusers.age36THEN'18 to 35'
WHENusers.age=36ANDusers.age65THEN'36 to 64'
WHENusers.age=65THEN'65 or Above'
ELSE'Undefined'
ENDAS`users.age_cohort`,
AVG(`age`)AS`users.average_age`,
COUNT(*)AS`users.count`
FROM
`thelook`.`users`AS`users`
GROUPBY
1,
2
ORDERBY
1
LIMIT500

```

## Related resources
  * SQL concepts for joins
  * SQL concepts for derived tables
  * Using Looker's SQL generator
  * How Looker generates SQL
  * Looker cookbook: Maximizing code reusability with DRY LookML


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


