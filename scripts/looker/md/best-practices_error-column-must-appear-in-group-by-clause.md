# Error: Column < name > must appear in the GROUP BY clause or be used in an aggregate function  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/error-column-must-appear-in-group-by-clause

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Error: Column < name > must appear in the GROUP BY clause or be used in an aggregate function
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
This page can help you troubleshoot the `column `name` must appear in the GROUP BY clause or be used in an aggregate function` error in Looker. 
This error commonly occurs when a dimension is used in a measure that does not have an aggregate type. Our measure type documentation contains a list of measure types and whether each is an aggregate type. 
For example, a `type: number` measure is not an aggregate measure, so this LookML would produce an error: 
See more code actions.
Light code theme
Dark code theme
```
measure: bad_measure {
 type: number
 sql: ${measure} + ${dimension} ;;
}

```

Typically you fix this problem by first turning the dimension into a measure, and then using that new measure in your calculations. For example: 
```
measure: dimension_total {
 type: sum
 sql: ${dimension} ;;
}

measure: good_measure {
 type: number
 sql: ${measure} + ${dimension_total} ;;
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


