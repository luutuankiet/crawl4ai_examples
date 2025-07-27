# Designing and configuring a system of access levels  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/access-levels

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Types of access to folders
  * Open and closed systems of access to folders
  * How access to a folder affects its subfolders
  * Configuring a completely open system
  * Configuring an open system with restrictions
    * Plan out your structure
    * Configure groups to provide granular access
    * Change the All Users group's access to View on the Shared folder
    * Remove the All Users group from folders you don't want viewable
  * Configuring a closed system
    * Ask for the Closed System option
    * Plan out your structure
    * Configure groups to provide granular access
    * Enable the Closed System option in the Admin panel
    * Give each company group View access for the Shared folder
    * Configure access levels for each subfolder
    * Migrate content into subfolders




Send feedback 
#  Designing and configuring a system of access levels
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Types of access to folders
  * Open and closed systems of access to folders
  * How access to a folder affects its subfolders
  * Configuring a completely open system
  * Configuring an open system with restrictions
    * Plan out your structure
    * Configure groups to provide granular access
    * Change the All Users group's access to View on the Shared folder
    * Remove the All Users group from folders you don't want viewable
  * Configuring a closed system
    * Ask for the Closed System option
    * Plan out your structure
    * Configure groups to provide granular access
    * Enable the Closed System option in the Admin panel
    * Give each company group View access for the Shared folder
    * Configure access levels for each subfolder
    * Migrate content into subfolders


Different levels of content access determine which users may view and edit content in Looker folders. Whereas **permissions** are associated with a user according to that person's role, _content access_ is associated with a folder, and defines how open the folder is to users at various levels.
## Types of access to folders
One of two access levels can be assigned to each Looker user or group for any given folder:
  * **View** : With this access level, a user can see that the folder exists, can view the Looks and dashboards inside it, and can copy the Looks and dashboards in the folder.
  * **Manage Access, Edit** : This access level lets a user do everything that the **View** access level does, plus make changes to the folder, such as the following:
    * Editing Looks and editing dashboards in the folder
    * Specifying which users and groups of users can view or manage the folder
    * Creating subfolders
    * Renaming, moving, and deleting a folder
    * Moving Looks and dashboards
    * Deleting Looks and dashboards


For additional discussion of content access and permissions, see Controlling user content access and How content access and permissions interact.
## Open and closed systems of access to folders
Looker's settings will help you structure user access based on your company's policies and the kinds of users who will be interacting with your folders. In general, the system you devise will fall into one of three broad categories: completely open, open with restrictions, or closed.
Level of Access to Folders | Description | Recommended Use  
---|---|---  
Completely open | All users can view and modify all shared content. This is Looker's default configuration. | An open system is recommended for small companies or teams using Looker, companies with open policies about data, and companies where sharing editable reports is a primary use case.  
Open with restrictions | Access to shared content is restricted in some way so that either only some people can edit certain content, or some content is entirely invisible to certain people. | An open system with restrictions is recommended for medium-sized or larger teams and companies, highly diversified user bases where reports aren't relevant to everybody, or companies that want content to be viewable by everybody but editable by only a few.  
Closed | Also called a multitenant installation, this system silos content to certain groups and prevents users from different groups from knowing about each other. | To safeguard your customers' private information, we strongly recommend the use of a closed system for private label and signed embed use cases where customers host clients into the system who may be from different companies or groups and who shouldn't know about one another.  
Once you determine what kind of system you want, this page will walk you through the steps to configure it. For the initial setup, we recommend using the **Content Access** section of the **Admin** panel, as it's a single place to make changes to each folder.
## How access to a folder affects its subfolders
Before you decide how open or closed you want your system to be, it's important to understand how the access levels you set in parent folders will affect their subfolders, as well as what you can and can't change at lower levels in the hierarchy.
Access Type | Inheritance Pattern | Description  
---|---|---  
Manage Access, Edit | Flows all the way down the folder hierarchy | Once you give a user access to **Manage Access, Edit** in a folder, they will retain that access level to all Looks, dashboards, and subfolders within that folder. You won't be able to lock down their access at a lower part of the folder hierarchy.  
View | Can be removed at any point down the folder hierarchy | Removing **View** access at the folder level revokes a user's ability to see that folder and all its content. You can also remove **View** access at any point lower in the hierarchy to restrict users from viewing specific Looks, dashboards, or subfolders within an otherwise viewable folder.  
Looker admins have **Manage Access, Edit** access to all folders and therefore all content. This ensures their ability to manage the system, prevent orphaned content, and assist any user who runs into issues.
## Configuring a completely open system
Looker's default configuration allows completely open access to all folders. The **All Users** group is assigned to **Manage Access, Edit** on the Shared folder, and all subfolders within the Shared folder will inherit that access from it. Manage this setting from the **Content Access** section of the **Admin** panel.
Once a user has **Manage Access, Edit** access to a folder, they also have **Manage Access, Edit** access to all content in that folder, including all subfolders under it. That means there are no restrictions on content access in this system.
Personal folders exist in a separate hierarchy, and they also have default settings. The **All Users** group is set to **View** on all personal folders. Each user can choose to remove this group from their personal folder if they want their personal folder to be private.
## Configuring an open system with restrictions
These steps will help you configure an open system with restrictions:
  1. Plan out your structure.
  2. Configure groups to provide granular access.
  3. Change the **All Users** group's access to **View** on the Shared folder.
  4. Remove **All Users** from any folder you don't want viewable by the whole company.


### Plan out your structure
Who do you want to allow to view and edit particular folders? It will make your life easier if you sketch out your plan _before_ you start configuring access. This also gives you a place to check off changes as you go through the process, so you don't have to go back to check on various folders. Placing users into groups will help you manage access for different departments or teams within your company.
One of the most common configurations is to have one folder per department or team, which looks something like this:
  * Within your Shared folder, create a folder for a department, team, or project. We'll use the example of a Finance team in this section.
  * Give the CFO (or the main analyst for Finance) the **Manage Access, Edit** access on that folder. Give the rest of the team **View** access.
  * Create two subfolders: One for editable content and one for read-only content. If needed, add a third subfolder for private content.
  * In the subfolder for editable content, grant **Manage Access, Edit** access to the whole Finance team using a Finance group. Once you give the Finance group that level of access, all of its members can add, delete, or change content in that subfolder.
  * In the subfolder for read-only content, grant **View** access to the whole Finance group. The CFO is still able to **Manage Access, Edit** content in this folder, because they inherit that access from the main Finance folder.
  * In the (optional) private subfolder, remove the Finance group completely. Only the CFO can see this folder or manage its content.


### Configure groups to provide granular access
If you're planning to restrict access to content, Looker groups make things much easier. Groups can be granted access to folders and subfolders the same way that users are, and groups can contain other groups. For information about how to configure groups, see the Groups page.
_Start by setting access to individual subfolders first, and then work your way up to setting access for the whole Shared folder._ Because access flows down the hierarchy of folders, it's safest to begin by manipulating the access to the lowest subfolders individually. Then you can move up through parent-level folders, giving them the access level you want and making sure that your changes don't conflict with decisions you have made at the lower levels.
In this example, we'll start with the subfolders inside of the Shared folder. Manage these settings from the **Content Access** section of the **Admin** panel:
  1. Set each folder within the Shared folder to **A custom list of users**.
  2. Assign **Manage Access, Edit** access to the users and groups that you want to be able to edit content.
  3. Assign **View** access to the users and groups that you want to have read-only access.


Until you change the settings for the top-level Shared folder, nothing goes into effect. The access level for the **All Users** group is set to **Manage Access, Edit** in the Shared folder and flows down through all individual subfolders. You cannot modify the settings for **All Users** in individual subfolders until the access level for that group is changed in the Shared folder.
Click on the folder that you want to configure, and then click **Manage Access**.
### Change the **All Users** group's access to **View** on the Shared folder
This is when your changes go into effect. Remember to consult the plan for your structure.
First, unless you want everyone to have editing access to all content in your system, click **Manage Access** for the Shared folder and change **All Users** from **Manage Access, Edit** to **View**.
Then, if your plan is to display certain subfolders only to certain groups, continue to the following section.
### Remove the **All Users** group from folders you don't want viewable
To make a folder private to a certain subgroup of users, remove **All Users** completely from those folder using the `X` to the right of the folder's access level. Now the folder will only appear for users and groups that you explicitly list.
## Configuring a closed system
Looker offers a **Closed System** option that makes the following changes:
  * Removes the **All Users** group. There will be no way to refer to all the users in the system as one group. Instead, Looker admins should create one group per tenant, or customer, as discussed in the Configure groups to provide granular access section. For this discussion, we'll assume that each customer is a company.
  * Makes all user folders private by default. Users can still choose to share content in their folders with other members of their groups.
  * Prevents users from seeing other users unless they share a group. So, if a user is a member of the Company C group, that user will only see other members of Company C, and not the members of Companies A and B.
The Homepage: Recently Viewed Content is an example of a place in Looker where that user will only see other Company C members and their content.


These steps will help you configure a closed system:
  1. Ask for the **Closed System** option.
  2. Plan out your structure.
  3. Configure groups to provide granular access.
  4. Enable the closed system in the **Admin** panel.
  5. Give each company group in your system **View** access for the Shared folder.
  6. Configure access levels for each subfolder of the Shared folders.
  7. Migrate content into subfolders.


_These steps assume that no content for multitenant users is housed in the Shared folders. To silo content under a closed system and prevent customers or other groups from seeing each other, move any such content out of the Shared folder and into separate subfolders before you begin the following steps._
### Ask for the Closed System option
To request that the **Closed System** option be enabled for your instance, contact a Google Cloud sales specialist or open a support request.
### Plan out your structure
It makes setting up your system much easier if you have set up your plan in advance. There are two main areas to think about:
First, be sure to create a group for each company. A company group associates all users from each company together, and keeps those users separate from other companies.
Second, consider whether you'll want to have multiple companies looking at the same folder (for example, for dashboards that are relevant to all companies), or whether you'll want one top-level folder for each company (for distinct content that only applies to a single company).
### Configure groups to provide granular access
While there should be at least one group per company, there may also be subgroups within that larger group. If you would like to allow some users at a company to edit and manage content while allowing others to only view content, you can create separate subgroups for the different types of users. For example, you can start by creating **Company A** as the umbrella group and then add two subgroups: **Editors at Company A** and **Viewers at Company A**.
For information about how to configure groups, see the Groups documentation page.
### Enable the Closed System option in the **Admin** panel
It's best to enable the **Closed System** option before setting up any access controls on folders, since enabling the **Closed System** option makes changes to your system (see the introduction to Configuring a closed system on this page). This option is located in the **Settings** section of the **General** panel in Looker's **Admin** section.
### Give each company group View access for the Shared folder
Grant **View** access to each company group for the Shared folders. This lets members of those groups access the Shared folder and see their own company's folder within it. If a group does not have **View** access to the Shared folders, they will not be able to see their own company's folders. Manage these settings from the **Content Access** section of the **Admin** panel.
### Configure access levels for each subfolder
Set access levels to establish who can view or edit content in each subfolder. Subfolders default to their parents' access settings until you change them. This means that a company with **View** access to the Shared folder could view content in another company's subfolder unless you restrict access to that subfolder. Review each subfolder and restrict access appropriately.
### Migrate content into subfolders
If your company has allowed users to see their own folder and other personal folders, we recommend migrating any content from those personal folders into the appropriate folders in the main Shared hierarchy.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


