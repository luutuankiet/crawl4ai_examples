# Link a Looker Studio Pro monthly active user subscription to a Google Cloud project

**Source:** https://cloud.google.com/looker/docs/studio/link-looker-studio-pro-to-a-google-cloud-project-mau-version

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Use Looker Studio Pro in your organization
    * Link to a Google Cloud project
    * Optional: Add principals to the project
  * Best practices
    * Create a separate Google Cloud project for your Looker Studio Pro assets
    * Limit the number of principals on the project
    * Follow the principle of least privilege
  * Organization changes
  * Limits of Google Cloud project linking




Was this helpful?
Send feedback 
#  Link a Looker Studio Pro monthly active user subscription to a Google Cloud project
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Use Looker Studio Pro in your organization
    * Link to a Google Cloud project
    * Optional: Add principals to the project
  * Best practices
    * Create a separate Google Cloud project for your Looker Studio Pro assets
    * Limit the number of principals on the project
    * Follow the principle of least privilege
  * Organization changes
  * Limits of Google Cloud project linking


In Looker Studio, individual users own the assets (reports, data sources, and explorations) that they create or that have been transferred to them. To keep Looker Studio assets working after their owner leaves an organization, an administrator must transfer those assets to another user. Otherwise, those assets will likely be deleted and the departing user's data credentials will be revoked, breaking that user's reports and data sources.
Looker Studio Pro assets, on the other hand, are organized hierarchically, with your Cloud Identity or Google Workspace organization as the ultimate owner. Organizational ownership ensures that your Looker Studio assets continue to work even if their individual owner leaves the organization.
Specifically, organizational ownership offers the following benefits:
  * All the Looker Studio assets that your users create are stored in a Google Cloud project that you control and manage.
  * Looker Studio Pro assets are protected from deletion should their creator leave your organization.
  * You can use IAM to assign project-level permissions that apply to all Looker Studio Pro assets in your organization.
  * Looker Studio Pro assets are available to other Cloud services (for example, lineage in Dataplex).


## Use Looker Studio Pro in your organization
To use Looker Studio Pro in your organization, you'll need to link Looker Studio Pro to a Google Cloud project. Optionally, you can add principals on the project to manage Looker Studio assets.
### Link to a Google Cloud project
To complete this step, you'll provide a Google Cloud project which you'll use to manage Looker Studio assets. This project will also be used to bill your organization for your Looker Studio Pro subscription.
#### Cloud project requirements
  * The project that you choose must use the same billing account that your organization uses for your Looker Studio subscription.
  * When you set up organizational ownership of Looker Studio Pro assets, Google Cloud automatically creates a lien on the project to prevent accidental deletion of those assets. Be sure you have the `resourcemanager.projects.updateLiens` permission, which is granted by the `roles/owner` and `roles/resourcemanager.lienModifier` roles, so that Google Cloud can create the lien for you.
  * The user who performs the upgrade to Looker Studio Pro must must have the Workspace Services Admin role, or a another role that grants them the `Manage Looker Studio Settings` privilege in the organization that owns the project.
  * The user who performs the upgrade to Looker Studio Pro must also have the **owner** role for the project.


**For resellers** : The resold customers will need to provide a project that is linked to the billing account of the reseller subscription.
See the best practices section for additional tips before proceeding.
### Steps
  1. Sign in with an administrator account to the **Google Admin console**.
  2. In the Google Cloud console, go to **Billing** and then select My Projects.
  3. Locate the project that you want to use for Looker Studio asset management and billing and make a note of its project ID.
  4. Sign in to Looker Studio.
  5. In the left navigation, click **Enterprise Admin**.
  6. In the settings dialog that appears, on the left, click **Project ownership**.
  7. In the **Project ID** field, enter your Google Cloud project ID.


### Optional: Add principals to the project
Individual Looker Studio users DO NOT need to be added to the project. However, if you want to allow others in your organization to manage the Looker Studio project, you can add principals to that project using the IAM resource manager in the Google Cloud console. See the best practices section for advice.
You can grant principals the following IAM roles:
Role  |  Description   
---|---  
Data Studio Admin  ( ` roles/datastudio.admin ` )  |  Includes all permissions to reports and data sources.   
Data Studio Asset Viewer  ( ` roles/datastudio.viewer ` )  |  Includes view permissions to reports and data sources.   
Data Studio Asset Editor  ( ` roles/datastudio.editor ` )  |  Includes edit permissions to reports and data sources. Does not include delete permissions.   
Keep the following information in mind while granting roles to principals:
  * Currently, these roles use the Data Studio name.
  * Looker Studio does not support custom roles.
  * To see the individual IAM permissions that each role includes, see the IAM permissions reference.


## Best practices
We recommend the following best practices when you're setting up your Looker Studio Pro project:
### Create a separate Google Cloud project for your Looker Studio Pro assets
It's a good idea to create a dedicated project to manage Looker Studio Pro assets. Keeping this project separate from your other projects helps make it clear what the project is used for and helps prevent accidental deletion of your assets.
### Limit the number of principals on the project
Keep the number of people you add to the project to a minimum. Remember, access to the project is NOT a requirement to use Looker Studio. Instead, think about Looker Studio project access as a way to delegate administrative functions to a select few individuals.
### Follow the principle of least privilege
If you add people to the project, grant them the minimum role that is required to manage your Looker Studio assets according to your organization's policies.
Use the roles that are specific to Looker Studio. **Don't use IAM basic roles**. Basic roles include thousands of permissions across all Google Cloud services. In production environments, don't grant basic roles unless there is no alternative. Instead, grant the most limited predefined roles that meet your needs.
Learn more about how to use IAM securely.
## Organization changes
If you've linked Looker Studio Pro to a project in one organization and later want to transfer that project to a different organization, do the following:
  1. Sign in with an administrator account to the **Google Admin console**.
  2. Complete the setup of the new organization in Google Cloud console.
  3. Migrate the original project, users, and resources from the old organization to the new organization. Learn more about migrating projects.
  4. Sign in to Looker Studio.
  5. In the left navigation, click **Enterprise Admin**.
  6. In the settings dialog that appears, on the left, click **Project ownership**.
  7. In the **Project ID** field, enter your Google Cloud project ID.
  8. Click **Link project**.


For other transfer scenarios, please contact Cloud Customer Care for assistance.
## Limits of Google Cloud project linking
  * You can link Looker Studio to only one project.
  * Once Looker Studio is linked to your project, you can't link it to another project.
  * Because Looker Studio Pro projects have a Google Cloud lien placed on them, your assets are protected from accidental deletion. However, if you manually delete the project, **ALL** assets in that project are **permanently deleted**. Be careful!


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


