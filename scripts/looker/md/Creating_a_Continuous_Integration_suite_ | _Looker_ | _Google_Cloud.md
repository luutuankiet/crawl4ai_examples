# Creating a Continuous Integration suite  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ci-create-suite

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Creating a CI suite
  * Deleting a suite




Was this helpful?
Send feedback 
#  Creating a Continuous Integration suite
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Creating a CI suite
  * Deleting a suite


A Continuous Integration (CI) suite is a set of validation instructions that is associated with your LookML project. A Looker user with the `manage_ci` permission can configure the following in a CI suite:
  * How a CI validation run is triggered (manually from the Looker IDE or automatically when a pull request is submitted to your repository).
  * Which CI validators to run.
  * Additional options for each validation test. See the documentation pages for each of the validators for details: 
    * Assert Validator
    * Content Validator
    * LookML Validator


## Before you begin
Before you can create a CI suite, you need the following:
  * A Looker instance that meets the requirements for CI and that is enabled for CI.
  * A Looker user account with the `manage_ci` permission (this permission is included in the Admin permission set).


## Creating a CI suite
You can configure and run the validators on the **Suites** page in the Looker IDE:
To create a CI suite, follow these steps:
  1. From the Looker IDE, click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click the **Suites** tab to open the **Suites** page.
  3. On the **Suites** page, you can create a new suite or edit an existing suite: 
     * To create a new suite, click the **Create suite** button.
     * To edit an existing suite, click the **Edit suite** button for the suite.
  4. Enter a name for the **Suite name**. If you are editing an existing suite, you can optionally click the pencil icon to edit the suite name.
  5. (Optional) Enable the **Trigger on pull requests from Looker** toggle if you want to set up automatic validation testing whenever a Looker developer submits a pull request to your repository. See the Triggers section of this page for more information.
If you enable pull request triggering for a CI suite, you can optionally use the **Only for target branch** field to specify that pull requests only to specific branches in the repository should trigger a run of the CI suite. See the Triggers section of this page for more information.
  6. Optionally, enable the validator toggles to turn on a validator and configure its options. See the documentation pages for each of the validators for details:
     * Assert Validator
     * Content Validator
     * LookML Validator
  7. Save your changes:
     * If you are creating a new suite, click the **Create suite** button.
     * If you are editing an existing suite, click the **Update suite** button. 


### Triggers
CI runs can be triggered in several ways:
  * Automatically, when a pull request is submitted to your LookML project's repository by a Looker developer.
  * Manually, using the **Run suite** button on the **Suites** page in the Looker IDE.
  * Manually, by rerunning a previous CI run, from the **Runs** page of the Looker IDE.


To configure a CI suite for automatic triggering on pull request, enable the **Trigger on pull requests from Looker** toggle. To use pull request triggering, your Git repository must be configured by your Looker admin on the **Continuous Integration** Admin page of Looker).
If you enable pull request triggers for a CI suite, you can optionally specify that pull requests only to specific branches in the repository should trigger a run of the CI suite. To limit automatic pull request triggers of CI runs to specific branches in your repository, enter a comma-separated list of the branches in the **Only for target branch** field.
For example, if a repository has three branches named `main`, `release_1`, and `dev`, you can enter `main, release_1` in the **Only for target branch** field. This means that CI runs will be triggered when a Looker developer submits a pull request to either the `main` or the `release_1` branch. If a Looker developer submits a pull request to the `dev` branch, this won't trigger an automatic run of the CI suite.
## Deleting a suite
To delete a CI suite, perform the following steps:
  1. From the Looker IDE, click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click the **Suites** tab to open the **Suites** page.
  3. On the **Suites** page, click the **Edit suite** button for the suite.
  4. On the suite's page, click the **Delete suite** button.
  5. In the confirmation dialog, click the **Delete suite** button.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


