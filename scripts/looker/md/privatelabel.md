# Admin settings - Private Label  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/privatelabel

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling private label
  * Private Label Admin page
    * Documentation Links
    * Email Subscription Options
    * Custom Document Title
    * Looker Mentions in Scheduled Emails
    * Custom Welcome Email Advanced Settings
    * Looker Mentions in Account Setup
    * Looker Logo in Alerts
    * Looker Links in Alerts
    * Looker Mentions in Folders Pages
  * Additional optional private label features
    * Download PDFs Without Logo
    * Embed Without Logo




Was this helpful?
Send feedback 
#  Admin settings - Private Label
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling private label
  * Private Label Admin page
    * Documentation Links
    * Email Subscription Options
    * Custom Document Title
    * Looker Mentions in Scheduled Emails
    * Custom Welcome Email Advanced Settings
    * Looker Mentions in Account Setup
    * Looker Logo in Alerts
    * Looker Links in Alerts
    * Looker Mentions in Folders Pages
  * Additional optional private label features
    * Download PDFs Without Logo
    * Embed Without Logo


You can customize Looker to remove references to Looker and blend the look and feel of Looker with your branding.
On the **Private Label** admin page, you can configure the following options:
  * Documentation Links
  * Email Subscription Options
  * Custom Favicon
  * Custom Document Title
  * Looker Mentions in Scheduled Emails
  * Custom Welcome Email Advanced Settings
  * Looker Mentions in Account Setup
  * Looker Logo in Alerts
  * Looker Links in Alerts
  * Looker Mentions in Folders Pages


Depending on your pricing plan, you can also customize the following options:
  * Download PDFs Without Logo
  * Embed Without Logo


## Enabling private label
Google Cloud must enable the private label option for your instance. Contact a Google Cloud sales specialist for pricing and additional information.
## Private Label Admin page
In the Looker **Admin** panel, the **Private Label** page lets you load custom logos and customize how certain links to Looker are shown or hidden.
### Documentation Links
**Documentation Links** lets you show or hide the following links to Looker's documentation:
  * The **Docs** and **User Guide** options in the **Help** menu:
  * The **Help + Syntax Reference** link in the **Custom Filters** panel:
  * The question mark icon in the **matches (advanced)** option in the **Filters** panel:
  * The question mark icon next to the custom format field in the **Series** tab of a table visualization:


### Email Subscription Options
Typically, there is a link on the Account page where a user can manage their email subscriptions. Your selection in **Email Subscription Options** determines whether or not that link is shown on the Account page.
### Help Menu
The **Help Menu** setting lets you show or hide the **Help** menu on the main menu bar:
### Custom Favicon
Toggle this switch on to upload a custom favicon. Looker displays the favicon in browser tabs and windows:
After you toggle the switch on, Looker displays buttons to let you choose your favicon file and upload it. The favicon must be in ICO, PNG, or GIF file format, and must be one of the following sizes:
  * 16 x 16 pixels
  * 32 x 32 pixels
  * 48 x 48 pixels
  * 64 x 64 pixels


### Custom Logo
Toggle this switch on to upload a custom logo.
Looker displays two versions of the logo. The first is small, rendered at 75 by 32 pixels, in the menu bar:
The second is large, rendered at 210 by 90 pixels, that appears on various pages in the product, including:
  * User login
  * Password reset
  * User account setup
  * Email unsubscribe
  * Download a dashboard as a PDF


After you toggle the switch on, Looker displays buttons to let you choose and upload your file icon. The logo must be in ICO, PNG, or GIF file format, and 500 KB or smaller.
### Custom Document Title
Enable this option to enter a custom document title. Looker displays the document title in the browser tabs and windows:
The document title usually shows a user's location within the Looker application, but Looker will display the custom document title when there is not an available specific document title.
### Looker Mentions in Scheduled Emails
By default, deliveries of Looks, dashboards, and LookML dashboards to email include a link that reads **View full report** or **View full dashboard** :
This link lets the email recipients connect to your Looker instance and further explore the data delivered in the email. Disabling the **Looker Mentions in Scheduled Emails** option replaces this text with **View full dashboard**.
To remove the link altogether, see the **Emailed Data Policy** options on the **Scheduled Emails** page in the **Admin** panel.
### Custom Welcome Email Advanced Settings
If you have enabled custom welcome emails, you can edit the body text of the emails that new Looker users will receive when they are added to your instance. By default, Looker welcome emails include the subject line "Welcome to Looker" and header text that reads "You've been invited to join Looker!"
If you enable the **Custom Welcome Email Advanced Settings** option, you can also edit the subject line and header text in welcome emails.
The header text and body text support HTML for adding formatting and links.
In addition, when you enable this option, the **Activate Your Account** button that is included in welcome emails is colored gray instead of purple.
### Looker Mentions in Account Setup
By default, new users activating their Looker account with email and password authentication will see references to Looker in the welcome message on the account setup page:
They will also see "Welcome to Looker" in the browser tab:
To remove the reference to Looker in the welcome message and browser tab, switch on the **Looker Mentions in Account Setup** option. When this is enabled, the new user will only see "Welcome" on the page:
The user will also only see "Welcome" on the browser tab:
If **Custom Logo** is also enabled, the Looker logo will be replaced with the specified logo image file. With both features enabled, a new user will see the following on the account setup page:
If **Custom Favicon** is also enabled, the Looker logo will be replaced with the specified icon image file on the account setup page browser tab:
### Looker Logo in Alerts
By default, alert notification emails include the Looker logo:
To remove the Looker logo from alert notification emails, switch on **Looker Logo in Alerts**. Recipients will then see whitespace instead of the Looker logo:
Use **Looker Logo in Alerts** together with **Looker Links in Alerts** to further customize the appearance of alert notification emails.
### Looker Links in Alerts
By default, alert notification emails include the following links:
  1. A purple **Go to Content** button that links back to the Looker content on which the alert is set.
  2. An **Unfollow this alert** link that removes the recipient from the alert subscription.
  3. An **Edit this alert** link that links back to the Looker content on which the alert is set.


The **Looker Links in Alerts** feature lets you remove the links from alert notification emails. To remove links back to Looker in alert notification emails, switch on **Looker Links in Alerts**. The purple **Go to Content** button will no longer appear, and the bottom two links will be replaced with instructions for navigating to the content in Looker to modify or disable the alert:
When **Looker Links in Alerts** is enabled along with **Looker Logo in Alerts**, recipients will only see the alert information and instructions to navigate to the content in Looker to modify or disable the alert:
### Looker Mentions in Folders Pages
By default, a user sees a message reading **Welcome to Looker!** in the folder when there is no content saved in their personal folder.
To remove the reference to Looker, switch on **Looker Mentions in Folders Pages**. When this is enabled, users will only see **Welcome!** in their empty personal folder:
## Additional optional private label features
There are two additional private label features that allow you to further customize PDF downloads and embedded content. Looker must enable these features for your instance. Contact a Google Cloud sales specialist for pricing and additional information.
### Download PDFs Without Logo
By default, generated PDFs include a footnote that reads **Generated by Looker on`<TIMESTAMP>`** :
When **Download PDFs Without Logo** is enabled for your instance, the footnote instead reads **Generated on`<TIMESTAMP>`** :
### Embed Without Logo
By default, content embedded in an iFrame includes a footer that reads **Powered by Looker**.
When **Embed without Logo** is enabled for your instance, the footer is removed.
For more embedded content customization options, see the **Remove Look Navigation** feature on the **Embed** page in the **Admin** panel.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


