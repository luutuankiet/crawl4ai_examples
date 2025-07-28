# COUNT  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/count

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  COUNT
Stay organized with collections  Save and categorize content based on your preferences. 
The `COUNT` function counts the number of items in a field.
## Syntax
`COUNT( X )`
### Parameters
  * - a field or expression that contains the items to be counted.


## How the `COUNT`
The `COUNT``COUNT`
To count only unique items, use `COUNT_DISTINCT` or `APPROX_COUNT_DISTINCT`.
> There are 2 other ways to apply this function:
>   * In a data source, change a field's **Aggregation** type to `Count`.
>   * in a report, edit the field's aggregation in a chart.
> 

## Examples
`COUNT(Page)`**Page** dimension.
## Limits of `COUNT`
You can't apply this function to a pre-aggregated field ( **Aggregation** type of **Auto** ), or to an expression which is the result of another aggregation function. For example, a formula such as `COUNT(SUM(x))` will produce an error. 
## Related resources
  * Looker Studio function list


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


