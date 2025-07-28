# view_label (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-view-label

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  view_label (for fields)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


> This page refers to the `view_label` parameter that is part of a dimension, measure, or filter.
> `view_label` can also be used as part of an Explore, described on the `view_label` (for Explores) parameter documentation page.
> `view_label` can also be used as part of a join, described on the `view_label` (for joins) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    view_label: "desired label name"
  }
}

```

Hierarchy `view_label` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, ParameterAccepts A string  
---|---  
## Definition
The `view_label` parameter lets you change the name of the view under which the field is listed in the field picker without changing how it is referenced in LookML. If the label matches the name of an existing view, the field will now appear under that view. If you specify a new name, that name will appear in the field picker with the field under it. If not specified, the view label defaults to the name of the view.
Fields with view labels are still referenced with the normal `${view_name.field_name}` syntax in LookML. The view label only impacts the appearance of the field picker. It does not alter an existing view or create a new view.
Also, note the difference between a field's `view_label` and the field's `label`. The `view_label` changes only the view name under which the field is listed, not the name that's displayed for the field itself.
## Examples
Make this dimension appear under the **Identifiers** view instead of the **Distribution Centers** view in the field picker.
```
view: distribution_centers {
  dimension: id {
    view_label: "Identifiers"
    type: number
    sql: ${TABLE}.id ;;
  }
}

```

For examples of using `view_label` with a Liquid parameter to define dynamic labels, see the Interesting ways to use Liquid in labels Best Practices page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


