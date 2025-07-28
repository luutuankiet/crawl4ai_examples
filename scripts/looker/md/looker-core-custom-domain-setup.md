# Set up a custom domain for a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-custom-domain-setup

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Set up a custom domain
    * Before you begin
    * Create a custom domain
  * Access the custom domain




Was this helpful?
Send feedback 
#  Set up a custom domain for a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Set up a custom domain
    * Before you begin
    * Create a custom domain
  * Access the custom domain


You can serve your instance through a custom web domain rather than through the default domain that Looker (Google Cloud core) provides.
This documentation page describes how to use the Google Cloud console to set up a custom domain for any type of Looker (Google Cloud core) instance.
## Set up a custom domain
After your Looker (Google Cloud core) instance has been created, you can set up a custom domain.
### Before you begin
Before you can customize the domain of your Looker (Google Cloud core) instance, identify where your domain's DNS records are stored, so that you can update them.
#### Required roles
To get the permissions that you need to create a custom domain for a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project the instance resides in. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
### Create a custom domain
In the Google Cloud console, follow these steps to customize the domain of your Looker (Google Cloud core) instance:
  1. On the **Instances** page, click the name of the instance for which you would like to set up a custom domain.
  2. Click the **CUSTOM DOMAIN** tab.
  3. Click **ADD A CUSTOM DOMAIN**.
This opens the **Add a new custom domain** panel.
  4. Using only letters, numbers, and dashes, enter the hostname of up to 64 characters for the web domain that you would like to use — for example: `looker.examplepetstore.com`.
  5. Click **DONE** on the **Add a new custom domain** panel to return to the **CUSTOM DOMAIN** tab.


Once your custom domain is set up, it is displayed in the **Domain** column on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) instance details page in the Google Cloud console.
After your custom domain has been created, you can view information about it, or delete it.
## Access the custom domain
After a custom domain is set up in the Google Cloud console, you must configure your network to allow users to access the domain. To learn more about that configuration for your use case, review the following documentation pages.
Access a custom domain from the internet:
  * Set up and access a custom domain for a public IP Looker (Google Cloud core) instance
  * Access a Private Service Connect instance from the internet


Access a custom domain through a private network:
  * Access a Looker (Google Cloud core) instance using private services access
  * Private northbound access to a Looker (Google Cloud core) instance using Private Service Connect


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


