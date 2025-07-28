# Templated filters and Liquid parameters  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/templated-filters

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Examples
    * Making a dynamic derived table with a templated filter
    * Making a dynamic measure with a Liquid parameter
  * Basic usage
    * Step one: Create something for the user to interact with
    * Step two: Apply the user input
  * Choosing between templated filters and Liquid parameters




Was this helpful?
Send feedback 
#  Templated filters and Liquid parameters
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Examples
    * Making a dynamic derived table with a templated filter
    * Making a dynamic measure with a Liquid parameter
  * Basic usage
    * Step one: Create something for the user to interact with
    * Step two: Apply the user input
  * Choosing between templated filters and Liquid parameters


This is an advanced topic that is aimed at users who have a good, pre-existing knowledge of SQL and LookML.
Looker automatically provides users with the ability to manipulate their queries by creating filters, which are based on dimensions and measures. While this method meets many use cases, it can't enable every analytical need. Templated filters and Liquid parameters vastly expand the possible use cases that you can support.
From a SQL perspective, dimensions and measures can only alter the outermost `WHERE` or `HAVING` clauses in your query. However, you might find that you want to let users manipulate other parts of the SQL. Adjusting part of a derived table, adjusting which database table gets queried, or creating multipurpose dimensions and filters are just some of the features you can enable with templated filters and Liquid parameters.
Templated filters and Liquid parameters make use of the Liquid templating language to insert user input into SQL queries. First, you use a LookML parameter to create a field for users to interact with. Next, you use a Liquid variable to inject the user input into SQL queries.
## Examples
Let's look at a few examples to demonstrate the value of templated filters and Liquid parameters.
### Making a dynamic derived table with a templated filter
Consider a derived table that calculates a customer's lifetime spend, within the northeast region:
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,                        -- Can be made a dimension
        SUM(sale_price) AS lifetime_spend   -- Can be made a dimension
      FROM
        order
      WHERE
        region = 'northeast'                -- Can NOT be made a dimension
      GROUP BY 1
    ;;
  }
}

```

In this query, you can create dimensions from `customer_id` and `lifetime_spend`. However, suppose you wanted the user to be able to specify the `region`, instead of hard-coding it to "northeast". The `region` cannot be exposed as a dimension, and therefore the user cannot filter on it as normal.
One option would be to use a templated filter, which would look like this:
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        SUM(sale_price) AS lifetime_spend
      FROM
        order
      WHERE
        {% condition order_region %} order.region {% endcondition %}
      GROUP BY 1
    ;;
  }

  filter: order_region {
    type: string
  }
}

```

Read more in the **Basic Usage** section for step-by-step instructions.
### Making a dynamic measure with a Liquid parameter
Consider a filtered measure that adds up the number of pants sold:
```
measure: pants_count {
  filters: [category: "pants"]
}

```

This is straightforward, but if there were dozens of categories, it would be tedious to create a measure for each. Furthermore, it may clutter the Explore experience for users.
An alternative would be to create a dynamic measure like this:
```
measure: category_count {
  type: sum
  sql:
    CASE
      WHEN ${category} = '{% parameter category_to_count %}'
      THEN 1
      ELSE 0
    END
  ;;
}

parameter: category_to_count {
  type: string
}

```

Read more in the **Basic usage** section for step-by-step instructions.
## Basic usage
### Step one: Create something for the user to interact with
  * For templated filters, add a `filter`.
  * For Liquid parameters, add a `parameter`.


In either case, these fields will appear to the user under the **Filter-Only Fields** section of the field picker.
Both `filter` and `parameter` fields can accept a series of child parameters, allowing you to customize how they operate. See the Field parameters documentation page for a complete list. There are two options that bear special mentioning for `parameter` fields.
First, `parameter` fields can have a special type called unquoted:
```
parameter: table_name {
  type: unquoted
}

```

This type allows values to be inserted into SQL without being enclosed in quotes, as a string would be. This can be useful when you need to insert SQL values such as table names.
Second, `parameter` fields have an option called allowed values that let you associate a user-friendly name with the value you want to insert. For example:
```
  parameter: sale_price_metric_picker {
    description: "Use with the Sale Price Metric measure"
    type: unquoted
    allowed_value: {
      label: "Total Sale Price"
      value: "SUM"
    }
    allowed_value: {
      label: "Average Sale Price"
      value: "AVG"
    }
    allowed_value: {
      label: "Maximum Sale Price"
      value: "MAX"
    }
    allowed_value: {
      label: "Minimum Sale Price"
      value: "MIN"
    }
  }

```

### Step two: Apply the user input
The second step is to use Liquid to add the templated filter or Liquid parameter as desired.
#### Templated filters
The syntax for templated filters breaks down like this:
```
{% condition filter_name %} sql_or_lookml_reference {% endcondition %}

```

  * The words `condition` and `endcondition` never change.
  * Replace `filter_name` with the name of the filter you created in the first step. You can also use a dimension if you did not create a filter-only field.
  * Replace `sql_or_lookml_reference` with the SQL or LookML that should be set "equal" to the user input (this is explained in more detail later in this section). If using LookML, use the `${view_name.field_name}` LookML syntax.


In the preceding example, Making a dynamic derived table with a templated filter, we used:
```
{% condition order_region %} order.region {% endcondition %}

```

It's important to understand the interaction between the Liquid tags and the SQL that you write in between the tags. These templated filter tags are always transformed into a logical expression. For example, if the user entered "Northeast" into the `order_region` filter, Looker would turn these tags into the following:
`order.region = 'Northeast'`
In other words, Looker interprets the user input and generates the appropriate logical expression.
Because templated filters return a logical expression, you can use them with other logical operators and logical expressions that are valid in the SQL `WHERE` statement. Using the previous example, if you wanted to return all values _except_ the region the user selected, you could use the following in the `WHERE` statement:
```
NOT ({% condition order_region %} order.region {% endcondition %})

```

It is also valid to use a LookML field as the filter condition. Any filters applied directly to the LookML field will determine the value of the `WHERE` statement:
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        SUM(sale_price) AS lifetime_spend
      FROM
        order
      WHERE
        {% condition region %} order.region {% endcondition %}
      GROUP BY 1
    ;;
  }

  dimension: region {
    type: string
    sql: ${TABLE}.region ;;
}

```

#### Liquid parameters
The syntax for Liquid parameters breaks down like this:
```
{% parameter parameter_name %}

```

  * The word `parameter` never changes.
  * Replace `parameter_name` with the `parameter` name you created in the first step.


For example, to apply the input from the `parameter` field in step one you could create a measure like this:
```
  measure: sale_price_metric {
    description: "Use with the Sale Price Metric Picker filter-only field"
    type: number
    label_from_parameter: sale_price_metric_picker
    sql: {% parameter sale_price_metric_picker %}(${sale_price}) ;;
    value_format_name: usd
  }


```

## Choosing between templated filters and Liquid parameters
Although templated filters and Liquid parameters are similar, there is an important difference between them:
  * **Liquid parameters** insert user input directly (or using the values you define with allowed values).
  * **Templated filters** insert values as logical statements, as described in the Templated filters section.


In situations where you want to offer users more flexible input (such as with various kinds of date ranges or string searches), try to use templated filters when possible. Looker can interpret the user input and write the appropriate SQL behind the scenes. This prevents you from having to account for every possible type of user input.
In situations where a logical statement can't be inserted, or where you know a finite set of options the user might enter, use Liquid parameters.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


