# Admin settings - Password requirements  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-authentication-password

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Admin settings - Password requirements
Stay organized with collections  Save and categorize content based on your preferences. 
By default, passwords in Looker must be a minimum of ten characters long and contain at least one uppercase and one lowercase letter (A, z), one numeric character (0-9), and one special character (such as !, %, @, or #). The **Passwords** page in the **Authentication** section of the **Admin** menu provides admins with additional control over password requirements for users on their instance.
## Customizing password requirements
Looker admins can enforce additional security requirements by specifying a minimum password length or requiring special characters in passwords. To manage password requirements for users on your instance, select **Passwords** in the **Authentication** section of the Looker **Admin** menu. This opens the **Password Requirements** page.
On the **Password Requirements** page, Looker displays current password requirement settings for existing users on your Looker instance. You can change these settings by choosing a minimum number of characters or requiring special characters.
> Password complexity requirement settings have no effect on passwords hosted by external authentication systems (SAML, LDAP, Google Auth, OpenID Connect).
### Specifying a minimum password length
In **Minimum Password Length** , you can specify the minimum number of characters required for a password. By default, a password in Looker must be at least 10 characters long. To require a different minimum password length, select a number from the drop-down menu.
### Requiring special characters
Looker admins can require that passwords contain special characters. In **Require at least one** , check the corresponding box to require at least one of the following:
  * Uppercase and lowercase letter (A, z)
  * Numeric character (0-9)
  * Special character (any character your environment will accept that is not an uppercase or a lowercase letter or a numeric character — for example, !, %, @, #, and so on)


### Saving your settings
Once you have chosen your desired settings, click **Save**. Any user on your instance who creates a new password will be required to meet the conditions you have specified.
## Requiring users to reset passwords
To require locally configured users to reset their passwords upon their next login to Looker, click **Require Password Reset**. The next time a user logs in to Looker, they will be required to create a new password that satisfies the current minimum password requirements.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


