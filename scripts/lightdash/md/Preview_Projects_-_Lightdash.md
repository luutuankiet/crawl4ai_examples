# Preview Projects - Lightdash

**Source:** https://docs.lightdash.com/references/preview-projects

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Reference
Preview Projects
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
  * Creating a preview project
  * Lighdash CLI Tool (Local)
  * Lightdash App
  * Pull Requests (GitHub Actions)
  * Permissions are copied from the parent project
  * Only content a user has access to will be copied to the preview project
  * Project connection settings
  * Lightdash CLI Tool (Local)
  * Lightdash App
  * Pull Requests (GitHub Actions)
  * Content in preview projects
  * Promoting content from preview projects
  * Deleting a Preview Project
  * Lightdash CLI Tool (Local)
  * Lightdash App
  * Pull Requests (GitHub Actions)


Charts and dashboards are copied from your production project into your preview project so you can test your changes and make updates to existing content. Preview projects are commonly used to:
  * test changes in models, metrics and dimensions.
  * make changes to important content in production without any downtime by promoting the content you’ve changed in your preview project when it’s ready.


##  Creating a preview project
Only users who have developer permissions or above in a project can create preview projects.
###  Lighdash CLI Tool (Local)
You can use the Lightdash CLI tool to generate preview projects in Lightdash from your command line.
Copy
Ask AI
```
# This will create a preview and will wait until you press a key to delete the preview project
lightdash preview

```

or
Copy
Ask AI
```
# This will create a preview and exit, you will have to run lightdash stop-preview to delete it
lightdash start-preview

```

You can see more information about the lightdash preview CLI command here.
###  Lightdash App
You can create a preview project in the Lightdash web app by clicking on the Projects list, then clicking `+ Create Preview`. Preview projects created in the app are useful in two main scenarios:
  1. You only want to make changes to Charts and Dashboards (not YAML or dbt models).
  2. You want to preview changes by pulling code from a specific git branch.

**Making changes to important content in production** You can leave out the **branch** and **schema** fields and you’ll get a preview project with a copy of all your content. You can create or update charts and dashboards, then promote the content back to your main project when it’s ready. **Creating a preview project from a Github branch** By choosing a branch (and optionally setting a schema or environment variables) you can create a preview project that uses code from a different branch than your main project. This is perfect for previewing changes you made on a branch in dbt Cloud or quick edits where you don’t want to fire up the CLI.
Preview projects from GitHub branches are a great solution for team members who don’t have local development or the CLI set up.
Note: this only works with GitHub. It is currently not possible to create previews from GitLab branches in the Lightdash App UI.
###  Pull Requests (GitHub Actions)
You can automatically create preview projects in GitHub each time you open a pull request. This allows you to easily test out changes you’ve made to your dbt project, in Lightdash. Learn more about setting up a Lightdash preview project for pull requests using GitHub Actions here.
##  Permissions
###  Permissions are copied from the parent project
All permissions from the parent project are carried over to the preview project. For example:
  * Priyanka is a **project interactive viewer** and Irakli is a **developer** in a project called `Marketing Insights`.
  * Irakli creates a preview project of `Marketing Insights` called `Marketing Insights Preview`.
  * He creates a chart in `Marketing Insights Preview` and shares it with Priyanka.
  * Priyanka can open the chart because she was an interactive viewer in `Marketing Insights`, so her permissions were copied over to `Marketing Insights Preview`.


**Only users who are developers or admins can see preview projects in the project list.** However, users with access to a preview project can open links shared with them from the preview project.
###  Only content a user has access to will be copied to the preview project
For the user creating a project, only content they have access to will be copied over to the preview project. For example:
  * Irakli is a developer in the `Marketing Insights` project
  * Inside the project, there is a space called `Finance private space`.
  * Irakli doesn’t have access to `Finance private space`
  * Irakli creates a preview project of `Marketing Insights` called `Preview Marketing Insights`
  * The `Finance private space` will not be copied over to his preview project (because he doesn’t have access to it).


##  Project connection settings
The project connection settings cannot be changed in a preview project.
###  Lightdash CLI Tool (Local)
For preview projects created from the CLI, all project connection settings come from your **local** `profiles.yml` file. That means that we will use the same default connection settings that you’re using locally for development, unless you specify different options in your CLI commands. For example:
  * By default, `lightdash preview` will use the `profiles.yml` file located at `~/.dbt/profiles.yml`. If you want to use a different `profiles.yml` file, you can specify this using the option `lightdash preview --profiles-dir path/to/directory`.
  * `lightdash preview` will use whatever default target that is set in your `profiles.yml` file. The database connection settings (schema, project, dataset, etc.) from this target will be used as the database connection settings for your preview project. You can override the target used to create your preview project using the flag `lightdash preview --target my-target-name`


###  Lightdash App
For preview projects created in the Lightdash app, all project connection settings are copied directly from the project the preview is built from. For example:
  * I have a project called `Lightdash Analytics` and I create a preview of that project called `Preview Lightdash Analytics`
  * `Preview Lightdash Analytics` will have the same project connection settings (warehouse connection, dbt project connection, etc.) as `Lightdash Analytics`.

The project connection settings cannot be changed in a preview project.
###  Pull Requests (GitHub Actions)
For preview projects created from GitHub actions, the project connection settings come from the `profiles.yml` file that you’ve specified to use in your GitHub action. If you haven’t changed anything from our default GitHub action script, then the connection settings used for your preview project should be whatever you’ve specified in your DBT_PROFILES secret. You have three options for setting up project connections in your GitHub Actions:
  1. Set up a single project connection that’s used in every pull request. E.g. always use the `prod` target. You can follow the instructions here for your data warehouse
  2. If you’re using dbt Cloud, you can use the dbt Cloud schema to manage the connection used in the pull request.
  3. Create a project connection per developer in GitHub (similar to `dev` profiles in your dbt project) so the connection changes depending on who opened the pull request. This is useful if you use different development schemas for team members developing in dbt.


##  Content in preview projects
When you create a preview project, the content is copied from the production project. The content in a preview project does not get re-synced from the project it’s been created from. For example:
  * I have a project called `Lightdash Analytics` with a chart called `Revenue by source`
  * I create a preview of that project called `Preview Lightdash Analytics`
  * The `Preview Lightdash Analytics` project has the same chart called `Revenue by source`
  * I change the `Revenue by source` chart in `Lightdash Analytics` (i.e. in the production project)
  * The `Revenue by source` chart in `Preview Lightdash Analytics` is not updated. It is the same chart as when the preview project was first created.


###  Promoting content from preview projects
Promoting content allows you to sync charts and dashboards that you’ve created or updated in your preview project to your production project. This means you can use preview projects to make changes to important content in production without any downtime. Learn more about promoting content from preview projects here.
##  Deleting a Preview Project
Preview projects created using any method can be deleted in the Lightdash App. There are also other more automated ways of deleting preview projects created in the Lightdash CLI and in GitHub Actions explained below.
###  Lightdash CLI Tool (Local)
If you use the command `lightdash preview` to generate a preview project from your CLI, then hitting `Enter` from your CLI should delete the preview project. If you use the command `lightdash start-preview` to generate a preview project from your CLI, then running the command `lightdash stop-preview` should delete your preview project. For more details on the `lightdash preview` CLI command, check out the docs here.
###  Lightdash App
You can delete preview projects you’ve created in the app by navigating to the `project settings`, then clicking on `all projects` in the sidebar under the `organization settings` header. You’ll see a list of all of the projects in your organization. You can switch to the `preview projects` tab to filter to a list of preview projects in your organization. If you have **developer** access, you can only delete preview projects that you created. If you are an **organization admin** , you can delete any preview project in the organization.
###  Pull Requests (GitHub Actions)
If you’ve added both the start-preview and stop-preview workflows in GitHub, then the preview environments you’ve created in your pull requests should automatically be deleted when the pull request gets merged.
Assistant
Responses are generated using AI and may contain mistakes.


