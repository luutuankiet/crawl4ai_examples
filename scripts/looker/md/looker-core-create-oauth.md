# Create OAuth authorization credentials for a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-create-oauth

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you create a Looker (Google Cloud core) instance
    * Generate the OAuth client ID and client secret
    * Configure the user consent screen, scopes, and test users
  * During Looker (Google Cloud core) instance creation
  * After you create a Looker (Google Cloud core) instance
    * Add the authorized redirect URI to the OAuth client
    * Edit the OAuth client for a Looker (Google Cloud core) instance




Was this helpful?
Send feedback 
#  Create OAuth authorization credentials for a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you create a Looker (Google Cloud core) instance
    * Generate the OAuth client ID and client secret
    * Configure the user consent screen, scopes, and test users
  * During Looker (Google Cloud core) instance creation
  * After you create a Looker (Google Cloud core) instance
    * Add the authorized redirect URI to the OAuth client
    * Edit the OAuth client for a Looker (Google Cloud core) instance


An OAuth client must be set up and OAuth credentials must be generated as part of Looker (Google Cloud core) instance creation, even if you want to use a different authentication method for authenticating your users into a Looker (Google Cloud core) instance.
## Required roles
To use the Google Cloud console to create and edit OAuth credentials, you need the following permissions. (To hide the list of permissions, collapse the **Required permissions** section.) 
#### Required permissions
  * clientauthconfig.*
    * clientauthconfig.brands.create
    * clientauthconfig.brands.delete
    * clientauthconfig.brands.get
    * clientauthconfig.brands.list
    * clientauthconfig.brands.update
    * clientauthconfig.clients.create
    * clientauthconfig.clients.createSecret
    * clientauthconfig.clients.delete
    * clientauthconfig.clients.get
    * clientauthconfig.clients.getWithSecret
    * clientauthconfig.clients.list
    * clientauthconfig.clients.listWithSecrets
    * clientauthconfig.clients.undelete
    * clientauthconfig.clients.update
  * oauthconfig.*
    * oauthconfig.clientpolicy.get
    * oauthconfig.testusers.get
    * oauthconfig.testusers.update
    * oauthconfig.verification.get
    * oauthconfig.verification.submit
    * oauthconfig.verification.update


You might also be able to get the required permissions through custom roles or other predefined roles. For more information about granting roles, see the Manage access to projects, folders, and organizations page in the Identity and Access Management (IAM) documentation.
## Before you create a Looker (Google Cloud core) instance
Before you create a Looker (Google Cloud core) instance, complete the steps that are described in these sections:
  * Generate the OAuth client ID and client secret
  * Configure the user consent screen, scopes, and test users


### Generate the OAuth client ID and client secret
First, create an OAuth client and generate the client ID and client secret for that client. These values are required during creation of the Looker (Google Cloud core) instance.
You can set up the OAuth client in any Google Cloud project you want. It doesn't need to be the same project as the Looker (Google Cloud core) instance. However, the Looker (Google Cloud core) API **must be enabled** in this project.
To create the client and its credentials, follow these steps:
  1. Navigate to the project that you want to create the OAuth client in.
  2. Navigate to **APIs & Services > Credentials**.
  3. From the **Credentials** page, click **Create Credentials**.
  4. From the drop-down menu, select **OAuth client ID**.
  5. In the **Application type** drop-down, select **Web application**.
  6. In the **Name** field, enter a name for your OAuth client.
  7. At this point, you **don't** need to add URIs in the **Authorized JavaScript origins** or **Authorized redirect URIs** sections.
  8. Click **Create**.


After you click **Create** , an **OAuth client created** window appears. This window displays the client ID and client secret created for your OAuth client. These values will be required when you create the Looker (Google Cloud core) instance.
Optionally, click **Download JSON** to download the credential information in a JSON file. To close the window, click **OK**.
### Configure the user consent screen, scopes, and test users
Next, you may want to configure the consent screen. The consent screen is shown to a user of the Looker (Google Cloud core) instance at their first login and at any point when their authorization expires or is revoked by the user.
Follow the instructions on the Configure the OAuth consent screen and choose scopes documentation page. While configuring your screen, complete the following settings as described:
  * In the **Branding** section, under **Authorized domains** , the domain must match the domain of the Looker (Google Cloud core) instance that uses the OAuth credentials. If you are going to create a custom domain for your Looker (Google Cloud core) instance and know the domain that you will assign to it, you can enter it now. Otherwise, you can leave this field empty; it will be automatically populated when you add the authorized redirect URI after the Looker (Google Cloud core) instance is created.
  * In the **Audience** section, under **User Type** , select one of the following:
    * **Internal** : This setting is the default. Only users within your organization can access the instance once they are added through IAM.
    * **Make external** : Users with any kind of Google Account can access the instance once they are added through IAM.


## During Looker (Google Cloud core) instance creation
When you are creating the Looker (Google Cloud core) instance, add the OAuth client ID and client secret in the **OAuth Application Credentials** section. You cannot create an instance without OAuth credentials. Find the OAuth client ID and client secret by navigating to the OAuth client in the Google Cloud console.
## After you create a Looker (Google Cloud core) instance
Complete the following instructions to finish configuration. When you add an authorized redirect URI, it will be added to your OAuth consent screen as an authorized domain.
### Add the authorized redirect URI to the OAuth client
If you haven't done so already, follow these steps to enter the URL of the newly created Looker (Google Cloud core) instance into the OAuth client.
  1. After you have created a Looker (Google Cloud core) instance, find and copy the URL for the instance. You can find the URL on the **Instances** page.
  2. In the Google Cloud console, navigate to **APIs & Services > Credentials**.
  3. Under the **OAuth 2.0 Client IDs** heading, click the name of the client you created.
  4. In the **Authorized redirect URIs** section, click **Add URI**.
  5. Paste the URL of the Looker (Google Cloud core) instance into the **URIs** field. Add `/oauth2callback` to the end of the URL. For example: `https://uuid.looker.app/oauth2callback`.
If you are going to set up OAuth authorization for BigQuery, you can also add a second redirect URI that points to the URL of the Looker (Google Cloud core) instance followed by `/external_oauth/redirect` added to the end of the URL. For example: `https://uuid.looker.app/external_oauth/redirect`.
  6. Click **Save**.


It may take from five minutes to a few hours for the update to take effect.
### Manage users
Once the OAuth client is configured and the Looker (Google Cloud core) instance is created, you can choose the authentication method for your instance.
If using OAuth as your primary authentication method, complete the steps as described on the Use Google OAuth for Looker (Google Cloud core) user authentication documentation page to complete OAuth setup for user authentication.
Once your authentication method is set up, you can add or remove users through your identity provider and manage them within Looker.
### Edit the OAuth client for a Looker (Google Cloud core) instance
If you want, you can edit or change the OAuth credentials for your Looker (Google Cloud core) instance by following these steps:
  1. Set up the new client or credentials.
  2. In the Google Cloud console, from the **Instances** page, click on an instance's name to open the **DETAILS** page.
  3. From the **DETAILS** page, click **Edit**.
  4. On the **Edit Looker (Google Cloud core) instance** page, enter the new values in the **OAuth Client ID** and **OAuth Client Secret** fields.
  5. Click **Save**.


## What's next
  * Create a public IP Looker (Google Cloud core) instance
  * Create a private IP Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


