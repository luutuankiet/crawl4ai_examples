# Following alerts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/following-alerts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Following alerts
  * Unfollowing alerts
  * Alerts that are not eligible for following
    * Following and Slack alerts
  * Viewing alerts from the Manage Alerts user page




Was this helpful?
Send feedback 
#  Following alerts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Following alerts
  * Unfollowing alerts
  * Alerts that are not eligible for following
    * Following and Slack alerts
  * Viewing alerts from the Manage Alerts user page


If you have the appropriate user permissions, you can "follow" an alert so that you receive an email notification when its conditions are triggered. You automatically follow any email alert on which you are listed as a recipient.
## Following alerts
To follow another user's alert, click the alert bell icon to open the list of alerts, and click the **Follow** button next to the alert you want to receive a notification for.
Some alerts cannot be followed, including:
  * Alerts marked **Private** by their creators
  * Alerts that have settings that cannot be exposed for security reasons
  * Alerts to the Slack or Slack Attachment (API Token) integrations


## Unfollowing alerts
To stop receiving notifications when the alert is triggered, click the **Unfollow** button next to the alert in the alert view window. You can also unsubscribe directly from the alert notification by clicking **Unfollow this alert** at the bottom of your alert email.
> If you unfollow an alert that uses an email notification, you'll be removed from its recipient list. You can still view the alert from the list of alerts on a tile; or, if you created the alert, you can view its information on the **Manage Alerts** user page.
## Alerts that are not eligible for following
Some types of alerts cannot be viewed or followed by other users for security purposes. When you create these alerts, you won't be able to view or set the alert permissions. An alert does not permit following if it meets one or more of these conditions:
  * The alert is based on any models with database connection strings that contain user attributes.
  * The alert is based on an Explore, a Look, a dashboard, or a LookML dashboard that uses filters that are based on user attributes.
  * The alert is based on any models with access grants.


> If you create a **Public** alert based on a model that does not meet any of these conditions and you later update the model or filter so that the alert does meet one or more of these conditions, then the alert remains **Public** and users may still follow it.
### Following and Slack alerts
Alerts to the Slack and Slack Attachment (API Token) integrations cannot be followed by default, and the **Follow** button next to the alert will be disabled. However, users with permissions to create alerts and access to the specific Slack channels in the alert settings can duplicate Slack alerts that are marked **Public**.
## Viewing alerts from the Manage Alerts user page
You can view additional details and history information about alerts you are following that are set on dashboard tiles from the **Alert Details** page, available on the **Manage Alerts** user page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


