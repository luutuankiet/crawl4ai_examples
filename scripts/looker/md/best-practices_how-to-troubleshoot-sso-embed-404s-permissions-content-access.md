# Troubleshooting signed embed 404s, permissions, and content access  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-sso-embed-404s-permissions-content-access

Skip to main content 

Console 


  * On this page
  * Troubleshooting the error
    * 1. Verify that the content path is correct
    * 2. Verify that the content exists
    * 3. Verify the embed URL's permissions
    * 4. Verify the user's content access




Was this helpful?
Send feedback 
#  Troubleshooting signed embed 404s, permissions, and content access
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Troubleshooting the error
    * 1. Verify that the content path is correct
    * 2. Verify that the content exists
    * 3. Verify the embed URL's permissions
    * 4. Verify the user's content access


When a user attempts to access embedded content, they may see the following error message: 
> The dashboard you requested could not be found. It either doesn't exist or you don't have permission to view it. 
This page addresses how to troubleshoot this error and avoid it in the future, saving developers and users time and frustration. 
## Troubleshooting the error
The error message provides you with next steps on what to verify. Essentially, the signed embed URL successfully created and authenticated the embed user, but one of two things has gone wrong: 
  * The path to the content is broken. 
  * The permissions and content access specified in the embed URL don't allow the embed user to view the embedded content. 


The Embed URI Validator on the **Embed** page in the **Platform** section of the **Admin** panel is a tool that is commonly used to troubleshoot embed URLs. However, because the validator only verifies that the embed URL is valid and can complete the authentication step, you can take the following troubleshooting steps to confirm which of the two problems is occurring: 
  1. Verify that the content path is correct.
  2. Verify that the content exists.
  3. Verify the embed URL's permissions.
  4. Verify the user's content access.


### 1. Verify that the content path is correct
Use this method to determine if the path to the content is broken. Depending on the method used to generate the signed embed URL, the location where the content path is specified can vary. In most scripts, there is a section that defines the path. For example, to embed a dashboard with the name **123** , you would use the path `/embed/dashboards/123`. 
Use the examples in the Embed URL section of the Signed embedding documentation page to confirm that the path is defined correctly. 
If you're using the `Create Signed Embed Url` API endpoint to generate the URL, the **Target URL** parameter for the same dashboard would look like this:
> `https://instance_name.looker.com<:optional_port>/dashboards/123`
Double-check that the path is defined correctly in the embed URL generation script. 
### 2. Verify that the content exists
After verifying that the content path is correctly defined, have an admin confirm that the content exists at that path. Admins by default bypass content access and permissions restrictions that might prevent a developer, for instance, from seeing the content. If an admin cannot see the content at that path, then it doesn't exist at that path. 
If the admin can see the content at that path, then it is likely that the correct permissions or content access has not been granted to the embed user. To determine if this is the case, an admin can find the user on the Users page in the **Admin** panel, and select the inline **Sudo** option. 
Sudoing as another user enables admins to see what the user sees with their given permissions, content access, and user attributes. If, while sudoing as the embed user, the admin can no longer see the content, you will need to take further steps to troubleshoot the user's permissions and content access. 
Once you have verified that the content exists and that the embed user cannot see it, the next steps are to check the embed URL's permissions and the user's content access, either of which, if configured incorrectly, can block the user from seeing the embedded content. 
### 3. Verify the embed URL's permissions
This next step lets you determine if the permissions specified in the embed URL don't allow the embed user to view the embedded content. Permissions in Looker are additive, and a combination of many permissions is needed for users to view content. For example, when viewing an embedded user-defined dashboard, at a minimum an embed user needs the `access_data`, `see_looks`, and `see_user_dashboards `permissions to view it. For this step, double-check the permissions given to embed users in the URL definition, and determine if any permission's dependencies are missing. Then check the roles the user is assigned in the embed URL. 
An embed user's role can be created in one of two ways: with the permissions and model set access in the signed embed URL, or with the groups to which a user is assigned, if those groups have any roles associated with them. Roles created in either of these two ways are **additive** , the same way that roles in the regular Looker environment are. Check the group or groups to which the the embed user is assigned in the URL specifications (and the group's or groups' inherited roles). 
> **Tip:** Keeping embed users' permissions and model access information in one place (either a Looker group's role assignment, or a signed embed URL specification) reduces the number of extra variables you need to check when you're troubleshooting user issues. For example, if a company leverages roles associated with group IDs when assigning embed user permissions, in addition to defining permissions in the signed script, the embed user information is stored both in Looker and in the parent application (via signed URL script), rather than in one or the other. Sometimes, Looker admins who manage roles for embed users don't have access to the embed URL generation script in the parent application and cannot troubleshoot thoroughly. In this case, it may be helpful to pass an empty array for the permissions and models parameters and to control roles exclusively through group assignments. 
Next, confirm that the specified or inherited roles and permissions are correctly assigned to the user by finding the user on the Users page in the **Admin** panel and selecting **View**. 
One thing to note is that embed users don't have access to all the permissions a regular Looker user has — see the full list of embed permissions on the Signed embedding documentation page. 
### 4. Verify the user's content access
After confirming that the embed user has the correct permissions and role assignments, you need to check the user's content access. To do this, verify the following information: 
  * What folder is the embedded content saved in? 
  * Does the embed user, or the group to which the embed user is assigned, have access (`View or Manage, Edit`) to this folder? 


The quickest way to confirm in which folder the content is saved is to view the content in the regular Looker environment and then find the folder name in the content header. After navigating to that folder, select the gear icon in the top right corner under **Manage Access**. You can quickly determine if a content-access issue is causing the 404 error by granting the specific embed user `View` access to the folder. 
If the embed user (or the group they've been assigned to with signed embed group IDs) has not been given access, the user will be unable to see any content that's been saved in the folder. Admins (or non-admins who have been granted `Manage Access, Edit` permissions to the folder) can make changes to the content access settings at this point to add the embed user or user group. 
A common complication can occur when a dashboard has been duplicated and exists in multiple folders. Each copy of a dashboard has a unique ID, so make sure the dashboard that is being embedded has the same ID as the dashboard that users are expecting to access — you can verify the ID in the dashboard's URL, in the following format: 
> `~/embed/dashboards/<specific_content_id>`
####  Closed systems 
Closed systems are a special case when it comes to checking content access. A closed system silos saved content for individual groups. Implementing a closed system is often recommended as a best practice for every Powered By Looker deployment (embedded analytics). The main benefit of this system is that it completely removes the **All Users** group, sets all personal folders to private, and prevents users from seeing other users or their content in the instance (unless all the users share a group). This effectively creates a multi-tenant instance for multiple clients so that they cannot access other users' content or information unless they're explicitly granted access. 
Double-check that the affected embed user is a part of the correct Looker groups; otherwise, they will be unable to view any of their organization's content. 
If you would like to enable a closed system for your instance, contact a Google Cloud sales specialist or open a support request. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


