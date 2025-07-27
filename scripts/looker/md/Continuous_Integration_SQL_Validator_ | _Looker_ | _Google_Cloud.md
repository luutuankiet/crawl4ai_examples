# Continuous Integration SQL Validator  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ci-sql-validator

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Resource consumption
  * Exclude dimensions from SQL validation
  * SQL Validator options
    * Explores to query
    * Explores to exclude
    * Query concurrency
    * Incremental validation




Was this helpful?
Send feedback 
#  Continuous Integration SQL Validator
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Resource consumption
  * Exclude dimensions from SQL validation
  * SQL Validator options
    * Explores to query
    * Explores to exclude
    * Query concurrency
    * Incremental validation


The Continuous Integration (CI) SQL Validator verifies that the dimensions in your Explores run correctly against your database. To do this, the SQL Validator runs a series of queries on the Explores in your LookML project. 
By default, the SQL Validator performs the following tasks:
  1. For each Explore in your project, the SQL Validator runs an Explore query that includes every dimension in the Explore.
  2. If Looker returns an error for the Explore query, the SQL Validator will then run a separate Explore query for each dimension in the Explore.


If you don't want the SQL Validator to test every dimension in every Explore, you can optionally do one or more of the following:
  * Configure the SQL Validator to query only certain Explores.
  * Configure the SQL Validator to exclude certain Explores.
  * Configure the SQL Validator to ignore your LookML dimensions that are defined with `hidden: yes`.
  * Add a `ci: ignore` comment or tag  to a dimension's LookML to prevent SQL Validator from including the dimension in any of its Explore queries.


See the SQL Validator options section of this page for details on the options you can configure when you create or edit a CI suite. For information on running the SQL Validator, see the Running Continuous Integration suites documentation page.
In the run results page, the SQL Validator shows each SQL error, categorized by dimension and Explore, with a link to the problematic LookML and an **Explore from here link** for debugging:
## Resource consumption
The SQL Validator is designed to consume the fewest resources within Looker and within your data warehouse. All SQL Validator queries include a `LIMIT 0` and `WHERE 1=2` clause. These clauses effectively instruct the query planner in your data warehouse not to process data but to check the validity of the SQL. 
With BigQuery, for example, this type of query is similar to running a dry run query in BigQuery. For BigQuery, `LIMIT 0` queries don't scan data, so you shouldn't be charged for the queries that the SQL Validator runs.
## Exclude dimensions from SQL validation
You may want to exclude certain dimensions from SQL validation, such as dimensions that are dependent on a parameter, since the parameter's value will be null during validation and will always cause a SQL error.
You may also want to exclude dimensions that don't have a `sql` parameter, such as dimensions of `type: distance`, `type: location`, or `type: duration`.
To exclude a dimension from SQL validation, you can modify the dimension's LookML in one of two ways:
  * You can add a `ci: ignore` statement in the `tags` parameter of the dimension's LookML definition, as shown in the following example:
```
dimension:addresses{
sql:${TABLE}.addresses;;
tags:["ci: ignore"]
}

```

  * You can add the comment `-- ci: ignore` to the `sql` field of your dimension's LookML, as shown in the following example:
```
dimension:addresses{
sql:
--ci:ignore
${TABLE}.addresses;;
}

```



## SQL Validator options
You can specify several options when you create or edit a Continuous Integration suite to configure how SQL Validator runs. The options are described in the following sections of this page:
  * Explores to query
  * Explores to exclude
  * Ignore hidden
  * Query concurrency
  * Incremental validation


### Explores to query
By default, the SQL Validator will run SQL validation on all models and Explores in your LookML project.
You can use the **Explores to query** field to specify the Explores and models that you want to include in the SQL validation.
You can specify Explores in the following format: `model_name/explore_name`
Note the following:
  * For `model_name`, use the name of the model file without the `.model.lkml` extension. For example, to specify the model defined in `thelook.model.lkml`, you would enter `thelook`.
  * For `explore_name`, use the `explore_name` from the `explore` LookML parameter. For example, to specify the Explore defined as `explore: users` in your LookML project, you would enter `users`.
  * You can create a comma-separated list to specify multiple Explores.
  * You can use the `*` wildcard in `model_name` or `explore_name`.


Here are some examples:
  * To specify only the **Users** Explore that is defined with `explore: users` in the file `thelook.model.lkml`, you would enter the following:
```
thelook/users

```

  * To specify the Explores named `users` and `orders` in the `thelook.model.lkml` file, you would enter the following:
```
thelook/users, thelook/orders

```

  * To specify all of the Explores in `thelook.model.lkml`, you would enter the following:
```
thelook/*

```

  * To specify every Explore named `users` across all models in your project, you would enter the following:
```
*/users

```



### Explores to exclude
By default, the SQL Validator will run SQL validation on all models and Explores in your LookML project.
You can use the **Explores to exclude** field to specify the Explores and models that you want to exclude from the SQL validation. 
You can specify Explores in the following format: `model_name/explore_name`
See the Explores to query section for more information about how to specify Explores for the SQL Validator.
### Fail fast
By default, the SQL Validator runs one query per Explore with all of the dimensions in the query. If that Explore query fails, the SQL Validator will then do an Explore query for each dimension in the Explore individually. 
For faster validation, you can enable the **Fail fast** option so that the SQL Validator will run only the initial query for an Explore, the query that contains all of the dimensions at once. If that query returns an error, the SQL Validator will display that error in the CI run results, and move on to the next Explore being validated.
With **Fail fast** enabled, the validation usually is completed faster. However, the SQL Validator results will show only the first error for each Explore, even if multiple dimensions may have errors. This means that, after you fix the first error, the next run of the SQL Validator may show an additional error.
### Ignore hidden
Enable the **Ignore hidden** field if you want the SQL Validator to ignore the LookML dimensions that your Looker developers defined with `hidden: yes`. The SQL Validator will leave these dimensions out of its Explore queries during validation.
### Query concurrency
By default, the SQL Validator runs no more than 10 queries at a time to avoid overwhelming your Looker instance. You can use the **Query concurrency** field to specify a different maximum number of queries that the SQL Validator can run concurrently. 
The maximum value for the **Query concurrency** field is limited to the Max concurrent queries for this connection setting on your database connection.
If you notice a slowdown in your Looker instance while running SQL validation, you can decrease this value.
### Incremental validation
Incremental validation is a method of finding errors that are unique to a specific development branch, errors that don't already exist in production. Incremental validation helps developers find and fix the errors that they are responsible for without being distracted by existing errors in the project, and it can also make validation faster, especially for LookML projects that contain many Explores.
For incremental validation, the SQL Validator runs only the Explore queries that have changed between a development version (the _base reference_) and the production version (the _target reference_). The SQL Validator returns only the errors that are unique to the development version, even if the production version itself has errors.
In the validator results, the SQL Validator indicates each Explore that was skipped because it had no changes to its compiled SQL in the branch or commit being validated. See Viewing results for incremental validation for an example of incremental validation results.
You can enable incremental validation for the SQL Validator by enabling the **Only incremental errors** checkbox in the **SQL Validator** section when you create or edit a Continuous Integration suite.
Note the following for incremental validation:
  * The incremental validation setting does not apply when the SQL Validator is validating the production branch itself, such as with manual runs on the production branch. When validating the production branch, the SQL Validator runs a full validation.
  * **Fail fast** mode is not supported for incremental validation runs, since individual dimension queries are required to expose the incremental errors that are specific to a development branch of the project.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


