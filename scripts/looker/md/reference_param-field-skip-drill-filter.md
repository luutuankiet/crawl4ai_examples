# skip_drill_filter  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-skip-drill-filter

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  skip_drill_filter
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
view: view_name {
  dimension: field_name {
    skip_drill_filter: yes 
  }
}

```
Hierarchy `skip_drill_filter` |  Possible Field Types DimensionAccepts A Boolean (yes or no)  
---|---  
## Definition
When users drill into a measure, the resulting dataset is filtered so that users arrive at the specific records that made up that measure. Looker achieves this by adding filters that match the dimension values in the same row as the measure. For most types of dimensions, this works well.
However, if the value of one of those dimensions changed _during_ the process of drilling, this might cause the dataset to be different than the user was expecting. If a dimension may change often (likely a pre-aggregation that occurs in a frequent ETL process), you can stop it from being included in drill filters by using `skip_drill_filter`. `skip_drill_filter` accepts `true` or `false`.
## Examples
Prevent the `transactions` dimension from being included in drill filters:
```
dimension: transactions {
  sql: ${TABLE}.transactions ;;
  type: number
  skip_drill_filter: yes
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


