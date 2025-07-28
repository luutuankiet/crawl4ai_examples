# Connecting to Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-studio-connector

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Connecting to Looker Studio
Stay organized with collections  Save and categorize content based on your preferences. 
With the Looker connector in Looker Studio, you can create a data source that lets you view and analyze data from a Looker Explore within Looker Studio.
Looker users who are less familiar with using Looker Studio may want to refer to the Looker and Looker Studio shared terms and concepts documentation page for more information about the nuances between similar terms and concepts in Looker and Looker Studio.
## Before you begin
A Looker data source in Looker Studio must be an Explore from a Looker instance that meets the requirements, which are listed on the Looker connector requirements, limits, feature support, and troubleshooting documentation page.
Only a Looker admin can enable the Looker connector for a Looker instance.
To interact with a Looker data source in Looker Studio, users must meet the permissions and roles requirements listed on the Overview of Looker connector permissions documentation page.
## Enabling and using the connector
To enable the connector, follow these steps:
  1. Navigate to the **BI Connectors** page in the **Platform** section of the Looker **Admin** panel.
  2. Either enable the **All Looker BI Connectors** setting or the **Looker Studio** setting. In Looker (Google Cloud core) instances, these settings are enabled by default.


## Disabling the connector
To disable the connector, follow these steps:
  1. Navigate to the **BI Connectors** page in the **Platform** section of the Looker **Admin** panel.
  2. Either disable the **All Looker BI Connectors** setting or the **Looker Studio** setting.


## Monitoring the Looker connector for Looker Studio
A Looker admin can view Looker Studio usage by using the **Query API Client Properties** group of fields in the System Activity History Explore. An entry is created in the **History** Explore every time a new query is run.
In the **Query API Client Properties** dimension group under the **History** view, the following fields are relevant to Looker Studio:
  * **API Client Name** — This field will always show `Looker Studio` to identify Looker Studio entries.
  * **Looker Studio Dashboard ID** — This field shows the ID of the Looker Studio report that issued the query.
  * **Looker Studio Datasource ID** — This field shows the ID of the data source in Looker Studio that is being queried.


The following example shows a System Activity URL that indicates Looker Studio usage. Replace `<instance_name.looker.com>` with your instance URL.
```
https://<instance_name.looker.com>/explore/system__activity/history?fields=query_api_client_context.name,query_api_client_context.ls_dashboard_id,query_api_client_context.ls_datasource_id,user.name,history.created_date,history.created_time_of_day&f[query_api_client_context.name]=looker%20studio&sorts=history.created_time_of_day+desc&limit=5000

```

## What's next
After you have enabled the connector, Explores in the Looker instance are available to use as data sources in Looker Studio.
See the Connect to Looker documentation page for information about using the Looker connector to add a Looker Explore as a data source in a Looker Studio report.
## Additional resources
  * Admin settings – BI Connectors
  * Connect to Looker
  * Understand Looker Explore data on a Looker Studio report


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


