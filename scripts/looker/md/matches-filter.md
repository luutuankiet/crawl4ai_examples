# matches_filter  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/matches-filter

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  matches_filter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `matches_filter` function can be used in custom filters and custom fields to determine whether the value of a field matches a filter expression.
### Syntax
**`matches_filter(field, `filter expression`)`**
The `matches_filter` function applies the filter expression to the field and returns `Yes` if the value in the field matches the filter expression or `No` if it does not.
### Examples
This example returns `Yes` in a custom field if the invoice date is less than 30 days old:
```
matches_filter(${billing.invoice_date}, `30 days`)

```

Use the function with `matches_filter` to return different values. The next example shows syntax of a custom field that returns "Late" if the invoice date is over 30 days old:
```
if(matches_filter(${billing.invoice_date}, `30 days`), "Current", "Late")

```

### Things to know
The string that defines the filter expression must be enclosed in backtick (`) characters.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


