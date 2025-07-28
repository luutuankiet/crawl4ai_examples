# Enabling the mobile application  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/mobile-app-enablement

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling the app for your instance
  * Assigning mobile app access to specific users
  * Forcing users to authenticate each time they log in to the mobile app
  * Considerations for Looker (Google Cloud core) instances
  * Considerations for customer-hosted instances




Was this helpful?
Send feedback 
#  Enabling the mobile application
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling the app for your instance
  * Assigning mobile app access to specific users
  * Forcing users to authenticate each time they log in to the mobile app
  * Considerations for Looker (Google Cloud core) instances
  * Considerations for customer-hosted instances


The Looker mobile application lets users perform the following functions from a mobile device:
  * View their favorite and recently viewed content
  * Access the boards they follow
  * Navigate to content in folders
  * View Looks and dashboards


Admins can enable the Looker mobile app to let users sign in to their Looker instance on an Android or iOS device.
## Enabling the app for your instance
> When IP allowlists are enabled, users cannot connect to the instance from their service providers' IP addresses.
Access to the Looker mobile app is enabled for your instance by default. To disable or enable access to the mobile app for your instance, follow these steps:
  1. Open the **Settings** page in the **General** section of the **Admin** panel.
  2. In the **Feature Configuration** section of the **General Settings** page, choose **Enabled** or **Disabled** under **Mobile Application Access**.
  3. Select **Update** to apply your changes.


When the app is enabled for your instance, users can install the app and sign in to your instance on their mobile devices.
If you disable the **Mobile Application Access** setting for your instance, any existing mobile app sessions will be invalidated.
## Assigning mobile app access to specific users
Admins can use the `mobile_app_access` permission to grant specific users and groups access to the Looker mobile app. To grant mobile app access to a specific user or group, follow these steps:
  1. Ensure that mobile app access is enabled for your Looker instance.
  2. Assign that user or group a role with a permission set that includes the `mobile_app_access` permission.


Users with the `mobile_app_access` permission can sign in to the Looker mobile app using the same authentication method that they use to sign in to your Looker instance. If a user does not have the `mobile_app_access` permission, Looker displays an error upon trying to sign in to the app.
See the Roles documentation page for information about assigning roles to users or groups.
## Forcing users to authenticate each time they log in to the mobile app
Admins can require users to sign back in to Looker every time they open the mobile app by enabling the **Force mobile authentication** setting in the **General Settings** section of the **Admin** panel. To enable this feature, follow these steps:
  1. Navigate to the **Settings** page in the **General** section of the **Admin** panel.
  2. Under **Force mobile authentication** , select **Enabled**.


When **Force mobile authentication** is enabled, users will be required to sign in to Looker every time they open the app on their mobile devices. Additionally, users will be logged out of the mobile app after 60 minutes of inactivity.
## Considerations for Looker (Google Cloud core) instances
If your instance is a Looker (Google Cloud core) instance that is using private services access or Private Service Connect, your private network must be reachable by the mobile device.
## Considerations for customer-hosted instances
Admins of customer-hosted instances should consider the following requirements when enabling the mobile app for their instance:
  * The web server and API endpoints must be publicly accessible or otherwise reachable by the mobile app. 
    * To test connectivity, try accessing the URL of your Looker instance from a web browser on your mobile device.
  * The API Host URL must have the same hostname as the instance URL and serve traffic on either port 443 or port 19999. The URL should follow this form: `https://<instance_name>.looker.com:<port>`


For additional information, see the Looker API troubleshooting documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


