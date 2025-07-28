# Admin settings - Roles  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com//looker/docs/admin-panel-users-roles

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Managing roles
    * Creating, editing, and deleting roles
  * Permission sets
    * Default permission sets
    * Creating permission sets
    * Permissions and dependencies
    * Permissions and Looker licenses
    * Permissions list
  * Model sets
    * Creating a model set
    * Editing a model set
    * Deleting a model set




Send feedback 
#  Admin settings - Roles
Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * Managing roles
    * Creating, editing, and deleting roles
  * Permission sets
    * Default permission sets
    * Creating permission sets
    * Permissions and dependencies
    * Permissions and Looker licenses
    * Permissions list
  * Model sets
    * Creating a model set
    * Editing a model set
    * Deleting a model set


Roles, permission sets, and model sets are used together to manage what users can do and what they can see. The **Roles** page in the **Users** section of the **Admin** panel lets you view, configure, and assign roles, permission sets, and model sets.
You can search for specific roles, permission sets, and model sets by entering a search term into the search box in the upper right and pressing **Enter**.
## Definitions
  * A **role** defines the privileges that a user or group will have for a specific set of models in Looker. You create a role by combining one permission set with one model set.
  * A **permission set** defines what a user or group can do. You select a combination of permissions that you want to assign to a user or group. It must be used as part of a role to have any effect.
  * A **model set** defines what data and LookML fields a user or group can see. You select a combination of LookML models to which a user or group should have access. It must be used as part of a role to have any effect.


## Managing roles
A role is a combination of one permission set and one model set. It's a common convention to name roles after types of people or groups of people in your organization — administrator, Looker developer, Finance team — although you can certainly follow your own naming conventions.
A user can have more than one role in Looker. This can be useful when you have users who play multiple roles in your company or when you want to create complex systems of access to your models.
### Creating, editing, and deleting roles
To create a role, follow these steps:
  1. Click the **New Role** button at the top of the **Roles** page.
  2. Looker displays the **New Role** page, where you can configure the following settings:
     * **Name** : Enter a name for the role.
     * **Permission Set** : Choose a permission set to associate with the role.
     * **Model Set** : Choose a model set to associate with the role.
     * **Groups** : Optionally, choose one or more groups to assign the role to.
     * **Users** : Optionally, choose one or more users to assign the role to.
  3. Once you've configured the role as intended, click the **New Role** button at the bottom of the page.


After a role has been created, you can edit it by clicking the **Edit** button to the right of the role on the **Roles** page. Clicking **Edit** takes you to the **Edit Role** page for that role, where you can edit the name, the permission set, the model set, and the groups or users who are assigned to the role.
To delete a role, click the **Delete** button to the right of the role on the **Roles** page.
### Default roles
For new instances, Looker creates the following default roles, each of which includes a default permission set of the same name:
  * Admin
  * Admin via IAM
  * Developer
  * Support Advanced Editor
  * Support Basic Editor
  * User
  * Viewer


The default roles in the following sections have conditions for use.
#### Admin via IAM
The Admin via IAM role is available only in Looker (Google Cloud core), and it can be managed only through the Google Cloud console. For more information, see the Authentication and authorization with OAuth and IAM and Admin Looker role versus the Admin via IAM Looker role documentation.
The **Admin via IAM** role uses the **Admin** permission set.
#### Gemini
The **Gemini** role cannot be renamed or deleted and contains only the `gemini_in_looker` permission in its permission set. By default, this role's permission set applies to all models on the Looker instance. To restrict users to accessing Gemini in Looker features with specific models, remove those users from the **Gemini** role and create a new role that applies the `gemini_in_looker` permission on selected models. Make sure to remove those users from the **Gemini Default Users** group.
The `gemini_in_looker` permission that is available in this role enables users to perform the following tasks in the Looker instance with Gemini assistance:
  * Write LookML — when they also have a Looker role that contains the `develop` permission for at least one model in a LookML project.
  * Create custom Looker visualizations — when they also have a Looker role that contains the `can_override_vis_config` permission.
  * Query Looker Explore data with Conversational Analytics, even if the user hasn't been assigned `explore` permissions, when they also have a Looker role that contains the `access_data` permission on the model that they are querying.


For more information about Gemini in Looker features, see the Gemini in Looker overview.
#### Support Advanced Editor and Support Basic Editor
These roles won't appear on a Looker (original) instance if a Looker admin has disabled the Tiered Support Access Labs feature. These roles won't appear on a Looker (Google Cloud core) instance if the instance uses private IP (private services access or Private Service Connect) networking or public IP and private IP networking.
The **Support Advanced Editor** and **Support Basic Editor** roles cannot be edited, deleted, or assigned to users other than support access users.
## Permission sets
A permission set defines what a user or group can do. Admins can use Looker's default permission sets or create original permission sets, keeping in mind permission dependencies.
All the available permissions, and their types, are discussed in more detail in the permissions list.
### Default permission sets
For new installations, Looker includes several default permission sets that you can start with:
Permission Set | Included Permissions  
---|---  
Admin | All permissions  
Developer |  `access_data`, `can_create_forecast`, `clear_cache_refresh`, `create_custom_fields`, `create_table_calculations`, `deploy`, `develop`, `download_without_limit`, `explore`, `manage_spaces`, `mobile_app_access`, `save_content`, `save_dashboards`, `save_looks`, `schedule_look_emails`, `see_drill_overlay`, `see_lookml`, `see_lookml_dashboards`, `see_looks`, `see_pdts`, `see_sql`, `see_user_dashboards`, `send_to_integration`, `use_sql_runner`**NOTE** : The `see_pdts` permission is included in the **Developer** default permission only for Looker installations that were created with Looker 21.18 or later. To verify whether the `see_pdts` permission is included in the **Developer** permission set on your instance, go to the **Roles** page in the **Admin** panel in the Looker UI.  
Gemini | `gemini_in_looker`  
Support Advanced Editor |  `access_data`, `clear_cache_refresh`, `create_custom_fields`, `create_table_calculations`, `develop`, `explore`, `follow_alerts`, `manage_embed_settings`, `manage_models`, `manage_privatelabel`, `manage_project_connections`, `manage_project_connections_restricted`, `manage_project_models`, `manage_themes`, `see_admin`, `see_alerts`, `see_datagroups`, `see_drill_overlay`, `see_logs`, `see_lookml`, `see_lookml_dashboards`, `see_looks`, `see_pdts`, `see_queries`, `see_schedules`, `see_sql`, `see_system_activity`, `see_user_dashboards`, `see_users`, `update_datagroups`, `use_global_connections`**NOTE** : The **Support Advanced Editor** permission set isn't available if the Tiered Support Access Labs feature is disabled. The **Support Advanced Editor** permission set can't be edited or deleted.  
Support Basic Editor |  `access_data`, `clear_cache_refresh`, `create_custom_fields`, `create_table_calculations`, `explore`, `follow_alerts`, `manage_privatelabel`, `manage_themes`, `see_admin`, `see_alerts`, `see_drill_overlay`, `see_logs`, `see_lookml`, `see_lookml_dashboards`, `see_looks`, `see_pdts`, `see_schedules`, `see_sql`, `see_datagroups`, `see_system_activity`, `see_user_dashboards`, `see_users`**NOTE** : The **Support Basic Editor** permission set isn't available if the Tiered Support Access Labs feature is disabled. The **Support Basic Editor** permission set can't be edited or deleted.  
LookML dashboard user |  `access_data`, `clear_cache_refresh`, `mobile_app_access`, `see_lookml_dashboards`, `send_to_integration`  
User |  `access_data`, `can_create_forecast`, `clear_cache_refresh`, `create_custom_fields`, `create_table_calculations`, `download_without_limit`, `explore`, `manage_spaces`, `mobile_app_access`, `save_content`, `save_dashboards`, `save_looks`, `schedule_look_emails`, `see_drill_overlay`, `see_lookml`, `see_lookml_dashboards`, `see_looks`, `see_sql`, `see_user_dashboards`, `send_to_integration`  
User who can't view LookML |  `access_data`, `can_create_forecast`, `clear_cache_refresh`, `create_custom_fields`, `create_table_calculations`, `download_without_limit`, `explore`, `manage_spaces`, `mobile_app_access`, `save_content`, `save_dashboards`, `save_looks`, `schedule_look_emails`, `see_lookml_dashboards`, `see_looks`, `see_user_dashboards`, `send_to_integration`  
Viewer |  `access_data`, `clear_cache_refresh`, `download_without_limit`, `mobile_app_access``,` `schedule_look_emails`, `see_drill_overlay`, `see_lookml_dashboards`, `see_looks`, `see_user_dashboards`  
You'll see these permission sets appear as options when you create a new role. If you select one of these permission sets, Looker will display the list of permissions that it includes.
> The Admin permission set cannot be edited or deleted, and it cannot be assigned to a role. It is assigned _only_ to the Admin role, which also cannot be edited or deleted. The only way to grant the Admin permission set to a user or group is to add the Admin role to that user or group.
### Creating permission sets
To create a permission set, click the **New Permission Set** button at the top of the **Roles** page. Looker will display a page where you can enter a name for the permission set and select the permissions that it should include. Once you've configured the set as needed, click the **New Permission Set** button at the bottom of the page.
After a permission set has been created, you can edit or delete it by clicking the **Edit** or **Delete** buttons to the right of the permission set on the **Roles** page.
### Permissions and dependencies
Some permissions depend on others to work properly. For example, it makes sense that someone who wants to develop in LookML must first be able to see LookML.
When you create a permission set, you'll see the available permissions in an indented list. If a privilege is indented under another (parent) privilege, you must select the parent privilege first. The permission list may look like this:
```
☑️ access_data
  ☑️ see_lookml_dashboards
  ☑️ see_looks
    ☑️ see_user_dashboards

```

In this example, Looker uses indentation to indicate the following:
  * The `access_data` privilege can be selected at any time.
  * The `see_lookml_dashboards` and `see_looks` privileges require the `access_data` privilege to be selected first.
  * The `see_user_dashboards` privilege depends on the `see_looks` privilege, which in turn depends on `access_data` privilege.


You cannot select a child privilege without first selecting its parent.
### Permissions and Looker licenses
Looker licenses classify users into three types:
  * Developer (Admin)
  * Standard (Creator)
  * Viewer


The permissions granted to a user determine how that user is classified under the Looker license:
  * A user is classified as a Developer (Admin) user if they have the Admin default role, or at least one of the following permissions:
  * A user is classified as a Standard (Creator) user if they have none of the Developer (Admin) permissions but do have at least one of the following permissions:
    * `create_prefetches`
    * `see_system_activity`
  * A user is classified as a Viewer if they have the `access_data` permission, but none of the Developer (Admin) permissions and none of the Standard (Creator) permissions.


### Permissions list
Permissions can be classified as one of three types:
  * **Model Specific:** This type of permission is applied only to the model sets that are part of the same role. This permission is applied to individual models or model sets, rather than across the entire Looker instance.
  * **Connection Specific:** This type of permission is applied at the connection level. A user with this type of permission will see content on pages in the **Admin** panel that uses a connection associated with a model to which they have data access, even if that connection is used with another model to which they do not have data access.
  * **Instance Wide:** This type of permission applies to the Looker instance as a whole and has three types: 
    * NN = **No content access, No menu access** : These permissions allow users to perform certain functions across the entire Looker instance, but do not allow users to access content based on models not included in their role's model set.
    * CN = **Content access, No menu access** : These permissions allow users to access content and query information across the entire Looker instance — even for content and queries based on models not included in their role's model set.
    * CM = **Content access, Menu access** : These permissions may expose parts of the Admin menu to non-admin users and allow users to see information about content and queries based on models not included in their role's model set.


The following list describes all the permissions that are available in Looker, in the order in which they appear on the **New Permission Set** page in the **Admin** section:
Permission | Depends On | Type | Definition  
---|---|---|---  
`access_data` | None | Model Specific |  Users can access data from Looker, but only the data that admins specify. This permission is necessary for almost all Looker functions.**Data** section of that project (such as a JSON custom map file).  
`see_lookml_dashboards` | `access_data` | Model Specific |  Users can see the LookML `Dashboards` folder, which includes all LookML dashboards. Users must have `explore` permission for any relevant models to explore those dashboards. Users who also have the `develop` permission can create LookML dashboards  
`see_looks` | `access_data` | Model Specific |  Users can see saved Looks (but not dashboards) within folders. Users must have `explore` permission for any relevant models to explore those Looks. Users will also need the **View** content access level to see Looks in folders.  
`see_user_dashboards` | `see_looks` | Model Specific |  Users can view user-defined dashboards in folders but must have `explore` permission for any relevant models to explore those dashboards. Users also need **View** content access to see dashboards in folders. Users who also have both the `save_dashboards` permission and the **Manage Access, Edit** content access to a folder can create user-defined dashboards in that folder.  
`explore` | `see_looks` | Model Specific |  Users can access and use the Explore page to generate Looks and dashboards. Without this permission, users can view saved dashboards only (if `see_lookml_dashboards` or `see_user_dashboards` has been granted).  
`create_table_calculations` | `explore` | Instance Wide NN |  Users can view, edit, or add table calculations  
`create_custom_fields` | `explore` | Instance Wide NN |  Users can view, edit, or add custom fields; users who have only the `explore` permission can only view custom fields.  
`can_create_forecast` | `explore` | Instance Wide NN |  Users can create and edit forecasts in visualizations; users who don't have this permission can only view existing forecasts in the content to which they have access.  
`can_override_vis_config` | `explore` | Instance Wide NN |  Users can access the Chart Config Editor, which lets them modify the Highchart API JSON values of a visualization and customize the visualization appearance and format.  
`save_content` | `see_looks` | Instance Wide NN |  This permission is a parent permission of `save_dashboards`, `save_looks`, and `create_public_looks`. This permission must be granted with either `save_dashboards` or `save_looks`.  
`save_dashboards` | `save_content` | Instance Wide NN |  Users can save and edit dashboards. Users must have `explore` permission for any relevant models to explore from those dashboards. Users must have `download_with_limit` and/or `download_without_limit` permissions to download the content.  
`save_looks` | `save_content` | Instance Wide NN |  Users can save and edit Looks. Users must have `explore` permission for any relevant models to explore from those Looks. Users must have `download_with_limit` and/or `download_without_limit` permissions to download the content.  
`create_public_looks` | `save_looks` | Model Specific |  Users can mark a saved Look as public, which will then generate URLs that grant access to that Look without authentication.  
`download_with_limit` | `see_looks` | Model Specific |  _This permission applies to Looks and dashboards in Looker and to reports in Looker Studio that use the Looker connector._ Users can download data but must specify a row limit of 5,000 or fewer to avoid memory problems from large downloads. Looker Studio Pro users with this permission can download Looker Studio reports that use the Looker connector.   
`download_without_limit` | `see_looks` | Model Specific |  _This permission applies to Looks and dashboards in Looker and to reports in Looker Studio that use the Looker connector._ The same as `download_with_limit`, but does not require the user to specify a row limit. Downloading all results for some types of queries may require substantial memory, potentially causing performance issues or even crashing the Looker instance.  
`schedule_look_emails` | `see_looks` | Model Specific |  _This permission applies to Looks and dashboards in Looker and to reports in Looker Studio that use the Looker connector._deliver any Looks, dashboards, and queries with visualizations to which they have data access to email. Users can schedule delivery to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs.System Activity dashboards, users must have access to all models.`create_alerts` permissions can send email alert notifications. **Email domain allowlist** on the **Settings** page of the **Admin** panel.  
`schedule_external_look_emails` | `schedule_look_emails` | Model Specific |  Users can deliver any Looks, dashboards, and queries with visualizations to which they have data access to email. Users can schedule delivery to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs.System Activity dashboards, users must have access to all models.`create_alerts` permissions can send email alert notifications. **Email domain allowlist** on the **Settings** page of the **Admin** panel contains any email domains.  
`create_alerts` | `see_looks` | Instance Wide NN |  _This permission applies to dashboards in Looker and to charts in Looker Studio that use the Looker connector._ From the dashboard tile, users can create, duplicate, and delete their own alerts; and can see and duplicate alerts that are marked **Public** by other users. The user must be signed in to Slack to see dashboard tile alerts that send Slack notifications. Users can view, edit, disable, and enable alerts that they own on the **Manage Alerts** user page. Users must have the `schedule_look_emails` or the `schedule_external_look_emails` permission to send email alert notifications. Looker Studio Pro users with this permission can create, duplicate, and delete alerts on Looker Studio reports that use the Looker connector.  
`follow_alerts` | `see_looks` | Instance Wide NN | Users can view and follow alerts. View the alerts that they have followed or for which they are listed as a recipient from the **Manage Alerts** user page.  
`send_to_s3` | `see_looks` | Model Specific |  Users can deliver any Looks, dashboards, and queries with visualizations to which they have data access to an Amazon S3 bucket. Users can schedule delivery to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs. **This permission is applied to individual models or model sets, rather than across the entire Looker instance.**  
`send_to_sftp` | `see_looks` | Model Specific |  Users can deliver any Looks, dashboards, and queries with visualizations to which they have data access to an SFTP server. Users can schedule delivery to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs. **This permission is applied to individual models or model sets, rather than across the entire Looker instance.**  
`send_outgoing_webhook` | `see_looks` | Model Specific |  Users can deliver any Looks, dashboards, and queries with visualizations to which they have data access to a webhook. Users can schedule delivery to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs. **This permission is applied to individual models or model sets, rather than across the entire Looker instance.**  
`send_to_integration` | `see_looks` | Model Specific | Users can deliver any Looks, dashboards, and queries with visualizations to which they have data access to the third-party services integrated with Looker using the Looker Action Hub. If using custom actions with user attributes, users must have this permission _and_ have a non-null and valid user attribute value for the specified user attribute to deliver Looker content to that action destination. This permission is not related to data actions. Users can schedule delivery to occur after a datagroup has been triggered, has managed the cache, and has rebuilt relevant PDTs. **This permission is applied to individual models or model sets, rather than across the entire Looker instance.**  
`see_sql` | `see_looks` | Model Specific |  Users can access the **SQL** tab while exploring and any SQL errors that are caused by their queries.  
`see_lookml` | `see_looks` | Model Specific |  Users have read-only access to LookML. Users must have this permission to see the Go to LookML link in the **Admin** panel. `develop` permission. **NOTE** : This permission interacts with model sets in a potentially unexpected way. If you assign the `see_lookml` permission to a user, and you've allowed that user to see _any_ model that is a part of a project, they will be able to see the LookML for _all_ models in that project. However, they will still not be able to _query_ models that you have not allowed.  
`develop` | `see_looks` | Model Specific |  Users can make local changes to LookML but won't let them make those changes available to everyone unless they also have the `deploy` permission. **Get support** option in the **Help** menu, and to see metadata in the Looker IDE. Users also need this permission to access the **Rebuild Derived Tables & Run** option in the Explore gear menu. This is not model-specific, so if a user has this permission in one model, they will have access to **Rebuild Derived Tables & Run** in all models.**NOTE** : This permission interacts with model sets in a potentially unexpected way. If you assign the `develop` permission to a user, and you've allowed that user to see _any_ model that is a part of a project, they will be able to develop the LookML for _all_ models in that project. However, they will still not be able to _query_ models that you have not allowed.  
`deploy` | `develop` | Instance Wide NN |  Users can push their local LookML changes to production so that those changes become available to everyone.  
`support_access_toggle` | `develop` | Instance Wide NN |  Users can enable or disable access by Looker analysts to your Looker instance.  
`manage_project_models` | `develop` | Model Specific |  Users can add, edit, or delete model configurations for allowed models on the Edit Model Configuration page. When configuring a model, users can use only project-scoped connections.**NOTE** : This permission interacts with model sets in a potentially unexpected way. If you create a role with the `manage_project_models` permission, the role will grant access to all models that share a project with any of the models in the role's model sets.  
`use_global_connections` | `manage_project_models` | Model Specific |  Users can configure allowed models with any project-scoped connection or any instance-wide connection.  
`manage_project_connections_restricted` | `develop` | Model Specific CM |  Users can see the Connections page in the Admin menu. They can see, edit, and create project-scoped connections for any projects in the model set. However, they can edit only the following connection settings: 
  * All settings in the **General settings** section
  * All settings in the **SSH Server** section
  * All settings in the **Time Zone** section
  * The **Additional JDBC Parameters** , **SSL** , **Verify SSL** , and **Use TNS** settings in the **Additional Settings** section

Users cannot edit any other settings in the **Additional Settings** section. They also cannot edit any settings in the **Persistent Derived Tables (PDTs)** section. **NOTE** : This permission interacts with model sets in a potentially unexpected way. If you assign the `manage_project_connections_restricted` permission to a user, the user will be able to see, edit, and create project-scoped connections for any projects included in the model set.   
`manage_project_connections` | `manage_project_connections_restricted` | Model Specific CM |  Users can see the Connections page in the Admin menu. They can see, edit, and create project-scoped connections for any projects included in the model set.**NOTE** : This permission interacts with model sets in a potentially unexpected way. If you assign the `manage_project_connections_restricted` permission to a user, the user will be able to see, edit, and create project-scoped connections for any projects included in the model set.  
`see_ci` | `develop` | Instance Wide NN |  Added 25.6  Users can view the results of Continuous Integration runs, view the Continuous Integration **Suites** page, and run test suites.  
`manage_ci` | `see_ci` | Instance Wide NN |  Added 25.6  Users can create Continuous Integration suites, manage Continuous Integration users, and configure the git connection with Continuous Integration.  
`use_sql_runner` | `see_lookml` | Model Specific |  Users can use SQL Runner to run raw SQL against their allowed connections. Users will also be able to download results from the **Download** option in the SQL Runner gear menu, regardless of whether the user has the `download_with_limit` or `download_without_limit` permissions.  
`clear_cache_refresh` | `access_data` | Model Specific |  Users can clear cache and refresh internal and embedded dashboards, dashboard tiles, Looks, and Explores.`clear_cache_refresh` permission is automatically added to any pre-existing permission sets that contain any of the following permissions: `see_user_dashboards`, `see_lookml_dashboards`, or `explore`. The `clear_cache_refresh` permission is not automatically applied to any embedded roles.  
`see_drill_overlay` | `access_data` | Model Specific |  Users can see the results of drilling into a dashboard tile but cannot explore those results. If `explore` is granted, this permission is also automatically granted (even if it isn't checked). Users must also have `explore` permissions to download drill results in PNG format.  
`manage_spaces` | None | Instance Wide CN |  Users can create, edit, move, and delete folders. Users will also need the **Manage Access, Edit** content access permission.  
`manage_homepage` | None | Instance Wide NN |  Users can edit and add content to the sidebar that all Looker users see on the pre-built Looker homepage.  
`manage_models` | None | Instance Wide CN |  Each LookML model is mapped to a specific set of database connections on the Manage LookML Projects page. With this permission, users can configure these mappings, create new projects, and delete projects. Non-admin users who are granted this permission will have access to all connections that are allowed by the models to which they have access.**NOTE** : This permission interacts with model sets in a potentially unexpected way. If you assign the `manage_models` permission to a user, the user will be able to access all models in all projects in the instance.  
`create_prefetches` | None | Instance Wide |  Prefetching is strongly discouraged. We recommend using datagroups instead.  
`login_special_email` | None | Instance Wide |  Users can log in with email/password credentials, even if other login mechanisms (such as Google, LDAP, or SAML) have been enabled on your instance. This can be useful for consultants or others who may not be a part of your normal authentication system.  
`embed_browse_spaces` | None | Instance Wide NN |  Enables the content browser for signed embeds. If you are using signed embeds, you should grant this permission to users who have the `save_content` permission.  
`embed_save_shared_space` | None | Instance Wide |  Allows user with the `save_content` permission to save content to the organization's **Shared** folder, if there is one. Users who have the `save_content` permission but not the `embed_save_shared_space` permission will only have the option to save content to their personal embed folder.  
`manage_embed_settings` | None | Instance Wide CM |  Users can edit embed settings on the **Embed** page in the **Platform** section of the **Admin** menu.  
`manage_modelsets_restricted` | None | Model Specific CM |  Added 25.2  Users can modify model sets for which they have the `manage_modelsets_restricted` permission. A user can only add models contained in model sets for which the user also has the `manage_modelsets_restricted` permission.**NOTE** : This permission interacts with model sets in a potentially unexpected way. If you assign the `manage_modelsets_restricted` permission to a user, and you've allowed that user to access _any_ model that is a part of a project, they will be able to assign _all_ models in that project to model sets that they have access to.  
`manage_schedules` | None | Model Specific CM |  Added 25.2  Users can reassign and delete schedules on the **Schedules** page for the specified models. This permission does not give a user the ability to see the **Schedule History** page.  
`manage_themes` | None | Instance Wide CM |  Users can configure theme settings on the **Themes** page in the **Platform** section of the **Admin** menu.  
`manage_privatelabel` | None | Instance Wide CM |  Users can configure private label settings on the **Private Label** page in the **Platform** section of the **Admin** menu.  
`see_alerts` | None | Instance Wide CM |  Users can access the **Alerts** and **Alert History** pages in the **Admin** section, allowing users to see all alerts on a Looker instance. Users can view, follow, edit, self-assign, and disable alerts that are owned by other users from the **Alerts** admin page.**Alert Details** page) or to navigate to its dashboard. This permission does not grant users the ability to view, create, follow, or delete alerts from the dashboard tile.  
`see_queries` | None | Instance Wide CM |  Users can see the Queries page in the **Admin** section of Looker. This privilege does not give a user the ability to terminate a query on the **Queries** page.  
`see_logs` | None | Instance Wide CM |  Users can see the Log page in the **Admin** section of Looker.  
`see_users` | None | Instance Wide CM |  Users can see the Users page (but not the Groups page) in the **Admin** section of Looker. This privilege does not give a user the ability to create new users, see or create API credentials, reset passwords, or otherwise modify users or privileges. A user granted this permission can see all users in all groups on an instance, even on a closed system. A user can see all group names and all role names, which some companies may consider sensitive.  
`sudo` | `see_users` | Instance Wide CM |  Users can sudo (in other words, act as and temporarily inherit the permissions of) another user by clicking the **Sudo** button on the Users page.`sudo` permission does not allow a non-admin to sudo as an admin, _but a non-admin could potentially escalate their privileges by using sudo_ , so exercise caution.   
`manage_groups` | `see_users` | Instance Wide CM |  Users can create, edit, and delete groups on the **Groups** page in the **Users** section of the **Admin** menu, with the exception of any groups that are associated with the **Admin** role.  
`manage_roles` | `manage_groups` | Instance Wide CM |  Users can create, edit, and delete roles, except for the **Admin** role, on the **Roles** page in the **Users** section of the **Admin** menu. Users still cannot create, edit, or delete permission sets or model sets.  
`manage_user_attributes` | `see_users` | Instance Wide CM |  Users can create, edit, and delete user attributes on the **User Attributes** page in the **Users** section of the **Admin** menu.  
`see_schedules` | None | Instance Wide CM | Users can see the **Schedules** (**Schedules**) and **Schedule History** (**Schedule History**) pages from the **Admin** panel in Looker. This privilege does not give a user the ability to reassign, edit, or delete other users' schedules on the **Schedules** and **Schedule History** pages.  
`see_pdts` | None | Connection Specific |  Users can see the Persistent Derived Tables page in the **Admin** section of Looker and view information about PDTs from projects that use any connection associated with models for which they have data access.**Developer** default permission set for new Looker installations.  
`see_datagroups` | None | Model Specific |  Users can see the Datagroups page in the **Admin** section of Looker. Users can see connection names, model names, and other information about datagroups defined in a model for which they have data access.  
`update_datagroups` | `see_datagroups` | Model Specific |  Users can trigger a datagroup, or reset its cache, through the Datagroups page in the **Admin** section of Looker. Like users who have the `see_datagroups` permission, users who have the `update_datagroups` permission can see datagroups that are defined in projects that use a model for which they have data access.  
`see_system_activity` | None | Instance Wide CM |  Users can access the System Activity Explores and dashboards to view usage, history, and other metadata about a Looker instance.  
`see_admin` | None | Instance Wide CM |  Users can have read-only access to admin resources, including pages in the **Admin** panel, with the exception of the following pages:
  * Support Access
  * Labs
  * Legacy Features
  * Export
  * Content Access
  * Actions (if the page displays only the enabled or disabled states of actions)

  
`mobile_app_access` | None | Instance Wide NN |  Users can sign in to your instance on a mobile device using the Looker mobile app. For users to be able to sign in to the Looker mobile app, the **Mobile Application Access** option in the **General Settings** page in the **Admin** section of Looker first must be enabled.`mobile_app_access` permission can be added to a new or existing permission set, and it is part of all of Looker's default permission sets.  
`gemini_in_looker` | None | Instance Wide NN |  This permission is the only permission that is included in the **Gemini** default role. This permission can't be added to any other permission sets or roles. write LookML using Gemini assistance when they also have a Looker role that contains the `develop` permission for at least one model in a LookML project.create custom Looker visualizations using Gemini assistance when they also have a Looker role that contains the `can_override_vis_config` permission.Conversational Analytics with Looker Explore data, even if they don't have a role that contains `explore` permissions, when they also have Looker role that contains the `access_data` permissions on the model that they are querying.  
#### Things to know about permission sets
The following permissions interact with model sets in a potentially unexpected way:
  * `develop`; `see_lookml` — In Looker's IDE, a single project can contain multiple model files. If you assign the `develop` or `see_lookml` permissions to a user, and you've allowed that user to see _any_ model that is a part of a project, they will be able to develop or see the LookML for _all_ models in that project. However, they will still not be able to _query_ models that you have not allowed.
  * `manage_models` — If you assign the `manage_models` permission to a user, the user will be able to access all models in all projects in the instance.
  * `manage_modelsets_restricted` — If you assign the `manage_modelsets_restricted` permission to a user, they can assign any model in a project to which they have access.
  * `manage_project_connections` — If you assign the `manage_project_connections_restricted` or `manage_project_connections` permissions to a user, the user will be able to see, edit, and create project-scoped connections for any projects that are included in the model set.


## Model sets
A model set defines what data and LookML fields a user or group can see. Each set is a list of LookML models to which a user or group should have access. You can think of a model set as performing two functions:
  1. A model set controls which models in your LookML the permissions apply to (if those permissions are model specific).
  2. A model set limits what data and LookML fields a user can see, because each model is connected to a specific database connection and contains certain LookML fields.


### Creating a model set
To create a model set:
  1. Click the **New Model Set** button at the top of the **Roles** page.
  2. Looker displays the **New Model Set** page. Enter a name for the new model set.
  3. Select the model or models that should be included in the new model set.
  4. Click the **New Model Set** button at the bottom of the page. The new model set will appear in the **Model Sets** section of the **Roles** page.


> Models that are included in pending projects appear in the **Models** list on the **New Model Set** and **Edit Model Set** pages.
> renamed, we recommend that Looker admins also remove that model's name from any associated model sets, using the **Edit Model Set** page. Removing a deleted model's name from a model set prevents a new model with the same name from unintentionally being included in that model set.
To learn more about models, see the Model parameters documentation page.
#### Creating multiple models and model sets
The following example illustrates how you can use multiple model sets to limit access to data. Consider a scenario where you have two teams, Marketing and Support. In this example, these two teams should not have access to the entire model, so you would create a separate model for each team. To separate their data access, you would perform the following steps:
  1. Copy the model into two new models.
  2. In the first of the new models, include only the views, fields, and Explores that the Marketing team should have access to.
  3. Create a model set for the Marketing team that includes only this new model.
  4. Create a new role for the Marketing team that includes this new model set and the appropriate permissions for the Marketing team.
  5. Assign this new role to the Marketing team group.
  6. Repeat steps 2 through 5 to configure the second model for the Support team.


### Editing a model set
After a model set has been created, perform the following steps to edit it:
  1. On the **Roles** page, click the **Edit** button to the right of the model set you want to edit.
  2. Looker displays the **Edit Model Set** page. If desired, enter a new name for the model set in the **Name** field.
  3. Add or remove any models from the model set in the **Models** section.
  4. Click the **Update Model Set** button at the bottom of the page.


> Models that are included in pending projects appear in the **Models** list on the **New Model Set** and **Edit Model Set** pages.
> renamed, we recommend that Looker admins also remove that model's name from any associated model sets, using the **Edit Model Set** page. Removing a deleted model's name from a model set prevents a new model with the same name from unintentionally being included in that model set.
### Deleting a model set
To delete a model set, on the **Roles** page, click **Delete** to the right of the model set that you want to delete.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


