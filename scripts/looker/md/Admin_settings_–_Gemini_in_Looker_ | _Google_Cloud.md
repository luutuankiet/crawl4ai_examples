# Admin settings – Gemini in Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-gil

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * What is Gemini in Looker?
    * Gemini in Looker feature availability
  * Before you begin
  * Enabling and disabling Gemini
  * Grant the Gemini in Looker permission to users
    * Granting the Gemini default role
    * Granting a custom role
    * Adding users to the Gemini Default Users group
    * Additional permissions
  * Provide feedback
  * Related resources




Send feedback 
#  Admin settings – Gemini in Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * What is Gemini in Looker?
    * Gemini in Looker feature availability
  * Before you begin
  * Enabling and disabling Gemini
  * Grant the Gemini in Looker permission to users
    * Granting the Gemini default role
    * Granting a custom role
    * Adding users to the Gemini Default Users group
    * Additional permissions
  * Provide feedback
  * Related resources


This documentation page describes how to administer Gemini in Looker for a Looker (original) instance. It covers the following topics:
  * Different configurations of Gemini in Looker features that are available in Looker (original)
  * How to enable and disable Gemini in Looker for a Looker (original) instance
  * The permissions that are required to use Gemini in Looker, and how to grant them


This page is intended for users who are assigned the Looker Admin role for the Looker (original) instance.
## What is Gemini in Looker?
Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data. Gemini in Looker can provide assistance for tasks in Looker (original) instances, in Looker (Google Cloud core) instances, and in Looker Studio.
Learn how and when Gemini for Google Cloud uses your data.
For more information about the types of tasks that Gemini in Looker can assist with, see the Gemini in Looker overview documentation page.
### Gemini in Looker feature availability
The availability of Gemini in Looker features is summarized in the following table. Depending on the needs of your organization, you can enable the settings that grant users access to the Gemini in Looker features that are available in the appropriate Looker platform.
Accessible Gemini in Looker features | Implementation  
---|---  
  * In Looker: Write LookML
  * In Looker: Create custom Looker visualizations
  * In Looker: Use Conversational Analytics

| 
  1. Enable Gemini in Looker.
  2. Grant permissions to use Gemini in Looker.

  
  * In Looker: Write LookML
  * In Looker: Create custom Looker visualizations
  * In Looker and in Looker Studio: Use Conversational Analytics
  * In Looker Studio: Create calculated fields using natural language
  * In Looker Studio: Export data to Slides

| 
  1. Enable Gemini in Looker (in Looker).
  2. Accept Looker Studio Pro licenses.
  3. Enable Gemini in Looker (in Looker Studio).
  4. Grant permissions to use Gemini in Looker.

  
## Before you begin
To enable or disable Gemini in Looker and to grant users permissions to use Gemini in Looker features, you must be assigned the Looker Admin role for the Looker (original) instance.
To support Gemini in Looker, the following requirements must be met:
  * The Looker instance must be on Looker 25.0 or higher
  * The Looker instance must be Looker-hosted


## Enabling and disabling Gemini
To enable Gemini in Looker, follow these steps:
  1. In the **Admin** panel, navigate to the **Platform** section and select the **Gemini in Looker** page.
  2. Under **Gemini in Looker enablement** , turn on the **Enable Gemini in Looker** setting. When this setting is enabled, users can access the Gemini in Looker features that are available as described in the Gemini in Looker feature availability table.
  3. Select **Enable Trusted Tester Features**. When this setting is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. **This setting must be enabled to allow users to access Gemini during the pre-GA preview.**
  4. Optionally, select **Enable Trusted Tester Data Use**. When this setting is enabled, you consent to your data being used by Google as described in the Gemini for Google Cloud Trusted Tester Program terms. This setting can be enabled only when the **Enable Trusted Tester Features** setting is enabled. This setting is enabled automatically when the **Enable Trusted Tester Features** setting is enabled.
  5. Optionally, select **Enable Code Interpreter**. When this setting is enabled, users can access the Code Interpreter in Conversational Analytics. This setting can be enabled only when the **Enable Trusted Tester Features** setting is also enabled. _The**Enable Code Interpreter** setting was enabled by default for Looker (original) instances that had the **Enable Gemini in Looker** and **Enable Trusted Tester Features** settings turned on prior to being updated to Looker 25.8 _and_ had been updated to Looker 25.8 on the first day of release deployments._


To disable Gemini for a Looker (original) instance, clear the **Enable Gemini in Looker** setting.
## Grant the Gemini in Looker permission to users
To grant Looker users the ability to use Gemini in Looker features in the Looker (Google Cloud core) instance, you must assign them a role that applies the `gemini_in_looker` permission to the appropriate models. You can do this in any of the following ways:
  * Grant them the **Gemini** default role
  * Grant them a custom role that contains the `gemini_in_looker` permission
  * Add them to the **Gemini Default Users** group


### Granting the **Gemini** default role
The `gemini_in_looker` permission is the only permission that is included in the **Gemini** default role, which by default applies to all models on the instance.
To update an individual user's settings to assign the default **Gemini** role, follow these steps:
  1. Navigate to the **Users** page in the **Users** section of the **Admin** panel.
  2. Select the user or group whose permissions you want to change.
  3. From the **Roles** drop-down menu, select **Gemini**.
  4. Select **Save** to retain these settings.


You can also assign the **Gemini** role to multiple users or groups from the **Roles** page in the **Users** section of the **Admin** panel by following these steps:
  1. Navigate to the **Roles** page in the **Users** section of the **Admin** panel.
  2. Next to the **Gemini** role, select **Edit**.
  3. Under **Groups** or **Users** , select the groups or users that you want to assign the **Gemini** role to.
  4. Click **Update Role** to retain these settings.


### Granting a custom role
To restrict users from accessing Gemini in Looker features for all models on the Looker instance, you can create a custom Looker role that applies the `gemini_in_looker` permission to specific models only, and assign it to the appropriate users. You may need to remove those users from the **Gemini Default Users** group, which is assigned the **Gemini** default role by default.
To assign a custom role, follow these steps:
  1. Navigate to the **Roles** page in the **Users** section of the **Admin** panel.
  2. Select **New Permission Set**.
  3. Provide a label for your new permission set in the **Name** field.
  4. Select the `gemini_in_looker` permission and click **New Permission Set**.
  5. Select **New Role**.
  6. Provide a label for your new role in the **Name** field.
  7. For **Permission Set** , select the permission set that you just created.
  8. For **Model Set** , select the specific models that you would like to apply the `gemini_in_looker` permission to. You may need to create a model set that contains the appropriate models before you can assign a model set to your new custom role.
  9. Under **Groups** or **Users** , select the groups or users that you want to assign the custom role to. You can also add users and groups to the role later by updating the role settings.
  10. Click **New Role** to save this custom role.


### Adding users to the **Gemini Default Users** group
The **Gemini Default Users** group has been created automatically for all Looker (original) instances that use an open system configuration. Users in this group are assigned the **Gemini** role, which grants them the ability to use Gemini in Looker features.
You can edit the **Gemini Default Users** group to add or remove users, or to delete the group entirely. You can also add additional roles to the group.
For more information about how users are added to this group, see the Groups documentation page.
### Additional permissions
The following Gemini in Looker features require additional permissions:
  * To create custom visualizations with Gemini assistance, you must be assigned a Looker role that contains the `can_override_vis_config` permission.
  * To write LookML with Gemini assistance, you must be assigned a Looker role that contains the `develop` permission for at least one model in a LookML project.
  * To query data or create a data agent with Conversational Analytics, you must be assigned a Looker role that contains the `access_data` permission for the model that you are querying.


## Provide feedback
You can provide feedback about each Gemini in Looker feature. Instructions for how to submit feedback are included in the documentation for each feature.
## Related resources
  * Learn more about Gemini for Google Cloud
  * Learn more about Gemini in Looker


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


