# Admin settings - Embed  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-embed

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Embedded Domain Allowlist
  * Same-Origin Protections for Looker Login Pages
  * Embed SSO Authentication
  * Alerts and scheduling custom url
    * Embed domain for schedules and alerts allowlist
    * Select content path
  * Show Filters on Embedded Looks
  * Remove Look Navigation
    * Removing Look navigation from embedded Explores
    * Removing Look navigation from embedded dashboards
  * Dashboard Embed Content Navigation
  * Embed Content Management
  * Cookieless Embed
  * Embed JWT Secret
  * Embed URI Validator




Was this helpful?
Send feedback 
#  Admin settings - Embed
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Embedded Domain Allowlist
  * Same-Origin Protections for Looker Login Pages
  * Embed SSO Authentication
  * Alerts and scheduling custom url
    * Embed domain for schedules and alerts allowlist
    * Select content path
  * Show Filters on Embedded Looks
  * Remove Look Navigation
    * Removing Look navigation from embedded Explores
    * Removing Look navigation from embedded dashboards
  * Dashboard Embed Content Navigation
  * Embed Content Management
  * Cookieless Embed
  * Embed JWT Secret
  * Embed URI Validator


The **Embed** page in the **Platform** section of the **Admin** menu lets you configure settings for embedded Looker content.
## Embedded Domain Allowlist
You need to use this setting to make use of JavaScript events to pass data or actions between a parent page and a Looker iframe.
In that case, add the domain where the iframe is being used to this field, and then select **Update**.
## Same-Origin Protections for Looker Login Pages
For the Looker login page, you can use the **Same-Origin Protections for Looker Login Pages** setting to indicate whether or not you want to allow cross-origin embedding:
  * **Disabled** : Looker allows cross-origin embedding.
  * **Enabled** : Looker doesn't allow cross-origin embedding.


For certain use cases, you must allow Looker login pages to appear within a Looker iframe even when the parent page is not compatible with the Looker instance's domain name. In these cases, you need to have the **Same-Origin Protections for Looker Login Pages** option set to **Disabled** :
  * If you use private embedding of Looker content in an iframe of a web page hosted by a non-Looker domain, you need to disable **Same-Origin Protections for Looker Login Pages** so that Looker can display the login page in the iframe and allow users to log into Looker.


Set **Same-Origin Protections for Looker Login Pages** to **Enabled** if either of the following is true:
  * You don't embed any Looker content.
  * You use only signed embedding, since the Looker login page isn't used for signed embeds.


To change the setting for same-origin protection, use the pull-down menu to select your desired option, and then be sure to select the **Update** button to save your selection.
## Embed SSO Authentication
The **Embed SSO Authentication** feature needs to be enabled if you want to make use of Looker's Signed embedding feature. To do so, select **Enabled** and then select **Update**.
## Alerts and scheduling custom url
Unless disabled, email deliveries from embedded dashboards, either from alerts or scheduled deliveries, include a link that reads **View full dashboard**. This link lets the email recipients connect to their Looker instance and further explore the data delivered in the email.
The **Alerts and scheduling custom url** option lets you configure a custom URL in alerts and scheduled email deliveries that will link embed users to the embedding application, rather than a Looker instance.
### Embed domain for schedules and alerts allowlist
Specify all domains that custom URLs in email deliveries may link to. The domains listed here will populate the **Domain** field in the scheduling and alerts dialogs.
If this field is left blank, custom links are unavailable, since there will be no domain for a user to select in the schedule or alerts dialog.
### Select content path
This drop-down lets you select how the URL in the custom link is formatted. It has the following options:
  * **Only embed domain** — The URL in the custom link includes only the domain selected in the **Domain** field in the scheduling or alerts dialog. For example, `app.customer.com`.
  * **User defined url** — The URL in the custom link includes the domain that is selected in the **Domain** field in the scheduling or alerts dialog and the path that is entered by the user in the **Path** field in the scheduling or alerts dialog. For example, `app.customer.com/my_embed_app`.
  * **Embed domain URL with Looker IDs** — The URL in the custom link will include the domain that is selected in the **Domain** field in the scheduling or alerts dialog and the Looker path to the embedded dashboard, using the content ID. For example, `app.customer.com/dashboards/12`.
  * **Embed domain URL with Looker slugs** — The URL in the custom link includes the domain that is selected in the **Domain** field in the scheduling or alerts dialog and the Looker path to the embedded dashboard, using the content slug. For example, `app.customer.com/dashboards/CQ1fu99Z9Y1ggq2wcHDfMm`.


**Select content path** is not available if the **Embed domain for schedules and alerts allowlist** field is left blank.
### URL label
Use this field to enter new default link text, which will replace the text **View full dashboard** in email deliveries. The default text can be changed in the scheduling and alerts dialogs.
## Show Filters on Embedded Looks
Set this option to **Enabled** if you want to display filter values in embedded Looks.
Set this option to **Disabled** to hide filter values in embedded Looks.
Select **Update** to save your setting.
## Remove Look Navigation
The **Remove Look Navigation** feature lets admins further customize embedded content, specifically embedded Explores and embedded dashboards.
### Removing Look navigation from embedded Explores
By default, embed users who have the `explore` and `save_content` permissions will see the following options in the **Explore Actions** gear menu of an embedded Explore:
  * The option to **Save as a Look**
  * The **Save & Schedule** option (for embed users who have the send or scheduling permissions)


When set to **Enabled** , the **Remove Look Navigation** feature removes all references to Looks, including the options **Save as a Look** and **Save & Schedule**, from the embedded Explore's **Explore Actions** gear menu.
Leave the option set to **Disabled** to keep references to Looks and the options **Save as a Look** and **Save & Schedule** in embedded Explores.
### Removing Look navigation from embedded dashboards
When **Remove Look Navigation** is **Enabled** , references and navigation options to Looks from embedded Explores and embedded Look-linked dashboard tiles will be removed.
When **Remove Look Navigation** is **Disabled** , embed users will have the option to **View Look** in the three-dot **Tile actions** menu in Look-linked tiles.
## Dashboard Embed Content Navigation
When this option is enabled, embedded dashboard viewers who have been granted the necessary permissions can view folders and the Looks and dashboards that they contain from embedded dashboards. Enabling this feature is required to let viewers of embedded dashboards copy, move, and delete dashboards.
## Embed Content Management
When this option is enabled, embedded dashboard viewers who have been granted the necessary permissions can copy, move, and delete dashboards.
## Cookieless Embed
Starting in Looker 23.8, the embed domain can be included when the cookieless session is acquired. This is an alternative to adding the embed domain using the Looker **Admin > Embed** panel. Looker saves the embed domain in the Looker internal database, so it won't be shown on the **Embed** page in the **Admin** panel. Instead, the embed domain is associated with the cookieless session and exists for the duration of the session only. Review the security best practices if you decide to take advantage of this feature.
## Embed JWT Secret
A JSON Web Token (JWT) secret is required to make use of the cookieless embed feature. Cookieless embed requires that **Embed SSO Authentication** be enabled, but cookieless embed uses **Embed JWT Secret** instead of **Embed Secret**.
This option lets you set or reset the embed JWT secret. Setting the JWT secret is _not_ necessary, since the very first attempt to create a cookieless embed session will create the JWT token. Unlike the embed secret, the embed JWT secret is never exposed as it is only used internally by the Looker server.
Resetting the JWT token will invalidate _all_ active cookieless embed sessions.
## Embed Secret
An embed secret is needed to make use of Looker's signed embedding feature.
To retrieve the embed secret, select the **Set Secret** button.
To change your secret, select the **Reset Secret** button — you should be aware that this will break any existing signed embeds, however.
## Embed URI Validator
After generating a URL for Looker's signed embedding feature, you can test the URL by pasting it in the **Embed URI Validator** field and clicking **Test URI**. The URI validator will return a message indicating whether the signed embed URL is valid.
After you enter a signed embed URL, the **Embed URI quick check** section will display the parameters and values that are included in the signed embed URL.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


