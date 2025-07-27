# Viewing the results of a CI run  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ci-view-results

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * CI run results
    * Viewing results for incremental validation




Was this helpful?
Send feedback 
#  Viewing the results of a CI run
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * CI run results
    * Viewing results for incremental validation


With Looker Continuous Integration (CI), if you manually trigger a new run of a suite or a rerun of a previous CI run, the Looker IDE automatically displays the run results page for the manual run. Otherwise, no matter how a run is triggered, a Looker user with the `see_ci` permission can access the run results from the **Runs** page in the Looker IDE:
The **Runs** page lists the CI runs for the LookML project, along with the following information:
  * **Status** : The status of the run: 
    * **Queued** : The run is waiting for another CI run to be completed before starting.
    * **Running** : The validators defined by the CI suite are running.
    * **Passed** : All of the validators in the CI suite were completed successfully and none of the validators returned an error.
    * **Failed** : All of the validators in the CI suite were completed successfully and at least one of the validators returned an error.
    * **Error** : One or more of the validators in the CI suite failed to run.
    * **Cancelled** : The CI run was cancelled.
  * **Suite** : The name of the CI suite.
  * **Trigger** : How the suite was triggered (manual, pull request, or API).
  * **Git state** : Information about the branch or commit that was validated in the run: 
    * For manual runs, the value is either "Production" or the name of the development branch.
    * For runs triggered by a pull request, the value is a hyperlink to the commit SHA of the pull request. Click the commit SHA hyperlink to open the pull request in another browser tab.
  * **Triggered at** : The time that the CI run was initiated.


## CI run results
On the **Runs** page, click the **View Run** button for a CI run to see its validation results:
The run results page for a CI suite shows the following information:
  1. The LookML project and Git details that the run validated (and the commit, for runs triggered by a pull request).
  2. Information about the CI run: 
     * How and when the run was triggered.
     * The Looker user who initiated the run (for manual runs) or the branch and commit (for runs triggered by a pull request).
     * How long it took the CI run to be completed.
     * How long the run was waiting in the queue before beginning.
  3. For validators that return errors, the results page shows each error, along with the error message and links to the LookML, Explore, or content so that you can test and correct each error.
  4. For validators that found no errors, the results page shows a success message.


### Viewing results for incremental validation
For CI validator runs configured for incremental validation (for the SQL Validator or the Content Validator), the validator will return errors that exist only on the development branch or pull request commit; validators enabled for incremental validation won't return an error if the error already exists in the production version.
The following is an example of a results page for an incremental validation of the SQL Validator:
  1. The results page shows errors that exist only in the development branch or commit.
  2. If an Explore has no changes in the development branch or commit, the validator will skip the Explore during validation. These Explores are marked with "Skipped" in the validator results.
  3. The validators that were run incrementally are marked with "Incremental" in the validation results.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


