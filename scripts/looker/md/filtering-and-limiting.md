# Filtering and limiting data  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/filtering-and-limiting

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Filtering data
    * Advanced matches filters
    * Filtering dimensions: restricts raw data before calculations
    * Filtering measures: restricts results after calculating measures
  * Limiting data




Was this helpful?
Send feedback 
#  Filtering and limiting data
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Filtering data
    * Advanced matches filters
    * Filtering dimensions: restricts raw data before calculations
    * Filtering measures: restricts results after calculating measures
  * Limiting data


This page explains how a user can filter and limit data in a Looker Explore. For example, a user can filter the Explore's query results to the last three months or for a certain customer. Users can also limit the number of rows that are displayed in an Explore or the number of pivot columns that are displayed in an Explore.
## Filtering data
Filters let you restrict the data that you are viewing to items of interest. Any field in your Looker instance can become a filter.
You also don't necessarily need to add a dimension or measure to your results to filter on it. For example, you can create a query that filters the **Order Date** to the last 90 days, even though your results only show **Customer** and **Number of Orders**.
You can use any combination of these filter types in your query:
  * **Basic Filters** are the most commonly used; Looker provides appropriate drop-down lists, calendar widgets, and text fields.
  * **Advanced Matches** allow for a more advanced condition for a field, such as intricate text searches, or a date range that starts in the past and extends for a certain number of days.
  * **Custom Filters** let you specify detailed business logic, combine `AND` and `OR` logic, or use Looker functions.


### Basic filters
There are a couple of ways to add a basic filter:
  * In the Field Picker, select **Filter by field** to the right of the field name.
  * In the **Results** tab of the **Data** panel, select the gear in the field header, and then select **Filter**.


Filters appear in the **Filters** section. To remove a filter, select **Remove** to the right of the filter clause.
#### Standard filters
Standard filter options vary by filter type. For example, a time dimension lets you select a time range; a numeric dimension provides you with options such as **is** or **is >**.
For text dimensions, Looker displays a list of existing data values for the field. As you type, Looker narrows the list to values that include that text.
To filter on a large set of values, paste a list of values into the filter field. The maximum number of values that you can paste may be limited by your browser or other elements in your network, and may be as small as 2,000.
To enter a special character in a standard filter, first add a leading backslash. For example, to filter on `Santa Cruz, CA`, you would enter `Santa Cruz \, CA`.
To add another option to the filter, select **+ Filter**. This action opens the **Add Filter** dialog, which lets you choose a field on which to create the new filter option. To add a new filter group, select **+ New group** in the **Filters** section.
When you add more than one filter, the option to specify between `AND` and `OR` filter logic and switch between them appears to the left of the filter fields. A new filter group creates a separate set of filters with the option to specify between `AND` and `OR` filter logic between groups.
#### Filters with user attributes
Looker admins can configure user attributes that specify user-specific values. For example, an admin can define a user attribute for a sales region and assign the appropriate values to individual users or groups of users.
User attributes let you automatically customize a Look or dashboard for each user who views it. The **matches a user attribute** condition provides this user-specific flexibility. For example, you can filter a sales region dimension in a Look to equal a sales region user attribute. The Look will filter for the user's specific sales region and automatically adjust to show each user the data for their own sales region.
### Advanced matches filters
To add an advanced matches filter, select the **matches (advanced)** option from the filter's condition drop-down menu.
In the text field, enter your filter expression. To view all available filter expressions, see the Looker filter expressions documentation page.
To enter a special character in an advanced matches filter, first add a leading carat (`^`). For example, to filter on `Santa Cruz, CA`, you would enter `Santa Cruz ^, CA`.
Your Looker admin can configure user-specific values, called **user attributes** , that let you automatically customize a Look for each user. To reference a user attribute in an advanced matches filter, use the following syntax:
```
{{ _user_attributes['USER_ATTRIBUTE_NAME'] }}

```

### Custom filters
Custom filters let you write the fields, constants, functions, and operators to customize your filtering. Looker lets you build an expression that evaluates as `yes` or `no`. When you run the query, Looker only returns rows for which that condition is `yes`.
#### Adding a custom filter
To add a custom filter from the **Filters** section, follow these steps:
  1. Select **+ Custom expression**.
  2. Enter a dimension or function to have Looker display a list of functions, operators, and field names to use in your expression. Select a term in the drop-down to add it to your expression. When finished, your custom filter expression must evaluate to `yes` or `no`.
  3. Select **Save**.
  4. Select **Run** (or use the keyboard shortcut Command-Enter for Mac or Ctrl+Enter for Windows) to run your query with your custom filter applied.


The **Creating Looker expressions** documentation page explains how to create Looker expressions and how the editor can assist you.
Looker expressions can use as many fields, functions, and operators as your business logic requires. The more complex your condition, the more work your database must do to evaluate it; complex conditions may lengthen query times.
#### Removing a custom filter
To remove a custom filter expression from the query, select **Remove** from the **Custom Filter** header. If you leave the browser page open, Looker remembers what you typed and your expression reappears if you select **Custom Filter** again.
### Filtering dimensions: restricts raw data before calculations
When you filter on a dimension, you restrict the raw data _before_ any calculations are made.
For example, say you've created an Explore to view how many orders were placed each day. The Explore includes the **Orders Created Date** and **Orders Count** fields. Then, you add a filter on an **Order Status** dimension with the condition `is COMPLETED`.
Looker removes all orders that have _not_ been completed from the data. The measure still counts the remaining orders for each day, but the measure values are lower.
### Filtering measures: restricts results after calculating measures
When you filter on a measure, you restrict the results _after_ the measure has been calculated.
For example, say you've created an Explore to view how many orders were placed each day. The Explore includes the **Orders Created Date** and **Orders Count** fields. Then, you add a filter on the **Order Count** measure with the condition `is < 20`.
Looker first counts all orders for each day. Then, the filter is applied. The filter limits the dataset to only the days that had fewer than 20 orders. You may need to turn off Looker's **dimension fill** option if Looker is returning null values.
## Limiting data
Looker supports up to 5,000 rows and 200 columns for pivoted or unpivoted query results. For browser performance, 50 or fewer columns is recommended. Looker sets a default column limit of 50 columns for pivoted query results.
To see a subset of your complete query results, you can set a row limit, a column limit, or both.
### Row limits
You can set a row limit of up to 5,000 rows. Looker warns you if you might be hiding data by setting a row limit that is too low. The sort order is important: Looker _first_ applies the sort and _then_ applies the limit. For example, in a query that contains the fields **Orders Created Month** and **Orders Count** , sort by **Orders Count** and then specify a row limit of **5** to see the months that had the top five number of orders.
For more information about row limits in other parts of Looker, see the What are all the row limits in Looker? Best Practices page.
### Column limits
If you added a pivot to your query results, you can apply a column limit of up to 200. Looker warns you if you might be hiding data by setting a column limit that is too low. The sort order of your pivot is important: Looker _first_ applies the sort and _then_ applies the limit. For example, in a query that contains the field **Orders Count** and that is pivoted by the **Orders Created Month** field, sort by **Orders Created Month** to see the five most recent months when orders were created.
Dimensions, dimension table calculations, row total columns, and measure table calculations outside of pivots are not counted toward the column limit. Pivoted groups count as one column toward the column limit.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


