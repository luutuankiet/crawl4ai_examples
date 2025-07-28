# Convert Text and Numbers to Date and Date & Time  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/convert-text-and-numbers-to-date-and-date--time

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Can't convert to date
    * Change the underlying data
    * Convert to date using a calculated field
  * Related resources




Was this helpful?
Send feedback 
#  Convert Text and Numbers to Date and Date & Time
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Can't convert to date
    * Change the underlying data
    * Convert to date using a calculated field
  * Related resources


Dates and times in your underlying data sets can be represented in different ways. Some data sets clearly indicate that a particular field is a date or datetime. In these cases, Looker Studio creates Date or Date & Time fields in your data source to handle that information.
Sometimes, though, the data is ambiguous, making it difficult for Looker Studio to know how to handle it. For example:
  * `20201210` could represent a number or currency value: `$20,201,210`.
  * `12/10/2020` could represent `Dec 10, 2020` or `Oct 12, 2020`


## Can't convert to date
If you connect to data that contains ambiguous dates or times, you may see a message saying `Looker Studio can't convert [field] to a date`. To resolve this, do one of the following:
### Change the underlying data
If you can edit the dataset, consider changing the format of your date field to a full year, month, and day format. You may also be able to set the field's data type to date or date and time. This is the recommended approach, especially if you'll be creating multiple data sources from this dataset.
### Convert to date using a calculated field
To create a valid Date or Date & Time field from your original unrecognized field, create a new calculated field and use the PARSE_DATE or PARSE_DATETIME function. See the following examples, replacing `field` with the name of the original (unrecognized) field.
#### Example formulas
If your `field` is originally a text field:
Format  |  Formula   
---|---  
2020-03-18  |  PARSE_DATE("%Y-%m-%d", _field_ )   
2020/03/18  |  PARSE_DATE("%Y/%m/%d", _field_ )   
20200318  |  PARSE_DATE("%Y%m%d", _field_ )   
3/18/2020  |  PARSE_DATE("%m/%d/%Y", _field_ )   
18/3/2020  |  PARSE_DATE("%d/%m/%Y", _field_ )   
Mar 18, 2020  |  PARSE_DATE("%b %d, %Y", _field_ )   
Wed, Mar 18, 2020  |  PARSE_DATE("%a, %b %d, %Y", _field_ )   
March 18, 2020  |  PARSE_DATE("%B %d, %Y", _field_ )   
Wednesday, March 18, 2020  |  PARSE_DATE("%A, %b %d, %Y", _field_ )   
If includes the time:
Format  |  Formula   
---|---  
2020-03-18 16:45:00.000000  |  PARSE_DATETIME("%Y-%m-%d %H:%M:%E\\*S", _field_ )   
2020-03-18T16:45:00.000000  |  PARSE_DATETIME("%Y-%m-%dT%H:%M:%E\\*S", _field_ )   
If your `field` is originally a number:
Format  |  Formula   
---|---  
20200318  |  PARSE_DATE("%Y%m%d", CAST( _field_ AS TEXT))   
## Related resources
  * About calculated fields


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


