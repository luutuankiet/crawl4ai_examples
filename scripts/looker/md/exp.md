# exp  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/exp

Skip to main content 
  * Español – América Latina
  * Português – Brasil

Console 


  * On this page




Was this helpful?
Send feedback 
#  exp
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `exp` function can be used in custom filters and table calculations to get _e_ raised to the power of a value.
## Syntax
**`exp(value)`**
The `exp` function evaluates a `value` by calculating _e_ raised to the power of that value.
## Examples
The `exp` function can be used to calculate compound interest. For example, the compound interest formula, _pe rt_, can be written as follows:
```
${investment.principal) * exp(${investment.rate}${investment.term})

```

## Things to know
The number _e_ (2.7182818284590...) is an important mathematical constant, which you can read more about in this Wikipedia article. It has many applications, including calculating compound interest, performing certain probability calculations, generating normal distributions, and so on.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


