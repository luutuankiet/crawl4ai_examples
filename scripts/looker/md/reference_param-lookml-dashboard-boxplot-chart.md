# Boxplot chart parameters for LookML dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-boxplot-chart

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Parameter definitions
  * Basic parameters
  * Query parameters
  * Series parameters
    * color_application
  * Style parameters
  * X-axis parameters
    * show_x_axis_label
    * show_x_axis_ticks
    * x_axis_gridlines
  * Y-axis parameters
    * show_y_axis_labels
    * show_y_axis_ticks
    * y_axis_gridlines
    * y_axis_tick_density
    * y_axis_tick_density_custom
    * y_axis_value_format
  * Advanced visualization configuration
    * advanced_vis_config




Was this helpful?
Send feedback 
#  Boxplot chart parameters for LookML dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Parameter definitions
  * Basic parameters
  * Query parameters
  * Series parameters
    * color_application
  * Style parameters
  * X-axis parameters
    * show_x_axis_label
    * show_x_axis_ticks
    * x_axis_gridlines
  * Y-axis parameters
    * show_y_axis_labels
    * show_y_axis_ticks
    * y_axis_gridlines
    * y_axis_tick_density
    * y_axis_tick_density_custom
    * y_axis_value_format
  * Advanced visualization configuration
    * advanced_vis_config


This page demonstrates how to add and customize a LookML dashboard element of `type: looker_boxplot` with LookML dashboard parameters in a `dashboard.lkml` file.
For information about building a boxplot chart through the Looker UI, see the Boxplot chart options documentation page.
## Example usage
An `N` indicates that a numeric value is required. Single quotation marks indicate descriptive text and should not be included in live code.
```

## BASIC PARAMETERS
name: element_name
title: 'Element Title'
type: looker_boxplot
height: N
width: N
top: N
left: N
row: N
col: N
refresh: N (seconds | minutes | hours | days)
note:
  text: 'note text'
  state: collapsed | expanded
  display: above | below | hover

## QUERY PARAMETERS
model: model_name
explore: explore_name
fields: [view_name.field_name, view_name.field_name, view_name.field_name, …]
dimensions: [view_name.field_name, view_name.field_name, …]
measures: [view_name.field_name, view_name.field_name, …]
sorts: [view_name.field_name asc | desc, view_name.field_name, …]
limit: N
filters:
  view_name.field_name: 'looker filter expression'
listen:
  dashboard_filter_name: view_name.field_name
query_timezone: 'specific timezone' | user_timezone
hidden_fields: [view_name.field_name, view_name.field_name, …]

## SERIES PARAMETERS

color_application:
  collection_id: 'collection ID'
  palette_id: 'palette ID'
  options:
    reverse: true | false

## STYLE PARAMETERS

show_view_names: true | false

## X-AXIS PARAMETERS

show_x_axis_label: true | false
x_axis_label: 'desired x-axis label'
show_x_axis_ticks: true | false
x_axis_gridlines: true | false
x_axis_reversed: true | false
x_axis_zoom: true | false

## Y-AXIS PARAMETERS

show_y_axis_labels: true | false
y_axis_labels: ['desired y-axis label']
show_y_axis_ticks: true | false
y_axis_gridlines: true | false
y_axis_min: ['N']
y_axis_max: ['N']
y_axis_tick_density: default | custom
y_axis_tick_density_custom: 'N'
y_axis_reversed: true | false
y_axis_value_format: ['Excel-style formatting']
y_axis_zoom: true | false

## ADVANCED VISUALIZATION CONFIGURATION PARAMETERS
advanced_vis_config: 'Highcharts JSON snippet'


```

## Parameter definitions
Parameter Name | Description  
---|---  
Basic Parameters  
`name` (for elements) | Creates an element  
`title` (for elements) | Changes the way an element name appears to users  
`type` (for elements) | Determines the type of visualization to be used in the element  
`height` (for elements) | Defines the height of an element, in units of `tile_size`, for `layout: tile` and `layout: static` dashboards  
`width` (for elements) | Defines the width of an element, in units of `tile_size`, for `layout: tile` and `layout: static` dashboards  
Defines the top-to-bottom position of an element, in units of `tile_size`, for `layout: static` dashboards  
Defines the left-to-right position of an element, in units of `tile_size`, for `layout: static` dashboards  
Defines the top-to-bottom position of an element, in units of rows, for `layout: newspaper` dashboards  
Defines the left-to-right position of an element, in units of columns, for `layout: newspaper` dashboards  
`refresh` (for elements) | Sets the interval at which the element will automatically refresh  
Starts a section of LookML to define a note for an element. This parameter has subparameters `text`, `state`, and `display`.  
Query parameters  
Defines the model to be used for the element's query  
`explore` (for elements) | Defines the Explore to be used for the element's query  
Defines the fields to be used for the element's query. This can be used in place of `dimensions` and `measures`.  
Defines the dimensions to be used for the element's query  
Defines the measures to be used for the element's query  
Defines the sorts to be used for the element's query  
Defines the row limit to be used for the element's query  
`filters` (for elements) | Defines the filters that _cannot_ be changed for the element's query  
Defines the filters that _can_ be changed for the element's query, if `filters` (for dashboard) have been created  
Defines the time zone that should be used when the query is run  
Specifies any fields to use in the query but to hide in the chart  
Series parameters  
`color_application` | Applies a color collection and palette to the chart  
Style parameters  
Shows or hides view names from chart labels  
X-axis parameters  
`show_x_axis_label` | Shows or hides the x-axis label  
Defines a custom x-axis label  
`show_x_axis_ticks` | Shows values on the x-axis  
`x_axis_gridlines` | Extends gridlines from the x-axis  
Reverses the direction of the x-axis  
Specifies whether to allow zooming along the x-axis  
Y-axis parameters  
`show_y_axis_labels` | Shows or hides the y-axis label  
Defines a custom y-axis label  
`show_y_axis_ticks` | Shows values on the y-axis  
`y_axis_gridlines` | Extends gridlines from the y-axis  
Defines a minimum value for the y-axis  
Defines a maximum value for the y-axis   
`y_axis_tick_density` | Enables the option to set a custom y-axis tick density with the `y_axis_tick_density_custom` parameter  
`y_axis_tick_density_custom` | Defines the density of y-axis ticks when `y_axis_tick_density` is set to `custom`  
Reverses the direction of the y-axis  
`y_axis_value_format` | Defines the number format of y-axis values  
Specifies whether to allow zooming along the y-axis. Disabled if `x_axis_zoom: false`.  
Advanced Visualization Configuration Parameters  
`advanced_viz_config` | Accepts a HighCharts JSON snippet that can override several visualization settings  
## Basic parameters
When defining a LookML dashboard element, you must specify values for at least the basic parameters `name` and `type`. Other basic parameters, such as `title`, `height`, and `width`, affect the appearance and position of an element on a dashboard.
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
When you define a LookML dashboard element, you must specify values for at least the `model` and `explore` query parameters.
Elements of `type: looker_boxplot` also require at least one dimension and either two, three, or five of the following types of measures (which must be listed in this order):
  * **Minimum** : A measure representing the minimum data value. This can be defined in LookML as a measure of `type: min`.
  * **25th percentile** : A measure representing the 25th percentile, or the first quartile. One quarter of your data values are less than or equal to this value. This can be defined in LookML as a measure of `type: percentile` with the value for `percentile` set to `25`.
  * **Median** : A measure representing the median or midpoint of the dataset, or the second quartile. Half of your data values are less than or equal to this value. This can be defined in LookML as a measure of `type: median`.
  * **75th percentile** : A measure representing the 75th percentile, or the third quartile. Three quarters of your data values are less than or equal to this value. This can be defined in LookML as a measure of `type: percentile` with the value for `percentile` set to `75`.
  * **Maximum** : A measure representing the maximum value. This can be defined in LookML as a measure of `type: max`.


You can use the `fields` parameter, or both of the parameters `dimensions` and `measures`, to specify the dimensions and measures that a boxplot element is based on. See the Building a boxplot chart section of the **Boxplot chart options** documentation page for more information on building a boxplot chart in the Looker UI.
You can use the other query parameters described in this section to control the way data is displayed in a dashboard element.
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

### `hidden_fields`
The `hidden_fields` parameter indicates which fields, if any, are used in the query but hidden in the chart. Any hidden fields will appear in the data table section of an Explore.
```
hidden_fields: [inventory_items.count, distribution_centers.id]

```

## Series parameters
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
By default, the first color of the designated palette is applied to the entire boxplot element. The optional subparameter `reverse` switches the application to the last color in the palette.
```
color_application:
  collection_id: blue-tone-collection
  palette_id: blue-tone-collection-categorical-0
  options:
    reverse: true

```

## Style parameters
### `show_view_names`
The `show_view_names` parameter determines whether view names are displayed in chart labels, such as axis names and column names.
```
show_view_names: true | false

## default value: true

```

## X-axis parameters
### `show_x_axis_label`
This parameter determines whether the x-axis label is shown.
```
show_x_axis_label: true | false

## default value: true

```

### `x_axis_label`
This parameter specifies a label for the x-axis. You can use this parameter when `show_x_axis_label` is set to `true`.
```
x_axis_label: Order Date

```

### `show_x_axis_ticks`
This parameter determines whether value labels are shown on the x-axis.
```
show_x_axis_ticks: true | false

## default value: true

```

### `x_axis_gridlines`
This parameter determines whether gridlines are extended from the x-axis.
```
x_axis_gridlines: true | false

## default value: false

```

### `x_axis_reversed`
This parameter sets the direction of the x-axis. When `x_axis_reversed` is set to `false`, values increase from left to right. When it is set to `true`, values decrease from left to right.
```

x_axis_reversed: true | false


```

### `x_axis_zoom`
This parameter specifies whether users can zoom into the x-axis of the visualization. When `x_axis_zoom` is set to `true`, zooming is available. When `x_axis_zoom` is set to `false`, zooming is not available.
If `x_axis_zoom` is set to `false`, `y_axis_zoom` is disabled.
```
x_axis_zoom: true | false

# default value: true

```

## Y-axis parameters
### `show_y_axis_labels`
This parameter determines whether labels are shown on the y-axis.
```
show_y_axis_labels: true | false

## default value: true

```

### y_axis_labels
This parameter specifies a label for the y-axis. You can use this parameter when `show_y_axis_labels` is set to `true`.
```
y_axis_labels: ['label']

```

### `show_y_axis_ticks`
This parameter determines whether values are shown on the y-axis.
```
show_y_axis_ticks: true | false

## default value: true

```

### `y_axis_gridlines`
This parameter determines whether gridlines are extended from the y-axis.
```
y_axis_gridlines: true | false

## default value: true

```

### `y_axis_min`
This parameter defines the minimum value for the y-axis.
```
y_axis_min: ['10']

## default value: true

```

### `y_axis_max`
This parameter defines the maximum value for the y-axis.
```
y_axis_max: ['100']

## default value: true

```

### `y_axis_tick_density`
This parameter enables the option to set a y-axis tick density. Set `y_axis_tick_density` to `custom` to enable this feature, then use the `y_axis_tick_density_custom` parameter to set the density.
```
y_axis_tick_density: default | custom

## default value: default

```

### `y_axis_tick_density_custom`
This parameter lets you set the density of y-axis ticks, if `y_axis_tick_density` is set to `custom`. It accepts an integer that represents the number of ticks you want to appear.
```
y_axis_tick_density_custom: 10

## default value: 5

```

### `y_axis_reversed`
This parameter sets the direction of the y-axis. When `y_axis_reversed` is set to `false`, values increase going up the axis. When it is set to `true`, values decrease going down the axis.
```

## y_axis_reversed: true | false

# default value: false


```

### `y_axis_value_format`
This parameter specifies the number format of the y-axis values, independent of the underlying dimension or measure. The parameter accepts Excel-style formatting. If no formatting is specified, the value will be displayed in the format of the underlying dimension or measure.
The value you specify for the `y_axis_value_format` parameter must be enclosed in double quotes:
```

y_axis_value_format: "*00#.00"


```

You can read Excel's complete guide about how to specify these formats in their documentation. However, at this time, date formatting and color formatting are not supported in Looker.
Some of the most common formatting options are shown here:
Value Format | Meaning  
---|---  
Integer (123)  
`*00#` | Integer zero-padded to 3 places (001)  
`0.##` | Number up to 2 decimals (1. or 1.2 or 1.23)  
`0.00` | Number with exactly 2 decimals (1.23)  
`*00#.00` | Number zero-padded to 3 places and exactly 2 decimals (01.23)  
`#,###` | Number with comma between thousands (1,234)  
`#,##0.00` | Number with comma between thousands and 2 decimals (1,234.00)  
`0.000,," M"` | Number in millions with 3 decimals (1.234 M). Division by 1 M happens automatically.  
Dollars with 0 decimals ($123)  
`$0.00` | Dollars with 2 decimals ($123.00)  
`$#,##0.00` | Dollars with comma between thousands and 2 decimals ($1,234.00)  
Percent with 0 decimals (1%). Multiplication by 100 happens automatically.  
`0.00%` | Percent with 2 decimals (1.00%). Multiplication by 100 happens automatically.  
`0.00\%` | Percent with 2 decimals (1.00%). Multiplication by 100 does NOT happen automatically.  
### `y_axis_zoom`
This parameter specifies whether users can zoom into the y-axis of the visualization. When `y_axis_zoom` is set to `true`, zooming is available.
When `y_axis_zoom` is set to `false`, users cannot zoom into smaller portions of the y-axis. However, users may still be able to zoom into smaller portions of the x-axis if the `x_axis_zoom` parameter is set to `true`.
If `x_axis_zoom` is set to `false`, `y_axis_zoom` is disabled.
```
y_axis_zoom: true | false

# default value: true

```

## Advanced visualization configuration
The parameters described in this section correspond to the optional chart configuration overrides, which you can apply to a chart by clicking the **Edit Chart Config** button in the **Plot** section of the visualization editor.
### `advanced_vis_config`
This parameter accepts a HighCharts JSON snippet that overrides several visualization settings and opens up new capabilities. See the Customizing visualizations using the Chart Config Editor documentation page for examples of using HighCharts JSON to achieve common use cases.
```

advanced_vis_config: "{ series: [{ formatters: [{ select: 'value >= 50', style: { color: 'orange' } }]}]}"

# This example changes the color to orange for any series value that is greater than or equal to 50.

# default value: null

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


