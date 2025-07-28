# Advanced deploy mode  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/advanced-deploy-mode

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling advanced deploy mode
  * Version control with advanced deploy mode
  * Deployment manager
    * Deploying a commit from the deployment manager
  * Deploying with webhooks
  * Deploying with the API




Was this helpful?
Send feedback 
#  Advanced deploy mode
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling advanced deploy mode
  * Version control with advanced deploy mode
  * Deployment manager
    * Deploying a commit from the deployment manager
  * Deploying with webhooks
  * Deploying with the API


With the default Looker Git integration, Looker developers commit their changes to their development branch, then merge their development branch into the production branch. Then, when you deploy to the Looker environment, Looker uses the latest commit on the production branch. (See the Using version control and deploying documentation page for the default Git workflow and other options for advanced Git implementations.)
For advanced Git implementations where you don't want the latest commit on your production branch to be used for your Looker environment, a Looker admin can enable advanced deploy mode. When enabled, advanced deploy mode lets a developer with `deploy` permission specify a different commit SHA or tag to deploy to your Looker production environment, instead of using the latest commit on the production branch. If you want to deploy a commit from a different branch, you can use the advanced deploy mode webhook or API endpoint.
Advanced deploy mode helps consolidate repositories in multi-environment developer workflows, where each environment points to a different version of a codebase. It also gives one or several developers or administrators greater control over the changes that are deployed to production.
When advanced deploy mode is enabled, Looker does not prompt developers to deploy their changes to production. Instead, Looker prompts developers to merge their changes into the production branch. From there, changes can be deployed only in the following ways:
  * Using the deployment manager
  * Triggering a webhook
  * Using an API endpoint


## Enabling advanced deploy mode
To enable advanced deploy mode:
  1. In the Looker IDE, navigate to the **Project Configuration** page by selecting the **Settings** icon from the icon menu and then selecting the **Configuration** tab.
  2. On the **Project Configuration** page, select the checkbox next to **Enable Advanced Deploy Mode** under the **Deployment** section.
  3. Select the **Save Project Configuration** button to save your change.


## Version control with advanced deploy mode
When advanced deploy mode is enabled, deploying to production from Looker is no longer an option for developers. Instead, when the developer makes a commit, the **Git button** will prompt them to merge their changes to the primary branch instead of prompting them to deploy to production.
Changes are deployed to production using a webhook, the API, or the deployment manager.
## Deployment manager
For projects with advanced deploy mode enabled, Looker developers who have the `deploy` permission can use the deployment manager to deploy a commit or tag to their Looker production environment.
You can access the deployment manager by selecting the **Deploy** icon from the icon menu.
The deployment manager shows all the commits and tags that were previously deployed using advanced deploy mode.
If you have not yet used advanced deploy mode to deploy a commit, click the **Select Commit** button to see the commit history with the commits that your Looker developers have merged to the production branch.
For projects that have used advanced deploy mode to deploy a commit, the commit history will also show a commit's associated tags, if any, and will indicate which commit is the current version being used for production.
If the production branch has more recent commits than the deployed commit, the deployment manager displays this information and shows the most recent commit that your Looker developers have merged to the production branch.
### Deploying a commit from the deployment manager
There are several ways to deploy a commit from the deployment manager:
  1. To deploy a commit that has not yet been deployed, click the **Select Commit** button to select from all the commits that have been merged to the remote production branch. (If you want to deploy a commit from a different branch, use the advanced deploy mode webhook or API endpoint.)
  2. To deploy the most recently merged commit on the remote production branch, click the **Deploy Latest** button.
  3. To deploy a commit or tag that has been deployed previously, click its three-dot **Options** menu more_vert from the deployment manager and then **Deploy to Production**.


If you choose a commit that has not been deployed previously, the deployment manager will display the **Deploy Commit** menu. To deploy a commit from the **Deploy Commit** menu, follow these steps:
  1. To deploy the commit without assigning it a tag, select **Deploy without tagging** and select **Deploy to Environment**. Otherwise, keep the **Tag and deploy** option selected.
  2. Specify a tag for the commit. A Git tag marks the significance of the commit in the repository's history, such as a release number or version name. Note the following about Git tags:
     * Git tags must be unique within the Git repository. You cannot use the same tag for two different commits in your repository.
     * Git tags cannot contain spaces or certain special characters. See the Git reference documentation for the rules for naming references in Git.
  3. Optionally, you can add a description for the tag to give further details about the commit.
  4. Select **Deploy to Environment** to deploy the commit to the production version of your Looker instance.


Once you a deploy a commit, the deployment manager will mark the commit as the current version on your Looker production environment.
## Deploying with webhooks
For projects with advanced deploy mode, you can use the deploy webhook to deploy changes to production.
To set up the deploy webhook, you must first add a webhook secret for your Looker project from the **Project Configuration** page. Adding a webhook secret ensures that only authorized parties can trigger the deploy webhook.
Two webhooks are available for deploying changes to production with advanced deploy mode enabled. One webhook is for deploying the head of a branch, and the other is for deploying a specific Git SHA or tag.
The webhook to deploy the head of a branch uses this format:
```
<Looker URL>/webhooks/projects/<LookML project name>/deploy/branch/<Git branch name>

```

The webhook to deploy a commit SHA or tag uses this format:
```
<Looker URL>/webhooks/projects/<LookML project name>/deploy/ref/<commit SHA or tag>

```

Replace the information in the angle brackets `< >` with the information specific to your instance address, LookML project, and branch name or commit SHA/tag. Here is an example webhook to deploy the `v1.0` tag name for the `e_faa` project on the `docsexamples.dev.looker.com` Looker instance:
```
https://docsexamples.dev.looker.com/webhooks/projects/e_faa/deploy/ref/v1.0

```

## Deploying with the API
For projects with advanced deploy mode, you can use the Looker API to deploy changes to production.
To deploy with the API, the API user making the call will need to have `deploy` permission. See the Looker API authentication and Getting started with the API documentation pages for more information about authenticating and using the Looker API.
To deploy with the API, use the `deploy_ref_to_production` endpoint. This endpoint can be called in several different ways. The following examples are for the HTTPS and SDK methods.
### HTTPS
To manually deploy by using the `deploy_ref_to_production` API endpoint, see the following examples, which use the HTTPS method. For more information and examples of manually calling the API by using CURL requests, see the How to Authenticate to the API GitHub readme, or use the API Explorer. You can install the API Explorer on your Looker instance from the Looker Marketplace.
Use the following examples in an HTTPS request to deploy either the head of a branch or a specific commit SHA or tag via the `deploy_ref_to_production` API endpoint:
**Deploy the head of a branch** : `<HOST_URL>/api/4.0/projects/<PROJECT_ID>/deploy_ref_to_production?branch=<BRANCH_NAME>`
**Deploy a commit SHA or tag** : `<HOST_URL>/api/4.0/projects/<PROJECT_ID>/deploy_ref_to_production?ref=<SHA_OR_TAG>`
### SDK
Alternatively, use one of Looker's SDKs instead of making manual requests to the API. SDKs handle the details of authentication, parameter and response serialization, and other concerns.
Deploying with the `deploy_ref_to_production` with the SDK method looks like the following:
**Deploy the head of a branch** : `deploy_ref_to_production(<PROJECT_ID>, {branch: <BRANCH_NAME>})`
**Deploy a commit SHA or tag** : `deploy_ref_to_production(<PROJECT_ID>, {ref: <SHA_OR_TAG>})`
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


