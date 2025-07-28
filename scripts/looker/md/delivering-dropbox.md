# Sending data to Dropbox  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/delivering-dropbox

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling the Dropbox integration in the Looker Action Hub
  * Delivering data to Dropbox




Was this helpful?
Send feedback 
#  Sending data to Dropbox
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling the Dropbox integration in the Looker Action Hub
  * Delivering data to Dropbox


> Customer-hosted instances may be unable to enable actions from the Looker Action Hub, especially actions that support streamed results or that use OAuth, if the customer-hosted instance does not fulfill the Looker Action Hub requirements.
> See the Sharing data through an action hub documentation page for suggested solutions to this potential issue.
The Dropbox action lets you save data and dashboards to the Dropbox file-hosting service directly from Looker. You can send Looker content to Dropbox in instant, one-time content deliveries or in periodic, recurring content deliveries — also called _schedules_.
Data sent to dropbox is limited to 5,000 rows.
To use the Dropbox action in Looker:
  1. A Looker admin enables the Dropbox integration in the Looker Action Hub. This step is only required once.
  2. A Looker user selects Dropbox as the destination for a delivery.


## Enabling the Dropbox integration in the Looker Action Hub
If you are a Looker admin, you can set up an action to let users select data in Looker and send it to the Dropbox file-hosting service, either as a one-off event or on a schedule.
To enable the action in Looker:
  1. Navigate to the **Actions** page in the **Platform** section of the **Admin** panel.
  2. Select **Enable** next to the Dropbox action to open the Dropbox action page.
  3. On the Dropbox action page, select the **Enabled** switch to enable the action.
  4. Select **Save**. You should see a Test Action message.


Now your users can send or schedule data to a Dropbox file or folder.
## Delivering data to Dropbox
You can select data in Looker and send it to the Dropbox file-hosting service either as a one-off event or on a schedule. If your admin has enabled the Dropbox action, you will see the option when you're sending or scheduling data.
To send Looker content to Dropbox:
  1. In the **Send** or **Schedule** menu of an Explore or a Look, under **Where should this data go?** , select **Dropbox** to access Dropbox delivery options.
If you're sending or scheduling from a dashboard, from the **Schedule a delivery** option in the dashboard's three-dot option menu, under **Destination** , select **Dropbox**.
  2. Select **Log in** to open the Dropbox login page. You'll only need to do this once. If you have previously logged in to Dropbox from Looker, skip to step 6.
  3. Log in to your Dropbox account on the Dropbox login page.
> Each individual user must log in to a Dropbox account the first time they use the Dropbox integration. Once you log in to a Dropbox account, you cannot log out or change accounts from Looker. Make sure you log in to a Dropbox account that is appropriate for Looker to access. To disconnect third-party applications like Looker in Dropbox, see the How to manage third-party apps on Dropbox Dropbox documentation page. Disconnecting or switching accounts may break any existing recurring schedules you have set up with the Dropbox integration.
  4. Once you log in, you must select **Allow** for Dropbox to complete the account connection with Looker. This lets you send or schedule deliveries to specific folders in your Dropbox account. Once you select this option, the Dropbox login page will close and you will be redirected to the Looker **Send** or **Schedule** menu to complete the delivery configuration.
  5. In the Looker **Send** or **Schedule** menu, select **Verify credentials** to load the Dropbox delivery options.
  6. In the **Select folder to save file** drop-down menu, select the Dropbox folder to which you'd like to send or schedule your data delivery. The drop-down menu displays the top-level folders in your Dropbox.
  7. In the **Enter a name** field, enter the filename for your data delivery. You can either specify an existing subfolder for delivery or create a new subfolder in this field by using the syntax `name_of_subfolder/file_name`. For example:
     * If you select the Home folder from the **Select folder to save file** drop-down menu and then specify `Looker/Data Deliveries/Business Overview` in the **Enter a name** field, Looker will name the delivery "Business Overview" and save it in the Data Deliveries subfolder of the Looker folder in your Dropbox.
     * If the specified directory doesn't exist — `Looker/Data Deliveries` in this case — Looker will create it.
  8. Configure the remaining options for your delivery.
  9. Save your selections for schedules or select **Send** for one-time deliveries for Looks or Explores. For dashboards, select **Save** for all delivery types.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


