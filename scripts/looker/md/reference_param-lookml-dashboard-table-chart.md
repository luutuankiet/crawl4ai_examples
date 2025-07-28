# Table chart parameters for LookML dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-table-chart

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Parameter definitions
  * Basic parameters
  * Query parameters
    * filter_expression
  * Column parameters
    * auto_size_all_columns
  * Plot parameters
    * show_row_numbers
    * limit_displayed_rows
    * limit_displayed_rows_values
  * Series parameters
    * series_column_widths
    * series_cell_visualizations
    * series_text_format
    * series_collapsed
    * series_value_format
  * Formatting parameters
    * color_application
    * header_font_color
    * header_background_color
    * header_text_alignment
    * header_font_size
    * enable_conditional_formatting
    * conditional_formatting_include_totals
    * conditional_formatting_include_nulls
    * conditional_formatting




Was this helpful?
Send feedback 
#  Table chart parameters for LookML dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Parameter definitions
  * Basic parameters
  * Query parameters
    * filter_expression
  * Column parameters
    * auto_size_all_columns
  * Plot parameters
    * show_row_numbers
    * limit_displayed_rows
    * limit_displayed_rows_values
  * Series parameters
    * series_column_widths
    * series_cell_visualizations
    * series_text_format
    * series_collapsed
    * series_value_format
  * Formatting parameters
    * color_application
    * header_font_color
    * header_background_color
    * header_text_alignment
    * header_font_size
    * enable_conditional_formatting
    * conditional_formatting_include_totals
    * conditional_formatting_include_nulls
    * conditional_formatting


This page demonstrates how to add and customize a LookML dashboard element of `type: looker_grid` with LookML dashboard parameters in a `dashboard.lkml` file.
For information about building a table chart through the Looker UI, see the Table chart options documentation page.
## Example usage
```

## BASIC PARAMETERS
name: element_name
title: 'Element Title'
type: looker_grid
height: N
width: N
top: N
left: N
row: N
col: N
refresh: N (seconds | minutes | hours | days)
note_state: collapsed | expanded
note_display: above | below | hover
note_text: 'note text'

## QUERY PARAMETERS
model: model_name
explore: explore_name
fields: [view_name.field_name, view_name.field_name, …]
dimensions: [view_name.field_name, view_name.field_name, …]
measures: [view_name.field_name, view_name.field_name, …]
sorts: [view_name.field_name asc | desc, view_name.field_name, …]
pivots: [view_name.field_name, view_name.field_name, …]
fill_fields: [view_name.field_name, view_name.field_name, …]
subtotals: [view_name.field_name, view_name.field_name, …]
total: true | false
row_total: right | left | false
limit: N
column_limit: N
filters:
  view_name.field_name: 'Looker filter expression' | 'filter value'
filter_expression:  'Looker custom filter expression'
listen:
  dashboard_filter_name: view_name.field_name
query_timezone: 'specific timezone' | user_timezone
analysis_config: # can only be used when the Forecasting Labs feature is enabled
  forecasting:
  - confidence_interval: N
    field_name: view_name.field_name
    forecast_n: N
    forecast_interval: day | month | a time frame with dimension fill
    seasonality: N
merged_queries:
- 'primary query definition'
- 'next source query definition'
  join_fields:
  - field_name: view_name.field_name
    source_field_name: view_name.field_name

## COLUMN PARAMETERS
auto_size_all_columns: true | false
column_order: [view_name.field_name, view_name.field_name, …]
pinned_columns:
    view_name.field_name: left

## PLOT PARAMETERS
table_theme: editable | white | gray | transparent | unstyled
show_row_numbers: true | false
hide_totals: true | false
hide_row_totals: true | false
transpose: true | false
hidden_fields: [view_name.field_name, view_name.field_name, …]
limit_displayed_rows: true | false
limit_displayed_rows_values:
  show_hide: show | hide
  first_last: first | last
  num_rows: 'N'

## SERIES PARAMETERS
truncate_text: true | false
show_view_names: true | false
size_to_fit: true | false
dynamic_fields:
- table_calculation: {'table calculation definition'}
- measure: {'custom measure or custom filtered measure definition'}
- dimension: {'custom dimension definition'}
series_labels:
    view_name.field_name: 'Series Label'
series_column_widths:
    view_name.field_name: N
series_cell_visualizations:
    view_name.field_name:
        is_active: true | false
        palette:
            palette_id: 'palette ID'
            collection_id: 'collection ID'
            custom_colors:
            - 'color value'
        value_display: true | false
series_text_format:
    view_name.field_name:
        fg_color: 'color value'
        bg_color: 'color value'
        bold: true | false
        italic: true | false
        align: left | center | right
series_collapsed:
    view_name.field_name: true | false
series_value_format:
    view_name.field_name:
        format_string: 'value formatting string'

## FORMATTING PARAMETERS
color_application:
    collection_id: 'collection ID'
    palette_id: 'palette ID'
header_font_color: 'color value'
header_background_color: 'color value'
header_text_alignment: left | center | right
header_font_size: N
rows_font_size: N
enable_conditional_formatting: true | false
conditional_formatting_include_totals: true | false
conditional_formatting_include_nulls: true | false
conditional_formatting:
  {'desired conditional formatting'}


```

## Parameter definitions
Parameter Name | Description  
---|---  
Basic Parameters  
`name` (for elements) | Creates an element  
`title` (for elements) | Changes the way an element name appears to users  
`type` (for elements) | Determines the type of visualization to be used in the element  
`height` (for elements) | Defines the height of an element in units of `tile_size` for `layout: tile` and `layout: static` dashboards  
`width` (for elements) | Defines the width of an element in units of `tile_size` for `layout: tile` and `layout: static` dashboards  
Defines the top-to-bottom position of an element in units of `tile_size` for `layout: static` dashboards  
Defines the left-to-right position of an element in units of `tile_size` for `layout: static` dashboards  
Defines the top-to-bottom position of an element in units of rows for `layout: newspaper` dashboards  
Defines the left-to-right position of an element in units of columns for `layout: newspaper` dashboards  
`refresh` (for elements) | Sets the interval at which the element will automatically refresh  
Defines whether the note will be collapsed or expanded if it is too big to fit on a single row within the element's width  
Defines where the note displays on an element  
Specifies the text that displays in the note  
Query Parameters  
Defines the model to be used for the element's query  
`explore` (for elements) | Defines the Explore to be used for the element's query  
Defines the fields to be used for the element's query. This can be used in place of `dimensions` and `measures`.  
Defines the dimensions to be used for the element's query  
Defines the measures to be used for the element's query  
Defines the sorts to be used for the element's query  
Defines the dimensions that should be pivoted to be used for the element's query  
Defines the dimensions that utilize the dimension fill option  
Defines the fields that are subtotaled  
Specifies whether column totals are displayed for a table visualization  
Specifies whether row totals are displayed for a table visualization  
Defines the row limit to be used for the element's query  
Defines the column limit to be used for the element's query  
`filters` (for elements) | Defines the filters that _cannot_ be changed for the element's query  
`filter_expression` | Defines a custom filter that _cannot_ be changed for the element's query  
Defines the filters that _can_ be changed for the element's query, if `filters` (for dashboard) have been created   
Defines the time zone that should be used when the query is run  
Added 21.14  Defines the forecast analysis that should be performed when the query is run. Requires the **Forecasting** Labs feature to be enabled.   
Defines a merged results query  
Column Parameters  
`auto_size_all_columns` | Autosizes each table column to the width of its column heading or longest data value, whichever is wider  
Orders the columns in the table chart  
Defines the columns to be pinned, or frozen, on the left side of the table chart  
Plot Parameters  
Applies one of five table coloring options to a table visualization  
`show_row_numbers` | Sets whether to show a row number at the beginning of each table row  
Sets whether a table visualization displays column totals  
Sets whether a table visualization displays row totals  
Sets whether to transpose table rows into columns  
Specifies any fields to use in the query but hide from the chart  
`limit_displayed_rows` | Shows or hides rows in a visualization based on their position in the results  
Series Parameters  
Shortens column headers and text inside data cells with an ellipsis (…)  
Shows the view name along with the field name for each column header  
Automatically sizes the widths of all columns so that the table perfectly fits the width of the element in which it is being viewed  
Includes table calculations or custom fields in your table chart  
Specifies a custom label for each column in the visualization  
`series_column_widths` | Specifies specific widths for columns in the visualization  
`series_cell_visualizations` | Specifies whether columns use the **Cell Visualization** visualization option. This parameter has the subparameters `is_active`, `palette`, and `value_display`.  
`series_text_format` | Specifies cell text layout for each column. This parameter has the subparameters `fg_color`, `bg_color`, `bold`, `italic`, and `align`.  
`series_collapsed` | Specifies whether a column that has subtotals will appear collapsed  
`series_value_format` | Defines the value format for a column using custom formatting  
Formatting Parameters  
`color_application` | Applies colors to cell visualizations and conditional formatting  
`header_font_color` | Applies a font color to column headers  
`header_background_color` | Applies a color to the backgrounds of column headers  
`header_text_alignment` | Applies left, right, or center alignment to column headers  
`header_font_size` | Applies a font size to column headers  
Applies a font size to text inside data cells  
`enable_conditional_formatting` | Sets to `true` to define color coding rules for a table visualization  
`conditional_formatting_include_totals` | Specifies whether totals are included in the color coding scheme  
`conditional_formatting_include_nulls` | Specifies whether null values should be represented as a zero  
`conditional_formatting` | Uses `conditional_formatting` and its subparameters to define the rules that color code your table visualization  
## Basic parameters
When defining a LookML dashboard element, you must specify values for at least the `name` and `type` parameters. Other basic parameters like `title`, `height`, and `width` affect the position and appearance of an element on a dashboard.
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
### `note_state`
The `note_state` parameter defines whether a note will be collapsed or expanded if it is too big to fit on a single row within the element's width. If you choose `collapsed` and the note is too long, the note will end in a clickable ellipsis (`...`) that can be used to read the full note. If you choose `expanded` and the note is long, the note will run onto additional lines.
### `note_display`
The `note_display` parameter defines where a note is displayed on an element. `above` places the note at the top of an element, `below` places it at the bottom of an element, and `hover` requires the user to hover their mouse over a `?` icon to see the note.
### `note_text`
The `note_text` parameter specifies the text displayed in an element note.
## Query parameters
When defining a LookML dashboard element, you must specify values for at least the `model` and `explore` query parameters, and at least one field must be specified using the `dimensions` parameter, the `measures` parameter, or the `fields` parameter. You can also use the other query parameters that are described in this section to control the way data is displayed in a dashboard element.
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
### `fields`
The `fields` parameter defines the fields to use for the element query. Use the syntax `view_name.dimension_name` to specify the fields.
```
## single field example
- name: orders_by_date
  fields: order.order_date

## multiple fields example
- name: orders_by_date
  fields: [order.order_date, order.order_count]

```

If you use the `fields` parameter, you do not need to use the `dimensions` and `measures` parameters.
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

### `fill_fields`
The `fill_fields` parameter defines the dimensions that utilize the dimension fill option. Use the syntax `view_name.dimension_name` to specify the dimensions.
```
- name: orders_by_date
  fill_fields: [orders.created_date, orders.shipped_date]

```

### `subtotals`
The `subtotals` parameter defines the dimensions that utilize the subtotals option. Use the syntax `view_name.dimension_name` to specify the dimensions.
```
subtotals: [products.department, distribution_centers.name]

```

### `total`
The `total` parameter sets whether a totals row is shown at the bottom of the table. See Displaying totals for more information.
```
total: true | false

## default value: false

```

### `row_total`
The `row_total` parameter sets whether a totals column is shown on the right or left of the table. Only works if a pivot is present. See Displaying Totals for more information.
```
row_total: right | left | false

## default value: false

```

### `limit`
The `limit` parameter defines the row limit that should be used for the element query. The limit applies to the number of rows **before** any pivots are applied.
```
- name: orders_by_date
  limit: 100

```

### `column_limit`
The `column_limit` parameter defines the column limit that should be used for the element query. The limit applies to the number of columns **after** any pivots are applied.
```
- name: orders_by_date
  column_limit: 100

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
### `filter_expression`
The `filter_expression` parameter defines a non-changeable custom filter for the element's query. If you would like filters that a user _can_ change in the dashboard, you should set up the filters using `filters` for dashboards, then apply them to the elements using `listen`.
```
- name: element_name
  filter_expression:
  - diff_days(${users.created_date},${user_order_facts.first_order_date}) > 60

```

The Looker filter expressions documentation page lists the Looker filter expressions.
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

### `analysis_config`
The `analysis_config` parameter and its subparameters describe any query analysis to use with the visualization, starting in Looker 21.14. The **Forecasting** Labs feature must be enabled to perform analyses on visualizations.
The following subparameters can be used to define analyses:
  * `confidence_interval`
  * `forecast_interval`


You can create a forecast using a syntax like this:
```

  analysis_config:
    - forecasting:
      confidence_interval: 0.95
      field_name: orders.count
      forecast_n: 14
      forecast_interval: day
      seasonality: 7

```

#### `forecasting`
`forecasting` is an analysis type that applies a forecast to a visualization. Forecasting lets analysts quickly add data projections to new or existing Explore queries to help users predict and monitor specific data points.
For more information, see the Forecasting in visualizations documentation page.
To add forecasts to visualizations, the **Forecasting** Labs feature must be enabled.
#### `confidence_interval`
`confidence_interval` sets the bounds of the forecasted data values, which are input as decimal expressions of percentages. `confidence_interval` is optional and is blank by default.
```

confidence_interval: 0.99 | 0.98 | 0.95 | 0.90 | 0.80


```

See the Prediction interval section on the **Forecasting in visualizations** documentation page.
To add forecasts to visualizations, the **Forecasting** Labs feature must be enabled.
#### `field_name`
`field_name` specifies the names of measures — up to five — to include in forecasts.
```

field_name: view_name.field_name


```

#### `forecast_n`
`forecast_n` specifies the length of the forecast.
```

forecast_n: N # An integer that represents the length of the forecast


```

See the Length section on the **Forecasting in visualizations** documentation page.
To add forecasts to visualizations, the **Forecasting** Labs feature must be enabled.
#### `forecast_interval`
`forecast_interval` sets the duration interval for which to forecast data values. `forecast_interval` is automatically populated based on the timeframe dimension in the Explore query.
```

forecast_interval: day | month # a timeframe with dimension fill


```

See the **Length** documentation page.
To add forecasts to visualizations, the **Forecasting** Labs feature must be enabled.
#### `seasonality`
`seasonality` lets analysts account for known cycles or repetitive data trends in a forecast. `seasonality` is optional and is blank by default.
```

seasonality: N # An integer that represents the number of rows over which a cycle or pattern repeats


```

The **Automatic** seasonality setting is represented as a blank `seasonality` value.
See the Seasonality section on the **Forecasting in visualizations** documentation page.
To add forecasts to visualizations, the **Forecasting** Labs feature must be enabled.
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
## Column parameters
The following parameters correspond to the ability to move and pin columns in table charts.
### `auto_size_all_columns`
The `auto_size_all_columns` parameter autosizes each table column to the width of its column heading or longest data value, whichever is wider. This parameter overrides the `series_column_widths` and `size_to_fit` parameters, if they are defined.
```
- name: orders_by_date
  auto_size_all_columns: true

```

### `column_order`
The `column_order` parameter defines the order of the columns in the table chart.
```
- name: orders_by_date
  column_order: [customer.city, customer.state, customer.count]

```

### `pinned_columns`
The `pinned_columns` parameter defines any columns that are pinned to the left of the table chart.
```
- name: orders_by_date
  pinned_columns:
    orders.created_date: left
    distribution_centers.name: left

```

## Plot parameters
The following parameters correspond to the options in the **Plot** menu of the visualization editor for table charts.
### `table_theme`
Use the `table_theme` parameter to apply one of the following table coloring options to a table element:
  * `editable`: The table has blue dimensions, orange measures, and green table calculations.
  * `white`: The table header is white, the data rows alternate between white and gray, and the text is black.
  * `gray`: The table header is gray, the data rows alternate between white and light gray, and the text is dark gray.
  * `transparent`: The table header is totally transparent, the data rows alternate between totally transparent and translucent gray, and the text color adjusts itself from black to white as needed according to the background color that shows through. Setting `table_theme` to `transparent` can be useful when you're using a customized embedded dashboard so that the tile background color shows through the visualization.
  * `unstyled`: The table header and data rows are white, and the text is black.

```

table_theme: editable | white | gray | transparent | unstyled


```

### `show_row_numbers`
The `show_row_numbers` parameter sets whether a row number will be displayed at the beginning of each table row.
```

show_row_numbers: true | false


```

### `hide_totals`
If your Explore includes column totals, `hide_totals` sets whether the visualization displays the totals.
```

hide_totals: true | false


```

### `hide_row_totals`
If your Explore includes row totals, `hide_row_totals` sets whether the row totals will display in the visualization.
```

hide_row_totals: true | false


```

### `transpose`
The `transpose` parameter lets you transpose table rows into columns. It accepts `true` or `false`.
```
- name: orders_by_date
  transpose: true

```

### `hidden_fields`
The `hidden_fields` parameter indicates which fields, if any, are used in the query but hidden in the chart. Any hidden fields will appear in the data table section of an Explore.
```
hidden_fields: [inventory_items.count, distribution_centers.id]

```

### `limit_displayed_rows`
The `limit_displayed_rows` parameter lets you show or hide rows in a visualization, based on their position in the results. For example, if your visualization displays a 7-day rolling average, you may want to hide the first 6 rows. Setting this to `true` lets you specify the values and positions in the visualization to which this applies using the `limit_displays_rows_values` parameter and its subparameters.
```
limit_displayed_rows: true
limit_displayed_rows_values:
  show_hide: hide | show
  first_last: first | last
  num_rows: '10'


```

### `limit_displayed_rows_values`
Use the `limit_displayed_rows_values` parameter, and its subparameters `show_hide`, `first_last`, and `num_rows`, with `limit_displayed_rows` to specify which rows to show or hide in a visualization. See the `limit_displayed_rows` section for sample usage.
#### `show_hide`
The `show_hide` subparameter sets whether to hide certain rows from the visualization. Set `show_hide` to `show` to display only a limited number of rows in the visualization, and set `show_hide` to `hide` to exclude certain rows from the visualization.
#### `first_last`
The `first_last` subparameter sets whether the rows to be hidden or shown will be the first or last rows in the result set. Setting `first_last` to `first` shows or hides the first rows, while set `first_last` to `last` shows or hides the last rows.
#### `num_rows`
The `num_rows` subparameter sets the number of rows to be hidden or shown. For example, `num_rows: '10'` will show or hide either the first or last 10 rows of the result set from the visualization.
## Series parameters
The following parameters correspond to the options in the **Series** menu of the visualization editor for table charts.
### `truncate_text`
The `truncate_text` parameter sets whether column headers and text inside data cells should be shortened with an ellipsis (…).
```

truncate_text: true | false


```

### `show_view_names`
The `show_view_names` parameter determines whether view names are displayed in chart labels, such as axis names and column names.
```
show_view_names: true | false

## default value: true

```

### `size_to_fit`
The `size_to_fit` parameter sets whether to size the widths of all columns so that the table perfectly fits the width of the element in which it is being viewed. If the `auto_size_all_columns` parameter is set to `true`, it overrides `size_to_fit`.
```

size_to_fit: true | false


```

### `dynamic_fields`
The `dynamic_fields` parameter and its subparameters describe any table calculations or custom fields to use with the visualization. You must have permission to create custom fields to add a `description` of up to 255 characters or to use `calculation_type` for custom groups or custom bins. You must have permission to create table calculations to add a `description` of up to 255 characters to table calculations or to use `calculation_type` for shortcut calculations.
The following subparameters can be used to define dynamic fields:
  * `table_calculation`


You can create a table calculation using a syntax like this:
```
dynamic_fields:
  - table_calculation: running_total
    label: Running Total of Items
    expression: running_total(${inventory_items.count})
    value_format_name: decimal_0
    description: your description of up to 255 characters here
    _kind_hint: measure
    _type_hint: number
    is_disabled: false

```

You can create shortcut calculations for several calculation types using a syntax like this:
```
dynamic_fields:
- category: table_calculation
  description: your description of up to 255 characters here
  label: Percent of Orders Count
  value_format:
  value_format_name: percent_0
  calculation_type: percent_of_column_sum
  table_calculation: percent_of_orders_count
  args:
  - orders.count
  _kind_hint: measure
  _type_hint: number
- category: table_calculation
  description: your description of up to 255 characters here
  label: Percent of previous - Orders Count
  value_format:
  value_format_name: percent_0
  calculation_type: percent_of_previous
  table_calculation: percent_of_previous_orders_count
  args:
  - orders.count
  _kind_hint: measure
  _type_hint: number
- category: table_calculation
  description: your description of up to 255 characters here
  label: Percent change from previous - Orders Count
  value_format:
  value_format_name: percent_0
  calculation_type: percent_difference_from_previous
  table_calculation: percent_change_from_previous_orders_count
  args:
  - orders.count
  _kind_hint: measure
  _type_hint: number
- category: table_calculation
  description: your description of up to 255 characters here
  label: Rank of Orders Count
  value_format: ## this field is optional
  value_format_name: ## this field is optional
  calculation_type: rank_of_column
  table_calculation: rank_of_orders_count
  args:
  - orders.count
  _kind_hint: measure
  _type_hint: number
- category: table_calculation
  description: your description of up to 255 characters here
  label: Running total of Orders Count
  value_format: ## this field is optional
  value_format_name: ## this field is optional
  calculation_type: running_total
  table_calculation: running_total_of_orders_count
  args:
  - orders.count
  _kind_hint: measure
  _type_hint: number


```

You can create a custom measure to use in your visualization using a syntax like this:
```
dynamic_fields:
  - measure: avg_sale_price
    label: Average Sale Price
    based_on: products.sale_price
    type: average
    value_format_name: usd
    description: your description of up to 255 characters here
    _kind_hint: measure
    _type_hint: number

```

You can create a filtered custom measure to use in your visualization using a syntax like this:
```
dynamic_fields:
  - measure: order_count_for_25_47_year_olds
    based_on: order_items.order_count
    type: count_distinct
    label: Order Count for 25- to 47-Year-Olds
    description: your description of up to 255 characters here
    value_format: 00#
    _kind_hint: measure
    _type_hint: number
    filter_expression: "${users.age} >= 25 AND ${users.age} <= 47"

```

You can create a custom dimension to use in your visualization using a syntax like this:
```
dynamic_fields:
  - dimension: user_city_state
    label: User City and State
    expression: concat(${users.city}, ", ", ${users.state})
    description: your description of up to 255 characters here
    _kind_hint: dimension
    _type_hint: string

```

You can create custom groups for a dimension to use in your visualization using a syntax like this:
```
  - category: dimension
  description: 'States by region'
  label: State Groups
  value_format: ## this field is optional
  value_format_name: ## this field is optional
  calculation_type: group_by
  dimension: state_groups
  args:
  - users.state
  - - label: Pacific Northwest
      filter: Oregon,Idaho,Washington
  - Other
  _kind_hint: dimension
  _type_hint: string

```

You can create custom bins for a dimension to use in your visualization using a syntax like this:
```
- category: dimension
  description: Order item sale prices, in tiers of 10
  label: Sale Price Bins
  value_format:
  value_format_name:
  calculation_type: bin
  dimension: sale_price_bins
  args:
  - order_items.sale_price
  - '10'
  - '0'
  - '100'
  -
  - classic
  _kind_hint: dimension
  _type_hint: string

```

You can add multiple dynamic fields to your element. You do not need to add table calculations to the `fields` parameter for them to appear in the visualization, but you do need to add other types of dynamic fields to `fields` in order for them to appear.
#### `table_calculation`
If you are defining a table calculation, the `table_calculation` subparameter names the table calculation. This is the name to use when you reference the table calculation in LookML.
#### `measure`
The `measure` subparameter defines the name for a custom measure or a filtered custom measure. This is the name you use to reference the measure in LookML.
#### `dimension`
The `dimension` subparameter defines the name for a custom dimension. This is the name to use to reference the dimension in LookML.
#### `label`
The `label` subparameter defines the title of the dynamic field as you'd like it to appear in the visualization. This may be the same as or different than the name given in the `table_calculation`, `measure`, or `dimension` subparameters.
#### `based_on`
If you are using a custom measure or a filtered custom measure, the `based_on` subparameter identifies the measure it is based on, using the `view_name.field_name` sytax.
#### `type`
If you are using a custom measure, the `type` subparameter identifies the type of aggregation. It accepts `count_distinct`, `sum`, `average`, `min`, `max`, or `median`.
#### `description`
You can add a description of up to 255 characters to any custom field or table calculation with the `description` subparameter. Looker displays the description when the user clicks on the information icon to the right of the field name in the field picker, and when the user hovers over the column name in a table or table chart visualization in an Explore, a dashboard, or a Look.
#### `expression`
If you are using a table calculation, the `expression` subparameter defines the Looker expression used to create the table calculation.
#### `filter_expression`
If you are using a custom filtered measure, the `filter_expression` subparameter defines the Looker expression used to filter the measure.
#### `value_format`
The optional `value_format` subparameter defines the value format for a dynamic field when you're using custom formatting. If you want to use a default Looker format, use `value_format_name` instead.
#### `value_format_name`
The optional `value_format_name` subparameter applies a default format to the dynamic field. If you want to use a custom format, use `value_format` instead.
#### `calculation_type`
The `calculation_type`subparameter defines the type of **Shortcut Calculation** or **Group** function to create a table calculation, or to create a custom group for a dimension:
**Custom fields`calculation_type` options:**
  * **`group_by`**— Groups dimension values under custom fixed labels, based on a specified custom condition. Similar to`CASE WHEN` in SQL, or the LookML `case` field parameter.
  * **`bin`**— Groups values in custom bins, or tiers, for numeric type dimensions and custom dimensions. Similar to the LookML`tier` dimension type.


**Table calculations`calculation_type` options:**
  * **`percent_of_column_sum`**— A row value divided by the sum of values in the column. This calculation only includes values that are in the data table when the query row limit has been reached.
  * **`percent_of_previous`**— A current row's value divided by the value of the following row.
  * **`percent_difference_from_previous`**— The difference between the current row's value and the value of the following row, divided by the value of the following row.
  * **`rank_of_column`**— The rank of a row's value among all values in the column. This calculation only includes values that are in the data table when the query row limit has been reached.
  * **`running_total`**— The cumulative sum of the current row's value and all previous row values in the column.
  * **`percent_of_previous_column`**— For pivoted fields, the current column's value divided by the value of the column to its left.
  * **`percent_change_from_previous_column`**— For pivoted fields, the difference between the current column's value and the value of the column to the left, divided by the value of the column to the left.
  * **`percent_of_row`**— For pivoted fields, the percent of the current column's value divided by the row sum of that field.
  * **`running_row_total`**— For pivoted fields, the cumulative sum of the current column and all previous columns in this row.


####  `args` for custom groups
If you are using custom groups for a dimension, `args` specifies the arguments for applying fixed labels to dimension values. `args` takes the following format:
```
args:
- view_name.field_name
  - label: specified custom label
    filter: condition for values
  - label: another specified custom label
    filter: a different condition for values
- Other ## An optional customizable group label for values that do not meet specified conditions.

```

You can add as many `label` and `filter` conditions as needed, depending on the number of groups desired.
See the previous example for reference.
####  `args` for custom bins
If you are using custom bins for a numeric dimension, `args` specifies the arguments for applying fixed tiers to dimension values. `args` takes the following format:
```
  args:
  - view_name.field_name
  - bin_size ## The numeric interval on which to base each bin, in single quotes
  - min ## The numeric value of the minimum bin size, in single quotes
  - max ## The numeric value of the maximum bin size, in single quotes
  - override ## A value will only appear when a custom bin uses a Custom-sized bin type.
  - style ## The bin display style. Currently, only classic is supported.

```

See the previous example for reference.
####  `args` for shortcut calculations
The `args` subparameter is where you specify the names of the numeric fields that you are using for a **Shortcut Calculation**. An argument takes the following format:
```
- args:
  - view_name.field_name   ## the field on which the calculation is based

```

See the previous example for reference.
#### `_kind_hint`
The optional `_kind_hint` subparameter identifies whether the dynamic field returns a dimension or measure. It accepts the values `dimension` and `measure`.
#### `_type_hint`
The optional `_type_hint` subparameter identifies the data type the dynamic field's expression should produce.
#### `is_disabled`
The optional `is_disabled` subparameter specifies whether a table calculation appears in the visualization and its underlying Explore. It accepts the values `true` and `false`.
### `series_labels`
Set the labels of one or more series based on the series name, using `name: label` pairs.
For a pivoted chart, the series names are the pivot names.
```
series_labels:
  'Yes': iOS Users
  'No': Android Users

```

For a chart with multiple measures, the series names are the measure field names.
```
series_labels:
  inventory_items.count: Inventory
  orders.count: Orders

```

### `series_column_widths`
Set the widths of one or more columns based on the series name. If the `auto_size_all_columns` parameter is set to `true`, it overrides `series_column_widths`.
```
series_column_widths:
  order_times.shipping_time: 50
  orders.count: 60

```

### `series_cell_visualizations`
Specify whether one or more columns use the **Cell Visualization** option by indicating series name using the `view_name.field_name` format. `series_cell_visualizations` has the subparameters `is_active`, `palette`, and `value_display`.
```
series_cell_visualizations:
  order_items.count:
    is_active: true
    palette:
      palette_id: my-custom-colors-sequential-0
      collection_id: my-custom-colors
    value_display: true

```

#### `is_active`
The optional `is_active` subparameter accepts `true` or `false` to indicate whether bar visualizations are enabled for that series. If `is_active` is not defined, it defaults to `true`.
#### `palette`
The `palette` subparameter is optional. If it is not used, the palette will default to a diverging palette in the instance's default color collection.
If `palette` is used, the child parameters `palette_id` and `collection_id` apply the colors from a specific palette to the bar visualizations. For `palette_id`, you must use the ID of a sequential or diverging palette. For more on palette IDs and color collection IDs, see the `color_application` section.
`palette` has an alternate child parameter, `custom_colors`, that sets two to five custom colors to use for the bars:
```
series_cell_visualizations:
  order_items.count:
    palette:
      custom_colors:
      - orange
      - "#0000ff"
      - red

```

#### `value_display`
The optional `value_display` subparameter accepts `true` or `false` to indicate whether the values for each data cell are shown along with the cell visualization. If `value_display` is not defined, it defaults to `true`.
### `series_text_format`
The `series_text_format` parameter and its subparameters specify cell text layout for each column. The series to be formatted is indicated using the `view_name.field_name` syntax, and the subparameters describe the formatting.
All subparameters are optional; only use the ones you need.
```
  series_text_format:
    order_items.shipping_time:
      align: right
    order_items.shipped_date:
      align: center
      fg_color: "#EA8A2F"
      bg_color: "#64518A"
      bold: true
      italic: true

```

#### `fg_color`
The `fg_color` subparameter indicates the font color for cell text. The color value can take a hex string, such as `#2ca6cd`, or a CSS named color string, such as `mediumblue`.
#### `bg_color`
The `bg_color` subparameter indicates the cell background color. The color value can take a hex string, such as `#2ca6cd`, or a CSS named color string, such as `mediumblue`.
#### `bold`
The `bold` subparameter indicates whether the cell text is bold and accepts `true` or `false`.
#### `italic`
The `italic` subparameter indicates whether the cell text is italic and accepts `true` or `false`.
#### `align`
The `align` subparameter indicates the alignment of cell text and accepts `left`, `center`, or `right`.
### `series_collapsed`
The `series_collapsed` parameter defines whether to collapse or expand the subtotals for a particular series. Identify the series using `view_name.field_name` syntax and `true` or `false`.
```
series_collapsed:
  users.city: false
  users.state: true

```

If the column is collapsed, the individual elements that make up the subtotal will be displayed by clicking the arrow on the left side of the data cell.
### `series_value_format`
The `series_value_format` parameter specifies the formatting to apply to a series, independent of any formatting applied to the underlying dimension or measure. If `series_value_format` is not specified, the value is displayed in the format of the underlying dimension or measure.
Identify the series to be formatted using the `view_name.field_name` syntax.
The `format_string` subparameter lets you define the format for the series, using Excel-style formatting.
```
series_value_format:
  products.retail_price:
    format_string: "$#,##0.00"

```

You can also define the formatting like this:
```

series_value_format:
  order_items.count: "00#"


```

The formatting used in the `format_string` subparameter is the same as formatting used with the `value_format` LookML parameter. You can read about how to specify these formats on the Adding custom formatting to numeric fields documentation page.
## Formatting parameters
The following parameters correspond to the options in the **Formatting** menu of the visualization editor for table charts.
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
### `header_font_color`
The `header_font_color` parameter applies a font color to column headers.
The color value can take a hex string, such as `#2ca6cd`, or a CSS named color string, such as `mediumblue`.
```

header_font_color: purple


```

The default color depends on the table theme defined using the `table_theme` parameter.
### `header_background_color`
The `header_background_color` parameter applies a color to the background column headers.
The color value can take a hex string, such as `#2ca6cd`, or a CSS named color string, such as `mediumblue`.
```

header_background_color: #add8e6


```

The default color depends on the table theme defined using the `table_theme` parameter.
### `header_text_alignment`
The `header_text_alignment` parameter applies `left`, `right`, or `center` alignment to column headers.
```

header_text_alignment: center


```

The default alignment is `left`.
### `header_font_size`
The `header_font_size` parameter applies a font size from `1` through `99` to column headers.
```

header_font_size: 16


```

The default size for header and row fonts is `12`.
### `rows_font_size`
The `rows_font_size` parameter applies a font size from `1` through `99` to text inside data cells, but not to column headers.
```

rows_font_size: 8


```

The default size for header and row fonts is `12`.
### `enable_conditional_formatting`
Setting `enable_conditional_formatting` to `true` lets you define rules that color code your table visualization, either on a scale or by specifying values of interest.
```

enable_conditional_formatting: true | false


```

### `conditional_formatting_include_totals`
If `enable_conditional_formatting` is set to `true`, `conditional_formatting_include_totals` specifies whether totals are included in the color coding scheme.
```

conditional_formatting_include_totals: true | false


```

### `conditional_formatting_include_nulls`
If `enable_conditional_formatting` is set to `true`, `conditional_formatting_include_nulls` specifies whether null values should be represented as zeroes.
```

conditional_formatting_include_nulls: true | false


```

### `conditional_formatting`
With `enable_conditional_formatting` set to `true`, use the `conditional_formatting` parameter to define the rules that color code your table visualization. For each conditional formatting rule, you can specify settings with the following parameters:


The following is an example of a conditional formatting rule:
```

conditional_formatting: [{type: less than, value: 20, background_color: "#9fdee0",
  font_color: "#b15928", bold: true, italic: false, strikethrough: false,
  fields: [order_items.count], color_application: {collection_id: my-custom-colors,
  palette_id: my-custom-colors-sequential-0}}]


```

#### `type`
The `type` parameter specifies whether to color code values along a scale or based on a logical condition.
If you are color coding values on a scale, you can set `type` to `along a scale...`.
If you are color coding values based on a logical condition, you can specify one of the following values for `type`, along with a value for `value`:
  * `equal to`: The rule applies to values equal to the number specified for `value`.
  * `not equal to`: The rule applies to values that are not equal to the number specified for `value`.
  * `greater than`: The rule applies to values that are greater than the number specified for `value`.
  * `less than`: The rule applies to values that are less than than the number specified for `value`.
  * `between`: The rule applies to values that are between the two numbers specified for `value`.
  * `not between`: The rule applies to values that are not between the two numbers specified for `value`.
  * `'null'`: The rule applies only to null values.
  * `not null`: The rule applies only to values that are not null.

```

type: along a scale... | equal to | not equal to | less than | between | not between | 'null' | not null


```

#### `value`
If you are color coding values based on a logical condition other than `'null'` or `not null`, specify the value to which the rule applies. The `value` parameter takes a single number or, when `type` is set to `between` or `not between`, a set of two numbers.
```

value: N | [N, N]


```

#### `background_color`
If your color coding is based on a logical condition (`type` is set to anything other than `along a scale...`), use the `background_color` parameter to specify a background color for the values to which your rule applies.
```

background_color: "#49cec1"


```

#### `font_color`
If your color coding is based on a logical condition (`type` is set to anything other than `along a scale...`), use the `font_color` parameter to specify a font color for the values to which your rule applies.
```

font_color: "#1f3e5a"


```

#### `color_application`
The `color_application` parameter, and its subparameters `collection_id`, `palette_id`, and `options`, can be used to apply a specific color collection and palette to a conditional formatting rule.
You can add colors to a LookML dashboard by collection ID and palette ID, if you have them. You can also use the UI to find the colors you want and generate the LookML to add them to your dashboard. Navigate to a piece of user-defined content (like a Look, a dashboard, or an Explore), and apply the colors you want to that content's visualization using the UI. Once you've done that, you can follow the steps to get dashboard LookML, copy the LookML that was produced, and paste it in the `color_application` section. For an overview of Looker's predefined color collections, see the Color collections documentation page.
The `options` subparameter can be used when you have set `type` to `along a scale...`. It has the following child parameters:
  * `steps`: This parameter limits the number of colors used to the value given and separates the data into that number of groups. When this parameter is not used, the data is colored according to a gradient covering the entire palette. It accepts values from `2` through `100`.
  * `mirror`: When set to `true`, this parameter applies equal color shifts on either side of the color palette for equal values on either side of a defined center point. It accepts `true` or `false`.
  * `constraints`: This parameter sets the data range that conditional formatting applies to and sets a center point to be used for palette application. It accepts the following syntax: `constraints: {min: {type: number, value: 3}, max: {type: percentile, value: 99}, mid: {type: average}}`
  * `reverse`: This parameter determines whether to reverse the color palette during color application. It accepts `true` or `false`.


#### `bold`
When color coding based on a logical condition, set whether to bold the values to which your rule applies.
```

bold: true | false


```

#### `italic`
When color coding based on a logical condition, set whether to italicize the values to which your rule applies.
```

italic: true | false


```

#### `strikethrough`
When color coding based on a logical condition, set whether to apply strikethrough formatting to the values for your rule.
```

strikethrough: true | false


```

#### `fields`
Specify the fields to which your rule should apply. By default, the rule applies to all numeric fields.
```

fields: [ view_name.field_name ]


```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


