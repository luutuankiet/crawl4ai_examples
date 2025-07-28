# Why are my fields with division showing up as 0?  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-fields-with-division-displaying-0

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * The solution: Cast your field as a floating-point number 




Send feedback 
#  Why are my fields with division showing up as 0?
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * The solution: Cast your field as a floating-point number 


In certain dialects, including Postgres and Redshift, performing a calculation between integers (like dividing counts) will return an integer even if the result would be a decimal in normal math. For example, you might make measures like the following: 
```
measure: sold_ratio {
    type: number
    sql: ${sold_count} / ${total_count} ;;
    value_format: "0.00" # Number with exactly 2 decimals (1.23)
}
```

However, when you run the measures in an Explore, the **Sold Ratio** column returns zero, and the **Sold Percent** column does not have its decimal places populated. This is not correct: 
Inventory Items Sold Percent | Inventory Items Sold Ratio | Inventory Items Count | Inventory Items Sold Count  
---|---|---|---  
48.00 | 0 | 1,165,224 | 560,223  
##  The solution: Cast your field as a floating-point number 
If the calculation is multiplied by a non-integer, the values will cast as floats, and decimals will be returned as expected. You can multiply the numerator by a decimal number (like 1.0 or 100.0) to force SQL to return a decimal result: 
```
measure: sold_ratio {
    type: number
    sql: 1.0 * ${sold_count} / ${total_count};;
    value_format: "0.00"
}
```

The resulting Explore **Data** table now displays the expected results: 
Inventory Items Sold Percent | Inventory Items Sold Ratio | Inventory Items Count | Inventory Items Sold Count  
---|---|---|---  
48.08 | 0.48 | 1,165,224 | 560,223  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


