# Access control and permission management  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/access-control-and-permission-management

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Users and groups
  * Controlling user content access
  * Controlling feature and data access
    * Building blocks you'll need to understand
    * Using the building blocks
  * How content access and permissions interact
    * Viewing data in Looks and dashboards
    * Viewing a folder and lists of Looks and dashboards
    * Modifying a folder
  * Making use of your user permission infrastructure (LDAP, SAML, and OpenID Connect)




Send feedback 
#  Access control and permission management
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Users and groups
  * Controlling user content access
  * Controlling feature and data access
    * Building blocks you'll need to understand
    * Using the building blocks
  * How content access and permissions interact
    * Viewing data in Looks and dashboards
    * Viewing a folder and lists of Looks and dashboards
    * Modifying a folder
  * Making use of your user permission infrastructure (LDAP, SAML, and OpenID Connect)


Looker admins can manage what a user or group of users can see and do in Looker by specifying the following access:
  * **Content Access** , which controls whether a user or group of users can view a folder or manage the folder. A user who can view a folder can navigate to the folder and view the lists of the dashboards and Looks in the folder. A user who can manage a folder can manipulate the contents of a folder (copying, moving, deleting, and renaming dashboards and Looks), organize the folder itself (renaming, moving, or deleting the folder), and give other users and groups access to the folder. Content access is managed by Looker admins in the **Admin** panel or, if allowed, by individual users from within the folder.
  * **Data Access** , which controls which data a user is allowed to view. Data access is primarily managed using **Model Sets**, which make up one half of a Looker role. These roles are then applied to users and groups. Data access can be further restricted within a model using access filters to limit which rows of data they can see, as though there was an automatic filter on their queries. You can also restrict access to specific Explores, joins, views, or fields using access grants.
  * **Feature Access** , which controls the types of actions a user is allowed to do in Looker, including viewing data and saved content, changing the LookML models, administrating Looker and so forth. Feature access is managed by **Permission Sets**, which make up the other half of a Looker role. Some of these permissions apply to the entire Looker instance, such as being able to see all schedules for sending data. Most permissions are applied to specific model sets, such as being able to see user-defined dashboards based on those models.


Data access, feature access, and content access for users and groups combine to specify what users can do and see in Looker.
## Users and groups
In Looker there are both individual users and groups of users. Users are managed on the **Users** page of Looker's **Admin** panel, while groups are managed on the **Groups** page of Looker's **Admin** panel.
The best practice is to use groups to avoid the tedium of assigning, adjusting, and removing controls for users individually. Typically the combination of activities to allow for a user can be arranged by having that user belong to one or more groups. If no combination of groups is enough, consider creating a group with only one user, which lets you potentially expand that group to more people in the future. For access filters, consider using user attributes since you can assign user attributes to groups.
## Controlling user content access
Looker folders let you organize sets of dashboards and Looks. They can also contain other folders, facilitating a nested hierarchy of organization.
Folders let you set access levels that determine which users may edit folder contents (such as Looks and dashboards), view the contents in a folder, and change settings:
  * A user needs to have at least the **View** access level to a folder to see that the folder exists, to view the Looks and dashboards inside it, and to copy the Looks and dashboards in the folder.
  * A user needs to have the **Manage Access, Edit** access level for a folder to manage access to the folder and to edit the folder and its content (including renaming folders, moving content, and deleting Looks and dashboards).


Folders do _not_ otherwise control what users can do on the Looker platform, or which data they can use to build their own content. To manage that level of access, see the Controlling Feature and Data Access section on this page.
The step-by-step instructions for adjusting folder access levels for users who are browsing content in Looker are discussed on our Organizing and managing access to content documentation page. Looker admins can also adjust folder access levels for all groups and users from the **Content Access** page of Looker. You can also view the Designing and configuring a system of access levels documentation page for information about instance-wide access level design.
Although content access is managed separately from feature access, the role that is assigned to a user can affect whether they can see Looks and dashboards listed in a folder, view a Look or dashboard, or manage a folder. The How content access and permissions interact section of this page describes how feature access affects content access in more detail.
## Controlling feature and data access
To control feature and data access in Looker, you usually create a group of users (this is optional, but recommended) and assign that group to a role. A role ties together a set of permissions with a set of LookML models. The models themselves define which fields and data is available.
You can apply specific data limits to specific users with access filters. And, you can limit Looker developers to working with models based on particular databases by using projects.
You can also control access to specific Explores, joins, views, or fields by creating access grants. Access grants limit access to only users that have been assigned specific user attribute values.
If you want to achieve this ... | These are the basic steps you'll take ...  
---|---  
Control the actions a user can perform | Create a permission set with the appropriate permissions, then assign a group or user to a role with that permission set  
Control what fields a user can access | Create a model with the appropriate fields, then assign a group or user to a role with that model  
Control what data a user can access | Create a model with the appropriate data limitations, then assign a group or user to a role with that model _- or -_access filters to limit a user to the appropriate data _- or -_user attributes to provide differing database credentials to a group or user _- or -_access grants to restrict access to specific Explores, joins, views, or fields  
Control what database connections a Looker developer can access | Create a project with the appropriate connections, associate the project with a set of models, then assign a group or user to a role with those models  
Feature access can also affect content access. See the How content access and permissions interact section of this page for more details on how data access and feature access affect content access.
### Building blocks you'll need to understand
#### Roles
A role is a combination of one permission set and one model set. A permission set is composed of one or more permissions, and it defines what the role may do. A model set is composed of one or more models, and it defines which LookML models the role applies to.
After you create a role you can assign an individual user, or a group of users, to that role. If you add some roles to an individual user, and other roles to a group that the user belongs to, the user will inherit all of those roles put together.
Some permissions are relevant to your entire Looker instance, others only apply to the models within the same role. See the Roles documentation page for more information.
#### Projects
Projects let you restrict which database connections may be used by which models. This can help you control which sets of data your Looker developers can interact with when they are creating models. A project may contain one or more models, and it may be configured to use one or more connections.
This restriction defined through projects also flows through to the Looker SQL Runner, which ensures that your developers cannot get access to prohibited database connections by using SQL Runner.
#### User attributes
User attributes let you assign arbitrary values to groups of users or individual users. These values are then used as inputs to various parts of Looker, customizing experiences for each user.
One way user attributes control access is by parameterizing database credentials to be specific to each user. This only has value if your database has multiple users with varying data access. See the User attributes documentation page for more information.
Another way user attributes control access is as part of access filters. Access filters let you utilize one or more user attributes as a data filter. For example, you might want to assign each user a company name, then make sure any content they see is filtered by that name. For a description of how to apply access filters, see the User attributes documentation page and the `access_filter` parameter documentation page.
User attributes also control access grants. An access grant specifies a user attribute and defines allowable values in that user attribute to grant access to an Explore, join, view, or field. You then use the `required_access_grants` parameter at the Explore, join, view, or field level to restrict access to those LookML structures to only those users who have the allowed user attribute values. For example, you could use an access grant to limit access to the `salary` dimension to only those users who have the value `payroll` in their **`department`**user attribute. For a description of how to define access grants, see the`access_grant` parameter documentation page.
### Using the building blocks
#### Control feature access
Permissions control the types of activities that a user or group can do. This is how a user can get permissions:
  1. The best practice is to identify one or more groups of users that should have a permission set, creating a group if necessary. You can give permissions to individual users if you choose.
  2. Create a permission set that contains the appropriate permissions.
  3. If some of the permissions to be assigned are model-specific, create or identify an existing model set.
  4. Create a role that combines the permission set and, if necessary, the model set.
  5. Assign the role from the **Roles** page. After the role exists, you also can assign the role to a user on the **Users** page.


You can assign multiple roles to a user or group. In that case, users will have all the permissions from all the roles they have. For example:
  * Role1 gives the ability to see dashboards on Model1.
  * Role2 gives the ability to see dashboards and to explore on Model2.


If you assign both roles to the same group of users, then they can see dashboards on both Model1 and Model2 but only can explore on Model2.
#### Control user access to Looker fields
The fields that a user can work with are controlled by the models that the user can access. This is how a user can get field access:
  1. Create a LookML model (or combination of LookML models) containing only the fields a user should have access to.
  2. Go to **Admin > Users > Roles**.
  3. On the **Roles** page, create a model set that contains those models and then assign it to a role.
  4. To work with groups of users, which is generally considered a best practice, create a group on the Looker **Groups** page. Then assign that group to the appropriate roles on the **Roles** page.
  5. To work with individual users, assign roles to those users from either the **Users** page or the **Roles** page.


You can assign multiple roles to a user or group. Users can then work with all models from all the roles that they have.
It's important to note that the `hidden` parameter for fields is designed to create cleaner experiences for users, not to control field access. The `hidden` parameter hides fields from the field picker, but it won't prevent a user from ever using that field. If someone sends them a link that uses that field they can see it, and other places in Looker will still show the field.
#### Control user access to data
There are several ways to control a user's access to data, depending on the use case:
  * To prohibit users from seeing certain _columns_ of data, control the fields that they can access, as described in the **Control user access to Looker fields** section. As long as a user cannot develop, and cannot use SQL Runner, they are constrained by the fields that they have access to.
  * To prohibit users from seeing certain _rows_ of data, apply access filter fields, as described on the `access_filter` parameter documentation page.
  * To limit access to specific Explores, joins, views, or fields, create access grants that limit access to only those users who are assigned the allowed user attribute values, as described on the `access_grant` parameter documentation page.
  * To limit _Looker_ users to running queries on a specific _database_ user, which your database team has configured to limit data access, use user attributes. They allow you to parameterize your database connection so that a group of users or individual users run their queries with specific database credentials. You should consider limiting users to the proper Looker fields as well. If you don't, the Looker user may try to query a field that their database user doesn't have access to, and they'll receive an error.


Just like the `hidden` field parameter is not intended for controlling field access, the `hidden` parameter for Explores does not prevent all users from viewing an Explore. The `hidden` parameter removes the Explore from the Explore menu, but if a user has saved content that references a hidden Explore, they will still have access to the Explore's data.
> If you are using signed embedding, be sure to configure data access controls through the signed embed URL.
#### Control developer access to database connections
Unlike regular users, Looker developers are not fully constrained by models and access filters, because they can make additions or changes to LookML models. However, admins can still limit Looker developers to certain database connections by using projects. To do so:
  1. Create a project that restricts a certain number of models to a certain number of database connections. This is done on the Looker **Manage Projects** page.
  2. Go to **Admin > Users > Roles**.
  3. On the **Roles** page, create a model set that contains at least one of the models in the project, and then assign it to a role.
  4. To work with groups of users, which is generally considered a best practice, create a group on the Looker **Groups** page. Then assign that group to the appropriate roles on the **Roles** page.
  5. To work with individual users, assign roles to those users from either the **Users** page or the **Roles** page.


> If a Looker developer can see _any_ model that is part of a project, they will be able to view _all_ models that are a part of that project. For example, this could happen if you assigned a Looker developer to a role with only one model, but that model happened to be a part of a project that contained other models.
## How content access and permissions interact
Content access is managed by users when they are viewing a folder, or managed by a Looker admin on the **Content Access** page in the **Admin** panel. The roles that are assigned to a user determine the user's feature and data access. This affects what the user can do in a folder and whether they can view Looks and dashboards.
### Viewing data in Looks and dashboards
To view a Look or dashboard's data, the user must have at least **View** access to the folder where the content is stored.
Users must have `access_data` and `see_looks` permissions to select a Look and view its data. Users must have `access_data` and `see_user_dashboards` permissions to select a dashboard and view its data.
To see the data in a Look or dashboard tile, the user must have access to that data. Without the necessary data access:
  * Even if the user can see a Look listed in a folder and can navigate to the Look, the Look's query is not run and the user can't see the Look's data.
  * Even if the user can see a dashboard listed in a folder and can navigate to the dashboard, any tile where the user doesn't have access is displayed as blank. If a dashboard that has tiles created from multiple models, a user will be able to see the tiles associated with models they have access to, and the tiles from other models will display an error.


For example, a user who has **View** access for a folder, data access for the data underlying all Looks in the folder, and both `access_data` and `see_looks` permissions can see a list of all Looks in the folder and can also view those Looks. If this user does not have access to see LookML or user-defined dashboards, the user would not see any dashboards that may exist in the folder.
### Viewing a folder and lists of Looks and dashboards
A user needs at least the **View** access level to a folder to view that folder and see the list of content stored inside that folder.
Users who also have at least `see_looks` permission can see the titles of Looks in the folder. Users who also have at least `see_user_dashboards` permission can see the titles of dashboards in the folder. However, this does not imply that they can view the data of the Looks or dashboards.
For example, a user who has the `see_looks` permission but lacks `access_data` permission can see the titles of Looks but can't view the Look's data.
Users that have the `access_data` permission, but don't have either the `see_looks` or `see_user_dashboards` are not be able to see any folders or any content.
### Modifying a folder
A user needs to have the **Manage Access, Edit** access level for a folder to be able to organize that folder, including copying and moving content, renaming and moving folders, and similar actions. Users must also have the `manage_spaces` permission to create, edit, move, and delete folders.
## Making use of your user permission infrastructure (LDAP, SAML, and OpenID Connect)
If you already have an LDAP, SAML or OpenID infrastructure setup, you can use that system to manage user logins. The instructions for setting up LDAP can be found on the LDAP authentication page. The instructions for setting up SAML can be found on the SAML authentication documentation page. The instructions for setting up OpenID Connect can be found on the OpenID Connect authentication documentation page.
If you've configured groups in your LDAP, SAML, or OpenID Connect implementation, you can also use those groups within Looker. However, there are a few things to keep in mind:
  * Any groups you've created automatically transfer into Looker, and will be visible on the **Groups** page. One Looker group will be created for each LDAP, SAML, or OpenID Connect group, and the Looker group name will mirror the LDAP, SAML, or OpenID Connect group name.
  * You'll be able to use these Looker groups to assign access levels for folders and user attributes to members of the groups.
  * You will _not_ be able to use Looker groups to configure roles like you would with a manually created group. Instead, you'll map your LDAP, SAML, or OpenID Connect groups to Looker roles during the setup process, and will only be able to change assigned roles from the LDAP, SAML, or OpenID Connect setup pages. We've required this approach so that your LDAP, SAML, or OpenID Connect groups remain your single source of truth. Without this restriction, group to role mapping could diverge from their intended function in your LDAP, SAML, or OpenID Connect scheme.


You may also use LDAP to apply user-specific database connections to Looker queries, as described on the LDAP authentication documentation page.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


