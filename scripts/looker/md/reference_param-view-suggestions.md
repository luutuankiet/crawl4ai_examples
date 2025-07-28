# suggestions (for views)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-suggestions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to know
    * suggestions at the view level works differently than suggestions at the dimension level
    * You can disable suggestions for individual dimensions




Was this helpful?
Send feedback 
#  suggestions (for views)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to know
    * suggestions at the view level works differently than suggestions at the dimension level
    * You can disable suggestions for individual dimensions


> This page refers to the `suggestions` parameter that is part of a view.
> `suggestions` can also be used as part of a dimension or filter field, described on the `suggestions` (for fields) parameter documentation page.
## Usage
```
view: view_name {
  suggestions: yes
}

```

Hierarchy `suggestions` |  Default Value `yes`Accepts A Boolean (`yes` or `no`)  
---|---  
## Definition
When a user filters an Explore on a field that supports suggestions, by default Looker will suggest possible values for the field (see Changing filter suggestions for information about how you can affect filter suggestions).
Looker provides the dimension's possible values from the database and suggests the possible values based on what the user has typed in the filter field. Suggestions are on by default for most dialects. You can add the `suggestions: no` statement to a `view` definition to disable filter value suggestions for all the dimensions in the view that support suggestions.
> For some dialects, such as Amazon Athena, Qubole Presto, Trino, Cloudera Impala, Apache Hive, and Apache Spark, providing suggestions requires querying the database, which may be expensive. Because of this, if you use Looker to automatically generate a project from your database for these dialects, Looker will create the views with the `suggestions: no` declaration.
## Example
Here is an example view where suggestions are disabled for all dimensions:
```
view: aircraft_types {
  sql_table_name: flightstats.aircraft_types ;;
  suggestions: no
  ...
}

```

## Things to know
###  `suggestions` at the view level works differently than `suggestions` at the dimension level
The `suggestions` parameter described on this page is applied to a view and works differently than the `suggestions` parameter applied to a dimension. When applied at the dimension level, `suggestions` lets you hard-code a list of suggestions for that dimension.
If you want to disable suggestions for an individual dimension, you can use the `suggestable: no` statement for the dimension.
### You can disable suggestions for individual dimensions
If you want to disable suggestions for an individual dimension, you can add the `suggestable: no` statement to the dimension's definition instead of using `suggestions: no` for the entire view. The inverse doesn't work, however: you cannot define a view with `suggestions: no` and then use the `suggestable: yes` statement to _enable_ suggestions for individual dimensions in the view. The behavior is set up this way because, if a developer is specifying `suggestions: no` at the view level, the developer wants to prevent expensive queries on the database for that view, so suggestions should be kept off for all dimensions in the view.
As an alternative, for a view with `suggestions: no`, you can use the `suggestions` parameter for individual dimensions to hard-code possible values for a filter even if the dimension's view has the `suggestions: no` statement, since hard-coded values don't require a query on the database.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


