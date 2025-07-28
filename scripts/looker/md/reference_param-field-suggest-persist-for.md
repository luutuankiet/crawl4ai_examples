# suggest_persist_for  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-suggest-persist-for

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Send feedback 
#  suggest_persist_for
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
```
view: view_name {
  dimension: field_name {
    suggest_persist_for: "5 hours"
  }
}

```

Hierarchy `suggest_persist_for` |  Possible Field Types Dimension, Filter, ParameterAccepts A string specifying the length of time in seconds, minutes, or hours as follows: "N (seconds | minutes | hours)"  
---|---  
## Definition
When Looker determines the values that it will suggest to users when they filter on a `dimension` or `filter` field, it runs a query to find the unique values of that field. By default this list of suggestions is cached for 6 hours. However, you can change the amount of time that suggestions are cached using `suggest_persist_for`.
Looker typically generates suggestions for a dimension by executing a `SELECT DISTINCT` query on that dimension. For some large tables this query can be too slow, or create too large of a database load. Caching suggestion values for a longer period reduces the number of `SELECT DISTINCT` queries. Alternatively, if your database is updated frequently, a shorter cache time results in fresher suggestion lists.
## Examples
Set the suggestion cache for the `name` dimension to 30 minutes:
```
dimension: name {
  sql: ${TABLE}.name ;;
  suggest_persist_for: "30 minutes"
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


