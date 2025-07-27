# Autogenerate Lightdash-ready .yml files for your models - Lightdash

**Source:** https://docs.lightdash.com/guides/cli/how-to-auto-generate-schema-files

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
CLI quickstart
Autogenerate Lightdash-ready .yml files for your models
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
    * How to install the Lightdash CLI
    * Authenticating your CLI (login)
    * Upgrading your Lightdash CLI
    * Autogenerate Lightdash-ready .yml files for your models
    * Sync your changes with Lightdash deploy
    * Test your changes with Lightdash compile
  * Guides
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
  * Auto-generate schema.yml files
  * Auto-sync schema.yml files after dbt run
  * Generating schema.yml for multiple models
  * Using doc blocks to build better .yml files
  * The Lightdash CLI will automatically add doc blocks to your .yml files


If your dbt model has been defined in a .yml file, it will appear in Lightdash as a Table.
Not too sure what a .yml file or a Table is? Be sure to check out our tutorial on Adding Tables to Lightdash for more details.
##  Auto-generate `schema.yml` files
To make it faster to write and maintain your `schema.yml` files, the Lightdash CLI will automatically generate and sync your `schema.yml` files. Inside your dbt project, open a terminal and run this command to generate the `schema.yml` file for a model called`mymodel`:
Copy
Ask AI
```
git commit # make sure to commit all your existing project first!
lightdash generate -s mymodel

```

This will create or update an existing `schema.yml` file to add any new columns that have appeared in the database.
##  Auto-sync `schema.yml` files after `dbt run`
Since the `generate` command relies on your database schema to detect which columns are required, you’ll often want to run `dbt run` before running `generate`. You can combine `dbt run` and `lighdash generate` into one command which will run models and then regenerate the`schema.yml` files for any models than changed:
Copy
Ask AI
```
git commit
lightdash dbt run  # Run dbt AND re-sync schema.yml files

```

##  Generating `schema.yml` for multiple models
`lightdash generate` supports dbt model selection syntax to generate files for a group of models:
Copy
Ask AI
```
lightdash generate # all models
lightdash generate -s payments  # just payments
lightdash generate -s payments+ # payments and all children
lightdash generate -s +payments # payments and all parents
lightdash generate -s +payments+ # payments and all children and parents
lightdash generate -s tag:prod # all models with the prod tag
lightdash generate -s payments customers # two specific models
lightdash generate -s payments+ +customers tag:prod # mix and match

```

##  Using doc blocks to build better .yml files
Doc blocks are markdown files defined in your dbt project that are useful for creating consistent documentation in your dbt project. For example, if I have a field called `product_category` that’s used a bunch of times throughout my project, I can create a doc block for this field:
Copy
Ask AI
```
{% docs product_category %}
This is a string field that tells us the category of the product that was sold. This is a higher level grouping than the `product_type`. Every `product_type` maps to a single `product_category`.
The valid product categories are:
- clothing
- home
- accessories
- beauty
{% enddocs %}

```

I can then reference this doc block in my .yml files like so:
Copy
Ask AI
```
models:
name: products
    description: 'one row per product ID'
    columns:
name: product_category
        description: '{{ doc("product_category") }}'

```

The docs for `product_category` (in Lightdash and in your dbt documentation) will become the doc block I’ve written above.
###  The Lightdash CLI will automatically add doc blocks to your .yml files
The nice thing about doc blocks is that Lightdash automatically adds these to the .yml files it generates. For example, if I had a .yml file for my `product_sales` model that looked like this:
Copy
Ask AI
```
models:
name: product_sales
    columns:
name: product_id
name: product_value
name: product_category

```

Then, I did:
Copy
Ask AI
```
lightdash dbt run -s product_sales # or lightdash generate -s product_sales

```

Then my `product_sales.yml` file would be updated to include the doc block for `product_category`:
Copy
Ask AI
```
models:
name: product_sales
    columns:
name: product_id
name: product_value
name: product_category
        description: '{{ doc("product_category") }}'

```

We recommend using doc blocks whenever you can! They help with keeping the definitions of fields across your project consistent, and they also allow you to get great docs, completely automatically with the Lightdash CLI.
Upgrading your Lightdash CLILightdash Preview
Assistant
Responses are generated using AI and may contain mistakes.


