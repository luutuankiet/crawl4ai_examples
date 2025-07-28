# Downloading content  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/downloading

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Downloading data from a Look or an Explore
    * Number of rows and columns to include
    * Download or open in browser
  * Downloading data from a merged results query
  * Downloading data from a dashboard
    * Downloading a dashboard as a PDF
    * Downloading a dashboard as CSVs
    * Downloading data from dashboard tiles
  * For admins: Enabling downloading data for your Looker instance




Was this helpful?
Send feedback 
#  Downloading content
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Downloading data from a Look or an Explore
    * Number of rows and columns to include
    * Download or open in browser
  * Downloading data from a merged results query
  * Downloading data from a dashboard
    * Downloading a dashboard as a PDF
    * Downloading a dashboard as CSVs
    * Downloading data from dashboard tiles
  * For admins: Enabling downloading data for your Looker instance


This page describes downloading content — visualizations or data — from Looker.
To download content, you must be given the `download_with_limit` or `download_without_limit` permission by a Looker admin.
The process and options for downloading content and formatting downloaded content vary based on whether you're downloading from a Look or an Explore, from a dashboard, or from a merged results query.
## Downloading data from a Look or an Explore
To download data from a Look or an Explore page, select the gear menu in the upper right and select **Download**.
Looker displays the **Download** window, where you can name and format your download.
The following sections will walk you through each field in the **Download** window:
  * Data values
  * Number of rows and columns to include


### Format
> Downloads to formats that use the renderer (PNG and PDF) will use results from Production Mode. If your download is in another format, the download will show results from whichever mode — development or production — you are in.
Data can be downloaded from Looks and Explores in the following file formats:
  * TXT (tab-separated values)
  * Excel spreadsheet (Excel 2007 or later)
  * CSV
  * JSON
  * HTML
  * Markdown
  * PNG (image of visualization)


While choosing your data format for downloading, if you don't see the HTML or PNG (image of visualization) options (for Looks), talk to your Looker admin about installing the appropriate version of the Chromium renderer for your Looker instance.
For JSON format, Looker uses field labels as its rendered value in its JSON output. See the Change in JSON formatting Community post for more information about how Looker renders fields in JSON format.
Transposed tables will render in PNG downloads only.
For Looker developers, if you are in Development Mode, data downloads in most file formats query your model as it is in Development Mode. PDF and PNG file formats are the exception; data downloads in those file formats always query your model as if it is in Production Mode.
### Filename
You can enter a filename for the download or use the default filename that is pre-populated in the field. Looker will automatically append the appropriate file extension based on your selection in the **Format** field.
### Results
In the **Results** section, choose whether you want visualization settings applied to your TXT, Excel, CSV, JSON, HTML, or Markdown data download.
If you choose **With visualization options applied** , Looker applies some of the visualization settings to your download. Any of the following settings in the Plot, Series, and Formatting menus that are configured for the visualization will be applied to the data download:
  * Limit Displayed Rows to a maximum of 500 rows shown or hidden
  * Show Full Field Name
  * Custom labels for each column (Looker uses field labels as its rendered value in its JSON output. See the Change in JSON formatting Looker Community post for more information about how Looker renders fields in JSON format).
  * Conditional Formatting for downloads of table chart visualizations in Excel format


> Conditional formatting will display in Excel deliveries of Looks and Explores with table chart visualizations only if the **Along a scale Rule** is applied.
Some visualization settings are not applied to downloaded results. For example:
  * Custom header text color and background color are not applied to downloaded results, except for PNG files.
  * For results tables with pivots and multiple measures, each pivot value is repeated across columns rather than represented as one merged column. HTML and PNG downloads are an exception, so the merged column is preserved.
  * When you download from a dashboard, the dashboard tile title is not included in downloaded results.
  * The **Totals** and **Row Totals** values are included in downloaded results, but the respective row and columns are not labeled.
  * Subtotals won't be downloaded for queries that can't be streamed.


Columns in table charts that have been manually rearranged will appear in their original order in the download if the query includes any of the following elements:
  * fields that are deliberately hidden from the visualization
  * fields that are present in the underlying SQL but that are not present in the visualization, such as the following:
    * a dimension present in the visualization that contains a `link` parameter that references another field that is not present in the visualization.
    * a field that uses the `case` parameter.
    * a dimension that is present in the visualization that references another field with the `{{ field_name._value }} Liquid variable syntax`, which is not present in the visualization.
  * One or more fields with dimension fill enabled
  * Three or more pivoted fields
  * Row totals enabled
  * One or more fields that include the `order_by_field` LookML parameter in the field definition


If you choose **As displayed in the data table** , visualization options won't be applied and the download will appear like the data table in the **Data** section of the Look or Explore.
### Data values
In the **Data values** section, choose how you want the downloaded query results to appear:
  * If you choose **Unformatted** , Looker does not apply any special formatting of your query results, such as rounding long numbers or adding special characters your Looker developers may have put in place. This is often preferred when data is being fed into another tool for processing.
  * If you choose **Formatted** , the appearance of the data will be similar to the **Explore** experience in Looker, although some features (such as linking) aren't supported by all file types. For example, any formatting applied with the `html` parameter won't be applied to TXT, CSV, Excel, or JSON downloads.


### Number of rows and columns to include
You can choose how much data you want to download as follows:
  * **Current result table** : Number of rows that are specified by the row limit of your content.
  * **All results** : All results that are returned by the query. Before selecting this option, see the All Results section on this page.
  * **Custom** : A custom number of rows. Users who have `download_with_limit` permissions are limited to 5,000 rows. The limit for other users is typically 100,000.


#### All results
When you select **Run** in a Look or an Explore, Looker checks your permissions and determines whether the complexity of the query and the database dialect will allow the entire query to be downloaded. If you have the permissions (for results over a set limit) and if Looker determines that your entire query can be downloaded, the **All results** option will be available in the **Download** window.
The **All results** option is typically disabled for queries that do any of the following:
  * Involve row totals or table calculations
  * Use percent of total, percent of previous, or running totals types of measures
  * Retrieve data from a database dialect that cannot stream results
  * Include pivoted columns that Looker calculates because the data comes from a database dialect that cannot calculate the pivots


> Even when the **All results** option is available, you should still use caution when downloading all results. Some queries are very large, containing thousands or millions of rows, which can overwhelm most spreadsheet programs — or even your Looker instance.
If the **All results** option is unavailable, you can use the **Custom** option to specify the maximum number of rows that are allowed with your permissions.
##### Streaming query results
Streaming refers to Looker's ability to process data in chunks, rather than all at once. If Looker can stream a result set, then unlimited downloads are possible. The **All results** option relies on Looker's ability to stream results, and **All results** won't be available if streaming results isn't possible.
In addition to the format limitations, there are two cases where streaming is not possible:
  1. **Table calculations** : Table calculations cannot be streamed. Therefore, to download unlimited results for a query, you must remove table calculations from the query.
  2. **Database limitations** : Some databases cannot stream if pivots are included in the query. For these databases, you must remove pivots to download unlimited results. Some databases can't stream any results, which means that unlimited downloads are not possible.


These databases support streaming:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner  
Greenplum | Yes  
HyperSQL  
IBM Netezza  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA  
SAP HANA 2+  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
These are the databases that support streaming with pivots applied:
Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+  
Apache Hive 2.3+  
Apache Hive 3.1.2+  
Apache Spark 3+ | Yes  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality  
Databricks | Yes  
Denodo 7  
Denodo 8  
Dremio  
Dremio 11+  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL  
Google Spanner  
Greenplum | Yes  
HyperSQL  
IBM Netezza | Yes  
MariaDB  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI  
MySQL  
MySQL 8.0.12+  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA  
SAP HANA 2+  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
##### Remove all sorts from query
When you select **All Results** , you may also see the option to **Remove all sorts from query**. This option prevents sorting on your query before you download the results. Selecting this option may speed up your download, since sorting a query can be costly to performance for certain database types.
> The **Remove all sorts from query** option is not supported for pivoted results.
##### Allow large results
When you are downloading a large result set in Looker using Google BigQuery as your database dialect and you select **All Results** , you may see the **Allow large results** option. This is because Google BigQuery has a _maximum response size_ for query results, as described in the Write query results Google Cloud documentation topic. In order to download results that exceed the BigQuery maximum response size, Looker must perform a different process.
If you select **Allow large results** , the download process is affected as follows:
  * The `allowLargeResults` BigQuery option is set to `true` for the query.
  * The `ORDER BY` clauses in the query are removed.
  * The query will write to a PDT temp schema and requires permission to write to one.
  * The results of the query are stored in this temporary scratch schema under a random table name for one hour.


### Download or open in browser
Once you've selected your options, you can select the **Download** button to download a file to your computer, or select **Open in Browser** to view the file in the browser.
## Downloading data from a merged results query
To download merged results queries, you can save the query to a dashboard and then download the dashboard as a PDF or as a collection of CSV files. However, you must download the entire dashboard — you cannot download the data from just a single tile that is based on a merged results query.
## Downloading data from a dashboard
To download the entire dashboard, select **Download** from the dashboard's three-dot menu >more_vert.
This opens a dialog box that lets you select PDF or CSV as your download format.
### Downloading a dashboard as a PDF
You can download your entire dashboard as a PDF, which means you will get a PDF that displays the dashboard title, any dashboard filters, some or all dashboard tiles, and the time zone the dashboard was run in. The PDF will also include a timestamp that shows when the dashboard was downloaded.
Downloads in PDF format always return data from the model as if it is in Production Mode, even if you are in Development Mode.
To download a dashboard as a PDF, follow these steps:
  1. Select **PDF** from the **Format** drop-down menu.
  2. Select an option from the **Paper Size** drop-down menu:
The **Fit Page to Dashboard** option is the default; it sizes the PDF to the default width for dashboards (1260 px). Other paper size options size the PDF to match a standard paper size and fit all or part of the dashboard within it. Depending on the layout of the dashboard and the paper size selected, some PDF outputs may differ from the dashboard layout when viewed within Looker. For example, when the paper size selected is narrower than the dashboard, you may encounter issues with the spacing or other formatting and need to make some adjustments:
     * Large visualizations or groups of overlapping tiles may need to be resized to fit in the PDF.
     * Tiles that contain tables may not show all table columns in the PDF.
     * Tiles may be reduced in width to fit the PDF. Similarly, tiles that require scrolling in the Looker app may not expand to display all content.
If you don't see the **Paper Size** option, talk to your Looker admin about installing the latest version of the Chromium renderer for your Looker instance.
  3. If you select something other than **Fit Page to Dashboard** in the **Paper Size** drop-down, an **Orientation** option appears. You can choose to orient the dashboard in portrait or landscape position.
  4. Select or leave unselected **Expand tables to show all rows**. If you select this option, for dashboard tiles that use table visualizations, the PDF will show all the rows that are available in the table visualization, not just the rows that are visible in the dashboard tile thumbnail. If you do not select this option, only the rows that are visible in the thumbnail without scrolling will appear in the PDF. Dashboard and query filters will still apply, as will visualization settings such as row limits, column limits, and settings that are made with the **Limit Displayed Rows** option.
If the **Expand Tables to Show All Rows** option is selected, dashboard tiles that contain table visualizations may look slightly different in downloaded PDFs than they do inside Looker. The following differences may be noticeable in the PDF:
     * Customizations to background colors and font sizes are removed from column headers and subtotal rows.
     * If no custom theme is set, Tables appear in the white theme. Otherwise, the custom theme is applied when downloaded.
     * The sort icon does not appear on pivoted tables that were not manually sorted.
     * Tables with **Size Columns to Fit** enabled stretch to the full width of the tile.
Additionally, for tables with more than 20,000 cells, the following differences may be noticeable in the PDF:
     * Conditional formatting options other than **Background color** no longer appear.
     * Cell visualizations on numeric columns no longer appear.
If you don't see the **Expand tables to show all rows** option, talk to your Looker admin about installing the appropriate version of the Chromium renderer for your Looker instance.
  5. Select or leave unselected **Arrange dashboard tiles in a single column**. If you select this option, the PDF displays dashboard tiles in a single vertical column. If you do not select this option, the dashboard tiles appear as they are arranged in the dashboard.
  6. Select **Open in Browser** to see an image of the PDF in a new tab of your browser. From there, you can opt to download the PDF using your browser's controls.
  7. Select **Cancel** if you no longer want to download the dashboard.
  8. Select **Download** to initiate the download. A new tab in your browser will open, showing the status of your download.


### Downloading a dashboard as CSVs
You can download all the query tiles from your dashboard as a zipped collection of CSV files. Text tiles are not included in the ZIP file. To download your dashboard as a collection of CSV files, follow these steps:
  1. Select **CSV** from the **Format** drop-down menu.
  2. Select **Cancel** if you no longer want to download the dashboard.
  3. Select **Download** to initiate the download of your zipped CSV collection.


When you download a dashboard as CSV files, the options for formatting downloads, such as setting custom row limits or choosing all results, are unavailable. The row limits in the downloaded files correlate to the row limits on the corresponding tiles.
Looker generates zipped files using UTF-8 encoding. If the characters in your CSV filenames appear garbled, there may be a conflict between Looker's UTF-8 encoding and the default encoding of your machine's operating system or a third-party application. Looker suggests that you use a file extractor that recognizes UTF-8, such as 7-Zip, and ensure that any third-party applications are configured to support UTF-8.
### Downloading data from dashboard tiles
> You cannot download the data from dashboard tiles based on merged results queries, but the data from merged results tiles is included if you download a dashboard as a PDF or as a collection of CSV files.
To download the data from a dashboard tile, select the three-dot icon on the tile and select **Download data** :
This opens a dialog box with several options that are are similar to those for a Look or an Explore. Expand the **Advanced data options** menu to see all available options for your download:
  * **Number of rows and columns to include**


#### Format
Data can be downloaded from dashboard tiles in the following formats:
  * TXT (tab-separated values)
  * Excel spreadsheet (Excel 2007 or later)
  * CSV
  * JSON
  * HTML
  * Markdown
  * PNG (image of visualization)


Depending on the format you select, some options in the **Advanced data options** menu may not be available.
If the HTML or PNG (image of visualization) options are missing, talk to your Looker admin about installing the appropriate version of the Chromium renderer for your Looker instance.
For JSON format, Looker uses field labels as its rendered value in its JSON output. See the Change in JSON formatting Community post for more information about how Looker renders fields in JSON format.
Transposed table visualizations will render in PDF and PNG downloads only.
Downloads in PNG format always return data from the model as it is in Production Mode, even if you are in Development Mode.
#### Results
In the **Results** section, choose whether you want visualization settings applied to your data download:
  * If you choose **With visualization options applied** , Looker applies some of the visualization settings to your download. Any of the following settings in the Plot, Series, and Formatting menus that are configured for the visualization will be applied to the data download:
    * Limit Displayed Rows to a maximum of 500 rows shown or hidden.
    * Show Full Field Name
    * Custom labels for each column (Looker uses field labels as its rendered value in its JSON output. See the Change in JSON formatting Looker Community post for more information about how {looker_name_short}} renders fields in JSON format).
    * Conditional Formatting for downloads of table chart visualizations in Excel format.
> Conditional formatting will display in downloads in Excel format with table chart visualizations only if the **Along a scale Rule** is applied.
Columns in table charts that have been manually rearranged will appear in their original order in the download if the query includes any of the following elements:
    * One or more fields that are hidden from the visualization
    * One or more fields that reference a dimension in the `link` parameter that is not selected in the current Explore
    * One or more fields with dimension fill enabled
    * Three or more pivoted fields
    * Row totals enabled


If you choose **As displayed in the data table** , visualization options will not be applied and the download will appear like the data table in the **Data** section of the Look or Explore.
#### Data values
In the **Data values** section, choose how you want the downloaded results to appear:
  * If you choose **Formatted** , the data will appear more similar to the **Explore** experience in Looker, although some features (such as linking) aren't supported by all file formats.
  * If you choose **Unformatted** , Looker does not apply any special formatting of your results, such as rounding long numbers or adding special characters your Looker developers may have put in place. This is often preferred when data is being fed into another tool for processing.


#### Number of rows and columns to include
You can specify how much data is included in your download in this section. In most tiles, this section of the download pop-up is named **Number of rows to include** ; if the tile query contains any pivoted dimensions, this section is named **Number of rows and columns to include**. Your options include:
  * **Current result table** : Number of rows specified by the row limit — and column limit, if the tile query contains at least one pivoted dimension — of your tile's underlying data table.
  * **All Results** : All results returned by the tile query, even if the tile's data table specifies a more restrictive row limit or column limit. Before selecting this option, see the Considerations when using the All Results or Custom option section on this page. This option is not visible to users who do not have `download_without_limit` permissions.
  * **Custom** : A custom number of rows to download. Users with `download_with_limit` permissions are limited to 5,000 rows. The limit for other users is typically 100,000 unless your Looker admin has increased that limit (see the Legacy feature: Allowing unlimited downloads (Looker 4.14+) Community post).


##### Considerations when using the All Results or Custom option
Looker checks your permissions and determines whether the complexity of the query and the database dialect will allow the entire query to be downloaded. If you have the permissions to download results over a set limit and if Looker determines that your entire query can be downloaded, the **All Results** option will be available in the **Download** window.
The **All Results** option is typically disabled for queries that:
  * Involve row totals
  * Use percent of total, percent of previous, or running totals types of measures
  * Retrieve data from a database dialect that cannot stream results
  * Include pivoted columns that Looker calculates because the data comes from a database dialect that cannot calculate the pivots


> Even when the **All Results** option is available, you should still use caution when downloading all results. Some queries are very large, containing thousands or millions of rows, which can overwhelm most spreadsheet programs — or even your Looker instance.
If the **All Results** option is unavailable, you can use the **Custom** option to specify the maximum number of rows allowed with your permissions. When you select **Custom** , you can specify a number of result rows to download. If your query contains any pivoted dimensions, you can also specify a number of columns to download.
## For admins: Enabling downloading data for your Looker instance
Certain downloading options require that admins of customer-hosted Looker deployments have installed the appropriate version of the Chromium renderer. If your instance is Looker-hosted, Chromium is already installed.
The Managing business user features documentation page has important admin information about the download process:
  * User permissions and dashboard downloads
  * Rendering image-based formats for download
  * Rendered formats and download permissions
  * Troubleshooting downloads of large Excel files


To learn more about the permissions that must be assigned to users to enable them to download — specifically the `download_with_limit` and `download_without_limit` permissions — visit the **Roles** documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


