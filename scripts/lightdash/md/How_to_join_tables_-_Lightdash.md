# How to join tables - Lightdash

**Source:** https://docs.lightdash.com/guides/how-to-join-tables

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Guides
How to join tables
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
  * Declare joins in dbt model properties


##  Declare joins in dbt model properties
Joins let you to connect different models to each other so that you can explore more than one model at the same time in Lightdash and see how different parts of your data relate to each other. You add joins to your YAML files under the `meta` tag at the model level:
Copy
Ask AI
```
models:
name: users
    meta:
      joins:
join: segment_web_sessions
          sql_on: ${segment_web_sessions.user_id} = ${users.user_id}
    columns:

```

Once you’ve added a join, you can refresh Lightdash to see your changes in action. The dimensions and metrics of the joined model are included in the list on the left, right below the original model:
##  Next steps
  * Read more about customising joins in the joins reference


How to create metricsMultiple tables from one dbt model
Assistant
Responses are generated using AI and may contain mistakes.


