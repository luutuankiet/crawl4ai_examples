# Continuous Integration Assert Validator  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ci-assert-validator

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Assert Validator options
    * Explores to query
    * Explores to exclude
    * Query concurrency




Was this helpful?
Send feedback 
#  Continuous Integration Assert Validator
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Assert Validator options
    * Explores to query
    * Explores to exclude
    * Query concurrency


The Continuous Integration (CI) Assert Validator runs the LookML data tests that were created by Looker developers in your LookML project and shows the results for each data test. For data tests that fail, the Assert Validator shows the error.
LookML data tests allow you to validate the logic of your Looker model. Data tests can test complex assumptions, such as the following:
  * Revenue in May of last year should equal $204,259.
  * Conversion rate should be greater than zero.
  * Order status shouldn't be null.


A LookML data test is made up of a small `explore_source` query and a `yesno` assert expression, such as in the following example:
```
test:historic_revenue_is_accurate {
explore_source:orders {
column:total_revenue { field:orders.total_revenue }
filters:[orders.created_date:"2024"]
}
assert:revenue_is_expected_value {
expression:${orders.total_revenue} = 626000 ;;
}
}

```

See the Assert Validator options section of this page for details on the options that you can configure when you create or edit a CI suite. For information on running the Assert Validator, see the Running Continuous Integration suites documentation page.
In the run results page, the Assert Validator shows the results for each data test. For data tests that fail, the Assert Validator shows the error or errors, as follows:
## Assert Validator options
There are several options you can specify when you create or edit a Continuous Integration suite to configure how Assert Validator runs. The options are described in the following sections of this page:
  * Explores to query
  * Explores to exclude
  * Query concurrency


### Explores to query
By default, the Assert Validator will run each data test in your LookML project.
Data tests are defined using an `explore_source` parameter that points to an Explore in your project, and you can use the **Explores to query** field to limit assert validation to specific Explores that your data tests are based on.
You can specify Explores in the following format: `model_name/explore_name`
For example, to specify the Explores named `users` and `orders` in the `thelook.model.lkml` file, you would enter the following: `thelook/users, thelook/orders`
See the SQL Validator documentation page for more information about and examples of how to specify Explores and models in this field.
### Explores to exclude
By default, the Assert Validator will run each data test in your LookML project. You can use the **Explores to exclude** field to exclude from assert validation specific Explores that your data tests are based on. The Assert Validator won't run data tests that are based on these excluded Explores.
You can specify Explores in the following format: `model_name/explore_name`
See the SQL Validator documentation page for more information about and examples of how to specify Explores and models in this field.
### Query concurrency
By default, the Assert Validator runs no more than 10 queries at a time to avoid overwhelming your Looker instance. You can use the **Query concurrency** field to specify a different maximum number of queries that the Assert Validator can run concurrently. 
The maximum value for the **Query concurrency** field is limited to the Max concurrent queries for this connection setting on your database connection.
If you notice a slowdown in your Looker instance while running Assert validation, you can decrease this value.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


