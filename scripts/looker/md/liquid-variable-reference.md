# Liquid variable reference  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/liquid-variable-reference

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Using Liquid variables
    * Two kinds of Liquid usage
    * Accessing variables from other fields
  * Liquid variable definitions
    * Usage of date_start and date_end
    * Usage of _in_query, _is_selected, and _is_filtered
    * Usage of Liquid variables with the label parameter
    * Usage of Liquid variables with the description parameter
  * Things to consider
    * Referencing yesno fields
    * Using logical operators with Liquid variables
    * Getting the "Variable not found" error
    * Naming conventions can affect query grouping
    * Using _filters['view_name.field_name'] in a derived table requires sql_quote
    * Liquid variables in aggregate measures affect grouping




Was this helpful?
Send feedback 
#  Liquid variable reference
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using Liquid variables
    * Two kinds of Liquid usage
    * Accessing variables from other fields
  * Liquid variable definitions
    * Usage of date_start and date_end
    * Usage of _in_query, _is_selected, and _is_filtered
    * Usage of Liquid variables with the label parameter
    * Usage of Liquid variables with the description parameter
  * Things to consider
    * Referencing yesno fields
    * Using logical operators with Liquid variables
    * Getting the "Variable not found" error
    * Naming conventions can affect query grouping
    * Using _filters['view_name.field_name'] in a derived table requires sql_quote
    * Liquid variables in aggregate measures affect grouping


Liquid is a templating language that you can use in Looker to create more dynamic content. For example, you could build URLs to external tools based on the results of a query, or change which database table is queried based on a user's selection.
Liquid statements are built from variables, filters, and tags. Variables contain information that you want to use, and the variables that Looker provides are described on this page. You can further modify those values by using filters and tags, which you can read about in this Liquid guide.
There are several places in LookML that you can use Liquid:
  * The `action` parameter
  * The `description` parameter of a field (but not of an Explore)
  * The `html` parameter
  * Label parameters at the field level, including the `label` parameter, `view_label` parameter, `group_label` parameter, and `group_item_label` parameter
  * The `link` parameter
  * Parameters that begin with `sql` (such as `sql` and `sql_on`)
  * The `default_value` dashboard filter parameter
  * The `filters` dashboard element parameter


## Using Liquid variables
Basic usage of Liquid variables is straightforward. Once you've identified the variable you'd like to use (see the following list), you can insert it into a valid LookML parameter. The specific Liquid variables that you can use in specific LookML parameters are defined next.
### Two kinds of Liquid usage
There are two ways to make use of a Liquid variable:
  1. **Output Syntax** : This type of usage can insert text and is probably the most common way to use Liquid in Looker. In this method, you enclose the Liquid variable in two curly braces. For example: `{{ value }}`
  2. **Tag Syntax** : This type of usage usually doesn't insert text; instead, it is for logical comparisons and other Liquid operations. In this method, you enclose the Liquid variable in one curly brace and a single percent sign. For example: `{% if value > 10000 %}`


### Basic examples
This section provides examples of using Liquid variables in the following ways:
  * Using Liquid with the `html` parameter to generate product images
  * Using Liquid with the `url` parameter to dynamically insert a selected value into a URL
  * Using Liquid with the `sql_table_name` parameter to set the database table based on the field that the user chooses
  * Using Liquid with the `label` parameter to change the label for a dimension depending on the LookML model name


#### Using Liquid with the `html` parameter to generate product images
In this example of HTML usage, a product ID is being inserted into an `<img>` tag to generate product images:
```
dimension: product_image {
  sql: ${product_id} ;;
  html: <img src="https://www.altostrat.com/product_images/{{ value }}.jpg" /> ;;
}

```

#### Using Liquid with the `url` parameter to dynamically insert a selected value into a URL
In this example of URL usage, an artist name is being inserted into a URL to produce a Google Search for that artist.
```
dimension: artist_name {
  sql: ${TABLE}.artist_name ;;
  link: {
    label: "Google"
    url: "https://www.google.com/search?q={{ value }}"
    icon_url: "https://google.com/favicon.ico"
  }
}

```

#### Using Liquid with the `sql_table_name` parameter to set the database table based on the field that the user chooses
In this example of SQL usage, the database table is being determined according to which fields the user chooses. The syntax uses an if, else if, else structure (denoted by `if`, `elsif`, and `else`) to check and react to the fields included in the query.
```
sql_table_name:
  {% if event.created_date._in_query %}
    event_by_day
  {% elsif event.created_week._in_query %}
    event_by_week
  {% else %}
    event
  {% endif %} ;;

```

#### Using Liquid with the `label` parameter to change the label for a dimension depending on the LookML model name
In this example of label usage, the `email` dimension changes its `label` value depending on the LookML model name. This will dynamically change the name of the field in the field picker and in any query results that include the `email` dimension:
```
dimension: email {
  label: "{% if _model._name == 'thelook' %} Looker Registered Email Address {% else %} External Email Address {% endif %}"
  type: string
  sql: ${TABLE}.email ;;
}

```

For additional usage examples, see the individual LookML parameter page you're interested in.
### Accessing variables from other fields
Liquid variables are usually based on the field where they are being used. However, you can also access values from other fields if needed.
Use the format `{{ view_name.field_name._liquid-variable-name }}` to access other fields from the same row in the query result. Replace `_liquid-variable-name` with any of the Looker Liquid variables. Make sure that the variable name is preceded by an underscore if it isn't normally, as follows:
  * `{{ view_name.field_name._value }}`
  * `{{ view_name.field_name._rendered_value }}`
  * `{{ view_name.field_name._model._name }}`


This example shows this type of usage to access a website URL from a different field:
```
dimension: linked_name {
  sql: ${name} ;;
  html: <a href="{{ website.url._value }}" target="_blank">{{ value }}</a> ;;
}

```

> When you reference another field with the `{{ field_name._value }}` Liquid variable syntax, the referenced field is added to the `SELECT` clause of the SQL query and added as an additional column in the `GROUP BY` clause. This is necessary to properly retrieve the values in the referenced field. However, it can cause unexpected results in the following areas:
>   * Aggregate measures — For more information, see the section on using Liquid variables in aggregate measures on this page.
>   * Chart downloads — When used in a query that is rendered as a table chart, if the table chart columns have been manually rearranged, some download formats of the chart display columns in their original orders.
> 

## Liquid variable definitions
The following table describes the Liquid variables that you can use with LookML. The **Usage** column indicates which LookML parameters each Liquid variable can be used with, and includes the following options:
A = Works with the `action` parameter.
DV = Works with the `default_value` (for dashboards) parameter.
DE = Works with the `description` parameter at the field level, but won't work with `description` at the Explore level.
F = Works with the `filters` (for dashboard elements) parameter.
H = Works with the `html` parameter.
LA = Works with the label parameters at the field level, including the `label` parameter, `view_label` parameter, `group_label` parameter, and `group_item_label` parameter, but won't work with label parameters at the model, Explore, view, or reference line level, or with `label` as a subparameter of `link`.
LI = Works with the `link` parameter.
S = Works with all LookML parameters that begin with `sql` (e.g. `sql`, `sql_on`, and `sql_table_name`).
Variable  |  Definition  |  Usage  | Example Output  
---|---|---|---  
Field Values  
`value` |  The raw value of the field returned by the database query. Can refer to a pivoted field's value.**Usage** column, `value` is supported in the `label` subparameter of the `action` and `link` parameters.`value` variable is HTML-escaped. For example, the character is changed to `&lt;`. As a result, HTML tags in `value` won't render as HTML. |  A H LI | 8521935  
`rendered_value` |  The value of the field with Looker's default formatting.date formatting syntax in `rendered_value`, as shown in the Easy date formatting with Liquid Best Practices page.**Usage** column, `rendered_value` is supported in the `label` subparameter of the `action` and `link` parameters. |  A H LI | $8,521,935.00  
`filterable_value` |  The value of the field formatted for use as a filter in a Looker URL. `value` variable returns two different strings, "Altostrat" and "Inc". The `filterable_value` variable corrects this by escaping special characters and returning a single string, in this example, "Altostrat, Inc". |  A H LI | 8521935  
Links  
`link` |  The URL to the Looker default drill link. Note that some fields won't have any default link.  |  A H LI S |  /explore/thelook/orders?fields=orders.order_amount&limit=500  
`linked_value` |  The value of the field with the Looker default formatting and default linking. Measures don't have default linking, so measures require configuration of the `drill_fields` parameter to work with `linked_value`.  |  A H LI  
Filters  
`_filters['view_name.field_name']` |  The user filters applied to the field you ask for with `view_name.field_name`.`_filters['view_name.field_name']` is also supported in the `sql` parameter of a derived table, but is not supported in other `sql` parameters. `_filters['view_name.field_name']` in a derived table `sql` parameter requires the `sql_quote` Liquid filter. |  A DE H LA LI |  NOT NULL  
`{% date_start date_filter_name %}` |  The beginning date in a date filter you ask for with `date_filter_name`. See the Usage of `date_start` and `date_end` section for more information. | 2017-01-01  
`{% date_end date_filter_name %}` |  The ending date in a date filter you ask for with `date_filter_name`. See the Usage of `date_start` and `date_end` section for more information. | 2017-01-01  
`{% condition filter_name %}``sql_or_lookml_reference``{% endcondition %}` |  The value of the filter you ask for with `filter_name` applied to the `sql_or_lookml_reference` as SQL. This variable is used with templated filters and conditional joins.  |  _See theTemplated filters documentation page and the Conditional joins section of the **`sql_on`**documentation page for examples._  
`{% parameter parameter_name %}` |  The value of the parameter filter you ask for with `parameter_name`.  |  DE LA S |  _See the`parameter` parameter documentation page for examples._  
`parameter_name._parameter_value` |  Injects the value of the parameter filter you ask for with `parameter_name` into a logical statement.  |  DE H LA LI S |  _See the`parameter` parameter documentation page for important details and examples._  
User Attributes  
`_user_attributes['name_of_attribute']` |  The value of the user attribute you ask for with `name_of_attribute`, for the particular user running the query, if user attributes are being used. The `_user_attributes['name_of_attribute']` variable can also be used in advanced filter syntax. |  A DE H LA LI S DV F |  northeast _(if, for example, the user attribute was "region")_Using user attributes for dynamic schema and table name injection Best Practices page for an additional example.  
`_localization['localization_key']` |  Returns the value associated with a localization key defined in a model's strings file based on a user's locale.  |  _See theLocalizing your LookML model documentation page for an example._  
LookML Objects  
`_model._name` |  The name of the model for this field.  |  A DE H LA LI S |  thelook  
`_view._name` |  The name of the view for this field.  |  A DE H LA LI S |  orders  
`_explore._name` |  The name of the Explore for this field.  |  A DE H LA LI S |  order_items  
`_explore._dashboard_url` |  Added 22.12  The relative URL for the current dashboard.  |  H LI S |  /dashboards/5  
`_field._name` |  The name of the field itself, in `view_name.field_name` format.  |  A DE H LA LI S |  orders.total_order_amount  
Queries  
`_query._query_timezone` |  The time zone in which the query was run.  |  A DE H LA LI S |  America/Los_Angeles  
`view_name._in_query` |  Returns `true` if any field from the view is included in the query or is included the a query using the `required_fields` parameter.  |  DE LA LI S |  true  
`view_name.field_name._in_query` |  Returns `true` if the field you ask for with `view_name.field_name` is selected and therefore included in the query, or is included in a filter for a query, or is included in a query using the `required_fields` parameter.  |  DE LA LI S |  true  
`view_name.field_name._is_selected` |  Returns `true` if the field you ask for with `view_name.field_name` is selected and therefore included in the query or is included in the query using the `required_fields` parameter.`_is_selected` returns `false` in certain cases:
  * Unpivoted dimensions return `false` in column totals
  * Pivoted dimensions return `false` in row totals
  * All dimensions return `false` in grand totals

|  DE LA LI S |  true  
`view_name.field_name._is_filtered` |  Returns `true` if the field you ask for with `view_name.field_name` is included in a filter for the query.  |  DE LA LI S |  true  
### Usage of `date_start` and `date_end`
The `date_start` and `date_end` Liquid variables are very useful for database dialects that partition data into multiple tables by date, such as BigQuery. You must use the tag syntax `{% date_start date_filter_name %}` or `{% date_end date_filter_name %}`. You cannot use the output syntax `{{ date_start date_filter_name }}` or `{{ date_end date_filter_name }}`, even though this syntax would typically be used to generate text.
For example, you can create these fields in a view:
```

filter: new_filter_test{
  type: date
}

dimension: filter_start{
  type: date
  sql: {% date_start new_filter_test %} ;;
}

dimension: filter_end{
  type: date
  sql: {% date_end new_filter_test %} ;;
}


```

If you filter an Explore on `new_filter_test` using the date range April 1, 2022 to May 25, 2022, the `filter_start` dimension would evaluate to **April 1, 2022** ; the `filter_end` would evaluate to **May 25, 2022**.
Note the following about `date_start` and `date_end`:
  * If the user doesn't filter the query using the filter that is specified in the `date_filter` part of the Liquid variable, both `{% date_start date_filter %}` and `{% date_end date_filter %}` will evaluate to NULL.
  * If the user filters the query with an open-ended range on the filter that is specified in the `date_filter` part of the Liquid variable, the open end of the range will resolve to NULL. For example, using the example, if in the Explore a user sets the `new_filter_test` to **before 2022-06-07** , the `{% date_start date_filter %}` output will be NULL, since the user specified a range that has an end date but no start date. If a user sets the `new_filter_test` to **after 2022-06-07** , the `{% date_end date_filter %}` output will be NULL.


In either of these scenarios where the Liquid output may show a result of NULL, be sure to include a SQL function in the `sql` parameter to account for NULL values, such as `IFNULL` or `COALESCE`, depending on your database dialect.
See the Using date_start and date_end Best Practices page for an in-depth explanation on how to use the `date_start` and `date_end` Liquid variables to deal with date-partitioned tables.
See the Analytic Block Flexible period-over-period analysis Community post for an example of using `date_start` and `date_end` for flexible period-over-period analysis.
### Usage of `_in_query`, `_is_selected`, and `_is_filtered`
Note that the `_in_query`, `_is_selected`, and `_is_filtered` variables provide either a true or a false value, as shown in this basic example of SQL usage. Consequently, choosing the proper type of Liquid variable reference is important.
If you want to determine whether or not something is included in your query, then insert certain text based on that, you should use a pattern like this:
```
{% if view_name.field_name._in_query %}
  something to insert if true
{% else %}
  something to insert if false
{% endif %}

```

If you want to literally insert the word "true" or "false", use a pattern like this:
```
{{ view_name.field_name._in_query }}

```

Some SQL dialects don't support the literal words "true" and "false". In that case, you can add the `sql_boolean` filter to get the true and false values you need:
```
{{ view_name.field_name._in_query | sql_boolean }}

```

The same patterns apply to the `_is_selected` and `_is_filtered` variables.
### Usage of Liquid variables with the `label` parameter
You can use Liquid variables in a field's `label` parameter to dynamically change the field's appearance in the field picker and in visualizations. See the table in the Liquid variable definitions section on this page to see which Liquid variables will work with the `label` parameter.
> Liquid variables work with label parameters at the field level, including the `label` parameter, `view_label` parameter, `group_label` parameter, and `group_item_label` parameter, but won't work with label parameters at the model, Explore, view, or reference line level, or with label as a subparameter of `link`.
The following variables can be used with `label` to affect the field picker, column headers in the data section of an Explore, and visualizations:
  * `_model._name`
  * `_view._name`
  * `_explore._name`
  * `_field._name`
  * `_user_attributes['name_of_attribute']`


The other Liquid variables marked with **LA** in the Liquid variable definitions table, such as those that return a value based on a filter (like `_filters`) or require that a query be run before the variable value can be determined (like `in_query`), won't change the name of the field in the field picker. In those cases, the field name will only be changed in the resulting visualization.
When using the `parameter` Liquid variable with `label`, `label` is passed the value of the `value` subparameter.
### Usage of Liquid variables with the `description` parameter
You can use Liquid variables with the `description` parameter to dynamically change the description for a field. This description appears when users hold the pointer over the field's information icon in the field picker, the field's column name in the data section of the Explore, or the field's column name in a table chart. See the table in the Liquid variable definitions section on this page to see which Liquid variables work with the `description` parameter.
> Liquid variables work with the `description` parameter only at the field level. They won't work with the `description` parameter at the Explore level.
The following variables can be used with `description` to affect the field picker, the data section of an Explore, and the column header in a table chart:
  * `_model._name`
  * `_view._name`
  * `_explore._name`
  * `_field._name`
  * `_user_attributes['name_of_attribute']`


The other Liquid variables marked with **DE** in the Liquid variable definitions table, such as Liquid variables that return a value based on a filter (like `_filters`) or require that a query run before the variable value can be determined (like `in_query`) won't change the description in the field picker or in the data section of an Explore. These Liquid variables will only affect the description shown when a user hovers over the field's column header in a table chart.
For examples of how to use Liquid in the `description` parameter, see the `description` parameter documentation page.
## Things to consider
### Referencing `yesno` fields
To reference a `yesno` field's value, the value is case-sensitive. Use `Yes` or `No`. For example:
```
{% if value == 'Yes' %}

```

### Using logical operators with Liquid variables
You can use the logical operators `and` and `or` with Liquid variables. Logical operators in Liquid are case-sensitive and must be written in all lowercase. For example:
```
{% if value == "Shirt" or value == "Shoes" %}
  This is a shirt or shoes.
{% endif %}

```

### Getting the "Variable not found" error
One reason you might get this error in Liquid is if you use `{{ }}` and `{% %}` at the same time, like this:
```
{% if value > {{ search_latency_top_hr.limit_95._value }} %}

```

Instead do this:
```
{% if value > search_latency_top_hr.limit_95._value %}

```

If you are using a templated filter, then check whether you are referencing a table name that you have not joined into the derived table.
### Naming conventions can affect query grouping
If there is a field with the name **value** , this field will be included in the **GROUP BY** clause of an Explore query whenever the `value` Liquid variable is referenced in another field within the same view.
For example:
```
dimension: id {
  primary_key: true
  type: number
  sql: ${TABLE}.id ;;
  html:
    {% if value > 10 %}
      <font color:"darkgreen">{{ rendered_value }}</font>
    {% elsif value > 11 %}
      <font color:"goldenrod">{{ rendered_value }}</font>
    {% else %}
      <font color:"darkred">{{ rendered_value }}</font>
    {% endif %} ;;
}

dimension: value {
  sql: ${TABLE}.status ;;
  type: string
}

```

This will generate the following SQL when only **id** is selected in an Explore:
```
SELECT
orders.id AS orders.id,
orders.status AS orders.value
FROM order_items
LEFT JOIN orders ON order_items.order_id = orders.id

GROUP BY 1,2
ORDER BY orders.id
LIMIT 500

```

To avoid this grouping behavior, make sure to scope the `value` variable with the name of the field to explicitly reference the field:
```
dimension: id {
  primary_key: true
  type: number
  sql: ${TABLE}.id ;;
  html:
    {% if value > 10 %}
      <font color:"darkgreen">{{ id._rendered_value }}</font>
    {% elsif value > 11 %}
      <font color:"goldenrod">{{ id._rendered_value }}</font>
    {% else %}
      <font color:"darkred">{{ id._rendered_value }}</font>
    {% endif %} ;;
}

```

### Using `_filters['view_name.field_name']` in a derived table requires `sql_quote`
When you are defining a SQL-based derived table, if you use the `_filters['view_name.field_name']` Liquid variable where the value is rendered in SQL and the filter returns a string value, you need to add single quotation marks around the output. You can do this by including the `sql_quote` Liquid filter.
For example, if you are using either of these Liquid variables in the `sql` parameter of a `derived_table` parameter:
```
{{ _filters['view_name.field_name'] }}

```

or
```
{% assign foo = _filters['view_name.field_name']  %} foo

```

You can append the Liquid filter `| sql_quote` to the Liquid variable declaration:
```
{{ _filters['view_name.field_name'] | sql_quote }}

```

and
```
{% assign foo = _filters['view_name.field_name'] | sql_quote %} foo

```

Here is an example derived table that uses the `_filters['view_name.field_name']` variable:
```
view: users_sql_based_dt {
  derived_table: {
    sql:
    SELECT
      users.id AS id,
          (DATE(users.created_at)) AS created_date,
      users.city AS city,
      COUNT(*) AS user_count
    FROM
        public.users AS users
    {% if users_sql_based_dt.city._is_filtered %}
      WHERE
        users.city = {{ _filters['users_sql_based_dt.city'] | sql_quote  }}
    {% endif %}
    GROUP BY
        1,
        2,
        3
    ORDER BY
        2 DESC
      ;;
  }

```

The `city` field is a string that will be output to SQL, so the `sql_quote` Liquid filter is needed to be sure that the output SQL is enclosed in single quotes. In the resultant Explore, when a user specifies a city name as a filter, Looker encloses the city name string in quotes. Looker sends this SQL to the database if a user filters the Explore query on the city value `New York`:
```
WHERE
    users.city = 'New York'

```

> If you are using the `_filters['view_name.field_name']` Liquid variable for a string field in a derived table where the value is rendered in SQL, you will get the following LookML warning if you don't append `| sql_quote` to the Liquid variable: 
> `Using "_filters[]" in Derived Table SQL without "sql_quote" is discouraged.`
You can also use `sql_quote` with this syntax to quote multiple values in an array:
```
{{ _filters['view_name.field_name'] | split:"," | sql_quote | join:"," }}

```

Here is an example where the Liquid output is being used as input for an `IN` statement:
```
 WHERE
    users.city IN({{ _filters['users_sql_based_dt.city'] | split:"," | sql_quote | join:"," }})

```

With this syntax, the Liquid output will have quotes around each individual value (`'value1','value2','value3'`) instead of having quotes around the full list (`'value1, value2, value3'`).
### Liquid variables in aggregate measures affect grouping
When you use the `{{ view_name.field_name._value }}` syntax or the `{{ field_name._value }}` syntax in the `link` or `html` parameter of a measure to reference a value from another field, Looker pulls that field into the SQL query to grab the field value. Because of this, Liquid can affect how SQL queries are generated and how many columns the `GROUP BY` clause uses, which can cause unexpected behavior when you're working with aggregate measures, such as measures of `type: count`.
For example, suppose you have the two following measures:
```
measure: count_without_liquid {
  type: count
}

measure: count_with_liquid {
  type: count
  link: {
    label: "Status Count"
    url: "https://www.google.com/search?q={{ status._value }}"
  }
}

```

When you generate a query using the `count_without_liquid` measure, you get the following results:
In this case, the query returns a single count for each month. The SQL that is generated for the previous results is shown next:
```
SELECT
TO_CHAR(DATE_TRUNC('month',order_items.created_at),'YYYY-MM')AS"order_items.created_month",
COUNT(*)AS"order_items.count_without_liquid"
FROMorder_itemsASorder_items

GROUPBYDATE_TRUNC('month',order_items.created_at)
ORDERBY1DESC
LIMIT500

```

However, when you generate a query using the `count_with_liquid` measure, you get the following results:
This example shows that, instead of a count for each month in the query, you receive a count for each month and for each status. That is because, in the generated SQL, the `status` field was added to the query so that its value could be retrieved. And, because it was added to the query, it was also added to the `GROUP BY` clause:
```
SELECT
TO_CHAR(DATE_TRUNC('month',order_items.created_at),'YYYY-MM')AS"order_items.created_month",
order_items.statusAS"order_items.status",
COUNT(*)AS"order_items.count_without_liquid"
FROMorder_itemsASorder_items

GROUPBYDATE_TRUNC('month',order_items.created_at),2
ORDERBY1DESC
LIMIT500

```

One option to stop this from happening is to use the `row[]` function with the Liquid variable, which pulls its value from the rendered results in the browser and therefore does not add the referenced field into the SQL query:
```
  link: {
    label: "{% if row['view_name.field_name'] %} some_label {% endif %}"
    url: "https://www.google.com/search?q={{ row['view_name.field_name'] }}"
  }

```

When you're using this syntax, note that the `link` parameter works only if the field is selected or included in the query by some other means.
To sum up, the use of the `row[]` syntax won't cause the field to be added to the query like `{{ field_name._value }}` does. The dynamic label will cause the link to have no label if the field is not available, which causes the link to disappear from the link menu.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


