# Looker Continuous Integration  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/continuous-integration

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling Continuous Integration




Was this helpful?
Send feedback 
#  Looker Continuous Integration
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling Continuous Integration


The Looker Continuous Integration (CI) features let you run tests on your LookML project to deliver more reliable, efficient, and user-friendly data experiences. You can use the CI validators to catch issues with SQL, data tests, content, and LookML before they hit production to verify your LookML and prevent query errors for your users. You can also configure the CI validators to run automatically when a pull request is submitted to your LookML repository.
CI is composed of the following validators, which run different checks against your Looker instance:
  * SQL Validator — Verifies that the dimensions in your Explores run correctly against your database.
  * Assert Validator — Runs any LookML data tests that were created by your Looker developers and returns all failures and errors.
  * Content Validator — Runs the Looker content validation to test for errors in the Looks and dashboards in your LookML project.
  * LookML Validator — Runs the LookML Validator to test for LookML errors in the project.


To use these validators on your LookML instance, you can create a _CI suite_ , which defines a set of validators and their options that are associated with your LookML project. See the following pages for information on CI suites:
  * Creating a Continuous Integration suite
  * Running Continuous Integration suites
  * Viewing the results of a CI run


## Requirements
To use Continuous Integration, you need the following:
  * A Looker-hosted instance that is enabled for Continuous Integration.
  * A Looker user account with at least one of the following permissions (both of these are included in the Admin permission set):
    * `see_ci`: required to view the results of CI runs, view the CI **Suites** page, and run CI suites.
    * `manage_ci`: required to create CI suites, manage CI users, and configure the Git connection with Continuous Integration.


## Enabling Continuous Integration
To enable Continuous Integration, a Looker admin must perform the following tasks:
  * Enable the instance for Continuous Integration in the **Continuous Integration** page of the Looker **Admin** panel.
  * Create a Continuous Integration user.
  * Install the CI GitHub app in your GitHub organization. (This is highly recommended for all implementations, and required if you want to use pull requests to trigger CI validation runs).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


