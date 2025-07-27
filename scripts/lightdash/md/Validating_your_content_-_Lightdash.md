# Validating your content - Lightdash

**Source:** https://docs.lightdash.com/references/validating-your-content

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Reference
Validating your content
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference
    * Lightdash CLI reference
    * Feature Maturity Levels
    * SQL Runner


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * How can I validate my content?
  * What content is included in the validation?
  * How to fix errors
  * How to dismiss errors


The content validation page can be opened by admins and developers from the project settings. There you’ll see any broken charts or dashboards in your project and information about what is causing the errors. You can access the content validation dashboard by heading to project settings, then selecting the **Validator** tab. Or, if you have active validation errors, you can also click on the bell icon in the navigation, then choose **Validation Errors**.
##  How can I validate my content?
Your project is validated any time the content validator is run. The content validator will run when:
  * a user hits `Refresh dbt` in the app
  * the command `lightdash deploy` is run on the Lightdash CLI (you can read more about automatically deploying your changes using GitHub actions here)
  * you update your project settings and hit `Test and compile`.
  * you hit `Run validation` directly inside the content validator dashboard
  * you run `lightdash validate` from the CLI


##  What content is included in the validation?
The validator will show you any errors caused by metrics or dimensions which no longer exist, have been renamed, or have invalid definitions. The validator does not show errors caused by invalid SQL at run time (e.g. invalid SQL syntax, division by 0, trying to perform numeric calculations on a string value type). Here are some examples of errors that would appear in your content validator:
  * Renaming a metric from `total_revenue` to `sum_revenue`. The old metric name is used in a chart, so it breaks the chart.
  * Deleting a dimension `is_premium_user` which is referenced in a metric’s custom SQL definition.
  * Deleting a dimension `is_premium_user` which is used as a filter on a dashboard.

The content types included in the validator dashboard are:
  * **Tables:** errors in tables are caused when dimensions or metrics that have been deleted or renamed but are still referenced in other places in the table.
  * **Charts:** errors in charts are caused when the results table or filters reference a metric or dimension which no longer exists.
  * **Dashboards:** errors in dashboards are caused when a chart is broken in the dashboard or a filter references a metric or dimension which no longer exists.


##  How to fix errors
There are a few ways to fix errors that appear in the validator: **Table errors** require you to check your YAML and fix orphaned references. This can be done with find and replace in your code editor. **Chart and dashboard errors** can be resolved by opening the content in Lightdash and updating the field references, but this usually means you have to rebuild your chart(s). The preferred method to resolve errors is to rename fields in the app or use `lightdash rename` in the CLI. You can also find and replace references in charts and dasboards using dashboards as code.
##  How to dismiss errors
You can dismiss errors from validation by clicking on the “x” button that appears when you hover over a row on the validation table. Dismissed validation errors are applied to everyone. So, if you dismiss an error, it will be removed from everyone else’s validation results as well as yours. The errors you dismissed will reappear again if you run another validation and the issue hasn’t been fixed yet.
Preview ProjectsFeature Maturity Levels
Assistant
Responses are generated using AI and may contain mistakes.


