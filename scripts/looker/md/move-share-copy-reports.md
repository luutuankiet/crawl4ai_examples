# Move, share, and copy reports  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/move-share-copy-reports

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to know about sharing reports
  * Move reports
    * Move individual reports
    * Move multiple reports
  * Copy reports
    * Copy individual reports
    * Copy multiple reports
  * Delete reports
    * Delete individual reports
    * Delete multiple reports




Was this helpful?
Send feedback 
#  Move, share, and copy reports
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to know about sharing reports
  * Move reports
    * Move individual reports
    * Move multiple reports
  * Copy reports
    * Copy individual reports
    * Copy multiple reports
  * Delete reports
    * Delete individual reports
    * Delete multiple reports


Looker stores reports, Looks (saved visualized query results), and dashboards (collections of tiles that show visualized query results) in folders. When you create a report in Looker, you can share it with other users by clicking **Save and Share** and saving it to a folder to which those users have access. Access to these folders is controlled by access levels and user permissions. Once a report is saved, you can move or copy the report to a different folder, or you can delete the report.
This page guides you through the components of sharing reports by moving and copying them to folders for other users to access in Looker. Read the following sections to learn about these concepts:
  * Things to know about sharing reports
  * Delete reports


## Things to know about sharing reports
There are several things to know about sharing reports in Looker:
  * Reports can't be stored in folders that are nested more than five folder levels deep, and they also can't be stored in folders with custom access levels. This restriction applies to saving, copying, and moving reports, as well as copying or moving folders that _contain_ reports. For example, consider the following use cases:
    * You can't save a report in a subfolder that is nested 10 folder levels away from the parent folder.
    * You can't move a folder that contains reports to a folder that has custom access levels.
    * You can't move a report to a folder that has custom access levels.
    * You _can_ move a folder into another folder that has inherited access levels.
  * Users can share a report with other users by moving it into a folder that those users have access to.
  * Copying reports with embedded data sources that support Owner credentials, for example, Sheets and BigQuery, can result in dataset configuration errors. We recommend that you don't copy reports that contain that have embedded data sources that support Owner credentials.


For more information about content access and permissions, see Controlling user content access and How content access and permissions interact.
If you want to change the access level settings for a folder, see Viewing and managing folder access levels.
## Move reports
Once a report is saved, you can move the report to another folder. To move reports, users must have one of the following types of access:
  * **Admin** access to the Looker instance.
  * **Manage Access, Edit** access level to the report's folder
  * **Manage Access, Edit** access level to the folder to which the report will be moved


You can move reports individually, or you can move multiple reports at once.
### Move individual reports
To move an individual report to a new folder, follow these steps:
  1. From a folder, click a report's more_horiz three-dot **Options** menu.
If the folder contents are displayed in grid view, hold the pointer over a report thumbnail to access the more_horiz three-dot **Actions** menu.
  2. Select the **Move** option to open the **Move reports** window.
  3. In the **Move reports** window, select the name of a top-level folder on the left to navigate to it.
  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.
  5. Click **OK**.


### Move multiple reports
To move multiple reports to a new folder, follow these steps:
  1. From a folder, click the check_box checkbox for any reports that you want to move.
If the folder contents are displayed in grid view, hold the pointer over a report thumbnail to access the check_circle_outline **Select** checkmark, and then select the checkmark to include the report in the bulk move.
  2. Select the **Move** option in the **Reports** section of the folder to open the **Move reports** window.
  3. In the **Move reports** window, select the name of a top-level folder on the left to navigate to it.
  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.
  5. Click **OK**.


## Copy reports
To copy reports, users must have one of the following types of access:
  * **Admin** access to the Looker instance
  * **Manage Access, Edit** or **View** access level to the report's folder
  * **Manage Access, Edit** access level to the folder to which the report will be copied, to save it in a folder other than the parent folder


You can copy reports individually, or you can copy multiple reports at once.
### Copy individual reports
To copy an individual report, follow these steps:
  1. From a folder, click a report's more_horiz three-dot **Options** menu.
If the folder contents are displayed in grid view, hold the pointer over a report thumbnail to access the more_horiz three-dot **Actions** menu.
  2. Select the **Copy** option to open the **Copy reports** window to select a folder to save the copy.
  3. In the **Copy reports** window, select the name of a top-level folder on the left to navigate to it.
  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.
  5. Click **Copy**.


### Copy multiple reports
To copy multiple reports, follow these steps:
  1. From a folder, click the check_box checkbox for any reports that you want to copy.
If the folder contents are displayed in grid view, hold the pointer over a report thumbnail to access the check_circle_outline **Select** checkmark, and then select the checkmark to include the report in the bulk copy.
  2. Select the **Copy** option in the **Reports** section of the folder to open the **Copy reports** window. Then, select a folder to save the copy.
  3. In the **Copy reports** window, select the name of a top-level folder on the left to navigate to it.
  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.
  5. Click **Copy**.


## Delete reports
To delete reports, users must have one of the following types of access:
  * **Admin** access to the Looker instance
  * **Manage Access, Edit** access level to the report's folder


To _restore_ deleted reports, users must have Admin access. See the Deleted and unused content for admins documentation page for more information about how to restore deleted content.
You can delete reports individually, or you can delete multiple reports at once.
### Delete individual reports
To delete an individual report, follow these steps:
  1. From a folder, click a report's more_horiz three-dot **Options** menu.
If the folder contents are displayed in grid view, hold the pointer over a report thumbnail to access the more_horiz three-dot **Actions** menu.
  2. Select the **Move to Trash** option.
  3. Click the **Move to Trash** button to confirm, or click the **Cancel** button to cancel.


### Delete multiple reports
To delete multiple reports, follow these steps:
  1. From a folder, select the check_box checkbox for any reports that you want to delete.
If the folder contents are displayed in grid view, hold the pointer over a report thumbnail to access the check_circle_outline **Select** checkmark, and then select the checkmark to include the report in the bulk delete.
  2. Select the **Move to Trash** option in the **Reports** section of the folder.
  3. Click the **Move to Trash** button to confirm, or click the **Cancel** button to cancel.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


