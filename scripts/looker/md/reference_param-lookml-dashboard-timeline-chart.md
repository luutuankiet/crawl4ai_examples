# Timeline chart parameters for LookML dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-timeline-chart

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Basic parameters
  * Query parameters
  * Option parameters
    * color_application




Was this helpful?
Send feedback 
#  Timeline chart parameters for LookML dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Basic parameters
  * Query parameters
  * Option parameters
    * color_application


> **Under Construction:** We're working on adding more to this page. In the meantime, check out the Timeline chart options documentation page to view information about creating and editing timeline charts using the visualization option menu.
The parameters described on this page can be used with LookML dashboard elements of `type: looker_timeline` in a `dashboard.lkml` file.
For information about building a timeline chart through the Looker UI, see the Timeline chart options documentation page.
## Basic parameters
When defining a LookML dashboard element, you must specify values for at least the `name` and `type` basic parameters. Other basic parameters like `title`, `height`, and `width` affect the appearance and position of an element on a dashboard.
### `name`
> This section refers to the `name` parameter that is part of a dashboard element.
> `name` can also be used as part of a dashboard filter, described on the Dashboard parameters documentation page.
Each `name` declaration creates a new dashboard element and assigns it a name. Element names must be unique. Names are sometimes referenced in the `elements` parameter when you're using `layout: grid` dashboards.
```
- name: orders_by_date

```

### `title`
> This section refers to the `title` parameter that is part of a dashboard element.
> `title` can also be used as part of a dashboard, described on the Dashboard parameters documentation page.
> `title` can also be used as part of a dashboard filter, described on the Dashboard parameters documentation page.
The `title` parameter lets you change how an element's name will appear to users. If unspecified, the title defaults to the element `name`.
Consider this example:
```
- name: sales_overview
  title: '1) Sales Overview'

```

If you used this format, instead of the element appearing as **Sales Overview** , it would appear as **1) Sales Overview**.
### `type`
> This section refers to the `type` parameter that is part of a dashboard element.
> `type` can also be used as part of a dashboard filter, described on the Dashboard parameters documentation page.
> `type` can also be used as part of a join, described on the `type` (for joins) parameter documentation page.
> `type` can also be used as part of a dimension, described on the Dimension, filter, and parameter types documentation page.
> `type` can also be used as part of a measure, described on the Measure types documentation page.
The `type` parameter determines the type of visualization to be used in the element.
```
- name: element_name
  type: text | looker_grid | table | single_value | looker_single_record |
        looker_column | looker_bar | looker_scatter | looker_line | looker_area |
        looker_pie | looker_donut_multiples | looker_funnel | looker_timeline |
        looker_map | looker_google_map | looker_geo_coordinates | looker_geo_choropleth | looker_waterfall | looker_wordcloud | looker_boxplot

```

See the `type` (for LookML dashboards) documentation page for an overview of the different types of LookML dashboard elements.
### `height`
> This section refers to the `height` parameter that is part of a dashboard element.
> `height` can also be used as part of a dashboard row, described on the Dashboard parameters documentation page.
#### For dashboards with `tile` or `static` layouts
The `height` parameter defines the height of an element, in units of `tile_size` (which is defined in pixels), for `layout: tile` and `layout: static` dashboards.
For example, the following code specifies `tile_size: 100` and `height: 4`, making the `orders_by_date` element 400 pixels in height.
```
- dashboard: sales_overview
  tile_size: 100
  ...

  elements:
  - name: orders_by_date
    height: 4
    ...

```

#### For dashboards with `newspaper` layout
The `height` parameter defines the height of an element, in units of row, for `layout: newspaper` dashboards.
A dashboard with newspaper layout defaults to an element height of 6 rows, or about 300 pixels. The minimum height is 1 row for dashboards with a `preferred viewer` parameter set to `dashboards-next`. The minimum height is 2 rows for dashboards with a `preferred viewer` parameter set to `dashboards`.
For example, the following code sets an element to be 12 rows tall, or twice as tall as other elements that are set to the default:
```
- dashboard: sales_overview
  layout: newspaper
  ...

  elements:
  - name: orders_by_date
    height: 12
    ...

```

### `width`
> This section refers to the `width` parameter that is part of a dashboard element.
> `width` can also be used as part of a dashboard, described on the Dashboard parameters documentation page.
The `width` parameter defines the width of an element, in units of `tile_size`, for `layout: tile` and `layout: static` dashboards.
For example, the following code specifies `tile_size: 100` and `width: 4`, making the `orders_by_date` element 400 pixels in width.
```
- dashboard: sales_overview
  tile_size: 100
  ...

  elements:
  - name: orders_by_date
    width: 4
    ...

```

The `width` parameter defines the width of an element, in units of columns, for `layout: newspaper` dashboards.
A dashboard with newspaper layout defaults to a width of 24 columns.
For example, the following code sets the element to half the width of the dashboard:
```
- dashboard: sales_overview
  layout: newspaper
  ...

  elements:
  - name: orders_by_date
    width: 12
    ...

```

### `top`
The `top` parameter defines the top-to-bottom position of an element, in units of `tile_size`, for `layout: static` dashboards.
For example, the following code specifies `tile_size: 100` and `top: 4`, positioning the top edge of the `orders_by_date` element 400 pixels from the top of the dashboard.
```
- dashboard: sales_overview
  tile_size: 100
  ...

  elements:
  - name: orders_by_date
    top: 4
    ...

```

### `left`
The `left` parameter defines the left-to-right position of an element, in units of `tile_size`, for `layout: static` dashboards.
For example, the following code specifies `tile_size: 100` and `left: 4`, positioning the left edge of the `orders_by_date` element 400 pixels from the left side of the dashboard.
```
- dashboard: sales_overview
  tile_size: 100
  ...

  elements:
  - name: orders_by_date
    left: 4
    ...

```

### `row`
For `layout: newspaper` dashboards, the `row` parameter defines the row that the top edge of an element is placed on.
A dashboard begins with row 0 at the top of the dashboard. A dashboard with newspaper layout defaults to an element height of 6 rows, meaning the dashboard elements at the top of a dashboard (`row: 0`) would default to taking up rows 0-5.
Each row is 50 pixels tall, which means the default element height of 6 rows is 300 pixels.
For example, the following code sets an element to be set on the second row of elements in the dashboard, assuming elements are set at the default height:
```
- dashboard: sales_overview
  layout: newspaper
  ...

  elements:
  - name: orders_by_date
    row: 6
    ...

```

### `col`
For `layout: newspaper` dashboards, the `col` parameter defines the column that the left edge of the element is placed on.
Dashboards are divided into 24 columns. A dashboard begins with column 0 at the left of the dashboard. A dashboard with newspaper layout defaults to an element width of 8 columns, meaning the dashboard elements at the left of a dashboard (`col: 0`) would default to taking up columns 0-7.
For example, the following code sets an element to be set in the third column of elements in the dashboard:
```
- dashboard: sales_overview
  layout: newspaper
  ...

  elements:
  - name: orders_by_date
    col: 16
    ...

```

### `refresh`
> This section refers to the `refresh` parameter that is part of a dashboard element.
> `refresh` can also be used as part of a dashboard, described on the Dashboard parameters documentation page.
The `refresh` parameter allows an element to reload automatically on some periodic basis, thereby retrieving fresh data. This is often helpful in settings where a dashboard is constantly displayed, such as on an office TV. Note that the dashboard must be open in a browser window for this parameter to have an effect. This setting does not run in the background to "pre-warm" the dashboard cache.
The refresh rate can be any number (without decimals) of seconds, minutes, hours, or days. For example:
```
- name: orders_by_date
  refresh: 2 hours

```

Use caution when setting short refresh intervals. If the query behind the element is resource-intensive, certain elements may strain your database more than desired.
### `note`
You can add descriptive notes to elements like this:
```
- name: element_name
  note:
    text: 'note text'
    state: collapsed | expanded
    display: above | below | hover

```

`note` has the subparameters `text`, `state`, and `display`.
#### `text`
The `text` subparameter specifies the text displayed in the note. The text can be localized.
#### `state`
The `state` subparameter determines whether the note will be `collapsed` or `expanded` if it is too big to fit on a single row within the element's width. If you choose `collapsed` and the note is too long, the note will end in a clickable ellipsis (`...`) that can be used to read the full note.
#### `display`
The `display` subparameter determines where the note is displayed on an element. `above` places the note at the top of an element, `below` places it at the bottom of an element, and `hover` requires the user to hover their mouse over the element to see the note.
## Query parameters
When defining a LookML dashboard element of `type: looker_timeline`, you must specify values for at least the `model` and `explore` query parameters. Your query must also include values for the `dimensions` and `measures` parameters, including at least one dimension representing the label field, such as a name, as well as a start field and end field, which can be a date or number. See the Timeline chart options documentation page for more information about the minimum requirements for creating timeline charts in Looker.
### `model`
The `model` parameter defines the model to use for the element query. If unspecified, it will default to the model where the dashboard resides.
```
- name: orders_by_date
  model: ecommerce

```

The `model` parameter accepts LookML constants. You can define a constant in the manifest file for your project, then use the syntax `"@{constant_name}"` to set the constant as the value for `model`. Using a constant lets you define the name of a model in one place, which is particularly useful if you're updating the name of a model that is used by multiple dashboard elements.
For more information and an example of using constants with LookML dashboards, see the `constant` parameter documentation page.
### `explore`
> This section refers to the `explore` parameter that is part of a dashboard element.
> `explore` can also be used as part of a model, described on the `explore` parameter documentation page.
> `explore` can also be used as part of a dashboard filter, described on the Dashboard parameters documentation page.
The `explore` parameter defines the Explore to use for the element query.
```
- name: orders_by_date
  explore: order

```

The `explore` parameter accepts LookML constants. You can define a constant in the manifest file for your project, then use the syntax `"@{constant_name}"` to set the constant as the value for `explore`. Using a constant lets you define the name of an Explore in one place, which is particularly useful if you're updating the name of an Explore that is used by multiple dashboard elements.
For more information and an example of using constants with LookML dashboards, see the `constant` parameter documentation page.
### `dimensions`
The `dimensions` parameter defines the dimension or dimensions to use for the element query. Use the syntax `view_name.dimension_name` to specify the dimension. Don't include `dimensions` if the query doesn't have any.
```
## single dimension example
- name: orders_by_date
  dimensions: order.order_date

## multiple dimension example
- name: orders_by_date
  dimensions: [order.order_date, customer.name]

```

### `measures`
The `measures` parameter defines the measure or measures to use for the element query. Use the syntax `view_name.measure_name` to specify the measure. Don't include `measures` if the query doesn't have any.
```
## single measure example
- name: orders_by_date
  measures: order.count

## multiple measure example
- name: orders_by_date
  measures: [order.count, order_item.count]

```

### `sorts`
The `sorts` parameter defines the sorts to be used for the element query. The primary sort is listed first, then the secondary sort, and so on. Use the syntax `view_name.field_name` to specify the dimension or measure. Don't include `sorts` if you want to use Looker's default sort order. Descending sorts are suffixed with `desc`; ascending sorts don't need a suffix.
```
## single sort example
- name: orders_by_date
  sorts: order.order_date desc

## multiple sort example
- name: orders_by_date
  sorts: [order.order_date desc, customer.name]

```

### `pivots`
The `pivots` parameter defines the dimensions that should be pivoted for the element query. Use the syntax `view_name.dimension_name` to specify the dimension. Don't include `pivots` if the query doesn't have any.
```
## single pivot example
- name: orders_by_date
  pivots: customer.gender

## multiple pivot example
- name: orders_by_date
  pivots: [customer.gender, customer.age_tier]

```

### `limit`
The `limit` parameter defines the row limit that should be used for the element query. The limit applies to the number of rows **before** any pivots are applied.
```
- name: orders_by_date
  limit: 100

```

### `filters`
> This section refers to the `filters` parameter that is part of a dashboard element.
> `filters` can also be used as part of a dashboard, described on the Dashboard parameters documentation page.
> `filters` can also be used as part of a measure, described on the `filters` parameter documentation page.
The `filters` parameter defines the non-changeable filters that should be used for the element's query. If you would like filters that a user _can_ change in the dashboard, you should set up the filters using `filters` for dashboards, then apply them to the elements using `listen`.
The syntax for `filters` is:
```
- name: element_name
  filters:
    orders.created_date: 2020/01/10 for 3 days
    orders.status: Shipped
    # You can create multiple filter statements

```

Each filter can accept a Looker filter expression or a value constant. You can also use the `_localization` or `_user_attributes` Liquid variables in the filter expression for flexible filter values.
### `listen`
Dashboard filters let viewers interactively refine the data that is shown in dashboard elements. Define dashboard filters with the `filters` parameter for LookML dashboards. Then, use the `listen` parameter to link dashboard elements to the dashboard filter.
The syntax for `listen` is as follows:
```
- name: element_name
  listen:
    filter_name_goes_here: dimension or measure on which to apply
                           the filter using view_name.field_name syntax
    # You can add more than one listen statement

```

Add the `listen` parameter to an element, and then provide the name of the filter followed by a colon and a reference to the field to which the filter should apply, using the `view_name.field_name` syntax. For example, you might create a filter called **Date** that requires a user to enter a date into the filter field in the UI. You could then apply the value that the user enters to the `orders_by_date` element like this:
```
- dashboard: sales_overview
  ...

  filters:
  - name: date
    type: date_filter

  elements:
 - name: orders_by_date
    listen:
      date: order.order_date
    ...

```

For additional examples of using the `filters` parameter and the `listen` parameter to apply dashboard filters to individual dashboard elements, see Building LookML dashboards.
### `query_timezone`
The `query_timezone` parameter specifies the time zone in which the query will be run. The time zone options are shown on the Values for `timezone` documentation page. If you want the query to run using the viewer's time zone, you can assign the value as `user_timezone`.
```
- name: orders_by_date
  query_timezone: America/Los Angeles

```
```
- name: orders_by_customer
  query_timezone: user_timezone

```

### `merged_queries`
The `merged_queries` parameter lets you combine the results of multiple queries into a single dashboard element. Define each source query within the element's `merged_queries` parameter and use the `join_fields`subparameter to specify how the results should be merged.
The following sample LookML code creates a merged results element of `type: looker_grid`. In this example, the `merged_queries` parameter is used to create a dashboard element that combines data from two separate queries into a single table chart:
```
- name: merged_results_element
  title: Merged Results Tile
  type: looker_grid
  merged_queries:
  - model: ecommerce
    explore: users
    type: table
    fields: [users.state, users.count, users.city]
    sorts: [users.count desc 0]
    limit: 5000
    column_limit: 50
    query_timezone: UTC
    listen:
    - State: users.state
  - model: ecommerce
    explore: users
    type: table
    fields: [users.state, users.city]
    sorts: [users.state]
    limit: 500
    column_limit: 50
    query_timezone: UTC
    join_fields:
    - field_name: users.state
      source_field_name: users.state
    - field_name: users.city
      source_field_name: users.city
    listen:
    - State: users.state

```

In this example, the dashboard element combines data from two source queries that are based on the `users` Explore in the `ecommerce` model. The primary query includes the `users.state`, `users.count`, and `users.city` fields, and it sorts the results by the `users.count` field. The second source query includes the `users.state` and `users.city` fields and sorts the results by the `users.state` field.
The `join_field` parameter merges the source queries based on matching values in the `users.state` and `users.city` fields.
The `listen` parameter applies a `State` filter to both queries, which lets dashboard viewers refine the query results that are displayed in the dashboard tile by selecting a specific state.
#### Example: Merging company data
Suppose you want to create a merged query that combines information about companies from two different Explores: `company_info` and `companies`. You want to join the queries on the `ipo.stock_symbol`, `companies.name`, and `companies.contact_email` fields from each Explore to create a query that returns results for company name, company contact email, IPO year, stock symbol, number of employees, and job count. You can define the merged query element in LookML as follows:
```
- name: merged_results_element
  title: Merged Results Tile
  merged_queries:
  - model: market_research
    explore: company_info
    fields: [companies.name, companies.contact_email, ipo.public_year, ipo.stock_symbol]
    filters:
      companies.contact_email: "-NULL"
      ipo.valuation_amount: NOT NULL
    sorts: [ipo.public_year desc]
  - model: company_data
    explore: companies
    fields: [companies.name, ipo.stock_symbol, companies.contact_email,
      companies.number_of_employees, jobs.job_count]
    filters:
      companies.number_of_employees: NOT NULL
      ipo.stock_symbol: "-NULL"
      companies.contact_email: "-NULL"
    sorts: [jobs.job_count desc]
    join_fields:
    - field_name: ipo.stock_symbol
      source_field_name: ipo.stock_symbol
    - field_name: companies.name
      source_field_name: companies.name
    - field_name: companies.contact_email
      source_field_name: companies.contact_email

```

#### Applying filters to merged query elements
The previous example of a merged query element demonstrates how to apply hard-coded filters directly within each source query by using the `filters` parameter. For example, the filters `companies.contact_email: "-NULL"` and `ipo.valuation_amount: NOT NULL` in the primary query restrict the results to companies that have valid contact emails and valuations. These query-level filters pre-filter the data before merging the queries and cannot be changed by the user.
You can also apply dashboard filters to merged query elements by using the `listen` parameter within the definition of each source query. For example, suppose you have a dashboard filter named `Industry` that you defined at the dashboard level by using the `filters` parameter for LookML dashboards:
```
filters:
- name: Industry
  title: Industry
  type: field_filter
  ui_config:
    type: dropdown_menu
    display: inline
  model: market_research
  explore: company_info
  field: companies.industry

```

To apply the `Industry` filter to the `companies.industry` field in both source queries, add the `listen` parameter to each of the merged query's source query definitions as follows:
```
listen:
  Industry: companies.industry

```

For example, the following sample code adds the `Industry` filter to both source queries in the merged results element from the previous example.
```
- name: merged_results_element
  title: Merged Results Tile
  merged_queries:
  - model: market_research
    explore: company_info
    fields: [companies.name, companies.contact_email, ipo.public_year, ipo.stock_symbol]
    filters:
      companies.contact_email: "-NULL"
      ipo.valuation_amount: NOT NULL
    sorts: [ipo.public_year desc]
    listen:
      Industry: companies.industry
  - model: company_data
    explore: companies
    fields: [companies.name, ipo.stock_symbol, companies.contact_email,
      companies.number_of_employees, jobs.job_count]
    filters:
      companies.number_of_employees: NOT NULL
      ipo.stock_symbol: "-NULL"
      companies.contact_email: "-NULL"
    sorts: [jobs.job_count desc]
    join_fields:
    - field_name: ipo.stock_symbol
      source_field_name: ipo.stock_symbol
    - field_name: companies.name
      source_field_name: companies.name
    - field_name: companies.contact_email
      source_field_name: companies.contact_email
    listen:
      Industry: companies.industry

```

With this addition, when a user interacts with the `Industry` dashboard filter, the corresponding source query in the merged query element will be filtered accordingly.
### `hidden_fields`
The `hidden_fields` parameter indicates which fields, if any, are used in the query but hidden in the chart. Any hidden fields will appear in the data table section of an Explore.
```
hidden_fields: [inventory_items.count, distribution_centers.id]

```

## Option parameters
Most of the parameters described in this section correspond to the options in the **Options** section of the visualization editor for timeline charts.
### `color_application`
The `color_application` parameter, and its subparameters `collection_id` and `palette_id`, can be used to apply a specific color collection and palette to a dashboard element. For an overview of Looker's native color collections, see the Color collections documentation page.
If you have the collection ID and palette ID for the palette you want to use, you can enter those IDs into the `collection_id` and `palette_id` subparameters. A collection ID or a palette ID may be an alphanumeric code or be based on the name of the color collection. Alphanumeric codes are used for Looker's native collections. They are instance-specific and look like this:
```

color_application:
  collection_id: 1297dk12-86a7-4xe0-8dfc-82de20b3806a
  palette_id: 93c8aeb7-3f8a-4ca7-6fee-88c3617516a1


```

Custom color collections use collection and palette IDs based on the name of the color collection, which are portable across instances and look like this:
```

color_application:
  collection_id: blue-tone-collection
  palette_id: blue-tone-collection-categorical-0


```

You can also use the UI to find the colors, collections, or palettes that you want and generate the LookML to add them to your dashboard. Navigate to a piece of user-defined content (like a Look, a dashboard, or an Explore), and apply the colors, collection, or palette that you want to that content's visualization using the UI. Once you've done that, you can follow the steps to get dashboard LookML, copy the LookML that was produced, and paste it in the `color_application` section.
### `groupBars`
Determine whether the visualization should display each record bar in its own row, or if the record bars for each label value should all be in the same row. If you set `groupBars` to `true`, all records that share the same label value appear as individual bars on the same row in the visualization.
```

groupBars: true | false


```

### `labelSize`
Specify a font size for the labels. For example:
```

labelSize: 12pt


```

### `valueFormat`
Specify the number format or date format for the value. The parameter accepts Excel-style formatting. If no formatting is specified, the value will be displayed in the format of the underlying dimension or measure.
### `showLegend`
Display or hide a legend at the bottom of the visualization.
```

showLegend: true | false


```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


