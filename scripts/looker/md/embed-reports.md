# Embed Looker reports  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/embed-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to know about embedding reports
  * Requirements and permissions
  * Development requirements
  * View embedded reports
  * Provide feedback and report issues
  * Related resources




Was this helpful?
Send feedback 
#  Embed Looker reports
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to know about embedding reports
  * Requirements and permissions
  * Development requirements
  * View embedded reports
  * Provide feedback and report issues
  * Related resources


Looker lets you embed Explores, reports, Looks (saved visualized query results), and dashboards (collections of tiles that show visualized query results) in any HTML-formatted web page, portal, or application. You can embed Looker reports with the private embed or signed embed methods. Like other Looker content, access to embedded reports is controlled by access levels and user permissions.
This page guides you through the methods and requirements of embedding reports. Read the following sections to learn about these concepts:
  * Things to know about embedding reports
  * Requirements and permissions
  * View embedded reports
  * Embed reports
  * Related resources


## Things to know about embedding reports
In addition to the requirements and permissions, which are described next, there are several things to know about embedding reports:
  * Embedding for reports is available only for Looker-hosted Looker (original) instances.
  * Embedded reports are _view only_. Reports can be edited only within the Looker application.
  * The permissions that can be implemented for reports that are embedded with the signed embed method are limited to content permissions (`access_data`, and `see_looks` or `see_user_dashboards` permissions) and folder access.


The following features are not available for embedded reports:
  * Downloading of embedded reports
  * Printing of embedded reports
  * Scheduling of embedded reports
  * Alerting for embedded reports
  * Custom theming of embedded reports
  * Mobile embedding of reports


## Requirements and permissions
Embedding reports requires that the following features be enabled:
  * The **Looker reports** feature
  * The **Embedding Looker Reports** labs feature


Embed users must have the following types of access to see embedded reports:
  * The `access_data`, and `see_looks` or `see_user_dashboards` permissions
  * **View** or **Manage Access, Edit** access to the parent folder where an embedded report is saved.


## Development requirements
Detailed instructions for setting up a development server, in addition to development considerations for reports, can be found in the Looker Embed SDK GitHub repository.
## View embedded reports
Users can navigate folders and view embedded reports the same way that they can view other embedded Looker content.
See Move, share, and copy reports for more information about the access and permissions that are required to move, copy, and delete reports.
## Embed reports
You can embed reports by using the private embed, cookieless embed and signed embed methods. The process for embedding a report using private embed or signed embed is the same as for embedding a dashboard or a Look. For example, the URL for a report is `https://instance_name.cloud.looker.com/reporting/bafbc704-c8fd-4ebc-aa57-21c4fe407e0b`. The format for the URL is as follows:
  * **Host name**: The name of your Looker instance. For example: `https://instance_name.cloud.looker.com`
  * **Path**: The name of the folder that a report is saved in, called `reporting`, and the ID of the report. For example: `/reporting/bafbc704-c8fd-4ebc-aa57-21c4fe407e0b`


To construct an embed URL, prefix the folder name and report ID in the URL with `/embed/`, like you would for a dashboard or a Look. For example, `https://instance_name.cloud.looker.com/embed/reporting/bafbc704-c8fd-4ebc-aa57-21c4fe407e0b`.
## Provide feedback and report issues
If you experience an issue with embedding Looker reports, or would like to provide feedback, submit a feedback form.
## Related resources
  * Get started with private embedding
  * Getting started with embedding — enabling signed embedding
  * Private embedding
  * Signed embedding
  * Cookieless embedding
  * Introduction to the Embed SDK


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


