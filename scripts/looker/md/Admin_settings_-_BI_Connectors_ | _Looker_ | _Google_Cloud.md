# Admin settings - BI Connectors  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/bi-connectors

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * All Looker BI Connectors
  * Connected Sheets
  * Microsoft Power BI




Was this helpful?
Send feedback 
#  Admin settings - BI Connectors
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * All Looker BI Connectors
  * Connected Sheets
  * Microsoft Power BI


The **BI Connectors** page in the **Platform** section of the **Admin** menu lets you enable or disable connections from Looker to other business intelligence (BI) applications.
In Looker (Google Cloud core) instances that use public IP or both public IP and private IP, the ability for Looker users to connect to other BI applications is enabled by default. Those with the Admin Looker role can use this page to disable any or all of these connectors.
In Looker (original), this ability is disabled by default. Looker admins can use this page to enable any or all of these connectors.
## Requirements
To view the **BI Connectors** page, the following requirements must be met:
  * Your Looker instance must be Looker-hosted.
  * Your Looker instance must be running Looker 22.20 or later. If your Looker instance is not hosted on Google Cloud, your instance must be running Looker 23.4 or later.
  * Your Looker instance must not use private IP only (either with private services access or Private Service Connect).
  * You must have the Admin role on your Looker instance.


## All Looker BI Connectors
Enable or disable the **All Looker BI Connectors** option to control connections to all BI applications to which Looker has a connection. When enabled, this option automatically enables all of the connectors on the Looker instance.
## Connected Sheets
Enable or disable this option to allow or disallow connections to Looker from Google Sheets. This option is automatically enabled if the **All Looker BI Connectors** option is enabled.
## Looker Studio
Enable or disable this option to allow or disallow connecting to Looker Studio from Looker Explores, monitoring System Activity information from Looker Studio data sources, and allowing connections from Looker Studio. This option is automatically enabled if the **All Looker BI Connectors** option is enabled.
## Microsoft Power BI
Enable or disable this option to allow or disallow connections to Looker from Microsoft Power BI. This option is automatically enabled if the **All Looker BI Connectors** option is enabled.
## Tableau Desktop
Enable or disable this option to allow or disallow connections to Looker from Tableau Desktop. This option is automatically enabled if the **All Looker BI Connectors** option is enabled.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


