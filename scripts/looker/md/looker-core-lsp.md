# Accept complimentary Looker Studio Pro licenses for a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-lsp

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Accept Looker Studio Pro licenses
  * Select a Google Cloud project
  * Add users to your Looker Studio Pro subscription
    * Remove licenses or users
  * Transfer complimentary Looker Studio Pro licenses to a different subscription
  * Effects of canceling a Looker Studio Pro subscription
  * Troubleshooting complimentary licenses




Was this helpful?
Send feedback 
#  Accept complimentary Looker Studio Pro licenses for a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Accept Looker Studio Pro licenses
  * Select a Google Cloud project
  * Add users to your Looker Studio Pro subscription
    * Remove licenses or users
  * Transfer complimentary Looker Studio Pro licenses to a different subscription
  * Effects of canceling a Looker Studio Pro subscription
  * Troubleshooting complimentary licenses


Looker Studio Pro licenses are available at no cost to Looker users as part of a Looker Studio Pro subscription. To get started using Looker Studio Pro, you need to set up a Looker Studio Pro subscription, accept your Looker account's complimentary licenses, and assign the licenses to Looker users.
The number of complimentary Looker Studio Pro licenses that are allocated to your Looker account is determined by the number of Looker licenses that are included in your Looker agreement. For more information about the terms of this offer, see the Complimentary Looker Studio Pro licenses offer details documentation page.
This page describes how to perform the following tasks for a Looker instance:
  1. Accept the complimentary Looker Studio Pro licenses that have been allocated to your Looker instance
  2. Specify the Google Cloud project that hosts your Looker Studio Pro content
  3. Add Looker users to your Looker Studio Pro subscription


## Before you begin
If you don't already have a Looker Studio Pro subscription, we recommend that you set up the Google Cloud project for your Looker Studio content _before_ you accept your account's allotted complimentary licenses. For more information about Google Cloud project requirements and setting a new Looker Studio Pro subscription, see the Start a new Pro subscription documentation page.
Each user with a Looker Viewer (`roles/looker.viewer`) role who will use Looker Studio Pro must also be a Google Workspace or Cloud Identity user with a Managed Google account.
### Required roles
Different permissions are required to perform the following tasks:
  * Accept complimentary Looker Studio Pro licenses
  * Set up a self-service subscription to Looker Studio Pro


To get the permission that you need to accept complimentary Looker Studio Pro licenses and update Looker (Google Cloud core) instance information, ask your administrator to grant you an IAM role containing the `looker.instances.update` permission for the Google Cloud project that your Looker (Google Cloud core) instance resides in. The Looker Admin (`roles/looker.admin`) IAM role contains this permission by default, but you may be able to get this permission with custom roles or other predefined roles.
To get the permission that you need to set up a self-service subscription to Looker Studio Pro, ask your administrator to grant you an IAM role containing the `lookerstudio.pro.manage` permission for the Google Cloud project that your Looker (Google Cloud core) instance resides in. The Owner (`roles/owner`) IAM role and the Looker Studio Pro Manager (`roles/lookerstudio.proManager`) role contain this permission by default, but you may be able to get this permission with custom roles or other predefined roles.
## Accept Looker Studio Pro licenses
Looker (Google Cloud core) instances are granted 50 complimentary Looker Studio Pro licenses by default.
To accept these licenses, follow these steps in the Google Cloud console:
  1. Navigate to the **Instances** page for the Google Cloud project in which your Looker (Google Cloud core) instance resides.
  2. Select the name of the Looker (Google Cloud core) instance that you want to use with Looker Studio Pro.
  3. Select the **Looker Studio Pro** tab.
  4. Select **Accept Looker Studio Pro licenses**.


## Select a Google Cloud project
After you have accepted the complimentary Looker Studio Pro licenses, you must associate your Looker (Google Cloud core) instance with the Google Cloud project that your Looker Studio Pro subscription uses. To specify your Looker Studio Pro Google Cloud project, follow these steps in the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings:
  1. Click **Select project**.
  2. In the **Select a resource** dialog, select your project from the list, and click **Select project**.
  3. In the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings, click **Save**.


The **Project name** field now displays the selected Google Cloud project ID.
## Add users to your Looker Studio Pro subscription
To finish setting up your new Looker Studio Pro subscription, add users to your subscription and assign their licenses. You can complete these steps in either the Google Cloud console or Looker Studio, per your preference. If you had already completed the setup for your Looker Studio Pro subscription before you accepted your complimentary licenses, your licenses have been applied automatically to your existing Looker Studio Pro users.
Looker Studio More
To finish setting up your new Looker Studio Pro subscription in the Google Cloud console, follow these steps starting on the **Looker Studio Pro** page or tab for your Looker instance:
  1. Click **Add users** , which opens the Looker Studio Pro homepage within the Google Cloud console.
  2. Click **Subscribe** to open the **Buy Looker Studio Pro licenses** panel: 
     * The **Current no-cost Pro licenses** line item displays the number of complimentary Looker Studio Pro licenses that have been allocated to your Looker (Google Cloud core) instance.
  3. In the **Add users / groups** field, add the email addresses of users or groups to your subscription. 
     * The **Total licenses** field displays the total number of licenses that are required to support the number of users that you have added.
     * Select **Auto-assign licenses to new users added to a group** to assign available licenses to users who are added to Google Groups under the Looker Studio subscription.
  4. Click **Buy**.


To finish setting up your new Looker Studio Pro subscription in Looker Studio, follow these steps from the **Looker Studio Pro** page or tab for your Looker instance:
  1. Click **add users in Looker Studio Pro**.
  2. Add users to your subscription by following the steps described on the Add people to the subscription documentation page.


### Remove licenses or users
Each Looker Studio Pro user requires a Looker Studio Pro license. If you need to decrease the number of licenses that are used with your Looker Studio Pro subscription, you will also need to remove the corresponding number of users.
To remove licenses and users from your Looker Studio Pro subscription in the Google Cloud console, follow these steps:
  1. In the Google Cloud project that hosts your Looker Studio Pro subscription content, navigate to the **Looker Studio** page.
  2. Select **Manage access**.
  3. Select the user or group that you want to remove from the subscription.
  4. Select delete **Delete**. In the resulting dialog, select **Delete** again.
  5. Close the **Manage access** window.
  6. Select **Add / remove licenses**.
  7. Next to the **Total licenses** field, select remove **Decrement license count** to decrease the number of licenses under the Looker Studio Pro subscription.
  8. Select **Confirm**.


For more information, see Remove users from a Pro subscription.
## Transfer complimentary Looker Studio Pro licenses to a different subscription
After you have saved the project that you selected for your Looker Studio Pro licenses in your Looker instance, we strongly recommend that you don't modify the project selection. Your complimentary licenses must be associated with the same Google Cloud project as your Looker Studio Pro subscription. If you need to transfer your licenses from one Looker Studio Pro subscription to another, follow these steps:
  1. Set up a new Looker Studio Pro subscription based on a different project.
  2. Add users to your new subscription.
  3. Transfer ownership for any "ownerless" content that resides in team workspaces that are associated with the old subscription.
  4. Cancel the old subscription.


Next, to associate your complimentary Looker Studio Pro licenses with the new Looker Studio Pro subscription, follow these steps:
  1. Navigate to the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings.
  2. Click **Select project**.
  3. In the **Select a resource** dialog, choose your new selection from the list, and click **Select project**.
  4. Select a Google Cloud project that is associated with the new Looker Studio Pro subscription.
  5. In the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings, click **Save**.


The **Project name** field now displays the Google Cloud project ID that is associated with the new Looker Studio Pro subscription.
## Effects of canceling a Looker Studio Pro subscription
If the Looker Studio Pro subscription is canceled, Looker will no longer recognize the subscription. Although the Google Cloud console will continue to reflect that the Looker instance and the Looker Studio Pro subscription are linked, you will no longer be billed for Looker Studio Pro usage on the Google Cloud project. Your Looker instance's Looker Studio Pro licenses are still available if you reinstate your subscription (within the 30-day grace period) or if you initiate a new subscription. The no-cost version of Looker Studio is also available for use.
For more information about the effects of canceling a Looker Studio Pro subscription or deleting a Google Cloud project that is associated with a canceled subscription, see Cancel a Looker Studio Pro subscription.
## Troubleshooting complimentary licenses
Errors may occur when you accept complimentary Looker Studio Pro licenses or add users to a Looker Studio Pro subscription. See the following table for steps on how to troubleshoot errors that are related to accepting licenses.
Error message | Steps to resolve | Example  
---|---|---  
`You have reached your license limit. To add more users, either delete some existing users/groups or purchase additional licenses.` | 
  1. In Looker Studio, select **Pro subscriptions** from the left navigation to open the list of Looker Studio Pro subscriptions.
  2. Looker Studio displays the number of complimentary licenses that are available for the Google Cloud project that hosts your Looker (Google Cloud core) instance. For that project, under **Actions** , select **Manage subscription**.
  3. Navigate to the **Review and confirm Looker Studio Pro licenses** step, and review the number of licenses in the **Number of licenses to buy** field.
  4. Enter the total number of licenses that you want to use, _including_ the number of complimentary licenses that are available for the subscription.

| If there are 10 complimentary licenses available, add 10 users to your subscription to use all licenses. If you add 11 users, you will be charged for 1 additional license. If you increase the **Number of licenses to buy** field to 11, you will be charged for 1 additional license, which you can assign at a later date.   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


