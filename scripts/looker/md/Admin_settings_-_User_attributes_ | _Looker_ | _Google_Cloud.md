# Admin settings - User attributes  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-users-user-attributes

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing user attributes
  * Creating user attributes
  * Assigning values to individual users
  * Assigning values to user groups
  * Where can user attributes be used?
    * Database connections
    * Custom actions in an action hub
    * Scheduled dashboards and Looks
    * Connecting to Git providers
    * Controlling access with access grants
    * Liquid variables
    * Google BigQuery data limits
    * Embedded dashboards
    * Accessing external API endpoints
  * Testing user attributes and access filters




Was this helpful?
Send feedback 
#  Admin settings - User attributes
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing user attributes
  * Creating user attributes
  * Assigning values to individual users
  * Assigning values to user groups
  * Where can user attributes be used?
    * Database connections
    * Custom actions in an action hub
    * Scheduled dashboards and Looks
    * Connecting to Git providers
    * Controlling access with access grants
    * Liquid variables
    * Google BigQuery data limits
    * Embedded dashboards
    * Accessing external API endpoints
  * Testing user attributes and access filters


User attributes provide a customized experience for each Looker user. A Looker admin defines a user attribute and then applies a user attribute value to a user group or to individual users.
Admins can also define user attributes for which the users themselves provide values, such as passwords or contact information. Various places throughout Looker can reference the user attributes to provide a custom experience for each user.
Looker automatically includes some user attributes, such as `email`, `first_name`, `landing_page`, `last_name`, `full_name`, `ID`, `timezone` (if configured), `locale`, and `number_format`.
## Viewing user attributes
To see your list of user attributes, go to the **User Attributes** page in the **Users** section of the **Admin** menu.
The table of user attributes gives the name, label, and type for each user attribute (see the following section for more information). In addition, the table provides a button for actions you can take for the user attribute. Some attributes show "System Default" instead of a button for actions, which means that Looker automatically creates those attributes for each user. The system default user attributes are reserved by Looker for internal use and cannot be edited.
## Creating user attributes
To define a user attribute, click the **Create User Attribute** button on the **User Attributes** page in the **Users** section of the **Admin** menu. Each user attribute has the following settings:
  * **Name** : The name of the user attribute, for use in text-based environments such as LookML (names can only contain lowercase letters, numbers, and underscores).
  * **Label** : The user-friendly version of the name. By default this will be the name of the attribute, with underscores replaced with spaces, and each word capitalized. However, the label can be modified as needed.
  * **Data Type** : This setting is used to check that valid values are assigned to users for this user attribute. The data type of the user attribute can be one of the following:
    * **String** : Select this option to create a user attribute that exactly matches one string value, such as a username. To use multiple string values or a Looker filter expression in the user attribute value, select the **String Filter (advanced)** option instead. If you want your user attribute to be treated as a literal string, be sure to include single quotes `'` in its syntax as in this example: `none '{{ _user_attributes['name_of_attribute'] }}'`
    * **Number** : Select this option to specify a single number, such as employee number. To use a range of numbers or a Looker filter expression, use the **Number Filter (advanced)** instead.
    * **Date/Time** : Select this option to specify a single date or time, such as user's birth date. To use a range of dates or a Looker filter expression, use the **Date/Time Filter (advanced)** instead.
    * **Relative URL** : Select this option to specify a relative URL, such as `/browse/boards/2`, that points to specific content like a board, a folder, or a Markdown file (such as a README or document file in a project) on your Looker instance. The `landing_page` user attribute, for example, has a data type of **Relative URL** and can be used to specify a specific home page for a user or group.
    * **String Filter (advanced)** : Select this option to allow multiple string values or a Looker filter expression in the user attribute. See the Filter expressions documentation page for a list of filter expressions you can use for strings.
    * **Number Filter (advanced)** : Select this option to allow a range of numeric values or a Looker filter expression in the user attribute. See the Filter expressions documentation page for a list of filter expressions you can use for numbers.
    * **Date/Time Filter (advanced)** : Select this option to allow a range of dates or a Looker filter expression in the user attribute. See the Filter expressions documentation page for a list of filter expressions you can use for date and time.
Use the **String Filter (advanced)** , **Number Filter (advanced)** , and **Date/Time Filter (advanced)** data types to enter values using Looker filter expressions, which will return a range of values for a user attribute.
  * **User Access** : You can choose the level of visibility and editing users have for a user attribute:
    * **None** : Won't appear on users' account pages.
    * **View** : Will appear on users' account pages, but won't be editable.
    * **Edit** : Will appear on users' account pages and can be set by the user.
  * **Hide Values** : Even if user attributes are visible to users, setting this option to **Yes** causes the user attribute values to be masked, which is useful for passwords or other sensitive information. Setting this value to **Yes** also masks the user attribute value in the user attribute drop-downs on the Connection Settings page. Once this value is set to **Yes** , it can never be changed back to **No**. When you set **Hide Values** to **Yes** , you must also specify a allowlist of domains that are allowed as a destination for the user attribute.
  * **Domain Allowlist** : When you hide the values for a new user attribute, you must also specify a domain allowlist that consists of the URLs to which the attribute can be delivered, such as host names for database connections and URLs for project Git HTTPS integrations. You can use the wildcard (*) to enable delivery to multiple pages on the same site. Once you have specified a domain allowlist, the user attribute can only be delivered to the destinations you have listed.
Once you have specified the domain allowlist for this user attribute, if the user attribute has been assigned any values — for a user, for a group, or by setting a default value — you cannot change the allowlist to make the URLs less restrictive. You can only make URLs more restrictive or remove URLs from the allowlist. For example, if **Domain Allowlist** includes an entry `my_domain/route/*`, you cannot later change it to `my_domain/*`. If you do need to make the allowlist less restrictive, delete all existing values assigned to the user attribute, including default values.
  * **Set a default value** : Select this checkbox to set a default value in case a value is not assigned to a user.


Once you define a user attribute, you can assign values to individual users or to user groups by clicking the **User Values** and **Group Values** tabs on the page.
## Assigning values to individual users
After defining a user attribute, you can assign a value for it to an individual user:
  1. Click the **User Values** tab on the **User Attributes** page in the **Users** section of the **Admin** menu.
  2. Choose the user to assign a value in the drop-down menu. This reveals a table of values that apply to that user.
  3. Click the **Set Value for User** button.
  4. Enter the new value in the **New Value** field.
  5. Click **Save**.


When a value is assigned to an individual user, that value _always_ takes precedence over any values that are assigned to that user's groups. The **User Values** tab shows when a custom value has been assigned to a user attribute that overrides a group value. The text "Overridden" will appear next to any overridden values, and these values won't be considered. The text "Current Value" will appear next to the active user attribute value.
To assign multiple values to a user attribute, use the data type **String Filter (advanced)** , and input multiple values separated by commas. Make sure there is no whitespace between the values. For example, you might enter the string: `Executive, Management, Contributors`.
To assign a Looker admin or other user all possible values, use a wildcard value in the user attribute:
  * To give an admin or another user access to all values of a string field, set the user attribute data type to **String Filter (advanced)** , and use a value of `%, NULL`.
  * To give an admin or another user access to all values of a number field, set the user attribute data type to **Number Filter (advanced)** , and use a value of `<0, >=0, NULL`.


## Assigning values to user groups
You can assign a value for a user attribute to a user group. From the **User Attributes** page of the **Admin** panel, select **Edit** to the right of the attribute you want to set. Then follow these steps:
  1. Click the **Group Values** tab.
  2. Click the **+ Add Group** button.
  3. Choose the group to assign a value in the drop-down menu.
  4. Enter the value for the group to have in the **Value** field.
  5. Click **Save**.


When a value is assigned to multiple groups you need to decide which group should take precedence, in case a user belongs to multiple groups. To do so, drag the groups into the order that should apply; each group takes precedence over the groups listed below it.
For example, you may have Executive Team and Management Team groups. Executives are also managers, so they are members of both groups. Dragging the Executive Team group to the top of the list will ensure that its members are assigned the **Executive** value instead of the **Manager** value.
If a user has set a custom value for a user attribute, the value the user set overrides any value given to a group that user belongs to.
## Where can user attributes be used?
User attributes have the following functions:
### Database connections
The host, port, database, username, password, and schema of a connection can each be given the value of a user attribute. (The connection host field won't accept a user attribute that has a **User Access** level set to **Editable**.)
These user attributes make the connection specific to the user who runs a query. User attributes can also be referenced in the **Additional JDBC parameters** field, which customizes the JDBC connection string. When a user runs a query using the connection, the user attribute values assigned to the user will be applied, allowing the connection to be customized based on the user.
#### Configuration
Any connection can be configured to use user attributes from the **Connections** page in the **Admin** section of Looker. (See the Admin settings - Connections documentation page for information on the **Connections** page.) To create a new connection, click **Add Connection**. To configure an existing connection, click **Edit** next to the connection.
If an input can be set to a user attribute, Looker displays a **User attribute** button next to the input .
Click the **User attribute** button to display a drop-down menu that lets you choose the desired user attribute. The list displays the user attribute name with the current user's user attribute value in parentheses.
To reference a user attribute in the **Additional JDBC parameters** field, you use the same Liquid templating syntax that is available in LookML. User attributes are made available through the `_user_attributes` Liquid variable. For example, to reference a user attribute named `my_jdbc_param_attribute`, use the following syntax:
```
my_jdbc_param={{ _user_attributes['name_of_attribute'] }}

```

#### Use case: Applying database-level permissions in Looker
If your database has different accounts with various access restrictions, you can use your database permissions in Looker. Parameterize the username and password of a connection so that each user connects with the appropriate credentials for their database access level. While this ensures that users don't see data to which they shouldn't have access, this won't affect which Explores, dimensions, and measures are shown to them in Looker.
For example, if a user is configured to connect to the database with an account that prevents them from seeing a `credit_card_number` column in the `user` table, any dimension using that database column still appears to them in Looker. They receive an error from the database if they attempt to run a query that includes that dimension.
#### Use case: Using one model for multiple identical databases
For example, if you have multiple databases with the exact same schema, such as when each customer's data is siloed into its own database for data security measures (such as HIPAA compliance). Or perhaps you want your LookML developers to run queries against a development copy of a production database.
If these databases live on the same database server, you don't need to set up separate connections and models. Instead, set the database of a connection to a user attribute and each user will be pointed to the database specified in their value for the `Database Name` user attribute.
### Data actions
Data actions can be configured to include certain user attributes with their JSON payload. Use this to send user-specific information along with the data, such as their credentials to perform an operation against a particular service.
#### Configuration
To include a user attribute in a data action, add a `user_attribute_param` block to the `action` definition. Each block takes two parameters:
  * `user_attribute`: The name of the user attribute
  * `name`: The name to use in the JSON payload


This example uses two user attributes — `salesforce_username` and `salesforce_password`— to hold each user's Salesforce credentials in Looker. When a user performs the Update in Salesforce data action, Looker sends their Salesforce credentials with the JSON payload, which the receiving server can use in authenticating to Salesforce.
```
dimension: stage_name {
  type: string
  sql: ${TABLE}.stage_name;;
  action: {
    label: "Update in Salesforce"
    url: "https://example.com/my_salesforce_url"
    user_attribute_param: {
      user_attribute: salesforce_username
      name: "username"
    }
    user_attribute_param: {
      user_attribute: salesforce_password
      name: "password"
    }
    form_param: {
      name: "new_stage_name"
      type: string
      required: yes
    }
  }
}

```

### Custom actions in an action hub
You can configure a custom action to include user attributes that restrict users from sending or scheduling Looker content to that action destination if they don't have a value defined for that user attribute.
#### Configuration
The `params` parameter in a custom action represents the form fields that a Looker admin must configure on the action's enablement page from the **Actions** list in the **Admin** panel. In the `params` parameter of your action file, include:
```
  params = [{
    description: "A description of the param.",
    label: "A label for the param.",
    name: "action_param_name",
    user_attribute_name: "user_attribute_name",
    required: true,
    sensitive: true,
  }]


```

where `user_attribute_name` is the user attribute defined in the **Name** field on the **User Attributes** page in the **Users** section of the **Admin** panel, `required: true` means that a user must have a non-null and valid value defined for that user attribute to see the action when delivering data, and `sensitive: true` means that user attribute value is encrypted and never displayed in the Looker UI once entered. You can specify multiple user attribute subparameters.
A Looker admin must configure the action's form fields with the user attribute:
  1. Click the **Enable** or the **Settings** button next to the action on the **Actions** page of the **Admin** panel.
  2. Click the user attribute icon for the appropriate field, and select the desired user attribute.


See the Adding user attributes to custom actions section of the Sharing data through an action hub documentation page.
### Filters
Filters on Explores, Looks, and dashboards can be set to a user attribute to customize the query based on the user who is running it.
For example, you could create a user attribute called `salesforce_username` and configure each Looker user so that their value for it is their Salesforce username. Then you could set a filter on a dashboard to the `salesforce_username` user attribute and each user would see that dashboard filtered for their particular Salesforce username.
#### Configuration
In the **FILTERS** section of an Explore, Look, or dashboard:
  1. Select the **matches a user attribute** option on the desired filter.
The select box to the right automatically updates with a list of user attributes that have the same type as the filter's field, such as number, string (text), date, and so forth. Looker displays your value for each user attribute in parentheses.
  2. Select the desired user attribute.


#### Advanced filter syntax
If you'd like to do something more complex than a simple equality check for the filter, select **matches (advanced)** and reference the user attribute using a Liquid variable:
```
{{ _user_attributes['name_of_attribute'] }}

```

For example, suppose you need to apply an `sf_` prefix to the value of the `salesforce_username` user attribute because that is how the values are stored in your database. To add the prefix to the user attribute value, use the `_user_attributes` Liquid variable syntax:
```

sf_{{_user_attributes['salesforce_username']}}


```

You can use the same pattern to insert user attributes into LookML dashboard filters and dashboard element filters.
### Scheduled dashboards and Looks
Dashboard and Look filters can be set on a per-schedule basis, including the option to use a user attribute. This lets you customize the data delivery results for each email recipient. You can customize deliveries for content that are sent as one-time deliveries and recurring deliveries.
For example, you could create a user attribute called `salesforce_username` and set the value to each user's Salesforce username. Set a filter on a dashboard or Look schedule to the `salesforce_username` user attribute so each recipient gets that dashboard filtered by their Salesforce username.
#### Prerequisites
Only Looker users have user attribute values set, so every recipient of the data delivery must have a Looker account. User attributes are applied by running the dashboard or Look once for each recipient.
#### Configuration
Open the Scheduler for the Look or dashboard:
  1. In the **Filters** section, select the **matches a user attribute** option on the desired filter.
The select box to the right automatically updates with a list of user attributes that are the same type as the filter. Your own value for each user attribute shows in parentheses.
  2. Select the desired user attribute.
  3. Check the **run schedule as recipient** checkbox next to the **Email options** field.


### Access filters
You can limit the data a user can access with access filters, which provide row-level security. Although you can use the `access_grant` parameter, access filters are more easily implemented and maintained with user attributes.
Access filters provide a secure way to apply user-specific data restrictions. Defining one or more access filters for a LookML Explore enforces that the data returned from an Explore is filtered based on the user running the query. Thus, access filters provide an extra layer of restriction, ensuring the user can only see specific subsets of the data from a database connection.
#### Configuration
  1. Create a user attribute: 
     * Configure with **User Access** set to **None** (recommended) or **View**. (A user attribute configured to be editable by users cannot be used for an access filter.)
     * Assign user attribute values to groups or individual users.
  2. In the LookML definition for the Explore where you want the access filter, add an `access_filter` block with the following parameters: 
     * `field`: The name of the LookML field on which to filter
     * `user_attribute`: The name of the user attribute that stores the value you want to use to filter the data
  3. Run a query against that Explore.
  4. Check the `WHERE` clause of the query's SQL to verify that the data is filtered according to your value for the user attribute.


This LookML ensures queries about orders are filtered by brand, with the particular brand being based on the user's assigned value for a user attribute named `company`:
```
explore: orders {
  view_name: orders
  access_filter: {
    field: products.brand_name
    user_attribute: company
  }
  join: products {
    foreign_key: orders.product_id
  }
}

```

### Connecting to Git providers
For LookML projects, you can configure Git authentication over HTTPS. Projects that use HTTPS Git authentication have the option of leveraging user attributes to log in to individual developer's Git accounts when performing Git operations for the developer.
User attributes for Git account passwords must be hidden. When creating the password attribute, select **Yes** under the **Hide Values** option and enter the Git provider URL in the **Domain Allowlist** field.
### Controlling access with access grants
You can create access grants that limit access of a LookML Explore, join, view, or field using user attribute values, the `access_grant` parameter, and the `required_access_grants` parameter.
Access grants work like this:
  1. You define an access grant using the `access_grant` parameter. As part of the definition, you associate the access grant with a user attribute. You also specify which user attribute values provide access to the access grant.
  2. Next, you use the `required_access_grants` parameter at the Explore, join, view, or field level to restrict that structure to only users who have access to every access grant listed.


For example, you could use an access grant to limit access to the `salary` dimension to only those users who have the value `payroll` in their `department` user attribute.
For more information about how to define access grants, see the `access_grant` parameter documentation page.
### Liquid variables
LookML enables the use of several different Liquid variables, which can be useful for more complex types of customized output. A user's attribute values can now be included in Liquid. The Liquid expression must use syntax that is appropriate to your database dialect.
You can see examples in the Connection section of this documentation page, and in the Using user attributes for dynamic schema and table name injection Best Practices page.
### Google BigQuery data limits
If you use Google BigQuery as your database, Google charges you for each query based on the size of the query. To help prevent users from accidentally running too expensive a query, you can apply a user attribute in the **Max Billing Gigabytes** setting in your BigQuery connection. The values that you supply in the user attribute should be the number of gigabytes that a user is allowed to pull in a single query.
### Embedded dashboards
You can limit the data that is displayed in embedded Looks and dashboards by basing filter values on user attribute values. For more information, see the Creating a proof of concept embedded dashboard (Powered by Looker)  Community post.
### Localization
The user attributes `locale` and `number_format` can set the appearance of data, visualizations, and parts of the Looker user interface for specific users or user groups. See the Localizing Looker documentation page for more information.
### Accessing external API endpoints
User attributes can be used by the Looker extension framework to access external API endpoints using a server proxy. For an example, see the Extension framework React and JavaScript code examples documentation page.
## Testing user attributes and access filters
You can test the effects of your user attributes with Looker's sudo function. Admins (or users with both the `see_users` and `sudo` permissions) can sudo as another user to see their experience of Looker.
When you are in Development Mode, your changes are not visible to other users until you deploy your changes to production. If you haven't deployed your changes for other users to see, you won't see your changes when you sudo as a different user.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


