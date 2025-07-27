# Groups - Lightdash

**Source:** https://docs.lightdash.com/references/groups

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Reference
Groups
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference
    * Roles and permissions
    * Personal access tokens


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Creating groups
  * Editing groups
  * Deleting groups
  * Adding roles to groups
  * Assigning user attributes to groups
  * Using OKTA to manage groups in Lightdash


**Groups are only available on Lightdash Cloud Pro and Enterprise plans.** For more information on our plans, visit our pricing page.
To view and manage your groups, go to the `Organization Settings` > `Users & groups` tab. Only users with an `organization admin` role can manage groups.
##  Creating groups
To create a new group, go to `Organization Settings` > `Users & groups` > `Add group`. You can name your group and add users in your organization to the group. By default, newly created groups don’t have access to anything.
##  Editing groups
To edit a group, click on the edit button to the right of a group in the list. You can add or remove users from a group and change the group name. To remove someone from that group, click on the `x` to the right of the group member.
##  Deleting groups
To delete a group, click the delete icon to the right of a group in the list to remove it.
##  Adding roles to groups
To assign a role to a group, use the `Project access` page in the `Organization settings` menu. From there, you can assign a group or groups to a role which determines their access to the project. For more information, see the Project roles page.
##  Assigning user attributes to groups
You can assign user attributes to groups as well as individual users. To learn more about managing data access for groups using user attributes, check out the user attributes docs here.
##  Using OKTA to manage groups in Lightdash
**This feature is deprecated and will be removed in a future release.** For more information on how to provision users and groups in Lightdash, see the SCIM integration documentation.
If your Lightdash instance is configured to use OKTA as an authentication provider, then users will automatically be assigned to the same groups in Lightdash as they are in OKTA. See the guide to setting up OKTA for more information on setting the correct environment variables as well as Okta configuration: with/without custom authorization server.
Note that users will only be assigned to groups that exist in Lightdash (groups won’t be created automatically) and exactly match the name of the group in OKTA.
To manage groups in Lightdash using OKTA, you’ll need to:
  1. Setup groups in your directory in OKTA
  2. Allow groups to login in to Lightdash from Okta
  3. Finally for group sync to work you need to configure Okta to share groups with Lightdash


Roles and permissionsUser Attributes
Assistant
Responses are generated using AI and may contain mistakes.


