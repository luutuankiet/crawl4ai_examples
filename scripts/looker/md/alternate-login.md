# Enabling the alternate login option  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/alternate-login

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling alternate login on the Looker instance
  * Granting the user permission to use alternate login
  * Creating email credentials for the user
    * Making a POST request to the Looker API
    * Using the Looker API SDK




Was this helpful?
Send feedback 
#  Enabling the alternate login option
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling alternate login on the Looker instance
  * Granting the user permission to use alternate login
  * Creating email credentials for the user
    * Making a POST request to the Looker API
    * Using the Looker API SDK


Looker can authenticate users using one of several authentication server types, such as Google OAuth, LDAP, SAML, or OpenID Connect. Enabling any of these authentication methods will disable other authentication systems, such as email and password.
Looker admins can give a user an alternate login option that uses their email address if the user has either an Admin role or the `login_special_email` permission.
## Enabling alternate login on the Looker instance
Before you can enable the alternate login option for a user, the Looker instance must be configured to accept email credentials:
  1. Navigate to the **Authentication** section of the **Admin** panel, and select the currently enabled authentication type, Google OAuth, LDAP, SAML, or OpenID Connect.
  2. In the **Migration Options** section, enable the **Alternate login for admins and specified users** toggle.


## Granting the user permission to use alternate login
Only users with the Admin role or the `login_special_email` permission may use alternate login. One way to grant the `login_special_email` permission to a non-admin user is to create a new role that contains that permission and then assign that role to the user, as follows:
  1. Navigate to the **Roles** page, located under the **Users** section in the **Admin** panel.
  2. Click the **New Permission Set** button.
  3. Enter a name for the new permission set, for example, **Alternate Login**.
  4. Select the box labeled **login_special_email**.
  5. Click **New Permission Set**.
  6. Click **New Role**.
  7. Enter a name for the new role, such as **Alternate Login Role**.
  8. In the **Permission Set** list, select your new permission set from the list.
  9. In the **Model Set** list, select **All**.
  10. In the **Users** list, select the user who is to be granted the alternate login permission.
  11. Click the **New Role** button to save the new role.
  12. Click **Confirm**.


## Creating email credentials for the user
Once the user has been granted permission to use email credentials, the next step is to create the credentials. To create email credentials, a Looker admin can either use the Looker API to make a `POST` request or use the Looker API SDK in the programming language of the admin's choice.
### Making a POST request to the Looker API
Because of its manual nature, this is a better method to use when you have only a limited number of users for whom you want to set up the alternate login option.
This example uses a `curl` command to make a `POST` request to the `create_user_credentials_email` API endpoint using a temporary access token:
  1. To generate the temporary token (`ACCESS_TOKEN`), follow the **Authentication without an SDK** instructions on the Looker API authentication documentation page.
  2. Using this temporary token in the authorization header, send a `POST` request to the Looker API using the user's `user_id`, and include their email in the body of the request.
```
curl -H "Authorization: token ACCESS_TOKEN" -H 'Content-Type: application/json' -X POST -d '{ "email": "example_name@example_email.com" }' https://<instance_name<.api.looker.com/api/4.0/users/{user_id}/credentials_email

```

  3. On the **Users** page in the **Admin** panel, find the user account and click **Edit**.
  4. Click the **Send reset link** button. This will send an email to the email address you specified in your `POST` request.


To use the alternate login method, when the user logs in to Looker they will need to click the **Alternate Login** link and then enter their name and email address. They can still authenticate using their OAuth, LDAP, SAML, or OpenID Connect credentials through the **Authenticate** button.
### Using the Looker API SDK
Rather than going through the manual steps of making requests directly to the Looker API, you can instead use a Looker-provided SDK to interact with the API in a programming language of your choice. After you have imported the Looker API SDK and established a client connection, follow these steps:
  1. Use the `create_user_credentials_email(user_id, body)` function, inserting the `user_id` and `body` as specified in the Looker API documentation. You can follow a similar example from this Looker Community post about automatically provisioning users with the Looker API.
  2. Once the user accounts have been updated using the SDK method, on the **Users** page in the **Admin** panel, find the user account and click **Edit**.
  3. Click the **Send reset link** button. This will send an email to the email address you specified in your `POST` request.


To use the alternate login method, when the user logs in to Looker, they will need to click the **Alternate Login** link and then enter their name and email address. They can still authenticate using their OAuth, LDAP, SAML, or OpenID Connect credentials through the **Authenticate** button.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


