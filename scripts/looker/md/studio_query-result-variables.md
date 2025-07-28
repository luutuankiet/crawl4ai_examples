# Query result variables  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/query-result-variables

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Create a query result variable
  * Edit and manage query result variables
  * Duplicate a query result variable
  * Delete a query result variable
  * Related resources




Was this helpful?
Send feedback 
#  Query result variables
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Create a query result variable
  * Edit and manage query result variables
  * Duplicate a query result variable
  * Delete a query result variable
  * Related resources


Query result variables let you insert data directly into text elements. For example, you could add text that describes a data point to your report, and then include that data point in the text as a chip. A query result chip updates its value when fresh data is available.
## Create a query result variable
To create a query result variable, follow these steps:
  1. Edit your report.
  2. Add text to your report, or edit an existing text element.
  3. Enter `@` to open the variable insert menu.
  4. Click **Add a variable** to open the **Create variable** dialog.
  5. Give your variable a unique name.
  6. In the **Data Source** section, select the data source that the query should start from.
  7. Create a query that returns the data point you'd like to display. 
     * You can add or remove dimensions in the **Dimension** section.
     * You can change or remove the selected metric in the **Metric** section. You can select up to one metric.
     * You can add or remove filters in the **Filters** section.
     * You can change the sorting of the table in the **Sort** section.
  8. In the **Select** section, select the column and row that contains the data point that you'd like to return. You can also click directly on a cell in the data table to select it.
  9. Optionally, edit the **Font color** and **Background color** settings of the query result chip. The **Preview** section displays how the chip will look.
  10. Click **Save**.


Looker Studio inserts the query result chip into the text element. Whenever a user views this text element, the data value is updated.
## Edit and manage query result variables
To edit a query result variable directly from a report page, follow these steps:
  1. Edit your report.
  2. Select the text field containing the variable, then click the variable.
  3. Click the **Edit variable** icon.
  4. Make any changes to the query or format of the query result variable.
  5. Click **Save**.


To edit a query result variable from a list of all variables, follow these steps:
  1. Edit your report.
  2. Click the **Resource** menu, and then select **Manage variables (parameters)**.
  3. Next to the query result variable that you'd like to edit, click **Edit**.
  4. Make any changes to the query or format of the variable.
  5. Click **Save**.


## Duplicate a query result variable
To duplicate a query result variable, follow these steps:
  1. Edit your report.
  2. Click the **Resource** menu, and then select **Manage variables (parameters)**.
  3. Next to the query result variable that you'd like to duplicate, click **Duplicate**.
  4. Make any changes to the query or format of the variable.
  5. Click **Save**.


## Delete a query result variable
To delete a query result variable directly from a report page, follow these steps:
  1. Edit your report.
  2. Click or hold the pointer over the query result chip, and then click the **Delete** icon.


To delete a query result variable from a list of all variables, follow these steps:
  1. Edit your report.
  2. Click the **Resource** menu, and then select **Manage variables (parameters)**.
  3. Next to the query result variable that you'd like to delete, click **Delete**.
  4. In the confirmation dialog, click **Remove variable**.


## Related resources
  * Add text, images, lines, and shapes to your reports


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


