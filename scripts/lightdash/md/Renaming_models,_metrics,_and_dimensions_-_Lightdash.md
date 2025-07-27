# Renaming models, metrics, and dimensions - Lightdash

**Source:** https://docs.lightdash.com/guides/renaming-models-and-fields

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
Renaming models, metrics, and dimensions
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
    * Lightdash semantic layer
    * Adding and managing Tables
    * How to create dimensions
    * How to create metrics
    * How to join tables
    * Multiple tables from one dbt model
    * Filtering a Dashboard in the URL
    * How to set up Lightdash YAML validation for VS Code
    * Renaming models, metrics, and dimensions
  * Reference


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
  * Rename in Lightdash
  * Rename in the CLI
  * Important CLI callouts
  * Example CLI Workflow
  * Reverting changes


This guide explains how to rename metrics, dimensions, or models across your entire project. All field or model references will be updated across charts, dashboards, and scheduled deliveries. This feature is useful when you need to standardize naming conventions, update your dashboards after making model changes or just fix some typos quickly.
**Admin access required:** This feature is restricted to admin users because it updates content project-wide, including charts and dashboards that users may not have access to modify.
Content can also be renamed using Dashboards as code. However, the rename methods in this doc require fewer steps and will automatically respect the right syntax for different field types.Chart names and descriptions will not be updated using these rename workflows. If you want to update those in bulk, we recommend using Dashboards as code.
##  Rename in Lightdash
If you change field or table names in dbt that are being used in Lightdash, you will receive validation errors. You can fix these directly on the validation page by renaming references in the broken charts. You can easily access the validation page by clicking on the bell on the navigation bar. Read the validation docs here. On the validation page, hover over the chart you want to fix, and click on the **Fix** button. You can now choose to rename a field or model using the list of **existing** values. You also have the option to **Fix all occurrences, **which allows you to rename the same field or table in all affected content, such as other charts, dashboards and scheduled deliveries. If you have made multiple field or table changes to the same chart (e.g., you changed two metrics), you will need to perform multiple rename actions. After renaming, you can rerun validation to ensure everything works as expected.
##  Rename in the CLI
The Lightdash CLI offers an alternative and more flexible approach to renaming models or fields across your project. This is a more advanced option than the UI and affects all the content in the project. The CLI will also allow you to rename content before changes happen to dbt.
###  Important CLI callouts
  * Renaming is project-wide by default, but can be scoped to a specific model using the `--model` option.
  * Always use `--dry-run` first to understand the impact of your changes.
  * You can use `--list` on your actual run to get a full list of everything that was updated.
  * Only lowercase letters (a-z) and underscores `_` are allowed in field and table names.


###  Example CLI Workflow
This is a sample of how you can take the most from this feature, when renaminig content on your dbt project.
  1. Rename a field in your dbt project YML file: `user_id` becomes `customer_id`.
  2. Create a preview environment to test those changes.
  3. Existing charts will fail, you can go into validation to confirm which ones are affected.
  4. Run `lightdash rename --type field --from user_id --to customer_id -p <preview-project-id> --dry-run` to list the affected charts.
  5. If you are happy with the changes, run rename without `--dry-run`.
  6. Confirm all charts are referencing new fields (they might still error if you haven’t updated your warehouses using dbt run).
  7. Merge the code, run dbt, then run `lightdash rename --type field --from user_id --to customer_id -p <production-project-id> --list` on your main project.


  * The `--list` option gives you a full list of content that was changed.

The CLI will show you which charts, dashboards, alerts, and dashboard schedulers will be updated and also, we will generate a JSON log that contains the affected chart and dashboard names and UUIDs, you can use those UUIDs to manually revert some of the charts to a previous version. Read the CLI reference doc for all arguments and more examples.
##  Reverting changes
When renaming, a new chart version is created with the new changes. If you make a mistake during renaming, you can restore individual charts by using version history.
How to set up Lightdash YAML validation for VS CodeOverview
Assistant
Responses are generated using AI and may contain mistakes.


