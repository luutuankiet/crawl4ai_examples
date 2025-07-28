# Administer Gemini on your Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-admin-gemini

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * What is Gemini in Looker?
    * Gemini in Looker feature availability
  * Before you begin
  * Enabling and disabling Gemini
    * Enabling and disabling the Code Interpreter for Looker (Google Cloud core)
  * Grant the Gemini in Looker permission to users
    * Granting the Gemini default role
    * Granting a custom role
    * Adding users to the Gemini Default Users group
    * Additional permissions
  * Provide feedback
  * Related resources




Was this helpful?
Send feedback 
#  Administer Gemini on your Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * What is Gemini in Looker?
    * Gemini in Looker feature availability
  * Before you begin
  * Enabling and disabling Gemini
    * Enabling and disabling the Code Interpreter for Looker (Google Cloud core)
  * Grant the Gemini in Looker permission to users
    * Granting the Gemini default role
    * Granting a custom role
    * Adding users to the Gemini Default Users group
    * Additional permissions
  * Provide feedback
  * Related resources


This documentation page describes how to administer Gemini in Looker for a Looker (Google Cloud core) instance. It covers the following topics:
  * Different configurations of Gemini in Looker features that are available in Looker (Google Cloud core), and the steps that are required to make them accessible to Looker users
  * How to enable and disable Gemini in Looker for a Looker (Google Cloud core) instance
  * How to enable and disable the Code Interpreter, for use with Conversational Analytics
  * The permissions that are required to use Gemini in Looker, and how to grant them


This page is intended for users who have the Looker Admin role for the Looker (Google Cloud core) instance and the Looker Admin (`roles/looker.admin`) role for the Google Cloud project in which the instance resides.
## What is Gemini in Looker?
Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data. Gemini in Looker can provide assistance for tasks in Looker (original) instances, in Looker (Google Cloud core) instances, and in Looker Studio.
Learn how and when Gemini for Google Cloud uses your data.
Gemini in Looker may not support the same compliance and security offerings as does Looker or your other data sources. Only enable Gemini in Looker if Gemini for Google Cloud's compliance offerings meet the needs of your organization.
Gemini in Looker features are enabled through the Google Cloud console and are available on a per-instance basis. Looker users are granted access to Gemini features within the Looker (Google Cloud core) instance. For more information about the types of tasks that Gemini in Looker can assist with, see the Gemini in Looker overview documentation page.
### Gemini in Looker feature availability
The availability of Gemini in Looker features is summarized in the following table. Depending on the needs of your organization, you can enable the settings that grant users access to the Gemini in Looker features that are available in the appropriate Looker platform.
Accessible Gemini in Looker features | Implementation  
---|---  
  * In Looker: Write LookML
  * In Looker: Create custom Looker visualizations
  * In Looker: Use Conversational Analytics
  * In Looker: Use the Code Interpreter with Conversational Analytics

| 
  1. Enable Gemini in Looker (Google Cloud core).
  2. Enable the Code Interpreter.
  3. Grant permissions to use Gemini in Looker.

  
  * In Looker: Write LookML
  * In Looker: Create custom Looker visualizations
  * In Looker and in Looker Studio:  Use Conversational Analytics
  * In Looker and in Looker Studio: Use the Code Interpreter with Conversational Analytics
  * In Looker Studio: Create calculated fields using natural language
  * In Looker Studio: Export data to Slides

| 
  1. Enable Gemini in Looker (in Looker).
  2. Accept Looker Studio Pro licenses.
  3. Enable Gemini in Looker and the Code Interpreter (in Looker Studio).
  4. Enable the Code Interpreter in Looker (Google Cloud core).
  5. Grant permissions to use Gemini in Looker.

  
## Before you begin
To get the permissions that you need to enable Gemini for a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project in which the instance resides. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
To perform the following tasks, you must be a Looker admin for the Looker (Google Cloud core) instance:
  * Enable the Code Interpreter for use with Conversational Analytics in the Looker (Google Cloud core) instance
  * Grant users permissions to use Gemini in Looker features


The Code Interpreter requires that the Looker (Google Cloud core) instance is on Looker 25.10 or later.
## Enabling and disabling Gemini
In the Google Cloud console, follow these steps to enable Gemini:
  1. On the **Instances** page, click the name of the instance for which you want to enable Gemini.
  2. Click **Edit**.
  3. Expand the **Gemini in Looker (Google Cloud core)** section.
  4. Select **Gemini**. When this setting is enabled, users can access the Gemini in Looker features that are available as described in the Gemini in Looker feature availability table.
  5. Select **Trusted Tester features**. When this setting is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. **This setting must be enabled in order for users to access Gemini during the pre-GA preview.**
  6. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the Gemini for Google Cloud Trusted Tester Program terms.


To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.
You must grant the `gemini_in_looker` permission to users before they can use Gemini in Looker features.
### Enabling and disabling the Code Interpreter for Looker (Google Cloud core)
In the Looker (Google Cloud core) instance, follow these steps to enable the Code Interpreter and make it available to Gemini in Looker users:
  1. Navigate to the **Admin** panel > **Platform** section > **Gemini in Looker** page.
  2. Enable **Code Interpreter**.


The Code Interpreter is disabled by default, even when **Gemini in Looker** is enabled in the Looker (Google Cloud core) instance settings in the Google Cloud console.
You must grant the `gemini_in_looker` permission to users before they can use the Code Interpreter.
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
Additional Looker permissions may be needed to perform the tasks that Gemini assists with. See the Additional permissions section on this page for a list of these permissions.
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


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


