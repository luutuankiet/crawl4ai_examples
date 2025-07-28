# Content validation  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/content-validation

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before using the Content Validator
  * Using the Content Validator to fix errors
    * Running the Content Validator
    * Viewing the content validation results
    * Replacing names for fields, views, Explores, and models
    * Removing a field name
  * Using the Content Validator to find and replace
  * Things to consider




Was this helpful?
Send feedback 
#  Content validation
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before using the Content Validator
  * Using the Content Validator to fix errors
    * Running the Content Validator
    * Viewing the content validation results
    * Replacing names for fields, views, Explores, and models
    * Removing a field name
  * Using the Content Validator to find and replace
  * Things to consider


The Content Validator searches your LookML for the model, Explore, and field names that are referenced in your Looker content (Looks and dashboards). It's a useful tool for validating your LookML references, for fixing errors in your LookML after you have made changes, and for updating the names of LookML elements across your project.
You must have the `develop` permission to use the Content Validator. The Content Validator will run validation on all of the content that is based on LookML projects for which you have `develop` permission.
To open the Content Validator, select **Content Validator** from the **Develop** menu in the main navigation panel. From here, you can use the Content Validator in two ways:
  * Click **Validate** to find and fix errors that were caused by changes in your LookML model.
  * Click **Find & Replace in All Content** to find and replace the model, Explore, or field names across your Looker content, whether or not there are errors in the Looker content.


## Before using the Content Validator
You must be **extremely** careful when making changes using content validation. The Content Validator does not have an undo function, and it has the potential to impact many Looks and dashboards, along with their **Explore from Here** links. If you do make a mistake, you should attempt to correct it as soon as possible, before additional changes make it harder to isolate the affected Looks.
Also, consider your timing when using the Content Validator. When you push development changes to production you should fix affected Looks and tiles at approximately the same time, so that they are broken for the minimum amount of time. If you fix Looks and tiles too early, based on your work in Development Mode, they will appear broken to users until you push your changes. Similarly, if you delay in fixing Looks and tiles until long after pushing the changes, the Looks and tiles will appear broken to users until you fix them.
## Using the Content Validator to fix errors
The Content Validator is a useful tool for finding and fixing errors resulting from changes in your LookML. For example, if you change a field name from `customer` to `user`, any Looks or dashboard tiles that included the `customer` field will no longer function (unless you used the `alias` parameter). The Content Validator will list any references to the `customer` field and will also provide **Replace** or **Remove** buttons to fix the error.
When you run the Content Validator, it validates all references that your Looks and dashboards make to your LookML models, Explores, views, and fields, and will show an error for any references your content makes to an unknown LookML object.
The Content Validator does _not_ show errors for the following:
  * **Looks that have been deleted and are in theTrash.** If you want to validate a deleted Look, your Looker admin must restore the Look first.
  * **Content that is based on LookML models for which you don't have`develop` permission.** You can use the Content Validator only on the content that is based on models for which you have `develop` permission (the models that you can see in the Looker IDE). See the Roles documentation page for information on model permissions. 


### Running the Content Validator
When you run the Content Validator, you can scope the validation to specific LookML projects and a specific content folder (including its subfolders, if any). This can improve the performance of the Content Validator.
Note the following for Content Validator scoping:
  * If you don't specify a folder or a LookML project, the validation won't be scoped. The Content Validator will validate all the content that is based on models for which you have `develop` permission.
  * If you specify a content folder, the Content Validator will run validation on the content folder and all of its subfolders, if any.
  * If you specify a content folder and one or more LookML projects, both conditions will apply: the Content Validator scopes its validation to only the content in the folder (and subfolders) that is based on the LookML projects you selected. 
  * Dashboard alerts, dashboard schedules, and Look schedules are not stored in content folders. Therefore, if you scope the content validation to a folder, the Content Validator won't validate any schedules or alerts.
  * If you specify a LookML project, the Content Validator determines the project's associated models by looking at the source LookML of the specified projects and by looking at the models configured for each project, which you can see on the **LookML Projects** page. If a model file has been deleted from a LookML project and isn't shown as a model in the project on the **LookML Projects** page, the Content Validator won't show errors that are related to content based on that deleted model. 


To run the Content Validator, follow these steps:
  1. Click the menu Looker **Main menu** icon and select **Develop** , if the **Develop** menu isn't already displayed.
  2. From the **Develop** menu, select **Content Validator**.
  3. On the Content Validator page, click **Validate**.
The Content Validator displays the **Choose Projects to Validate** dialog.
  4. In the **Choose Projects to Validate** dialog, do one of the following:
     * To run the validator on all LookML projects, leave the **Select projects** field as it is, with no projects selected, and then click **Next**.
     * To run the validator on one or more specific LookML projects, click the **Select projects** drop-down menu, select the projects that you want to validate, and then click **Next**.
The Content Validator displays the **Choose Folder to Validate** dialog.
  5. In the **Choose Folder to Validate** dialog, do one of the following:
     * To run the validator on all content folders, leave the **Folders** picker as it is, with no folders selected, and then click **Next**.
     * To run the validator on one specific content folder (and its subfolders, if any), use the **Folders** picker to select the folder that you want to validate, and then click **Next**.
The **Review Selections** dialog displays the projects and the folders that you selected for validation.
  6. In the **Review Selections** dialog, click **Validate**.


The Content Validator will run validation on the content that you specified and then display the results. See the section Viewing the content validation results for information about reviewing the results.
### Viewing the content validation results
When the Content Validator completes a validation, it displays an error table. The validation results are scoped to the projects and folders that you selected when you ran the Content Validator.
The content validation results show Looker content that uses model names, Explore names, view names, or field names that don't exist or can't be found. See the Using the Content Validator to fix errors section for details about the LookML elements that the Content Validator can find and validate.
Validation results are based on the LookML that is available in the mode you're in when you run the validator. If you are in Production Mode, the validation results will reflect all LookML that has been pushed to production. If you are in Development Mode, the validation results will reflect your saved LookML, even if the LookML hasn't been pushed to production. 
The error table displays each error, along with a list of Looks and tiles that contain the error, plus the underlying model and Explore that are producing the error. 
You can use the **Group by** tabs at the upper right of the page to change the layout of the error table:
  * **Error** : List each error, grouping together the Looker content that has the error. This is useful if you want to fix the same error in multiple pieces of content at once.
  * **Folder** : List each folder, grouping together the Looker content that has errors. This is useful if you want to fix only the errors in a particular folder.
  * **Content** : List each piece of content that has errors, grouping together its errors. This is useful if you want to fix all the errors in a single Look, tile, filter, etc.


The icon next to the content's name identifies the content type:
  * — Dashboard tile
  * — Dashboard alert
  * — Schedule for a dashboard or Look
  * — Filter for a dashboard, or a field on a tile that listens to a dashboard filter (see the Adding and editing user-defined dashboard filters documentation page for information on configuring tiles to listen to dashboard filters)


Errors may be caused by intentional changes in your LookML as well as a typo or a missing join.
For each row, Looker provides either a **Replace** button or a **Remove** button, or both, depending on the error type. These buttons provide functionality to fix the errors and are described in more detail in Using the Content Validator to fix errors. To adjust errors, you can use the **Replace** and **Remove** buttons in each line of the error table as follows:
  * **Replace** : Looker provides the **Replace** button for each error (see the Replacing names for fields, views, Explores, and models section later on this page for how to replace names with the Content Validator).
  * **Remove** : For errors with field names in the **Data** section of a Look or tile, Looker also displays the **Remove** button (see the Removing a field name section later on this page for how to remove names with the Content Validator).


Depending on your **Group by** setting, the **Replace** and **Remove** buttons will apply to a single item (Look or tile), or to multiple items:
  * If you group by **Error** , the buttons apply to all occurrences of that error in all Looks and tiles on your Looker instance — which lets you fix all occurrences in a single operation.
  * If you group by **Folder** or by **Content** , the buttons apply to one occurrence of the error in a single Look or tile — which lets you consider each occurrence of the error separately.


For example, an error table is grouped by **Error** and displays three instances of content with an unknown Explore named `customers`. The action provided for the three pieces of content is **Replace**. Clicking **Replace** would affect all three instances of content with the error `3 x Unknown explore 'customers'`.
In some cases, multiple errors may exist for pieces of content. For example, an error table is grouped by **Content** and displays a piece of content called **Order Details**. There are four `Unknown field` errors displayed in the **Errors** column, and each error has its own **Replace** and **Remove** action buttons in the **Actions** column.
In addition, if you group by **Content** , you have the additional option to delete Looks.
### Replacing names for fields, views, Explores, and models
The content validation results include a **Replace** button for the following types of elements so that you can rename them:
  * Model names in Looks and dashboard tiles
  * Explore names in Looks and dashboard tiles
  * View names in custom filters or table calculations
  * View names in Looks and dashboard tiles
  * Field names: 
    * In the **Data** section of a Look
    * In a query-based dashboard tile
    * Referenced in table calculations
    * Referenced in custom filters
    * Referenced in custom fields
    * Referenced in visualization configurations, such as the **Customizations** area of the **Series** tab for column charts
    * Referenced by a dashboard tile to listen to a dashboard filter (this is configured in the **Tiles to Update** tab of the filter configuration window, described on the Adding and editing user-defined dashboard filters documentation page)


For any of these errors, you can use the Content Validator to replace an attribute of the content that is equal to or more general than the attribute that is erroring:
  * If a field is causing an error, you can replace or remove the field, or you can replace the view, Explore, or model name.
  * If an Explore name is causing an error, you can replace the Explore name or the model name.
  * If a model name is causing an error, you can replace the model name.


Here's how to use the Content Validator to replace the names of elements in your model:
  1. Click **Validate** to run the Content Validator.
  2. Select a **Group by** setting to choose how errors are grouped. For example, you can group by **Error** so that you can adjust multiple items at the same time.
  3. In the error table, click the **Replace** button next to the error that you want to correct to open the **Update in Content** dialog.
  4. In the **Type** section of the **Update in Content** dialog, select the type of LookML element that you want to change: field, view, Explore, or model. Looker displays the appropriate options for each error.
  5. In the **Name** section, verify the name of the item that you want to replace. The Content Validator fills this information in automatically.
  6. In the **Replacement Name** section, enter the new name of the item.
  7. If you have grouped by **Error** and there are multiple items that will be affected, you can click **Show Content** to see a list of items that the Content Validator will update.
  8. Optionally, you can clear the checkboxes next to any listed items to leave their names unchanged.
  9. To make the change, click **Replace**.


### Removing a field name
For errors with field names in the **Data** section of a Look or tile, the error table will provide a **Remove** button to the right of the error. You can use the Content Validator to remove fields that are:
  * In the **Data** section of a Look or dashboard tile
  * Referenced in visualization configurations, such as the **Customizations** area of the **Series** tab for column charts
  * Referenced by a dashboard tile to listen to a dashboard filter (this is configured in the **Tiles to Update** tab of the filter configuration window, described on the Adding and editing user-defined dashboard filters documentation page)


You cannot use the Content Validator to remove fields from custom filters, custom fields, or table calculations, because typically you need to make additional changes to keep the expression working. Instead, use the content validation error messages to find places where custom filters, custom fields, and table calculation expressions need to be fixed, and then rework the expression as appropriate.
  1. Click **Validate** to run the Content Validator.
  2. Select a **Group by** setting to choose how errors are grouped. For example, you can group by **Error** so that you can adjust multiple items (Looks, tiles, or both) at the same time.
  3. In the error table, click **Remove** next to the field error that you want to correct to open the **Remove Field from Content** dialog.
  4. In the **Field** section of the **Remove Field from Content** dialog, verify the name of the item that you want to remove. The Content Validator fills this in automatically.
  5. If you have grouped by **Error** and there are multiple items (Looks, tiles, or both), you can click **Show Content** to see a list of items that the Content Validator will update.
  6. Optionally, you can clear the checkboxes next to any Looks or tiles to leave their names unchanged.
  7. Click **Remove Field** to make the change.


### Deleting Looks
If you group the error table by **Content** , you have the option to delete Looks in the table.
To use the Content Validator to delete Looks:
  1. Click **Validate** to run the Content Validator.
  2. Group the table by **Content**.
  3. In the error table, click the **Select** box next to the Look or Looks that you want to delete.
  4. Click the **Delete all selected Looks** button at the top of the error table.
  5. Click **OK** in the confirmation box to delete the selected Look or Looks.


## Using the Content Validator to find and replace
The Content Validator can also be used to search and replace the names for models, Explores, and fields. For example, you might decide that you prefer one field over another and want to make that replacement in your project, even though there is no error. The complete list of elements that the Content Validator can search and replace is provided in the Replacing names for fields, views, Explores, and models section.
To use the Content Validator as a find and replace tool:
  1. On the Content Validator screen, click **Find & Replace in All Content** to open the **Update in Content** dialog.
  2. Select the **Type** of LookML element that you want to change (field, view, Explore, or model).
  3. Enter the **Name** of the item that you want to replace.
  4. Enter a **Replacement Name** for the field, view, Explore, or model.
  5. Click **Replace** to make the change.


## Things to consider
Plan to rerun content validation to view the results of any fixes you make.
Note the following about the Content Validator:
  * For views, Explores, or models, you can change their names but you cannot _remove_ their names entirely. See the Removing a field name section for a list of items that you can remove with the Content Validator.
  * Table calculations can only reference fields that are included in the query of a Look or tile. This means that if you remove a field from a Look or tile's query but a table calculation still uses that field, you'll get a new content validation error.
  * Looks that have been deleted and are in the Trash folder won't be validated. If you want to validate a deleted Look, your Looker admin must restore the Look first.
  * If you are in Development Mode, the validation results will reflect your saved LookML even if it hasn't been pushed to production. However, any changes that you make using the Content Validator will affect users viewing content in Production mode. Consider switching to Production mode before running the Content Validator.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


