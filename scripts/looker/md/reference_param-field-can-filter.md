# can_filter  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-can-filter

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  can_filter
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
view: view_name {
  dimension: field_name {
    can_filter: yes 
  }
}

```
Hierarchy `can_filter` |  Possible Field Types Dimension, Dimension Group, MeasureAccepts A Boolean (yes or no)  
---|---  
## Definition
The `can_filter` parameter lets you prohibit a dimension or measure from being used as a filter. For example:
```
dimension: description {
  can_filter: no
}

```

-
The default value of `can_filter` is true, meaning that dimensions and measures can be used as filters as you would expect. However, there may be some cases when a field may be too demanding to search (like a large text description), and in these situations you can prevent that field from being used as a filter. Users will simply not see a **FILTER** option when they hover over the field.
Note that `can_filter` cannot be used with:
  * Measures of `type: list`, because they cannot be filtered on anyway
  * `filter` fields, which only exist for the purpose of filtering
  * The `filters` parameter that is used with measures


Additionally, drilling into a field will not be permitted if the drill requires a filterable dimension and the `can_filter` parameter is set to `no`. This occurs when you:
  * Attempt to drill on a dimension that uses `can_filter: no`
  * Attempt to drill on a measure if a `can_filter: no` dimension is used in the same query as that measure


See the documentation pages for `drill_fields` (for fields) and `drill_fields` (for views).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


