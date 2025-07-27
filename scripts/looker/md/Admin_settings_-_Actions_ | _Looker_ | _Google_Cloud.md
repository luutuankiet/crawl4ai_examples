# Admin settings - Actions  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-actions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling an action
  * List of integrated services




Was this helpful?
Send feedback 
#  Admin settings - Actions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling an action
  * List of integrated services


The **Actions** page in the **Platform** section of the **Admin** menu lets you enable services that are integrated with Looker. For information on how to build and test actions to request to add to the Looker Action Hub _or_ to add to your own private action hub server, see the Sharing data through an action hub documentation page.
## Requirements
To access the **Actions** page in the **Platform** section of the **Admin** menu, your user must have the Admin role.
## Enabling an action
> Prompt Looker to check the Looker Action Hub server for new actions by selecting **Refresh** at the top of the actions list.
Each service that is integrated into Looker's **Actions** page has its own requirements. The list of integrations later on this page has a table of all the available services. See the **How to use this integration** column for links to articles about setting up and using each service.
First perform any setup steps required on the integrated service. Then enable the integration in Looker, specifying any required information for that service.
To enable an integration, perform the following steps:
  1. On the **Platform** page of the **Admin** , select **Actions**.
  2. Find the service that you want to enable, and select the **Enable** button to the right of the service.
Looker then displays the enablement page for the selected service.
If applicable, enter the required information to configure this action. You should be able to gather this information from your account with the service that you're enabling.
  3. Turn on the **Enabled** switch. Looker automatically tests the action's configuration and displays an error if the action is configured incorrectly. Once you've made changes, select **Test Again** to retest the action's configuration.
  4. Select **Save** to save the action's configuration and close the action enablement page. The action is now available as a destination in the Looker Scheduler.


## List of integrated services
The following list shows the services that are are available in the Looker Action Hub.
Here is how to use the list:
  * The URLs that are shown in the **Link to README file** column provide instructions for enabling and configuring the integrated service to work with Looker.
  * The URLs that are shown in the **How to use this integration** column provide instructions for how to send data from Looker to the integrated service. Some of these articles also contain enablement instructions.
  * **Required LookML tags** lists any required tags that must be used with the `tags` parameter in the content's underlying model.
  * **Action type** indicates what level of data the integrated service is sending: field, query, or dashboard. A field-level action sends the value of a single, specified cell in a data table. A query-level action sends the results of an entire query, such as all rows in an Explore or a Look. A dashboard-level action sends an image of a dashboard.
  * **Content available for scheduled deliveries** indicates what type of Looker content this integrated service can send as an ad hoc or scheduled content delivery.
  * **Uses Google OAuth authentication** indicates whether the integrated service uses Google OAuth credentials for authentication. Customer-hosted instances may be unable to enable actions from the Looker Action Hub that use Google OAuth. See the Sharing data through an action hub documentation page for suggested solutions to this potential issue.
  * **Uses data streaming** indicates whether the integrated service supports streamed query results. Customer-hosted instances may be unable to enable actions from the Looker Action Hub that stream results. See the Sharing data through an action hub documentation page for suggested solutions to this potential issue.
  * **Minimum supported Looker version** provides the earliest Looker version that your instance must be using in order to use this integration.


Integrated service | Description | Link to README file | How to use this integration | Required LookML tags | Action type | Content available for scheduled deliveries | Uses Google OAuth authentication (Yes/No) | Uses data streaming (Yes/No) | Minimum supported Looker version  
---|---|---|---|---|---|---|---|---|---  
Airtable | Add records to a table in Airtable. | View README on GitHub | None | Query | Look, Explore | No | No | 5.6  
Amazon SageMaker Infer | Perform an inference using Amazon SageMaker. | No README available | No article available | None | Query | Look, Explore | No | Yes | 5.6  
Amazon SageMaker Train: Linear Learner | Start a training job on Amazon SageMaker, using the Linear Learner algorithm. | No README available | No article available | None | Query | Look, Explore | No | Yes | 5.6  
Amazon SageMaker Train: Xgboost | Start a training job on Amazon SageMaker, using the Xgboost algorithm. | No README available | No article available | None | Query | Look, Explore | No | Yes | 5.6  
Amazon Web Services EC2 Stop Instance | Stop an EC2 Instance using the Amazon EC2 API. | View README on GitHub | aws_resource_id | Field, query | Look, Explore | No | No | 5.6  
Auger | Use query result to build a predictive model. | View README on GitHub | See README | None | Query | Look, Explore | No | Yes | 5.24  
Azure Storage | Send and store a data file on Azure Storage. | View README on GitHub | None | Query, dashboard | Look, Explore, dashboard | No | Yes (for queries), No (for dashboards) | 5.6  
Braze | The Braze action lets you flag users within Braze using the REST API Endpoint from a Look. Ensure there's a `braze_id` field tagged in the results. MAX EXPORT: 10000. | View README on GitHub | See README | braze_id | Query | Look, Explore | No | Yes | 5.6  
DataRobot | Send data to DataRobot and create a new project. | See README | None | Query | Look, Explore | No | Yes | 5.24  
DigitalOcean — Stop Droplet | Stop DigitalOcean process using the DigitalOcean API. | View README on GitHub | digitalocean_droplet_id | Field, query | Look, Explore | No | No | 5.6  
DigitalOcean Spaces | Send to and store a data file in DigitalOcean Storage. | View README on GitHub | None | Query, dashboard | Look, Explore, dashboard | No | Yes (for Looks and Explores), No (for dashboards) | 5.6  
Dropbox | Send and store a data file on Dropbox. | No README available | View documentation | None | Query, dashboard | Look, Explore, dashboard | Yes | No | 6.8  
Facebook Custom Audiences | Upload data to Facebook Ads Custom Audiences from Customer List. | See README | None | Query | Look, Explore | Yes | Yes | 6.10  
Firebase | Use Firebase to send push notifications to mobile. | No README available | No article available | None | Query | Look, Explore | No | No | 22.4  
Google Ads Customer Match | Upload data to Google Ads Customer Match. | None | Query | Look, Explore | Yes | Yes | 6.10  
Google Analytics Data Import | Upload data to a Google Analytics dataset. | See README | None | Query | Look, Explore | Yes | Yes | 6.10  
Google Cloud Storage | Write data files to a Google Cloud Storage bucket. | None | Query, dashboard | Look, Explore, dashboard | No | Yes (for Looks and Explores), No (for dashboards) | 5.6  
Google Drive | Send data to Google Drive. | No README available | None | Query, dashboard | Look, Explore, dashboard | Yes | Yes (for Looks and Explores), No (for dashboards) | 7.4  
Google Sheets | Send CSV data to a Google Sheet. | No README available | None | Query | Look, Explore | Yes | Yes | 7.4  
Hubspot Companies | Add properties to your Companies using the Hubspot V3 API. | View README on GitHub | See README | hubspot_company_id | Query | Look, Explore | No | Yes | 5.6  
Hubspot Contacts | Add properties to your Contacts using the Hubspot V3 API. | View README on GitHub | See README | hubspot_contact_id | Query | Look, Explore | No | Yes | 5.6  
Kloudio | Add data to a Google Sheet. | View README on GitHub | See README | None | Query | Look, Explore | No | No | 5.6  
mParticle | Bulk export your user or event data from Looker to mParticle. | View README on GitHub | See README | See README | Query | Look, Explore | No | Yes | 5.6  
Salesforce Campaigns | Add contacts or leads to Salesforce campaign. | See README | sfdc_contact_id or sfdc_lead_id | Query | Look, Explore | Yes | No | 22.6  
Segment Group | Add traits and/or users to your Segment groups. | View README on GitHub | View documentation | segment_group_id and user_id, or segment_group_id and segment_anonymous_id | Query | Look, Explore | No | Yes | 4.20  
Segment Identify | Add traits to your Segment users using Identify. | View README on GitHub | View documentation | email or user_id or segment_anonymous_id or segment_group_id | Query | Look, Explore | No | Yes | 4.20  
Segment Track | Connect to a number of integrations provided by Segment to identify and target users for marketing workflows. | View README on GitHub | View documentation | email or user_id or segment_anonymous_id or segment_group_id | Query | Look, Explore | No | Yes | 4.20  
SendGrid | Send data and schedule results to send to an email address using SendGrid's API. | View README on GitHub | None | Query, dashboard | Look, Explore, dashboard | No | No | 5.6  
Slack | Send Looker content in direct messages, public channels, and private channels in Slack using OAuth. It is available for Looker-hosted deployments on 6.24+ with the IP Allowlist feature disabled. | No README available | View documentation | None | Query, dashboard | Look, Explore, dashboard | Yes | Yes (for Looks and Explores), No (for dashboards) | 6.24  
Slack Attachment (API Token) | Send data directly into a Slack channel along with user credentials. You may also want to reference Lookerbot documentation for additional Slack functionality. | None | Query, dashboard | Look, Explore, dashboard | No | No | 5.6  
Teams — Incoming Webhook | Send data to Microsoft Teams using an incoming webhook. | View README on GitHub | See README | None | Query, dashboard | Look, Explore, dashboard | No | No | 5.6  
Tray | Connect to a number of integrations provided by Tray.io to automate workflows. | View README on GitHub | View Community article | None | Query | Look, Explore | No | Yes | 5.6  
Twilio — Send Data | Send data from a Look or schedule results to send to a phone number using Twilio's API. | View README on GitHub | None | Query | Look, Explore | No | No | 5.6  
Twilio — Send Message | Send a message to a series of phone numbers (data columns that are tagged as phone numbers) in a Look. | View README on GitHub | See README | phone | Field, query | Look, Explore | No | No | 5.6  
Zapier | Connect to a number of integrations that are provided by Zapier to automate workflows. | View README on GitHub | None | Query | Look, Explore | No | Yes | 5.6  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


