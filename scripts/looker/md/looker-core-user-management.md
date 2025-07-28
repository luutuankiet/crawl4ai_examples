# Manage users within Looker (Google Cloud core)

**Source:** https://cloud.google.com/looker/docs/looker-core-user-management

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Required permission
  * Adding users to a Looker (Google Cloud core) instance
    * Creating an API-only service account
  * Removing access to Looker (Google Cloud core)
  * Selecting an authentication method for Looker (Google Cloud core) users
  * Setting a default Looker role within the Looker (Google Cloud core) instance




Was this helpful?
Send feedback 
#  Manage users within Looker (Google Cloud core)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Required permission
  * Adding users to a Looker (Google Cloud core) instance
    * Creating an API-only service account
  * Removing access to Looker (Google Cloud core)
  * Selecting an authentication method for Looker (Google Cloud core) users
  * Setting a default Looker role within the Looker (Google Cloud core) instance


Within a Looker (Google Cloud core) instance, several settings are available for managing users.
## Required permission
In order to manage users within a Looker (Google Cloud core) instance, you must have the Admin role within Looker.
## The Users page
The **Admin > Users** page within Looker displays active users within Looker (Google Cloud core) and lets you make certain edits to their accounts within Looker, such as editing the following account settings:


Users' names and email addresses must be edited within the identity provider that is used for authentication.
Unlike within Looker (original) instances, the following is not available in the Looker (Google Cloud core) **Users** page:
  * add users (with the exception of service accounts)
  * send setup link / send reset link
  * set up two-factor authentication
  * sudo as a user


## Adding users to a Looker (Google Cloud core) instance
To add individual Looker (Google Cloud core) users, add users within your identity provider. Their Looker accounts will be created upon first login. Individual users cannot be added on the **Users** page; however, API-only service accounts can be added on the **Users** page.
### Creating an API-only service account
You can create API-only accounts (often called "service accounts") from the **Users** page within a Looker (Google Cloud core) instance. These accounts can be granted Admin Looker roles and can be granted Looker API credentials. However, these accounts cannot log in to Looker (Google Cloud core) through the UI. To add a service account, follow these steps:
  1. Click the **Add Service Account** button.
  2. Enter an email address for the service account.
  3. Select the Groups and Roles to assign to the service account.
  4. Click the **Save** button.


## Removing access to Looker (Google Cloud core)
Remove access to a Looker (Google Cloud core) instance by updating the identity provider that was used for authentication. Although the user can no longer log in to the instance, the user account will still appear active on the **Users** page. To remove the user account from the **Users** page, delete the user within the Looker (Google Cloud core) instance.
## Selecting an authentication method for Looker (Google Cloud core) users
An OAuth client must be set up as part of instance creation, and OAuth authentication is the backup authentication method for Looker (Google Cloud core). However, you can choose between several different primary authentication methods. The Authentication methods for Looker (Google Cloud core) documentation page lists the available authentication methods.
## Setting a default Looker role within the Looker (Google Cloud core) instance
Before you add any users, you can set the default Looker role that will be granted to user accounts with the Looker Instance User IAM role upon their first login to a Looker (Google Cloud core) instance. To set a default role, follow the steps provided in the documentation for your identity provider: OAuth, SAML, or OpenID Connect.
## What's next
  * Connect Looker (Google Cloud core) to your database
  * Configure a Looker (Google Cloud core) instance
  * Looker (Google Cloud core) admin settings
  * Administer a Looker (Google Cloud core) instance from the Google Cloud console


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


