# Connect to Looker  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/connect-to-looker

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Use the Looker connector to add a Looker Explore as a data source
    * Connect to a Looker instance
    * Select a model and an Explore
    * Add the Looker data source to a report
  * Related resources




Was this helpful?
Send feedback 
#  Connect to Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Use the Looker connector to add a Looker Explore as a data source
    * Connect to a Looker instance
    * Select a model and an Explore
    * Add the Looker data source to a report
  * Related resources


The Looker connector lets you add a Looker Explore as a data source so that you can analyze Looker data from within Looker Studio. This document describes how to create a data source with data from a Looker (original) instance or from a Looker (Google Cloud core) instance that uses a public IP network connection.
## Before you begin
Your Looker instance must fulfill certain requirements to be eligible to connect to Looker Studio. Additionally, a Looker Admin must enable the **Looker Studio** BI connector in the **Platform** section of the instance's **Admin** panel.
To add a Looker Explore as a data source in Looker Studio, you must have `explore` permissions for the model that contains the Explore.
A Looker data source uses viewer's data credentials, so any user viewing Looker data in Looker Studio must have at least `access_data` and `clear_cache_refresh` permissions for the model that contains the data source's Looker Explore.
Learn more about the Looker permissions that are required to enable the Looker connector, create a Looker data source, and view Looker data in Looker Studio.
## Use the Looker connector to add a Looker Explore as a data source
To add a Looker Explore as a data source for a Looker Studio report, you must complete the following tasks:
  1. Connect to a Looker instance and link your Looker and Google accounts.
  2. Select a Looker model and Explore.


Each Looker data source represents a single Looker Explore. You can add multiple Explores to a Looker Studio report, even those that don't belong to the same Looker model.
### Connect to a Looker instance
To connect to a Looker instance, follow these steps:
  1. Sign in to Looker Studio.
  2. On the Looker Studio home page, in the top left, click **Create** , and then select **Data Source**.
  3. Select the Looker connector.
  4. Enter the URL for the Looker instance that contains the Looker Explore that you want to connect to. This is the URL that you use to access Looker on your browser.
    1. If the instance URL belongs to a Looker instance that doesn't meet the Looker connector requirements, Looker Studio displays the message `Invalid Looker URL or the Looker URL does not support account linking. Please use different Looker URL.`
    2. If you have previously connected a Looker instance as a data source, that Looker instance name appears under **Saved Looker Instances**. You can click the name of a Looker instance and proceed to the section on selecting a model.
  5. Click **Connect Looker Account**.
  6. In the authorization menu, click **Agree and continue** to link your Google Account credentials to your Looker account credentials. You can link one Google Account to one Looker account for each Looker instance that you connect to Looker Studio.
  7. In the Looker instance menu, click **AUTHENTICATE** ​​.


Now you're ready to select a model–Explore pair to connect to as a data source for your report.
### Select a model and an Explore
Once you have connected to a Looker instance, a list of models that are defined in that instance automatically populates a new panel that is called **Models** in the **Add data to report** windows.
To select a model, follow these steps:
  1. In the **Models** panel, scroll the list of pre-populated models, or click the magnifying glass icon to open a search field where you can enter the name of a specific model. Hover over a model name to see the model filename as it appears in the Looker project. Click the model name to select the model. A new panel will populate with the list of Explores that are defined within that model.
  2. To select an Explore, scroll the list or click the magnifying glass icon to open a search field where you can enter the name of a specific Explore. Hover over an Explore name to see the `explore` parameter value as it's declared in the model file. Click the Explore name to select the Explore.
  3. Click **CONNECT**.


It may take a few minutes to connect to the Looker Explore. Once it is connected, the data source has the format `Explore – model`. Learn more about how Looker Explores appear and behave in Looker Studio reports.
### Add the Looker data source to a report
To add the data source to a report, you can choose one of the following options:
  * Select **CREATE REPORT** to create a report that includes a chart that is pre-populated with some fields from this data source.
  * Select **EXPLORE** to open a blank report that uses the Looker data source.


You're now ready to view and interact with Looker data in your report.
Once you have created your Looker data source and added it to a report, Looker Studio displays a list of the fields that are associated with the Looker Explore. From this list, you can perform the following tasks:
  * Change the data source type from an embedded data source to a reusable data source.
  * Update the data source data freshness. The the default data freshness value for a Looker data source is 12 hours.
  * Manage whether other report editors can edit the field definitions at the chart level for reports that use this data source.
  * Make a copy of the data source.


## Related resources
  * Create a data source
  * Exploring data in Looker 
  * Connecting to Looker Studio
  * Looker and Looker Studio shared terms and concepts


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


