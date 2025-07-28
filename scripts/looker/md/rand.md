# rand  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/rand

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  rand
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The `rand` function can be used in custom filters and table calculations to return a random number between 0 and 1.
## Syntax
**`rand()`**
The `rand` function returns a random number between 0 and 1.
## Examples
The `rand` function is often used to generate random integers, sometimes to select a random sampling of data. For example, to generate an integer between 1 and 100 (inclusive) you could use:
```
(floor(rand()*100)+1)

```

This expression works as follows:
  1. Uses the `rand()` function to generate a random number between 0 and 1.
  2. Multiplies by 100 to turn it into a random number between 1 and 100.
  3. Uses the `floor` function to round down the random number to the nearest integer, producing a random number between 0 and 99 (inclusive).
  4. Adds 1 to bring the random integer up to 1 to 100 (inclusive).


You could then filter your query to only include data below a certain random number.
## Things to know
The `rand` function produces a number with 16 decimal places, such as 0.04277424614631747.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


