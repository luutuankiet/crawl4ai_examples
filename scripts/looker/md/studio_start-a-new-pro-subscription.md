# Start a new Pro subscription  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/start-a-new-pro-subscription

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Looker customers: Start here instead
  * Before you begin
  * Ways to subscribe
    * Subscribe to Looker Studio Pro from Looker Studio
    * Subscribe to Looker Studio Pro from the Google Cloud console




Was this helpful?
Send feedback 
#  Start a new Pro subscription
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Looker customers: Start here instead
  * Before you begin
  * Ways to subscribe
    * Subscribe to Looker Studio Pro from Looker Studio
    * Subscribe to Looker Studio Pro from the Google Cloud console


This page provides an overview of the steps you need to take to start a new Looker Studio Pro subscription.
> ## Looker customers: Start here instead
> Organizations that use Looker can receive complimentary Looker Studio Pro licenses. Select your version for instructions on how to subscribe and redeem these licenses:
>   * Looker (original)
>   * Looker (Google Cloud core)
> 

## Before you begin
To set up a self-service subscription to Looker Studio Pro, you must meet all of the following requirements:
  * You must be a Google Workspace or Cloud Identity user with a Managed Google account to subscribe to or use Looker Studio Pro.
  * You will need to provide a valid Google Cloud project that is linked to a billing account. Learn how to set up a Google Cloud billing account.
  * You must have the **Owner** (`roles/owner`) or **Looker Studio Pro Manager** (`roles/lookerstudio.proManager`) IAM role on the Google Cloud project that you use for Looker Studio Pro.
  * You must have the `resourcemanager.projects.updateLiens` permission on the Google Cloud project that you use for Looker Studio Pro. This is required so that Google Cloud can create a lien on the Google Cloud project, which helps to prevent accidental deletion of your Looker Studio Pro assets.
  * Your organization must own the Google Cloud project that you use for Looker Studio Pro.
  * You must belong to the same organization that owns the Google Cloud project that is used for the subscription. (For example, you can't make someone who is outside your organization an owner on the project and have that outside user subscribe to Looker Studio Pro on behalf of the organization.)
  * The Google Cloud project that you use for Looker Studio Pro must not be in use for a Pro subscription.


For more information about granting Cloud IAM roles, see the Manage access to projects, folders, and organizations documentation page. You might also be able to get the required permissions through custom roles or other predefined roles.
## Ways to subscribe
You can subscribe to Looker Studio Pro in the following ways:
  * From within Looker Studio
  * From the Google Cloud console


### Subscribe to Looker Studio Pro from Looker Studio
To subscribe to Looker Studio Pro from within the product, follow these steps:
  * Sign in to Looker Studio.
  * In the left navigation, click **Pro subscription**.
  * Click **Add subscription**.


### Subscribe to Looker Studio Pro from the Google Cloud console
To subscribe to Looker Studio Pro from the Google Cloud console, follow these steps:
  * Navigate to the Looker Studio homepage: https://console.cloud.google.com/looker-studio/home
  * If necessary, select the Google Cloud project to use with Looker Studio Pro.
  * Click **Get started**.


The articles that follow give details for each of the subscription steps:
  * Step 1: Select a Google Cloud project
  * Step 2: Add people to the subscription
  * Step 3: Buy additional Looker Studio Pro licenses


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


