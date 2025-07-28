# Adding custom fields  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/custom-fields

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Custom fields are different from LookML-defined fields and table calculations
  * Custom field types
    * Custom field types for dimensions
    * List of unique values
    * Custom field types for measures
    * How custom fields interpret date and time data types
    * How custom fields interpret numeric measures
  * Creating a custom measure from a dimension
    * Using the dimension's three-dot More menu
    * Using the Custom Fields section
  * Adding a filter to a custom measure
  * Creating a filtered measure from another measure
  * Creating a custom dimension using a Looker expression
  * Viewing and using custom fields
    * Viewing custom fields
    * Using custom fields
  * Duplicating a custom field
  * Editing a custom field
    * Editing a custom dimension
    * Editing a custom measure
  * Deleting a custom field




Was this helpful?
Send feedback 
#  Adding custom fields
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Custom fields are different from LookML-defined fields and table calculations
  * Custom field types
    * Custom field types for dimensions
    * List of unique values
    * Custom field types for measures
    * How custom fields interpret date and time data types
    * How custom fields interpret numeric measures
  * Creating a custom measure from a dimension
    * Using the dimension's three-dot More menu
    * Using the Custom Fields section
  * Adding a filter to a custom measure
  * Creating a filtered measure from another measure
  * Creating a custom dimension using a Looker expression
  * Viewing and using custom fields
    * Viewing custom fields
    * Using custom fields
  * Duplicating a custom field
  * Editing a custom field
    * Editing a custom dimension
    * Editing a custom measure
  * Deleting a custom field


Most fields in the field picker are created by your Looker developers. By using custom fields, however, you can create new ad hoc custom dimensions and measures in an Explore. This page discusses how to create and use custom fields to enhance your data analysis.
To use custom fields, your Looker admin must grant the `create_custom_fields` permission to users or groups to allow access to the feature.
When you have access to custom fields, there are several types of custom fields you can create:
  * A custom measure based on an existing dimension
  * A filtered custom measure based on an existing measure
  * A custom dimension based on a Looker expression


## Custom fields are different from LookML-defined fields and table calculations
There are a few differences between custom fields and dimensions and measures that are defined in LookML, including:
  * There is no drilling capability for custom fields.
  * Custom fields only persist in an Explore's field picker for certain users.


There are a few differences between custom fields and table calculations:
  * Custom fields generate SQL that will run against the database, similar to a LookML field.
  * Custom fields are not dependent on data from the data table.


## Custom field types
You can create and customize several types of custom fields, depending on the base LookML field type or types. The following tables outline the types of custom fields that are available to create based on the LookML field type:


### Custom field types for dimensions
You can create several custom field types from dimensions in an Explore's field picker, depending on the base LookML field type or types. The following table outlines the types of custom fields that are supported for each type of dimension.
S = Works with the `string` data type
N = Works with the `number` data type and numeric measures
T = Works with the `tier` data type
ZC = Works with the `zipcode` data type
YN = Works with the `yesno` data type
DI = Works with the `distance` data type
DU = Works with the `duration` data type
TS = Works with most timestamp data types
ID = Works with most integer date data types
SD = Works with most string date data types
L = Works with the `location` data type
Each custom field type that you can create from a dimension falls into one of the following categories:
  * **Aggregate** — Aggregated fields are measures types that perform aggregations, such as sum and average. Aggregate measures can reference only dimensions, not other measures.
  * **Non-aggregate** — Non-aggregated fields are dimensions that can be grouped by in an Explore query.


Custom field name | Category | Description | LookML field type compatibility  
---|---|---|---  
### Count distinct
Count distinct  |  Aggregate  |  Creates a `count_distinct` measure that calculates the number of distinct values for a selected dimension.  |  S N T ZC YN DI DU TS ID SD L  
### Sum
Sum  |  Aggregate  |  Creates a `sum` measure that adds up the values of a selected dimension.  |  N DI DU ID  
### Average
Average  |  Aggregate  |  Creates an `average` measure that averages the values of a selected dimension.  |  N DI DU ID  
### Min
Min  |  Aggregate  |  Creates a `min` measure that finds the smallest value of a selected dimension.  |  N DI DU ID  
### Max
Max  |  Aggregate  |  Creates a `max` measure that finds the largest value of a selected dimension.  |  N DI DU ID  
### Median
Median  |  Aggregate  |  Creates a `median` measure that finds the midpoint value for the values of a selected dimension.  |  N DI DU ID  
### List of unique values
List of unique values  |  Aggregate  |  Creates a `list` measure that creates a list of the distinct values of a selected dimension.  |  S T ZC YN SD L  
### Bin
Bin  |  Non-aggregate  |  Creates bins, or tiers, that separate the values of a selected numeric dimension into a custom set of number ranges.  |  N DI DU ID  
### Group
Group  |  Non-aggregate  |  Creates a group that lets you bucket results of a selected dimension under custom labels.  |  S N T ZC YN DI DU TS ID SD L  
**Note about date and time data:** Looker interprets some timeframes and time-based types as different data types when you're creating custom fields, and this can affect the custom field types that are available for those timeframe and time-based fields. For example, Looker interprets the `hour_of_day` timeframe as a `number` data type and therefore has custom field options available to other `type: number` fields. For more specific information, see the **How custom fields interpret date and time data types** section on this page.  
### Custom field types for measures
You can create only one custom field type, a filtered measure, from measures in an Explore's field picker, depending on the base LookML measure type. The following table outlines the LookML fields to which measure types you can add a filter.
LI = Works with the `list` measure typeDT = Works with the `date` measure typeYN = Works with the `yesno` measure typeN = Works with numeric measure types
Custom field name | Description | LookML field type compatibility  
---|---|---  
### Filter measure
Filter measure  |  Adds a filter condition to a measure to limit the values included in the measure's aggregation.  |  LI DT YN N  
* For more specific information on the types of measures Looker interprets as numeric while it's using custom fields, see the **How custom fields interpret numeric measures** section on this page.  
### How custom fields interpret date and time data types
Looker interprets some timeframes and time-based types as different data types when you're creating custom fields, which affects the type of custom fields that you can create for a given date or time field. Custom fields categorize date and time fields in the following ways:


These categories are compatible with different types of custom fields, as indicated in the **Custom field types for dimensions** table.
#### Timestamp date data types
Custom fields treat the following LookML time data types as timestamp data types:


#### Integer date data types
Custom fields treat the following LookML date and time data types as integer date types:


#### String date data types
Custom fields treat the following LookML date and time data types as string data types:
  * `fiscal_quarter_of_year`


### How custom fields interpret numeric measures
Custom fields treat the following measure types as numeric types:


These measure types are compatible with the filtered measure custom field type, as indicated in the **Custom field types for measures** table.
## Creating a custom measure from a dimension
You can create a custom measure from a dimension in one of the following ways:
  * Using the dimension's three-dot **More** menu
  * Using the **Custom Fields** section of the field picker.


The second method lets you customize the custom field as you create it, such as renaming, adding an optional description, or selecting a different format other than the default.
### Using the dimension's three-dot **More** menu
In many cases, you can use this shortcut technique:
  1. Expand the field picker view that contains the dimension that you want to measure.
  2. Select the dimension's three-dot **More** menu.
  3. Select **Aggregate** to display options for creating a custom measure. The suggested functions vary based on the type of dimension you've chosen (such as number, string, or date). Select a function.


Expand the **Custom Fields** section in the field picker to see your new field.
As with other fields, you can select a custom field's name to add or remove it from a query. You can also hover over the field to reveal more options that are available for that field, including selecting its **Filter** icon to use it as a filter in a query. You can also edit the field as necessary.
### Using the Custom Fields section
If you want to define a format or a filter for your custom measure while creating it, start with the **Add** button on the **Custom Fields** section:
  1. Select **Add** in the **Custom Fields** section of the field picker.
  2. Select the type of field that you want to create. This example uses **Custom Measure**.
  3. Select a field to measure from the **Field to measure** drop-down, select the measure type from the **Measure type** drop-down options, and then specify a name in the **Name** field. The name appears in the field picker and in the data table.
  4. If you want to add a filter condition, select a field from the **Filter name** drop-down on the **Filters** tab. You can add or remove filter conditions using the **Add** and **Remove** plus and minus **Filter value** buttons. 
     * You can also select the arrow next to **Custom filter** to create a custom filter expression using any Looker functions and operators that can be used in custom filters. The Looker expression editor will suggest field names and display syntax help for any functions you use. Fields that are both currently used in an Explore and eligible to be used with the field type that you're creating are marked with a black circle. Refer to the Adding a custom filter to a custom measure section on this page for more details about adding filters to measures.
  5. On the **Field details** tab, you can specify a format in the **Format** section and add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  6. Select **Save**.


The field picker will display your new custom measure in the **Custom Fields** section.
As with other fields, you can select a custom field's name to display it in a query. You can also select its **Filter** button to use it as a filter in a query.
## Custom grouping
The **Group** custom field type lets you create ad hoc custom groups for dimensions without needing to use logical functions in Looker expressions or needing to develop `CASE WHEN` logic in `sql` parameters or `type: case` fields.
This can be helpful when you want to assign fixed labels or category names to values that match specific conditions, for example, by grouping specific states or countries into regions or order costs into categories.
To create a group, follow these steps:
  1. Expand the view that contains the dimension for which you want to create custom groups.
  2. You can perform the next step in two different ways:
     * Expand the view, select the dimension's three-dot **More** menu, and then select **Group** to open the **Group By** menu.
     * If the field is already selected in an Explore, you can select **Group** from the dimension's gear menu in the **Data** table to open the **Group By** menu, and follow the next steps to create custom groups.
  3. Specify a label for the first group of values in the **Group Name** field. This example illustrates how to create a group of states for the Pacific Northwest region of the United States using the **State** dimension, which is reflected by the **Group Name** 'Pacific Northwest'.
  4. Select the existing condition button in the **Group Value** section, which by default is **is any value** , to customize the conditions that you want to apply for the group.
  5. Select the condition, and enter or select one or more values. In this case, one of the conditions applied is **State is Oregon**. You can add or remove conditions using the **Add** and **Remove** plus and minus buttons. To save, click outside the filter condition, or use the escape key.
     * When available, value suggestions will appear in a drop-down list, which is indicated with a downward-facing arrow in the value input box, for users to select or search against. Suggestions are most commonly available for fields of `type: string`.
     * Looker automatically applies SQL conditions such as `AND` or `OR` logic when multiple conditions are created, based on the field types, conditions, and values that you specify.
     * If you're editing an existing custom group, consider changing the name to reflect the updated conditions.
  6. To add more groups for that dimension, hover over the existing group and select the **Add** plus sign button; to remove groups, select the **Remove** minus sign button. You can edit an existing group by selecting the group condition — **is Oregon or Idaho or Washington** in this case. Looker automatically applies SQL conditions such as `AND` or `OR` logic when multiple conditions are created, based on the field types, conditions, and values that you specify.
  7. Optionally, select the **Group remaining values** checkbox to create a category for grouping all other values that do not satisfy any group conditions. In this example, any state that is not Oregon, Idaho, or Washington will be grouped under a label named **Other**. **Other** is the default name, but you can customize it in the **Group Name** field, as desired.
     * If you're editing a custom group and want to remove grouping for all other values, uncheck the **Group remaining values** checkbox to remove that group.
  8. Specify a name in the **Field name** field. The name appears in the field picker and in the data table.
  9. Select **+ Add Description** to open the **Description** box and add an optional description of up to 255 characters to give other users more information about the custom group.
     * If you're editing a custom group and there is an existing description, the **Description** box will automatically appear.
  10. Select **Save** and then **Run** to rerun the Explore.


The new field will appear in the data table and display labels for all states: "Pacific Northwest" for the states Oregon, Washington, and Idaho, and "Other" for all other states.
You can use the new group to make new insights into your data. For example, compare how many orders have been placed by users in the Pacific Northwest region to users living in other regions in the United States.
The new field will appear in the **Custom Fields** section of the field picker.
As with other fields, you can select the field's name to add or remove it from a query. You can also hover over the field to reveal more options that are available for that field, including selecting its **Filter** icon to use it as a filter in a query. You can also edit the custom group as desired.
## Custom binning
The **Bin** custom field type lets you create ad hoc custom bins, or tiers, for numeric type dimensions and custom dimensions without needing to use logical functions in Looker expressions or needing to develop `type: tier` LookML fields.
This can be helpful when you want to quickly group values into specific integer ranges to adjust the granularity of your data.
**Bin** custom fields appear in the `classic` tier notation style.
To create a bin, follow these steps:
  1. Expand the field picker view that contains the dimension for which you want to create custom bins.
  2. You can perform the next step in two different ways:
     * Select the dimension's three-dot **More** menu, and then select **Bin** to open the **Bin** menu.
     * If the field is already selected in an Explore, you can select **Bin** from the dimension's gear menu in the **Data** table to open the **Bin** menu, and follow the next steps to create custom bins.
  3. As an optional starting point, select **Get field info** to learn more about the values for the dimension for which you're creating custom bins, including the dimension's minimum value, its maximum value, and its range of values. Having this information can be helpful in determining the way in which you specify value bins. 
  4. Select a bin type in the **Bin type** section.
     * Select **Equal-sized** to bin numeric values into equal integer ranges. For example, tiers of values ranging from 0-10, 10-20, and 20-30.
     * Select **Custom-sized** to create custom bin sizes of varying integer ranges. For example, tiers of values ranging from 0-15, 15-75, and 75-100.
  5. Customize the bin sizes and ranges.
     * If the selected **Bin type** is **Equal-sized** , enter the desired values in the **Bin size** , **Minimum value** , and **Maximum value** fields. The preceding example displays specifications of bins of 10, ranging from 0 to 100. Bins are automatically created for values in the data that fall outside the specified ranges.
     * If the selected **Bin type** is **Custom-sized** , specify the tier breakpoints in ascending order in the **Bin breakpoints** box, separated either by commas or new lines.
  6. Specify a name in the **Field name** field as desired. The name appears in the field picker and in the data table.
  7. Select **+ Add Description** to open the **Description** box to add an optional description of up to 255 characters to give other users more information about the custom bin.
     * If you're editing a custom bin that has an existing description, the **Description** box automatically appears.
  8. Select **Save** and then **Run** to rerun the Explore.


The new field will appear in the data table and displays tier levels for values depending on where they fit into specified bins.
You can use the new bin to make new insights into your data. For example, for a custom bin that is based on a **Cost** dimension, you can compare the number of orders that contain items priced in specific cost ranges.
The new field will appear in the **Custom Fields** section of the field picker.
As with other fields, you can select the field's name to add or remove it from a query. You can also hover over the field to reveal more options that are available for that field — for example, you can select the field's **Filter** icon to use it as a filter in a query. You can also edit the custom bin as desired.
## Adding a filter to a custom measure
Applying filters to custom measures allows a measure to limit the data, such as only including orders from certain regions. You can add a custom filter to a custom measure when you're creating or editing a custom measure. To add a filter to a custom measure:
  1. In the field picker, expand the **Custom Fields** section.
  2. Select **Add** and select **Custom Measure** to create a new custom measure, or select an existing custom measure's three-dot **More** menu to edit an existing custom measure.
  3. If you're editing a field, select **Edit**.
  4. Select the field that you want to filter by from the **Filter name** drop-down in the **Filters** section.
  5. Select the existing condition button, which by default **is any value** , under **Filter value** to customize the filter conditions that you want to apply.
  6. Select the condition, and enter or select a value. Select the **Add** plus sign button next to the value to add multiple conditions for the selected field. To save, click outside the filter condition, or use the escape key. 
     * When available, value suggestions will appear in a drop-down list, which is indicated with a downward-facing arrow in the value input box, for users to select or search against. Suggestions are most commonly available for dimensions of `type: string`.
     * If you're editing an existing custom measure, consider changing the custom measure's name to reflect the filter condition. The field name appears in the field picker and in the data table.
  7. To add more filters, select the **Add** plus sign button in the **Filter value** section; to remove filters select the **Remove** minus sign button. 
     * Looker automatically applies SQL conditions such as `AND` or `OR` logic when you create multiple filters, based on the field types, conditions, and values that you specify.
  8. Optionally, click the downward-facing arrow next to **Custom filter** at the bottom of the **Filters** tab to expand the **Expression** text box to add a custom filter instead of or in addition to a UI-based filter. Enter a Looker expression in the **Custom filter** box using any Looker functions and operators that can be used in custom filters. The Looker expression editor will suggest field names and display syntax help for any functions you use. Fields that are both currently used in an Explore and eligible to be used with the field type that you're creating are marked with a black circle.
  9. On the **Field details** tab you can specify a format in the **Format** section and add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  10. Select **Save**.


## Creating a filtered measure from another measure
To create a custom measure that copies an existing measure and adds a filter, follow these steps:
  1. Expand the view that contains the measure to which you want to add a custom filter. The measure _cannot_ be a custom measure or a `type: number` measure. To add a filter expression to an existing custom measure, you will need to edit the custom measure.
  2. Select that measure's three-dot **More** menu.
  3. Select **Create filtered measure**.
  4. Specify a name other than the default in the **Name** field as desired. The name appears in the field picker and in the data table.
  5. In the **Filters** section, select the field that you want to filter by from the **Filter name** drop-down.
  6. Select the existing condition button, which by default **is any value** , under **Filter value** to customize the filter conditions that you want to apply.
  7. Select the condition, and enter or select a value. Select the **Add** plus sign button next to the value to add multiple conditions for the selected field. To save, click outside the filter condition, or use the escape key. 
     * When available, value suggestions will appear in a drop-down list, which is indicated with a downward-facing arrow in the value input box, for users to select or search against. Suggestions are most commonly available for dimensions of `type: string`.
     * If you're editing an existing custom measure, consider changing the custom measure's name to reflect the filter condition.
  8. To add more filters, select the **Add** plus sign button in the **Filter value** section; to remove filters select the **Remove** minus sign button. 
     * Looker automatically applies SQL conditions such as `AND` or `OR` logic when you create multiple filters, based on the field types, conditions, and values that you specify.
  9. Optionally, click the arrow next to **Custom filter** at the bottom of the **Filters** tab to expand the **Expression** text box to add a custom filter instead of or in addition to a UI-based filter. Enter a Looker expression in the **Custom filter** box using any Looker functions and operators that can be used in custom filters. The Looker expression editor will suggest field names and display syntax help for any functions you use. Fields that are both currently used in an Explore and eligible to be used with the field type that you're creating are marked with a black circle.
  10. On the **Field details** tab you can specify a format in the **Format** section and add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  11. Select **Save**.


The field picker will display the new measure in the **Custom Fields** section.
As with other measures, you can select a custom measure's name to add or remove it from a query. You can also hover over the field to reveal more options that are available for that field, including selecting its **Filter** icon to use it as a filter in a query. You can also edit the field as necessary.
## Creating a custom dimension using a Looker expression
To create a custom dimension using a Looker expression and one or more other dimensions, follow these steps:
  1. Select **Add** in the **Custom Fields** section of the field picker.
  2. Choose **Custom Dimension**.
  3. In the **Expression** box, enter a Looker expression that calculates the value for your dimension, using any Looker functions and operators. The Looker expression editor will suggest field names and display syntax help for any functions you use. Fields that are currently used in an Explore and that are eligible to be used with the field that you're creating are marked with a black circle.
  4. Select a formatting option other than the default in the **Format** drop-down as desired.
  5. Specify the custom dimension's name in the **Name** field. The name appears in the field picker and in the data table.
  6. Select **+ Add Description** to add an optional description of up to 255 characters in the **Description** box to give other users more context or information about the custom dimension.
  7. Select **Save**.


The field picker will display your new custom dimension in the **Custom Fields** section.
As with other fields, you can select a custom dimension's name to add or remove it from a query. You can also hover over the field to reveal more options that are available for that field, including selecting its **Filter** icon to use it as a filter in a query. You can also edit the field as necessary.
## Viewing and using custom fields
The ability to see custom fields, and how you can interact with them, will be different depending on whether you're allowed to create them or not.
### Viewing custom fields
If you're allowed to create custom fields, then you can see and edit any that appear in the **Custom Fields** section of the field picker.
If you're not allowed to create custom fields, then the **Custom Fields** section is not displayed in the field picker.
However, if you include a custom field in an Explore, a Look, or a dashboard tile, any users with whom you then share that content can see the custom field regardless of whether they have the ability to create custom fields. If you're sharing this content by sharing an Explore's URL, the URL must include the `qid` parameter (such as `instance_name.looker.com/explore/ec/order_items?qid=lEPPueGN7cHkozOEZVDQbO`). Users who aren't allowed to create custom fields will see only the field's title, not its description, so it's important to name fields precisely if you'll be using them in queries shared with these users.
### Using custom fields
If you're allowed to create custom fields, then you can edit and use any that appear in the **Custom Fields** section of the field picker. You can interact with them almost exactly as you would with any other measures or dimensions, including filtering on them, adding them to visualizations, and (for custom dimensions) using them to pivot results. One exception is that you cannot use custom fields to create dashboard filters.
Only users who are allowed to create custom fields can _add_ them to queries in Explores, Looks, or dashboard tiles. However, if a user selects **Explore from here** on a shared Look or dashboard tile that includes a custom field, they can create a new query using that field whether or not they have the ability to create custom fields.
## Duplicating a custom field
If you're allowed to create custom fields, you can also duplicate existing custom fields. Duplicating and then editing custom fields can be helpful if you'd like to create multiple custom fields with only small differences (for example, 30-day, 60-day, or 90-day sums).
To duplicate a custom field, follow these steps:
  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to duplicate.
  3. Select **Duplicate**.
Alternatively, select **Duplicate** from the custom field's data table gear menu.


The duplicated field appears under the original, using the name of the original field plus the word "Copy" appended to the end.
Next, you can edit the duplicated field, as described in the next section.
## Editing a custom field
If you're allowed to create custom fields, you also can edit custom fields that you or other users have created.
### Editing a custom dimension
To edit a custom dimension, follow these steps:
  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to edit.
  3. Select **Edit**.
Alternatively, select **Edit** from the custom field's data table gear menu.
  4. Change the custom dimension definition as necessary in the **Expression** box.
  5. Select a new format from the **Format** drop-down if desired.
  6. Enter a new name in the **Name** field as desired. The name appears in the field picker and in the data table. If you have changed a custom field's definition, consider modifying the name to match.
  7. Select **+ Add Description** to add an optional description of up to 255 characters in the **Description** box to give other users more context or information about the custom dimension.
     * If there is an existing description, the **Description** box will automatically appear.
  8. Select **Save**.


### Editing a custom measure
To edit a custom measure, follow these steps:
  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to edit.
  3. Select **Edit**.
Alternatively, select **Edit** from the custom field's data table gear menu.
  4. To change the field that should be aggregated, select a new field from the **Field to measure** drop-down.
  5. To change the type of measure function, select a new measure type from the **Measure type** drop-down.
  6. Enter a new name in the **Name** field as desired. The name appears in the field picker and in the data table. If you change a field or measure type, typically you should also change the custom measure's name to match. For example, if you change the field **Sale Price** to **Cost** , you should also change the custom field name, in this case from **Sum of Sale Price** to **Sum of Cost**.
  7. Add, change, or remove a UI-based or custom filter on the **Filters** tab.
     * If there is an existing custom filter, the custom filter **Expression** box will automatically appear. If there is no existing custom filter, click the downward arrow next to **Custom filter** to add an optional custom filter in the **Expression** box instead of or in addition to a UI-based filter.
  8. On the **Field details** tab, add, change, or remove any formatting in the **Format** section or add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  9. Select **Save**.


## Deleting a custom field
If you're allowed to create custom fields, you can also delete custom fields you or other users have created. When you delete a custom field, it disappears from the Explore but not from any Looks or dashboard tiles that use that field. Additionally, anyone using a URL for an Explore that had the custom field will still have the field.
To delete a custom field from the field picker, follow these steps:
  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to delete.
  3. Select **Delete**.
Alternatively, select **Delete** from the custom field's data table gear menu.


You can also use the keyboard shortcuts Command-K (Mac) or Ctrl+K (Windows) to delete custom fields.
You can reinstate a custom field that you've deleted by clicking the back arrow on your browser.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


