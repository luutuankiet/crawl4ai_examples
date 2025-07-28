# Overview of permissions for Looker reports  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to know about permissions for Looker reports
  * Permissions for Looker reports




Was this helpful?
Send feedback 
#  Overview of permissions for Looker reports
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to know about permissions for Looker reports
  * Permissions for Looker reports


In addition to the requirements that a Looker instance must fulfill to enable the Looker reports feature, certain tasks that are related to the setup and use of Looker reports require specific Looker permissions. Additional permissions are required to view and use data from Looker data sources. Permissions are granted in the Looker instance by a Looker admin.
Read the following sections on this page to learn about Looker permissions for reports:
  * Things to know about permissions for Looker reports
  * Permissions for Looker reports


## Things to know about permissions for Looker reports
There are several things to know about how Looker permissions are applied to Looker report users:
  * Users _must_ have access to underlying LookML models to view or use data from Looker data sources in Looker reports.
  * User access to folders is controlled by access levels and user permissions. To change the access level settings for a folder, see Viewing and managing folder access levels.
  * See Controlling user content access and How content access and permissions interact to understand the additive nature of permissions and content access.


## Permissions for Looker reports
Looker admins can assign roles, permissions, and model sets to users and groups on the **Roles** page in the **Admin** panel.
In addition to default permission sets in Looker, you can create permission sets for Looker reports and model sets to assign to Looker reports users and groups.
See the following table for an overview of Looker permissions that control how users can interact with Looker report features.
Looker permission | Depends on | Type | Looker report task  
---|---|---|---  
`access_data`, `see_looks` | Model specific for Looker data sources |  Users can view Looker Explore data, and create reports from an Explore.  
`access_data`, `see_looks` | Model specific for Looker data sources |  Users can view reports in folders.  
`access_data`, `see_looks`, `save_content` | Instance wide |  Users can save and edit reports.  
`access_data`, `see_looks` | Model specific for Looker data sources |  Users can download reports, but _must_ specify a limit of 5,000 rows or fewer.  
`download_without_limit` |  `access_data`, `see_looks` | Model specific for Looker data sources |  Users can download reports without specifying a limit, up to a maximum of 5,000 rows.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


