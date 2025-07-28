# Presenting content with boards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/presenting-content

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing and managing access to a board
    * Board access levels
    * Viewing the access levels for a board
    * Managing the access levels for a board
  * Creating a board
    * Creating a board from the Create button
    * Creating a board from the Boards option
    * After board creation
  * Adding a board to your list
  * Arranging content on a board
    * Adding sections to a board
    * Reordering sections on a board
    * Removing sections from a board
    * Moving content within sections on a board
    * Moving content between the sections of a board
  * Adding descriptions to a board
    * Adding a description for the entire board
    * Adding descriptions to the sections of a board
  * Adding content to a board
    * Adding Looks and dashboards to a board
    * Adding links to a board
    * Removing content from a board
  * Sharing a board
    * Sharing a link to a board
    * Sending an email notification
  * Deleting a board




Was this helpful?
Send feedback 
#  Presenting content with boards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing and managing access to a board
    * Board access levels
    * Viewing the access levels for a board
    * Managing the access levels for a board
  * Creating a board
    * Creating a board from the Create button
    * Creating a board from the Boards option
    * After board creation
  * Adding a board to your list
  * Arranging content on a board
    * Adding sections to a board
    * Reordering sections on a board
    * Removing sections from a board
    * Moving content within sections on a board
    * Moving content between the sections of a board
  * Adding descriptions to a board
    * Adding a description for the entire board
    * Adding descriptions to the sections of a board
  * Adding content to a board
    * Adding Looks and dashboards to a board
    * Adding links to a board
    * Removing content from a board
  * Sharing a board
    * Sharing a link to a board
    * Sending an email notification
  * Deleting a board


**Boards** in Looker provide a way for teams to find curated dashboards and Looks. Dashboards and Looks, which are stored in folders, can be added to multiple boards. Boards provide a way for users to perform the following tasks:
  * Add Looks and dashboards to boards to make it easier for users to find the information that is most relevant to them
  * Add links and descriptions to provide context and to guide users to resources


Users will only see boards that they have access to view. A user must have the **View** access level to see a board. Users with the **Manage Access, Edit** access level can add dashboards and Looks to the board and provide context for that content to help guide other users.
## Viewing and managing access to a board
Access to boards and the content that is added to them, like Looks or dashboards, depends on a user's or group's board access, their access to the folder in which that content is stored, and the model that the Look or dashboard is based on.
If a user doesn't have folder access for viewing a dashboard or Look, that dashboard or Look will not be displayed to that user on the board. If the user has folder access but not model access, they will see a thumbnail but will not be able to view the underlying Look or dashboard.
### Board access levels
There are two access levels that can be assigned to a user or group for a board: **View** and **Manage Access, Edit**.
With the **View** access level, a user can see that the board exists, add the board to their list, and view any board content that they have access to view.
With the **Manage Access, Edit** access level, a user can do everything that the **View** access level allows and can also make the following changes to the board:
  * Manage access to the board
  * Organize and manage content on the board
  * Add and remove Looks, dashboards, and links
  * Delete the board


### Viewing the access levels for a board
You must have the **Manage Access, Edit** access level for a board to view the access levels that other users and groups have for it. To see who can access a board:
  1. Navigate to the board and select the share icon.
  2. Looker displays the **Manage access** window for the board.
  3. The **Who can access this board** section of the window lists users and groups who have access to the board as well as their access levels.


### Managing the access levels for a board
To manage access to a board, you need the **Manage Access, Edit** access level for that board. To make changes to the access level that a group or user has for a board:
  1. Navigate to the board and view its access levels by selecting the share icon.
  2. To change the access level for a user or group that is already listed, select their current access level and choose the access level that you want from the menu. You cannot change the ability of Looker admins to manage the board.
  3. Remove user or group access by clicking the **X** to the right of the name.
  4. Add one or more groups by selecting the **Add group or user** field and choosing any groups or users that you want to change.
  5. For any users or groups whose access you want to change, select the existing access level and choose the desired access level from the drop-down menu.
  6. Save your changes by selecting **Save**.


## Creating a board
By default, when a board is created, admins and the creator have the **Manage Access, Edit** access level. All other users can interact with the board at the **View** access level.
You can create a new board from the **Create** button or the **Boards** option in the left navigation panel.
### Creating a board from the **Create** button
To create a board from the **Create** button, follow these steps:
  1. Click the **Create** button in the left navigation panel.
  2. Select the **Board** menu item. This opens a **Create board** window.
  3. Enter a name for your new board in the **Name** field.
  4. Select **Create board**.


### Creating a board from the **Boards** option
To create a board from the **Boards** option, follow these steps:
  1. Select the **Create or find a board** plus icon next to the **Boards** option in the left navigation panel, and then select **Create a new board**.
  2. In the **Name** section of the **Create board** window, enter a name for your board and select **Create Board**.


### After board creation
After a board is created, Looker adds the new board to your list in the left sidebar in **Boards**. As the creator of the board, you will also be listed as a contributor in the **Contributors** section of the **About this board** information panel.
You can now manage the content on the board in a number of ways, including:
  * Adding sections
  * Adding a description
  * Managing access to the board


## Adding a board to your list
You can create a shortcut to a board that was created by another user by adding the board to a personal list of boards, similar to a "Favorites" section. When you add a board to your list, it will be listed on the left sidebar under **Boards** when you browse content in Looker.
To add a board to your list, select **Add to my list** beneath the title of the board.
To remove a board from your list, select the board's three-dot **Board options** menu and choose **Remove from my list**.
You can also remove a board from your list by selecting the three-dot menu that appears when you hover over a board in the left navigation panel and choosing **Remove from sidebar**.
The number of users who have added a board to their list is reflected in the **About this board** section of the board's information section.
## Arranging content on a board
To arrange the content on a board, you must have the **Manage Access, Edit** access level. In addition to adding content to a board, contributors to a board can arrange the content on a board in the following ways:
  * Reorder sections
  * Move content within sections
  * Drag and drop content between sections


If you make changes to a board, you will be listed as a contributor in the **Contributors** section of the **About this board** information panel.
### Adding sections to a board
When you create a board, there is a default section named **Untitled section**. To edit the title of the section, choose the **Edit Title** pencil icon to the right of **Untitled section** , and enter a new title.
To add a new section to a board, select **New section** at the bottom of your board. Enter a name for your new section, and press Enter (Windows) or return (Mac) to save the name.
You can now begin to add content to the new section.
### Reordering sections on a board
To change the order of the sections on a board:
  1. Hover your cursor over the section you want to move and select the vertical six-dot icon to the left of the section title.
  2. Holding the vertical six-dot icon, drag the section to reposition it.


### Removing sections from a board
If you have the **Manage Access, Edit** access level for a board, you can also delete its sections. To remove a section from a board:
  1. Select the trash icon for the section you want to delete:
  2. Looker displays a pop-up menu to confirm that you want to delete the section. Select **Delete** to delete the section.


> Removing a section from a board also removes any Looks, dashboards, or links that have been added to the board in that section. However, the Looks and dashboards still exist in their folders.
### Moving content within sections on a board
To change the order of content within a section of a board:
  1. Click on the content that you want to move.
  2. Holding the added content, drag and drop it to move it to the desired position within the same section.


### Moving content between the sections of a board
You can move content from one section to another by dragging and dropping the content you want to move. To move content from one section to another:
  1. Select the content that you want to move.
  2. Holding the content, drag it until it is positioned within the desired section of the board. If you hold the pointer over the new section while holding the content you are moving, Looker displays a message informing you that the content will be placed at the end of the section.
  3. Drop the content into the desired section.


## Adding descriptions to a board
For boards that you have created or for which you have the **Manage Access, Edit** access level, you can add a description that will appear in the board's information panel and in the window that Looker displays when you view all boards. You can also add a description to each section of a board.
### Adding a description for the entire board
In the **About this board** information panel of a board, you can add a text description that will appear in the **Description** section. This description can be seen by anyone who can view the board and is a great way to give people context around the data added to the board. Your description can be up to 250 characters and can include URLs and Markdown links.
To add or edit a board's description:
  1. Select the **Board Information** icon at the top of the board to open the board's information panel.
  2. Under **Description** in the information panel, select the **Add a description** text to add a new description.
  3. To edit an existing description, hover over the description and select the **Edit Description** pencil icon.
  4. Add a description in the **Description** section and select **Done** to save the description.


### Adding descriptions to the sections of a board
You can add or edit descriptions for each of the sections of a board that you have created or for which you have the **Manage Access, Edit** access level. To add or edit a description to one of a board's sections:
  1. Select the **Add description** text beneath the section title.
  2. Type in a description of up to 1,300 characters for the section, and press Enter (Windows) or return (Mac) to save the description.
  3. The description you have added will appear beneath the title of the section.


Users with **Manage Access, Edit** access to a board can modify an existing section description by selecting the existing text and performing the previous steps.
## Adding content to a board
You can add content to a board that you created or have access to edit. You can also remove content from a board once it has been added.
Other users will be able to see and interact with added content if they have access to it. Because content is stored in folders rather than on boards, adding and removing content from boards does not actually affect the underlying content.
If you add content to a board, you will be listed as a contributor in the **Contributors** section of the **About this board** information panel.
### Adding Looks and dashboards to a board
You can add a dashboard to one or more boards by selecting the **Add to boards** icon on a dashboard.
You can also add Looks and user-defined dashboards to a board in the following ways:
  * By adding from the board
  * By adding from a Look or dashboard's thumbnail in a folder
  * By adding from a Look's **Explore actions** gear menu or a dashboard's three-dot **Dashboard actions** menu


You can also add a LookML dashboard to a board from the thumbnail in the **LookML dashboards** folder or from the three-dot **Dashboard actions** menu of the LookML dashboard that you are viewing.
#### Adding from a board
To add a Look or user-defined dashboard to a board while you are viewing or editing the board:
  1. If the section already has content, hover over the section and select the **+** (plus) icon.
If the section doesn't have any content, select the **Add content** tile.
  2. Select **Saved content** from the pop-up.
  3. In the **Add saved content** window, select the Look or dashboard that you want to add to the board. The Look or dashboard you have selected will now appear in the section that you have chosen.


#### Adding from a folder
To add a Look, user-defined dashboard, or LookML dashboard to a board from a folder:
  1. In a folder, select the three-dot menu on the thumbnail for the dashboard or Look that you want to add to a board, and choose **Add to a board** from the drop-down menu.
  2. Choose an existing board and section from the **Select a board** and **Select a section in the board** drop-down menus, and select **Add**.


#### Adding from a Look or dashboard
To add a Look that you are viewing to a board:
  1. Select the Look's **Explore actions** gear menu and choose **Add to a board**.
  2. Choose an existing board and section from the **Select a board** and **Select a section in the board** drop-down menus, and select **Add**.


To add a user-defined dashboard or a LookML dashboard to a board:
  1. Select the **Dashboard actions** three-dot menu, and choose **Add to a board**. This opens the **Add to Boards** window, where you can choose one or more boards to which you want to add the dashboard.
  2. In the **Add to Boards** window, select the checkboxes for any boards to which you want to add the dashboard. See the Adding with the **Add to boards** icon section of this page for more information on the actions you can take with the **Add to Boards** window.


#### Adding with the **Add to boards** icon
You can add a dashboard to a board by selecting the **Add to boards** icon on the dashboard, which is located to the right of the dashboard title and the heart-shaped favorites indicator:
Selecting the **Add to boards** icon opens the **Add to Boards** window, where you can choose one or more boards to which you want to add the dashboard.
Select the checkboxes for any boards to which you want to add the dashboard:
You can also add dashboards to specific sections on one or more boards. Select the arrow beside the name of the board to expand the list of sections on that board. Then select the sections to which you want to add the dashboard:
Any boards that you have selected appear in the right-hand pane of the **Add to Boards** window.
##### Adding dashboards to boards with custom filter values applied
If you have made any temporary changes to the filters on a dashboard that you are saving to one or more boards, you can choose whether the dashboard will be saved to those boards with its default filter values or with the current filter values applied.
To save a dashboard to one or more boards with its default filter values applied, disable the **Include custom filter values** toggle. The **Include custom filter values** toggle is disabled by default.
To save a dashboard to one or more boards with custom filter values applied, enable the **Include custom filter values** toggle.
For example, suppose you have an **Order Analysis** dashboard with a filter on the field **Created Date**. In this example, the default value for the filter on the **Created Date** field is **Last 7 Days** :
If you temporarily change the value of the filter on the **Created Date** to **Last 14 Days** , the dashboard will display values for the last 14 days, but this will not affect anyone else's filter results. However, if you enable the **Include custom filter values** toggle when you save the **Order Analysis** dashboard to one or more boards, the **Order Analysis** dashboard will be saved to those boards with the custom filter on **Last 14 Days** , rather than on its default value of **Last 7 Days**.
### Adding links to a board
You can add URLs to boards by using the following method:
  1. If the section already has added content, hover over the section and select the **Add content** plus icon.
If the section doesn't have any content, select the **Add content** tile.
  2. Select **URL Link** from the pop-up.
  3. In the **Link** field, paste or enter the URL that you want to add to your board.
     * If the URL you used is to a Look or dashboard, the **Title** and **Description** fields will be filled in automatically.
     * Otherwise, add a **Title** for the link, and, if desired, add a **Description** of up to 255 characters.
  4. If you added a Looker dashboard URL with custom filters applied, the option to **Include custom filter values in URL** will appear. When this option is enabled, the dashboard link uses the custom filter values. When this option is disabled, the link excludes any custom filter values and uses the default filter values.
It is possible to include multiple tiles on a board that reference the same dashboard, but with different filter values set for each tile. However, each of these tiles will use the same title and description, which could make it confusing for users to navigate a board.
  5. Click **Add** to include the link.


### Removing content from a board
To remove content from a board:
  1. Select the three-dot **Options** menu at the top right of the content.
  2. Choose **Remove from board**.


> If you remove a section from a board, any Looks, dashboards, and links in that section will also be removed.
## Sharing a board
You can share boards for which you have the **Manage Access, Edit** access level by sharing a link to the board or by sending an email notification. Users must have at least the **View** access level for a board in order to view it.
### Sharing a link to a board
To obtain a link to a board that you can share with others:
  1. Navigate to the board and select the share icon.
  2. In the **Manage access** window, under **Share this board with someone** , select and copy the URL field, or click **Copy URL**.


### Sending an email notification
When you grant a user access to a board, you are given the option of sending that user an email notification. If you add a user group to a board, however, email notifications will not be sent to the members of the group unless you also add the group members as individual users. To send an email notification:
  1. In the **Manage access** window for the board, grant access to the user.
  2. Select the **Email the people you have just added** checkbox in the **Manage access** window.
  3. Select **Save**.


Individual users you have added to the board will receive an email notifying them that they have been granted **View** or **Manage Access, Edit** access to the board. The email also invites users to view the board and encourages them to add it to their lists.
## Deleting a board
> When you delete a board, you will not be able to recover it.
To delete a board, you must have the **Manage Access, Edit** access level. Deleting a board will not delete the Looks and dashboards that are added to the board, as they are stored in folders. To delete a board:
  1. Select the board's three-dot **Board options** menu, and choose **Delete board**.
  2. Confirm that you want to delete the board in the window that Looker displays.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


