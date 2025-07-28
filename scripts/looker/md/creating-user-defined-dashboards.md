# Creating user-defined dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/creating-user-defined-dashboards

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Creating a dashboard from the Create button
  * Creating a dashboard from a folder
  * Creating a dashboard from a Look or an Explore
  * Adding tiles and text to a dashboard
    * Types of dashboard tiles
    * Building query tiles within a dashboard
    * Adding query tiles from an Explore
    * Adding tiles from a Look
    * Adding extensions
    * Adding data actions to tiles
  * Adding dashboard filters to a dashboard
  * Configuring dashboard settings
  * Adding a description to a dashboard
  * Improving dashboard performance using aggregate awareness




Was this helpful?
Send feedback 
#  Creating user-defined dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Creating a dashboard from the Create button
  * Creating a dashboard from a folder
  * Creating a dashboard from a Look or an Explore
  * Adding tiles and text to a dashboard
    * Types of dashboard tiles
    * Building query tiles within a dashboard
    * Adding query tiles from an Explore
    * Adding tiles from a Look
    * Adding extensions
    * Adding data actions to tiles
  * Adding dashboard filters to a dashboard
  * Configuring dashboard settings
  * Adding a description to a dashboard
  * Improving dashboard performance using aggregate awareness


User-defined dashboards are created in the Looker UI. To compare and contrast user-defined dashboards and LookML dashboards, see the Comparing user-defined and LookML dashboards documentation page.
To create a dashboard, you must have the following:
  * The **Manage Access, Edit** access level for the folder in which you want to place the dashboard
  * The `save_content` and `see_user_dashboards` Looker permissions


Additionally, you must have access to the LookML models for any data you wish to use in the dashboard.
When you're creating a dashboard, keep in mind best practices for dashboard construction. Find information and recommendations about building performant dashboards in the Considerations when building performant Looker dashboards Best Practices page.
## Creating a dashboard from the **Create** button
A **Create** button in the left navigation panel of Looker lets you create dashboards. To create a dashboard, follow these steps:
  1. Click the **Create** button.
  2. Select the **Dashboard** menu item. This opens a **Create dashboard** window.
  3. Enter a name for your new dashboard in the **Name** field.
  4. Navigate to and select the folder that you want to save the dashboard in. Alternatively, you can select the **Create New Folder** icon create_new_folder to create a new folder for the dashboard.
  5. Click **Create dashboard**.


Next, your new blank dashboard appears. From here, you can add tiles or text by entering edit mode. To enter edit mode, click **Edit dashboard** from the **Dashboard actions** menu more_vert, or click the **Edit Dashboard** button in the center of the dashboard pane.
## Creating a dashboard from a folder
To create a dashboard from a folder, follow these steps:
  1. Navigate to a folder where you'd like the dashboard to be located.
  2. Click the **New** button at the top right of the folder.
  3. Click the **Dashboard** option.
This opens the **Create Dashboard** window.
  4. Enter a name for your new dashboard in the **Name** field.
  5. Click **Create Dashboard**.


Next, your new blank dashboard appears. From here, you can add tiles or text by entering edit mode. To enter edit mode, click **Edit dashboard** from the **Dashboard actions** three-dot icon menu more_vert, or click the **Edit Dashboard** button in the center of the dashboard pane.
## Creating a dashboard from a Look or an Explore
To create a dashboard from a Look or an Explore, follow these steps:
  1. Navigate to a Look or an Explore.
  2. Click **Save** from the **Explore Actions** gear icon menu settings.
  3. Click **As new dashboard** from the submenu.
This opens a **Save as a new Dashboard** window.
  4. In the **Title** field, enter a name for your new dashboard.
The name that you enter applies to both the tile and the dashboard. You can modify title names at any time. To change the tile name for a query tile, see the Editing a query tile title subsection on the **Editing user-defined dashboards** documentation page. To change the dashboard name, enter edit mode on the dashboard.
  5. On the **Settings** tab, click the folder where you want to save your dashboard. You must have the **Manage Access, Edit** access level for the folder.
  6. On the **Filters** tab, click whether to use the Look's or Explore's filters as the dashboard filters. Custom filters can't become dashboard filters, but they do remain as tile filters.
  7. Click **Save**.
The Look or Explore will be saved as a query tile on the dashboard.


## Adding tiles and text to a dashboard
Once you've created a dashboard, the next step is to add tiles and text to the dashboard.
The first tile that you add to a dashboard takes up the entire width of the dashboard. Additional tiles that you add are sized to one-third of the dashboard's width and are added horizontally under the first tile. Looker adds additional rows of tiles as necessary. You can move and resize tiles however you like. You can also edit tiles once you've created them to adjust the names of the tiles, the visualizations, or the underlying queries or Looks.
For any new tiles that are added to a dashboard, if they were created from the same Explore as a dashboard filter, the dashboard filter is automatically applied to that tile.
### Types of dashboard tiles
You can add four kinds of tiles to a dashboard:
  * Look-linked tiles
  * Extension tiles


#### Query tiles
Query tiles can be built directly within a dashboard or added to a dashboard from a Look or from an Explore.
A query tile is based on an independent query, one that is not linked to a Look. The query underlying a query tile belongs to the dashboard. Even if you use an existing Look to create a query tile, the Look is used only during the creation of the query tile. The tile is unaffected by any later changes to that Look and still exists on the dashboard even if the Look is deleted.
When possible, use query tiles to avoid cluttering your folders with unnecessary Looks.
#### Look-linked tiles
Look-linked tiles are added to a dashboard from a Look.
A Look-linked tile links the tile's underlying query to a Look. That Look is used when creating the tile and every time the dashboard is refreshed. The Look and the dashboard must be in the same folder. If you want to add Looks from a different folder, first copy the Look into the same folder as the dashboard.
A Look-linked tile is a good choice if you want to create, change, and test a query in one place but use it in multiple dashboards. If the Look changes, any tiles linked to that Look change. If the Look is deleted, dashboards show an error for the tile.
#### Text tiles
Text tiles are built directly within a dashboard.
You can use text tiles to define visual sections on a dashboard and to add descriptions. Text tiles in dashboards are designed to have flexible formatting and to default to look more like headings and descriptions than tiles.
There are two types of text tiles, each of which offers a different editing experience but results in the same kind of tile:
  * **Text**: A dashboard text tile that provides a visual editing experience
  * **Markdown**: Looker's pre-existing text tile option, which lets you use some HTML and a subset of the Markdown markup language to style the output of the tile


#### Extension tiles
Extension tiles are custom applications called extensions that are added to a dashboard and run from inside a dashboard tile.
### Building query tiles within a dashboard
If you're in a dashboard, you can build a query tile from inside the dashboard.
Once you're in the dashboard's edit mode, you can add a query tile in one of two ways:
  * You can click the **Add** button from the top left of the dashboard pane, and then choose the **Visualization** option.
  * However, if the dashboard is blank, you can instead select the **Add** button in the center of the dashboard pane, and then choose the **Visualization** option.


Next, Looker displays a menu of Explores. Choose an Explore to begin building your query.
Looker opens the Explore window to let you build your query. To build a query, follow these steps:
  1. In the top left title field, enter a name for your query. This will be the name of the tile on the dashboard.
  2. Select the fields and filters from the field picker.
  3. Configure your visualization options in the **Visualization** pane.
  4. Once you have set up your query, click **Run**.
  5. Click **Save** to save the query as a tile on your dashboard.


For any new tiles that are added to a dashboard, if they were created from the same Explore as a dashboard filter, the dashboard filter is automatically applied to that tile.
### Adding query tiles from an Explore
You can save a query tile to a dashboard directly from an Explore. Once you are in an Explore and have a query that you want to add to the dashboard, follow these steps:
  1. Select **Save** from the **Explore Actions** gear icon menu settings.
This action opens an **Add to Dashboard** window:


  1. In the **Title** field, give your tile a title.
  2. From the list of folders, select the folder where the dashboard is located.
  3. From the list of dashboards, select the dashboard name, or type a dashboard name in the **Filter by title...** search bar to narrow the results.
  4. Click **Save to Dashboard**.


A confirmation message appears at the top of the Explore once you have added it as a tile on a dashboard. If you click the title of the dashboard in the confirmation message, Looker takes you directly to the dashboard in edit mode. From there, you can move and resize tiles however you like.
For any new tiles that are added to a dashboard, if they were created from the same Explore as a dashboard filter, the dashboard filter is automatically applied to that tile.
### Adding tiles from a Look
You can add both query tiles and Look-linked tiles to dashboards from a Look.
#### Adding query tiles from a Look
To add query tiles from a Look, follow these steps:
  1. Navigate to a Look.
  2. From the **Explore Actions** gear icon menu settings, select **Save** . This action opens a submenu.
  3. Select **To an existing dashboard** from the submenu.
This action opens an **Add to Dashboard** window.
  4. When you add a query tile from a Look, the tile is given the same title as the name of the Look in the **Title** field (which can be edited later).
  5. From the list of folders, select the folder where the dashboard is located.
  6. From the list of dashboards, select the dashboard name, or type a dashboard name in the **Filter by title...** search bar to narrow the results.
  7. Click **Save to Dashboard**.


Any tiles that you add to a dashboard through this method are not connected to the Look you created them from. You can edit the tiles without affecting the Look. You can edit or delete the Look without affecting the tiles.
A confirmation message appears at the top of the Look once you have added it as a tile on a dashboard. If you click the title of the dashboard in the confirmation message, Looker takes you directly to the dashboard in edit mode. From there, you can move and resize tiles however you like.
For any new tile that is added to a dashboard, if the Look it was based on was created from the same Explore as a dashboard filter, the dashboard filter is automatically applied to that tile.
#### Adding Look-linked tiles from a Look
You can save a Look-linked tile to a dashboard directly from a Look. However, the Look and the dashboard must be in the same folder.
To add a Look-linked tile to a dashboard (see the Adding query tiles from a Look section for visuals), follow these steps:
  1. Make sure the dashboard and the Look are in the same folder, or copy the Look into the same folder as the dashboard.
  2. Select **To an existing dashboard** from the submenu. This opens an **Add to Dashboard** window.
  3. Make sure the folder that contains the Look and dashboard is selected.
  4. Select the dashboard.
  5. Click **Add Look to Dashboard**.


Any tiles that you add to a dashboard through this method are connected to the Look that you created them from and have the same title as the Look. If you edit the tile, the Look and any other tiles that are linked to that Look are affected. If you edit or delete the Look, the tiles are affected.
A confirmation message appears at the top of the Look once you have added it as a tile on a dashboard. If you click the title of the dashboard in the confirmation message, Looker takes you directly to the dashboard in edit mode. From there, you can move and resize tiles however you like.
For any new tile that is added to a dashboard, if the Look it was based on was created from the same Explore as a dashboard filter, the dashboard filter is automatically applied to that tile.
### Adding text
Once a dashboard is in edit mode, you can add text tiles to it by clicking the **Add** button from the top left of the dashboard pane.
There are two types of text tiles, each of which offers a different editing experience but results in the same kind of tile:
  * **Text** : A dashboard text tile that provides a visual editing experience
  * **Markdown** : Looker's pre-existing text tile option, which lets you use some HTML and a subset of the Markdown markup language to format the tile


Once you save your **Text** or **Markdown** tile, you will see it at the bottom of the dashboard. You can then move and resize your text tile just as you would move and resize other tiles.
#### Adding Text tiles
**Text** tiles are dashboard text tiles that provide a visual editing experience.
To format the tile's text, follow these steps:
  1. Highlight the text in the tile that you want to format.
  2. Click the text style icons at the top of the tile.
As you edit the text tile, it will change to show you how it will appear when you save it.
  3. To save your tile, click **Save** on the dashboard.


To edit an existing tile, enter edit mode, click the tile text to make your changes, and save the dashboard.
#### Adding Markdown tiles
**Markdown** tiles are dashboard text tiles that can be formatted using HTML and Markdown.
Once you select **Markdown** , a window appears where you can add a title, subtitle, and body. These elements are optional.
Titles and subtitles support some HTML, including links and images. You can also use some HTML in the bodies of **Markdown** tiles. To understand how Looker renders HTML, see the HTML sanitization documentation page.
Body text supports a subset of the Markdown markup language. See the Using Markdown in Markdown tiles documentation page for more information about which Markdown syntax is supported in the body text.
### Adding buttons
The **Button** option in the **Add** menu lets you add custom buttons to your dashboard. You can assign the button a link to either a Looker URL or an external URL. Then, when a dashboard viewer selects the button, they are taken to the URL.
To add a button to your dashboard, follow these steps:
  1. Make sure the dashboard is in edit mode.
  2. From the **Add** button menu at the top left of the dashboard pane, select the **Button** option.
A new button appears at the top of the dashboard with an open button edit window.
  3. In the **Content** tab of the button edit window, complete the following fields:
     * **Label** : This text will appear on the button. The button expands its width to accommodate the label until the label reaches the width of its tile box. Once the label reaches that limit, it will be truncated. If the label is truncated, it can be repeated in the **Description** field.
     * **Link** : This is the link that the button takes viewers to.
     * **Description** : This description will appear when you hover over the button. If you don't enter a value, the description defaults to the link.
     * **Open in a new browser tab** : Select this option to automatically open the link in a new browser tab rather than navigating away from the dashboard. This option defaults to enabled.
  4. In the **Design** tab of the button edit window, you can customize the appearance of the button:
     * **Button Style** : Select one option:
       * **Filled** : Button has a colored background and white text.
       * **Outlined** : Button has an outline and colored text.
       * **Transparent** : Button has no outline or background. It has only colored text.
     * **Color** : Select a color from one of Looker's color collections in the **Themes** tab, or customize a color in the **Custom** tab. Then select **Save**.
     * **Button Size** : Choose **Small** , **Medium** , or **Large** to set the size of the button text. The height of the button adjusts to fit the text. The default size is medium.
     * **Alignment** : Choose **Left** , **Center** , or **Right** to horizontally align the button within its tile box. The button's tile box defaults to full width, and the alignment defaults to center.
  5. Click **Save** to save your changes.


#### Moving and resizing buttons
Once added, a button can be moved and its tile box can be resized just as with any other tile.
By default, a new button is placed at the top of a dashboard within a tile box that is set to the full width of the dashboard.
Resizing a button's tile box may affect the placement of other dashboard elements, and it may affect a button's width. However, you can only adjust a button's text size or height through the **Button Size** option in the button edit window.
### Adding extensions
If you have the Looker Admin role or the `develop` permission, or if you have been granted access to one or more extensions, you will see the the **Extension** option in the **Add** menu. The **Extension** option lets you add a custom extension as a tile to your dashboard.
To add an extension as a tile, follow these steps:
  1. Make sure that the dashboard is in edit mode.
  2. From the **Add** button menu at the top left of the dashboard pane, select the **Extension** option. The Extensions panel will appear, listing all available extensions that can be installed as a tile on your dashboard.
  3. In the **Extensions** panel, in the section of the extension that you want to install, click **Add to tile**. The selected extension will be installed in the new tile on your dashboard.


### Adding data actions to tiles
If you have the `develop` permission for the model that a tile is based on, you can add data actions to that model. Data actions let dashboard viewers perform tasks with other tools directly from the dashboard tile, such as sending an email or setting values in other applications. These data actions appear in the drill menu **Actions** section.
See the `action` parameter documentation page for more information.
## Adding dashboard filters to a dashboard
The queries that underlie dashboard tiles may include filters, but you can also add filters to a dashboard itself, which can affect all tiles or just select tiles. Dashboard filters let users narrow a dashboard's results to only the data they are interested in.
To add dashboard filters, you must have at least one query tile or Look-linked tile on the dashboard. Then, you can add filters by entering edit mode and selecting the **Filters** button filter_list from the top toolbar.
To learn more about building standard dashboard filters, visit the Adding and editing user-defined dashboard filters documentation page.
To learn about turning on dashboard cross-filters, visit the Cross-filtering dashboards documentation page.
## Configuring dashboard settings
You can access the dashboard settings at the upper left of the dashboard in the blue toolbar. The default settings when you create a dashboard are as follows:
  * **Timezone**: Each tile's time zone
  * **Run on load**: Enabled
  * **Default filters view**: Expanded


See the Editing user-defined dashboards documentation page for more information about editing these settings.
## Adding a description to a dashboard
To add a description to a dashboard, make sure that the dashboard is in edit mode, and then select **Show dashboard details** from the **Dashboard actions** three-dot icon menu more_vert.
The **Description** text box will then become editable.
Once you've added a description, click **Save** to save the change.
## Improving dashboard performance using aggregate awareness
LookML developers may be able to improve dashboard performance by using aggregate awareness. With aggregate awareness, developers can create aggregate tables under LookML `explore` parameters, which can optimize queries for one or more tiles in a dashboard. The first step is to get the aggregate table LookML, which appears under the **Get LookML** option in the **Dashboard actions** three-dot icon menu more_vert. For more information, see the `aggregate_table` parameter documentation page.
Find other information and recommendations about building performant dashboards in the Considerations when building performant Looker dashboards Best Practices page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


