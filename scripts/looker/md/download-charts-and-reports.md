# Download Looker reports  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/download-charts-and-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to know about downloading charts and reports
  * Download individual charts
  * Download entire reports




Was this helpful?
Send feedback 
#  Download Looker reports
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to know about downloading charts and reports
  * Download individual charts
  * Download entire reports


This page guides you through the components of downloading Looker reports. You can download individual charts in CSV or Excel format and entire reports in PDF format. Read the following sections to learn about these concepts:
  * Things to know about downloading charts and reports
  * Download individual charts
  * Download entire reports


## Requirements
To download charts and reports, users must have either the Looker **Admin** role or the following content and data access:
  * One of the following types of access to the folder in which a report is saved: 
    * View
    * Manage Access, Edit
    * The `download_with_limit` or `download_without_limit` permission
  * Access to the underlying LookML model, if a chart or report includes a Looker data source


For more information about content access and permissions, see Controlling user content access and How content access and permissions interact.
If you want to change the access level settings for a folder, see Viewing and managing folder access levels.
## Things to know about downloading charts and reports
There are several things to know about downloading charts and reports in Looker:
  * Individual charts can be downloaded only in CSV or Excel style formats.
  * Entire reports can be downloaded only in PDF format.
  * The limit for data downloads for users, including those with the `download_without_limit` permission, is 5,000 rows.
  * When a report link is included in a downloaded PDF, users will be directed to that specific report within Looker. Users _must_ have access to the folder in which the report is saved to view the report in Looker.
  * If a user is not granted the required permissions, they won't see the option to download content.
  * If a user does not have the required model access to Looker data on a report, that data won't be included in downloads.


## Download individual charts
To download content from an individual chart in CSV or Excel format, follow these steps:
  1. Open the report that contains the data that you want to download.
  2. Click the chart's more_vert three-dot menu.
  3. Click **Export** to open the **Export data** dialog.
  4. In the **Export data** dialog, enter a name for the download in the **Name** field.
  5. Choose an option in the **Export as** section. The options include the following:
     * CSV
     * CSV (Excel)
     * Google Sheets
  6. Click the check_box **Keep value formatting** checkbox to carry over the value format settings from the chart to the exported file.
  7. Click **Export** to export the file, or click **Cancel** to close the dialog.


## Download entire reports
To download an entire report as a PDF, follow these steps:
  1. Open the report that contains the data that you want to download.
  2. Click group_add **Share** in the report banner.
  3. Click download **Download** to open the **Download as PDF** dialog.
  4. Click the check_box checkboxes to enable or disable the following export settings:
     * **Ignore custom background color** : Select this option to override any background color settings on the report.
     * **Add a link back to the report** : Select this option to include a link to the report in Looker. See the Things to know about downloading charts and reports section on this page for more information about including links in downloads.
     * **Password protect report** : Select this option to set a password for the PDF file.
  5. Click **Download** to download the PDF, or click **Cancel** to close the dialog.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


