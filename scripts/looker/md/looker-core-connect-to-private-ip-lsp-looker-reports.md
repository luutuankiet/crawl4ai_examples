# Connect to a Looker (Google Cloud core) instance that uses private IP from a Looker Studio Pro report or a Looker report

**Source:** https://cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-looker-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Connect to a Looker (Google Cloud core) instance
    * Find the Looker instance ID
    * Use the instance ID to connect from a report
  * Add or remove a public IP connection after connecting to Looker Studio Pro or Looker reports




Was this helpful?
Send feedback 
#  Connect to a Looker (Google Cloud core) instance that uses private IP from a Looker Studio Pro report or a Looker report
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Connect to a Looker (Google Cloud core) instance
    * Find the Looker instance ID
    * Use the instance ID to connect from a report
  * Add or remove a public IP connection after connecting to Looker Studio Pro or Looker reports


The Looker connector lets you add a Looker Explore as a data source so that you can analyze Looker data in a Looker report or a Looker Studio Pro report. This documentation page describes how to connect a Looker Studio Pro report or a Looker report to a Looker (Google Cloud core) instance that uses a Private IP only network connection by performing the following tasks:
  * Find the Looker instance ID
  * Use the Looker instance ID to set up a Looker data source


## Before you begin
Your Looker instance must fulfill certain requirements to be eligible to connect to Looker Studio. Additionally, a Looker admin must enable the **Looker Studio** BI connector in the **Platform** section of the instance's **Admin** panel.
To add a Looker Explore as a data source in Looker Studio, you must have `explore` permissions for the model that contains the Explore.
A Looker data source uses viewer's data credentials, so any user viewing Looker data in Looker Studio must have at least `access_data` and `clear_cache_refresh` permissions for the model that contains the data source's Looker Explore. Learn more about the Looker permissions that are required to enable the Looker connector, create a Looker data source, and view Looker data in Looker Studio.
## Connect to a Looker (Google Cloud core) instance
When connecting to a Looker (Google Cloud core) instance, you specify the Looker (Google Cloud core) instance by using either the instance URL or the instance ID, depending on the instance's network configuration:
  * Use the **Instance URL** to connect to instances that use a public IP network, including the following types of instances:
    * Private IP (private services access) and public IP
    * Private IP (Private Service Connect) and public IP


If your Looker (Google Cloud core) instance uses a public IP network, refer to the Connect to Looker documentation page for instructions on how to connect to your instance.
  * Use the **Instance ID** to connect to instances that use only a private IP network, including the following types of instances:
    * Private IP only (private services access)
    * Private IP only (Private Service Connect)


### Find the Looker instance ID
To find your Looker instance ID, from the Looker **Help** menu, select **Looker Instance ID**.
Looker displays the instance ID in the following format:
```
projects/PROJECT_ID/locations/REGION/instances/INSTANCE_NAME

```

The variables in the previous example represent the following information about your instance:
  * `PROJECT_ID`: The name of the Google Cloud project in which you created the Looker (Google Cloud core) instance.
  * `REGION`: The region in which your Looker (Google Cloud core) instance is hosted.
  * `INSTANCE_NAME`: The name of your Looker (Google Cloud core) instance; it isn't associated with the instance URL.


You can copy the instance ID to your clipboard by clicking the **Copy** button.
### Use the instance ID to connect from a report
Next, you can use the Looker connector to connect to a Looker (Google Cloud core) private IP (private services access) instance or a private IP (Private Service Connect) instance.
Within your report, perform the following steps:
  1. From the **Data** panel, select **Add data**.
  2. Select the Looker connector.
  3. In the **Enter Looker Instance URL/ID** field, enter the instance ID that you copied from your instance.


Once connected, you will see the instance listed in the **Saved Looker Instances** list, and it will be listed by the full instance ID.
## Add or remove a public IP connection after connecting to Looker Studio Pro or Looker reports
For instances that use private services access or Private Service Connect, admins can add or remove a public IP connection. Adding or removing a public IP connection has the following effects:
  * To create new connections to Looker (Google Cloud core) instances that have a public IP connection, you must use the instance URL. No network check is performed when data is accessed.
  * To create new connections to Looker (Google Cloud core) instances that don't have a public IP connection, you must use the instance ID. Private network enforcement is in place for data access.
  * Data sources that were created when a public IP connection was enabled will function only when a public IP connection is enabled. If the Looker (Google Cloud core) instance's public IP connection has been disabled, users must reconnect to the instance using the instance URL.
  * Data sources that were created when a public IP connection was disabled will function only when a public IP connection is disabled. Users must reconnect to the data source if the public IP connection has been enabled.


## Troubleshooting
If you receive an error while trying to connect to a Looker (Google Cloud core) private IP (private services access) only instance or to a private IP (Private Service Connect) only instance or data source, you may not be on the correct network to access the instance data. Select the same network as the one being used by the instance and retry the connection.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


