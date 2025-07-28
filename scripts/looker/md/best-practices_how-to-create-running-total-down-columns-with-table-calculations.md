# Creating a running total down columns with table calculations  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-create-running-total-down-columns-with-table-calculations

Skip to main content 

Console 


  * On this page
  * Using the running_total() function




Was this helpful?
Send feedback 
#  Creating a running total down columns with table calculations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using the running_total() function


> As an alternative to the methods described on this page, when you have the appropriate permissions to create table calculations, you can use shortcut calculations. Shortcut calculations let you perform common calculations on numeric fields that are in an Explore's data table without the need to use Looker functions and operators. 
Table calculations let you create ad hoc metrics and perform calculations on the data that is returned by an Explore query. This is convenient for calculating metrics like running totals. 
This page shows you how to calculate a running total down columns in an Explore's **Data** table. You can also create a running total across rows using table calculations, which you can read more about in the Aggregating across rows (row totals) in table calculations Best Practices page. 
## Using the `running_total()` function
To create a running total down a column using table calculations, you can use the `running_total()` function, which returns the running total of the values in a specified column. 
For example, to create a running total of the column **Inventory Items Count** in the following Explore **Data** table that shows **Inventory Items Count** grouped by **Inventory Items Created Date** , you can create this table calculation: 
```
running_total(${inventory_items.count})
```

This expression yields the following results: 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


