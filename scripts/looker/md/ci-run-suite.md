# Running Continuous Integration suites  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ci-run-suite

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Automatic triggering from pull requests
  * Manually triggering a new run of a CI suite
  * Manually re-running a previous CI run
  * Cancelling a CI run




Was this helpful?
Send feedback 
#  Running Continuous Integration suites
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Automatic triggering from pull requests
  * Manually triggering a new run of a CI suite
  * Manually re-running a previous CI run
  * Cancelling a CI run


Continuous Integration (CI) runs can be triggered in several ways:
  * Automatically when a pull request is submitted to your LookML project's repository by a Looker developer (see the Creating a Continuous Integration suite page for information on setting this up).
  * Manually triggering a new run of a CI suite from the Looker IDE.
  * Manually re-running a previous CI run from the Looker IDE.


Once the validation tests have completed, you can review the results, as described on the Viewing Continuous Integration run results documentation page.
## Automatic triggering from pull requests
If you have enabled your CI suite with **Trigger on pull requests from Looker**, CI will trigger a validation run automatically when a Looker developer submits a pull request to your LookML repository. (You can optionally specify that pull requests only to certain branches in your repository should trigger automatic CI runs.)
For automatic pull request validation runs, CI validates the latest pull request commit and returns all of the errors in that version of the repository. 
See the Viewing Continuous Integration run results documentation page for information on viewing the results.
## Manually triggering a new run of a CI suite
A Looker user with the `see_ci` permission can manually trigger a CI run from the Looker IDE.
To manually trigger a new run of a CI suite, follow these steps:
  1. From the Looker IDE, click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click **Suites** to open the **Suites** page.
  3. Click the **Run suite** button for the CI suite that you want to run (if you don't have any CI suites for your project, you can create a CI suite).
  4. In the **Trigger a run manually** dialog, use the **Workspace** options to select the branch that you want to validate (see the Workspace section for details):
     * To validate the production version of your LookML project, click **Production**.
     * If you want to validate a development branch of your LookML project, click **Dev Mode**. Use the **Branch** pull-down menu to select which development branch to validate.
  5. To trigger the run of the CI suite, click **Start run**.


The CI suite may take several minutes to complete running, depending on the size of your project, the validators that are included in the CI suite, and the configuration of the CI suite.
After you trigger a run, the Looker IDE will display the **Run** page for the suite that you triggered. Once the validation tests are completed, the **Run** page will show the results for each of the validators. You can navigate away from the **Run** page while the validation tests are running, and then later return to the **Run** page to see the results.
See the Viewing Continuous Integration run results documentation page for information on viewing the results.
### Workspace
When you manually trigger a CI run, you can use the **Workspace** options to validate either the production version of your repository or a development branch of your repository.
For the **Production** option, if you want to identify which branch or commit is used for the production version, you can look in the Looker IDE in the **Default Production Branch** field of the **Git Summary** section of the **Branch Management** page of the **Project Settings** :
  * For projects configured with advanced deploy mode, the production version is a commit or tag that is selected in the deployment manager by a Looker developer who has the `deploy` permission.
  * For projects without advanced deploy mode, the production version is the branch configured in the **Git Production Branch Name** field in the **Project Configuration** page of the **Project Settings**.


For the **Dev Mode** option, note the following for validating development branches in your project:
  * To see the branches in your LookML project and to identify the production branch and the personal branches of your developers, refer to the **Branch Management** page of the **Project Settings** of your project in the Looker IDE. 
  * To validate a development branch, the development branch must be pushed to your LookML repository. In the Looker IDE, that means the developer must click the **Commit Changes & Push** button or select the **Commit** option from the Git Actions panel in the IDE.


## Manually re-running a previous CI run
For runs that have finished (if the run passed, failed, errored, or was cancelled), a Looker user with the `see_ci` permission can manually trigger a rerun of the CI run from the Looker IDE:
  * If you rerun a PR-triggered run, Continuous Integration runs against the same commit as the original run.
  * If you rerun a manually-triggered run, Continuous Integration runs against the production state or branch HEAD _at the time of the rerun_ , which will include any subsequents commits that were made since the initial CI run.


In addition, if you have edited the CI suite since the initial run, a rerun will include any changes that you made to the CI suite since the initial run.
To rerun a CI run, follow these steps:
  1. From the Looker IDE, click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click **Runs** to open the **Runs** page.
  3. On the **Runs** page, click the **View Run** button for the CI run you want to cancel.
  4. On the run results page for the selected run, click the **Rerun** button at the top of the page.


Once you click **Rerun** , the Content Validator will initiate the run and return you to the **Run** page for the new run.
See the Viewing Continuous Integration run results documentation page for information on viewing the results.
## Cancelling a CI run
If you want to cancel a CI run that is running, you can do so from its **Run** page by following these steps:
  1. From the Looker IDE, click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click **Runs** to open the **Runs** page.
  3. On the **Runs** page, click the **View Run** button for the CI run you want to cancel.
  4. On the **Run** page for the selected run, click the **Cancel** button at the top of the page.


Once you click **Cancel** , Continuous Integration will cancel the run display the **Cancelled** status on the **Run** page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


