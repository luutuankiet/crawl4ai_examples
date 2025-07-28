# Setting up a local action hub for actions that use OAuth and streaming  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/action-hub-oauth-actions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Creating a container or virtual machine (VM) setup for the action hub server
    * Recommended memory allocation
    * Network requirements
    * Required dependencies
  * Configuring Google OAuth credentials
    * Creating the Google OAuth credentials
    * Configuring the OAuth consent screen
  * Setting your environment variables
  * Generating an API key
  * Starting your local action hub server
  * Adding your action hub to your Looker instance




Was this helpful?
Send feedback 
#  Setting up a local action hub for actions that use OAuth and streaming
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Creating a container or virtual machine (VM) setup for the action hub server
    * Recommended memory allocation
    * Network requirements
    * Required dependencies
  * Configuring Google OAuth credentials
    * Creating the Google OAuth credentials
    * Configuring the OAuth consent screen
  * Setting your environment variables
  * Generating an API key
  * Starting your local action hub server
  * Adding your action hub to your Looker instance


If a customer-hosted Looker instance is unable to communicate with the Looker-hosted action hub, Looker admins may be unable to enable actions that support streamed results or that use OAuth. Additionally, Looker users may experience hanging queries when sending or scheduling data to actions that support streamed results and may be unable to configure OAuth actions. 
To use Looker integrations, the Looker Action Hub and the Looker instance must be able to communicate with one another. Admins of customer-hosted instances who are interested in reading about solutions that are appropriate for their instance architecture can consult the recommendations described in the Considerations for customer-hosted instances section of the **Sharing data through an action hub** documentation page. 
> If the instance uses an SSL certificate issued by a Certificate Authority (CA) that is not on this list of root certificates, the OAuth and streaming actions might not be usable on a customer-hosted Looker instance. 
To see the actions that are configured to support streamed results or OAuth, see the list of Looker's integrated services on the Admin settings - Actions documentation page. 
This page describes how to spin up a local action hub server to use Looker actions that support streamed results or that use Google OAuth. You can set up your own local action hub server by creating either a container or a virtual machine (VM) that hosts a cloned copy of the Looker Action Hub repo code and then following these steps, as described in more detail in the following sections: 
  1. Create a container or virtual machine (VM) setup for the action hub server.
  2. Configure Google OAuth credentials.
  3. Configure the Google OAuth consent screen.
  4. Set up your environment variables.
  5. Generate an API key.
  6. Start the new action hub.
  7. Add the new action hub to your Looker instance.


## Creating a container or virtual machine (VM) setup for the action hub server
Your VM or container should fulfill the following allocation and network requirements and dependencies: 
  * Recommended memory allocation
  * Network requirements
  * Required dependencies


### Recommended memory allocation
Looker recommends allocating 2 threads of CPU/vCPU and at least 2 GB of memory for this container or VM. If you expect heavy usage of your actions, consider increasing memory beyond 2 GB. 
### Network requirements
> Your action hub must have either a static IP address _or_ an address that can be resolved via an internal Domain Name System (DNS). 
Your network must support the following communication requirements: 
  * The Looker instance must be able to communicate with the action hub.
  * Google Auth must be able to communicate with the action hub.
  * An internally connected browser must be able to reach the action hub.
  * The action hub must be able to reach the Google Drive servers.


### Required dependencies
When you're cloning the Looker actions repo into your newly created VM or container: 
  * Ensure that Node 12.13 is installed.
  * Run `yarn install` to install the necessary packages.


Once you have your environment set up, you will need to create Google OAuth credentials for your action hub server in the Google Cloud API Console. 
## Configuring Google OAuth credentials
To configure Google OAuth credentials for your actions, you'll need to: 
  * Create OAuth credentials
  * Configure an OAuth consent screen


### Creating the Google OAuth credentials
To make your Google OAuth client ID and client secret: 
  1. Go to the Google Cloud Manage resources page and click **CREATE PROJECT** to create a new project. 
For more information about creating a project, see the Creating and managing projects guide.
  2. Once your new project is created, select the new project. 
  3. From the console left sidebar, navigate to the **APIs & Services > Credentials** page.
  4. Click **Create Credentials**.
  5. In the drop-down, click **OAuth client ID**.
  6. You may need to configure an OAuth consent screen. If so, follow the instructions in the Configuring the OAuth consent screen section later on this page, and then proceed with step 7.
  7. For **Application type** , select **Web application**. 
  8. Provide your application name in the **Name** field.
  9. In the **Authorized JavaScript origins** section, add the root Looker application address that you use internally.
  10. Set the **Authorized redirect URIs** for the Google Drive and Google Sheets consoles where `ACTION_HUB_BASE_URL` is the address of your action hub: ```
            https://<ACTION_HUB_BASE_URL>/actions/google_sheets/oauth_redirect
            https://<ACTION_HUB_BASE_URL>/actions/google_drive/oauth_redirect
        
```

  11. Click the **Create** button to generate your OAuth client ID and the OAuth client secret. You will need both of these later.


### Configuring the OAuth consent screen
This page of the Google API Console allows you to configure a consent screen for all applications in your project, which allows users to grant access to their data as well as giving them a link to any legal or privacy documentation. If you have already completed this step or don't need to configure a consent screen, skip this section and return to your terminal window to set your environment variables, as described in Setting your environment variables later on this page. 
To configure the consent screen: 
  1. Click **CONFIGURE CONSENT SCREEN**.
  2. Select whether this is an internal or external application, and click **CREATE**.
  3. Enter the name of your application in the **App name** field.
  4. For **User support email** , enter an email address to display on the **Oauth consent screen** for user support.
  5. Optionally, for the **App logo** , upload an image file to use on the **Oauth consent screen**.
  6. Optionally, enter your **Application home page link** , which should be hosted on the same root domain as your action hub.
  7. Optionally, enter a link to your application's privacy policy in the **Application privacy policy link** field. The link must be hosted on the same root domain as your action hub.
  8. Optionally, enter a link to your application's terms of service in the **Application terms of service link** field. The link must be hosted on the same root domain as your action hub. 
  9. For the **Authorized domains** section, click **ADD DOMAIN** , and enter the root domain that your action hub is using.
  10. In the **Developer contact information** field, enter an email where Google can contact you.
  11. Click **SAVE AND CONTINUE**.
  12. In the **Scopes** section, add the types of user data that your application must access. This includes email, profile, OpenID, and `https://mail.google.com`. Because this list includes sensitive user information, Google will need to verify your **Oauth consent screen** before it can be published.
  13. Click **SAVE AND CONTINUE**.
  14. Optionally, in the **Test users** section, add any users whom you want to have access to the action hub prior to verification.
  15. Click **SAVE AND CONTINUE**.
  16. Click **BACK TO DASHBOARD**.
  17. In the left sidebar, click **Credentials** to return to configuring your OAuth credentials.


Once you have configured your OAuth consent screen, if you were in the process of configuring Google Oauth credentials, return to step 7 of that procedure and finish configuring credentials. Otherwise, you can return to your terminal window to set your environment variables. 
## Setting your environment variables
In your VM or container environment, set these environment variables: 
```
    ACTION_HUB_LABEL=<your action hub label name>
        ACTION_HUB_SECRET=<some secret>
        ACTION_HUB_BASE_URL=<your action hub base address>
            # For example https://actions.company.com
            # DO NOT INCLUDE A TRAILING SLASH
        GOOGLE_SHEET_CLIENT_ID=<OAuth client ID>
        GOOGLE_SHEET_CLIENT_SECRET=<OAuth client secret>
        GOOGLE_DRIVE_CLIENT_ID=<OAuth client ID>
        GOOGLE_DRIVE_CLIENT_SECRET=<OAuth client secret>

```

You should be able to use the same `OAuth client ID` and `OAuth client secret` for both Google Drive and Google Sheets; however, it is best to have both sets of Google API tokens set. 
Also set the encryption key: 
```
    CIPHER_MASTER="<hex aes-256 key>"

```

This key is _not_ used for long-term encryption; it's used only for encrypting `state` during an OAuth flow. The following is an example of a hex aes-256 key: 
```
    "C4EFBBE2C364248419776459A00F2F4017CE77E29D9E8F64940687EA440A0CC9"

```

## Generating an API key
To get your API key, run this command: 
`y     arn generate-api-key `
Retain the generated key for later use in the setup. This key is generated based on the `ACTION_HUB_SECRET`. 
## Starting your local action hub server
To start your action hub, run this command: 
`     yarn start `
## Adding your action hub to your Looker instance
To add your action hub to your Looker instance: 
  1. In Looker, navigate to the **Actions** page under **Platform** in the **Admin** panel.
  2. Scroll to the bottom of the page and click the **Add Action Hub** button.
  3. Enter your `ACTION_HUB_BASE_URL` and click **Add Action Hub**. Your action hub should appear under a new heading with its name and `ACTION_HUB_BASE_URL`. Your Google Drive and Google Sheets actions should appear under this heading.
  4. If the connection fails, enter the `api-key` that you generated earlier in the **Authorization Token** field, and click the **Refresh** link at the top of your action hub heading.
  5. Enable your Google Drive and Google Sheets actions, and verify that they are configured correctly in your action hub.


## Next step
The next step is to publish the application that you created in the Google API Console. To publish, go to the **OAuth consent screen** page and click the **Submit for verification** button. Please note that the application publication process may take some time and will require some verification steps with Google. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


