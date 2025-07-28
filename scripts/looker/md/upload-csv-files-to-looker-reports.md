# Upload CSV files to Looker reports  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/upload-csv-files-to-looker-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Create a CSV file data source
  * Add CSV files to a data set
  * Sharing data sets
  * Upload file format
    * Only tabular data
  * Troubleshooting
    * Error: File is Invalid
  * Limits of CSV file upload
  * Related resources




Was this helpful?
Send feedback 
#  Upload CSV files to Looker reports
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create a CSV file data source
  * Add CSV files to a data set
  * Sharing data sets
  * Upload file format
    * Only tabular data
  * Troubleshooting
    * Error: File is Invalid
  * Limits of CSV file upload
  * Related resources


You can bring data into Looker reports from any source that provides CSV (comma-separated values) files. You can upload CSV files directly from your computer.
## Create a CSV file data source
Looker reports store uploaded CSV files in data sets. A data set can contain one or more CSV files with the same column headers. A CSV file data source can contain one or more data sets.
To create a new CSV file data source, follow these steps:
  1. Open a Looker report.
  2. Click the **Create** button and then select **Data source**.
  3. Select the **CSV file upload** Google connector.
  4. Create a new data set by clicking the **Add data set** button. 
     * You can also drag one or more CSV files to the **Available data sets** section, and the Looker report will create a new data set that contains the uploaded files.
  5. When you have finished uploading files, click the **Connect** button.


Your uploaded data is stored in Cloud Storage. There are many benefits to this storage setup, including both the ability to access and download your data from the cloud and the ability to use other Google Cloud services with your data.
Learn more about Cloud Storage.
## Add CSV files to a data set
You can upload multiple files to a data set, as long as the column headers match. When you add new files, that data gets appended to the data set. This lets you update your data as time goes on.
To add CSV files to a data set, follow these steps:
  1. Open a Looker report.
  2. Click the **Data sources** tab.
  3. Select the data source that contains your CSV files.
  4. Click **Edit Connection**.
  5. From the **Available data sets** section, select the data set from which you'd like to add files.
  6. Click the **Add file** button. 
     * You can also drag one or more CSV files to the **Files in the data set** section.
  7. Once you have finished uploading files, click the **Reconnect** button.


## Sharing data sets
The data sets that you create belong to you and are not shareable. However, once you create a data source that is based on your data set, you can share that data source with other users. This means that your data sets can be used in shared data sources and reports, but only you can access the data set itself.
## Upload file format
Confirm that the files you upload are correctly formatted. Otherwise, errors might occur during the upload, or your data may not look right in your reports.
A common cause of content errors is the improper use of separators, quotation marks, and line break characters in the uploaded data. Understanding how CSV file upload handles these can save you trouble in the future.
### UTF-8 encoding
Your upload file should be in UTF-8 encoding. This is a standard encoding for most applications on the web.
However, if you are exporting data from certain desktop products, such as Microsoft Excel™, you may need to convert your file to UTF-8 before you upload it to a Looker report. Otherwise, the Looker report may return an error message such as `File is Invalid.`
### Only tabular data
CSV file upload can only import files of tabular data. This means that your files must have a regular structure of rows and columns. Each row must have the same number of columns, even if data is missing for a particular cell in the table. Trying to upload a file with merged cells, or an inconsistent structure, will fail with an upload error.
### Separators
All the fields in your data must be separated from each other by commas.
If there are commas within the actual data in a field you want to upload, that field must be surrounded by quotes. If your data includes double quotes, you can use a single quote character to surround the field.
### Header row
The first line in your file must be a header row. This row will tell the Looker report how to name your fields. Field names must be unique, so you can't have duplicate values in your header row.
Column names must:
  * Contain only letters, numbers, or underscores. Other punctuation or special characters are not allowed.
  * Start with a letter or underscore
  * Be at most 128 characters long


The header row must also follow the rules for separators.
### Line breaks
Each line in the file must end with a line break. CSV file upload does not support line breaks in your data even if these are escaped by quotes.
## Troubleshooting
The following sections describe common errors that you may see while uploading CSV files.
### Error: File is Invalid
If Looker displays the error `File is Invalid` after attempting to upload a CSV file, check for the following possible causes:
  * The file contains invalid UTF-8 characters.
  * The file is not actually a CSV file. For example, if you rename a PDF file to use the ".csv" extension, then the Looker report won't be able to properly parse the file.


## Limits of CSV file upload
CSV file upload is subject to the following limits:
  * 1000 data sets per user
  * 2GB total storage per user
  * 100 uploads per data set per day
  * 100MB file size limit per data set


## Related resources
About data sources
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


