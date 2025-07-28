# suggest_dimension  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-suggest-dimension

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  suggest_dimension
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: view_name {
  dimension: field_name {
    suggest_dimension: dimension_name
  }
}

```

Hierarchy `suggest_dimension` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, ParameterAccepts A fieldname in the current view or viewname.fieldname Special Rules To refer to a field in another view, use viewname.fieldname where viewname is a view joined in the Explore  
---|---  
## Definition
This parameter changes how Looker generates suggestions for a `filter` field or a `dimension` of `type: string` when someone uses that field to filter a query.
Looker typically generates these suggestions by executing the following query on the filter field:
`SELECT DISTINCT <field name> FROM <table> LIMIT 1000`
If the field is in a large table, this query can be too slow or create too large a database load.
By using `suggest_dimension`, you can make Looker query an alternative dimension for the suggestion values. If that dimension is defined in a different Explore, `suggest_explore` tells Looker where to find it. In this case, include both the view name where the dimension is defined and the dimension name in the format `view_name.field_name`. In addition, ensure that the view is joined to the Explore that is specified in the `suggest_explore` parameter.
If the dimension is defined in the current view, `suggest_explore` is not required.
## Examples
In this example, instead of looking through a huge list of user names from the `event` Explore, we've told Looker to query the names from a `user` Explore instead:
```
dimension: event_user_name {
  type: string
  sql: ${TABLE}.event_user_name ;;
  suggest_explore: user
  suggest_dimension: user.name
}

```

In this example, rather than a different Explore, the suggestion uses a dimension in another view joined to the same Explore:
```
dimension: event_company_name {
  type: string
  sql: ${TABLE}.event_company_name ;;
  suggest_dimension: company.name
}

```

## Things to know
Fields with `suggest_dimension` will not be affected by linked filters in dashboards.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


