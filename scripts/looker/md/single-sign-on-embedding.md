# Signed embedding  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/single-sign-on-embedding

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Signed embedding
Stay organized with collections  Save and categorize content based on your preferences. 
Signed embedding is a way to present private embedded Looks, visualizations, Explores, dashboards, or LookML dashboards to your users without requiring them to have a separate Looker login. Instead, users will be authenticated through your own application.
Signed embedding works by creating a special Looker URL that you will use in an iframe. The URL contains the information you want to share, the ID of the user in your system, and the permissions that you want the user to have. You'll then sign the URL with a secret key provided by Looker.
For public embedding, see the Public embedding with `iframe` tags section of the **Public sharing, importing, and embedding of Looks** documentation page.
Before you can use signed embedding on your Looker instance, a Looker admin must enable signed embedding in the Looker Admin panel and create an embed secret key. For instructions, see the **Getting started with embedding — enabling signed embedding** documentation page.
## Proper hosting for signed embedding
Some browsers — for example, Safari, or browsers with extensions installed that block ads or tracking cookies — default to a cookie policy that blocks third-party cookies. When the **Cookieless Embed** feature is enabled, browsers that block third-party cookies can authenticate users in the embedded iframe across different domains. Cookieless embed authentication requires server-side configuration. See the Cookieless embedding documentation page for setup examples.
If the **Cookieless Embed** feature is not enabled, Looker uses cookies for user authentication. In this case, attempting to authenticate the embedded iframe across domains is not possible in browsers that block third-party cookies (unless the user modifies their browser's cookie privacy settings). For example, if you want to embed information on `https://mycompany.com`, you need to make sure that Looker shares the same domain, such as `https://analytics.mycompany.com`. In this case, if Looker is hosting your instance, contact Looker Support to set up the necessary DNS configuration to enable custom domain use. This will allow Looker to share the same domain as the embed application and to utilize first party cookies, which are accepted by default in all browsers.
If you have a customer-hosted Looker instance, make sure that the application that will use signed embedding uses the same domain as your Looker instance.
## Controlling client visibility with a closed system
It is common in a signed embed configuration for Looker users to present data to their own customers while having clients from different companies or groups who shouldn't know about one another. In this scenario, to safeguard your customers' private information, we strongly recommend that you configure Looker as a closed system, also called a _multitenant installation_. In a closed system, content is siloed to prevent users from different groups from knowing about each other. For this reason, we recommend that you enable the **Closed System** option before you grant any external users access to your instance.
For more information, see the Designing and configuring a system of access levels and the Security best practices for embedded analytics documentation pages.
## Generating the signed embed URL
There are multiple ways to generate the signed embed URL. You can use one of these methods:
  * You can generate a signed embed URL using the **Get embed URL** option on the three-dot dashboard menu of a dashboard, or on the Explore actions gear menu of a Look or Explore.
  * Use the Looker API Create Signed Embed Url endpoint, as described later in this document.
  * Use the Looker Embed SDK.
  * Code the signed embed URL. Building the proper URL will require you to write code so that you can properly encode the URL with your secret key and generate other security-related items. You can find several sample scripts in the Looker Embed examples GitHub repository. The following sections explain the information that you'll need to supply to those scripts, as well as how to build a signed embed URL without using a script.


## Manually coding the signed embed URL
To code the signed embed URL, first collect the necessary Looker information, and then create the signed embed URL.
### Collecting the necessary Looker information
As a starting point for building your URL, you'll first want to determine all the information that will need to be included. You will need:
#### Embed URL
Retrieve the URL of the Look, Explore, query visualization, or dashboard that you want to embed. Then remove the domain and place `/embed` before the path, as follows:
Item | Normal URL Pattern | Embed URL  
---|---|---  
Look | `https://instance_name.looker.com/looks/4` | `/embed/looks/4`  
Explore | `https://instance_name.looker.com/explore/my_model/my_explore` | `/embed/explore/my_model/my_explore`  
Query visualization |  `https://instance_name.looker.com/explore/my_model/my_explore?qid=1234567890abcdefghij12``qid=` parameter in the Explore URL comprise the `Query.client_id`. The `Query.client_id` value is a unique string that represents the query and the visualization settings.`Query.client_id` value, and copy the `Query.client_id` into your embed URL.Explore UI to build a query with a supported visualization and copy the `Query.client_id` value from the `qid=` parameter, or you can retrieve the `Query.client_id` with the Looker API, using the `Get Query` method, for example. | `/embed/query-visualization/Query.client_id`  
User-defined dashboard |  `https://instance_name.looker.com/dashboards/1`hiding filter values, the `hide_filter` parameter in the dashboard URL.  
User-defined legacy dashboard | `https://instance_name.looker.com/dashboards-legacy/1` | `/embed/dashboards-legacy/1`  
LookML dashboard | `https://instance_name.looker.com/dashboards/my_model::my_dashboard` | `/embed/dashboards/my_model::my_dashboard`  
Legacy LookML dashboard | `https://instance_name.looker.com/dashboards-legacy/my_model::my_dashboard` | `/embed/dashboards-legacy/my_model::my_dashboard`  
> Embedded content always reflects the production version of the content. Any changes made while in Development Mode that affect content and that have not been deployed to production will not appear in an embed.
#### Permissions
A permission set defines what a user or group can do. Permissions can be applied in one of two ways:
  * **Model Specific:** This type of permission is applied only to the model sets that are part of the same role.
  * **Instance Wide:** This type of permission applies to the Looker instance as a whole. Embed users with instance-wide permissions can perform certain functions across the entire Looker instance, but cannot access content based on models not included in their role's model set.


Determine the permissions that you'll want the user to have. The following list shows all available permissions for signed embedding. Permissions that are not on the following list are not supported for signed embedding:
Permission | Depends On | Type | Definition  
---|---|---|---  
`access_data` | None | Model Specific | Allows user to access data (required for viewing Looks, dashboards, or Explores)  
`see_lookml_dashboards` | `access_data` | Model Specific |  Lets user see LookML dashboards  
`see_looks` | `access_data` | Model Specific |  Lets user see Looks  
`see_user_dashboards` | `see_looks` | Model Specific |  Lets user see user-defined dashboards and to browse folders from an embed  
`explore` | `see_looks` | Model Specific | Lets user see Explore pages  
`create_table_calculations` | `explore` | Instance Wide |  Needed to create table calculations in an Explore  
`create_custom_fields` | `explore` | Instance Wide |  Needed to create custom fields in an Explore  
`can_create_forecast` | `explore` | Instance Wide |  Allows users to create or edit forecasts in visualizations.  
`save_content` | `see_looks` | Instance Wide |  Lets user make and save changes to Looks and dashboards  
`send_outgoing_webhook` | `see_looks` | Model Specific | Lets user schedule Looker content deliveries to an arbitrary webhook  
`send_to_s3` | `see_looks` | Model Specific | Lets user schedule Looker content deliveries to an Amazon S3 bucket  
`send_to_sftp` | `see_looks` | Model Specific | Lets user schedule Looker content deliveries to an SFTP server  
`schedule_look_emails` | `see_looks` | Model Specific |  Lets user schedule Looker content deliveries to their own email (if set with a user attribute named "email") or to an email address that is within the limitations set by the email domain allowlist. Lets user with `create_alerts` permissions send alert notifications to an email address that is within the limitations set by the email domain allowlist.  
`schedule_external_look_emails` | `schedule_look_emails` | Model Specific |  Lets user schedule Looker content deliveries to any email domain. Lets user with `create_alerts` permissions send alert notifications to any email domain.  
`send_to_integration` | `see_looks` | Model Specific | Lets user deliver Looker content to the third-party services integrated with Looker through the Looker Action Hub. This permission is not related to data actions.  
`create_alerts` | `see_looks` | Instance Wide |  Lets user create alerts on dashboard tiles to receive notifications when specified conditions are met or exceeded. Users can edit, duplicate, and delete their own alerts and other users' **Public** alerts. If the user's Slack workspace is not connected to the Looker instance, the user will not be able to create alerts that send notifications to Slack.  
`download_with_limit` | `see_looks` | Instance Wide | Lets user download a query's results with a limit applied  
`download_without_limit` | `see_looks` | Instance Wide | Lets user download a query's results with no limit applied  
`see_sql` | `see_looks` | Model Specific | Lets user see the SQL for queries and any SQL errors resulting from running queries  
`clear_cache_refresh` | `access_data` | Model Specific | Users can clear cache and refresh embedded dashboards, legacy dashboards, dashboard tiles, Looks, and Explores.  
`see_drill_overlay` | `access_data` | Model Specific | Lets user drill without needing to go to the full Explore page.  
`manage_spaces` | None | Instance Wide | Enables the content browser so that users can create, copy, move, and delete folders. Users will also need the **Manage Access, Edit** content access permission for the folder, or, in the case of creating a new folder, for the parent folder.  
`embed_browse_spaces` | None | Instance Wide | Enables the content browser so that a user can browse folders from an embed. Any embed user who is granted `embed_browse_spaces` permission is given access to a personal embed folder and to your organization's **Shared** folder, if there is one. `embed_browse_spaces` permission is recommended for users who have the `save_content` permission, so that the user can browse folders when selecting where to save content. `see_looks`, `see_user_dashboards`, and `see_lookml_dashboards` permissions.  
`embed_save_shared_space` | None | Instance Wide |  Lets user who also has the `save_content` permission navigate to the organization's **Shared** folder, if there is one, from within the **Save** dialog. Users who have the `save_content` permission but not the `embed_save_shared_space` permission will only have the option to save content to their personal embed folder.`embed_save_shared_space` permission does not override content access permissions. For example, to enable a user to be able to save to the **Shared** folder, they still need **Manage Access, Edit** access to the **Shared** folder. In addition, the lack of the `embed_save_shared_space` permission doesn't prevent a user who has the `save_content` permission and **Manage Access, Edit** access to the **Shared** folder from saving content there if they have an alternate way to navigate to the **Shared** folder, such as by using the **Explore from here** option from an embedded dashboard.  
#### Model access
Determine which LookML models the user should have access to. This will simply be a list of model names.
#### User attributes
Determine which user attributes the user should have, if any. You'll need the name of the user attribute from Looker, as well as the value that the user should have for that attribute.
#### Groups
Determine which groups the user should belong to, if any. You'll need the group IDs as opposed to the group names. Adding a signed embed user to a Looker group lets you manage that user's access to Looker folders. Signed embed users will have access to any folders that are shared with members of their Looker groups.
You can also use the `external_group_id` parameter to create a group that is external to the regular Looker groups. In that case, signed embed users with the same `external_group_id` will have access to a shared folder, named "Group," that is unique to the external group.
#### Embedded roles
The `permissions` and `models` parameters create a role for the embed user. This role appears as an "Embedded Role" in the **Users** page in Looker's **Admin** section. If the `permissions`, `models`, and `group_ids` parameters are all specified in the embed URL, then the embedded role is _additive_ to any roles already assigned to the groups listed in the `group_ids` parameter. This is the same as standard roles in that all roles in Looker are additive.
For example, say you have an existing group in Looker with the group ID `1`, and that group already has the `explore` permission for a model named `model_one`, and you create an embed URL with the following parameters:
  * `group_ids` = `["1"]`
  * `permissions` = `["access_data","see_looks"]`
  * `models` = `["model_two"]`


In that case, the embed user will inherit the ability to view and explore the data on `model_one`, and the embed role created with the preceding parameters will also grant the ability to view the data on `model_two`.
### Creating the embed URL
A signed embed URL has the following format:
https://HOST/login/embed/EMBED URL?PARAMETERS&signature=SIGNATURE
#### Host
The host is the location where your Looker instance is being hosted. For example, `analytics.mycompany.com`. Be sure to include the port number if you haven't enabled port forwarding, such as `analytics.mycompany.com:9999`.
#### Embed URL
The embed URL was determined previously. It will have a format such as:
  * `/embed/looks/4`
  * `/embed/explore/my_model/my_explore`
  * `/embed/query-visualization/Query.client_id`
  * `/embed/dashboards/1` or `/embed/dashboards-legacy/1`
  * `/embed/dashboards/my_model::my_dashboard` or `/embed/dashboards-legacy/my_model::my_dashboard`


This does mean that the pattern `/embed//embed/` will show up in your final URL; this is correct.
If you are using embedded JavaScript events be sure to add an `embed_domain` (the domain where the iframe is being used) to the end of the embed URL, like this:
`/embed/looks/4`
`/embed/looks/4?embed_domain=https://mywebsite.com`
`embed_domain` is added after the embed URL, and before any parameters. So if you had existing parameters, such as `nonce=626`, the addition of the `embed_domain` would look like:
`/embed/looks/4?nonce=626`
`/embed/looks/4?embed_domain=https://mywebsite.com?nonce=626`
If you are using the Embed SDK be sure to add the `embed_domain` and also include `sdk=2` to the end of the embed URL, like this:
`/embed/looks/4`
`/embed/looks/4?embed_domain=https://mywebsite.com&sdk=2`
The `sdk=2` parameter lets Looker identify that the SDK is present and can take advantage of additional features provided by the SDK. The SDK cannot add this parameter itself because it is part of the signed URL.
#### Parameters
The following URL parameters are used to specify the necessary information for the signed embed:
Parameter | Default Value | Description | Data Type | Example  
---|---|---|---|---  
`nonce` | Value Required | Any random string you like, but it cannot be repeated within an hour and must be less than 255 characters. | JSON String | `"22b1ee700ef3dc2f500fb7"`  
`time` | Value Required | The current time as a UNIX timestamp. | Integer | `1407876784`  
`session_length` | Value Required | The number of seconds that the user should remain logged in to Looker, between 0 and 2,592,000 seconds (30 days). | Integer | `86400`  
`external_user_id` | Value Required |  An identifier for each user in the application that is embedding Looker. Looker uses `external_user_id` to differentiate signed embed users, so each user must have a unique ID assigned to them.`external_user_id` for a user with any string you like, as long as it's unique to that user. Each ID is associated with a set of permissions, user attributes, and models. A single browser can support only one `external_user_id`, or user session, at a time. No changes can be made to a user's permissions or user attributes mid-session.`external_user_id` across different embed sessions for different interactive users, and ensure that you are not using the same `external_user_id` for a single user who has different permissions, user attribute values, or model access.`external_user_id` for multiple users or for the same user with multiple permissions, user attributes, or model sets, can cause data to be visible to users who otherwise wouldn't have access to it. | JSON string | `"user-4"`  
`permissions` | Value Required | The list of permissions the user should have.Permissions section on this page for the list of allowed permissions. | Array of strings |  `[``"access_data",``"see_looks"``]`  
`models` | Value Required |  The list of model names the user should have access to. | Array of strings |  `[``"model_one",``"model_two"``]`  
`group_ids` | [] | The list of Looker groups the user should be a member of, if any. Use group IDs instead of group names. | Array of strings | `["4", "3"]`  
`external_group_id` | "" | A unique identifier for the group that the user belongs to in the application that is embedding Looker.shared Looker folder called "Group". The `external_group_id` parameter is the only available method for creating external groups of embed users. There is no way to configure external embed user groups from within the Looker UI.`external_group_id` shouldn't exceed 81 characters. A corresponding folder is created for the group, and folder names have a limit of 100 characters. The folder name is prefixed with "Embed Shared Group ", so the `external_group_id` is restricted to 81 characters to keep it to the 100 or fewer character limit. | JSON string | `"Accounting"`  
`user_attributes` | {} |  The list of user attributes the user should have, if any. Contains a list of user attribute names followed by the user attribute value.LookML model is localized, you can use the `locale` user attribute in the embed URL to specify a language for the embed. For example, including the parameter `user_attributes { "locale" : "fr_FR" }` would cause the embed to load French as its language. | Hash of strings |  `{``"vendor_id" : "17",``"company" : "xactness"``}`  
`access_filters` | Value Required | In Looker 3.10 this parameter was removed, but it is still required in the URL. Use `access_filters` with an empty placeholder, for example `access_filters={}`. | Empty Placeholder  
`first_name` | "" | The user's first name. If left blank, `first_name` will retain the value from the last request, or be "Embed" if no first name has ever been set. | JSON string | `"Alice"`  
`last_name` | "" | The user's last name. If left blank, `last_name` will retain the value from the last request, or be "Embed" if no last name has ever been set. | JSON string | `"Jones"`  
`user_timezone` | "" |  If you've enabled User Specific Time Zones, sets the value of the **Viewer Time Zone** option in the **Time Zone** drop-down on the embedded Look or dashboard. This parameter does not directly change the time zone in which the content is shown; the user will need to select a time zone from the drop-down.Signed embedding time zone reference documentation page.**Chat team tip:** If you want your embedded content to default to the viewer's time zone, use one of the following methods:
* Add the parameter `?query_timezone=user_timezone` to the embed URL. For example:`/embed/dashboards/1?query_timezone=user_timezone`
* Save the embedded dashboard or Look with the default time zone set to **Viewer Time Zone** , which will use the user's time zone by default for both embed users and non-embed users.
| JSON string or null |  `"US/Pacific"``null`  
`force_logout_login` | Value Required | If a normal Looker user is already logged in to Looker, and they view a signed embedded item, you can choose if: | Boolean (true or false) | `true`  
#### Signature
Looker uses the signature to verify that the correct embed secret was used to generate the signature in the embed URL and that the parameters in the embed URL have not changed. If either the embed secret or URL parameters are different or have changed, the signature won't match and the authentication will be rejected.
As a result, the signature in the embed URL provides cryptographically strong proof that the embed URL was not modified in transit and that the embed URL was created by a trusted party who has possession of the embed secret key.
To generate the signature you'll need to follow these steps.
  1. Gather the following parameter values in this order: 
     * Host, followed by `login/embed/` (for example, `analytics.mycompany.com/login/embed/`)
     * Embed URL
     * Nonce
     * Current Time
     * Session Length
     * External User ID
     * Permissions
     * Models
     * Group IDs
     * External Group ID
     * User Attributes
     * Access Filters (requires an empty placeholder)
  2. Format all values other than Host and Embed URL as JSON
  3. Concatenate the values with line breaks (`\n`)
  4. HMAC-SHA1 sign the concatenated string with your Looker embed secret key


#### Encoding
The final step is to URL encode your URL.
_Before_ you encode the URL, a properly formatted embed URL that uses all possible parameters might look like this:
```
https://analytics.mycompany.com/login/embed//embed/dashboards/1?
nonce="22b1ee700ef3dc2f500fb7"&
time=1407876784&
session_length=86400&
external_user_id="user-4"&
permissions=["access_data","see_user_dashboards","see_looks"]&
models=["model_one","model_two"]&
group_ids=[4,3]&
external_group_id="Allegra K"&
user_attributes={"vendor_id":"17","company":"xactness"}&
access_filters={}&
first_name="Alice"&
last_name="Jones"&
user_timezone="US/Pacific"&
force_logout_login=true&
signature=123456789ABCDEFGHIJKL

```

As noted previously, it is correct for `/embed//embed/` to appear in your URL.
_After_ you encode the URL, it would look like this:
```
https://analytics.mycompany.com/login/embed/%2embed%2Fdashboards%2F1?
nonce=%2222b1ee700ef3dc2f500fb7&%22&
time=1407876784&
session_length=86400&
external_user_id=%22user-4%22&
permissions=%5B%22access_data%22%2C%22see_user_dashboards%22%2C%22see_looks%22%5D&
models=%5B%22model_one%22%2C%22model_two%22%5D&
group_ids=%5B4%2C3%5D&
external_group_id=%22Allegra%20K%22&
user_attributes=%7B%22vendor_id%22%3A%2217%22%2C%22company%22%3A%22xactness%22%7D&
access_filters%7B%7D%26%0A
first_name=%22Alice%22&
last_name=%22Jones%22&
user_timezone=%22US%2FPacific%22&
force_logout_login=true&
signature=123456789ABCDEFGHIJKL

```

## Using the Create Signed Embed Url API endpoint
The Looker API includes the Create Signed Embed Url endpoint, which takes a set of signed embed parameters that includes the URL of the content that you want to embed and returns a complete, encoded, cryptographically signed URL.
To use this API endpoint from a web server, the web server must be able to authenticate into the Looker API with admin privileges. The web server domain must also be listed in the Embed Domain Allowlist.
You can also use the API Explorer to generate a signed URL that uses this endpoint. You can install the API Explorer on your Looker instance from the Looker Marketplace. Once generated, the signed URL must be copied exactly and can be used only once — otherwise, it will fail. The API Explorer is also useful for generating a signed URL and comparing it to a manually created signed URL for troubleshooting purposes.
For more information about the Looker API, see the Getting started with the Looker API documentation page.
## Testing the embed URL
To test your final URL, paste it into the Embed URI Validator on the **Embed** page of Looker's **Admin** section. While this option can't tell you if the data and permissions you envision have been set up correctly, it can validate that your authentication is working properly.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


