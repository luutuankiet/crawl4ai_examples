# How to set up Lightdash YAML validation for VS Code - Lightdash

**Source:** https://docs.lightdash.com/guides/vs-code-yaml-validation

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
How to set up Lightdash YAML validation for VS Code
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


If you use VS Code to make edits to your dbt project, we recommend setting up Lightdash YAML validation. The validator will flag any formatting or configuration issues before compiling your project, so you can fix issues faster. The validation uses the same logic that Lightdash uses when compiling your project. All you have to do is add this snippet to your `settings.json` file in VS Code. Read this guide to details on how to edit your `settings.json`.
Copy
Ask AI
```
    "yaml.schemas": {
        "https://raw.githubusercontent.com/lightdash/lightdash/main/packages/common/src/schemas/json/lightdash-dbt-2.0.json": [
            "/**/models/**/*.yml",
            "/**/models/**/*.yaml"



```

You’ll also need to install the YAML VS Code extension for validation to work. Once you have the extension installed and settings updated, you’ll see warnings like this when working on your `schema.yml` files.
Filtering a Dashboard in the URLRenaming models, metrics, and dimensions
Assistant
Responses are generated using AI and may contain mistakes.


