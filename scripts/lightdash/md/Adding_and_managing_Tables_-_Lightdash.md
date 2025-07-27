# Adding and managing Tables - Lightdash

**Source:** https://docs.lightdash.com/guides/adding-tables-to-lightdash

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
Adding and managing Tables
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
  * What are Tables?
  * Adding Tables to your Lightdash project using the CLI
  * Step 1. Install the Lightdash CLI
  * Step 2. Add Tables to Lightdash
  * Step 3. Preview your changes
  * Step 4. Deploy changes to production
  * Configuring which Tables appear in your Lightdash project
  * Changing your Table’s labels, adding joins, and more
  * Advanced tips for managing Tables
  * One model per YAML file
  * Limiting the Tables in Lightdash using dbt tags
  * Select the models you want to run using dbt selection syntax
  * Generate Tables and dimensions for your entire dbt project in one command


In Lightdash, everything you need for BI is written as code in your dbt project. You use dbt to transform all of the data from your data warehouse, then you use Lightdash to explore it. So, to add and manage Tables in Lightdash, we use dbt. We’ll walk you through the steps of installing + using the Lightdash CLI and generating the YAML you need to add a new table to your dbt project.
**New to dbt?** If you haven’t used dbt before, follow dbt’s getting started guide before proceeding with setting up Lightdash.
##  What are Tables?
Tables are the starting point to any data exploration in Lightdash - they’re the data in Lightdash that you can query. The beauty of Lightdash is that we’re pretty well synced with your dbt project. So, in Lightdash, Tables actually come from dbt models that have been defined in your dbt project’s YAML files. If your dbt model has been defined in a YAML file, it will appear in Lightdash as a Table.
Not sure what a YAML file is? Check out dbt’s docs about model properties to learn more about adding YAML files for your dbt models.
##  Adding Tables to your Lightdash project using the CLI
###  Step 1. Install the Lightdash CLI
The Lightdash CLI is the recommended way to develop your dbt + Lightdash project. It makes development faster and easier, as well as giving you options for building more powerful automation to manage your Lightdash instance. If you haven’t installed the Lightdash CLI yet, then follow this guide to installing and setting it up, then come back to these docs once you’re ready!
###  Step 2. Add Tables to Lightdash
You’ll do this using `lightdash dbt run -s my_model`.
Before you get started with the next steps, you might want to check out onto a new branch.
To get a model in dbt Lightdash-ready, we need to define all of the columns that we want to explore in Lightdash. We’ve made this really easy to do using our CLI tool and the command:
Copy
Ask AI
```
lightdash dbt run -s my_model

```

This will generate the Table and dimensions for the model you’ve selected. It will also document all of the columns in your new model in a `schema.yml` file. For example, if you just created a new `orders.sql` model and you run `lightdash dbt run -s orders`, an `orders.yml` file will be generated in your dbt project with all columns documented, like this:
Copy
Ask AI
```
models: 
name: orders
    columns:
name: basket_total
name: browser

```

###  Step 3. Preview your changes
You’ll be using the `lightdash preview` command for this step. Once you’ve generated your Tables and YAML files in dbt, you can test them out in a Lightdash preview environment. **Developer previews** are temporary Lightdash projects where you can safely experiment with your metrics, dimensions and charts without affecting your production project. So, let’s spin up a developer preview and check out our changes. In your terminal, run the commands:
Copy
Ask AI
```
lightdash preview

```

Following our example from Step 2, in Lightdash, you’ll see a Table called `Orders` and each column will appear as a dimension: You can read more about Lightdash preview environments here.
###  Step 4. Deploy changes to production
If you’re working with a version controlled project, make sure to **merge your changes into production**. If you’re working with a local project that isn’t version controlled, you don’t need to worry about syncing your changes. Once you’ve merged your changes, you’ll want to deploy them to production. To do this, run this command in your terminal from your dbt project:
Copy
Ask AI
```
lightdash deploy

```

This will deploy the changes in your dbt project to the Lightdash project you set up on your CLI tool earlier.
Lightdash’s deploy command will deploy using your **default dbt target** unless you specify to use a different target.For example, if you’ve set up a developer profile where it targets a dev dataset (like `dbt_khindson.my_model_names`), then you’ll need to pass the production target in your `lightdash deploy` command. Something like: `lightdash deploy --target prod`.
Now your Table is Lightdash-ready!
We don’t recommend using `lightdash deploy` from the CLI after initial project setup. It’s better to have an automated process like Github actions that push code changes in your dbt projet into Lightdash.
##  Configuring which Tables appear in your Lightdash project
Sometimes, there are models in our dbt project with YAML files that we might not want to appear in Lightdash (`staging` tables, I’m looking at you 👀). So, we’ve made it possible for you to configure which Tables you want to appear in Lightdash. To get to your table settings:
  1. Click the ⚙️ gear icon in the top-right navigation bar
  2. Choose **Project settings**
  3. Click on **Tables configuration** in the left sidebar (if you don’t see it you might not have access)

You have three options for configuring the Tables that show up in Lightdash:
  1. **Show entire project** : I hope this one isn’t too much of a surprise. If you select this option, it shows _all_ of the models with YAML files in your dbt project in Lightdash.
  2. **Show models with any of these tags** : This option depends on dbt tags. You can learn more about using tags to manage your project here. If you already have a specific model tag (or tags) you want to limit Lightdash to using, this is where you can add them in. For example, all of our production models have the tag `prod`, so we’ve configured our Tables using that tag.
  3. **Show models in this list** : If you’re not keen on using tags then you can manually select the models you want to include as Tables in your Lightdash project using this option.


##  Changing your Table’s labels, adding joins, and more
Once you’re happy with which Tables are showing up in Lightdash, you can add configurations to your Tables like:
  * Changing how the Table name appears in Lightdash (using the `labels` config)
  * Joining your Table to other Tables (using the `joins` config)

All of these configurations and more are outlined in the Tables reference doc here.
##  Advanced tips for managing Tables
###  One model per YAML file
We recommend structuring your dbt project with one .yml file per model (or .sql file). We’ve found that this makes it easier to navigate through your .yml files and easier to manage your dbt models, especially as your project becomes bigger. Here’s an example of our dbt project at Lightdash too see what that looks like in practice:
  * We have one `.sql` file per model (these are the files where all of our models’ business logic sits)
  * We have one `.yml` file per model (these are the files where all of your Tables’ configuration sits)

**But, in my dbt project, I have a single schema.yml file. Not one for each model. Will that still work?** Yep! We realize that schema files come in all shapes and sizes. Some people prefer to write the `schema.yml` details for all of their models in a single YAML file at the directory level, and that’s totally fine - it will still work with Lightdash. But, like we said just above, if you’re trying to decide how to setup your dbt project, **we’d recommend having one YAML file per model.**
###  Limiting the Tables in Lightdash using dbt tags
There may be a specific set of models that you want include as Tables in Lightdash. If this is the case, we recommend using dbt tags to tag models. You can use sets of existing tags, or you can create a new Lightdash-specific tag. You can add tags to your YAML file like this:
Copy
Ask AI
```
models:
name: model_name
    config:
      tags: ['prod']

```

Or, to your model’s SQL file in the config block:
Copy
Ask AI
```
{{ config(
    tags=["prod"]

select ...

```

Then, you’ll set your Table Configuration:
###  Select the models you want to run using dbt selection syntax
The `lightdash dbt run` command supports dbt model selection syntax to generate YAML files for a group of models. This means you can use tags or other model selection syntax to specify which models you want to generate dimensions for in your dbt project.
Copy
Ask AI
```
lightdash dbt run -s tag:lightdash # all models with the lightdash tag
lightdash dbt run -s payments  # just payments
lightdash dbt run -s payments+ # payments and all children
lightdash dbt run -s +payments # payments and all parents

```

###  Generate Tables and dimensions for your entire dbt project in one command
To do this, you just need to run the following on your command line:
Copy
Ask AI
```
lightdash dbt run

```

This command will run + generate tables for all of the models with YAML files. It will also generate dimensions for all of the columns in your dbt project.
Lightdash semantic layerHow to create dimensions
Assistant
Responses are generated using AI and may contain mistakes.


