# power  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/power

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  power
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `power` function can be used in custom filters and table calculations to raise a number to the power of a given exponent.
## Syntax
**`power(base, exponent)`**
The `power` function evaluates a `base` by raising it to the power of a given `exponent`.
## Examples
The `power` function can be used to raise a number to the power of another number. For example, 23 would be written as:
```
power(2, 3)

```

Typically, the `power` function is used with a field reference or an expression. For example:
```
power(${order_item.standard_deviation_profit},
```

## Things to know
The `power` function can also be used to take the nth root of a number by using 1/n as the `exponent`. For example, the cube root (the 3rd root) of 7 would be:
```
power(7, 1/3)

```

For a square root (the 2nd root) just use the `sqrt` function.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


