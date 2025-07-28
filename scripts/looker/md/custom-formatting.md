# Adding custom formatting to fields  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/custom-formatting

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Using custom formatting in visualizations
  * Using custom formatting with table calculations and custom fields
  * Custom formatting examples
  * Time formatting for charts




Was this helpful?
Send feedback 
#  Adding custom formatting to fields
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using custom formatting in visualizations
  * Using custom formatting with table calculations and custom fields
  * Custom formatting examples
  * Time formatting for charts


> For Looker developers: The formatting shown on this page is the same as formatting used with the `value_format` LookML parameter, except that the `value_format` parameter requires the formatting string to be enclosed in double quotes.
Custom formatting gives you greater control over how numeric data appears in a Looker result set. With custom formatting, you can apply Excel-style formatting options to numeric data shown in visualizations, or produced by custom fields or table calculations.
## Using custom formatting in visualizations
For visualizations with a **Values** tab in the gear menu:
  1. Select the **Edit** menu on the **Visualization** bar.
  2. Select the **Values** tab.
  3. In the **Value Format** field, enter the custom formatting string.


For example, to add custom formatting for a table visualization:
  1. Select the **Edit** menu on the **Visualization** bar.
  2. Select the **Series** tab.
  3. In the **Customizations** section, select the **Format** drop-down and choose **Custom...**.


A new blank field will appear when you select **Custom...**. Enter the custom formatting string in the blank field.
## Using custom formatting with table calculations and custom fields
When you create or edit a table calculation or custom field, select the **Custom** option in the **Format** drop-down and enter the custom format in the blank field.
## Custom formatting examples
You can reference Excel's complete guide to specifying these formats on their Number format codes documentation page, or you can use a third-party tool to build a custom format, such as Custom Formats Builder.
Some of the most common formatting options are listed in the following table. A format code that uses `0` requires that non-significant zeros be displayed if the number contains fewer digits than specified in the code. A format code that uses `#` displays only the significant digits, even if there are fewer digits than specified in the code.
Some special characters, such as international currency symbols, must be treated as strings and enclosed in double quotes.
Format | Result  
---|---  
Integer (123)  
`00#` | Integer zero-padded to 3 places (001)  
`0 "String"` | Integer followed by a string (123 String)  
`0.##` | Number up to 2 decimals (1. or 1.2 or 1.23)  
`0.00` | Number with exactly 2 decimals (1.23)  
`00#.00` | Number zero-padded to 3 places and exactly 2 decimals (001.23)  
`#,##0` | Number with comma between thousands (1,234)  
`#,##0.00` | Number with comma between thousands and 2 decimals (1,234.00)  
`0.000,, "M"` | Number in millions with 3 decimals (1.234 M)  
`0.000, "K"` | Number in thousands with 3 decimals (1.234 K)  
Dollars with 0 decimals ($123)  
`$0.00` | Dollars with 2 decimals ($123.00)  
`"€"0` | Euros with 0 decimals (€123)  
`$#,##0.00` | Dollars with comma between thousands and 2 decimals ($1,234.00)  
`$#.00;($#.00)` | Dollars with 2 decimals, positive values displayed normally, negative values wrapped in parenthesis  
`0\%` | Display as percent with 0 decimals (1 becomes 1%)  
`0.00\%` | Display as percent with 2 decimals (1 becomes 1.00%)  
Convert to percent with 0 decimals (.01 becomes 1%)  
`0.00%` | Convert to percent with 2 decimals (.01 becomes 1.00%)  
## Time formatting for charts
If your chart as a time dimension on the x-axis, you can change the formatting of the x-axis label by using the **Time Label Format** setting in the **X** tab of the visualization options. You can format time values in by using the syntax on the Time formatting for charts page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


