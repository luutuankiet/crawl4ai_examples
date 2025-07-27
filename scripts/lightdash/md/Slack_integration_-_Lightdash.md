# Slack integration - Lightdash

**Source:** https://docs.lightdash.com/references/slack-integration

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Integrations
Slack integration
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
  * Required permissions
  * Select a notification channel
  * Slack bot avatar
  * AI Bot channel mappings
  * Unfurl Lightdash links
  * Scheduled deliveries
  * Saved Chart Alerts in Slack
  * AI analyst agents


For walk through videos, check out our guides on adding the Slack integration and using the Slack integration.
##  Required permissions
The Lightdash Slack app will request permission for these scopes:
  * **`[links:read]`for lightdash.cloud** : Links to lightdash.cloud will be sent to our App so we can make an internal request and fetch information from charts and dashboards so we can later share it in slack.
  * **`[links:write]`**: This allows us to unfurl the URL previously mentioned.

No other content will be shared from your workspace.
##  Settings
After installing the app you’ll see these settings:
###  Select a notification channel
Here you may choose a Slack channel where Lightdash will send alerts when any scheduled deliviries fail in your organization. You must add the Lightdash app into that organization for notifications to work properly.
###  Slack bot avatar
You can customize the avatar for your Lightdash slack app by adding an image URL in the Profile photo URL field. Slack recommends these images be square with a minimum of 512x512 pixels, but no larger than 1024x1024 pixels.
###  AI Bot channel mappings
Here you can choose which project is used by the Lightdash AI analyst co-pilot for each of your Slack channels. Only one project can be used for each channel.
##  Unfurl Lightdash links
After installing the Slack app it will automatically unfurl links you share in Slack from your Lightdash project. The Lightdash app must be invited to a channel before it will unfurl links in that channel. Chart and dashboard links unfurl for links copied from the URL field and also “share” links copied by clicking the link icon. Here’s what an individual chart looks like unfurled: And an unfurled dashboard:
##  Scheduled deliveries
Once Slack is added to your Lightdash organization you can use it as a destination for scheduled deliveries. You can schedule refreshes for either Charts or Dashboards and push the results into a Slack channel or DM. The result will look like this for charts if you choose to attach an image of the chart: And like this for dashboards if you chose _not_ to include an image:
##  Saved Chart Alerts in Slack
In addition to scheduled deliveries, you can also set up alerts on saved charts that only send to slack if certain criteria are met.
##  AI analyst agents
The Slack integration is also used by AI analyst agents to chat with your data and build charts in Slack. Once you have access to AI analysts you can give them access to Slack threads in your integration settings. Remember, to trigger AI responses you need to mention the agent name in every message.
Assistant
Responses are generated using AI and may contain mistakes.


