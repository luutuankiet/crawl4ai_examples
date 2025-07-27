# Lightdash Validate - Lightdash

**Source:** https://docs.lightdash.com/guides/cli/how-to-use-lightdash-validate

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
CLI quickstart
Lightdash Validate
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
  * Validate your changes against your project by running lightdash validate
  * Validate any project using the project UUID
  * Validate only specific elements of your project
  * Configure Github actions


You can trigger a validation on a project using the Lightdash CLI so you can check locally if your changes will break anything. You can also add `lightdash validate` to your GitHub Actions so changes can’t be merged unless they pass the validation.
##  Usage
###  Validate your changes against your project by running lightdash validate
You can run `lightdash validate` to check if your changes break any of the content in production. By default, `lightdash validate` will check your changes against the content in the project you’ve selected on the CLI. You can change your project using `lightdash config set-project`.
Copy
Ask AI
```
lightdash validate

```

Optionally you can use the `--preview` argument to validate your last preview environment created from the CLI. You will get a list of errors if your local files are going to break some content on your project. These errors will not be reflected on the validation table on Lightdash settings.
###  Validate any project using the project UUID
You can run a validation on any project by specifying the project UUID in the `lightdash validate` command.
Copy
Ask AI
```
lightdash validate --projectproject uuid

```

**Note:** you can get your project UUID from the Lightdash URL by selecting the ID after the `projects/`
###  Validate only specific elements of your project
You can select which parts of your project you would like to validate using the `--only` argument.
Copy
Ask AI
```
lightdash validate --only tables charts dashboards

```

Available options:
  * `tables`
  * `charts`
  * `dashboards`


##  Configure Github actions
This command will create a preview environment, and then validate this preview by specifying `--preview` on the validate command.`lightdash validate` will return an error (return code 1) if there is at least 1 validation error on your project. You can use this output to block a deploy on Github actions like this
Copy
Ask AI
```
- name: Start preview
  run: lightdash start-preview
- name: Validate preview
  run: lightdash validate --preview

```

To learn more about setting up GitHub actions for Lightdash, check out the docs here.
Test your changes with Lightdash compileLightdash semantic layer
Assistant
Responses are generated using AI and may contain mistakes.


