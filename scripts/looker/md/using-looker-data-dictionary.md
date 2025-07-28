# Using the Looker Data Dictionary extension  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/using-looker-data-dictionary

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Data Dictionary workflow
    * Before you begin
  * Installing the Looker Data Dictionary
    * Granting permissions to access the Looker Data Dictionary extension
    * Granting permissions to interact with field comments
  * Navigating to the Looker Data Dictionary extension
  * Viewing model metadata with the Looker Data Dictionary
  * Selecting a model and an Explore
  * Filtering fields in an Explore
  * Viewing field metadata
    * Customizing displayed metadata
  * Using field comments
    * Adding a field comment
    * Viewing field comments
    * Editing or deleting a field comment
    * Sharing a field comment
  * Using the field profiler




Was this helpful?
Send feedback 
#  Using the Looker Data Dictionary extension
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Data Dictionary workflow
    * Before you begin
  * Installing the Looker Data Dictionary
    * Granting permissions to access the Looker Data Dictionary extension
    * Granting permissions to interact with field comments
  * Navigating to the Looker Data Dictionary extension
  * Viewing model metadata with the Looker Data Dictionary
  * Selecting a model and an Explore
  * Filtering fields in an Explore
  * Viewing field metadata
    * Customizing displayed metadata
  * Using field comments
    * Adding a field comment
    * Viewing field comments
    * Editing or deleting a field comment
    * Sharing a field comment
  * Using the field profiler


The Looker Data Dictionary is an extension — a web application built using Looker components — developed using the Looker extension framework and deployed through the Looker Marketplace.
The Looker Data Dictionary extension provides a dedicated, centralized interface for searching through all your Looker fields and descriptions. Use this extension to perform these tasks:
  * Provide a searchable directory for all metrics and descriptions for users to identify the appropriate dimension or measure for analysis.
  * Enable external stakeholders to identify and locate unique metrics.
  * Audit LookML models to assess whether consistent naming conventions are followed, whether there are redundant fields, or whether fields are annotated with descriptions.
  * Add and share comments about specific fields (if your Looker Data Dictionary application is on version 2.0.0 or later). You can verify that you have the most updated version of the Data Dictionary by going to the Looker Marketplace, selecting **Manage** , and selecting the **Update** button next to the extension.


## Data Dictionary workflow
For users to access and use the Looker Data Dictionary, a Looker admin must perform the following steps:
  1. Enable the appropriate features.
  2. Install the Looker Data Dictionary extension.
  3. Grant permissions to access the Looker Data Dictionary.


Once the extension is available to users, you can do the following:
  1. Navigate to the Looker Data Dictionary extension.
  2. View your model's metadata.


### Before you begin
Before installing the Looker Data Dictionary from the Marketplace, a Looker admin must enable these features:
  * **Marketplace**: To access the Looker Marketplace (enabled by default)
  * **Extension Framework**: To deploy extensions that are developed using the Looker extension framework (enabled by default)


Installing applications and tools — such as extensions — from the Looker Marketplace requires that you have the `develop`, `manage_models`, and `deploy` permissions.
## Installing the Looker Data Dictionary
See the Using the Looker Marketplace documentation for instructions on installing a tool from the Looker Marketplace. After the Data Dictionary is installed, a Looker admin must grant users permissions to perform the following tasks:
  * Access the Looker Data Dictionary extension
  * Interact with field comments


### Granting permissions to access the Looker Data Dictionary extension
After the Looker Data Dictionary is installed, a model called `data-dictionary` is automatically added to the list of available models on the **New Model Set** and **Edit Model Set** pages, accessible from the **Roles** page in the **Admin** panel.
A Looker admin must grant users `explore` or `develop` permissions to access the `data-dictionary` model and any models they need to explore in the Data Dictionary. See the Setting permissions for Looker extensions documentation page for information on granting users permissions to access and use extensions.
### Granting permissions to interact with field comments
Field comments provide users with the ability to add context to field definitions without having to update any LookML. By default, all users who have access to the data dictionary extension will be able to see all comments, and add, edit, and delete their own comments.
A Looker admin can manage how users interact with the field comment functionality by creating specific user groups on the **Groups** page of the **Admin** panel and assigning users to those groups. See the Groups documentation page for more information about how to assign users to groups.
The user groups must be created with the predefined names that are shown in the Group Name column of the following table. The table also shows the predefined privileges that users assigned to each group will have.
Group Name | Privileges  
---|---  
`marketplace_data_dictionary_comments_disabled` | Users cannot see or otherwise interact with any comments; all comment capabilities are disabled. This group's privileges always take precedence over those of other groups — any user included in the `disabled` group won't be able to see or make comments, even if they also belong to another group that has more elevated privileges.  
`marketplace_data_dictionary_comments_reader` | User can see existing comments, but cannot add any.  
`marketplace_data_dictionary_comments_writer` | Users can see all comments, add new comments, and edit/delete their own. **This is the default privilege.**  
`marketplace_data_dictionary_comments_manager` | Users can see all comments, add new comments, and edit/delete all comments.   
If a user doesn't belong to any of these groups, they will default to `writer`. If a user is assigned to multiple groups (not including `marketplace_data_dictionary_comments_disabled`), their more elevated privilege takes precedence.
## Navigating to the Looker Data Dictionary extension
You can navigate to the Data Dictionary from the list of installed applications and extensions in the left sidebar.
## Viewing model metadata with the Looker Data Dictionary
In the Looker Data Dictionary, users with `explore` permissions on a model can select this model and view its metadata, including its Explores and each Explore's list of fields, grouped by view. The Looker Data Dictionary displays the selected model's Explores in the left sidebar and the selected Explore's views and fields on the main part of the page.
Users can collapse the sidebar by selecting the icon.
The Looker Data Dictionary shows the following information:
  1. The name of the selected model
  2. The list of Explores contained in the selected model
  3. The selected Explore
  4. A text field to filter the fields in an Explore
  5. Quick filters to narrow displayed fields based on selected characteristics
  6. The name of the view
  7. Metadata about each field. Select what metadata is displayed by selecting the **View Options** button. See the field's entire set of metadata in the field profiler.
  8. Rows containing metadata for each field in a given view
  9. Navigation to the Explore in the Looker UI


## Selecting a model and an Explore
The **Select a Model** drop-down lists all the models for which a user has `explore` permissions. When choosing a model from the **Select a Model** drop-down menu, the left sidebar will populate with a list of that model's Explores.
You can also search the selected model for a specific Explore by typing in the **Search Model** search box. The list of Explores will filter to display only the results that match your search terms.
Select the name of an Explore to see its fields, grouped by view, displayed on the main part of the page.
You can also select the **Explore** button in the upper right corner to go straight to the Explore page in Looker.
## Filtering fields in an Explore
You can filter the displayed fields by typing text into the **Filter fields in this Explore** box to match against the list of fields' **Field Label** or **Description**.
You can also select specific metadata attributes to filter on, such as whether the field:
  * Has a description
  * Is a dimension or a measure
  * Has type string, number, date, zipcode, count, sum, average, list, or unquoted


## Viewing field metadata
The Looker Data Dictionary displays the metadata for an Explore's fields, grouped by view:
  * **Field Label** : The field name according to the field's `label` parameter
  * **Category** : The field category as a dimension or a measure
  * **Description** : The field's description according to the field's `description` parameter
  * **LookML Name** : The field name in `view_name.field_name` syntax
  * **Type** : The field type as string, number, date, zipcode, count, sum, average, list, or unquoted according to the field's `type` parameter
  * **SQL** : The SQL expression that references that field
  * **Tags** : The LookML tags associated with that field


### Customizing displayed metadata
You can specify what metadata is displayed for each field by selecting the **View Options** button in the upper right corner and checking or unchecking the boxes for metadata you want to view.
## Using field comments
LookML developers often include additional information or explanations about a model's fields in the field-level `description` parameter. However, these descriptions are not always meaningful or useful to all users. With field-level comments, users can add context to a specific field. These comments are viewable by other users but will not affect the model's underlying LookML.
A Looker admin must grant users the ability to interact with comments by adding them to specific groups on the **Groups** page of the **Admin** panel. By default, all users with access to the data dictionary extension can view all comments and add, edit, and delete their own comments.
### Adding a field comment
To add a comment to a field:
  1. Hover over the field row to reveal a **+** icon (if there are no existing field comments) or a notepad icon (if a field has existing comments). Click the icon to open the **Comments** tab of the field profiler panel.
  2. Click the **Add Comment** button.
  3. Type your comment and select the **Comment** button to save your entry. Click **Cancel** to close the field profiler. You can expand the comment box by selecting and dragging the bottom right corner.


Once a comment has been added, it appears on the **Comments** tab of the field profiler and is viewable to other users.
### Viewing field comments
When a field includes comments, a notepad icon appears with the number of comments that exist on that field. Click the notepad icon to view the field's comments listed in the **Comments** tab of the field profiler.
The number of comments on that field is also indicated in parentheses on the **Comments** tab. Each comment entry shows the following information:
  * The commenter's name
  * The timestamp showing when the comment was added
  * A preview of the comment


### Editing or deleting a field comment
To edit or delete your own field comments:
  1. Select the field's notepad icon.
  2. On the **Comments** tab, locate and hover over the comment that you would like to edit or delete.
  3. Click the three-dot menu, and select **Edit Comment** to edit the comment or **Delete Comment** to delete the comment. If you're deleting the comment, confirm your intention.
  4. If you're editing your comment, select **Save** once you've made your changes.


### Sharing a field comment
The URL of the **Comments** tab for each field is unique and can be copied and shared with other users who have access to that model in the Looker Data Dictionary.
## Using the field profiler
Click a specific field row to open a field profiler panel that displays the field's entire set of metadata, options to preview numeric dimension values, and buttons to navigate to the Looker IDE or the Explore page.
> If you're using version 2.0.0 or later of the Looker Data Dictionary extension, the field profiler opens by default to the **Details** tab.
In the **Distribution** section, select **Calculate** to show a preview of a column chart depicting the distribution of the count values for numeric dimensions on a view with a measure that has `type: count`. The **Distribution** section will also display the minimum, maximum, and average values of the numeric dimension series.
Under **Values** , select **Calculate** to show a preview of count values for numeric dimensions on a view with a measure that has `type: count`. Select the **Explore More** button to open the Explore UI with the numeric dimension and count measure pre-selected from the field picker.
Select **Go to LookML** to open the view file from the LookML project that is associated with the selected model in the Looker IDE.
Select the **Explore with Field** button to open the Explore page with that field automatically selected from the field picker.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


