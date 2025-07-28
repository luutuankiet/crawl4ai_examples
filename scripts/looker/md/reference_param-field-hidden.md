# hidden (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-hidden

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  hidden (for fields)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


> This page refers to the `hidden` parameter that is part of a field.
> `hidden` can also be used as part of an Explore, described on the `hidden` (for Explores) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    hidden: yes 
  }
}

```

Hierarchy `hidden` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, ParameterAccepts A Boolean (yes or no)  
---|---  
## Definition
If you want a field to be available for modeling, but not shown to users, you can hide it from the field picker by using the `hidden` parameter.
Hidden fields can still be accessed in the UI if they are manually added to the URL. The `hidden` value is a way to keep the field picker clean; it is not a security feature.
The default value of `hidden` is `no`, unless the field is defined in a view that has the `fields_hidden_by_default: yes` parameter.
You can use the `fields_hidden_by_default: yes` view parameter to set the default for all the view's fields to `hidden:yes`. This is helpful if you want to hide the majority of fields in a view, since you won't have to add `hidden:yes` to each of the view's fields. To display a field in a view that has the `fields_hidden_by_default: yes` parameter, add the `hidden:no` parameter to the field.
## Examples
Prevent the `raw_event_stream` dimension from appearing in the field picker:
```
dimension: raw_event_stream {
  sql: ${TABLE}.event_stream ;;
  hidden: yes
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


