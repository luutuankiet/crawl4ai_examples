# Creating tailored tables from a single dbt model - Lightdash

**Source:** https://docs.lightdash.com/guides/explores

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
Creating tailored tables from a single dbt model
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
  * What this guide covers
  * When to use explores
  * Table config options you can use


##  What this guide covers
You’ll learn how to use the `explores` config in Lightdash to define **multiple curated table experiences** from a single dbt model. Each explore appears as its own table in the **Query from tables** list in Lightdash.
##  When to use explores
Use the explores config when you want to create tailored versions of the same table for different teams or use cases. For example:
  * Show different columns or joins depending on the audience (e.g. Users + CRM for Sales, Users + product usage for PMs)
  * Customize each version of the table to match a specific workflow or department
  * Restrict access to certain versions or fields using user attributes (e.g. exec-only views, region-based filters, or hiding PII)


##  Quickstart
Start with your base model
This is your regular dbt model, for example, `deals`.
Copy
Ask AI
```
models:
name: deals
    meta:
      primary_key: deal_id

```

Add an explores section under meta
Use the `explores` config to define multiple versions of the table. Each explore has its own `label`, `joins`, joined fields, and access rules.
Copy
Ask AI
```
models:
name: deals
    meta:
      primary_key: deal_id
      label: Deals (Basic)
      description: Basic deals table with no joins
      explores:
        deals_accounts:
          label: Deals w/Accounts
          description: Deals table with accounts joined in, limited acount fields included
          joins:
join: accounts
              relationship: many-to-one
              sql_on: ${deals.account_id} = ${accounts.account_id}
              fields: [industry, segment, count_accounts]
        deals_exec_view:
          label: Deals (Exec View)
          description: Deals table with account info, for execs only, all acount fields included
          required_attributes:
            is_exec: "true"
          joins:
join: accounts
              relationship: many-to-one
              sql_on: ${deals.account_id} = ${accounts.account_id}

```

Preview the result in Lightdash
Once you commit and deploy your dbt changes:
  * Go to Query from tables in Lightdash
  * You’ll now see: 
    * **Deals (Basic)**
    * **Deals w/Accounts**
    * **Deals (Exec View)** (only visible to users with the required attribute)

Each shows up as its own table in the UI, but all use the same `deals` model.
##  Table config options you can use
Inside each explore definition, you can use any of the existing table config options, including:
  * `label`
  * `joins`
  * `sql_filter`
  * `description`
  * `default_filters`
  * `required_attributes`

📚 Read the Tables reference docs for all configuration options
How to join tablesFiltering a Dashboard in the URL
Assistant
Responses are generated using AI and may contain mistakes.


