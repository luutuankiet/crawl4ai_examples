# Connect to YouTube Analytics  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/connect-to-youtube-analytics

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How to connect to YouTube Analytics
    * Connection options
  * Configure the data source
  * Control who sees the data
  * Create a new report from the data source
    * New to Looker Studio?
  * Related resources




Was this helpful?
Send feedback 
#  Connect to YouTube Analytics
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How to connect to YouTube Analytics
    * Connection options
  * Configure the data source
  * Control who sees the data
  * Create a new report from the data source
    * New to Looker Studio?
  * Related resources


YouTube allows billions of people to discover, watch, and share original videos content.
Anyone with a Google Account can upload videos to a YouTube channel. The YouTube Analytics connector lets you use Looker Studio to report on analytics data about the YouTube channels you own.
## How to connect to YouTube Analytics
  1. Sign in to Looker Studio.
  2. On the Looker Studio home page, in the top left, click add **Create** , and then select **Data Source**.
  3. Select the **YouTube Analytics** connector.
  4. If prompted to grant Looker Studio access to your account, click **AUTHORIZE**.
> You can revoke this access at any time.
  5. Select a connection option (described below) and provide your connection details.
  6. In the upper right, click **CONNECT**.
    1. The data source fields panel appears.
    2. The data source is now connected to your data set.


### Connection options
When creating a YouTube Analytics data source, you can connect to your YouTube channel data in the following ways:
#### All
The **All** option provides a list of all the accounts and channels to which you have access.
#### My Channel
The **My Channel** option provides a list of the channels associated with your current Google Account.
#### Content Owners
If you use YouTube's Content ID Matching system, you are considered to be a YouTube Content Owner. You can manage multiple channels, and allow other users to access this channel data on your behalf. The Content Owners option provides a list of all the content owner accounts to which you have access. Selecting an account will then show you a list of your channels.
#### Advanced
Use the **Advanced** option to specify either a channel or a content owner ID directly.
## Configure the data source
The data source fields panel is where you configure the data source by renaming fields and adding descriptions, adding calculated fields, and changing data types and aggregations. Learn more about working with data source fields.
## Control who sees the data
At the top of the fields panel, you can change the data credentials. Credentials control who can see the data that this data source provides.
**OWNER'S CREDENTIALS** let other people view or create reports that use this data without requiring them to have their own access to the dataset.
**VIEWER'S CREDENTIALS** , on the other hand, require each user of the data source to provide their own credentials to access the dataset.
**SERVICE ACCOUNT CREDENTIALS** rely on a special type of Google Account that represents a non-human user that can authenticate and be authorized to access data.
Learn more about data credentials.
## Create a new report from the data source
To create a new report from the data source, follow these steps:
  1. In the upper right, click **CREATE REPORT**. The report editor appears.
  2. Click **ADD TO REPORT**. 
    1. This action adds the data source to the report.
    2. You can now create charts and controls that get their data from this data source.


### New to Looker Studio?
Take the Create a report tutorial.
## Notes
Only 50 channels are displayed in the **Content Owners** and **Google+ Pages** options. Use the advanced option to access other channels.
To protect viewer privacy, if there are fewer than 10 viewers of a video, country and state data won't appear in the report.
On March 31, 2025, YouTube changed the way views are calculated: the Views metric will count the number of times a Short starts to play or replay, with no minimum watch time requirement. If you created a data source before this date, you don't need to take any action: the changes are automatically applied to your data source.
The existing Shorts view metric, now called "Engaged views," is available in YouTube Analytics. We will add this metric to Looker Studio in the coming months.
Learn more about the change to YouTube Shorts views.
## Related resources
  * Create a data source
  * Learn more about YouTube


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


