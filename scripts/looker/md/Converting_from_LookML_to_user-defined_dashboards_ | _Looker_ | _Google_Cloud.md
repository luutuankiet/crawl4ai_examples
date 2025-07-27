# Converting from LookML to user-defined dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/converting-lookml-to-user-defined-dashboard

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Individual import from folders
  * Individual import from the dashboard




Was this helpful?
Send feedback 
#  Converting from LookML to user-defined dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Individual import from folders
  * Individual import from the dashboard


> You can also move LookML dashboards to folders other than the **LookML dashboards** folder if you have the `develop` permission on the model that includes the LookML dashboard.
Looker lets you copy a LookML dashboard into a folder as a user-defined dashboard. You can then edit your user-defined dashboard through the user interface, instead of through LookML, if your access settings for the folder contains the dashboard.
## Bulk import
You can bulk import LookML dashboards as user-defined dashboards.
  1. Select **All folders** from the left navigation panel, and open the **LookML dashboards** folder.
  2. Select the checkboxes for the dashboards to convert to user-defined dashboards.
  3. Click the **Import** button. This opens the **Import Dashboards** menu.
  4. In the **Import Dashboards** menu, choose a folder in which to place the dashboard.
  5. Click **OK**.


## Individual import from folders
You can import a single LookML dashboard as a user-defined dashboard:
  1. From the **LookML dashboards** folder, select a dashboard's horizontal three-dot menu option more_horiz.
  2. Select **Import** to open the **Import Dashboards** menu.
  3. In the **Import Dashboards** menu, choose a folder for the dashboard. You must have the **Manage Access, Edit** access level for the folder.
  4. Select **OK**.


## Individual import from the dashboard
To import a LookML dashboard as a user-defined dashboard from the dashboard itself, follow these steps:
  1. From the dashboard's three-dot menu more_vert, select **Copy LookML dashboard**.
  2. In the **Title** section of the **Copy** menu, enter a new name for the dashboard. (Optional)
  3. Select the folder to save the dashboard to. You must have the **Manage Access, Edit** access level for the folder.
  4. If your LookML project is localized, an option displays to preserve the localization keys: 
     * Don't select the option to save the dashboard just as you see it. This is useful if you want the dashboard to be immediately presentable and you don't plan to save the dashboard back to LookML. If you are not a Looker developer, choose this option.
     * Select the option to preserve the localization keys so the dashboard can be converted back to a localized LookML dashboard in the future. Localization keys will display in the dashboard. This option is for Looker developers who intend to edit the dashboard and copy it back to LookML.
  5. Select **Copy** to copy the dashboard into the selected folder.
  6. Use the links in the confirmation dialog to navigate to the new user-defined dashboard or to the folder that contains it, or select **Done** to close the dialog.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


