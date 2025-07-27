# Alerts - Lightdash

**Source:** https://docs.lightdash.com/guides/how-to-create-alerts

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
Alerts
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
    * Interacting with your dashboards
    * Using the Slack integration
    * Scheduled deliveries
    * Chart Version History
    * Formatting your fields
    * How to promote content
    * Table calculation SQL templates
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
  * Enabling alerts
  * Creating an alert
  * Editing and deleting your alerts
  * Sending to private Slack channels
  * Sending to Microsoft teams
  * 🔗 How to Create a Webhook in Teams


At the scheduled time, Lightdash will run the query and check the results. If the first value in the results set meets the alerting condition, the alert will be sent. This notification will continue to be sent if the condition is true until it is manually disabled or deleted. You can create or select an existing saved chart, add an alert to it, and tell Lightdash when you’d like the send out your update. You can set up as many alerts to a saved chart as you like, and if you make any changes to the content, Lightdash will update the alert the next time they’re sent. Alerts can be sent to an email address or into Slack (assuming your org has added Slack).
**For security reasons, the delivered files expire after 3 days.** This means old emails or Slack shares will have broken images and there is not an option to retrieve them. If you want to keep the sent files, it’s best to download them from the alert.
##  Enabling alerts
Email alerts are available on all Lightdash Cloud plans. To set up Slack, an organization admin will have to add the Slack integration.
##  Creating an alert
Only users with admin, developer or edit access can create alerts. To create an alert, click on the three-dot menu in the top-right corner of your chart, then click on `Alerts`. You’ll get a modal that pops up and shows you the list of existing alerts for your saved chart, and gives you the option to `Create new`. Once you click on `Create new`, you’ll be brought to a configuration screen for your new alert. Here, you can configure your alert. The options are:
  * **Alert name** : this is the name of your alert.
  * **Conditions** : Configure the condition that is going to be evaluated against the first result(s). 
    * `Alert field` The numeric field is going to be evaluated
    * `Condition`: Operator we are going to use to evaluate your value. 
      * **is greater/less than** : Check if the `first` value in your results is greater/less than your threshold value.
      * **increased/decreased by** : Verify whether the percentage change in the first value relative to the second value exceeds the specified threshold, either by increasing or decreasing.
  * **Run frequency** : This is the frequency at which Lightdash runs a query to check your data for changes. (You will be notified if the conditions on the latest value are met) . All times for the scheduler are in UTC.
  * **Send to** : here, you can pick if you want to send your alert to Slack, email, or both. You can add as many Slack channels and email addresses as you’d like to here. You can send an alert to a person in Slack using `@persons-name` or to a channel using `#channel-name`.


##  Editing and deleting your alerts
To edit an alert, click on the pencil-icon next to the alert you want to edit. This will bring you back to the configuration screen for your alert, where you can make any changes you’d like. In case you want to delete a alert, click on the trash-icon next to the alert you want to delete. You can also pause alerts by clicking the toggle button on the list of alerts.
##  Sending to private Slack channels
You can also send alerts to private Slack channels. To do this, simply type the name of the Slack channel exactly as it appears in Slack into the input text box. Then click on it to confirm and save the alert.
You must add the Lightdash slack bot into the private Slack channel for it to be able to post alert results.
##  Sending to Microsoft teams
You can send your Lightdash alerts directly to Microsoft Teams using incoming webhooks. This allows you to keep your team updated with key metrics and reports, right inside your Teams channels.
###  🔗 How to Create a Webhook in Teams
  * In Microsoft Teams, go to the channel where you want to receive the alert.
  * Click the `...` (More Options) next to the channel name and select Connectors.
  * Find and click on Incoming Webhook, then click Add.
  * Name your webhook (e.g., “Lightdash Reports”) and optionally upload an image.
  * Click Create, then Copy the webhook URL. You’ll need this for Lightdash.

For more info about how to create webhooks, check the official Microsoft teams documentation. Once you have a webhook, add it to the the list of destinations in the alerts form.
Scheduled deliveriesChart Version History
Assistant
Responses are generated using AI and may contain mistakes.


