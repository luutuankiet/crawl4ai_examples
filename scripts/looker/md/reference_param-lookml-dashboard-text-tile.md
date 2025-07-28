# Text tile parameters for LookML dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-text-tile

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Parameter definitions
  * Basic parameters
  * Text parameters




Was this helpful?
Send feedback 
#  Text tile parameters for LookML dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Parameter definitions
  * Basic parameters
  * Text parameters


This page demonstrates how to add and customize a LookML dashboard element of `type: text` with LookML dashboard parameters in a `dashboard.lkml` file.
For information about adding text to a dashboard through the Looker UI, see the Creating user-defined dashboards documentation page.
## Example usage
```

## BASIC PARAMETERS
name: element_name
type: text
height: N
width: N
top: N
left: N
row: N
col: N

## TEXT PARAMETERS
title_text: title text
subtitle_text: subtitle text
body_text: body text


```

## Parameter definitions
Parameter Name | Description  
---|---  
Basic Parameters  
`name` (for elements) | Creates an element  
`type` (for elements) | Determines the type of visualization to be used in the element  
`height` (for elements) | Defines the height of an element in units of `tile_size` for `layout: tile` and `layout: static` dashboards  
`width` (for elements) | Defines the width of an element in units of `tile_size` for `layout: tile` and `layout: static` dashboards  
Defines the top-to-bottom position of an element in units of `tile_size` for `layout: static` dashboards  
Defines the left-to-right position of an element in units of `tile_size` for `layout: static` dashboards  
Defines the top-to-bottom position of an element in units of rows for `layout: newspaper` dashboards  
Defines the left-to-right position of an element in units of columns for `layout: newspaper` dashboards  
Text Parameters  
Specifies a title for a dashboard element of `type: text`  
Specifies a subtitle for a dashboard element of `type: text`  
Specifies body text for a dashboard element of `type: text`  
## Basic parameters
When defining a LookML dashboard element of `type: text`, you must specify values for at least the `name` and `type` parameters.
### `name`
> This section refers to the `name` parameter that is part of a dashboard element.
> `name` can also be used as part of a dashboard filter, described on the Dashboard parameters documentation page.
Each `name` declaration creates a new dashboard element and assigns it a name. Element names must be unique. Names are sometimes referenced in the `elements` parameter when you're using `layout: grid` dashboards.
```
- name: orders_by_date

```

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

## Text parameters
> Dashboard LookML that is generated from text tiles created with the **Text** option in the Looker UI will not use the `title_text` or `subtitle_text` parameters.
The parameters described in this section can be used to add content to a LookML dashboard element of `type: text`.
### `title_text`
The `title_text` parameter specifies the text that will appear on a `type: text` element in the largest font size available. It is shown at the top of the tile.
```
title_text: title text

```

### `subtitle_text`
The `subtitle_text` parameter specifies the text that will appear on a `type: text` element in the middle font size available. If `title_text` is present, the `subtitle_text` will appear below it.
```
subtitle_text: subtitle text

```

### `body_text`
The `body_text` parameter specifies the text that will appear on a `type: text` element in the smallest font size available. This parameter is shown last in the text tile. The Using Markdown in Markdown tiles documentation page provides an overview of the Markdown that you can use to format text or to add links and images to a text tile.
```
body_text: body text

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


