# Admin settings - Users  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-users-users

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing and searching users
  * Editing users
    * Send setup link / Send reset link
    * Two-Factor Secret
  * Removing user access
  * Impersonating (sudoing) users




Was this helpful?
Send feedback 
#  Admin settings - Users
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing and searching users
  * Editing users
    * Send setup link / Send reset link
    * Two-Factor Secret
  * Removing user access
  * Impersonating (sudoing) users


The **Users** page in the **Users** section of the **Admin** panel lists all user accounts on your Looker instance.
## Viewing and searching users
The **Users** page shows the following information:
  1. Tabs group your users by type:
     * The **Standard Users** tab shows users who sign in to Looker directly, through either the regular authentication process or through the Looker API.
     * The **Embed Users** tab shows signed embed users who are authenticated through a third-party application.
     * The **Looker Support** tab shows Looker Support analysts who were granted access to your Looker instance.
  2. The **Filter List** field limits which users are shown. You can filter on user ID, name, or email address. To filter on user ID, enter a user ID to display that user. For name and email address, when you enter any string, the list of users displayed shows all users whose name or email address contains the string entered in the filter field. The **Filter List** replaces the search function on the previous version of the **Users** page.
  3. Clicking the **User** column heading sorts the table by username in ascending or descending order.
  4. Each row lists the user's name, ID, and email address, and it includes an icon that indicates the type of access the user has. Hold your cursor over the icon to see what the icon represents.
Click the row to edit the user. Users who cannot be edited are indicated by a lock on the user icon. These users are either system created (such as members of the All Users group) or externally managed by the LDAP, SAML, or OpenID Connect protocol.
  5. The **Active Credential** column lists the types of access that the user has to your Looker instance.
  6. The **Group** column lists all groups to which the user belongs.
  7. The **Role** column lists all roles assigned to the user.
  8. You click the **Add Users** button to create new users.
  9. You click the three-dot **Options** menu to disable the user, sudo as the user, or delete the user.
> Deleting a user is irreversible. Consider your organization's compliance and security needs before doing so.


## Adding users
To add a user, click the **Add Users** button.
In the **Adding a new user** page, type or paste a comma-separated list of email addresses, and select the groups and roles that will be assigned to each. To view the list of groups, start typing into the **Groups** field; all group names that include that text appear. Click the **Save** button to create the users and, if you've selected the **Send setup emails** checkbox, to send sign-up emails.
## Editing users
To edit a user, click the user's row. On the **Edit User** page, adjust the following settings as needed.
### Account
Enable or disable a user's account. Consider disabling the user account instead of deleting it.
### First Name
Add or edit the user's first name, if applicable. This field does not require a value, but it can be useful for organizational purposes.
### Last Name
Add or edit the user's last name, if applicable. This field does not require a value, but it can be useful for organizational purposes.
### Email
Add or edit the user's email address. When the user logs in to Looker, the email address serves as their username.
### Locale
The **Locale** field sets the user-interface language and model locale for a user.
If you want the user to view certain user interface (UI) text in a specific language, Looker supports the UI translations that are shown in the following table. Enter the code in the **Locale** field.
If you want the user to view a localized version of one or more data models, enter the title of the model's strings file for that locale in the **Locale** field.
If you want the user to view _both_ model localization and Looker's built-in UI translations, the model's strings file should have the same name as the appropriate locale code in the following table; and that code should be entered in the **Locale** field.
To confirm the **Locale** setting, click **Save** at the bottom of the page.
Language | Locale Code and Strings Filename  
---|---  
English  
Czech | `cs_CZ`  
German | `de_DE`  
Spanish (Spain) | `es_ES`  
Finnish | `fi_FI`  
French (France) | `fr_FR`  
Hindi | `hi_IN`  
Italian | `it_IT`  
Japanese | `ja_JP`  
Korean | `ko_KR`  
Lithuanian | `lt_LT`  
Norwegian (Bokmål) | `nb_NO`  
Dutch | `nl_NL`  
Polish | `pl_PL`  
Brazilian Portuguese | `pt_BR`  
Portuguese | `pt_PT`  
Russian | `ru_RU`  
Swedish | `sv_SE`  
Thai | `th_TH`  
Turkish | `tr_TR`  
Ukrainian | `uk_UA`  
Simplified Chinese | `zh_CN`  
Traditional Chinese | `zh_TW`  
For users with no **Locale** set, Looker uses the locale chosen on the **Localization** page of the **Admin** panel as the default locale; and, if no locale is set there, Looker defaults to `en`.
#### Setting a custom locale
Looker developers can create custom locales to use for model localization only. Custom locale codes are designated by the titles of the string files that are created in the model localization process. To apply that custom locale to users, perform these steps:
  1. Enter the custom locale code in the **Locale** field. As you begin typing in the field, any pre-existing text disappears.
  2. Click **Create "your_custom_locale_code"**.
  3. Click **Save** at the bottom of the page. The code will be added to the user's locale drop-down menu.


The Looker UI does not support custom locales. If you use a custom locale in a user's **Locale** field, that user's UI defaults to the language that is set in the instance locale.
### Number format
Looker's default number format setting for numbers that appear in data tables and visualizations is **1,234.56**. However, the number format can be set to any of the following:
  * **1,234.56** : Thousands separated with commas; decimals separated with a period
  * **1.234,56** : Thousands separated with periods; decimals separated with a comma
  * **1 234,56** : Thousands separated with spaces; decimals separated with a comma


For more information and examples of using the **Number format** setting, see the Localizing number formatting documentation page.
### Timezone
If you've enabled User Specific Time Zones on your Looker instance, you can select the time zone that will be used when this user runs a query in Looker.
### Send setup link / Send reset link
If the user has never logged in, this button is labeled **Send setup link**. If the user has logged in previously, this button is labeled **Send reset link**. If you need to set or reset a password, you can click this button to send a link to the user's email address that you previously specified. See the Password requirements documentation page to learn about specifying password complexity requirements in Looker. If the user does not reset their password within one hour, the password's reset link will expire.
### Two-Factor Secret
This option appears if you have enabled two-factor authentication (2FA) on your instance. Click the **Reset** button to reset 2FA for the user. This causes Looker to prompt the user to rescan a QR code with the Google Authenticator app the next time they attempt to sign in to the Looker instance.
### API Keys
An API key is used to access the Looker API. API keys are created by Looker and consist of a client ID and a client secret. Looker requires an API key to execute commands with the Looker API.
To generate API keys, click the **Edit Keys** button. The **Edit User API keys** page opens and shows the existing API keys. Click the **New API key** button to generate a new key.
The API keys have the same permissions as the user account from which they were created.
It is best practice to create dedicated user accounts for API scripts — one user account for each script. That way, you can configure a user account with the specific set of permissions that allows the script to perform its function and _only_ its function. For example, for an API script that runs queries, you can create a user account with the `access_data` permission, but no other permissions.
Dedicated user accounts for API scripts let you increase security by compartmentalizing a script's access. Also, if you ever need to stop a script, you can disable (or delete) that script's user account. Be sure to read the Removing user access section on this page before you delete any user account.
### Groups
Lists the groups the user is a member of. You can add the user to a new group by selecting the group from the drop-down, or remove the user from a group by clicking the `X` next to the group name in the list.
Users can also be added to groups on the **Groups** page in the **Admin** panel.
### Roles
Lists the roles assigned to the user. You can add a new role to the user by selecting the role from the drop-down, or remove a role from the user by clicking the `X` next to the role name in the list.
Roles can also be added on the **Roles** admin page.
### User attributes
Sets and unsets the values of a user's user attributes. Values that are assigned to an individual user always override any values that are assigned as a result of membership in a group. System settings are not editable.
## Removing user access
To remove a user's access to Looker, you can either disable or delete their account. For most situations, the best practice is to disable the account.
Differences between disabling and deleting a user account are described in the following table:
Description | Disabled | Deleted  
---|---|---  
The user can sign in to the Looker instance | No | No  
The user's personal folder | Still exists | Deleted  
Looks and dashboards in the user's personal folder | Still exist | Moved to the Trash folder  
Looks and dashboards the user saved to a Shared folder | Still exist in the Shared folder | Still exist in the Shared folder  
Schedules created by the user | Schedules are disabled | Schedules are deleted  
Schedules based on the user's content, but created by another user | Schedules continue to run | User's content is deleted; schedules based on that content are deleted  
Schedules that list the user as a recipient and are created by another user with the ability to deliver content to external email accounts | Schedules will continue to run and deliver normally (user will be treated as an external user) | Schedules continue to run and deliver normally (user will be treated as an external user)  
Schedules that have **Run schedule as recipient** enabled and list the user as a recipient | Schedules will continue to run but will fail to deliver to the disabled user upon next run | Schedules continue to run but will fail to deliver to all users with error `run_as_recipient was specified on ScheduledPlan but recipient is not a Looker user`  
Boards created by the user | Still exist | Still exist  
Alerts created by the user | Remain active, but are not visible or editable from the dashboard on which the alert is set unless self-assigned by an admin. Admins can edit or self-assign the alert from the **Alerts** management admin page in the **Admin** panel. | Alerts are deleted immediately from dashboards and from the **Alerts** management admin page in the **Admin** panel.  
Historical usage information for the user | Kept | Most are deleted  
### Disabling users
To prevent user access to Looker, it is typically best practice to disable the user account. When you disable a user account, the user's usage history and personal content is retained. For details about the differences between disabling and deleting users, see the table in the Removing user access section on this page.
If you are using a Looker (Google Cloud core) instance, disabling a user won't affect that user's IAM permissions. Remove Looker IAM permissions to ensure a user can't access the instance.
To disable a user account, select **Disable user** from the three-dot **Options** menu to the right of the user's row.
### Deleting users
Instead of deleting a user, consider disabling the user account instead. This prevents a user from being able to sign in, but their information, content, and history remain intact. For details about the differences between disabling and deleting users, see the table in the Removing user access section on this page.
If you are using a Looker (Google Cloud core) instance, deleting a user won't affect that user's IAM permissions. Remove Looker IAM permissions to ensure a user can't access the instance.
To delete a user account, select **Delete User** from the three-dot **Options** menu to the right of the user's row.
## Impersonating (sudoing) users
Sudoing lets you navigate Looker as if you were a different user, with all of their privileges and abilities.
Sudoing is also a useful way to validate that you've properly configured permissions and other features or to view a user's LookML development before they've committed and pushed changes.
The `see_users` and `sudo` permissions are both required to sudo as another user. Admins can sudo as any other user, including other admins. Non-admin users can only sudo as other non-admin users.
To sudo as a user, select **Sudo as this user** from the three-dot **Options** menu to the right of the user's row:
A bar at the top of the screen warns you that you're in a sudoed state. That lets you exit the sudoed state. Any changes made in this state will impact the user that you're emulating.
If you are in Development Mode, your changes are not visible to other users until you deploy your changes to production. If you haven't deployed your changes for other users to see, you won't see your changes when you sudo as a different user.
> Sudoing as a signed embed user and interacting with a Looker instance directly and not through an embedded iframe can cause unexpected results. In addition to any restrictions from their regular permissions, signed embed users are restricted by the embedded iframe. However, those restrictions may not be present when someone is sudoing as a signed embed user and interacts outside of an iframe.
> For database connections that use OAuth, such as Snowflake and Google BigQuery, an admin who is sudoing as another user will use the sudoed user's OAuth access token when they run queries. For Snowflake connections, if the user's access token is expired, the admin cannot create a new token on behalf of the sudoed user; the user must sign in to Snowflake and reauthorize Looker.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


