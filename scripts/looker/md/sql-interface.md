# Open SQL Interface  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-interface

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How the Open SQL Interface surfaces LookML project elements
  * Setting up the Open SQL Interface
    * Download the Open SQL Interface JDBC driver
  * Authenticating to the Open SQL Interface
    * Generating an access token using API keys
  * Running queries with the Open SQL Interface
    * Use backticks around database identifiers
    * Specify LookML measures with AGGREGATE()
    * Specify filter-only fields and parameters with JSON_OBJECT
    * Provide always_filter or conditionally_filter values in a WHERE or HAVING clause
  * Accessing database metadata
    * DatabaseMetadata.getSchemas
    * DatabaseMetadata.getTables
    * DatabaseMetadata.getColumns
  * Identifying Open SQL Interface queries in the Looker UI
  * Repository for third-party dependencies




Was this helpful?
Send feedback 
#  Open SQL Interface
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How the Open SQL Interface surfaces LookML project elements
  * Setting up the Open SQL Interface
    * Download the Open SQL Interface JDBC driver
  * Authenticating to the Open SQL Interface
    * Generating an access token using API keys
  * Running queries with the Open SQL Interface
    * Use backticks around database identifiers
    * Specify LookML measures with AGGREGATE()
    * Specify filter-only fields and parameters with JSON_OBJECT
    * Provide always_filter or conditionally_filter values in a WHERE or HAVING clause
  * Accessing database metadata
    * DatabaseMetadata.getSchemas
    * DatabaseMetadata.getTables
    * DatabaseMetadata.getColumns
  * Identifying Open SQL Interface queries in the Looker UI
  * Repository for third-party dependencies


The Looker LookML semantic modeling layer enables a data analyst to define dimensions, aggregates, calculations, and data relationships in a SQL database. LookML models provide code reusability and Git integration. A well-structured LookML model empowers users to do their own self-service data exploration and reporting.
The LookML model is the foundation of any data that is requested from Looker, whether that request comes from the Looker Explore interface in the Looker UI, an embedded visualization in your company portal or another third-party application, or a custom application that was developed with the Looker API. The Open SQL Interface provides access to the LookML models to any third-party application that supports Java Database Connectivity (JDBC). Applications can connect to a LookML model as if it were a database, allowing users to take advantage of all the work that was done by their data analysts in the LookML model, while using whatever tools they are most comfortable with.
## How the Open SQL Interface surfaces LookML project elements
To understand how the Open SQL Interface surfaces the elements of a LookML project, it's important to understand how LookML projects are structured.
A LookML project is a collection of files that describe the objects, database connections, and user interface elements that are used to carry out SQL queries in Looker (see LookML terms and concepts for more information). The following LookML project concepts are related to the Open SQL Interface:
  * A LookML model specifies a database connection and one or more Explores. The Open SQL Interface surfaces models as **database schemas**.
  * An Explore is a logical grouping of one or more views and the join relationships between those views. The Open SQL Interface surfaces Explores as **database tables**.
  * A view defines a collection of fields (both dimensions and measures). A view is generally based on a table in your database or a derived table. Views can contain the columns from the underlying database table as well as any custom dimensions or measures that your end users may require. The Open SQL Interface surfaces the combination of a view name and a field name as a **database column name**. For example, the `id` dimension in the `order_items` view is surfaced by Open SQL Interface as a database column called `order_items.id`.


A Looker Explore can define join relationships between several views. Because it is possible that one view might have a field with the same name as a field in a different view, the Open SQL Interface includes both the view name and the field name when referencing a column. Therefore, use this format to reference a column name when sending queries to the Open SQL Interface:
```
`<view_name>.<field_name>`

```

As an example, if there was an Explore named `order_items` that joins a view called `customer` with a view called `product` and both of these views had an `id` dimension, you would refer to the two `id` fields as ``customer.id`` and ``product.id``, respectively. To use the fully-qualified name with the Explore name as well, you would refer to the two fields as ``order_items`.`customer.id`` and ``order_items`.`product.id``. (See Use backticks around database identifiers for information on where to put the backticks when referring to database identifiers.)
## Setting up the Open SQL Interface
To use the Open SQL Interface, perform the following steps:
  1. Verify that the requirements are satisfied.
  2. Download the Open SQL Interface JDBC driver file.


The following sections describe these steps.
### Requirements
The following components are required to use the Open SQL Interface:
  * The third-party application that you want to use (such as Tableau, ThoughtSpot, or a customized application) must be able to connect to your Looker instance. The Open SQL Interface can be used with customer-hosted Looker instances, as long as the Looker instance is networked in a way that allows the third-party application to access the Looker instance.
  * A LookML project that uses data from a Google BigQuery connection. (The LookML project must have a model file that specifies a Google BigQuery connection in its `connection` parameter.)
  * A Looker user role that includes the `explore` permission on the LookML model that you want to access with the Open SQL Interface.


### Download the Open SQL Interface JDBC driver
The Looker Open SQL Interface JDBC driver is called `avatica-<release_number>-looker.jar`. Download the latest version from GitHub at https://github.com/looker-open-source/calcite-avatica/releases.
The JDBC driver expects the following URL format:
```
jdbc:looker:url=https://Looker instance URL

```

For example:
```
jdbc:looker:url=https://myInstance.cloud.looker.com

```

The JDBC driver class is:
```
org.apache.calcite.avatica.remote.looker.LookerDriver

```

## Authenticating to the Open SQL Interface
The Open SQL Interface supports three methods for authentication:
  * Generating an access token using API keys


### OAuth
JDBC clients that support OAuth can be configured to use a Looker instance's OAuth server. Follow the steps to configure OAuth authentication:
  1. Use the API Explorer extension to register the JDBC OAuth client with your Looker instance so the Looker instance can recognize OAuth requests. See Registering an OAuth client application for instructions.
  2. Log in to Looker with OAuth to request an access token. See Performing user login using OAuth for an example.
  3. Use a Properties object to pass the OAuth credentials when opening the JDBC connection to Open SQL Interface.


The following is an example using `DriverManager#getConnection(<String>, <Properties>``):
```
String access_token = getAccessToken() //uses the Looker OAuth flow to get a token
String URL = "jdbc:looker:url=https://myInstance.cloud.looker.com"
Properties info = new Properties( );
info.put("token", access_token);
Connection conn = DriverManager.getConnection(URL, info);

```

### Generating an access token using API keys
Instead of using the standard OAuth flow for generating an access token, you can follow these steps to use the Looker API to generate an access token that can be passed to the Open SQL Interface JDBC driver:
  1. Generate API keys for your Looker user as described on the Admin settings - Users page.
  2. Use the `login` API endpoint for your Looker instance. The response includes an access token in the format `Authorization: token <access_token>`. The following is an example of the curl command that you can use to make this request:
```
  curl -k -d "client_id=<client_id>&client_secret=<client_secret>" https://<looker_host>/login\

```

  3. Pass the `<access_token>` value of the response as the token in the Properties object to pass the OAuth credentials when opening the JDBC connection to Open SQL Interface.


### API keys
You can also use API keys to authenticate in place of a username and password. API keys are considered less secure than OAuth and may only be available during the preview of the Open SQL Interface. See API keys for information on creating API keys for your Looker instance.
Use the **Client ID** portion of the Looker API key as the username. Use the **Client Secret** portion for the password.
## Running queries with the Open SQL Interface
Note the following guidelines when running queries with the Open SQL Interface:
  * The Open SQL Interface accepts SQL queries that adhere to GoogleSQL syntax.
  * The Open SQL Interface requires backticks (`) around model, Explore, and field identifiers. See Use backticks around database identifiers for additional information and examples.
  * The Open SQL Interface supports most of the BigQuery operators.
  * With the Open SQL Interface, you must designate any LookML measures that are included in a query by wrapping the measure (including backticks) in the special function `AGGREGATE()`. See the Specify LookML measures with `AGGREGATE()` section.


### SQL limitations
Note the following SQL limitations when sending queries to the Open SQL Interface:
  * The Open SQL Interface supports `SELECT` queries only. The Open SQL Interface doesn't support `UPDATE` and `DELETE` statements, or any other data definition language (DDL), data manipulation language (DML), or data control language (DCL) statements.
  * The Open SQL Interface doesn't support the `JOIN` operator. 
    * You cannot send a query with the `JOIN` operator to the Open SQL Interface to create joins within the same Explore or across two different Explores.
    * If you want to create a join between two tables in your database, you can do so in the LookML model by creating joins to one or more views in an Explore definition within a model file in your LookML project.
  * The Open SQL Interface doesn't support window function calls.
  * The Open SQL Interface doesn't support subqueries.
  * The Open SQL Interface doesn't support time zone conversion. The date times in the LookML model will have the `DATETIME` type in the time zone that is defined in your settings (user time zone, application time zone, or database time zone settings).
  * The Open SQL Interface doesn't support the BigQuery data types geography, JSON, and time.


### Use backticks around database identifiers
When sending queries to Open SQL Interface, use backticks around schema, table, and column identifiers. Here is how to specify database elements using backticks with Looker terms:
  * schema: ``<model_name>``
  * table: ``<explore_name>``
  * column: ``<view_name>.<field_name>``


Here is an example `SELECT` statement format using these elements:
```
SELECT `view.field`
  FROM `model`.`explore`
  LIMIT 10;

```

### Specify LookML measures with `AGGREGATE()`
Database tables typically contain only _dimensions_ , data that describes a single attribute about a row in the table. LookML projects, however, can define both dimensions and measures. A _measure_ is an aggregation of data across multiple rows, such as `SUM`, `AVG`, `MIN` or `MAX`. (Other types of measures are supported as well, see the Measure types page for the full list of supported LookML measure types.)
With the Open SQL Interface, you must designate any LookML measures that are included in a query by wrapping the measure (including backticks) in the special function `AGGREGATE()`. For example, use this to specify the **count** measure from the **orders** view:
```
AGGREGATE(`orders.count`)

```

You must wrap LookML measures in the `AGGREGATE()` function whether the measure is in a `SELECT` clause, a `HAVING` clause, or an `ORDER BY` clause.
If you are not sure whether a field is a LookML measure, you can use the `DatabaseMetaData.getColumns` method to access metadata for the LookML project. The `IS_GENERATEDCOLUMN` column will indicate `YES` for any LookML measures, and `NO` for LookML dimensions. See the Accessing database metadata section for more information.
### Specify filter-only fields and parameters with `JSON_OBJECT`
Open SQL Interface supports parameters and filter-only fields.
When running queries with Open SQL Interface, you can apply parameters and filter-only fields to the query by including a `JSON_OBJECT` constructor call with the following format:
```
JSON_OBJECT(
    '<view>.<parameter name>', '<parameter value>',
    '<view>.<filter name>', '<Looker filter expression>'
)

```

The JSON object can contain zero or more filter key-value pairs and zero or more parameter key-value pairs.
  * The key in the `JSON_OBJECT` constructor must be the name of a filter-only field or parameter.
  * For filter-only fields, the value for each key must be a Looker string filter expression.
  * For parameters, the value for each key must be a plain value that is defined in the `parameter` definition.


See the following sections for examples of using parameters and filter-only fields with Open SQL Interface.
#### Parameter example
As an example for using a `parameter` with Open SQL Interface, if the `customers` view had a parameter defined in Looker as follows:
```
parameter:segment{
type:string
allowed_value:{
label:"Small (less than 500)"
value:"small_customers"
}
allowed_value:{
label:"Larger (greater than 10,000)"
value:"large_customers"
}
allowed_value:{
label:"Medium customers (Between 500 and 10,000)"
value:"medium_customers"
}
}

```

You could send this query to Open SQL Interface to apply the `segment` parameter value of `medium_customers` to the query:
```
SELECT`customers.segment_size`,
AGGREGATE(`orders.total_amount`)
FROM`ecommerce`.`orders`(JSON_OBJECT(
'customers.segment','medium_customers'
))
GROUPBY`customers.state`,`customers.city`
HAVINGAGGREGATE(`orders.count`)10
ORDERBY3DESCLIMIT5;

```

Open SQL Interface will pass this parameter value to the query in Looker, and Looker will apply the `medium_customers` value to any fields in the Explore that are configured to use the `segment` parameter. See the `parameter` documentation for information on how parameters work in Looker.
#### Filter-only field example
You can use a `filter` field with Open SQL Interface. For example, if a `products` view had a dimension and a filter-only field defined in Looker as follows:
```
filter: brand_select {
  type: string
  }

dimension: brand_comparitor {
  sql:
    CASE
      WHEN {% condition brand_select %} ${products.brand_name} {% endcondition %}
      THEN ${products.brand_name}
      ELSE "All Other Brands"
    END ;;
    }

```

You could use the `brand_select` filter with Open SQL Interface by sending a query such as the following:
```
SELECT`products.brand_comparator`,`products.number_of_brands`,
AGGREGATE(`products.total_revenue`)
FROM`ecommerce`.`orders`(JSON_OBJECT(
'products.brand_select','%Santa Cruz%'
))
GROUPBY`products.brand_comparator`
ORDERBY3DESCLIMIT5;

```

Open SQL Interface will apply the Looker string filter expression `%Santa Cruz%` to the query in Looker. See the `filter` documentation for information on how filter-only fields work in Looker.
### Provide `always_filter` or `conditionally_filter` values in a `WHERE` or `HAVING` clause
The Open SQL Interface can support an Explore that has either `always_filter` or `conditionally_filter`, but not both. 
If you have defined your LookML Explore with `always_filter` or `conditionally_filter`, you need to pass values for the filter fields in your SQL query to the Open SQL Interface:
  * If the filter definition specifies one or more dimensions, you must include a `WHERE` clause in your SQL query for each of the filter dimensions.
  * If the filter definition specifies one or more measures, you must include a `HAVING` clause in your SQL query for each of the filter measures.


For example, there is an `faa` model in which you've defined a LookML Explore `flights` with an `always_filter` parameter that specifies the `country` and `aircraft_category` dimensions and the `count` measure, as follows: 
```
explore: flights {
  view_name: flights
  always_filter: {
    filters: [country : "Peru" , aircraft_category : "Airplane", count : ">1"]
  }
}

```

In your query to the Open SQL Interface, you must use a `WHERE` clause to pass values for the filter dimensions and a `HAVING` clause to pass a value for the measure filter to your LookML model, such as the following:
```
SELECT
`flights.make`
FROM
`faa`.`flights`
WHERE`flights.country`='Ecuador'AND`flights.aircraft_category`='Airplane'
GROUPBY
1
HAVING`flights.count`2)LIMIT5

```

If you don't pass filter values for each of the dimensions and measures that are specified in the `always_filter` parameter, the query will return an error. The same is true for dimensions and measures specified in a `conditionally_filter` parameter, except that you can define a `conditionally_filter` parameter with an `unless` subparameter, like this:
```
explore: flights {
  view_name: flights
  conditionally_filter: {
    filters: [country : "Peru" , aircraft_category : "Airplane"]
    unless: [count]
  }
}

```

In this case, you must pass a filter value for each of the dimensions and measures that are specified in the `filters` subparameter of `conditionally_filter`, unless you instead specify a filter on a field in the `unless` subparameter. (See the `conditionally_filter` documentation page for details about using the `unless` subparameter.)
For example, either of the following queries to the Open SQL Interface would be acceptable. The first query provides filter values for the fields that are specified in the `filters` subparameter, and the second query provides a filter value for the field that is specified in the `unless` subparameter:
```
SELECT
`flights.make`
FROM
`faa`.`flights`
WHERE`flights.country`='Ecuador'AND`flights.aircraft_category`='Airplane'
LIMIT5

```
```
SELECT
`flights.make`
FROM
`faa`.`flights`
GROUPBY
1
HAVING`flights.count`2

```

### Example
Here is an example query using both dimensions and measures. This query retrieves the **state** and **city** dimensions from the **customers** view and the **total amount** measure from the **orders** view. Both of these views are joined into the **orders** Explore in the **ecommerce** model. For the cities that have more than 10 orders, this query response shows the top 5 cities by order amount:
```
SELECT`customers.state`,`customers.city`,
AGGREGATE(`orders.total_amount`)
FROM`ecommerce`.`orders`
GROUPBY`customers.state`,`customers.city`
HAVINGAGGREGATE(`orders.count`)10
ORDERBY3DESCLIMIT5;

```

## Accessing database metadata
The Open SQL Interface supports a subset of the standard JDBC DatabaseMetaData interface, which is used to obtain information about the underlying database. You can use the following methods of the DatabaseMetaData interface to get information about your LookML model:
  * `DatabaseMetadata.getSchemas`
  * `DatabaseMetaData.getTables`
  * `DatabaseMetaData.getColumns`


### DatabaseMetadata.getSchemas
The following table describes how a LookML model relates to the standard database structures in the response of the `DatabaseMetadata.getSchemas` interface method.
`getSchemas` response column | Description  
---|---  
`TABLE_SCHEM` | LookML model name  
`TABLE_CATALOG` | (null)  
### DatabaseMetadata.getTables
The following table describes how a LookML model relates to the database structures in the response of the `DatabaseMetaData.getTables` interface method. The response includes standard JDBC metadata as well as Looker-specific metadata:
`getTables` response column | Description  
---|---  
JDBC standard metadata  
`TABLE_CAT` | (null)  
`TABLE_SCHEM` | LookML model name  
`TABLE_NAME` | LookML Explore name  
`TABLE_TYPE` | Always returns the value `TABLE_TYPE`  
Looker-specific metadata  
`DESCRIPTION` | Explore description  
`LABEL` | Explore label  
`TAGS` | Explore tags  
### DatabaseMetadata.getColumns
The following table describes how a LookML model relates to the database structures in the response of the `DatabaseMetaData.getColumns` interface method. The response includes standard JDBC metadata as well as Looker-specific metadata:
`getColumns` response column | Description  
---|---  
JDBC standard metadata  
`TABLE_CAT` | (null)  
`TABLE_SCHEM` | LookML model name  
`TABLE_NAME` | LookML Explore name  
`COLUMN_NAME` | LookML field name in ``<view_name>.<field_name>`` format. For example, ``orders.amount``.  
`DATA_TYPE` | The `java.sql.Types` code of the column. For example, Looker `yesno` fields are SQL type code `16` (BOOLEAN).  
`ORDINAL_POSITION` | The 1-based ordinal of the field within the Explore (mixing dimensions and measures together alphabetically by view name, then field name)  
`IS_NULLABLE` | Always returns the value `YES`  
`IS_GENERATEDCOLUMN` |  `YES` for measures, `NO` for dimensions  
Looker-specific metadata   
`DIMENSION_GROUP` | Name of the dimension group if the field is part of a dimension group. If the field is not part of a dimension group, this will be null.  
`DRILL_FIELDS` | List of drill fields set for the dimension or measure, if any  
`FIELD_ALIAS` |  Alias for the field, if any  
`FIELD_CATEGORY` | Whether the field is a `dimension` or `measure`  
`FIELD_DESCRIPTION` | Field description  
`FIELD_GROUP_VARIANT` | If the field is presented under a field group label, the `FIELD_GROUP_VARIANT` will specify the shorter name of the field that is displayed under the group label.  
`FIELD_LABEL` | Field label  
`FIELD_NAME` | Name of the dimension or measure  
`HIDDEN` | Whether the field is hidden from the field picker in Explores (`TRUE`), or if the field is visible in the field picker in Explores (`FALSE`).  
`LOOKER_TYPE` | LookML field type for the dimension or measure  
`REQUIRES_REFRESH_ON_SORT` | Whether the SQL query must be refreshed in order to re-sort the field's values (`TRUE`), or if the field's values can be re-sorted without requiring a refresh of the SQL query (`FALSE`).  
`SORTABLE` | Whether the field can be sorted (`TRUE`) or cannot be sorted (`FALSE`)  
`TAGS` | Field tags  
`USE_STRICT_VALUE_FORMAT` | Whether the field uses strict value format (`TRUE`) or not (`FALSE`)  
`VALUE_FORMAT` |  Value format string for the field  
`VIEW_LABEL` |  View label for the field  
`VIEW_NAME` | Name of the view in which the field is defined in the LookML project  
## Identifying Open SQL Interface queries in the Looker UI
Looker admins can use the Looker UI to identify which queries originated from the Open SQL Interface:
  * In the **Queries** admin page, queries from the Open SQL Interface have a **Source** value of "SQL Interface". The **User** value will show the name of the Looker user who ran the query. You can click the **Details** button for a query to bring up additional information about the query. In the **Details** dialog, you can click **SQL Interface query** to see the SQL query that was sent to Looker from the Open SQL Interface.
  * In the System Activity History Explore, queries from the Open SQL Interface have a **Source** value of "sql_interface". The **User Email** value will show the email address of the Looker user who ran the query. You can go directly to the **History** Explore filtered on "sql_interface" by inserting your Looker instance address to the beginning of this URL:
```
https://Looker instance URL/explore/system__activity/history?fields=history.source,history.completed_date&f[history.source]=%22sql_interface%22

```



## Repository for third-party dependencies
The following link provides access to the Google-hosted repository for third-party dependencies used by the Looker JDBC driver:
https://third-party-mirror.googlesource.com/looker_sql_interface/+/refs/heads/master/third_party/
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


