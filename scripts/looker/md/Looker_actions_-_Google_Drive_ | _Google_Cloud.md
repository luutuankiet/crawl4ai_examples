# Looker actions - Google Drive  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-use-the-google-drive-integration

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling the Google Drive action in Looker
  * Delivering data to a Google Drive folder
  * Switching Google Accounts




Was this helpful?
Send feedback 
#  Looker actions - Google Drive
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling the Google Drive action in Looker
  * Delivering data to a Google Drive folder
  * Switching Google Accounts


> Customer-hosted instances may be unable to enable actions from the Looker Action Hub, especially actions that support streamed results or that use OAuth, if the customer-hosted Looker instance does not fulfill the Looker Action Hub requirements.
> See the Sharing data through an action hub documentation page for suggested solutions to this potential issue.
You can use Looker's secure OAuth-based Google Drive action to send Looks, Explores, and dashboards from Looker to Google Drive on a one-off or recurring basis. The Google Drive action is integrated with Looker through the Looker Action Hub. Once the Looker admin has enabled the Google Drive action in the Action Hub, users can select Google Drive as a possible destination when sending or scheduling Looks, Explores, and dashboards. 
Since the Google Drive action leverages Google OAuth, users will be able to deliver content only to the Drive folders that their Google credentials enable them to access. The Google Drive action enables users to connect their Google Drive to Looker using Google OAuth 2.0 so that they can store files in their Google Drive folders. 
This page walks admins through enabling the Google Drive action. It also describes how any user who has the appropriate permissions can send or schedule data deliveries to a Google Drive folder. 
## Enabling the Google Drive action in Looker
Looker admins can enable the Google Drive action in Looker with the following steps: 
  1. Go the **Admin** panel and, under **Platform** , go to the **Actions** page. 
  2. On the list of Action Hub actions, scroll to Google Drive and click the **Enable** button. 
  3. On the Google Drive action page, click the **Enabled** toggle to the on position, and click **Save**. 
  4. When you return to the list of Action Hub actions, your Google Drive action should be enabled. 


You and your users — if they have `send_to_integration` permissions — can now send or schedule Looks, Explores, and dashboards to a Google Drive folder. 
## Delivering data to a Google Drive folder
Any Looker user who has `send_to_integration` permissions can send or schedule Looks, Explores, or dashboards to a Google Drive folder. 
Your format options to send and schedule dashboards include the following: 
  * PDF
  * Visualization
  * CSV (ZIP file) — if delivering a ZIP file, each tile on your dashboard will be delivered as a separate CSV file. You can extract the file in the Cloud with a Chrome extension, or you can extract it from your Drive. 


Your format options to send and schedule Looks or Explores include the following: 
  * CSV
  * XLSX
  * JSON — Simple
  * JSON — Label
  * JSON — Simple, Inline
  * JSON — Detailed, Inline
  * Text
  * HTML

To send or schedule your content, follow these steps: 
  1. From the Scheduler, next to **Where should this data go?** , select **Google Drive** as your delivery destination. 
  2. If you're delivering to Google Drive for the first time, you'll need to authenticate with your Google credentials. Click **Sign in with Google** , specify your Google Account, and then click **Allow** to connect your Looker account to your Google OAuth credentials. You can connect only one set of Google OAuth 2.0 credentials to this integration.
  3. In the Scheduler, click **Verify credentials** to load your Google Drive. 
  4. From the **Select Drive to save file** drop-down, choose the Google Drive where your file will be saved.
Next, you can either enter the URL for a folder in this Drive or fetch all folders in your Drive.
     * In the **Google Drive Destination URL** field, enter the full Google Drive URL of the folder where you want to save your data. For example: `https://drive.google.com/corp/drive/folders/abcxyz`. If this URL isn't accessible, your data will be saved to the root folder of your Google Drive. 
     * From the **Select Fetch to fetch a list of folders in this drive** drop-down, select **Fetch**. After the Scheduler dialog refreshes, from the **Select folder to save file** drop-down, select the Google Drive folder where your file will be saved. 
  5. Specify the name of your file in the **Enter a filename** field. You don't need to include the file extension — the action will automatically append it during delivery. 
  6. Advanced options for customizing your content delivery depend on the data format. Click **Send** or **Schedule**. 
  7. Refresh your Google Drive folder to see your file delivery.


> Your files won't be overwritten or renamed during subsequent deliveries of files with the same filename, so if you have scheduled content for repeated delivery, your Drive folder will contain multiple files of the same name. 
## Switching Google Accounts
To associate a different Google Account with this action, you must delete the account's connection to the Looker instance. To learn more, see Manage connections between your Google Account and third-parties.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


