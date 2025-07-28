# Admin settings - General settings  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-general-settings

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Settings
    * Force BigQuery Readonly Scope usage
    * Technical Contacts
    * Application Time Zone
  * Feature Configuration
    * Login Consent Configuration
    * Message Configuration
    * Default Private Personal Folders
    * New Account Notification
    * Cookie Notification Banner
    * Limit Automatically refresh dashboard option
    * Google Cloud Project Number
    * User Specific Time Zones
    * Default Visualization Colors
    * Selecting an existing color collection
    * Load Assets from CDN
    * Persist Assets in Browser cache
    * Mobile Application Access
    * Force mobile authentication
  * Data Policy
    * Email Domain Allowlist for Scheduled Content
    * URL Allowlist for Data Actions
    * Block Inline Embedded Images in Query Results
    * Block Formulas and Macros in CSV and Excel Files
    * Outgoing Webhook Token
    * Automated Gemini in Looker enablement and user management
    * Default Export Format




Was this helpful?
Send feedback 
#  Admin settings - General settings
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Settings
    * Force BigQuery Readonly Scope usage
    * Technical Contacts
    * Application Time Zone
  * Feature Configuration
    * Login Consent Configuration
    * Message Configuration
    * Default Private Personal Folders
    * New Account Notification
    * Cookie Notification Banner
    * Limit Automatically refresh dashboard option
    * Google Cloud Project Number
    * User Specific Time Zones
    * Default Visualization Colors
    * Selecting an existing color collection
    * Load Assets from CDN
    * Persist Assets in Browser cache
    * Mobile Application Access
    * Force mobile authentication
  * Data Policy
    * Email Domain Allowlist for Scheduled Content
    * URL Allowlist for Data Actions
    * Block Inline Embedded Images in Query Results
    * Block Formulas and Macros in CSV and Excel Files
    * Outgoing Webhook Token
    * Automated Gemini in Looker enablement and user management
    * Default Export Format


The **Settings** page in the **General** section of the **Admin** panel lets Looker admins configure the instance-wide settings for Looker. Some settings are available only for Looker (original) instances or only for Looker (Google Cloud core) instances.
## Settings
The following settings are available for Looker instances.
### Force BigQuery Readonly Scope usage
Enabling this setting signs out users that have OAuth credentials that allow read and write scope on any of BigQuery connections. When the users authenticate again, Looker will create read-only OAuth credentials for those users instead. See Restricting OAuth scope to read-only for Google BigQuery connections for more information.
### License Key
The license key is unique to the Looker instance that you're using. It enables or disables certain Looker features based on your licensing agreement.
The license key is hidden by default. Select the eye icon visibility to display the license key.
### Host URL
The host URL is the base portion of your Looker instance's URL. It is used specifically when links to your instance are created in scheduled emails and in all absolute URLs that Looker generates.
Make sure the **Host URL** setting uses `http://` or `https://` appropriately, based on your instance's server configuration.
Changing the host URL may affect the functionality of some Looker features. See the What happens if the URL changes for my Looker instance? Best Practices page for more information about changing instance URLs.
### Technical Contacts
Email addresses that are added to this box will receive notifications of security updates, major bug fixes, and new Looker releases. The email address must belong to a valid Looker user. If you add an email that doesn't belong to a valid Looker user — for example, an email address for a distribution list — the email address will appear in the **Technical Contact** field, but Looker won't be able to deliver notifications to this address.
Looker Support requires permission from a technical contact to do any of the following:
  * Cause downtime for the instance, which could be due to a non-scheduled version update, performance changes to your Looker server, or other reasons
  * Change something about your Looker license, possibly to enable new features for you.


### Application Time Zone
When displaying data in an Explore, a Look, or a dashboard, Looker can convert time data from the connection's **Database Time Zone** to the appropriate time zone for that user.
If the **User Specific Time Zones** option is enabled, then an admin can set the user's default time zone or users can set their own default time zone. If the admin or user has not set the user's default time zone, then the **Application Time Zone** is used for that user, and all time-based data queried by that user will be converted to the **Application Time Zone**.
The **Application Time Zone** setting is also used as the default time zone for content deliveries. The time zone used for schedules does not affect time data returned by a query; it affects only the time a data delivery is sent.
See the Using time zone settings documentation page for more information.
## Feature Configuration
The following feature configuration settings are available for Looker instances.
### Closed System
The **Closed System** setting is used in conjunction with groups to prevent users in one group from knowing about the users in another group. This is often useful for multi-tenant installations.
The locations in Looker where users might see other users include the following:
  * The Users page in the **Admin** section of Looker
  * Users' folders in the **Folders** section of the Looker main menu, if they have been granted at least **View** access to another user's personal folder
  * The Manage Access pop-up, which is a part of folder management


When the **Closed System** setting is enabled, a non-admin user without the `see_users` permission can see only the other users with whom they share a group and only those groups of which they are a member.
Admins and any users who have been granted the `see_users` permission can see all users and groups on the instance.
### Login Consent Configuration
When enabled, **Login Consent Configuration** causes a consent screen to be displayed to all users who attempt to sign in to the Looker instance. The consent screen will display the message that was entered in the **Message Configuration** field, and will require users to click the **I Agree** button on the consent screen before they can sign in to the instance. Once you have enabled **Login Consent Configuration** , the **Message Configuration** field becomes visible.
### Message Configuration
If the **Login Consent Configuration** option is enabled, in the **Message Configuration** field, enter the message that will be displayed to all users who attempt to sign in to the Looker instance. This field becomes visible only after **Login Consent Configuration** is enabled.
### Default Private Personal Folders
When **Default Private Personal Folders** is enabled, a user's personal folder is by default visible only to that user and to Looker admins. By default, other users won't see the folder in the People folder, and the content in the folder won't be visible on boards or in content searches.
If you do want to provide access to a personal folder, you can add access to other users or to user groups through the **Manage Access** option from the personal folder's gear menu.
If you disable the **Default Private Personal Folders** option, a user's personal folder can be viewed by any Looker user in the **All Users** user group.
### New Account Notification
The **New Account Notification** setting can be enabled or disabled. When it is enabled, any Looker admin user will be emailed when a new Looker account is created. (Signed embed users are an exception; emails are not generated when a signed embed user is created.) The email will contain the new user's email address.
### In-App Guides
In-app guides let Looker communicate with users in the application through tutorials, banners, alerts, and surveys. These communications are used to help users get more out of the platform, alert them to new features, get user feedback on the platform, and invite users to trainings and events where they can learn how to better use Looker.
Administrators can choose to disable guides for their instance, which will disable the guides for all users on that instance. There is no way to selectively turn off in-app guides for certain users. Looker won't show in-app guides to embedded users or non-admin users on private label instances.
Guides are designed and deployed by Looker's Customer Experience team and will change over time. Looker uses third-party software (Pendo) JavaScript to serve the guides. Looker vets the individual guides and adds them to the allowlist. When fetching a guide from Pendo, Looker uses SHA-256 integrity hashes to validate that the guide is unchanged. If there are any changes to the guide after Looker's review, Looker prevents use of the changed guide. If a user's browser cannot reach the Pendo server, then the guide isn't displayed.
### Onboarding
When enabled, Looker admins and developers who log in to a new Looker instance will see the Looker onboarding walkthrough, which guides users through the four major steps to make use of a Looker instance:
  1. Adding a connection
  2. Creating a project
  3. Editing project files as needed
  4. Exploring data


Once any combination of admins or developers completes the full guide, it stops being displayed.
The **In-App Guides** setting must be enabled for the **Onboarding** option to be available.
### Cookie Notification Banner
When enabled, this setting will show a cookie notification banner to all users on your instance. This setting is disabled by default.
We recommend that you enable this setting if your Looker instance must comply with the European Union's data protection regulations.
### Curated Search
When **Curated Search** is enabled, a user can search for content across shared folders, their personal folder, and boards. Content that is saved in other users' personal folders will be included in the results only if such content is also pinned to a board. The search results will exclude content that exists only in the personal folders of other users. A user has the option to exclude content in personal folders by selecting the switch next to the **Curated Search** feature name in the search dialog modal.
### Limit Automatically refresh dashboard option
When this setting is enabled, only Looker admins will be able to enable the Automatically refresh dashboard option on user-defined dashboards. This prevents non-admin users from automatically refreshing data on dashboards and dashboard tiles. Automatically refreshing dashboard data can place a significant strain on some database systems.
### Google Cloud Project Number
A Google Cloud project number is required to enable in-app support. This value can be obtained from the Cloud Overview page in the console_name_short.
This change can take up to two hours to take effect. To implement the change immediately, click the **Update** button next to the License Key setting after entering your Google Cloud project number.
If you don't have a Google Cloud project for Looker yet, you can create one by following our Create a Google Cloud project guide or our more in-depth documentation on Creating and managing projects.
### Use Gravatar
When enabled, this setting displays the **Profile Picture** option on the user menu, letting users select or create an avatar for their account using the Gravatar app.
### User Specific Time Zones
When adding a connection, you specify what time zone your database stores time information as the **Database Time Zone**.
When **User Specific Time Zones** is enabled, each user is assigned a time zone, and Looker converts time-based data from the **Database Time Zone** to a user's time zone when the user views query results or interprets filters.
When **User Specific Time Zones** is disabled, Looker converts time-based data for all users to the **Query Time Zone** value.
See the Using time zone settings documentation page for more information.
### Default Visualization Colors
Each Looker instance must have a default color collection. The **Default Visualization Colors** setting lets you define a default color collection for visualizations, and also lets you create new color collections for use in your instances. You can select an existing color collection or create a custom color collection.
### Selecting an existing color collection
To set an existing color collection as your default, choose the color collection from the drop-down menu and click **Update**. Note: Setting a new default color collection will update all visualizations on Looks and dashboards that use the default color collection. Visualizations that are saved with a different color collection, or a custom palette, won't be affected.
You can see the first categorical, sequential, and diverging palettes of each collection directly under the drop-down menu. These are the palettes that will be used as the visualization defaults. To view all the palettes in the color collection, visit the Color collections documentation page.
#### Creating a custom color collection
To create a custom color collection, follow these steps:
  1. Select last **New color collection** option from the **Default Visualization Colors** collection drop-down menu.
  2. Give your new collection a unique name in the **Name** field.
  3. Click each color palette to open the **Colors in Palette** menu.
  4. Select individual colors in the **Colors in Palette** menu to edit one at a time, or select **Edit All** to edit all of the colors at once.
  5. Repeat steps 3 and 4 for each color palette.
  6. When you're finished editing your new color collection, click **Create**.


Color values can be formatted as hex strings, such as `#2ca6cd`, or as CSS color names, such as `mediumblue`. Or you can click the color wheel to open and select a shade from the color picker. If you choose to edit all colors, use a comma between each color name to separate them. To add or remove a color, click the **+** or **-** signs.
The new collection will automatically become the instance default, but you can choose a different default if you want.
Collection IDs and palette IDs for any new custom color collections are based on each collection's name. This allows LookML dashboards that use those collections to render consistently across instances if both instances have the same custom collections named identically.
#### Deleting a custom color collection
You can delete a custom color collection by selecting the collection from the drop-down menu and clicking the **Delete** button that appears. You cannot delete Looker's built-in color collections.
### Load Assets from CDN
This option is available only for customer-hosted instances. Because Looker-hosted instances always load assets from the CDN, you cannot disable this setting for these instances.
CDN stands for _content delivery network._ A CDN is a network of servers that stores content in multiple geographic locations to reduce page load time for users. Your data is never stored on these servers; only items that are specific to Looker (such as images) are stored on the CDN.
The **Load Assets from CDN** setting can be either enabled or disabled. When it is enabled, Looker pages should load faster.
### Persist Assets in Browser cache
When this setting is enabled, static assets such as JavaScript files and fonts are cached in each user's browser storage. This speeds up subsequent navigations, because the browser does not need to continue to reload these assets from the Looker server.
### Mobile Application Access
When this setting is enabled, users can log in to their Looker account on the instance using the Looker mobile app and the Looker (Legacy) app. When this setting is disabled, any existing mobile sessions are terminated.
### Force mobile authentication
When this setting is enabled, users are required to sign in to the Looker mobile app and the Looker (Legacy) app every time they open the app on their mobile device.
Additionally, users will be logged out of the mobile app after 60 minutes of inactivity.
## Data Policy
The following data policy settings are available for Looker instances.
### Public URLs
The **Public URL** setting can be enabled or disabled. When this setting is enabled, Looker users with appropriate permissions can generate public URLs to access Looker data.
### Email Domain Allowlist for Scheduled Content
This setting lets Looker admins define the email domains to which your users can deliver Looker content — Looks, dashboards, queries with visualizations — or alert notifications through email.
To limit content deliveries and alert notifications to email addresses with a specific domain, you can enter the domain in the format `domain.suffix`. For example, to limit email deliveries to just emails with `gmail.com` and `friendly_domain.org` domains, you can specify these domains in the **Email Domain Allowlist for Scheduled Content** field and then grant users the `schedule_look_emails` permission.
See more about how this setting and a user's permissions affect their ability to deliver Looker content and alert notifications in the Permissions overview section on this page.
####  `looker_internal_email_domain_allowlist` user attribute
In addition to the email domains that are included in the global **Email Domain Allowlist for Scheduled Content** field, you can also specify email domains on a per-group level using the `looker_internal_email_domain_allowlist` user attribute. The user attribute accepts the same string format as the **Email Domain Allowlist for Scheduled Content** admin setting.
If a group is assigned multiple email domain sets, for example through membership in multiple groups, then members of that group will be able to send emails to all domains that are assigned to each of the user attribute values, as well as the domains that are listed in the **Email Domain Allowlist for Scheduled Content** admin setting. In other words, the set of email domains that a group can send emails to is the union of the set of email domains that are listed in the **Email Domain Allowlist for Scheduled Content** field and every set of email domains that are assigned to the group by the `looker_internal_email_domain_allowlist` user attribute.
#### Permissions overview
Embed and non-embed users must have at least the `schedule_look_emails` permission to be able to email any Looker content. To send alert notifications, a user must also have `create_alerts` permissions.
Embed and non-embed users who have the `schedule_look_emails` permission may also be granted the `schedule_external_look_emails` permission (see more on permissions and dependencies on the **Roles** documentation page).
For an overview of how user permissions affect the domains to which users can send Looker content deliveries or alert notifications, see the following table:
**User type** | **Permissions** | **Email Domain Allowlist for Scheduled Content contains the domain`friendly_domain.org`** | **Email Domain Allowlist for Scheduled Content contains no domains**  
---|---|---|---  
Non-embed |  `schedule_look_emails` only | Can email content deliveries to their own email address, to the email address of another Looker user on the same instance, or to an email address with the `friendly_domain.org` domain | Can email content deliveries to any email address  
`schedule_look_emails` and  | Can email content deliveries and alert notifications to their own email address, to the email address of another Looker user on the same instance, or to an email address with the `friendly_domain.org` domain | Can email content deliveries and alert notifications to any email address  
`schedule_external_look_emails` only | Can email content deliveries to any email address | Can email content deliveries to any email address  
`schedule_external_look_emails` and  | Can email content deliveries and alert notifications to any email address | Can email content deliveries and alert notifications to any email address  
Signed embed |  `schedule_look_emails` only | Can email content deliveries to an email address with the `friendly_domain.org` domain | Cannot email any Looker content  
`schedule_look_emails` and  | Can email content deliveries and alert notifications to an email address with the `friendly_domain.org` domain | Cannot email any Looker content or alert notifications  
`schedule_external_look_emails` | Can email content deliveries to any email address | Can email content deliveries to any email address  
`schedule_external_look_emails` and  | Can email content deliveries and alert notifications to any email address | Can email content deliveries and alert notifications to any email address  
Embedded Looker content is accessed through a dedicated embed user account, not by individual user accounts. When a person accesses Looker content through an embed, Looker isn't expected to know the individual user's email address.
One exception to the rules that are stipulated in the table is as follows: You can provide Looker with an embed user's email address by defining it in the `email` user attribute in the signed embed URL. For example:
```
...&user_attributes={"email":"joe@domain.com"}

```

If you define the `email` user attribute in the embed URL, Looker will allow an embed user who has only the `schedule_look_emails` permission to email Looker content to their own email address, even if their email domain isn't in the **Email Domain Allowlist for Scheduled Content** field, or if the **Email Domain Allowlist for Scheduled Content** field is blank.
### URL Allowlist for Data Actions
This setting lets you define URLs (such as `https://looker.com`) where your users can process data actions.
For example, if you add the URL `https://looker.com` to the URL allowlist for data actions, data actions will be able to be processed only at `https://looker.com`. Attempts to process data actions at other URLs won't be allowed.
If this field is left blank, there are no URL restrictions for data actions. However, if you have included a user attribute in a data action, this field is required. In that case, you must provide valid URLs to process data actions.
### Block Inline Embedded Images in Query Results
By default, Looker does not display Base64 encoded images in query results. Disable this setting to display Base64 encoded images in query results.
### Block Formulas and Macros in CSV and Excel Files
When this setting is enabled, Looker prepends a `'` character to all values that could be interpreted as formulas or macros in queries that are downloaded in CSV or Excel spreadsheet formats.
### Outgoing Webhook Token
If a user uses a webhook to deliver content — such as a dashboard or a Look — the request will include a special Looker token that can be set here. Servers that receive webhooks can then verify that requests contain this value to verify the legitimacy of webhook requests. To reset the roken, click **Reset**.
### Automated Gemini in Looker enablement and user management
A new user group called **Default Gemini Users** has been created automatically for all Looker (original) instances that use an open system configuration. Users in this group are assigned the **Gemini** role, which grants them the ability to use Gemini in Looker features.
The status of the **Automated Gemini in Looker enablement and user management** setting affects the group as follows:
  * If you enable the setting: 
    * New users who are added to the instance are added to the group automatically.
  * If you disable the setting: 
    * New users who are added to the instance must be added to the group manually.
    * If you want to remove members from the **Default Gemini Users** group, you must remove them manually.


The status of the setting as of June 9, 2025, has the following effects:
  * If the setting was enabled prior to June 9, 2025, all existing users have been added to the group and all new users will be added to the group. Gemini in Looker has been enabled automatically.
  * If the setting was disabled as of June 9, 2025, all users must be added to the group manually. Gemini in Looker has not been enabled automatically.


Gemini in Looker can be enabled or disabled manually on the Gemini in Looker page in the **Platform** section of the **Admin** panel. Its status is not affected by the status of the **Automated Gemini in Looker enablement and user management** setting.
### Default Export Format
The **Default Export Format** setting lets you choose the default file format that is used when users choose to download data. Users can still choose a different file format if they like. The following formats are available:
Format | File extension | Description  
---|---|---  
TXT | `.txt` | Generates a text file delimited by tabs.  
Excel Spreadsheet | `.xlsx` | Generates a spreadsheet file using the format for Microsoft Excel 2007 and later.  
CSV | `.csv` | Generates a text file delimited by commas.  
JSON | `.json` | Generates a JSON file with one record per line.  
HTML | `.html` | Generates basic HTML to display the data in a way that is similar to how the user sees it in their browser; however, the formatting is not exactly the same because Looker's CSS won't be included.  
Markdown | `.md` | Generates a standard Markdown file with a `|` delimited table.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


