# suggestable  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-suggestable

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  suggestable
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: view_name {
  dimension: field_name {
    suggestable: yes 
  }
}

```

Hierarchy `suggestable` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, ParameterAccepts A Boolean (yes or no)  
---|---  
## Definition
When a user filters an Explore on a field that supports suggestions, by default Looker will suggest possible values for the field (see Changing filter suggestions for information about how you can affect filter suggestions).
The `suggestable` parameter lets you disable suggestions for a field when a user filters on that field in a Look or an Explore. The default value of `suggestable` is `yes`, and suggestions are provided when possible. If you set `suggestable` to `no`, Looker won't suggest values for the field.
## Examples
Prevent Looker from providing filter value suggestions for the `name` dimension:
```
dimension: name {
  type: string
  sql: ${TABLE}.name ;;
  suggestable: no
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


