# Personalizing user account settings  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/user-account

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Changing standard account settings
  * Changing your email subscription settings
  * Configuring OAuth connection credentials
  * Configuring integrations with third-party services
  * Changing custom user settings




Was this helpful?
Send feedback 
#  Personalizing user account settings
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Changing standard account settings
  * Changing your email subscription settings
  * Configuring OAuth connection credentials
  * Configuring integrations with third-party services
  * Changing custom user settings


The **Account** page lets you configure some of your Looker user account settings. To access this page, select the **Profile** menu and then select **Account**.
This topic includes the following sections:
  * Changing standard account settings
  * Changing your email subscription settings
  * Configuring OAuth connection credentials
  * Configuring integrations with third-party services
  * Changing custom user settings
  * Saving changes


### Changing standard account settings
The top section of the **Account** page shows your Looker account's settings:
  * **Profile Picture** : If your Looker admin has enabled it, you can use the Gravatar app to select or create an avatar for your account.
  * **First Name** : First name that is configured on the account.
  * **Last Name** : Last name that is configured on the account.
  * **Email** : Email address that is associated with the Looker account (this field is not editable).
  * **Password** : Password that is associated with the account. Select the **Change Password** button to set a new password.
  * **Time Zone** : Default time zone to be used for queries for this user.
  * **Development Mode** : The user's Git branch for LookML development. This field defaults to the branch created when the user account was created, but you can select other branches.
  * **Text Editor Mode** : The style of text editor for the LookML IDE. You can choose from Looker's default text editor style, a Vim text editor, or an Emacs text editor.
  * **Subscription Settings:** The types of Looker emails that the user will receive, as described in the Changing your email subscription settings section.


### Changing your email subscription settings
You can manage your Looker email subscription settings. Choose whether you want to receive product and event announcements, tips and tricks, and other types of information.
You can view and update these settings in Looker's **Preference Center**. From the **Profile** section of your Looker **Account** page, select **Manage your email subscription settings** to open the preference center.
Follow these steps to update your preferences for Looker email subscriptions:
  1. In **Preferences for** , Looker fills in the email address from your account settings. If you would prefer a different email address, contact your Looker admin.
  2. In **Content** , select checkboxes for the types of emails you want to receive from Looker.
  3. If you want to suspend delivery of Looker emails for three months, or if you want to unsubscribe from all Looker emails, select the corresponding checkbox in **Settings**.
  4. Once you have selected your desired subscription settings, select **Update Preferences**.


When you select the **Update Preferences** button, Looker saves your email subscription preferences and sends you an email confirming your changes. You can return to this page to update your settings anytime by clicking the **Manage your email subscription settings** link on the **Account** page.
> If you don't have a Looker account, you can sign up for a subset of these email preferences by navigating to the **Looker Preference Center**, typing your email address, and making your selections.
### Configuring OAuth connection credentials
If your Looker instance has database connections that use OAuth, such as Snowflake or Google BigQuery, Looker displays a section for **OAuth Connection Credentials**.
Select **Log In** to enter your OAuth credentials through an OAuth interface. If you have already logged in, Looker instead displays the options **Reauthorize** and **Log Out**.
Select **Reauthorize** to open the OAuth login page, or select **Log Out** to log your Looker user account out of the OAuth session.
See the Snowflake documentation page for more information on using OAuth for Snowflake connections. See the Google BigQuery documentation page for more information on using OAuth for BigQuery connections.
### Configuring integrations with third-party services
Some third-party services integrated with Looker — such as Slack — require users to perform a one-time authentication before use.
The integrations that require your authentication are listed in the **Integrations** section of your user **Account** page.
If no integrations that require your authentication are enabled for your Looker instance, Looker displays a note in the **Integrations** section:
```
There are no installed integrations. Contact your admin to install an integration.

```

If your admin has enabled an integration that requires you to authenticate into a third-party service, Looker displays the name of the service that is listed in the **Integrations** section, along with an indication of what action you need to take.
Once you have successfully authenticated, Looker displays the name of the service that is listed in the **Integrations** section, along with any options to revoke authentication that may exist for that service.
### Changing custom user settings
Your Looker admin can set up additional user attributes that help with customizing your experience in Looker. The **Additional Details** section displays the values of the user attributes that are configured for your Looker account. It shows a list of each of your user attributes followed by its assigned value. If your Looker admin has set any of the user attributes to `hidden`, Looker won't display that value. Instead, the value will be indicated by a series of asterisks.
The **Custom Value** column indicates if the user attribute value is a custom value. A custom value is a value that is assigned to your user account individually, instead of a value that your account inherited from a group. If the **Custom Value** switch next to a user attribute is turned on, that user attribute has a custom value.
You may be able to edit some user attributes, depending on how your Looker admin has configured your account. To do so, turn on the **Custom Value** switch next to a user attribute, enter the value you want, and select **Save**.
### Saving changes
After making changes to any of the options on this page, select the **Save** button to save your changes.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


