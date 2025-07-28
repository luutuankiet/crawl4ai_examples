# pivot_where Function  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/pivot_where

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  pivot_where Function
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `pivot_where` function can be used in a table calculation to select a pivot column by a condition.
## Syntax
**`pivot_where(select_expression, expression)`**
The `pivot_where` function returns the value of `expression` for the pivot column which uniquely satisfies `select_expression` or `null` if such a column does not exist or is not unique.
## Examples
In the following example we look for the pivot column that is based on "Order Status", and has a value of "pending". If we find it, return the "Order Count" in that cell:
```
pivot_where(${orders.status}${orders.count})

```

## Things to know
  1. If there is _exactly_ one pivot column where `select_expression` is true, the `expression` is returned. Otherwise the `expression` returns NULL.
  2. `pivot_where` cannot be used in a custom filter.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


