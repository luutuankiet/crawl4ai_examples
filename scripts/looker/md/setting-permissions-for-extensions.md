# Setting permissions for Looker extensions  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/setting-permissions-for-extensions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Granting users permissions to extensions
    * Permissions to develop extensions
    * Permissions to install extensions from the Looker Marketplace
    * Permissions to use extensions
  * Example: Data Dictionary extension




Was this helpful?
Send feedback 
#  Setting permissions for Looker extensions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Granting users permissions to extensions
    * Permissions to develop extensions
    * Permissions to install extensions from the Looker Marketplace
    * Permissions to use extensions
  * Example: Data Dictionary extension


Extensions are web applications built with Looker components that are developed through the Looker extension framework. These extensions will inherit the permissions structure of your Looker instance, handling permissions at the model set level. If a user does not have permissions to access certain models in the standard Looker application, they won't be able to access those models in Looker extensions. This page explains how Looker admins can grant users the appropriate permissions to access Looker extensions.
The Looker Marketplace deploys an extension by importing a new project into your Looker application. This project contains everything required to run the extension and has at least one model file. Looker admins can control how a user views or interacts with content based on that model by assigning them a role that has permissions to access the extension's model.
For example, if your Looker instance has data based on models called `finance`, `marketing`, and `sales`, but you only want certain users to access the finance data, you would grant users access to only the `finance` model. Permissions for extensions work similarly.
> Looker admins can control permissions to access an extension's model (and therefore access the extension itself) as well as the model or models upon which any content _within_ the extension is based.
Looker admins can configure the available model sets for a Looker instance by navigating to the **Roles** page in the **Admin** panel. To access and use the extension, users must be assigned a role that has either `manage models` permissions or `explore` or `develop` permissions for all models or the model set that contains the extensions's model.
## Granting users permissions to extensions
Looker extensions are developed through the Looker extension framework and are available for installation through the Looker Marketplace. Extensions require that the **Extension Framework** and **Marketplace** features be enabled.
In addition to these features, there are three types of permissions associated with extensions:
  * Permissions to develop extensions
  * Permissions to install extensions from the Looker Marketplace
  * Permissions to use extensions


### Permissions to develop extensions
To develop an extension using the Looker extension framework, users need LookML developer permissions to the instance, as well as the skills recommended on the Introduction to the Looker extension framework documentation page.
### Permissions to install extensions from the Looker Marketplace
Each extension will have a project with at least one dedicated LookML model. For example, the Data Dictionary extension uses the `data-dictionary` model.
To install an extension from the Looker Marketplace, a user must have `develop`, `manage_models`, and `deploy` permissions for the extension's model.
When installing an extension that requires an access key from the Looker Marketplace, a configuration screen prompts the user for access key values, which will be stored as user attributes for the Looker instance.
### Permissions to use extensions
If the extension is installed through the Looker Marketplace or made available from within a Looker instance, the Looker admin will need to configure user permissions.
For most extension use cases, the extension always runs with the permissions granted to the user when they log in. By default, once the extension is installed, any user with a role that has `explore` or `develop` permissions and **Model Set** access set to **All** will automatically have the ability to view and use the extension _and_ its content with no additional permission configuration required. Users must have access to all the models that the extension uses for the extension to function fully.
Looker displays the extension in the **Applications** section of the Looker main menu.
> Looker only displays the extension for Looker users who have access to at least one of the extension's underlying models.
For embedded extensions, the extension takes on the permissions given to the created embed user ID, just like an embedded Look, dashboard, or Explore.
For full screen extensions that use the `/spartan` option in the extension URL, you can add users to an **Extensions Only** user group. Users in this group are prevented from viewing Looker pages outside of the extension. Looker admins can customize the **Extensions Only** group like any other group and assign it a role that has certain permissions and model set access. Users are not required to belong to the **Extensions Only** group to view a full screen extension; if a user is not in that user group, the extension will run with the permissions of that logged-in user.
#### Adding user permissions
A Looker admin will need to grant users and embed users a permission set that includes `access_data` and any more restrictive permissions associated with that extension. These permissions must be applied to a model set that includes the extension's model or models.
To grant users access to the extension, Looker admins must:
  1. Create a model set that includes the extension's model — or edit an existing model set to add the extension's model.
  2. Confirm that users are assigned to a role with at least the `access_data` permission (and any more restrictive permissions associated with that extension) for this model set.


## Example: Data Dictionary extension
The Data Dictionary extension project uses the `data-dictionary` model.
Users whose roles don't include `explore` or `develop` permissions or that have **Model Set** access _not_ set to **All** will need a Looker admin to grant them `explore` or `develop` permissions for a model set that includes the `data-dictionary` model.
For example, say that you want to give your finance team access to the Data Dictionary extension. The finance team is assigned the `Finance Team` model set, but it does not currently grant access to the `data-dictionary` model:
To add the `data-dictionary` model to their model set, select the **Edit** button next to the `Finance Team` model set and check the `data-dictionary` model checkbox.
Select **Update Settings** to save your selection.
After adding the `data-dictionary` model to the `Finance Team` model set, confirm that the finance team's role uses a permission set that contains `explore` or `develop` permissions. In this example, the finance team's role (**Finance Department**) contains the `Developer` permission set, along with the `Finance Team` model set.
The `Developer` permission set contains both the `explore` and the `develop` permissions.
Now, any users assigned to the **Finance Department** role will have access to the Data Dictionary extension because that role contains the appropriate permissions and the appropriate model access.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


