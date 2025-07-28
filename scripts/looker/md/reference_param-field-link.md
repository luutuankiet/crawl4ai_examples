# link  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-link

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  link
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
view: view_name {
  dimension: field_name {
    link: {
      label: "desired label name"
      url: "desired_url"
      icon_url: "url_of_an_image_file"
    }
    # Possibly more links
  }
}

```
Hierarchy `link` |  Possible Field Types Dimension, MeasureAccepts Various parameters  
---|---  
## Definition
The `link` parameter lets you add web links to dimensions and measures to enable users to easily navigate to related content directly from Looker. The form of a `link` parameter is:
```
dimension: field_name {
  link: {
    label: "desired label name"
    url: "desired_url"
    icon_url: "url_of_an_image_file"
  }
  # Possibly more links
}

```

The `link` parameter has several child parameters:
  * `label` is the name of the link that you want to appear to users.
  * `url` is the URL that you want the link to go to. You can use Liquid variables to make the links dynamic, as described in the Using Liquid variables with `link` section on this page.
  * `icon_url` is a URL, accessible to the user's browser, that contains an image file. This makes it easier for users to understand, at a glance, where the link will take them. The `icon_url` parameter is not required if you do not want an icon. If you need corporate logos, try running a Google search with the pattern `http://www.google.com/s2/favicons?domain=[company website of interest]` to find images in the `.ico` format.


### Example
An e-commerce company wants employees to be able to contact warehouse support directly from Looker content, such as a Look displaying pending orders from the past month. The Look contains order IDs and the user ID of the customer associated with each order.
You can add a link to the **Orders ID** dimension to make this action available to the user viewing the Look:
```

dimension: id {
  primary_key: yes
  type: number
  sql: ${TABLE}.id ;;
  link: {
    label: "Contact Warehouse Support"
    url: "mailto:warehouse@altostrat.com"
  }
}


```

In the Look, the user will see the **Contact Warehouse Support** link among the options in the link menu, accessed by clicking the three-dot menu for any of the values of the **Orders ID** field.
Clicking the link name will take the user to the linked content — in this case, a new tab with a blank email draft addressed to the specified email address.
### Link behavior
When a user clicks a link, Looker will open the link either in a new browser tab or in the same tab (or iframe, for embedded queries):
  * Absolute links, such as `https://example.looker.com`, will open in a new browser tab.
  * Relative links, such as `/dashboards/456`, will open in the same browser tab or iframe. Once the link is opened, the user can click **Back** in the browser to navigate back to the original query.


A user must have either the `explore` or `see_drill_overlay` permission to access links.
## Using Liquid variables with `link`
The `link` parameter supports Liquid variables to make content even more interactive down to the row and value level. LookML supports two kinds of Liquid usage tags: value input `{{  }}` tags and conditional logic `{%  %}` tags.
Of the two, `{{  }}`, in conjunction with the `value` and `_filters['view_name.field_name']` Liquid variables, is most commonly used with `link`. This is because `{{  }}` tags input values directly where they are placed, such as within a URL.
See the examples on this page for examples of using Liquid `{{ }}` tags with the `value` and `_filters['view_name.field_name']` variables to make content interactive with `link`.
### Linking to external content
For example, suppose you had an `artist_name` dimension and wanted the user to have the option of executing a Google search for that artist, right from Looker. You can use the `value` Liquid variable to add that option to a dimension like the following:
```
dimension: artist_name {
  link: {
    label: "Google"
    url: "http://www.google.com/search?q={{ value }}"
    icon_url: "http://google.com/favicon.ico"
  }
}

```

When a user clicks the three-dot menu for a value of the **Artist Name** field, Looker displays the **Links** menu, which includes the link that was created in the sample LookML. The link opens a new browser tab to a Google search for the artist they selected. The selected artist name is inserted into the URL where `{{ value }}` is placed.
This pattern can be replicated for other external websites that a user's browser has access to, such as ticket management systems, client management systems, and other business-related tools, for ease of navigation between web applications.
### Linking to content in Looker
In addition to external sites, you can use the `link` parameter to direct users to other relevant Looker Explores, Looks, or dashboards for a custom drilling experience. You can also apply the same examples to links in the LookML `html` parameter for fields.
To start, you will need to obtain the URL of an existing Explore, Look, or dashboard that you want to link to. Then you can replace specific elements of the URL, such as filter values and names, with `{{  }}` tags containing `value` and `_filters['view_name.field_name']` variables. The variables will input user selected values into the URL elements they replace. The basic structure of content URLs is as follows:
  * **Explore** : `/explore/YOUR_MODEL_NAME/YOUR_EXPLORE_NAME?fields=view_name.field_name1,view_name.field_name2...`
    * You can obtain the Explore URL for existing Explores by selecting the **Expanded URL** gear icon option.
    * Explore filters will appear in URLs as `f[view_name.field_name]`. See the Linking to a related Explore section for an example.
  * **Look** : `/looks/YOUR_LOOK_NUMBER`
    * You can obtain the URL for an existing Look by copying the browser URL from the Look page.
    * Look filters will appear in URLs as `f[view_name.field_name]`. See the Passing an existing filter value to linked content section for an example.
  * **User-Defined Dashboard** : `/dashboards/YOUR_DASHBOARD_NUMBER?FILTER_NAME_1=VALUE&FILTER_NAME_2=VALUE`
    * You can obtain the URL for an existing dashboard by copying the browser URL from the dashboard page.
  * **LookML Dashboard** : `/dashboards/YOUR_MODEL::YOUR_DASHBOARD`
    * You can obtain the URL for an existing LookML dashboard by copying the browser URL from the dashboard page.


Dashboard filters for both user-defined and LookML dashboards will appear in URLs as `filter_name`, where `filter_name` is the name given to the filter placed on the dashboard. See the Passing an existing filter value to linked content section for an example.
Elements of URLs, such as filter values and names, are URL encoded with special characters, such as `?` to indicate the start of a query string, to separate elements, and `%20` for spaces. See the URL encoding for other comparison operators section for an example.
Once you have the URL of the content you want to link to, you can use Liquid to insert the value of a field into any element of the URL, using the `value` or `_filters['view_name.field_name']` variables and `{{  }}` tags. See the Using URLs and query parameters Looker Community post for more information on the parts of a query URL.
#### Example: Linking to a related Explore
We have a dimension called **City**. We want users to be able to access another existing Explore, with city metrics and a **City** filter. We want the linked Explore to be filtered by the city the user selects.
To achieve this:
  1. Obtain the URL of the existing Explore to drill to.
  2. Add a `link` parameter to the **City** dimension:

```
  dimension: city {
  type: string
  sql: ${TABLE}.city ;;
  link: {
    label: "City Metrics Explore"
    url: "/explore/ecommerce_model/order_items_explore?fields=users.city,orders.count,users.count&f[users.city]=&sorts=orders.count+desc&limit=500"
  }
  }

```

Here, the URL has been shortened to `limit=500`, which limits the Explore results to 500 rows, for clarity — you can include the rest of the URL, which typically includes URL encoding of visualization settings, as necessary.
  1. Insert the Liquid `{{ value }}` tag and variable where you would like to insert the value into the URL. In this case, we want to put the value where the filter element, `f[users.city]=`, is located in the URL string for the Explore to be filtered by the user-selected city:

```
dimension: city {
  type: string
  sql: ${TABLE}.city ;;
  link: {
    label: "City Metrics Explore"
    url: "/explore/ecommerce_model/order_items_explore?fields=users.city,orders.count,users.count&f[users.city]={{ value }}&sorts=orders.count+desc&limit=500"
  }
}

```

The **City** dimension will then display a three-dot link menu that displays the **City Metrics Explore** option.
When a user clicks the link, they are redirected to the **City Metrics Explore** , filtered by the selected city.
You can also preserve existing filter values when linking to Looker content, as discussed in the following example.
#### Example: Passing an existing filter value to linked content
Another Liquid variable supported by the `link` parameter is `_filters['view_name.field_name']`. This variable takes the existing values entered for a filter and passes them to a linked Explore, dashboard, or Look.
In content URLs, you can see where the filter values are specified and replace them with your `_filters['view_name.field_name']` variable. See the Using URLs and query parameters Looker Community post for information on the parts of a query URL.
Here is an example of a dimension that uses the `_filters['view_name.field_name']` variable in its `link` parameter to pass an existing filter value for a field called `users.state`:
```
dimension: name {
  link: {
    label: "Business Pulse By State Dashboard"
    url: "/dashboards/694?State={{ _filters['users.state'] | url_encode }}"
  }
}

```

In this example, if a user filters a query by the `users.state` dimension, the linked dashboard is automatically filtered by the same states chosen in the original query. Including the Liquid filter `url_encode` in this example converts URL-unsafe strings into percent-encoded strings. This ensures that filter values containing special characters, like spaces or commas, can be passed to the linked dashboard.
For example, suppose a user has filtered a query by the state "California." When the user clicks the three-dot menu next to a value for the **Name** field, the **Links** menu displays a link to the dashboard **Business Pulse by State**. When the user clicks this link, the **Business Pulse by State** dashboard will already be filtered on the state "California."
This also works for passing filter values to linked Looks and Explores:
```
dimension: name {
    link: {
      label: "Average Order Profit Look"
      url: "/looks/249?&f[users.state]={{ _filters['users.state'] | url_encode }}"
    }
    link: {
      label: "User Facts Explore Explore"
      url: "/explore/ecommerce/users?fields=users.id,users.name&f[users.state]={{ _filters['users.state'] | url_encode }}"
    }
  }

```

You can pass multiple filters by placing between them, such as in the following URLs:
```
dimension: name {
  link: {
    label: "Business Pulse By State Dashboard"
    url: "/dashboards/694?State={{ _filters['users.state'] | url_encode }}&Date={{ _filters['orders.date'] | url_encode }}"
  }
  link: {
    label: "Average Order Profit Look"
    url: "/looks/249?&f[users.state]={{ _filters['users.state'] | url_encode }}&f[orders.date]={{ _filters['orders.date'] | url_encode }}"
  }
}

```

For information on creating dashboard filters, see the Building LookML dashboards and the Adding and editing user-defined dashboard filters documentation pages.
#### Example: Using `link` to customize drill visualizations
If your Looker admin has enabled the **Visual Drilling** Labs feature, you can customize the visualization displayed in the drill overlays of Explores and Looks by using the `link` parameter and Liquid variables. Dashboards support visual drilling using the `link` parameter without the need to enable the **Visual Drilling** Labs feature.
Here is an example of setting a drill visualization to a scatter chart:
```

  measure: count {
    type: count_distinct
    sql: ${id} ;;
    drill_fields: [created_date, total_sale_price]
    link: {
      label: "Drill as scatter plot"
      url: "
      {% assign vis_config = '{\\"type\\": \\"looker_scatter\\"}' %}
        \{\{ link \}\}&vis_config=\{\{ vis_config | encode_uri \}\}&toggle=dat,pik,vis&limit=5000"
    }
  }


```

See the More powerful data drilling Best Practices page for more examples of customizing drill visualizations.
#### Things to consider when linking to Looker content
There may be cases where you need to include filter comparison operators besides **equal to** , include multiple filters, or escape commas in links to Looker content. The following sections provide more information on these use cases.
##### URL encoding other comparison operators
If you would like to include a comparison operator in a linked filter other than **equal to** (**=**), you can do so by URL encoding the operator.
For example, if you wanted an `order_id` filter on a linked Look to include values that are **less than** () the `order_id` field associated with the value you are clicking, you would partially encode the operator character (`%3C` in this case) and add it to the URL:
```
f[orders.order_id]=%3C{{ other_orders.order_id._value }}

```

##### Including multiple filters
More than one filter can be applied to linked Looks, dashboards, and Explores by using an ampersand () to separate each filter:
```
dimension: name {
  link: {
    label: "Drill Look"
    url:"/looks/looknumber?&f[users.state]={{ value }}[users.region]={{ users.region._value }}&f[users.age]={{ _filters['users.age'] | url_encode }}"
  }
}

```

##### Escaping commas
You can escape commas in linked values with the `filterable_value` variable where you might normally use the `value` variable.
The following link drills to an Explore that will filter the results by the `users.city` value that is selected:
```
dimension: city {
    type: string
    sql: ${TABLE}.city ;;
    link: {
        label: "Drill by City"
        url: "/explore/model_name/explore_name?fields=users.email,users.id&f[users.city]={{ value }}"
    }
}

```

If the user clicks **Santa Cruz, CA** to drill to the results filtered by this city, the resulting drill will return all results that contain either **Santa Cruz** or **CA**.
If `filterable_value` is used instead of `value`, the comma will be escaped:
```
dimension: city {
    type: string
    sql: ${TABLE}.city ;;
    link: {
        label: "Drill by City"
        url: "/explore/model_name/explore_name?fields=users.email,users.id&f[users.city]={{ filterable_value }}"
    }
}

```

The resulting drill will return all results that contain the entire string value **Santa Cruz, CA**.
If you want to hard-code a filter value that contains a comma in a drill URL, you can escape the comma by wrapping the value in double quotes and then escaping them with a backslash (`\`):
```
dimension: city {
    type: string
    sql: ${TABLE}.city;;
    link: {
        label: "Drill by City"
        url: "/explore/model_name/explore_name?fields=users.email,users.id&f[users.city]=\"Santa Cruz, CA\"&sorts=users.email"
    }
}

```

### Additional resources
  * See the More powerful data drilling Best Practices page for more advanced custom drilling examples.
  * Refer to the Liquid variables documentation page for more examples of using `{{ value }}` in links.


## Things to know
When a dimension contains a `link` parameter that references another field, that additional field may be added to the underlying SQL of a query that the dimension is used in. If the referenced field is not present in the query's visualization, and the visualization is a table chart with manually rearranged columns, the column order in some downloaded formats may be affected.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


