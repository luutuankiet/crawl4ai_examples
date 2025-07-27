# Google Sheets - Lightdash

**Source:** https://docs.lightdash.com/references/google-sheets

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Integrations
Google Sheets
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Enabling scheduled deliveries
  * Creating a Sync
  * Editing and deleting your Syncs
  * Overview of your Syncs
  * Google API Services User Data Policy


##  Syncs
You can set up as many syncs as you like, and if you make any changes to the content, Lightdash will update the syncs the next time they’re sent.
##  Enabling scheduled deliveries
If you are self-hosting Lightdash, make sure you have the Google Sheets integration configured before you start. See setting up Google Sheets for more information. If you’re using Lightdash Cloud, this is already set up and available for you to use immediately.
##  Creating a Sync
All users with editor access or above can create Syncs. To do this, open your chart in view or edit mode, click the three-dot menu in the top-right corner, then click on `Google Sheets Sync`. The pop-up shows you a list of any existing Syncs for the saved chart, you also have the option to `Create new Sync`. Clicking `Create new Sync` takes you to the configuration screen to setup a new Google Sheets Sync. When you create a Sync, Lightdash also creates a special tab in your Google Sheet called metadata which includes information on when the sheet was last updated and the frequency interval. This allows users to easily understand how often data is refreshed inside their Google Sheet.
If you are uploading data from a chart, the data will be uploaded to the first tab in your selected Google Spreadsheet and it will overwrite all the content.
##  Sync options
  * **Name** : this is the name of your Sync in Lightdash
  * **Frequency** : this is how often your Google Sheet will be synced. You can make this hourly, daily, weekly, monthly, or custom - each frequency has its own options. For example, with a monthly schedule, you set the day of the month and the time that you want your Sync to be happen. The custom frequency lets you write out your own custom Cron expression if you need something more specific than our standard options. All times for the scheduler are in UTC.
  * **Select Google Sheet** : Use the file picker to select the Google Sheet that you’d like to sync your chart results to. Note: You need to sync to an existing Google Sheet, so ensure you have created it before you can select it here.

This is what a Sync looks like when it’s been set up: Once you’ve set up all of your Sync options, you can click `Sync`.
##  Editing and deleting your Syncs
To remove a Sync from a chart, click on the three-dot-menu beside the Sync name. From there, you can choose to `edit` or `delete` it.
##  Overview of your Syncs
Users who have an admin role in your project can access an overview of your Syncs in the Project Settings. In the `Syncs & Scheduled deliveries` overview page, you can see a list of all of your Syncs (along with your Scheduled Deliveries), their most recent delivery status, and a history of all of the previous deliveries in your project. To access the overview page, just head to your Project Settings, then to the `Syncs & Scheduled deliveries` tab. Here, you can also click on the three-dot-menu beside each Sync to edit or delete it. Editing a Sync from the overview page will bring you to the same configuration screen as when you create a new Sync. Deleting a Sync from the overview page will remove it from your chart.
##  Google API Services User Data Policy
Lightdash’s use and transfer of information received from Google APIs adhere to Google API Services User Data Policy, including the Limited Use requirements.
SlackEmbedding quickstart
Assistant
Responses are generated using AI and may contain mistakes.


