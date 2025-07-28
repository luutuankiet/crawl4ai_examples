# Visualization and Query property tables  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/components-vis-prop-tables

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Area chart properties
  * Bar and column chart properties
  * Line chart properties
  * Scatter chart properties
  * Single value chart properties
  * Sparkline chart properties
  * Table chart properties
  * Pie chart properties




Was this helpful?
Send feedback 
#  Visualization and Query property tables
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Area chart properties
  * Bar and column chart properties
  * Line chart properties
  * Scatter chart properties
  * Single value chart properties
  * Sparkline chart properties
  * Table chart properties
  * Pie chart properties


## `Visualization`
This component grabs the data and config from the query context and renders the appropriate visualization. You can customize the width and height by passing numeric pixel values to those properties.
Property  | Values  | Notes   
---|---|---  
`width` | number (in pixels)  | Default 100% when prop is undefined.   
`height` | number (in pixels)  | Default 500px when prop is undefined.   
`chartTypeMap` | key/value object  | Accepts a key/value object that defines what component to render when the adapter system encounters specfic chart type values. This can be used to override Looker's default charts or to add new chart types to the adapter system.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'
import { MyCustomRadar } from '../MyCustomRadar'

<Query query='12345' config={{ type: 'radar'}}>
   <Visualization
      width={1000}
      height={500}
      chartTypeMap={{ radar: MyCustomRadar}}
    />
</Query>

```

## `Query`
`Query` integrates with our JavaScript API to handle the request/response cycle and to grab a query response by the query ID or `qid` value. You can pass vis config overrides to be merged with the API response, and have all the data loaded into React context.
Property  | Values  | Notes   
---|---|---  
`query` | number | string  | Can accept either the `Query.client_id`, which comes after the `qid` property in an Explore's URL, (`3fdrdE0b3ATltUvXBaSOPN`), or a numeric query ID (`1234`). If you have access to the numeric query ID, starting from this value can save one additional server request.`Query` accepts either the `query` prop or the `dashboard` prop, but not both.   
`dashboard` | number  | Can accept a numeric dashboard ID (`1234`). If you have access to the numeric dashboard ID, starting from this value can save one additional server request.`dashboard` does not accept the string IDs of LookML dashboards.`Query` accepts either the `query` prop or the `dashboard` prop, but not both.   
`config` | Depending on `type` value, accepts the following properties:`type`, `legend`, `positioning`, `render_null_values`, `tooltips`, `series`, `x_axis`, `y_axis` | Set and override configuration settings for charts.   
`LoadingIndicator` | component reference  | Accepts an unmounted component reference. Default: `ProgressCircular`  
```
import { Visualization, Query } from '@looker/visualizations'
import { ProgressCircular } from '@looker/components'

<Query
  query='12345'
  config={{
      /* specific properties described later on this page */
  }}
  LoadingIndicator={ProgressCircular}
>
  <Visualization />
</Query>

```

## Area chart properties
The following are the `config` properties for area charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'area'`  
`legend` |  `false` (to disable) OR `{ position: 'left' | 'bottom' | 'right' | 'top' }` | Sets legend position or disables the legend by setting it to `false`.`{ position: 'bottom' }`  
`positioning` |  `'overlay' | 'stacked' | 'percent'` | Chart stacking mode. Default: `'overlay'`  
`render_null_values` | boolean  | Treats null values as 0. Default: `false`  
`tooltips` | boolean  | Enable or disable tooltips appearing when hovering over data points. Default: `true`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
`x_axis` | x-axis configuration  | See the x-axis section for configuration options and example usage.   
`y_axis` | y-axis configuration  | See the y-axis section for configuration options and example usage.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'area',
    legend: { position: 'left' },
    positioning: 'stacked',
    render_null_values: true,
    tooltips: true,
  }}
>
  <Visualization />
</Query>

```

### `series`
The `series` property can accept either an array of series configurations or a named object overriding a specific series in your response.
Property  | Values  | Notes   
---|---|---  
`color` | string  | Hex code   
`label` | string   
`line_width` | number  | Set the line stroke width in pixels. Default: 3   
`shape` |  `'circle' | 'diamond' | 'square' | 'triangle' | 'triangle-down'` | Set point shape. Default: `'circle'`  
`style` |  `'none' | 'filled' | 'outline'` | Set point style. Default: `'none'` (points disabled)   
`visible` | boolean  | Show or hide the data series. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

/* named series overrides */
<Query
  query='12345'
  config={{
    type: 'area',
    series: {
      'orders.count': {
        color: '#4285F4',
        label: 'Total Orders',
        shape: 'square',
      }
    }
  }}
>
  <Visualization />
</Query>

/* ordered list series overrides */
<Query
  query='12345'
  config={{
    type: 'area',
    series: [{ color: '#4285F4', label: 'Total Orders', shape: 'square' }],
  }}
>
  <Visualization />
</Query>

```

### `x_axis`
Even though our charts only currently support a single x-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`  
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the x-axis label. Default: `false` (no label)   
`reversed` | boolean  | Reverses the order of the data points. Default: `false`  
`values` | boolean  | Show or hide the values rendered along the axis. Default: true   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'area',
      x_axis: [{ gridlines: true, label: 'Date of first purchase' }],
    }}
  >
    <Visualization />
  </Query>

```

### `y_axis`
Even though our charts only currently support a single y-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`.   
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the y-axis label. Default: `false` (no label)   
`range` | [number (min) | `'auto'`, number (max) | `'auto'` | Sets the min and max value of the y-axis. Setting min to `'auto'` defaults to 0, and setting max to `'auto'` defaults to the maximum data point value in the set. Default: `['auto' | 'auto']`  
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'area',
      y_axis: [
        { gridlines: true, label: 'Number of orders', range: [50, 'auto'] },
      ],
    }}
  >
    <Visualization />
  </Query>

```

## Bar and column chart properties
The following are the `config` properties for bar and column charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'bar' | 'column'`  
`legend` |  `false` (to disable) OR `{ position: 'left' | 'bottom' | 'right' | 'top' }` | Sets legend position or disables the legend by setting it to `false`. Default: `{ position: 'bottom' }`  
`positioning` |  `'grouped' | 'stacked' | 'percent'` | Chart stacking mode. Default: `'overlay'`  
`tooltips` | boolean  | Enable or disable tooltips appearing when hovering over data points.`true`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
`x_axis` | x-axis configuration  | See the x-axis section for configuration options and example usage.   
`y_axis` | y-axis configuration  | See the y-axis section for configuration options and example usage.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'bar',
    legend: { position: 'left' },
    positioning: 'stacked',
    tooltips: true,
  }}
>
  <Visualization />
</Query>

```

### `series`
The `series` property can accept either an array of series configurations or a named object overriding a specific series in your response.
Property  | Values  | Notes   
---|---|---  
`color` | string  | Hex code   
`label` | string   
`visible` | boolean  | Show or hide the data series. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'column',
    series: {
      'orders.count': {
        color: '#4285F4',
        label: 'Total Orders',
        visible: false,
      },
    },
  }}
>
  <Visualization />
</Query>

/* ordered list series overrides */
<Query
  query='12345'
  config={{
    type: 'column',
    series: [{ color: '#4285F4', label: 'Total Orders', visible: false }],
  }}
>
  <Visualization />
</Query>

```

### `x_axis`
Even though our charts only currently support a single x-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`.   
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the x-axis label. Default: `false` (no label)   
`reversed` | boolean  | Reverses the order of the data points. Default: `false`  
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'column',
      x_axis: [{ gridlines: true, label: 'Date of first purchase' }],
    }}
  >
    <Visualization />
  </Query>

```

### `y_axis`
Even though our charts only currently support a single y-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`.   
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the y-axis label. Default: `false` (no label)   
`range` | [number (min) | `'auto'`, number (max) | `'auto'` | Sets the min and max value of the y-axis. Setting min to 'auto' defaults to 0, and setting max to 'auto' defaults to the maximum data point value in the set. Default: `['auto' | 'auto']`.   
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'bar',
      y_axis: [
        { gridlines: true, label: 'Number of orders', range: [500, 'auto'] },
      ],
    }}
  >
    <Visualization />
  </Query>

```

## Line chart properties
The following are the `config` properties for line charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'line'`  
`legend` |  `false` (to disable) OR `{ position: 'left' | 'bottom' | 'right' | 'top' }` | Sets legend position or disables the legend by setting it to `false`. Default: `{ position: 'bottom' }`  
`render_null_values` | boolean  | Treats null values as 0. Default: `false`  
`tooltips` | boolean  | Enable or disable tooltips appearing when hovering over data points. Default: `true`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
`x_axis` | x-axis configuration  | See the x-axis section for configuration options and example usage.   
`y_axis` | y-axis configuration  | See the y-axis section for configuration options and example usage.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'line',
    legend: { position: 'left' },
    render_null_values: true,
    tooltips: true,
  }}
>
  <Visualization />
</Query>

```

### `series`
The `series` property can accept either an array of series configurations or a named object overriding a specific series in your response.
Property  | Values  | Notes   
---|---|---  
`color` | string  | Hex code   
`label` | string   
`line_width` | number  | Set the line stroke width in pixels. Default: 3   
`shape` |  `'circle' | 'diamond' | 'square' | 'triangle' | 'triangle-down'` | Set point shape. Default: `'circle'`  
`style` |  `'none' | 'filled' | 'outline'` | Set point style. Default: `'none'` (points disabled)   
`visible` | boolean  | Show or hide the data series. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

/* named series overrides */
<Query
  query='12345'
  config={{
    type: 'line',
    series: {
      'orders.count': {
        color: '#4285F4',
        label: 'Total Orders',
        shape: 'square',
      },
    },
  }}
>
  <Visualization />
</Query>

/* ordered list series overrides */
<Query
  query='12345'
  config={{
    type: 'line',
    series: [{ color: '#4285F4', label: 'Total Orders', shape: 'square' }],
  }}
>
  <Visualization />
</Query>

```

### `x_axis`
Even though our charts only currently support a single x-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`.   
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the x-axis label. Default: `false` (no label)   
`reversed` | boolean  | Reverses the order of the data points. Default: `false`  
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'line',
      x_axis: [{ gridlines: true, label: 'Date of first purchase' }],
    }}
  >
    <Visualization />
  </Query>

```

### `y_axis`
Even though our charts only currently support a single y-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`  
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the y-axis label. Default: `false` (no label)   
`range` | [number (min) | `'auto'`, number (max) | `'auto'` | Sets the min and max value of the y-axis. Setting min to 'auto' defaults to 0, and setting max to 'auto' defaults to the maximum data point value in the set. Default: `['auto' | 'auto']`.   
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'line',
      y_axis: [
        { gridlines: true, label: 'Number of orders', range: [500, 'auto'] },
      ],
    }}
  >
    <Visualization />
  </Query>

```

## Scatter chart properties
The following are the `config` properties for scatter charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'scatter'`  
`legend` |  `false` (to disable) OR `{ position: 'left' | 'bottom' | 'right' | 'top' }` | Sets legend position or disables the legend by setting it to `false`. Default: `{ position: 'bottom' }`  
`render_null_values` | boolean  | Treats null values as 0. Default: `false`  
`tooltips` | boolean  | Enable or disable tooltips appearing when hovering over data points. Default: `true`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
`x_axis` | x-axis configuration  | See the x-axis section for configuration options and example usage.   
`y_axis` | y-axis configuration  | See the y-axis section for configuration options and example usage.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'scatter',
    legend: { position: 'left' },
    render_null_values: true,
    tooltips: true,
  }}
>
  <Visualization />
</Query>

```

### `series`
The `series` property can accept either an array of series configurations or a named object overriding a specific series in your response.
Property  | Values  | Notes   
---|---|---  
`color` | string  | Hex code   
`label` | string   
`line_width` | number  | Used to set the size of points in a scatterplot. Think of it as the outline value of each point. Default: `3`  
`shape` |  `'circle' | 'diamond' | 'square' | 'triangle' | 'triangle-down'` | Set point shape. Default: `'circle'`  
`style` |  `'none' | 'filled' | 'outline'` | Set point style. Default: `'none'` (points disabled)   
`size_by` |  `false` | string  | Series name for which to calibrate the size of each point. Set `false` to disable dynamic point sizing. Default: `false`  
`visible` | boolean  | Show or hide the data series. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

/* named series overrides */
<Query
  query='12345'
  config={{
    type: 'scatter',
    series: {
      'orders.count': {
        color: '#4285F4',
        label: 'Total Orders',
        shape: 'square',
        size_by: 'orders.count',
      },
    },
  }}
>
  <Visualization />
</Query>

/* ordered list series overrides */
<Query
    query='12345'
    config={{
      type: 'scatter',
      series: [
        {
          color: '#4285F4',
          label: 'Total Orders',
          shape: 'square',
          size_by: 'orders.count',
        },
      ],
    }}
  >
    <Visualization />
  </Query>


```

### `x_axis`
Even though our charts only currently support a single x-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`.   
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the x-axis label. Default: `false` (no label)   
`reversed` | boolean  | Reverses the order of the data points. Default: `false`  
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'scatter',
      x_axis: [{ gridlines: true, label: 'Date of first purchase' }],
    }}
  >
    <Visualization />
  </Query>

```

### `y_axis`
Even though our charts only currently support a single y-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`gridlines` | boolean  | Show or hide vertical gridlines. Default: `false`.   
`label` |  `false` (to hide label) | string (value to render)  | Sets the value to render as the y-axis label. Default: `false` (no label)   
`range` | [number (min) | `'auto'`, number (max) | `'auto'` | Sets the min and max value of the y-axis. Setting min to 'auto' defaults to 0, and setting max to 'auto' defaults to the maximum data point value in the set. Default: `['auto' | 'auto']`.   
`values` | boolean  | Show or hide the values rendered along the axis. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

  <Query
    query='12345'
    config={{
      type: 'scatter',
      y_axis: [
        { gridlines: true, label: 'Number of orders', range: [500, 'auto'] },
      ],
    }}
  >
    <Visualization />
  </Query>

```

## Single value chart properties
The following are the `config` properties for single value charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'single_value'`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query query='12345' config={{ type: 'single_value' }}>
  <Visualization />
 </Query>

```

## Sparkline chart properties
The following are the `config` properties for sparkline charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'sparkline'`  
`render_null_values` | boolean  | Treats null values as 0. Default: `false`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
`y_axis` | y-axis configuration  | See the y-axis section for configuration options and example usage.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query="12345"
  config={{ type: 'sparkline', render_null_values: true }}
>
  <Visualization />
</Query>

```

### `series`
Although Sparkline inherently only supports a single series, we maintain an API pattern involving named or array series overrides in order to stay consistent with the other chart types in our library.
Property  | Values  | Notes   
---|---|---  
`color` | string  | Hex code   
`line_width` | number  | Set the line stroke width in pixels. Default: `3`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

/* named series overrides */
<Query
  query='12345'
  config={{
    type: 'sparkline',
    series: {
      'orders.count': {
        color: '#4285F4',
        line_width: 10,
      },
    },
  }}
>
  <Visualization />
</Query>

/* ordered list series overrides */
<Query
  query='12345'
  config={{
    type: 'scatter',
    series: [
        {
          color: '#4285F4',
          line_width: 10,
        },
      ],
  }}
>
  <Visualization />
</Query>

```

### `y_axis`
Even though our charts only currently support a single y-axis, our API is future-proofed and is structured to support the configuration of multiple axes.
Property  | Values  | Notes   
---|---|---  
`range` | [number (min) | `'auto'`, number (max) | `'auto'` | Sets the min and max value of the y-axis. Setting min to 'auto' defaults to 0, and setting max to 'auto' defaults to the maximum data point value in the set. Default: `['auto' | 'auto']`.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'sparkline',
    y_axis: [
      { range: [50, 'auto'] },
    ],
  }}
>
  <Visualization />
</Query>

```

## Table chart properties
The following are the `config` properties for table charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'table'`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
`column_order` |  `string[]` | An array of series names (for example, `'orders.count'`) indicating how you would like the table columns to be ordered from left to right.   
`show_row_numbers` |  `boolean` | Toggle the display of the totals row at the bottom of the table. Default: `true`  
`show_totals` |  `boolean` | Toggle the display of the totals row at the bottom of the table. Default: `true`  
`show_row_totals` |  `boolean` | Toggle the display of row totals on the right side of the table. Default: `true`  
`truncate_text` |  `boolean` | When `true`, table cell text is limited to a single line and content overflow is truncated with an ellipsis. When `false`, the content is allowed to wrap to multiple lines. Default: `true`  
`truncate_header` |  `boolean` | When `true`, table header labels are limited to a single line and content overflow is truncated with an ellipsis. When `false`, the headers are allowed to wrap to multiple lines. Default: `true`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'table',
    column_order: ['orders.count', 'users.city'],
    show_row_numbers: true,
    show_totals: true,
    show_row_totals: true,
    truncate_text: true,
    truncate_header: true
  }}
>
  <Visualization />
</Query>

```

### `series`
The series property can accept either an array of series configurations or a named object overriding a specific series in your response.
Property  | Values  | Notes   
---|---|---  
`cell_visualization` |  `boolean` | Toggles on or off the inline cell visualization. Defaults to `true` for the first measure, and `false` for the others.   
`color` |  `string` | Specify the color used to render the table cell visualization.   
`value_format` |  `string` | A number formatting string indicating whether to render values as currency, the floating point precision, whether to use commas or periods to delineate thousands, and so on.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'table',
    series: {
      'orders.count': {
        color: '#4285F4',
        cell_visualization: true,
        value_format: '$#,##0.00',
      },
    },
  }}
>
  <Visualization />
</Query>

/* ordered list series overrides */
<Query
  query='12345'
  config={{
    type: 'table',
    series: [{
      color: '#4285F4',
      cell_visualization: true,
      value_format: '$#,##0.00',
    }]
  }}
>
 <Visualization />
</Query>

```

## Pie chart properties
The following are the `config` properties for pie charts.
Property  | Values  | Notes   
---|---|---  
`type` |  `'pie'`  
`legend` |  `false` (to disable) | legend configuration  | Setting to `false` disables the legend. Default: enabled. See the legend section for configuration options and example usage when enabled.   
`tooltips` | boolean  | Enable or disable tooltips appearing when hovering over data points. Default: `true`  
`series` | series in `view_name.field_name` format  | See the series section for configuration options and example usage.   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'pie',
    legend: false,
    tooltips: true,
  }}
>
  <Visualization />
</Query>

```

### `legend`
The `legend` property can accept the following legend configurations:
Property  | Values  | Notes   
---|---|---  
`type` |  `'labels' | 'legend'` |  `labels` places labels pointing directly to each slice. `legend` places a separate legend. Default: `'legend'`  
`position` |  `'top' | 'bottom' | 'left' | 'right'` | Position the legend when `type: 'legend'`. Default: `'right'`  
`width` | number  | Maximum width of the legend in pixels when `type: 'legend'`. Default: `300`  
`value` |  `'label' | 'label_value' | 'value' | 'percent' | 'label_percent'` | Sets the legend content: label, label and value, value, percent, label and percent. Default: `'label_percent'`  
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'pie',
    legend: {
      type: 'legend'
      position: 'right'
      width: 200,
      value: 'label_value',
    },
  }}
>
  <Visualization />
</Query>

```

### `series`
Unlike Cartesian charts, each data point in a pie chart gets treated as a new series:
Property  | Values  | Notes   
---|---|---  
`color` | string  | Hex code   
Example usage:
```
import { Visualization, Query } from '@looker/visualizations'

<Query
  query='12345'
  config={{
    type: 'pie',
    series: {
      'New York': {
        color: '#4285F4',
      },
      'Los Angeles': {
        color: '#b73ec3',
      },
      'Chicago': {
        color: '#db4da8',
      },
    },
  }}
>
  <Visualization />
</Query>

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


