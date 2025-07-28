# Enable and disable Gemini in Looker for Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/enable-and-disable-gemini-in-looker-for-looker-studio

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * What is Gemini in Looker?
  * Before you begin
  * Gemini in Looker settings management
  * Enable and disable Gemini in Looker
  * Permissions to use Gemini in Looker features
  * Provide feedback
  * Related resources




Was this helpful?
Send feedback 
#  Enable and disable Gemini in Looker for Looker Studio
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * What is Gemini in Looker?
  * Before you begin
  * Gemini in Looker settings management
  * Enable and disable Gemini in Looker
  * Permissions to use Gemini in Looker features
  * Provide feedback
  * Related resources


This documentation page describes the settings that are available to manage Gemini in Looker as part of a Looker Studio Pro subscription. It covers the following topics:
  * The enablement options that are available for Looker Studio
  * How to enable and disable Gemini in Looker
  * The permissions that are required to use Gemini in Looker features


## What is Gemini in Looker?
Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data. Gemini in Looker can provide assistance for tasks in Looker (original) instances, in Looker (Google Cloud core) instances, and in Looker Studio.
Learn how and when Gemini for Google Cloud uses your data.
For more information about the types of tasks that Gemini in Looker can assist with, see the Gemini in Looker overview documentation page.
## Before you begin
Before Gemini in Looker can be enabled in Looker Studio, the following requirements must be met:
  * Your organization must have a Looker Studio Pro subscription
  * To view and modify Gemini in Looker settings in Looker Studio:
    * For a standard self-service subscription, you must be assigned a role that contains the `lookerstudio.pro.manage` IAM permission for the Google Cloud project that you use for your Looker Studio Pro subscription. The `lookerstudio.pro.manage` permission is included in the Owner (`roles/owner`) IAM role and the Looker Studio Pro Manager (`roles/lookerstudio.proManager`) IAM role. You may also be able to get this permission with custom roles or other predefined roles.
    * For a "whole organization, monthly active user (MAU)" subscription, you must be assigned a role that contains the `Manage Looker Studio Settings` Workspace privilege, which is included in the Workspace Services Admin and the Workspace Super Admin roles. You may also be able to get this privilege with a custom admin role.


For more information about Looker Studio Pro subscription types, see the Looker Studio Pro subscription overview.
## Gemini in Looker settings management
You can manage Gemini in Looker settings on the **Gemini in Looker** page in the Looker Studio user settings. Although you're managing these settings for a Google Cloud project, the settings that you configure here will actually apply to the users under the Looker Studio Pro subscription that is associated with the project.
To access the **Gemini in Looker** page, click settings**User settings** and select the **Gemini settings** tab.
From the **Gemini in Looker** page, you can view and manage the following Gemini in Looker settings:
  * **Enabled** : When this setting is enabled, Gemini in Looker features are available for the users of the Looker Studio Pro subscription that is associated with the Google Cloud project that you are managing.
  * **Trusted Tester features** : When this setting is enabled, users of the selected Looker Studio Pro subscription can access the Trusted Tester capabilities of Gemini in Looker. **This setting must be enabled to allow users to access Gemini during the pre-GA preview.**
  * **Enable Trusted Tester Data Use** : When this setting is enabled, you consent to your data being used by Google as described in the Gemini for Google Cloud Trusted Tester Program terms. This setting is optional.
  * **Code Interpreter** : When this setting is enabled, Looker Studio Pro users can use the Code Interpreter in Conversational Analytics. This setting can be enabled only when Gemini in Looker is enabled. The setting is disabled by default when the **Trusted Tester features** setting is disabled. This setting is enabled by default when both Gemini in Looker is enabled and the **Trusted Tester features** setting is enabled.


## Enable and disable Gemini in Looker
To enable Gemini in Looker for users under a Looker Studio Pro subscription, follow these steps for the Google Cloud that is associated with that subscription:
  1. Sign in to Looker Studio.
  2. Click settings**User settings** , and select the **Gemini settings** tab to open the **Gemini in Looker** page.
  3. On the **Gemini in Looker** page, turn on the **Enabled** setting for a selected project. When this setting is enabled, you can also choose to enable the **Trusted Tester features** setting, which enables the **Trusted Tester data use** and the **Code Interpreter** settings automatically. You can disable the **Trusted Tester data use** and the **Code Interpreter** settings manually if needed.


To disable Gemini in Looker and revoke access to Gemini in Looker features for all users under a Looker Studio Pro subscription, follow these steps for the Google Cloud that is associated with that subscription:
  1. Sign in to Looker Studio.
  2. Click the settings**User settings** icon and select the **Gemini settings** tab.
  3. On the **Gemini in Looker** page, turn off the **Enabled** setting for a selected project. If you turn off the **Enabled** setting, then the **Trusted Tester features** , **Trusted Tester data use** , and **Code Interpreter** settings, if enabled, are disabled automatically.


## Permissions to use Gemini in Looker features
Some Gemini in Looker features require additional permissions depending on the task that Gemini is assisting with.
To create calculated fields with Gemini assistance, you must be an editor of the report.
To generate Google Slides presentations from your Looker Studio reports, you must be a viewer or an editor of the Looker Studio report that you want to generate Google Slides from. You must also be an editor of the Google Slides presentation that you want to import content into.
To query data or create a data agent with Conversational Analytics, you must be assigned a Looker role that contains the `access_data` permission for the model that you are querying.
## Provide feedback
You can provide feedback about each Gemini in Looker feature. Instructions for how to submit feedback are included in the documentation for each feature.
## Related resources
  * Gemini in Looker
  * Gemini for Google Cloud overview


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


