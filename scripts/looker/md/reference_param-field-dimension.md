# dimension  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-dimension

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  dimension
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
view: view_name {
  dimension: field_name { ... }
}

```
Hierarchy `dimension` |  Accepts A Looker identifier to name the dimension  
---|---  
## Definition
The `dimension` parameter declares a new dimension and specifies a name for that dimension.
The name must meet the following requirements:
  * It must be unique within any given view.
  * It must consist of characters `a` through `z`, `0` through `9`, or `_`. The dimension name is case-sensitive. Because of this, we recommend using a consistent lowercase name for all LookML objects, including dimensions.
  * It must start with a letter.


There are many types of dimensions, as discussed further on the Dimension, filter, and parameter types documentation page.
## Subparameters for `dimension`
See the Field parameters reference page for a list of subparameters that are available for LookML fields.
## Examples
Create an `id` and a `supplier_name` dimension in a view named `products`:
```
view: products {
  dimension: id {
    primary_key: yes
    sql: ${TABLE}.id ;;
  }
  dimension: supplier_name {
    sql: ${TABLE}.supplier_name ;;
  }
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


