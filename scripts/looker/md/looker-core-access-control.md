# Looker (Google Cloud core) access control with IAM

**Source:** https://cloud.google.com/looker/docs/looker-core-access-control

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * What is Identity and Access Management (IAM)
  * IAM roles versus Looker roles
  * Looker (Google Cloud core) IAM roles




Was this helpful?
Send feedback 
#  Looker (Google Cloud core) access control with IAM
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * What is Identity and Access Management (IAM)
  * IAM roles versus Looker roles
  * Looker (Google Cloud core) IAM roles


Looker (Google Cloud core) uses Identity and Access Management (IAM) to provision user and admin access through a set of IAM roles. For a detailed description of Google Cloud IAM, see the IAM documentation.
## What is Identity and Access Management (IAM)
IAM lets you control who has access to the resources in your Google Cloud project. IAM lets you adopt the security principle of least privilege, so you grant only the necessary access to your resources.
Principals are the "who" of IAM. Principals can be individual users, groups, or Workspace domains. Principals are granted roles, which give them the ability to perform actions with Looker (Google Cloud core) as well as Google Cloud more generally. Each role is a collection of one or more permissions. Permissions are the basic units of IAM: each permission allows a principal to perform a certain action.
For example, the `looker.instances.login` permission lets a principal log in to Looker (Google Cloud core) instances. This permission is included in several predefined roles, including the Looker Admin role (`roles/looker.admin`) and the Looker Instance User role (`roles/looker.instanceUser`).
## Required role
To get the permissions that you need to assign Looker (Google Cloud core) IAM roles, ask your administrator to grant you the Project IAM Admin  (`roles/resourcemanager.projectIamAdmin`) IAM role on the project in which the instance was created. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
## IAM roles versus Looker roles
Two different kinds of roles grant permissions for Looker (Google Cloud core): IAM roles and Looker roles.
  * **Looker IAM roles:** These kinds of roles govern the following abilities:
    * Users' capabilities within the Google Cloud console with regard to Looker (Google Cloud core)
When used together with OAuth, they also govern the following abilities:
    * Users' abilities to sign in to a Looker (Google Cloud core) instance
    * Whether or not users are automatically assigned the **Admin via IAM** Looker role once they sign in to a Looker (Google Cloud core) instance. For more information, see the Authentication and authorization with OAuth and IAM documentation.
See the IAM documentation for information on how to grant IAM roles.
  * **Looker roles:** These kinds of roles govern what users can do once they sign in to a Looker (Google Cloud core) instance. See the Roles and Groups documentation pages for information on how to grant Looker roles.


Looker roles are assigned or revoked within a Looker (Google Cloud core) instance, with the exception of the **Admin via IAM** Looker role, which can be assigned or revoked only through IAM. IAM roles can be assigned or revoked only in the Google Cloud console.
## Looker (Google Cloud core) IAM roles
Three predefined roles for Looker (Google Cloud core) users are available. These roles are granted at the Google Cloud project level and will control access uniformly for all Looker (Google Cloud core) instances within a Google Cloud project. If a user is authenticating with OAuth, the IAM role assigned to each principal also affects which Looker roles are assigned at sign into the instance.
Role Name | Permissions  
---|---  
**Looker Viewer** `(roles/looker.viewer)` Read-only access to all Looker (Google Cloud core) resources in the Google Cloud console. |  looker.backups.get looker.backups.list looker.instances.get looker.instances.list looker.instances.login looker.locations.get looker.locations.list looker.operations.get looker.operations.list resourcemanager.projects.get resourcemanager.projects.list  
**Looker Instance User** `roles/looker.instanceUser` Access to sign in to a Looker (Google Cloud core) instance. |  looker.instances.get looker.instances.login resourcemanager.projects.get resourcemanager.projects.list  
**Looker Admin** `roles/looker.admin` Full access to all Looker (Google Cloud core) resources. |  looker.backups.create looker.backups.delete looker.backups.get looker.backups.list looker.instances.create looker.instances.delete looker.instances.export looker.instances.get looker.instances.import looker.instances.list looker.instances.login looker.instances.update looker.locations.get looker.locations.list looker.operations.cancel looker.operations.delete looker.operations.get looker.operations.list resourcemanager.projects.get resourcemanager.projects.list  
At least one principal must have the Looker Admin (`roles/looker.admin`) IAM role.
If the predefined roles don't provide the set of permissions that you want, you can also create your own custom roles.
## What's next
  * Use Google OAuth for Looker (Google Cloud core) user authentication
  * Manage users within Looker (Google Cloud core)
  * Configure a Looker (Google Cloud core) instance
  * Looker (Google Cloud core) admin settings
  * Administer a Looker (Google Cloud core) instance from the Google Cloud console


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


