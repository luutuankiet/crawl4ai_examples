# Quick start guide  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/quick-start-guide

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Start with a report
  * Add data to the report
    * Create a new data source
    * Connect to an existing data source
  * Add charts and controls to the report
  * View your report
  * Share the report
  * Share the data source




Was this helpful?
Send feedback 
#  Quick start guide
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Start with a report
  * Add data to the report
    * Create a new data source
    * Connect to an existing data source
  * Add charts and controls to the report
  * View your report
  * Share the report
  * Share the data source


This page explains six key steps that will help you to quickly get started using Looker Studio.
##  Start with a report
Reports let you visualize your data, gain insights, and share those insights with others.
When you sign in to Looker Studio, the home page appears with the **Reports** tab selected. All the reports that you have access to appear in the middle of the screen. The plus buttons let you create a new blank report, or you can start with one of the pre-built report templates along the top.
### View a report
To view a report that's been shared with you, click the report name in the list in the middle of the screen.
### Edit a report
To edit a report, follow these steps:
  1. View a report.
  2. In the upper right corner, click **Edit** .


If you don't see an **Edit** button, then the report has been shared with only "Can View" access. If the owner of the report has allowed it, you can make a copy, which you can then edit.
### Create a report
To create a report, follow these steps:
  1. In the top left, click **Create**.
  2. Select **Report**.


The report editor will open with the **Add data to report** panel open.
##  Add data to the report
Data sources connect to your data and let you configure the fields that you can use in your report.
When you create a new report, the **Add data to report** panel opens. This lets you create a new data source or add an existing data source.
### Create a new data source
For example, you might want to connect to a BigQuery public data set (to complete this step, you'll need a Google Cloud project that is associated with a valid Google Cloud billing account).
To create a new BigQuery data source, follow these steps:
  1. In the **Add data to report** ** panel, click **Connect to data**.
  2. Select the BigQuery connector.
  3. If prompted, click **Authorize** to allow Looker Studio to access your data on your behalf.
  4. Select **Public datasets**.
  5. Select your **Billing project**.
  6. Select the **faa** public dataset.
  7. Select the **us_airports** table.
  8. In the lower right corner of the screen, click **Add** , then confirm that you want to add the new data source to your report.
  9. The report editor will appear, and a table with fields from your data source will be placed on the canvas.
  10. To customize the table's data and style, on the right side of the screen, use the **Properties** panel.
  11. To rename your report, in the top left corner of the screen, click **Untitled report** and enter a new name.


### Connect to an existing data source
For example, you might want to connect to the sample Google Analytics data source that comes with Looker Studio.
To connect to an existing Google Analytics data set, follow these steps:
  1. In the **Add data to report** panel, click **My data sources**.
  2. Select the **Sample Google Analytics Data** data source.
  3. In the lower right corner of the screen, click **Add** , and then confirm that you want to add the new data source to your report.
  4. The report editor will appear, and a table with fields from your data source is placed on the canvas.
  5. To customize the table's data and style, on the right side of the screen, use the **Properties** panel.
  6. To rename your report, in the top left corner of the screen, click **Untitled report** and enter a new name.


##  Add charts and controls to the report
To add components to a report canvas, follow these steps:
  1. In the toolbar at the top of the editor, click **Add a chart** and then select a chart from the list.
  2. Click the canvas where you want the chart to appear.
  3. Move and resize the chart, as desired.
  4. Add or change the dimensions and metrics by clicking the fields in the properties panel, or dragging and dropping them from the data panel (to the right of the chart panel) directly onto the chart.
  5. You can also create new charts by dragging a field from the data panel onto the canvas.


##  View your report
See your report the way it looks to other viewers.
View mode lets users see the data and use any interactive controls that you've placed on the report without being able to change the structure of the report. If you can edit a report, you can switch between view mode and edit mode.
To enter view mode from edit mode, click **View** .
To return to edit mode from view mode, click **Edit** .
##  Share the report
Share reports with other viewers. Collaborate with other editors.
To share a report with users, follow these steps:
  1. In the upper right, click **Share** .
  2. Specify the people or groups with whom you want to share your report.
  3. Use the advanced options to change how individual addresses can access the report.


##  Share the data source
Let other people create their own reports that are based on your data source.
To share a data source, you must access it directly from the **Data Sources** page (not through the report). You must be signed into a Google account to view or edit a data source.
To share a data source, follow these steps:
  1. In the upper left of your report, return to the Looker Studio home page by clicking the Looker Studio logo .
  2. On the left, click **Data Sources**.
  3. Locate the data source that you want to share.
  4. On the right, click **More options**.
  5. Click **Share** .
  6. Specify the people or groups with whom you want to share your data source.
  7. Use the advanced options to change how individual addressees can access the data source.


## Key concepts
Here's a recap of the terms and concepts used in on this page and throughout the Looker Studio documentation.
Concept  |  What it does   
---|---  
Report  |  A Looker Studio asset that contains a collection of **components** whose purpose is to present to viewers information and insights derived from your data.  Learn more  about reports .   
Component  |  A widget that you add to a report to display your data, such as **charts** , **tables** , and interactive **date range controls** and **filter controls**. Data components get their information from a **data source**.  You can also annotate your report with **text** , **shape** , **image** , and  embedded content  components.   
Connector / Data source  |  In Looker Studio, connecting to your data involves the following components: 
  * **Connectors** connect Looker Studio to your underlying data. Connecting to your data creates a **data source** in Looker Studio. 
  * **Data sources** represent a particular instance of a connector: for example, a connection to a specific BigQuery table or query, a Google Analytics property, or Google Sheets. Data sources let you configure the fields and options provided by the connector used to create that connection instance. In addition, the data source gives you a secure way to share information and insights with report viewers who may not be able to directly access the underlying data. 

Learn more about  connecting to your data .   
Field  |  A column of data.  Looker Studio uses two basic types of fields: 
  * **Dimensions** are things that you want to measure, or that serve as ways to categorize your data. 
  * **Metrics** are numbers that measure the things that are contained in dimensions. 

Learn more about  fields in reports .   
Credentials  |  The mechanism by which a data source determines who can see the data it provides.  Learn more about  data source credentials .   
View mode / Edit mode  | 
  * **Edit mode** allows you to edit the structure of a report and change, add, or remove data sources, and to use interactive controls. 
    * People who can edit a report or data source are referred to as **editors**. 
  * **View mode** lets you see all the data that you are authorized to see, and to use interactive controls. View mode does not allow you to modify the report structure. 
    * People who can only view a report or data source are referred to as **viewers**. 

  
Sharing and access permissions  |  When you share reports and data sources, you determine how other people can access the asset: 
  * **Can edit** access lets people modify and share the asset (making them **editors** ). 
  * **Can view** access lets people view the asset, but they can't modify or share it (making them **viewers** ). 

The advanced sharing options let you control other aspects of asset access, such as the ability to download the data or print the report.  The link sharing options let you share your assets more broadly around the internet.  Learn more  about sharing .   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


