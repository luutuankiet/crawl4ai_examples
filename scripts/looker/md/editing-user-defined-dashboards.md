# Editing user-defined dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/editing-user-defined-dashboards

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Entering edit mode in dashboards
  * Rearranging and resizing tiles
  * Editing dashboard settings
    * Allow full-screen mode for visualizations
    * Default filters view
    * Filters location
  * Editing dashboard details
  * Deleting dashboards
  * Keyboard shortcuts when dashboards are in edit mode




Was this helpful?
Send feedback 
#  Editing user-defined dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Entering edit mode in dashboards
  * Rearranging and resizing tiles
  * Editing dashboard settings
    * Allow full-screen mode for visualizations
    * Default filters view
    * Filters location
  * Editing dashboard details
  * Deleting dashboards
  * Keyboard shortcuts when dashboards are in edit mode


To edit a dashboard, you must have the following prerequisites:
  * The **Manage Access, Edit** access level for the folder in which the dashboard resides
  * The appropriate Looker permissions to edit the dashboard


Additionally, to edit a specific dashboard tile, you must have access to the model that the tile is based on.
If you don't have access to all the models that a particular dashboard's tiles are based on, you can still edit other parts of the dashboard, such as the dashboard title, dashboard settings, dashboard filters (although you will not see filter suggestions for filters based on fields in a model you do not have access to), and tiles for which you do have model access.
When editing a dashboard, keep in mind best practices for dashboard construction. Find information and recommendations about building performant dashboards in the Considerations when building performant Looker dashboards Best Practices page.
## Entering edit mode in dashboards
To enter edit mode, select **Edit dashboard** from the three-dot **Dashboard actions** menu.
In edit mode, you can add, move, edit, or delete tiles or filters, or edit the dashboard title.
When you are in edit mode, Looker displays a blue toolbar at the top of the dashboard that contains the following options:
  * **Add**
  * **Filters**
  * **Settings**
  * **Quick layout**
  * **Cancel**
  * **Save**


After you make at least one edit, the **Save** button becomes available. Click **Save** to save your edits and exit edit mode.
To discard your edits, click **Cancel**. In the **Discard changes?** dialog box, click **Discard** to confirm that you want to cancel and exit edit mode. The **Discard changes?** dialog box also appears if you attempt to navigate away from the dashboard by clicking on the navigation breadcrumb or the forward or back arrows on your browser.
## Rearranging and resizing tiles
In edit mode, you can move and resize tiles on a dashboard.
To move a tile, drag the six-dot icon in the upper left of a tile. When you drag a tile to a new location on the dashboard, blue grid lines appear to help you position the tile.
To resize a tile, either drag the bottom right corner of the tile or use the **Resize tile** option in the three-dot **Tile actions** menu at the top right of each tile. The available preselected sizes are as follows:
  * **Extra small** — Each tile takes up one-sixth of the dashboard row.
  * **Small** — Each tile takes up one-fourth of the dashboard row.
  * **Medium** — Each tile takes up one-third of the dashboard row.
  * **Large** — Each tile takes up one-half of the dashboard row.
  * **Extra Large** — Each tile takes up the entire width of the dashboard row.


Only the selected tile is resized. Tile sizes are responsive to the size of the dashboard.
If you want to resize a tile to be very short, hiding the tile title can help you make the tile as short as possible.
You can also use the **Move tile** option in the tile's edit menu to move the tile to the top or the bottom of the dashboard.
#### Tile size and grid layout
When you add a visualization using grid layout to a dashboard, the grid arrangement can become responsive to the size of the dashboard tile.
For example, you have a dashboard tile with a visualization that uses a grid layout of four small charts. If you size the tile to be short and wide, the small charts appear as one row of four. If you size the tile as a square, the small charts reposition to two rows of two. If you size the tile to be narrow but tall, the charts reposition to four rows of one.
To ensure that the grid arrangement is responsive, do not enter a number into the visualization's **Number of Charts per Row** setting. If you enter a value into **Number of Charts per Row** , the dashboard tile respects that setting regardless of the size or shape of the dashboard tile.
## Adding tiles
In edit mode, you can add tiles or text to your dashboard. See the Creating user-defined dashboards documentation page for information about how to add text and tiles.
## Editing tiles
In edit mode, the three-dot **Tile actions** menu at the top right of each tile shows the available edit options.
These options differ slightly depending on whether or not you are viewing a query tile or a Look-linked tile.
  * In both cases, Looker displays the options **Edit** , **Hide title** , **Add note** , and **Move tile**. 
    * For query tiles, Looker also displays the options **Duplicate tile** , **Delete** , and **View**.
    * For Look-linked tiles, Looker also displays the option **Remove Look**.


#### Editing a query tile title
In edit mode, you can edit a query tile's title by clicking on the title and making your edits. Click **Save** at the upper right of the dashboard to save your changes.
You can also edit tile titles for both query tiles and Look-linked tiles when editing a tile's underlying query or Look.
#### Editing a tile's query or Look
> If you save edits to a Look, it affects every dashboard where that Look is used.
In edit mode, you can edit a tile's underlying query or Look — including the title of the tile and the visualization — directly in the dashboard.
Click **Edit** in the tile's three-dot **Tile actions** menu.
If you are editing a Look, the **Edit Look** toolbar displays the dashboards that contain tiles linked to that Look. Those dashboards will be affected by your changes. If you are editing a query tile, you will not see a list of dashboards affected in the edit pane, because your edits only affect the tile and dashboard you are in.
> When you're editing a dashboard tile that contains a funnel chart or a timeline chart, the charts look different on the dashboard tile than they do in the edit window. Additionally, map charts' tooltips function differently when viewed on dashboard tiles. For more information, visit the funnel chart, timeline chart, and map chart documentation pages.
#### Hiding or showing a tile title
In edit mode, you can hide or show the title of a tile. By default, tile titles are shown. You can hide a title by clicking **Hide title** in the tile's three-dot **Tile actions** menu.
If the title is hidden, Looker instead displays the option **Show title** in the tile's three-dot **Tile actions** menu.
The hide/show option does not appear in the three-dot **Tile actions** menu of text tiles or tiles that use single value visualizations. To hide or show the title of a single value visualization, click **Edit** in the tile's three-dot **Tile actions** menu, toggle the **Show Title** switch in the style menu, and save. To hide or show a title of a text tile, click **Edit** in the tile's three-dot **Tile actions** menu, remove or reinstate the tile title, and save.
#### Adding a tile note
In edit mode, click the **Add note** button in the tile's three-dot **Tile actions** menu.
Enter the note text and configure the following display options:
  1. In the **Note Text** field, enter the note text to show on the tile. You can use plain text or HTML.
  2. In the **Display Location** field, select the location of the note. The options are above the visualization, below the visualization, or as text that appears when users hold their pointers over a circled _i_ icon to the right of the tile title. For tiles containing single value visualizations that are sized to be 150 pixels tall or shorter, title notes render as hover text regardless of the location selected in this field.
  3. Check the **Collapse note** box to collapse the note by default. A collapsed note shows only the first line, with an ellipsis at the end of the line. Unchecking this box displays the note's full text by default. If you select **On icon hover** under **Display Location** , you won't see this option.
  4. Click **Add** or **Cancel** to add the note to the tile, or cancel it.


The note appears on the tile with a collapse/expand arrow to the left of the note. Clicking that arrow or anywhere on the note toggles between collapsed and expanded displays.
Once you add a note to a tile, the tile's three-dot **Tile actions** menu changes to display **Edit note** instead of **Add note**. Click **Edit note** to edit or delete your note.
#### Duplicating a query tile
In edit mode, you can duplicate query tiles by clicking **Duplicate tile** from the tile's three-dot **Tile actions** menu:
Looker creates a copy of the tile with the same query and visualization settings and adds the new tile to the bottom of the dashboard. From there, you can move or resize the tile, edit the tile title, or edit the new tile to adjust the visualization or the underlying query.
You cannot duplicate a Look-linked tile and will not see **Duplicate tile** in the three-dot **Tile actions** menu of Look-linked tiles.
#### Editing text
There are two types of text tiles, each of which offers a different editing experience but results in the same kind of tile:
  * **Text** : A dashboard text tile that provides a visual editing experience.
  * **Markdown** : A dashboard text tile that can be edited using some HTML and a subset of the Markdown markup language to format the tile.


To edit a **Text** tile, enter edit mode and click within the tile to make edits.
To edit a **Markdown** tile, enter edit mode and select **Edit** from the tile's three-dot **Tile actions** menu.
#### Move tile options
In edit mode, you can move a tile to the top, bottom, left, or right side of the dashboard. Click the three-dot **Dashboard actions** menu, select **Move tile** , and then select one of the following options:
  * **Move to top**
  * **Move to bottom**
  * **Move to left side**
  * **Move to right side**


The tile will remain in the column or row it's located in. If the tile is already at the top, bottom left, or right side of the column, the option to move it to that spot is disabled.
#### Deleting a tile
In edit mode, you can delete a tile from a dashboard. Select **Delete** (for a query tile) or **Remove Look** (for a Look-linked tile) from the tile's three-dot **Tile actions** menu. This deletion cannot be undone.
Deleting a Look-linked tile from a dashboard does not affect the underlying Look.
## Editing dashboard settings
In edit mode, click **Settings** in the upper left of the blue toolbar to edit dashboard settings.
### Time zone
This option is only available if your Looker admin has enabled the **User Specific Time Zone** setting.
Select the time zone in which your dashboard will be run. Dashboard viewers will be able to temporarily change the time zone setting when viewing the dashboard.
You can choose one of the following options:
  * **Each tile's time zone** to run all the tiles in the time zone in which they were saved
  * **Viewer time zone** to run all tiles in each viewer's time zone
  * Select a specific time zone from list in the drop-down menu to run all the tiles in that time zone


### Run on load
If **Run on load** is enabled, dashboard data automatically loads when the dashboard is first loaded.
If **Run on load** is disabled, the dashboard does not display any data until the reload data icon is clicked.
### Allow full-screen mode for visualizations
If your Looker admin has enabled the **Full Screen Visualizations** Labs feature, an option for **Allow full-screen mode for visualizations** appears in the dashboard settings. This option defaults to enabled.
Disabling this option on a dashboard prevents viewers of that dashboard from seeing the **View** option in each dashboard tile's three-dot **Dashboard actions** menu, and viewers will not be able to see dashboard tiles in full-screen or expanded formats.
### Autorefresh
It might make sense to automatically refresh the data on a regular schedule to ensure that it is up-to-date. You can set autorefresh frequencies for an entire dashboard or for individual tiles. Autorefresh never pulls results from the Looker cache; it always pulls the data from the database.
**To set autorefresh for a dashboard and all its tiles:**
  1. Enable the **Automatically refresh dashboard** switch.
  2. Select a refresh frequency to automatically update the dashboard and all its tiles.
  3. To adjust the frequency for any individual tiles, do so in the **Tile** section, where each tile in the dashboard is listed. Click the drop-down for that tile in the **Refresh frequency** column, select **Refresh every** , and then set your frequency.
  4. Click **Save** to save your changes.


**To set autorefresh for individual tiles but not for the dashboard:**
  1. Disable the **Automatically refresh dashboard** switch (if previously enabled).
  2. In the **Refresh frequency** column of the **Tile** section, click the drop-down for a tile to autorefresh.
  3. Select **Refresh every**.
  4. Set your frequency.
  5. For any tiles you do not want to autorefresh, leave the setting as **Does not refresh**.
  6. Click **Save** to save your changes.


The frequency settings accept whole numbers.
The autorefresh intervals begin at the time of day that you turn on this feature, and the dashboard refreshes on the interval you set as long as the dashboard is open in a browser tab and is not in edit mode. If the dashboard is closed or in edit mode during a scheduled refresh time, it won't refresh. If the dashboard is closed or goes into edit mode, regardless of whether or not it is during a scheduled refresh time, the refresh interval restarts as soon as the dashboard is opened again or leaves edit mode.
For example, if it is 8:33 a.m. when you set a daily refresh, the dashboard will refresh the next day at 8:33 a.m. and then refresh again each following day at 8:33 a.m. However, if one day you enter edit mode at 9:02 a.m. and exit edit mode at 9:45 a.m., from then on, the daily refresh will occur at 9:45 a.m, beginning the following day.
The **Clear cache and refresh** and **reload data** options are independent of the autorefresh interval, meaning that manually refreshing the dashboard does not restart the autorefresh interval. For example, if a dashboard's autorefresh interval is 1 hour, you can use the **Clear cache and refresh** option 40 minutes after an autorefresh and the dashboard will still autorefresh 20 minutes later (1 hour after it was last autorefreshed).
Similarly, autorefresh works regardless of whether **Run on load** is enabled or disabled. If **Run on load** is disabled and you open a dashboard with autorefresh settings, the refresh interval begins upon opening regardless of whether you click the reload data icon to load the data initially.
#### Autorefresh and performance
Frequent dashboard updates, especially on large dashboards, can place a significant strain on some database systems. You may want to discuss this consideration with your Looker admin. At a minimum, avoid setting a refresh interval that is shorter than your database update interval, as there would be no new data to refresh and this would trigger unnecessary queries.
Likewise, when multiple users access a dashboard with autorefresh, it may impede performance. To display your dashboard on a shared screen while multiple users simultaneously access it, you can create two identical dashboards and configure only the dashboard on the shared screen to refresh automatically.
Find more information and recommendations about building performant dashboards in the Considerations when building performant Looker dashboards Best Practices page.
### Default filters view
On the **Filters** tab of the **Settings** window, you can set the **Default filters view** option to one of the following:
  * **Expanded** — The filter bar shows on page load and filters are shown by default.
  * **Collapsed** — The filter bar does not show on page load and filters are hidden by default.


Click **Save** to save the change.
The **Default filters view** option defaults to **Expanded**. If you change the setting to **Collapsed** , you need to exit edit mode and then refresh the dashboard to see your change.
Dashboard viewers can temporarily change the filter bar back and forth between collapsed and expanded by clicking the filters icon. However, only the **Default filters view** setting permanently changes the default state of the filter bar.
### Filters location
On the **Filters** tab of the **Settings** window, you can set the **Filters location** option to one of the following:
  * **Top** — The filter bar appears at the top of the dashboard.
  * **Right** — The filter bar appears at the right of the dashboard.


Click **Save** to save the change.
The **Filter location** option defaults to **Top**.
## Quick layout
In edit mode, click **Quick layout** in the upper left of the blue toolbar to set all tiles to the same size. The five options for tile size are as follows:
  * **XS** — Six tiles fit in a row on the dashboard.
  * **S** — Four tiles fit in a row on the dashboard.
  * **M** — Three tiles fit in a row on the dashboard.
  * **L** — Two tiles fit in a row on the dashboard.
  * **XL** — One tile fits in a row on the dashboard.


Tile sizes are responsive to the size of the dashboard. Quick layout affects all tiles including text tiles, visualization tiles, Markdown tiles, and buttons.
## Editing dashboard details
In edit mode, select **Show dashboard details** from the three-dot **Dashboard actions** menu. The **Description** text box then becomes editable.
Once you are finished editing the description, click **Save** to save the change.
## Deleting dashboards
If you have the **Manage Access, Edit** access level for a dashboard, you can delete it in one of two ways:
  * You can delete one or more dashboards at a time from folders, as described on the Organizing and managing access to content documentation page.
  * You can delete a single dashboard by selecting **Move to trash** from the dashboard's three-dot **Dashboard actions** menu.


Once you delete a dashboard, only a Looker admin can retrieve it from the trash.
## Keyboard shortcuts when dashboards are in edit mode
To see the keyboard shortcuts that you can use when editing dashboards, visit the Keyboard shortcuts in Looker documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


