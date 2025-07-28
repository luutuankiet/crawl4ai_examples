# Scheduling deliveries to the Slack integration  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/scheduling-slack

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling the integration in the Looker Action Hub
    * Managing Slack workspace connections to Looker
  * Authenticating into your Slack workspace
    * Authenticating into a Slack workspace from the Account page
    * Authenticating into a Slack workspace from the Send or Schedule window
  * Delivering data to Slack
  * Accessing Looker from Slack
    * Sharing links to Looker content in Slack
    * Using slash commands to retrieve Looker information in Slack
    * Viewing your Looker app Home tab in Slack
  * Setting a default Looker instance for your Slack workspace




Was this helpful?
Send feedback 
#  Scheduling deliveries to the Slack integration
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling the integration in the Looker Action Hub
    * Managing Slack workspace connections to Looker
  * Authenticating into your Slack workspace
    * Authenticating into a Slack workspace from the Account page
    * Authenticating into a Slack workspace from the Send or Schedule window
  * Delivering data to Slack
  * Accessing Looker from Slack
    * Sharing links to Looker content in Slack
    * Using slash commands to retrieve Looker information in Slack
    * Viewing your Looker app Home tab in Slack
  * Setting a default Looker instance for your Slack workspace


You can install the Looker app into your Slack workspace to send or schedule data deliveries directly to public and private Slack channels. To enable installation of the Looker app, your Slack workspace owner may need to adjust the app installation settings for your Slack workspace.
The Slack Attachment (API Token) integration is also still available for use.
## Enabling the integration in the Looker Action Hub
If your Looker instance meets the required conditions, your Looker admin must enable the Slack integration in the Looker Action Hub, for each Looker instance, before users can deliver data with the Slack integration.
  1. From the **Admin** panel under **Platform** , go to the **Actions** page.
  2. Click the **Enable** button to enable the Slack integration in the Looker Action Hub.
  3. On the **Slack** action page, click **Connect** to connect to your Slack workspace.
Looker will request access to the Slack workspace that is indicated in the drop-down menu on the top right of the page. To connect multiple Slack workspaces to a single Looker instance, click the **+ Connect to Slack workspace** link.
  4. Click **Allow** , and return to the **Slack** action page.
  5. Click the **Enable** switch, and click **Save**.


### Managing Slack workspace connections to Looker
You can manage the instance's Slack workspace connections from the **Slack** action page. Click the **Settings** button next to the Slack integration on the **Actions** page in the **Admin** panel.
Admins can perform the following operations with each Slack workspace connection: Connect, Disconnect, and Reset.
  * To connect additional Slack workspaces to the Looker instance, click the **+ Connect to Slack workspace** link.
  * To disconnect an existing Slack workspace connection, click the **Disconnect** button and click **OK** on the pop-up warning message. You do _not_ need to click **Save** on the **Slack** action page to save these settings, and the action will still show as **Enabled** even if no Slack workspace is connected.
  * To refresh your Slack workspace connection without having to disconnect and reconnect it, click the **Reset** button.


## Authenticating into your Slack workspace
> Users must authenticate into the same Slack workspace that the Looker admin has connected to Looker. Users must also be existing members of the workspace before they can authenticate into it from Looker.
You can authenticate into a Slack workspace for the first time from the:
  * **Account** page. (This is your only option if there are multiple Slack workspaces connected to your Looker instance.)
  * **Send** or **Schedule** window.


You receive a confirmation Slack message after you successfully authenticate into Slack from Looker.
### Authenticating into a Slack workspace from the Account page
  1. In Looker, click your user profile icon in the upper right of the screen, and select **Account**.
  2. Any integrations that are enabled for your instance appear under **Integrations**. If your Looker admin has enabled at least one Slack workspace, a button to **Sign in with Slack** will be present. If your Looker admin has connected more than one Slack workspace to your Looker instance, a list of workspaces appears with options to log in to each one individually.
  3. Looker will request access to the Slack workspace. If your Looker admin has connected multiple Slack workspaces to your Looker instance, a drop-down menu appears in the upper right of the OAuth page. Select the appropriate Slack workspace from the drop-down. Click **Allow**.
  4. When you return to your **Account** page, an option will now appear in the **Integrations** section that will let you revoke your Slack credentials for any workspaces that you're connected to. Caution: Be careful not to revoke your Slack token — if you do, any schedules that you created will fail.


Now that you're authenticated, you can send or schedule dashboards, Looks, and Explores. See the Delivering Data to Slack section on this page for more information.
### Authenticating into a Slack workspace from the Send or Schedule window
  1. In Looker, navigate to the content to be delivered, click the gear menu, and click **Send** or **Schedule**. For dashboards, select **Schedule delivery**.
  2. In the **Send** or **Schedule** window of an Explore or a Look, select the **Slack** action as the delivery destination under **Where should this data go?**. For dashboards, select **Schedule delivery** in the **Schedule and send window**.
  3. Next to **Slack** , click **Log in**.
  4. Looker will request access to the Slack workspace. If your Looker admin has connected multiple Slack workspaces to your Looker instance, a drop-down menu appears in the upper right of the OAuth page. Select the appropriate Slack workspace from the drop-down. Click **Allow**.
  5. The **Send** or **Schedule** window (or the **Schedule delivery** window for dashboards) now shows your Slack delivery options, including your Slack workspace's public and private channels.


## Delivering data to Slack
You can deliver content to one of multiple Slack workspaces. After a Looker admin sets up the workspace connections, you can sign in to each one from your user **Account** page. Then, you can select a destination workspace from those listed in the **Workspaces** drop-down of the **Send** or **Schedule** pop-up, or **Schedule delivery window** for dashboards.
The formatting options for delivering a dashboard are as follows:
  * PDF
  * Visualization (PNG)
  * CSV ZIP file


Sending or scheduling a Look or an Explore has different formatting options available, including:
  * CSV
  * XLSX
  * JSON — Simple: In this format, Looker uses a dimension or measure's field name as its rendered value rather than the field's label.
  * JSON — Label: In this format, Looker uses field labels as its rendered value in its JSON output.
  * JSON — Simple, Inline: In this format, Looker uses a dimension or measure's field name as its rendered value rather than the field's label.
  * JSON — Detailed, Inline: In this format, Looker uses a dimension or measure's field name as its rendered value rather than the field's label.
  * Text
  * HTML


To deliver a user-defined dashboard, a LookML dashboard, a Look, or an Explore, navigate to your content and perform these steps:
  1. Click the gear menu, and click **Send** or **Schedule**. (You will not have the option to schedule an Explore.) For dashboards, select **Schedule delivery** from the dashboard's three-dot menu.
  2. In the **Send** or **Schedule** window, select the Slack integration as the delivery destination under **Where should this data go?** For dashboards, select the Slack integration as the delivery destination under **Destination**. If this is your first time using the Slack integration, you first need to authenticate into the Slack workspace.
  3. Looker displays delivery options that are specific to the Slack workspace or workspaces connected to this Looker instance. 
     * In the **Share In** field, enter the name of the Slack channel to post your data to. You can send direct messages or messages to public or private channels. Include the leading # character, for example, #Sales.
     * In the **Comment** field, enter any text that you want to include with the delivery. You can also use Slack's advanced formatting with special parsing to mention specific groups, users, or channels or to make any other special mentions.
     * In the **Filename** field, enter a name for the attachment file.
  4. If you are scheduling a data delivery, click **Save All**. Your query or dashboard will be delivered to Slack as scheduled. If you are sending your data, click **Send**. Your data will be delivered to your Slack channel.


## Accessing Looker from Slack
You can access Looker data from within Slack by:
  * Sharing links to Looker content
  * Using slash commands to retrieve Looker information in Slack
  * Viewing your Looker app **Home** tab in Slack


### Sharing links to Looker content in Slack
You can share links to SQL Runner visualizations, user-defined dashboards, LookML dashboards, Looks (but not publicly embedded Looks), or Explores in Slack.
The link unfurls in Slack to show the content's title and some of its metadata, which is visible only to those who have access to the underlying content. After the link unfurls, you or other users can:
  * Post a link back to the content in Looker and a snapshot of the content in the channel — click **Post to this Channel**. After the content is posted to the channel, anyone in the channel can view the content snapshot and title, _even if they do not have access to the underlying content in Looker_.
  * Add the content to a Looker **Favorites** folder — click **Add to Favorites**. After you add content to your **Favorites** folder, the Looker app in Slack displays a message in Slack with a link to access your **Favorites** folder in Looker.


If you have multiple Looker instances connected to the workspace, you must set the default instance to match the Looker instance from which you're sharing the link.
### Using slash commands to retrieve Looker information in Slack
> If you also have Lookerbot enabled, you may need to rename some slash commands. Custom Slack commands are not available for the Slack integration, but you can configure custom commands in Lookerbot. Ensure that you are using Lookerbot version 0.0.16 or later by updating from the Lookerbot GitHub repo as instructed in the Getting started with Lookebot section of the **Using Lookerbot for Slack** Best Practices page.
Use the following slash commands to retrieve information from Looker and post it to Slack:
  * `/looker` and `/looker whoami` — The Looker app in Slack greets you by name; tells you the Looker instance to which you're connected; and provides links to your Looker **Favorites** folder, to your personal folder, and to **Help**.
  * `/looker help` — The Looker app in Slack lists supported slash commands.
  * `/looker favorites` — The Looker app in Slack lists the content from your Looker **Favorites** folder. Click the ellipsis (`...`) beside each piece of content to access a menu from which you can **Post to this Channel** or **Remove from Favorites**.
  * `/looker folder` — The Looker app in Slack lists the content from your Looker personal folder. Click the ellipsis (`...`) beside each piece of content to access a menu from which you can **Post to this Channel** or **Remove from Favorites** (if the content is also in your **Favorites** folder).
  * `/looker select` — The Looker app in Slack lists the instance or instances connected to that Slack workspace. To set a default instance for your Slack workspace, click it from this list. All instance-specific slash commands would apply to the default Looker instance.


### Viewing your Looker app Home tab in Slack
To see a list of your favorite Looker content and folders in Slack, click on the **Home** tab in the Looker app.
If you set a default Looker instance for your Slack workspace, you only see content from that instance from your Looker app **Home** tab.
## Setting a default Looker instance for your Slack workspace
> If your Looker admin has connected only a single Looker instance to your Slack workspace, that instance is your default.
If your Looker admin has connected multiple Looker instances to your Slack workspace, you can set one of the instances as the default Looker instance. Any instance-specific slash commands — most commands besides `/looker help` — and link unfurling would apply to the default instance.
  1. In Slack, run the slash command `/looker select` to see a list of the Looker instances connected to your Slack workspace.
  2. The Looker app asks **Which instance would you like to set as a default?** Click the button corresponding to the name of the Looker instance to set this instance as your default.
The Looker app will confirm your selection.


To switch your default Looker instance, run `/looker select` again and select a different Looker instance. You must switch default instances if you're unfurling links from a Looker instance that is not the default instance. If you do not switch instances and try to unfurl a link from a non-default Looker instance, you will be prompted to log in to that Looker instance.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


