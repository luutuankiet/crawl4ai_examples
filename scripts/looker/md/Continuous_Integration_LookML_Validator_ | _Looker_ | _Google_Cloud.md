# Continuous Integration LookML Validator  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ci-lookml-validator

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * LookML Validator options
    * Setting a severity threshold




Was this helpful?
Send feedback 
#  Continuous Integration LookML Validator
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * LookML Validator options
    * Setting a severity threshold


For LookML projects where all the developers are working in the Looker IDE, there is LookML validation built in to the process of deploying the project to production. But for LookML projects where some or all of your developers are working outside of the Looker IDE, using an external IDE like VSCode or Vim to write LookML, it is possible to deploy the project to production without ever validating your LookML syntax. In this case, you can run the Continuous Integration (CI) LookML Validator to find syntax issues with your LookML, such as a missing `}` or an invalid `${}` reference.
See the LookML Validator options section of this page for details on the options that you can configure when you create or edit a CI suite. For information on running the LookML Validator, see the Running Continuous Integration suites documentation page.
In the run results page, the LookML Validator provides the LookML errors in your project, along with a link to the LookML:
## LookML Validator options
The following sections describe the options for running the LookML Validator:
  * Setting a severity threshold


### Setting a severity threshold
The severity level setting determines the lowest severity level of LookML message that will cause the CI run to show a **Failed** CI status on the CI **Runs** page and the CI run results page.
In the Looker IDE, LookML validation returns syntax messages at three levels of severity: info, warning, and error.
By default, the LookML Validator will cause a **Failed** CI status only if the LookML Validator finds LookML warnings or errors in the LookML project. You can select the lowest-level message severity for which the CI LookML Validator should return a **Failed** result:
  * **Error** : The CI LookML Validator will return a **Failed** result if the LookML validation returns an error message.
  * **Warning** : The CI LookML Validator will return a **Failed** result if the LookML validation returns a warning or an error message.
  * **Info** : The CI LookML Validator will return a **Failed** result if the LookML validation returns an info, a warning, or an error message.


This severity threshold affects only the CI run status value. Regardless of the severity level setting, the LookML Validator results will show all syntax issues and display all the LookML syntax messages on the CI run results page. 
### Timeout
You can specify the number of seconds that the CI LookML Validator should run before timing out (the default is 600 seconds). If the CI LookML Validator takes longer than the timeout duration, the validation will abandon the job and return an **Error** run status. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


