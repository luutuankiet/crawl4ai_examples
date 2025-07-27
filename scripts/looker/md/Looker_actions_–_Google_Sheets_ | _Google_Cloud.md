# Looker actions – Google Sheets  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-use-the-google-sheets-integration

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling the Google Sheets action in Looker
  * Delivering data in CSV format to a Google Sheet
  * Switching Google Accounts




Was this helpful?
Send feedback 
#  Looker actions – Google Sheets
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling the Google Sheets action in Looker
  * Delivering data in CSV format to a Google Sheet
  * Switching Google Accounts


> Customer-hosted instances may be unable to enable actions from the Looker Action Hub, especially actions that support streamed results or that use OAuth, if the customer-hosted Looker instance does not fulfill the Looker Action Hub requirements.
> See the Sharing data through an action hub documentation page for suggested solutions to this potential issue.
Does your work require you to spend a lot of time in Google Sheets? You can use Looker's secure, OAuth-based action to send CSVs directly from Looker to Google Sheets on a one-off or recurring basis. 
The Google Sheets action is integrated with Looker through the Looker Action Hub. Once the Looker admin has enabled the Google Sheets action in the Action Hub, users can select Google Sheets as a possible destination when sending or scheduling Looks or Explores. 
This page walks admins through enabling the Google Sheets action in Looker. It also describes how any user who has the appropriate permissions can send or schedule deliveries in CSV format to a Google Sheet. 
## Enabling the Google Sheets action in Looker
Looker admins can enable the Google Sheets action in Looker with the following steps:
  1. Go the **Admin** panel and, under **Platform** , go to the **Actions** page. 
  2. On the list of Action Hub actions, scroll to Google Sheets and click the **Enable** button. 
  3. On the **Google Sheets** action page, click the **Enabled** toggle to the on position, and click **Save**. 
  4. When you return to the list of Action Hub actions, your Google Sheets action should be enabled. 


You and your users — if they have `send_to_integration` permissions — can now send or schedule Looks or Explores in CSV format to a Google Sheet. 
## Delivering data in CSV format to a Google Sheet
Any Looker user who has `send_to_integration` permissions can send or schedule Looks or Explores in CSV format to a Google Sheet. 
> Google Sheets are limited to 10 million cells for the entire Sheet. If your data table has columns, rows, or tabs that exceed this limit, any deliveries to the Google Sheet integration will fail.
To prepare your data before sending or scheduling it, follow these steps:
  * **Horizontal scaling:** If your data table contains more than 26 columns and you plan to import the data to an existing Google Sheet, you'll need to manually expand the Google Sheet before you can import your data into it. 
  * **Vertical scaling:** If your data table contains more than 1,000 rows, Looker will add those rows to your Google Sheet by default. 
  * **Overwriting:** If you're going to import your data into an existing Google Sheet, write any formulas on a separate tab of your Google Sheet to preserve the logic in your formulas. If you use the Google Sheets action's overwrite function, the action dynamically updates your Google Sheet, and your data will automatically be loaded into the first or leftmost tab of your Google Sheet. If you'd prefer to create a new spreadsheet with each data delivery so that you have a full history of your data and can track changes over time, don't use the Google Sheets action's overwrite function. 


To send or schedule your content, follow these steps: 
  1. From the Scheduler, next to **Where should this data go?** , select **Google Sheets** as your delivery destination. 
  2. If you're delivering to Google Drive for the first time, you'll need to authenticate with your Google credentials. Click **Sign in with Google** , specify your Google Account, and then click **Allow** to connect your Looker account to your Google OAuth credentials. You can connect only one set of Google OAuth 2.0 credentials to this integration.
  3. In the Scheduler, click **Verify credentials** to load your Google Drive. 
  4. From the **Select Drive to save file** drop-down, choose the Google Drive where your CSV file will be saved.
Next, you can either enter the URL for a folder in this Drive or fetch all folders in your Drive.
     * In the **Google Drive Destination URL** field, enter the full Google Drive URL of the folder where you want to save your data. For example: `https://drive.google.com/corp/drive/folders/abcxyz`. If this URL isn't accessible, your data will be saved to the root folder of your Google Drive. 
     * From the **Select Fetch to fetch a list of folders in this drive** drop-down, select **Fetch**. After the Scheduler dialog refreshes, from the **Select folder to save file** drop-down, select the Google Drive folder where your CSV file will be saved. 
  5. Specify the name of your Google Sheet file in the **Enter a filename** field. You don't need to include the file extension — the Google Sheets action will automatically append it during delivery. 
  6. In the **Overwrite Existing Files** drop-down, select **Yes** or **No**. Selecting **No** will generate a new Google Sheet with a snapshot of your data with every data delivery. Selecting **Yes** will load your data in the first or leftmost tab of your existing Google Sheet. 
> Because of Google Sheets cell limits, if you choose the overwrite option, keep in mind that the tabs that are added during each delivery cannot cause the Sheet to exceed the 10 million cell limit. Once the cell limit is exceeded, subsequent schedules will fail.
  7. Advanced options for CSVs include customizable limit and format. Click **Send** or **Schedule**. 
  8. Refresh your Google Drive folder to see your file delivery.


## Switching Google Accounts
To associate a different Google Account with this action, you must delete the account's connection to the Looker instance. To learn more, see Manage connections between your Google Account and third-parties.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


