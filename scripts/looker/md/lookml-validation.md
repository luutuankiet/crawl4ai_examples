# Validating your LookML  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/lookml-validation

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Running validation
  * Validation messages
  * Deploying your changes




Was this helpful?
Send feedback 
#  Validating your LookML
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Running validation
  * Validation messages
  * Deploying your changes


When you edit your LookML, the Looker IDE will alert you to any unresolved syntax errors within a single file (see the Looker IDE overview documentation page).
To perform a full model validation, use the LookML Validator. Some errors, such as an invalid field reference due to a missing join, require a holistic look at the model and therefore are only surfaced when the LookML Validator is run. Be sure to validate your LookML changes before publishing them to the production environment. Although validation won't catch _every_ issue, such as database permission issues, it will prevent most errors.
The LookML Validator scans only LookML files that have been updated since the last LookML validation, or files that are affected by updates:
  * If a model-level setting changes, everything is validated again.
  * If a view changes, only the Explores where it is used are validated again.
  * If an Explore changes, only that Explore is validated again.


### Running validation
To run the LookML Validator, select the **Validate LookML** button at the top right of the Looker IDE; or select the **Project Health** icon at the top of the IDE to open the **Project Health** panel, and then click the **Validate LookML** icon.
After you run the LookML Validator, you may see a list of errors and other warnings that you should address. You can select any arrow to expand the lists of errors or warnings.
The validator button in the **Project Health** panel will become available again if you make and save another change.
### Validation messages
Looker displays validation messages after running validation on your LookML.
#### No LookML errors found
When there are no issues found by the validator, Looker displays a green checkmark along with the text **No LookML errors found**.
#### LookML errors
LookML errors are issues that could prevent queries from running. The number in parentheses is the number of errors found (nine in the following example):
Within the expanded list of issues you will see the reason validation didn't pass. Often times, if you click on the error, it will bring you directly to the problem row of code. You'll see a red "X" next to the row. Hovering over it will provide more detailed error information in some cases:
> **Chat Team Tip** : The validation error we are asked about most is "Unknown or inaccessible field." Visit the Error: Unknown or inaccessible field Best Practices page for the causes and what to do about it.
#### LookML warnings
LookML warnings may not prevent a query from being run, but they may still result in broken or unintended functionality for your users. As with errors, the number in parentheses is the number of warnings found (three warnings in the following example):
As with LookML errors, you can expand warnings and jump to the problem code by selecting the warning in the **Project Health** panel and then hovering over the red **X** icon to view more information:
## Deploying your changes
After you've validated that your changes will work properly, you can use Looker's Git integration to commit and deploy your changes to production.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


