# Quickstart: Create a Looker (Google Cloud core) Public IP standard edition instance

**Source:** https://cloud.google.com/looker/docs/looker-core-quickstart-public-ip-standard-edition

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Create the Looker (Google Cloud core) instance




Was this helpful?
Send feedback 
  * On this page
  * Before you begin
  * Create the Looker (Google Cloud core) instance


# Create a Looker (Google Cloud core) public IP standard edition instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Learn how to create a Looker (Google Cloud core) instance that uses default configuration settings. Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.
To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 
## Before you begin
Before you can create an instance, you need to complete these steps for the Google Cloud project in which you want to create the Looker (Google Cloud core) instance:
  1. Work with Sales to ensure that your annual contract is completed and that you have quota allocated in your project.
  2. Make sure that billing is enabled for your Google Cloud project.
  3. In the Google Cloud console, on the project selector page, create a Google Cloud project or navigate to an existing one. 
Go to project selector
  4. Enable the Looker API for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 
Enable the API
  5. Create authorization credentials. You can use any OAuth 2.0 client to create authorization credentials when you're creating an instance. See the Create authorization credentials for a Looker (Google Cloud core) instance documentation page for an example that uses the Google Cloud console to create OAuth credentials.
  6. Ensure that the Looker Admin IAM role is enabled for the Google Cloud project in which you want to create the Looker (Google Cloud core) instance.


## Create the Looker (Google Cloud core) instance
To create a Looker (Google Cloud core) instance that uses default configuration settings, follow these steps:
  1. Click Go to Looker (Google Cloud core) and select the Google Cloud project in which you want to create the Looker (Google Cloud core) instance, if it is not already pre-selected. When you click the button, depending on what Looker instances already exist in this project, you'll see one of the following: 
     * If a Looker (Google Cloud core) instance already exists within this project, the **Instances** page will open. Click **Create Instance** to open the instance creation page.
     * If no Looker (Google Cloud core) instances have been created in this project, the Looker (Google Cloud core) product page will open. Click **Create An Instance** to open the instance creation page.
  2. In the **Instance name** field, provide a name for your Looker (Google Cloud core) instance. The instance name is not associated with the instance's URL. You won't be able to rename the instance after it has been created.
  3. In the **OAuth Application Credentials** section, enter the **OAuth client ID** and **OAuth secret** that you created when you set up your OAuth client.
  4. In the **Region** field, select the region that matches your subscription contract, as this is where the quota for your project is allocated. Then click **OK**.
  5. In the **Edition** section, set the instance edition to **Standard**. This edition provides a Looker platform that is best for small organizations or teams with fewer than 50 users. This edition is billed monthly while the instance is active.
  6. Click **Create**. Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.


## What's next
This Quickstart covered how to create a **Standard** Looker (Google Cloud core) instance that uses a Public IP network connection and Google-managed encryption and that requires no deferred or denied maintenance windows and no additional users beyond the default number that is provided for a **Standard** edition.
For more information about creating and configuring an instance, see the Looker (Google Cloud core) documentation:
  * Create a Looker (Google Cloud core) instance
  * Configure a Looker (Google Cloud core) instance
  * Connect to your database
  * Use the sample LookML project on a Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


