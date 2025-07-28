# Deleting personal user information  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/deleting-personal-user-information

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Option 1: Overwrite personal information
  * Option 2: Delete the user
  * Deleting the user's Git activity
  * SSO authentication considerations




Was this helpful?
Send feedback 
#  Deleting personal user information
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Option 1: Overwrite personal information
  * Option 2: Delete the user
  * Deleting the user's Git activity
  * SSO authentication considerations


There are two methods to delete a user's personal information.
## Option 1: Overwrite personal information
It is best practice to disable users, rather than delete them, to maintain user history and content. For details, see the Removing User Access documentation.
  1. Go to the Users page in Looker's **Admin** panel.
  2. Select the **Sudo** button to the right of the user's information to impersonate the user.
  3. Go to the user's **Account**.
  4. Delete or overwrite any user changeable **User Attributes** that contain personal information. These do not always appear on the user admin page.
  5. Select **Save**.
  6. Select **Stop Sudoing** in the red bar at the top of the screen.
  7. Go back to the Users page in Looker's **Admin** panel.
  8. Select **Edit** to see the user's details.
  9. Change the user's account to Disabled.
  10. Overwrite the **First Name** to something else, like "disabled-user-1".
  11. Overwrite the **Last Name** to something else, like "disabled-user-1".
  12. Overwrite the **Email** to something else, like "disabled@user-1.com".
  13. Delete or overwrite any **User Attributes** that contain personal information. If an attribute's source is "System setting" you can't change it directly. Looker will update it as you work through this procedure.
  14. Delete or overwrite any **Access Filter Fields** that contain personal information.
  15. Select **Save**.


Be sure to address the user's Git activity.
## Option 2: Delete the user
> Deleting a user is irreversible. Consider your organization's compliance and security needs before doing so.
Looker generally suggests disabling a user. If you delete a user, all of their history and content is erased _and cannot be recovered_. For details, see the Removing User Access documentation.
To delete the user, navigate to the Users page in Looker's **Admin** panel, and then follow these steps:
  1. To see the user's details, select the **Edit** button to the right of the user's information.
  2. Scroll to the bottom of the page and select **Delete**.
  3. Confirm the deletion.


Be sure to address the user's Git activity.
## Deleting the user's Git activity
Looker's developer branch names contain the first and last name of the user. You must delete any Looker user's Git branch.
If you host your Git repo, ask your Git administrator to delete the user's branch.
If Looker hosts your Git repo, contact privacy@looker.com to request that the branch be deleted.
## SSO authentication considerations
If you use a single sign-on (SSO) method — like SAML, LDAP, OpenID, or Google — it is not sufficient to change user information on your SSO provider. Looker stores copies of user information; you must complete the steps described on this documentation page to delete the information within Looker. Removing user information from the SSO provider does not remove API authentication credentials.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


