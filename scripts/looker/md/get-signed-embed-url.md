# Getting a signed embed URL  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/get-signed-embed-url

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Getting a signed embed URL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
To generate a signed embed URL, select the **Get embed URL** option from the three-dot dashboard menu on a dashboard, or from the Explore actions gear menu on a Look or Explore, and then click the **Signed Embed** tab.
  1. The **Content URL** field shows the full content URL, including the `/embed` path.
  2. The **Apply theme to dashboard/explore/look URL** field lets you select a theme to be added to the embed URL if you are generating a dashboard, an Explore, or a Look embed URL and your instance has custom themes enabled. The theme will be applied when the embedded dashboard or Explore is viewed.
  3. The **Include current params in URL** switch lets you choose whether to apply current parameters, such as filter values, to the embed URL. If enabled, those parameters will be applied when the embedded content is viewed.
  4. Enter a unique identifier for the user. You can assign the user any string, as long as it is unique. See the `external_user_id` parameter definition for more information.
  5. Optional: Enter the user's first name and last name. If one or both of these fields are left blank, they will retain the value from the last request. If no value has ever been set, each field will be assigned the value "Embed".
  6. Optional: Enter an **External Group ID**. This is a unique identifier for the group that the user belongs to in the application that is embedding Looker. Users who have permission to save content, and share an external group ID, will be able to save and edit content in a shared Looker folder called "Group". An external group ID is the only available method for creating external groups of embed users. There is no way to configure external embed user groups from within the Looker UI.
  7. The model on which the dashboard, Look, or Explore is based is listed in the **Models** field. The user will be granted access to that model. To grant the user access to additional models, from the **Search Models** drop-down field, click the **Models** field to expand it, and then select the additional models to which you want to grant the user access.
  8. The minimum permissions that are required by the user to view the embedded content will be selected by default. To grant the user additional permissions, click the **Permissions** field to expand it, and then select any additional permissions that you want to grant to the user.
  9. To grant the user one or more user attributes, click **Add Row**. Select the user attribute that you want the user to have in the **Key** drop-down field, and then enter the user's value for that user attribute in the **Value** field. You can add additional user attributes by clicking **Add Row** , or you can remove a user attribute by clicking the trash can icon. You cannot add multiple user attributes with the same **Key** value.
  10. In the **Session Length** field, enter the number of seconds that can elapse before the signed embed URL session should be invalidated.
  11. To return all values to default settings, click **Clear Form**. All values will also reset if you navigate away from the **Get Embed URL** window.
  12. Click **Generate URL**.


Using the parameters that you specified, Looker will generate a signed embed URL, a signed SDK call, and a signed embed SDK call.
  * To copy the generated signed embed URL to the clipboard, click **Copy Link**.
  * You can view either the SDK call or the embed SDK call by clicking **View Code** , which will open a code window.
  * From within the code window, to copy the generated SDK call or Embed SDK call results to your clipboard, click **Copy to Clipboard**.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


