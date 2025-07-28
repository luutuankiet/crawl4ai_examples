# Configuring project version control settings  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/git-options

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Project settings
    * Import Credentials
    * Branch Management
  * Git integration options
  * Integrating external links to your Git provider
  * Integrating pull requests for your project
    * Setting up your project with integrated pull requests
    * Adding a webhook to your Git provider
    * Using a deploy webhook to pull from a remote Git repository
    * Merge options in the Git provider's interface




Was this helpful?
Send feedback 
#  Configuring project version control settings
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Project settings
    * Import Credentials
    * Branch Management
  * Git integration options
  * Integrating external links to your Git provider
  * Integrating pull requests for your project
    * Setting up your project with integrated pull requests
    * Adding a webhook to your Git provider
    * Using a deploy webhook to pull from a remote Git repository
    * Merge options in the Git provider's interface


This page describes how to configure elements of your project to integrate with Git for version control.
## Project settings
To see your project settings, open your project, then select the **Settings** icon from the Looker IDE icon menu.
From here you can access three **Project Settings** tabs:
  * Configuration
  * Import Credentials
  * Branch Management


### Configuration
The **Configuration** tab of the **Projects Settings** page opens the **Project Configuration** page. On the **Project Configuration** page, you can configure the following settings:
  * **Name** : The name of your project. You can rename your project by editing the text and clicking the **Save Project Configuration** button. See the Accessing and editing project information documentation page for more details.
  * **Git Production Branch Name** : Specify the Git branch name to use as the merge target for development branches for your project. The Git branch must exist in your Git repository. See the Git production branch name section on this page for more information.
  * **Code Quality** : Determines whether to require developers to successfully run the LookML Validator on the project before committing any changes to the project. **Code Quality** has the following options:
    * **Require fixing errors and warnings before committing** : Looker developers can commit changes only after successfully running the LookML Validator and resolving all errors and warnings. This is the recommended setting.
    * **Only require fixing errors before committing** : Looker developers can commit changes only after successfully running the LookML Validator and resolving all errors. Developers can commit changes when warnings exist. While not recommended, this option can be useful, for example, if new warnings are introduced to working LookML after a Looker update.
    * **Allow committing broken code** : Looker developers can commit changes without running the LookML Validator and regardless of whether errors or warnings exist in the LookML. This option is not recommended as it can result in LookML that doesn't function or that produces erroneous results.


  * **Require data tests to pass before deploying this project to production** : If the LookML project has one or more `test` parameters, this option requires developers to run the data tests before deploying any changes. If the data tests pass, the IDE will allow the developer to deploy changes to production. See the `test` parameter documentation page for information on setting up data tests in your LookML project. See the Using version control and deploying documentation page for information on running data tests on your project. By default, the **Require data tests to pass before deploying this project to production** option is enabled for new LookML projects.
  * **Git Integration** : Specifies the levels of integration with your Git provider. See Git integration options for details.
  * **Enable Advanced Deploy Mode** : A setting that, when enabled, lets users deploy any SHA, tag, or branch to production. See the Advanced deploy mode documentation page for more information about using version control with **Advanced Deploy Mode** enabled.
  * **Webhook Deploy Secret** : Sets up authentication for deploying changes to production on your Looker instance. See the Configuring the webhook deploy secret documentation page for details.
  * **Reset Git Connection** : This button opens the **Configure Git** window, where you can update the connection settings for your Git repository.
> Resetting your Git connection will preserve Git history for the main branch. It will also preserve the history of each Looker developer's personal branch once they sync their dev mode. To preserve history for all branches, see the Migrating to a new Git repository Best Practices page.
  * **Delete Project** : This button deletes the project, removing all LookML from the project in all development and production environments across your Looker instance.
  * **Git Summary** : This section shows the project's Git configuration and the current user's Git branch information.


#### Git production branch name
With the default Looker Git integration, all Looker developers merge their changes into a main branch called `master`. You can use the **Git Production Branch Name** field to specify which branch from your Git repository that Looker should use as the target branch into which your Looker developers' branches are merged. (See the Using version control and deploying documentation page for the default Git workflow and other options for advanced Git implementations.)
For existing projects, consider doing the following before changing the Git production branch name:
  * Ask all developers on the Looker project to commit their changes and merge their branches to the existing production branch, and then pause their work until the Git production branch name is updated and saved in the Looker project configuration.
  * If your project uses integrated pull requests, finalize and merge any open pull requests, as appropriate.
  * Perform any necessary preparations on the Git provider side, such as creating a new branch in your repository, renaming the existing default Git branch, or whatever actions might be necessary to prepare the branch so that Looker can use it as a target branch for merging. At the least, you must verify that the branch you want to use is an existing branch in your Git repository.


To change the Git branch that your project uses as the merge target for development branches:
  1. Select the **Settings** icon from the Looker IDE icon menu to display the project settings. The **Configuration** tab will open by default.
  2. In the **Git Production Branch Name** field, enter the name of the Git branch you want to use as the production branch for your Looker project.
  3. Click the **Save Project Configuration** button to save your change.


### Import Credentials
The **Import Credentials** section is where you can manage authentication credentials for private remote repositories. See the Importing files from other projects  documentation page for details.
### Branch Management
On the **Branch Management** tab of the **Projects Settings** page, you can see all the Git branches associated with the project. See the Using version control and deploying documentation page for details.
## Git integration options
Once you set up your Git connection, Looker will use your Git provider for managing your LookML source files, as described on the Using version control and deploying documentation page.
If you are a Looker admin, you can configure additional options for Looker integration with Git using the **Git Integration** options on the **Configuration** tab of the project's settings panel:
  * **Off** : Looker won't display any external links to your Git provider's interface.
  * **Show Links** : Looker will provide external links to your Git provider's interface so that your developers can view the project in the Git provider's interface. Looker will also provide links for each project file so that your developers can view the file's history and Git blame information on your Git provider's interface. See the Integrating External Links to Your Git Provider section for information about the links.
  * **Pull Requests Recommended** : In addition to providing external links to your Git provider's interface, Looker will give developers the option to submit a pull request so that another developer can approve changes before adding them to the project. See the Integrating pull requests for your project section for information on setting this up.
  * **Pull Requests Required** : This is the same as **Pull Requests Recommended** , except that your LookML developers are required to open a pull request to submit changes to the project. See the Integrating pull requests for your project section for information on setting this up.


To save your Git integration settings, click **Save Project Configuration** under the **Deployment** section.
## Integrating external links to your Git provider
If you have enabled any of the extra Git integration options (**Show Links** , **Pull Requests Recommended** , or **Pull Requests Required**), Looker provides external links to your Git provider's interface. These external links open a new browser tab to your Git provider's site.
> To view these external links, your developers must have an account with your Git provider, and must have access to the project's Git repository.
In the three-dot **File Options** menu for each of your LookML files, Looker provides links to your Git provider's site to view the file, to view the Git blame information for the file, and to view the commit history for the file.
In the **Git Actions** panel, you can also use the **View Project on`<Git provider>`** option to open your project files on your Git provider's site.
## Integrating pull requests for your project
With the default Looker Git integration, Looker developers commit their changes to their development branch, then merge their development branch into the production branch. Then, when you deploy to the Looker environment, Looker uses the latest commit on the production branch. (See the Using version control and deploying documentation page for the default Git workflow and other options for advanced Git implementations.)
Instead of allowing Looker developers to merge their development branch into the Looker production branch, you can set up your project with either the **Pull Requests Recommended** or the **Pull Requests Required** option:
  * **Pull Requests Recommended** : After a developer commits changes to their development branch, the Git button in the Looker IDE prompts the developer to open a pull request to merge their development branch into the production branch. The developer can then open a pull request for other Looker developers to review and approve from the Git provider's web interface. Or the developer can instead use the **Deploy to Production** option from the Git Actions panel to skip creating a pull request and deploy their changes to production. (The **Deploy to Production** option is not available if the project is enabled with advanced deploy mode.)
  * **Pull Requests Required** : After a developer commits changes to their development branch, the Git button in the Looker IDE prompts the developer to open a pull request. The developer must open a pull request to merge their development branch into the production branch. Then, other Looker developers can review and approve the pull request from the Git provider's web interface.


Looker supports pull request integration for the following Git providers:
  * GitHub
  * GitLab
  * Bitbucket Cloud
  * Bitbucket Server (formerly "Stash")


Here are some additional notes on using pull requests with Looker:
  * To open pull requests, your developers must have an account with your Git provider and must have access to the project's Git repository.
  * If the IP Allowlist feature is enabled on your instance, to integrate pull requests with any LookML projects you will need to add to the allowlist the range of IP addresses from which your Git provider makes outbound requests. For example, current GitHub IP addresses are listed in the GitHub changelog. IPs are subject to change and will be different for other Git providers.
  * If you have enabled advanced deploy mode, it is not necessary to configure a webhook in the Setting Up Your Project with Integrated Pull Requests section, since advanced deploy mode separates the merge and deployment functions.
  * If a Looker developer has issued a pull request that you would like to revert, see the How to revert pull requests from Looker via GitHub Community post for more information.
  * Git pull requests can make it possible to use a staging instance for Looker, so you can have a staging instance and a production instance, with pull requests enabled on the staging instance. All development and code review can be done in the staging environment, and the reviewed code can then be deployed to the production instance. To set this up, see the Git Workflow Using One Repository Across Multiple Instances — Development, Staging, and Production Community post.
  * Looker merges changes from a Looker developer branch into the production branch using the _merge commit_ method of merging. When using your Git provider's interface, be sure your developers don't use _squash merging_ , nor _rebase merging_. See the Merge Options in the Git Provider's Interface section for more information.


### Setting up your project with integrated pull requests
To set up your Looker project with Git pull requests:
  1. From your project, select **Settings** from the Looker IDE icon menu.
  2. In the **Git Integration** section of the **Configuration** tab, select **Pull Requests Recommended** or **Pull Requests Required**.
  3. Optionally, if you want to set up an automatic deploy webhook on your Git provider's interface, copy the webhook information and paste it into a text file. If your project is configured to use advanced deploy mode, you can skip this step. You can also decide later and come back to the project settings to get the webhook information.
  4. Optionally, you can set up a webhook deploy secret to authenticate an automatic deploy webhook from your Git provider or an advanced deploy mode webhook. To create a webhook secret, click **Set Webhook Secret**. Copy the deploy secret and paste it into a text file to use when you add the webhook to your Git provider's interface. You can also decide later and come back to the project settings to add a deploy secret. See the Configuring the webhook deploy secret documentation page for more information.
  5. Click **Save Project Configuration**.


Now, whenever a Looker developer commits changes to your project, the Looker IDE will show the **Open Pull Request** button. The button opens a new browser tab directly to the new pull request page on your Git provider's website.
Once you have set up your Looker project to use pull requests, do one of the following to set up how commits are deployed to your production environment:
  * To automatically deploy the latest commits that are merged to your production branch, use your Git provider's interface to add a webhook, as described in the next section on this page.
  * To manually specify which branches or commits are deployed, enable advanced deploy mode. See the Advanced deploy mode documentation page for information on enabling and managing advanced deploy mode.


### Adding a webhook to your Git provider
For Looker projects enabled for pull requests, you can set up a deploy webhook on your Git provider's interface. This webhook will trigger Looker to deploy the latest commit from the production branch whenever you merge a pull request on the Git provider's interface.
> In most cases, you don't want to set up an automatic deployment webhook if your project is configured to use advanced deploy mode. Advanced deploy mode lets you select the commit and branch that you want to deploy, so in most cases setting up an automatic deploy webhook would nullify the features of advanced deploy mode.
To add an automatic deploy webhook on your Git provider's interface, first go to your project settings in Looker by clicking the **Settings** icon from the project's Looker IDE icon menu. Next, copy the webhook from the **Git Integration** section.
The webhook takes the form `<instance_url>/webhooks/projects/<project_name>/deploy`.
Replace the `<instance_url>` with the URL for your Looker instance. For example, if your Looker instance URL is `example.looker.com` and your project name is `e_faa`, then the webhook would look like this:
`https://example.looker.com/webhooks/projects/e_faa/deploy`
From the Looker project settings, you can also get a webhook deploy secret to authenticate your project's Git integrations with your Git provider. See the Configuring the webhook deploy secret documentation page for more information.
Once you have the webhook URL and the deploy webhook secret, you can enter them into your Git provider's interface. If your Git provider is GitHub, follow these steps:
  1. Navigate to your project's repository settings on your GitHub repository.
  2. In your repository's settings, click **Webhooks**. Click **Add Webhook** to open the **Add Webhook** window.
  3. In the **Payload URL** field, paste the webhook information you copied from the **Git Integration** section in Looker.
  4. Optionally, you can add a webhook deploy secret that authenticates your project's Git integrations with your Git provider. Copy the deploy secret from the project settings of your LookML project and paste the secret into the **Secret** field in the Git provider's interface. See the Configuring the webhook deploy secret documentation page for more information.
  5. Select the **Just the push event** option in the **Which events would you like to trigger this webhook?** field.
  6. Click **Add webhook**.


### Using a deploy webhook to pull from a remote Git repository
When pull requests are enabled for your LookML project — and deploy webhooks are not automated — you may occasionally find that the LookML you see in the Looker Production Mode doesn't match the LookML on the main branch of your Git repository. This can occur in the following situations:
  * When pull requests are enabled for the repository
  * When the LookML has been edited outside of the Looker development environment, such as: 
    * In the Git repository itself
    * On another Looker instance, such as a staging instance


You can sync the Looker production branch to the repository's main branch by using a deploy webhook:
  1. Open a new browser tab and type the following URL, replacing `<instance_url>` with your Looker instance URL, and `<project_name>` with the name of your LookML project:
```
<instance_url>/webhooks/projects/<project name>/deploy

```

  2. After you run the deploy webhook URL, a blank web page will display a success message similar to the following:
```
{"operations":[{"error":false,"error_code":0,"command":"Checkout Branch #\u003cLooker::GitBranch:0x5798672b\u003e","node_id":728,"results":["Success"]},{"error":false,"error_code":0,"command":"jgit revert_repo","node_id":728,"results":["Success"]}],"new_head":"05f772af48709fc2799fefe408e3fdd895a63284","old_head":"77412cad9fd7ed3eed1627afa201fdf7dcb97dd1"}

```



Now your Production Mode in Looker has been updated to reflect your remote Git main branch. Your personal developer branch and shared branches are unaffected.
#### Pulling from a remote Git repository for webhooks with deploy secrets
If your LookML project also requires a webhook deploy secret for pushing changes from your main branch to your production branch, you will receive one of the following errors when you sync the production branch with the repository's main branch using the method described in the preceding section, Using a deploy webhook to pull from a remote Git repository:
```
{"error":"Uh oh! Something went wrong."}

```

Or:
```
{"error":"Not found."}

```

Instead of using the deploy webhook, you can run the following cURL command in your terminal with the webhook secret. Make sure to replace the following fields:
  * Replace `<instance_URL>` with your Looker instance URL.
  * Replace `<deploy_secret>` with your project's deploy secret.
  * Replace`<project_name>` with the name of your LookML project.

```
curl -i -X POST -H "X-Looker-Deploy-Secret:<deploy_secret>" https://<instance_url>/webhooks/projects/<project_name>/deploy

```

For example, if you were to sync a production branch for the **ecommerce_project** on the **Brettcase** instance with the repository's main branch:
```
curl -i -X POST -H "X-Looker-Deploy-Secret:123123123secretgoeshere123123123" https://brettcase.looker.com/webhooks/projects/ecommerce_project/deploy

```

### Merge options in the Git provider's interface
If your Looker project is integrated with pull requests, your developers use your Git provider's interface to submit pull requests and merge changes into the production branch.
Looker supports the _merge commit_ method of merging changes from a development branch into your production branch. However, your Git provider's interface may show additional options for merging, such as **Squash and merge** or **Rebase and merge**.
Looker does not support _squash merging_ or _rebase merging_ , so your developers should avoid using these options. If possible, the best practice is to disable these options for your repository. To disable these options in a GitHub repository, follow these steps:
  1. Navigate to the **Settings** tab to access your project's repository settings on GitHub.
> **TIP** : For projects that are configured with Git integration, you can use the **View Project on Git** option from the project's Git menu in Looker.
  2. In your repository's settings, click **Options** from the navigation menu.
  3. Go to the **Merge button** section and leave checked only the **Allow merge commits** option. Disable the **Allow squash merging** and **Allow rebase merging** options.


Once you disable the merge options, they won't be available in GitHub when your developers merge a branch in the repository.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


