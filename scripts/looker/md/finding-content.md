# Finding content in Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/finding-content

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Using the main navigation menu
    * Navigating to content in folders
    * Navigating to content on boards
  * Searching for saved content
  * Viewing content on your homepage




Was this helpful?
Send feedback 
#  Finding content in Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using the main navigation menu
    * Navigating to content in folders
    * Navigating to content on boards
  * Searching for saved content
  * Viewing content on your homepage


Content in Looker can take the form of either a Look, which is a saved snapshot of the data that results from a query, or a dashboard, which is a collection of tiles that show visualized query results.
All navigation occurs within the main navigation menu. To open or hide the menu, click the **Main menu** icon menu.
You can also search for content and navigate to content directly from your homepage.
## Using the main navigation menu
You can navigate to saved content from the main navigation menu. Depending on your permissions, the main navigation menu may include the following options:
  * **Create** button: Depending on your permissions, lets you create the following items:
    * Dashboards: You must have the `save_content` permission to see this option.
    * LookML models: You must have the `develop` permission to see this option.
    * Connections: You must have the `manage_project_connections` permission to see this option.
  * **Explore** : Opens the **Explore** panel, from which you can search for, select, and view Explores.
  * **Develop** : Opens the **Develop** panel, from which you can access LookML projects and develop in LookML.
  * **Admin** : Opens the **Admin** panel, from which you can administer Looker.
  * **Home** : Shows your homepage, if your Looker admin has enabled the prebuilt homepage or another homepage option. If your admin has set a board as your homepage, the name of the board appears instead of the text **Home**.
  * **Overview** : Shows the organization-wide default homepage, if your admin has configured a different default homepage for you or a group that you belong to. If your admin has set a board as your organization-wide homepage, the name of the board appears instead of **Overview**.
  * **Recently Viewed** : Lists your most recently viewed Looks and user-defined dashboards.
  * **Favorites** : Shows a list of Looks or dashboards that you've marked as favorites.
  * **Boards** : Lists boards that you have created or added to your list of boards.
  * **Folders** : Lists folders that you have access to, including the following folders:
    * **All folders** , a top-level directory with entry points to additional folders
    * Your personal folder
    * Your default folder, if you have configured one
    * **People** , which contains all the personal folders for other users that you have access to
    * **Shared folders** , which contains folders, Looks, and user-created dashboards that are typically used company-wide or within departments
    * **LookML dashboards**, a folder that contains dashboards that developers have created using LookML


### Navigating to content in folders
In Looker, content is saved into **folders**. A folder can include Looks, dashboards, or even subfolders. You can only see folders that you have access to view.
Within a folder, dashboards and Looks are listed under the **Dashboards** and **Looks** headings. Folders display the following information and options for Looks and dashboards:
  * **Checkbox** : Select the checkbox to move, delete, or copy an item. When you select an item, Looker displays buttons for the actions that you can take.
  * **Tile, description, and metadata** : Includes a visual preview of the dashboard or Look. If a description was added to the dashboard or Look, the description is displayed under the dashboard or Look title. Metadata, or information about how many views the dashboard or Look has and who created it, is also displayed under the title. 
  * **Favorite icon** favorite: Click the favorite icon to add or remove the Look or the dashboard from your favorites.
  * **Dashboard or Look three-dot menu** more_horiz: Provides options for configuring the content and for delivering its data.


Looks have the following additional information and options:
  * **Last Updated** column: Shows when the Look was last edited.
  * **Explore From Here** : A link to explore from that Look.
  * **Model** column: Shows the name of the model that is associated with the Look.


Dashboards and Looks may also display the following information, depending on their settings:
  * **On dashboard icon** : For Looks, the presence of the **On dashboard** dial icon indicates that the Look is used in a dashboard. Hold the pointer over over the icon to see the list of dashboards. If the Look isn't used in a dashboard, it won't have a dashboard icon.
  * **Calendar icon** calendar_month: The presence of the calendar icon indicates that the Look or the dashboard is scheduled for content delivery. Click the icon to open the content's **Schedule** dialog, where you can see and edit the content's delivery options. Clicking the calendar icon for a dashboard opens the legacy Scheduler.


#### Sorting lists of content
You can sort lists of subfolders, Looks, and dashboards within folders in the following ways:
  * By using the **Sort by** drop-down menu in section headers to select a sort option
  * By using the **Order** ascending arrow expand_less and descending arrow expand_more at the top of the section headers to change the sort order of the content by name


You can also sort Looks and dashboards by name by clicking the **Name** column header. Click the header multiple times to switch between ascending and descending sort order.
#### Using list view and grid view
Folders display dashboards and Looks using thumbnails that give you a preview of their appearance—without revealing the actual data. You can switch between two views within a folder:
  * **List view (default)** : Dashboards and Looks are shown in a detailed list.
  * **Grid view** : Dashboards and Looks are shown as thumbnails. Hold the pointer over over a thumbnail to see the following details: 
    * Description and metadata
    * Checkbox for selecting the item to copy, move, or move to trash
    * **On dashboard** icon (for Looks)
    * Favorites icon favorite
    * Three-dot options menu more_horiz


Click the **Show items in a grid** icon grid_view to switch to grid view. Click the **Show items in a list** icon to switch back to list view.
### Navigating to content on boards
**Boards** let you organize existing dashboards and Looks without changing their locations in folders.
To view a board and its contents, you must have at least the **View** access level for that board. If you have the **Manage Access, Edit** access level, you can make changes to the board, such as adding and removing content.
#### Finding a board
You can find boards in several ways:
  * **Search** : Use the search input box to find boards by name.
  * **Main navigation menu** :
    * The **Boards** section lists boards that you have created or that you have added to your list of boards.
    * Click the **Create or find a board** icon add, and then select **Browse all boards**. Looker displays the **Find boards at your organization** window, which lists all boards that you have created or that you can access.
You can filter to show only boards that you have created or added, and you can sort the list of boards by name, creator, creation date, or popularity.


#### Viewing the content on a board
Boards are organized into sections that users with the **Manage Access, Edit** access level can create and arrange.
When you navigate to a board, you'll see any Looks or dashboards that have been added to that board and that you have access to view. The content that you can see on a board depends on the following factors:
  * Your access level for the board
  * Your access levels for the folders in which the Looks and dashboards are stored
  * Your access to the model that the Look or dashboard is based on


To open the information section of a board, click the **Board Information** icon info. The information section of a board displays the following information:
  * **About this board** : The number of people who have added the board.
  * **Description** : Board contributors can add a description that contains text and Markdown links to a board. If a description has been added to the board, that description is displayed in this section.
  * **Created** : Displays information about who created the board and when the board was created.
  * **Contributors** : Lists the number of contributors in parentheses. Beneath the **Contributors** heading is a list of contributors. A board's contributors include the creator of the board and users who have made changes to the board.


## Searching for saved content
As an alternative to browsing folders, you can use specific words or phrases to search your Looker instance for saved content.
To perform a search, follow these steps:
  1. Place your cursor in the search **Start typing to search** search input box in the application header. If the application window is narrow, the input box will be replaced by a **Search** icon.
  2. Enter your search term.
  3. You'll see a list of search results that includes folders, boards, Looks, dashboards, and other content to which you have access.
  4. Select a search result to view that content.


There are three types of search experiences:
  * Improved search:
    * Includes improved ranking that automatically includes both curated and non-curated results without your needing to choose which result set you want to see. This is why the Curated Search switch is not available when improved search is enabled.
    * Faster search results. To increase search performance, improved search does not return LookML files. You can still search for LookML files within a LookML project.
  * Legacy search: If improved search is not enabled on your instance, you will see Looker's legacy search.
  * Curated search:
    * When the **Curated Search** feature is enabled, search results will include content from shared folders, your personal folder, and boards. Content that is saved in other users' personal folders will be included in the results only if such content is also pinned to a board. The search results will exclude content that exists only in the personal folders of other users.
    * To include content from other users' personal folders, turn off the **Curated Search** switch in the search results dialog box.


## Viewing content on your homepage
To navigate to your homepage, select the Looker logo in the header, or select **Home** from the main navigation menu. If your Looker admin has set a board or a different Looker page (such as **Favorites**) as your homepage, the name of the board or the page will appear instead of **Home**.
Depending on the settings that your admin has specified, you might see one of the following when you navigate to your homepage or log in to Looker:
  * **Prebuilt Looker homepage** : If your admin has chosen the prebuilt Looker homepage option, your homepage displays visually representative thumbnails for dashboards and Looks. Content is organized on this page in the following sections:
    * A **Recently Viewed** tab shows content that has been most recently viewed. The **Filter by group** drop-down menu in this tab filters the recently viewed content in the following ways:
      * **Viewed by you** : Shows content that you have recently viewed.
      * If your Looker admin has configured multiple groups, you can select a group from the drop-down list to show the most viewed content for that group.
Clicking the **See all** link next to the drop-down list takes you to the **Recently Viewed** page.
    * **Favorites** shows the Looks or dashboards that you have marked as favorites by clicking their **Add to favorites** heart icons, which you can do from your homepage as well as on the folder or page that you want to favorite.
    * **Discover sidebar** appears on your personalized homepage if your Looker admin has set the prebuilt Looker homepage as your homepage and you haven't previously closed it. This sidebar contains links to documentation that can help you get started using Looker and modeling with LookML. To close it, click the **Close** close icon in the sidebar. Closing the **Discover** sidebar reveals the announcement sidebar, if your admin has set it up. To re-open the **Discover** sidebar, click the **Help** icon live_help in the header and select the **Discover** option.
    * **Announcement sidebar** appears on your personalized homepage if your Looker admin has set the prebuilt Looker homepage as your homepage and added content to the sidebar. The sidebar may include text, links, and images from your admin. You can hold the pointer over over the sidebar to see additional information and links, if your admin has included them.
  * **A Looker page** : Your admin may set your homepage to another page within Looker. For example, if your homepage has been set to the **Favorites** or **Recently Viewed** page, you will see that page when you log in to Looker. The **Home** option in the main navigation menu will also be replaced by a reference to that page.
  * **A folder** : Your admin may have set your homepage to the Shared folder or to another folder in your organization. For example, if your homepage has been set to the **Shared folders** folder, you will see the **Your organization's folders** page when you log in to Looker.
  * **A board** : If your admin has set a board as your homepage, the name of the board appears in the main navigation menu.
  * **A Markdown page (or another URL within Looker)** : An admin may set the homepage to point to a URL-based folder, boards, or another page in Looker, such as a Markdown file or a specific dashboard.
If your admin has set your homepage to a URL other than a folder or board, you can navigate to your homepage by selecting the Looker icon in the header of the application.


## Next steps
You now know how to find existing dashboards and Looks that were created by someone else. Next, learn how to view and use dashboards.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


