# Configuring alerts for Looker users  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/alerts-for-admins

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Configuring alerts for Looker users
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Looker has several user permissions that are associated with alerts. Some permissions determine what the user can do with alerts; others determine what destinations a user can send an alert notification to. See the Roles documentation page for more information about Looker permissions, including dependencies.
Looker user permissions are distinct from the alert setting called **Permissions**, which lets the alert's creator determine whether other users will be able to view and potentially follow the alert.
In addition to the permissions that are described in the following table, users need `see_looks` permissions and `see_user_dashboards` and/or `see_lookml_dashboards` permissions for the models on which the dashboard or LookML dashboard tiles, respectively, are based.
* Users must have permissions to access the alert's underlying content to view or explore from the alert's visualization (in the **Alert Details** page) or to navigate to its dashboard.
* This permission does _not_ grant the ability to create, follow, or delete alerts from the dashboard tile.
Permission | Lets Users | Notes  
---|---|---  
  * See the tile's bell icon: The numeric indicator shows the total number of enabled public alerts on the tile
  * Manage alerts from the **Alerts** management admin page, even private alerts that are created by other users
  * Access the **Alert History** admin page
  * View, follow, edit, self-assign, and disable any alert on the Looker instance 

| The user must be signed in to Slack from Looker to see alerts that send Slack notifications.  
  * Access the **Alerts** management admin page
  * View, follow, edit, self-assign, disable any alert on the Looker instance, even private alerts that are created by other users
  * Access the **Alert History** admin page

  
  * See the tile's bell icon: The numeric indicator shows the sum of any public or private alerts that the user has created and other users' alerts that are marked **Public**
  * From the dashboard tile: create, duplicate, and delete their own alerts; duplicate alerts marked **Public** by other users
  * View, edit, disable, and enable their alerts on the **Manage Alerts** user page

| The user must be signed in to Slack to see alerts that send Slack notifications.  
  * View and follow public, followable alerts on a dashboard tile
  * View the alerts that they have followed or for which they are listed as a recipient from the **Manage Alerts** user page

  
`schedule_look_emails` | Send email notifications | Users must also have `create_alerts` permissions.  
`schedule_external_look_emails` | Send notifications to emails with any domain | Users must also have `create_alerts` permissions.  
Send alert notifications to the Slack or Slack Attachment (API Token) integrations, if enabled for the Looker instance | Users must also have `create_alerts` permissions.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


