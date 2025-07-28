# ln  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ln

Skip to main content 
  * Español – América Latina
  * Português – Brasil

Console 


  * On this page




Was this helpful?
Send feedback 
#  ln
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `ln` function can be used in custom filters and table calculations to get the natural logarithm of a value.
## Syntax
**`ln(value)`**
The `ln` function takes the logarithm of a `value` to the base of the mathematical constant _e_.
## Examples
The `ln` function can be used to model exponential growth linearly by taking `ln` of the dependent variable. For example:
```
ln(order_items.growth_rate)

```

## Things to know
`ln` can be used to give you the time needed to reach a certain level of growth. For instance, modeling growth exponentially as:
_growth = e time_
_time_ can be determined using `ln` as follows:
```
ln(growth)

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


