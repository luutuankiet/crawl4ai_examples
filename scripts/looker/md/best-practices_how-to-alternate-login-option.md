# Enabling the alternate login option  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-alternate-login-option

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Step 1: Enable alternate login on the Looker instance
  * Step 2: Grant the user permission to use alternate login
  * Step 3: Creating email credentials for the user
    * Option 1: Making a POST request to the Looker API
    * Option 2: Using the Looker API SDK




Was this helpful?
Send feedback 
#  Enabling the alternate login option
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Step 1: Enable alternate login on the Looker instance
  * Step 2: Grant the user permission to use alternate login
  * Step 3: Creating email credentials for the user
    * Option 1: Making a POST request to the Looker API
    * Option 2: Using the Looker API SDK


Looker can authenticate users through one of several authentication server types, such as LDAP, SAML, or Google OAuth. Enabling any of these authentication methods will disable other authentication systems, such as email/password. 
Admins can give users an alternate login option that uses their email address if the user or users have either an Admin role or `login_special_email` permissions. 
## Step 1: Enable alternate login on the Looker instance
First, the Looker instance must be configured to accept email credentials. To configure Looker to accept email credentials, follow these steps: 
  1. Navigate to the **Authentication** tab of the **Admin** panel, and select the currently enabled authentication type. Some examples include **LDAP** , **SAML** , and **Google OAuth**.
  2. Enable the **Alternate login for admins and specified users** switch in the **Migration Options** section. 


## Step 2: Grant the user permission to use alternate login
Only users with the Admin role or with the `login_special_email` permission may use alternate login. One way to grant the `login_special_email` permission to a non-admin user is to first create a new role containing that permission and then assign that role to the user, as follows: 
  1. Navigate to the **Roles** page, located under the **Users** tab of the **Admin** panel.
  2. Click the **New Permission Set** button at the top of the page.
  3. Enter a name for the new permission set, for example, "Alternate Login".
  4. Check the box labeled `login_special_email`.
  5. Click the **Save** button at the bottom of the page.
  6. Click the **New Role** button at the top of the page.
  7. Enter a name for the new role, for example, "Alternate Login Role".
  8. Under the **Permission Set** section, select your new permission set from the list of permission sets.
  9. Under the **Model Set** section, select **All**.
  10. Under the **Users** section, select the user that should be granted the alternate login permission.
  11. Click the **New Role** button at the bottom of the page to save the new role.
  12. Click the **Confirm** button in the pop-up dialog box.


## Step 3: Creating email credentials for the user
Now that the user has been enabled to use email credentials, those email credentials must be created. To create these credentials, a Looker admin can either use the Looker API to make a POST request or use the Looker API SDK in the programming language of the admin's choice. 
### Option 1: Making a POST request to the Looker API
Because of its manual nature, this is a better method to use when you have a limited number of users for whom you want to set up the alternate login option. 
This example uses a curl command to make a POST request to the `create_user_credentials_email` API endpoint using a temporary access token: 
  1. To generate the temporary token (`ACCESS_TOKEN`), follow the steps on the API Authentication documentation page in the **Authentication without a SDK** section. 
  2. Using this temporary token in the authorization header, send a POST request to the Looker API using the user's `user_id`, and include their email in the body of the request. ```
 curl -H "Authorization: token ACCESS_TOKEN" -H 'Content-Type: application/json' -X POST -d '{ "email": "example_name@example_email.com" }' https://<instance_name<.api.looker.com/api/3.1/users/{user_id}/credentials_email
```

  3. On the **Users** page of the **Admin** section, find the user account and click **Edit**. 
  4. Click the **Send reset link** button. This will send an email to the email address you specified in your POST request. 


To use the alternate login method, when the user logs in to Looker they will need to click the **Alternate Login** link and then enter their name and email address. They can still authenticate by using their SAML, LDAP, or OAuth credentials through the **Authenticate** button. 
### Option 2: Using the Looker API SDK
Rather than going through the manual steps of making requests directly to the Looker API, you can instead use a Looker-provided SDK to interact with the API in a programming language of your choice. After you have imported the Looker API SDK and established a client connection, follow these steps: 
  1. Use the `create_user_credentials_email(user_id, body)` function, inserting the `user_id` and `body` as specified in the Looker API documentation. You can follow a similar example from this Looker Community post about automatically provisioning users with the Looker API. 
  2. Once the user accounts have been updated using the SDK method, on the **Users** page of the **Admin** section, find the user account and click **Edit**. 
  3. Click the **Send reset link** button. This will send an email to the email address you specified in your POST request. 


To use the alternate login method, when the user logs in to Looker, they will need to click the **Alternate Login** link and then enter their name and email address. They can still authenticate by using their SAML, LDAP, or OAuth credentials through the **Authenticate** button. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


