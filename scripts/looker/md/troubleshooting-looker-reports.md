# Troubleshooting Looker report errors  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/troubleshooting-looker-reports

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Troubleshooting Looker report errors
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
If you encounter issues while using Looker reports, refer to the following table for potential solutions. If you encounter an unexpected error that isn't listed in the following table, contact Looker Support.
**Error message** |  **Possible cause** |  **Possible solution**  
---|---|---  
Can't save report. The selected folder is more than 5 levels deep. Choose a folder that's 5 or fewer levels deep.  | You are trying to save a report to a folder that is too deeply nested.  | Choose a folder that is 5 or fewer levels deep.   
Can't save a report to a folder with custom access. Select a folder without custom access.  | You are trying to save a report to a folder with a custom list of users.  | Select a folder that doesn't provide access to a custom list of users.   
There was a problem saving the report(s).  | An unexpected error occurred while saving the report or reports.  | Try saving the report or reports again. If the issue persists, contact Looker Support.   
Can't move a report to a folder with custom access. Select a folder without custom access.  | You are trying to move a report to a folder with a custom list of users.  | Select a folder that doesn't provide access to a custom list of users.   
Can't move a report to the same folder.  | You are trying to move a report to the folder that it's already in.  | Choose a different destination folder.   
Can't move `_number_`out of` _total_`reports. | Some reports couldn't be moved because an error occurred.  | Try moving the reports again. If the issue persists, contact Looker Support.   
There was a problem moving the report(s).  | An unexpected error occurred while moving the report or reports.  | Try moving the report or reports again. If the issue persists, contact Looker Support.   
Can't copy report. The selected folder is more than 5 levels deep. Choose a folder that's 5 or fewer levels deep.  | You are trying to copy a report to a folder that is too deeply nested.  | Choose a folder that is 5 or fewer levels deep.   
Can't copy a report to a folder with custom access. Select a folder without custom access.  | You are trying to copy a report to a folder with a custom list of users.  | Select a folder that doesn't provide access to a custom list of users.   
Can't copy `_number_`out of` _total_`reports. | Some reports couldn't be copied because an error occurred.  | Try copying the reports again. If the issue persists, contact Looker Support.   
Can't copy `_number_`out of` _total_`reports.`_number_`of these reports have a restricted datasource. Contact your admin for more details. | Some reports couldn't be copied because a report datasource was unavailable.  | This error will occur if a connector that provides a datasource to the report has been disabled. Request that your Looker admin enable the connector.   
There was a problem copying the report(s).  | An unexpected error occurred while copying the report or reports.  | Try copying the report or reports again. If the issue persists, contact Looker Support.   
There was a problem renaming the report.  | An unexpected error occurred while renaming the report.  | Try renaming the report again. If the issue persists, contact Looker Support.   
Can't add report to favorites.  | An error occurred while adding the report to your favorites.  | Try adding the report to your favorites again. If the issue persists, contact Looker Support.   
Can't remove report from favorites.  | An error occurred while removing the report from your favorites.  | Try removing the report from your favorites again. If the issue persists, contact Looker Support.   
Can't move folder. The selected folder contains reports and the destination folder is more than 5 levels deep. Choose a folder that's 5 or fewer levels deep.  | You are trying to move a folder to a destination that is too deeply nested.  | Choose a destination folder that is 5 or fewer levels deep.   
Can't move folder. The selected folder contains reports and the destination folder has custom access. Select a folder without custom access.  | You are trying to move a folder to a destination folder with a custom list of users.  | Select a destination folder that doesn't provide access to a custom list of users.   
Can't add user(s). Users must also have access to the parent folder.  | You are trying to add a user to a subfolder, but the user doesn't have access to the parent folder.  | Confirm that the user has access to the parent folder before adding them to the subfolder.   
Can't set custom access to this folder. A folder that contains reports can only inherit access permissions from the top-level folder. Grant the users or groups access to the top-level folder and try again.  | You are trying to specify a custom list of users or groups for a folder that contains reports.  | Grant the users or groups access to the appropriate top-level folder, such as the **Shared** **folders** folder.   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


