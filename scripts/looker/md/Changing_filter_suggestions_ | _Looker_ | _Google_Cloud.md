# Changing filter suggestions  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/changing-filter-suggestions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Default behavior
  * Field types that support suggestions
  * Enabling or disabling filter suggestions
    * suggestions (view)
    * suggestable (field)
  * Filter suggestion values
    * allowed_value (field)
    * bypass_suggest_restrictions (field)
    * full_suggestions (field)
    * suggest_dimension (field) and suggest_explore (field)
    * suggestions (field)
  * Caching filter suggestions
    * suggest_persist_for (field)




Was this helpful?
Send feedback 
#  Changing filter suggestions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Default behavior
  * Field types that support suggestions
  * Enabling or disabling filter suggestions
    * suggestions (view)
    * suggestable (field)
  * Filter suggestion values
    * allowed_value (field)
    * bypass_suggest_restrictions (field)
    * full_suggestions (field)
    * suggest_dimension (field) and suggest_explore (field)
    * suggestions (field)
  * Caching filter suggestions
    * suggest_persist_for (field)


This page provides an overview of LookML parameters that affect filter suggestions. This page lists each parameter with a link to its full reference page and a short description of its function.
## Default behavior
By default, in a Look or an Explore, when a user enters a filter value for a field that supports suggestions, Looker suggests options that match what the user enters. On a dashboard, if the dashboard filter is filtering on a field that supports suggestions, Looker also suggests filter options. These filter suggestions are created using a SELECT DISTINCT query on the field, so the suggestions will only return values that match existing data for that field:
If you experience any unexpected behavior and need to troubleshoot filter suggestions, see the Troubleshooting common filter suggestion issues Best Practices page.
## Field types that support suggestions
Looker supports suggestions for the following `type` values for `dimension`, `dimension_group`, `filter`, and`parameter` fields.
Dimension `type` values that support suggestions:


Dimension group `type` value that supports suggestions:
  * `type: time`, with the following `timeframes` values:
    * `type: date_day_of_week`
    * `type: date_quarter_of_year`
    * `type: date_fiscal_quarter_of_year`
    * `type: date_time_of_day`


Filter `type` value that supports suggestions:
  * `type: string`


Parameter `type` values that support suggestions:
  * `type: string`


## Enabling or disabling filter suggestions
This section describes the following LookML parameters that let you enable or disable filter suggestions:
  * `suggestions` (view)
  * `suggestable` (field)


###  `suggestions` (view)
By default, when a user filters an Explore on a field that supports suggestions, Looker will suggest possible values for the field.
You can define a view with `suggestions:no` to disable suggestions for all the fields in the view.
###  `suggestable` (field)
By default, when a user filters an Explore on a field that supports suggestions, Looker will suggest possible values for the field.
You can define an individual field with `suggestable:no` to disable suggestions for the field.
## Filter suggestion values
This section describes the following LookML parameters that let you set or restrict the values shown in filter suggestions:
  * `allowed_value` (field)
  * `bypass_suggest_restrictions` (field)
  * `case` (field)
  * `full_suggestions` (field)
  * `suggest_dimension` (field) and `suggest_explore` (field)
  * `suggestions` (field)


###  `allowed_value` (field)
`allowed_value` works with the `parameter` LookML parameter. If a Looker developer provides a `parameter` filter-only field, the values entered or selected by users can be referenced using a {% parameter %} Liquid variable. Optionally, you can use `allowed_value` to define a list of values a user can choose for that parameter field.
`allowed_value` has two subparameters, `label` and `value`. The `label` subparameter specifies the options that the user will see in the filter suggestions. The `value` subparameter contains the values that are passed to the `{% parameter %}` Liquid variable.
For example, a parameter may be defined as follows:
```
parameter:order_amount{
type:string
allowed_value:{
label:"Less than $50"
value:"< 50"
}
allowed_value:{
label:"Between $50 and $100"
value:"<= 100"
}
allowed_value:{
label:"Over $100"
value:"> 100"
}
}

```

Then, when a user filters on the parameter, they can choose from the options **Less than $50** , **Between $50 and $100** , and **Over $100**.
For more information, see this section of the `parameter` reference page.
###  `bypass_suggest_restrictions` (field)
`bypass_suggest_restrictions` enables filter suggestions in situations where they would otherwise be disabled or limited. If you have used `sql_always_where` or `access_filter` to restrict the rows users can see, then Looker also restricts the filter suggestions to the values in the permitted rows. However, if you're certain that there are no possible values in a particular field that would reveal sensitive information, you can use `bypass_suggest_restrictions` to reinstate the full set of filter suggestions.
###  `case` (field)
`case` lets you bucket a dimension's results with case logic. This impacts filter suggestions because only the values defined in the `case` statement are shown as filter suggestions for that dimension.
A dimension that uses `case` can be used with linked filters, if the dimension is used in the filter that is updating the other filter. A dimension that uses `case` cannot be used in the filter that is being updated.
###  `full_suggestions` (field)
You can define a field with the `full_suggestions` parameter to control how Looker queries your database to provide suggestions for the field's values for a filter:
  * `full_suggestions: no`: Looker will use a basic query of distinct values, and will query only the view that contains the filter field.
  * `full_suggestions: yes`: Looker will add the Explore logic to its filter suggestion query, meaning that Looker will include any of the Explore's joins that are required to query the filter's field, and Looker will include the logic from the Explore's parameters, such as `sql_always_where`, `access_filter`, and `conditionally_filter`.


See the `full_suggestions` page for information on the Looker default behavior for providing suggestions and for considerations for Explores with `sql_always_where` or `access_filter`
###  `suggest_dimension` (field) and `suggest_explore` (field)
Looker typically generates filter suggestions by executing a SELECT DISTINCT query on the filter field. For some large tables this query can be too slow or create too large a database load. You can use `suggest_dimension` to make Looker query an alternative dimension for filter suggestions, in combination with `suggest_explore` if that dimension lives in a different Explore.
###  `suggestions` (field)
`suggestions` lets you hard-code a list of possible filter suggestion values. This can be useful if you don't want certain data values in a field to appear as suggestions, and instead want to specify a more limited list.
## Caching filter suggestions
This section describes the `suggest_persist_for` parameter, which lets you configure the length of time that filter suggestions are cached.
If you want to reduce the load on your database and the number of data values for a field is very high, consider using a parameter to disable filter suggestions for your field. If you want filter suggestions to appear, consider using a parameter to limit the filter values that are queried or to hard-code the appropriate options.
###  `suggest_persist_for` (field)
By default, filter suggestions are cached for six hours, resulting in the same list of suggestions for that length of time. The `suggest_persist_for` parameter lets you change how long filter suggestions are cached.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


