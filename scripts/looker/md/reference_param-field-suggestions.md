# suggestions (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-suggestions

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  suggestions (for fields)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


> This page refers to the `suggestions` parameter that is part of a dimension, filter field, or parameter.
> You can also use `suggestions` as part of a view, as described on the `suggestions` (for views) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    suggestions: ["suggestion string", "suggestion string", "…"]
  }
}

```

Hierarchy `suggestions` |  Possible Field Types Dimension, Filter, ParameterAccepts A string or a list of strings  
---|---  
## Definition
When a user filters an Explore on a field type that supports suggestions, by default Looker will suggest possible values for the field (see Changing filter suggestions for information about how you can affect filter suggestions). To provide suggestions for a filter field, Looker executes a query on your database to retrieve a list of distinct values for the field. Looker typically generates these suggestions by executing a query such as the following on the filter field:
```
SELECT DISTINCT field_name FROM table
WHERE (field_name LIKE '%' OR field_name LIKE '% %')
GROUP BY 1 ORDER BY 1 LIMIT 1000

```

The `suggestion` parameter lets you hard-code the list of suggested values for a dimension, filter field, or parameter that will appear when someone uses that field to filter a query.
If the field is in a large table, this query can be too slow or create too large a database load. By using `suggestions` you can hard-code a list of possible values instead and improve performance.
The `suggestions` parameter is also useful because it lets you specify a more limited list if you don't want certain values from a field to appear as suggestions.
## Examples
Replace the default suggestions for the `colors` dimension with a hard-coded list:
```
dimension: colors {
  type: string
  sql: ${TABLE}.colors ;;
  suggestions: ["red", "yellow", "blue"]
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


