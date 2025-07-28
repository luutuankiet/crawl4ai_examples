# Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/unixdate

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Syntax
  * Return data type
  * Related resources




Was this helpful?
Send feedback 
  * On this page
  * Syntax
  * Return data type
  * Related resources


#  UNIX_DATE
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the number of days since 1970-01-01.
## Sample usage
`UNIX_DATE(Order Date)`
## Syntax
`UNIX_DATE( date_expression )`
### Parameters
  * `date_expression`


## Return data type
Number
## Examples
Example formula  |  Output   
---|---  
` UNIX_DATE(DATE(2020,11,3)) ` |  18569   
## Notes
This function is not available for compatibility mode date types.
UNIX_DATE ignores the time parts of a Date & Time field or expression.
## Related resources
  * Looker Studio function list


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


