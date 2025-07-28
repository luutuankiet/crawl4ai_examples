# pivot_index function  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/pivot_index

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  pivot_index function
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `pivot_index` function can be used in table calculations to extract and manipulate the value of a pivoted column based on its index (in other words, its position).
## Syntax
**`pivot_index(expression, pivot_index)`**
The `pivot_index` function evaluates `expression` in the context of the pivot column at the position `pivot_index` (1 for first pivot, 2 second pivot, etc.) The function returns null for unpivoted results.
## Examples
The following table shows a query that counts the number of orders made in each season of the year. The query includes a pivoted dimension, **Products Category** , which has the values `Swimwear` and `Coats`. To compute the total number of orders made in each season across all categories, create a **Total Orders Count** table calculation.
Products Category | Swimwear | Coats | Total Orders Count  
---|---|---|---  
Season | Orders Count | Orders Count  
Winter | 3 | 671 | 674  
Spring | 278 | 120 | 398  
Summer | 840 | 21 | 861  
Fall | 30 | 432 | 462  
The **Total Orders Count** table calculation adds the value of the first pivot column to the value of the second pivot column. The formula is:
```
pivot_index(${orders.count},${orders.count},
```

## Things to know
`pivot_index` cannot be used in a custom filter.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


