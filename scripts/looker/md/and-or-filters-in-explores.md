# AND/OR Filters in Explores  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/and-or-filters-in-explores

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Creating AND/OR filters
    * Filter section options
    * AND/OR filters and required filters
    * AND/OR filters on dashboards




Was this helpful?
Send feedback 
#  AND/OR Filters in Explores
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Creating AND/OR filters
    * Filter section options
    * AND/OR filters and required filters
    * AND/OR filters on dashboards


Group and use AND/OR filter logic without the need to manually create filter expressions in an Explore.
## Creating AND/OR filters
AND/OR filters appear in the **Filters** section in an Explore. You can customize filters with AND/OR logic when you add or edit a filter on an Explore.
You can add a filter in several ways:
  * Select a field's **Filter by field** icon filter_list in the Explore field picker.
  * Select the **Filter** option from a field's data table gear menu.
  * Select the **Filter** button in the **Filters** section of the Explore.


To remove a filter, click the **Remove** `X` icon next to the filter.
### Filter section options
When you add more than one filter, the option to specify between `AND` and `OR` filter logic and switch between them appears to the left of the filter fields. A new filter group creates a separate set of filters with the option to specify between `AND` and `OR` filter logic between groups. The filters section contains the following options:
  1. **AND/OR** logic button — Select this option to switch filter logic. It will say **AND** or **OR** depending on the logic selected. Important: Depending on the filter conditions, the **AND** or **OR** buttons may be unactionable, indicating that the logic cannot be switched.
  2. **+ Filter** button — Select this option to add another filter in the same group.
  3. **+ New Group** button — Select this option to create a new filter group.
  4. **+ Custom expression** button — Select this option to create a custom expression manually using Lexp.


### Filter groups
Filters can be sorted into separate groups that are connected through AND/OR filter logic. For example, there can be multiple filters in groups A and B, and you can set the Explore to filter on `group A` OR `group B`. Groups allow you to filter Explores for multiple conditions that are not directly related.
For example, the following Explore filters contain two groups separated with OR logic:
  1. **Orders Status** is `pending` AND **Users State** is `California` OR
  2. **Products Category** is `active` AND **Inventory Items Cost** is <= `100`


The resulting explore will show order data of `pending` orders in `California` OR orders that contain `Active` category goods costing `less than or equal to 100`.
### AND/OR filters and required filters
Required filters (for example, a filter that is required with the `always_filter` parameter or `conditionally_filter` parameter) always appear in the first filter group, or `group A`.
To add multiple filter conditions to a field that is referenced by a required filter, click the **Add** button add next to each condition. `OR` filter logic will automatically be applied between each condition that is added to the required filter field.
You can add multiple filters to `group A` by clicking the **+ Filter** button, and you can add subsequent filter groups by clicking **+ New Group**.
### AND/OR filters on dashboards
AND/OR filters are created in the Explore Filters section and are translated into Looker expressions before the query is run. As a result, AND/OR filters behave differently from basic filters on dashboards.
If a query that uses both AND and OR filters is added to a dashboard, the filters will not appear in the dashboard filters section. The filters are still applied to that query, and can be edited in the corresponding query tile.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


