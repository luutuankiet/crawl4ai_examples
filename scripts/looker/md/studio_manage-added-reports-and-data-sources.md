# Manage added reports and data sources  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/manage-added-reports-and-data-sources

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Manage added data sources
    * Add a data source
  * Manage added reports
  * Related resources




Was this helpful?
Send feedback 
#  Manage added reports and data sources
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Manage added data sources
    * Add a data source
  * Manage added reports
  * Related resources


## Manage added data sources
  1. Edit your report.
  2. Select **Resources** arrow_forward_ios **Manage added data sources**.


You'll see the following information:
### Type
**Embedded** data sources are part of the report and can only be used in the report in which they were created. You can edit the data source from within the report. If you share or copy the report, all of its embedded data sources are shared and copied, as well. Learn more.
**Reusable** data sources exist as separate assets and can be used in multiple reports. You can edit a reusable data source from within the report, or from the Looker Studio home page.
### Used in report
Shows the number of charts using each data source.
### Status
Shows whether the data source is working properly or if there is a problem with the data source connection.
#### Problems with the connection
If you see problems with the data source connection, it may mean that the report-data source claim has been broken. Charts based on this data source will display the message "Failed To Get Data. The data source needs to be added to the report."
This can happen when the person who added the data source to the report leaves your organization, or has their permission to access the data source removed. In this case, someone else with permission to access that data source needs to add it back before those charts will work again. If you have this permission, you'll see a link to request access.
### Edit
Click this link to edit the data source. For a reusable data source, you must have edit access to that data source.
### Remove
If you added the data source to the report, you can remove it and release your claim to that data source. Any components that used that data source will show an alert instead of data.
To fix any broken charts or controls, you can:
  * Add the data source back to the report.
  * Select a different data source for the affected charts or controls.
  * Delete the affected charts or controls.


Note that changing a component to use a different data source does not remove the original one from the report.
### Add a data source
Click **ADD A DATA SOURCE**.
  1. To create a new data source: 
    1. The **Connect to data** tab lets you select a connector, create a new data source, and add that to your report: 
      1. Select the type of data you want to visualize.
      2. Provide your account or other details.
      3. In the bottom right, click **Add**.
  2. The **My data sources** tab lets you add an existing data source to your report: 
    1. Locate the data source you want.
    2. In the bottom right, click **Add.**


## Manage added reports
To see the reports which use a particular data source:
  1. Sign in to Looker Studio.
  2. Navigate to the **Data sources** tab.
  3. Locate the data source that you want to manage, and then click more_vert **More option**.
  4. Click **Manage Added Reports**.


  * **Status** shows if the data source has been added properly. If not, an alert icon will appear.
  * **Used in report** shows if there are charts or controls that reference the data source. This can help you make sure it's safe to remove a data source
  * Add a data source back to the report by clicking **Add** in the Action column.
  * Remove a data source from the report by clicking remove_circle_outline **Remove report from datasource**.


## Related resources
  * Add data to a report
  * Edit a data source
  * Change the data source for a chart, page, or report
  * Remove and restore a data source


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


