# Saving and editing Looks  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/saving-and-editing-looks

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Saving Looks from an Explore
  * Navigating to folders to see your Looks
  * Moving and copying Looks
  * Editing Looks
    * Editing a Look's source query
    * Turning off automatic Run on Load
    * Editing a Look's description




Was this helpful?
Send feedback 
#  Saving and editing Looks
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Saving Looks from an Explore
  * Navigating to folders to see your Looks
  * Moving and copying Looks
  * Editing Looks
    * Editing a Look's source query
    * Turning off automatic Run on Load
    * Editing a Look's description


While exploring, you can save your work by saving a Look. This saves all your choices for filters, visualizations, fields, sorting, and so on.
Both Looks and dashboards can be organized in folders (for example, you can have folders named Marketing, Q4 Sales Review, and so on) and later edited as needed.
This page explains how to save, edit, and make other changes to Looks and Look settings that affect what other users can see. For more information about the components on the Look page and interacting with a Look's data, visit the Viewing Looks in Looker documentation page.
## Saving Looks from an Explore
To save a Look from an Explore:
  1. In the upper right of the Explore, select the **Explore actions** gear menu.
  2. Choose **Save**.
  3. Select **As a Look** to open the **Save Look** menu.
  4. In the **Title** field, enter a new title.
  5. In the **Description** field, you can enter a description of the Look.
  6. In the **Folder** drop-down menu, select a folder where you want to save the Look. You will not be able to select folders to which you do not have access.
  7. You can locate subfolders where you want to save the Look by expanding top-level folders.
  8. You can filter on subfolder titles in the filter field.
  9. Save the Look.
     * To save your Look and return to the Explore page, select **Save**.
     * To save and view your Look, select **Save & View Look**.
     * Alternatively, select the **X** at the top right of the **Save Look** menu to close the menu and return to the Explore without saving the Look.


## Navigating to folders to see your Looks
You can access your company's folders by expanding the list of folders in the **Folders** section of the left navigation panel.
## Moving and copying Looks
Once you create and save a Look to a folder, you can move and copy it to other folders to which you have access.
Continue reading for details regarding how to copy or move Looks to other locations within Looker.
### Copying Looks
There are two ways to copy a Look:
  * From the gear menu on a Look's page


#### Copying Looks from the Look page gear menu
To copy a Look from the Look page:
  1. In the upper right of the Look page, select the **Explore actions** gear menu.
  2. Choose **Save**.
  3. Select **Save As...** to open the **Save Look** menu.
  4. In the **Title** field, enter a new title as desired.
  5. In the **Description** field, you can change or enter a description of the Look.
  6. In the **Folder** drop-down menu, select a folder where you want to save the Look. You will not be able to select folders to which you do not have access.
  7. You can locate subfolders where you want to save the Look by expanding top-level folders.
  8. You can filter on subfolder titles in the filter field.
  9. Save the Look.
     * To save your Look and remain on the original Look page, select **Save**.
     * To save and view the copied Look, select **Save & View Look**.
     * Alternatively, select the **X** at the top right of the **Save Look** menu to close the menu and return to the original Look without saving the copy.


#### Copying Looks from a folder
Once you create and save a Look or Looks to a folder, you can move and copy one individual Look or more than one Look in bulk to other folders to which you have access. You can view the detailed steps for moving and copying Looks on the Organizing and managing access to content documentation page.
### Moving Looks
Currently, you can only move Looks from a folder. You can move Looks individually or in bulk to other folders to which you have access. You can view the detailed steps for moving Looks on the Organizing and managing access to content documentation page.
## Editing Looks
After creating a Look, you can edit its underlying query, edit its name, and decide if it should automatically run when loaded. If you have permission to do so, you can also give access to the Look through publicly accessible URLs, described in more detail on the Public sharing, importing, and embedding of Looks documentation page.
### Editing a Look's source query
You can edit a saved Look's fields, filters, visualizations, sorting, and so on by following these steps on the saved Look's page:
  1. Select **Edit** on the saved Look's page to open the **Edit Look** menu.
  2. On the **Edit Look** menu, make any changes you want to the Look's fields, filters, visualization, and so on. You can make changes from both the field picker and the **Filters** panel, as necessary. For example, **Users** , a count of users, was added to the query.
     * For more information regarding making changes to an Explore query, see the Creating and editing Explores documentation page.
  3. After you make the desired changes, select the **Run** button to update the data and preview the changes.
  4. Select **Save** to save the changes and navigate back to the Look page.
     * Alternatively, select the **Cancel** option next to the **Save** button in the **Edit Look** menu header to navigate back to the Look page without saving the changes.


### Renaming a Look
There are two ways to rename an existing Look, including:
  * Renaming a Look from a Look's page
  * Renaming a Look from a folder


#### Renaming a Look from a Look's page
  1. Select **Edit** on the saved Look's page to open the **Edit Look** menu.
  2. Input the desired name in the title field underneath the header on the **Edit Look** menu. In this example, the Look title "Order count by month" was changed to "Monthly order count".
  3. Select **Save** to save the changes.


#### Renaming a Look from a folder
Whether viewing Looks in a folder with list view or grid view, you can rename an existing Look from a folder in the following way:
  1. Select the Look's three-dot menu icon.
  2. Select **Rename** to open the **Rename Look** pop-up.
  3. Change the Look title in the **Name** field, as desired.
  4. Select **OK**.
     * Alternatively, select **Cancel** to close the **Rename Look** pop-up without saving the changes.


### Turning off automatic Run on Load
You can prevent a Look from automatically loading its data when a user opens it by disabling the **Run on Load** option, which is enabled by default. This can be useful if you want to give the user a chance to select their filters before a Look's query is run.
If you choose to prevent the Look from running automatically, users will see an empty visualization that displays the text **Press "Run" to load this data** when they initially view the Look.
There are two ways to adjust the **Run on Load** option:
  * From the Look page **Explore actions** gear menu


#### Disabling automatic Run on Load from the Look page Explore actions gear menu
To disable automatic **Run on Load** from the Look page **Explore actions** gear menu, perform the following steps:
  1. Select the **Explore actions** gear menu.
  2. Select **Edit Settings** to open the **Look Settings** pop-up.
  3. Select the **Run on Load** switch to disable automatic **Run on Load**.
  4. Select **Save**.


You can also follow the preceding instructions to enable automatic **Run on Load** if it is disabled.
#### Disabling automatic Run on Load from a folder
Whether viewing Looks in a folder with list view or grid view, you can disable a Look's automatic **Run on Load** setting from a folder in the following way:
  1. Select the Look's three-dot menu icon.
  2. Select **Edit Settings** to open the **Look Settings** pop-up.
  3. Select the **Run on Load** switch to disable automatic **Run on Load**.
  4. Select **Save**.


You can also follow the preceding instructions to enable automatic **Run on Load** if it is disabled.
### Editing a Look's description
A Look's description appears under the Look's name in folders that are set to list view, or when you hold the pointer over the Look's thumbnail in a folder that is set to grid view.
If your admin has set your homepage to the pre-built Looker homepage, the description is also displayed when you hover over the Look's thumbnail on your homepage.
You can add or edit a Look's description directly from the Look page:
  1. Open the Look page and select the **Edit** link in the **Description** section of the **Details** panel to expand the **Description** text box.
  2. Add or edit the text for the description in the text box, as desired.
  3. Select **Save** to save the updated description, or select **Cancel** to close the **Description** text box without saving.


## Deleting Looks
You can delete a Look or Looks in one of two ways:
  * Individually or in bulk from folders, as described on the Organizing and managing access to content documentation page
  * Individually from the Look page **Explore actions** gear menu


To delete a Look using the Look page **Explore actions** gear menu, perform the following steps:
  1. Select the **Explore actions** gear icon to open the menu options.
  2. Select **Move to trash**.
  3. Select **OK** in the confirmation pop-up box to delete the Look.


If you delete a Look that is the source for a dashboard tile, the dashboard's Look-linked tile returns an **Element not found** error.
> If you accidentally delete a Look, your Looker admin _might_ be able to recover it for you. Looker stores deleted content in the trash until your Looker admin team empties the trash as part of their maintenance process.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


