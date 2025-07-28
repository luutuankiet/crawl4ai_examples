# Scheduling and sending dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/scheduling-and-sending-dashboards

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Starting a delivery from a dashboard
    * Existing schedules window
    * Schedule and send window
  * Starting a delivery from a folder
  * Naming a delivery
  * Recurrence
    * Time-based and date-based schedules
    * Schedules triggered by datagroup updates
  * Destination
    * Integrated service destinations
  * Advanced options
    * Run schedule as recipient
    * Include custom link
    * Expand tables to show all rows
    * Arrange dashboard tiles in a single column
    * Table resolution
    * Delivery time zone
  * Filters
    * When dashboard filters change
    * Using user attribute filters
  * Testing a schedule
  * Saving a schedule or sending now
  * Editing a schedule
  * Duplicating a schedule
  * Deleting a schedule
  * Scheduling challenges
  * Delivery considerations for admins




Was this helpful?
Send feedback 
#  Scheduling and sending dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Starting a delivery from a dashboard
    * Existing schedules window
    * Schedule and send window
  * Starting a delivery from a folder
  * Naming a delivery
  * Recurrence
    * Time-based and date-based schedules
    * Schedules triggered by datagroup updates
  * Destination
    * Integrated service destinations
  * Advanced options
    * Run schedule as recipient
    * Include custom link
    * Expand tables to show all rows
    * Arrange dashboard tiles in a single column
    * Table resolution
    * Delivery time zone
  * Filters
    * When dashboard filters change
    * Using user attribute filters
  * Testing a schedule
  * Saving a schedule or sending now
  * Editing a schedule
  * Duplicating a schedule
  * Deleting a schedule
  * Scheduling challenges
  * Delivery considerations for admins


This page is about scheduling and sending a dashboard. To learn about scheduling Looks or Explores, visit the Using the Looker Scheduler to deliver content documentation page.
Looker lets you schedule immediate or recurring deliveries of dashboards with the **Schedule delivery** dashboard menu option.
Depending on how your Looker admin has set up your permissions for data delivery, you may be able to deliver your content to one or more of Looker's native delivery destinations:
  * Amazon S3 bucket
  * SFTP server


You may also be able to schedule a data delivery to a third-party service that is integrated with Looker, such as Slack.
If there are valid results in cache, Looker will deliver cached results. If there are no results or if the cached results have expired, Looker will rerun the query and cache those results.
## Starting a delivery from a dashboard
Make sure the dashboard is not in edit mode. Select the **Dashboard actions** three-dot menu in the upper right of the dashboard and choose **Schedule delivery**. If you do not see the **Schedule delivery** option, talk to your Looker admin about your assigned permissions.
Once you select **Schedule delivery** , either an existing schedules window appears or a schedule and send window appears, depending on whether you have already created existing schedules on the dashboard.
### Existing schedules window
If you have already created schedules for this dashboard, an existing schedules window appears. This window shows the schedules that you have set along with information about each schedule, such as destination and format. Deliveries that use the **Send now** recurrence and schedules that were created by other people do not appear in this window.
You can perform the following functions in the existing schedules window:
  * Select **Send now** to send an immediate delivery of existing scheduled content without disrupting the scheduled cadence.
  * Select the three-dot menu to edit, duplicate, or delete a schedule.
  * Select **Done** to exit the window.
  * Select **New** to open the schedule and send window and create a new schedule or immediately send a new delivery.


### Schedule and send window
If you select **New** from the existing schedules window, or, if you do not have any pre-existing schedules for the dashboard, a schedule and send window opens. This window lets you customize recurrence, destination, format, filters, and more:
The **Settings** tab in the schedule and send window lets you customize your delivery's recurrence, destination, format, and more.
## Starting a delivery from a folder
You can also start a delivery of a dashboard from the folder where the dashboard is located.
Select **Schedule delivery** from the three-dot menu on the right side of that dashboard's row (in list view) or from the three-dot menu at the top right of the thumbnail (in grid view).
## Naming a delivery
The top of the schedule and send window shows the name that is automatically given to the delivery. The name defaults to the dashboard's name. To edit the delivery's name, select the name (indicated by the dotted underscore), and make your edits.
Depending on the destination of your delivery, the title may also appear in other places:
  * For email deliveries, the title is used for the email's subject line and as part of the filename if you select a format that uses an email attachment.
  * For webhooks, the title is included in the webhook payload under the **Title** field.
  * For deliveries to an Amazon S3 bucket, the title is used in the filename of the delivery and in any error emails that are sent. The filename of the delivery follows the format `TITLE_TIMESTAMP_HASH`, where `HASH` is a random six-character identifier and `TIMESTAMP` follows the pattern `YYYY-MM-DDTHHMM` (for example, the timestamp portion would look like `2019-05-31T0933` for May 31, 2019 at 9:33 AM). The timestamp's timezone will match the **Delivery time zone**.
  * For SFTP deliveries, the title is included in the filename of the delivery. The filename of the delivery follows the format `TITLE_TIMESTAMP_HASH`, where `HASH` is a random six-character identifier and `TIMESTAMP` follows the pattern `YYYY-MM-DDTHHMM` (for example, the timestamp portion would look like `2019-05-31T0933` for May 31, 2019 at 9:33 AM). The timestamp's timezone will match the **Delivery time zone**.
  * For deliveries to integrated services that generate a file attachment, the title is included in the filename of the delivery.


## Recurrence
Customize the timing of your delivery in the **Recurrence** section.
### Send now
If you select **Send now** from the **Recurrence** drop-down menu, a one-time delivery of the dashboard is sent after you fill in the required fields and select the **Send now** button at the bottom of the window.
### Time-based and date-based schedules
Select one of the following options from the **Recurrence** drop-down menu:
  * **Monthly**
  * **Weekly**
  * **Daily**
  * **Hourly**
  * **Minutes**
  * **Specific months**
  * **Specific days**


Timing options change depending on the option that you choose. For example, the **Hourly** settings include a **Start** time and an **End** time. Looker will send the delivery every hour starting at the **Start** time and ending at the **End** time.
The **Time** , **Start** , and **End** fields use a 24-hour clock. If the desired time is not available in the drop-down menu, select the field and manually enter your desired time, such as 9:15 or 15:37.
**Hourly** and **Minutes** schedules repeat daily within the **Start** and **End** timeframe that you set. The end time for **Hourly** and **Minutes** intervals is not inclusive. The last delivery is sent at the last selected interval prior to the specified end time. For example, if a dashboard is scheduled **Hourly** between 12:00 a.m. and 11:00 p.m., then it is sent on the hour, every hour, from 12:00 a.m. to 10:00 p.m. If a recurrence is every 30 minutes between 12:00 a.m. and 11:00 p.m., then the last delivery is sent at 10:30 p.m.
### Schedules triggered by datagroup updates
If your LookML developer has configured datagroups, you can schedule delivery of a dashboard to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs.
Select **Datagroup update** from the **Recurrence** drop-down menu. This reveals a **Datagroup** field with a drop-down menu. Select the datagroup whose update should prompt delivery.
To schedule a dashboard using a datagroup update trigger, the dashboard must contain at least one tile that is based on a model file that includes a datagroup parameter. The **Datagroup** drop-down menu lists all datagroups defined in the models that are included in the dashboard, even if the datagroups are not used to handle caching for queries or PDTs. Even if the datagroup is used in only one tile's model, the entire dashboard will be sent when the selected datagroup update completes.
Schedules based on datagroups only send after the regeneration process has completed for all PDTs that are persisted with that datagroup parameter, ensuring that your delivery includes the most up-to-date data.
## Destination
The **Destination** setting may display several destination options for dashboard deliveries. Once you've selected a data destination, a new setting field appears for you to add specific details about that destination, such as an email address or a webhook URL. See the following sections for information about each destination's settings.
### Email
When **Email** is selected in the **Destination** field, a new **Email addresses** field appears. This is a required field.
Enter the email addresses of the recipients in the **Email addresses** field. If you're entering multiple email addresses, select the Enter key, or add a comma, after each address.
Depending on the settings for your Looker instance and your assigned permissions, you may be able to send emails to email addresses that are unassociated with any user account on your Looker instance. These emails are classified as external. The **All** and **External** indicators at the right of the field show both the number of all email recipients and the number of just the external email recipients. Select each indicator to toggle between showing all email recipients and showing only external email recipients. To enable you to deliver content to external users, your Looker admin must have granted you permissions to deliver content to external users or have added those recipients' email domains to the Email Domain Allowlist for Scheduled Content.
If a recipient is another Looker user, that person will see the option to link back to the dashboard from the email, unless your Looker admin has set your Looker instance's emailed data policy to **Send Data Only** or the **Include links** option is deselected.
Emailed deliveries may not exceed 20 MB (for formats that are delivered in the email body) and 15 MB (for formats that are delivered as an attachment).
See the Advanced options section on this page for more information about email deliveries.
### Webhook
Webhooks are a way to trigger exchanges between internet-based services. With a web service like Zapier, webhooks can let Looker data be delivered to a wide range of applications; for example, you may be able to schedule periodic delivery of a dashboard to a webhook.
To set up a webhook, go to your web service and do the following:
  * Obtain a URL to which Looker should send an HTTPS request.
  * Specify a destination application for your Looker data delivery. The destination application may require additional configuration in order to receive data from Looker.


The exact procedure differs depending on what web service and destination application you're using to deliver the data. See the Scheduling Looks and Dashboards Using Webhooks Community post for guidelines on setting up another application to receive the webhook data from Looker.
When **Webhook** is selected in the **Destination** field, a new **Webhook URL** field appears. This is a required field.
Enter the URL where Looker should send an HTTPS request for this delivery in the **Webhook URL** field. You can obtain this URL from the web service you're using to handle your webhook.
### Amazon S3
Amazon S3 buckets are a common way to store large amounts of data. You or your company will need to have created an S3 bucket with Amazon before Looker can use it.
When **Amazon S3** is selected in the **Destination** field, several new fields appear and prompt you for information about your Amazon S3 bucket:
  * **Bucket** : The name of your Amazon S3 bucket. This is a required field.
  * **Optional Path** : The folder, if any, that you want to save your data to.
  * **Access Key** : The Access Key ID to your S3 bucket, provided by Amazon. This is a required field.
  * **Secret Key** : The Secret Access Key to your S3 bucket, provided by Amazon. This is a required field.
  * **Region** : The Amazon services region where your S3 bucket is hosted.


Check out the Scheduling (unlimited) Results to S3 Community post for more details about delivering data using an Amazon S3 bucket.
### SFTP
Sending results to an SFTP server is a good method to use when your data or visualization is too large to send through email.
When **SFTP** is selected in the **Destination** field, several new fields appear and prompt you for information about your Amazon S3 bucket:
  * **Address** : The URL or IP address of the SFTP server to which you want to send your data. This is a required field. For example:
    * `sftp://files.looker.com/Marketing/In/`
    * `sftp://192.168.0.10/Marketing/In/`
  * **Username** and **Password** : Login credentials for the SFTP server. These are required fields.
  * **Preferred key exchange algorithm** : This field is optional. To configure it, choose the preferred SSH key exchange algorithm for establishing the connection. If the connection is not established within five minutes, choose a different algorithm. Some algorithms take a long time to generate an SSH key. This option lets you use an algorithm that might take less time. Choosing one of the algorithms makes it the preferred algorithm for establishing the SSH connection. If the algorithm is not supported by the server, all the other algorithms are used in subsequent attempts. When this field is set to **Default** , the original order of algorithms in the connection library is used.


SFTP support is limited to username and password credentials. SSH private key credentials are not supported.
Looker stores SFTP fingerprints for your SFTP server. If you encounter errors with your SFTP delivery, it could indicate that the SFTP fingerprints are invalid. In this case, contact your Looker admin.
### Integrated service destinations
You can schedule or send dashboard deliveries to a service that is integrated with Looker, such as Slack, Dropbox, Google Drive, and others. Integrations must be enabled by your Looker admin. Looker admins must specifically give permissions for users and embed users to send and schedule data to third-party integrations.
When an integrated service is selected in the **Destination** field of the Scheduler, several new fields may appear and prompt you for more information.
The following list shows the Looker Action Hub services to which you can deliver the contents of a dashboard.
Here is how to use the list:
  * The URLs shown in the **Link to README file** column provide instructions for enabling and configuring the integrated service to work with Looker.
  * The URLs shown in the **How to use this integration** column provide instructions for how to send data from Looker to the integrated service. Some of these articles also contain enablement instructions.
  * **Required LookML tags** lists any required tags that must be used with the `tags` parameter in the content's underlying model.
  * **Action type** indicates what level of data the integrated service is sending: field, query, or dashboard. A field-level action sends the value of a single, specified cell in a data table. A query-level action sends the results of an entire query, such as all rows in an Explore or a Look. A dashboard-level action sends an image of a dashboard.
  * **Uses Google OAuth authentication** indicates whether the integrated service uses Google OAuth credentials for authentication.
  * **Uses data streaming** indicates whether the integrated service supports streamed query results. Dashboards cannot stream data.


Integrated service | Description | Link to README file | How to use this integration | Required LookML tags | Uses Google OAuth authentication (Yes/No) | Uses data streaming (Yes/No)  
---|---|---|---|---|---|---  
Azure Storage | Send and store a data file on Azure Storage. | View README on GitHub | None | No | No  
DigitalOcean Spaces | Send to and store a data file in DigitalOcean Storage. | View README on GitHub | None | No | No  
Dropbox | Send and store a data file on Dropbox. | No README available | View documentation | None | Yes | No  
Google Cloud Storage | Write data files to a Google Cloud Storage bucket. | None | No | No  
Google Drive | Send data to Google Drive. | No README available | None | Yes | No  
SendGrid | Send data and schedule results to send to a email address using SendGrid's API. | View README on GitHub | None | No | No  
Slack | Send Looker content in direct messages, public channels, and private channels in Slack using OAuth. It is available for Looker-hosted deployments on 6.24+ with the IP Allowlist feature disabled. | No README available | View documentation | None | Yes | No  
Slack Attachment (API Token) | Send data directly into a Slack channel along with user credentials. You may also want to reference Lookerbot documentation for additional Slack functionality. | None | No | No  
Teams — Incoming Webhook | Send data to Microsoft Teams using an incoming webhook. | View README on GitHub | See README | None | No | No  
## Format
The **Format** field contains a drop-down menu of available formats:
  * **CSV zip file** : The unformatted data from the dashboard delivered as a collection of comma-separated values (CSV) files in a zipped directory. For deliveries to email, the ZIP file is delivered as an email attachment.
  * **PDF** : An image of the dashboard as a single PDF file. The default layout displays tiles as they are arranged in the dashboard, but other layout and sizing options are available under **Advanced options**. For deliveries to email, the file is delivered as an email attachment.
  * **PNG visualization** : An image of the dashboard as a single PNG file. The default layout displays tiles as they are arranged in the dashboard, but other layout options are available under **Advanced options**. For deliveries to email, the image appears inline within the body of the email.


## Advanced options
The **Advanced options** tab provides additional customization for your delivery. The options available depend on the selected destination and format of your delivery.
### Custom message
This option is available only for the email destination.
Enter a message you would like included in the body of emails to recipients. Looker limits the number of characters in a custom message to 1,500.
### Run schedule as recipient
This option is available only for the email destination.
The **Run schedule as recipient** option lets users specify a list of recipients who will each receive the content delivery as if each one of them had run the query, based on each person's permissions. This means that each user's access filters and user attributes will be applied to the data that is included in each email.
If a user is a Looker admin, the **Run schedule as recipient** option lets the admin specify a list of users who will each receive the content delivery as if each one of them ran the query, based on each person's permissions. Non-admin users may also enter their own email address to receive a delivery as if they had queried the content, based on their permissions. This means that each user's access filters and user attributes will be applied to the data that is included in each email.
In the following example, a Looker admin needs to schedule a data delivery that lists counts of users per state.
User A has an access filter set as `users.state = 'California'`. When **Run schedule as recipient** is selected, the scheduled query will apply the access filter `users.state = 'California'` and send filtered results to user A. The filtered results will include data only about California.
In the **Advanced options** tab, select the **Run schedule as recipient** checkbox and then add email addresses for your recipients in the **Email addresses** text field under the **Settings** tab. This option takes into account the permissions of the user creating the schedule as well as the types of email addresses added to the **Email addresses** field. In some cases, the **Run schedule as recipient** option is not available:
  1. When a user adds the email of a disabled user
  2. When a user adds an email that does not belong to a Looker user, as indicated by the **External** count next to the list of email addresses:


In these situations, regardless of whether the option was selected before or after entering the external email address, the **Run schedule as recipient** option will remain enabled but the schedule cannot be saved until the **Run schedule as recipient** option is de-selected or the external email addressed is removed from the list of recipients.
In the special case where a user is listed as a recipient on a schedule that has **Run schedule as recipient** enabled and then that user's account is disabled, the schedule will fail to deliver to the disabled user starting the next time it runs. If that user's account is deleted, the entire schedule will fail to deliver to any recipients. A Looker admin or user with the `see_schedules` permission will be able to diagnose this failure in the **Scheduler History** page in the **Admin** panel.
### Include links
This option is available only for the email destination.
If your Looker admin has set your Looker instance's emailed data policy to **Send Links and Data**, the schedule and send window displays the **Include links** option. Select this option to include in the data delivery emails a **View full dashboard** link that goes to the dashboard in Looker. Dashboard links do not include any `hide_filter` parameters.
Recipients must log in to Looker and have permissions to access the models on which the delivered dashboard is based to view that content in Looker. If you want to remove this link from your data delivery emails, clear the **Include links** checkbox.
### Include custom link
This option is available only for the email destination, and only for embedded dashboards. It is displayed when the **Include links** option is selected.
The **Include custom link** option lets you configure a custom URL to which the **View full dashboard** link will connect, instead of linking to the dashboard in Looker. You can also optionally change the **View full dashboard** link text.
To use this option, a Looker admin or a user with either the `schedule_look_emails` or the `create_alerts` permission first must specify allowed domains for the custom link and select the format of the custom link URL in the **Embed** page in the **Admin** menu.
#### Domain
Select the URL domain from the list of domains configured on the allowlist. For example, `app.customer.com`.
#### Path
The **Path** option is displayed only if **User defined URL** is selected in the **Select content path** field on the **Embed** page in the **Admin** menu.
Enter a custom path for the link URL here. For example, if you want your custom link to point to the URL `app.customer.com/my_embed_app`, enter the path `/my_embed_app` here.
#### URL label
Use this field to enter new link text, which will replace the text **View full dashboard** in email deliveries. This field will display any text that is entered in the **URL label** field in the **Embed** page in the **Admin** menu by default and can be changed in this field.
### Results
This field is available only for CSV ZIP file formats of dashboard deliveries. It contains two options: **With visualizations options applied** or **As displayed in the data table**. You can choose one or the other.
Choose the **With visualizations options applied** option to apply some of the visualization settings from the dashboard tiles to your dashboard delivery. This causes the files in your delivery to appear similar to table charts. Any of the following settings in the **Plot**, **Series**, and **Formatting** menus that are configured for a visualization will be applied to the data delivery:
  * Limit Displayed Rows to a maximum of 500 rows shown or hidden
  * Show Full Field Name
  * Custom labels for each column


Choose the **As displayed in the data table** option to deliver the data as it appears in the data table of each dashboard tile's **Explore from here** window.
### Values
This field is available only for CSV ZIP file formats of dashboard deliveries. It contains two options: **Formatted** or **Unformatted**. You can choose one or the other.
  * Select **Formatted** if you want the data to appear similar to how it appears in the **Explore** experience in Looker, although some features (such as linking) aren't supported by all file types.
  * Select **Unformatted** if you do not want to apply any special formatting of your query results, such as rounding long numbers or adding special characters, that your Looker developers may have put in place. This is often preferred when data is being fed into another tool for processing.


### Expand tables to show all rows
This option is available only for PDF formats of dashboard deliveries.
Select the **Expand tables to show all rows** box to display all rows of any table visualizations in the dashboard — rather than just those rows that display in the dashboard tile thumbnails.
If the **Expand Tables to Show All Rows** option is selected, dashboard tiles that contain table visualizations may look slightly different in delivered PDFs than they do inside Looker. The following differences may be noticeable in the PDF:
  * Customizations to background colors and font sizes are removed from column headers and subtotal rows.
  * Tables appear in the white theme.
  * The sort icon does not appear on pivoted tables that were not manually sorted.
  * Tables with **Size Columns to Fit** enabled stretch to the full width of the tile.


Additionally, for tables with more than 20,000 cells, the following differences may be noticeable in the PDF:
  * Conditional formatting options other than **Background color** no longer appear.
  * Cell visualizations on numeric columns no longer appear.


If you do not see the **Expand tables to show all rows** option when you've chosen **PDF** in the **Format** field, talk to your Looker admin about installing the appropriate version of the Chromium renderer for your Looker instance.
### Arrange dashboard tiles in a single column
This option is available only for the PDF and PNG visualization formats of dashboard deliveries. When Slack is selected as the delivery destination only PDFs are supported.
Select the **Arrange dashboard tiles in a single column** box to format your PDF or your PNG visualization in a single column layout. This layout displays dashboard tiles in a single vertical column. Leave the box unchecked to show the tiles as they are arranged in the dashboard.
### Paper size
This option is available only for PDF formats of dashboard deliveries.
You have the option to specify the optimal size and orientation of dashboard PDFs by selecting from the **Paper size** drop-down menu. Large visualizations or groups of overlapping dashboard tiles may need to be resized to fit cleanly on a PDF page. If you do not see the **Paper size** option, talk to your Looker admin about installing the latest version of the Chromium renderer for your Looker instance.
### Table resolution
This option is available only for the PNG visualization format and when the **Arrange dashboard tiles in a single column** box is checked.
You can customize the width of your visualization by using the **Table resolution** drop-down menu. Your width options are:
  * **Normal** : 800 pixels
  * **Wide** : 1680 pixels


For deliveries to email, if you choose **Wide** and the visualization width exceeds the limit set by your email client, email delivery recipients may need to scroll horizontally to see the entire visualization.
### Delivery time zone
By default, Looker uses the time zone associated with your account to determine when to send your data delivery. If you don't have a time zone associated with your account, Looker uses your Application Time Zone setting.
If you want to specify a different time zone, select the time zone from the drop-down menu. The time zone you select does not affect the data in your Look or dashboard, just the timing of the delivery.
## Filters
The **Filters** tab in the schedule and send window shows any filters applied to the dashboard as well as their values. In this tab, you can edit the values for any existing filters applied to the dashboard and the new values will be applied to the delivery. The dashboard itself will not be affected.
You cannot add filters to your schedule in the **Filters** tab, only view and edit the values for existing dashboard filters.
For example, you might send regional teams results that are filtered for their states of interest.
If a dashboard filter requires a filter value, you must enter a value in the **Filters** tab to create or save any edits to the delivery.
### When dashboard filters change
Sometimes dashboard filters change after a schedule is created. The following table explains how that affects filters applied to the scheduled deliveries.
Action | Effect on Schedule Filter  
---|---  
A schedule is created with a filter. Later, the filter value is changed on the dashboard. | No effect on the schedule filter value. It remains the value set in the **Filters** tab, even if that value is **is any value**.  
A schedule is created with a filter. Later, the filter is renamed in the dashboard. | The filter is removed from the delivered data.  
A schedule is created with a filter. Later, the filter is deleted in the dashboard. | The filter is removed from the delivered data.  
A schedule is created. Later, a new (non-required or required) filter is added to the dashboard. | The filter is applied to the delivered data, using the filter value set in the **Filters** tab. If no value is set in the **Filters** tab, the value is interpreted as **is any value** , essentially removing the filter.  
### Using user attribute filters
If your Looker admin has configured user-specific values, called user attributes, and you have edit privileges for a dashboard, you can create a dashboard filter that uses the **matches a user attribute** filter option. A filter of this type automatically customizes the filter value for each dashboard viewer. With this kind of filter, you can deliver customized results to each delivery's recipients. To read more about user attributes, visit the User attributes documentation page.
## Testing a schedule
If you set the **Recurrence** field to anything other than **Send now** , a **Test now** button appears at the bottom left of the schedule and send window.
Select the **Test now** button to send a one-time test delivery of the schedule only to yourself. A green checkmark appears to confirm that a test has been sent. If the **Test now** button is not available, you can set the **Recurrence** field to **Send now** to send a one-time test delivery.
## Saving a schedule or sending now
If you set the **Recurrence** field to **Send now** , select the **Send now** button at the bottom of the window for a one-time delivery to the listed destination.
If you set the **Recurrence** field to anything other than **Send now** , select the **Save** button to save your schedule and close the window.
Select the **Cancel** button to exit the window without saving or sending the schedule.
Your saved schedules for a dashboard appear in its existing schedules window. Your saved schedules for all content appear on the **Schedules** page of your user profile.
## Editing a schedule
You can edit only the schedules you have created. To edit a schedule:
  1. Select the three-dot **Dashboard actions** menu at the top right of the dashboard.
  2. Select **Schedule delivery** from the drop-down menu.
  3. In the existing schedules window, select the three-dot menu that applies to the schedule that you want to edit.
  4. Choose **Edit** from the drop-down menu.
  5. The schedule and send window appears for that schedule. Make your edits in this window.
  6. Select **Save** when your edits are complete, or select **Cancel** to cancel your edits.


## Duplicating a schedule
You may want to duplicate a schedule and then edit it. To duplicate a schedule:
  1. Select the three-dot **Dashboard actions** menu at the top right of the dashboard.
  2. Select **Schedule delivery** from the drop-down menu.
  3. In the existing schedules window, select the three-dot menu that applies to the schedule that you want to edit.
  4. Choose **Duplicate** from the drop-down menu.
  5. The schedule and send window appears for the duplicate schedule. "Copy" is appended to the schedule name.
  6. Make your edits.
  7. Select **Save** when your edits are complete, or select **Cancel** to cancel your edits and delete the duplicated schedule.


The original schedule remains unchanged when you make a duplicate.
The filters in a duplicate schedule will be set to the same values as are present in the **Filters** tab of the original schedule, although you can edit these values. If any filters have changed since the creation of the original schedule, the filters will be affected as shown in the **When dashboard filters change** section. If a required filter was later added to the dashboard that the original schedule is based on, you need to select a value for that filter before saving the duplicated schedule.
## Deleting a schedule
You can delete only the schedules you have created. To delete a schedule:
  1. Select the three-dot menu at the top right of the dashboard.
  2. Select **Schedule delivery** from the drop-down menu.
  3. In the existing schedules window, select the three-dot menu that applies to the schedule that you want to edit.
  4. Choose **Delete** from the drop-down menu.
  5. A new window appears. Select **Delete** to delete the schedule, or select **Cancel** to keep the schedule.


You can also delete a schedule from the **Schedules** page of your user profile.
## Scheduling challenges
At times, a scheduled delivery could fail to reach one or more of its recipients. This could happen if the underlying model has an error, if the recipient does not have access to the data, or if there are rendering problems or page errors. The data destination reports an error if it is unable to connect to the specified endpoint.
If such issues occur, Looker sends an email to notify the schedule's creator. The email includes a link to the scheduled content, a list of the recipients it failed to reach, and more information, if available, about the problem Looker encountered when trying to reach the recipients.
## Delivery considerations for admins
Looker admins can see, edit, reassign, and delete any users' schedules. Additionally, Looker admins should bear some things in mind when setting up data delivery for their Looker instance and granting users permissions to send or schedule data deliveries. For more information, visit the following documentation pages:
  * Admin settings - Schedules
  * Admin settings - Schedule History
  * Managing business user features
  * Labs - Render Long Tables


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


