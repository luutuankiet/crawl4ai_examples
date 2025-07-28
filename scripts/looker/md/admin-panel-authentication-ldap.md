# Admin settings - LDAP authentication  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-authentication-ldap

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
#  Admin settings - LDAP authentication
Stay organized with collections  Save and categorize content based on your preferences. 
The **LDAP** page in the **Authentication** section of the **Admin** menu lets you configure Looker to authenticate users with Lightweight Directory Access Protocol (LDAP). This page describes that process and includes instructions for linking LDAP groups to Looker roles and permissions.
## Requirements
Looker displays the **LDAP** page in the **Authentication** section of the **Admin** menu only if the following conditions are met:
  * Your Looker instance is not a Looker (Google Cloud core) instance.
  * You have the Admin role.
  * Your Looker instance is enabled to use LDAP.


If these conditions are met, and you don't see the **LDAP** page, open a support request to enable LDAP on your instance.
## Considerations
Keep the following considerations in mind while setting up LDAP authentication on your Looker instance:
  * Looker authentication uses LDAP's "simple" authentication. Anonymous authentication is not supported.
  * You must create a single LDAP user account that has read privileges to user entries and any group entries that will be used by Looker.
  * Looker only reads from the LDAP directory (no writes).
  * Looker can migrate existing accounts to LDAP using email addresses.
  * Looker API usage does not interact with LDAP authentication.
  * If your LDAP server restricts IP traffic, you will need to add Looker's IP addresses to your LDAP server's IP allowlist or inbound traffic rules.
  * LDAP overrides two-factor authentication. If you have previously enabled two-factor authentication, your users will not see the two-factor authentication login screens after you enable LDAP.


### Be careful if disabling LDAP authentication
If you are logged in to Looker using LDAP and want to disable LDAP authentication, be careful to first do _both_ of the following steps:
  * Ensure that you have other credentials to sign in.
  * Enable the **Alternate Login** option on the LDAP configuration page.


Otherwise, you could lock yourself and other users out of Looker.
## Getting started
Navigate to the **LDAP Authentication** page in the **Admin** section of Looker to see the following configuration options.
### Set up your connection
Looker supports transport and encryption with LDAP in the clear and LDAP over TLS. **LDAP over TLS is strongly recommended.** StartTLS and other encryption schemes are not supported.
  1. Enter your **Host** and **Port** information.
  2. Select the box next to **TLS** if you are using LDAP over TLS.
  3. If you are using LDAP over TLS, Looker enforces peer certificate verification by default. If you need to disable peer certificate verification, check **No Verify**.
  4. Click **Test Connection**. If any errors are surfaced, correct them before proceeding.


### Connection authentication
Looker requires access to an LDAP account that is password-protected. The LDAP account should have read access to people entries and to a new set of role entries. The Looker LDAP account does not require write access (nor access to any other aspects of the directory), and it does not matter what namespace the account is created in.
  1. Enter the **Password**.
  2. [Optional] Select the **Force No Paging** checkbox if your LDAP provider does not provide paged results. In some cases, this may help if you are not receiving any matches when searching for users, although it is not the only solution for such a problem.
  3. Click the **Test Authentication** button. If any errors are surfaced, ensure that your authentication information is correct. If your credentials are valid but errors still persist, contact your company's LDAP administrator.


### User binding settings
The details in this section specify how Looker will find users in your directory, bind for authentication, and extract user information.
  1. Set the **Base DN** , which is the base of the search tree for all users
  2. [Optional] Specify a **User Object Class** , which controls the types of results that Looker will find and return. This is useful if the Base DN is a mix of object types (people, groups, printers, and so on), and you only want to return entries of one type.
  3. Set the **Login Attrs** , which defines the attribute(s) your users will use to sign in. These must be unique per user, and something your users are familiar with as their ID within your system. For example, you might choose a user ID or full email address. If you add more than one attribute, Looker will search through both to find the appropriate user. Avoid using formats that could result in duplicate accounts, such as first name and last name.
  4. Specify the **Email Attr** , **First Name Attr** , and **Last Name Attr**. This information tells Looker how to map those fields and extract their information during login.
  5. Set the **ID Attr** , which indicates a field that Looker uses as the unique ID for users. This will generally be one of the login fields.
  6. Optionally, enter an **Optional Custom Filter** , which lets you provide arbitrary LDAP filters that will be applied when searching for a user to bind during LDAP authentication. This is useful if you want to filter out sets of user records, such as disabled users or users who are in a different organization.


### Example
This example ldiff user entry demonstrates how to set corresponding Looker settings:
**Ldiff User Entry**
```
dn: cn=mward,ou=People,dc=example,dc=com
objectClass: person
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: top
cn: mward
userpassword: normal
givenname: Marcus
telephonenumber: +1 408 555 5688
sn: Ward
mail: mward@example.com
ou: People

```

**Corresponding Looker Settings**
```
Base DN: ou=People,dc=looker,dc=com
User Object Class: person
Login Attrs: cn
Email Attr: mail
First Name Attr: givenname
Last Name Attr: sn
ID Attr: cn

```

### Pairing LDAP user attributes with Looker user attributes
You can optionally use the data in your LDAP user attributes to automatically populate values in Looker user attributes when a user logs in. For example, if you have configured LDAP to make user-specific connections to your database, you could pair your LDAP user attributes with Looker user attributes to make your database connections user-specific in Looker.
Note that the LDAP attribute must be a user attribute, not a group attribute.
To pair LDAP user attributes with corresponding Looker user attributes:
  1. Enter the name of the LDAP user attribute in the **LDAP User Attribute** field and the name of the Looker user attribute you want to pair it with in the **Looker User Attributes** field.
  2. Check **Required** if you want to require an LDAP attribute value to allow a user to sign in.
  3. Click **+** and repeat these steps to add more attribute pairs.


### Test user information
  1. Enter a test user's credentials and click the **Test User Authentication** button. Looker will attempt a full LDAP authentication sequence and show the result. Upon success, Looker outputs the user information from the directory plus some trace information about the authentication process which can aid in resolving configuration problems.
  2. Verify that authentication succeeds **and that all fields are mapped correctly**. For example, confirm that the `first_name` field doesn't contain a value that belongs to `last_name`.


## Groups and roles
You can configure Looker to create groups that mirror your externally managed LDAP groups, and then you can assign Looker roles to users based on their mirrored LDAP groups. When you make changes to your LDAP group membership, those changes are automatically propagated into Looker group configuration.
Mirroring LDAP groups lets you use your externally defined LDAP directory to manage Looker groups and users. This, in turn, lets you manage your group membership for multiple software as a service (SaaS) tools, such as Looker, in one place.
If you turn on **Mirror LDAP Groups** , then Looker will make one Looker group for every LDAP group that is introduced into the system. Those Looker groups can be viewed on the **Groups** page of the **Admin** section of Looker. Groups can be used for assigning roles to group members, setting content access controls, and assigning user attributes.
### Default groups and roles
By default, the **Mirror LDAP Groups** switch is off. In this case, you can set a default group for new LDAP users. In the **New User Groups** and **New User Roles** fields, enter the names of any Looker groups or roles to which you want to assign new Looker users when they first sign in to Looker.
These groups and roles are applied to new users at their initial login. The groups and roles are not applied to pre-existing users, and they are not reapplied if they are removed from users after the users' initial login.
If you later enable mirrored LDAP groups, these defaults will be removed for users upon their next login and replaced by roles assigned in the **Mirror LDAP Groups** section. These default options will no longer be available or assigned, and they will be fully replaced by the mirrored groups configuration.
### Enabling mirror LDAP groups
If you choose to mirror your LDAP groups within Looker, turn on the **Mirror LDAP Groups** switch. Looker displays these settings:
**Group Finder Strategy** : Choose an option from the drop-down to tell Looker how to find a user's groups:
  * **Groups Have Member Attributes** : This is the more common option. When looking for a group member, Looker will only return the groups to which a user is directly assigned. For example, if a user is a member of the Database-Admin group, and the Database-Admin group is a member of the Engineering group, a user would only get the permissions affiliated with the Database-Admin group.
  * **Groups Have Member Attributes (deep search)** : This option lets groups be members of other groups, which is sometimes referred to as _LDAP nested groups_. This means that a user can have the permissions of more than one group. For example, if a user is a member of the Database-Admin group, and the Database-Admin group is a member of the Engineering group, a user would get the permissions affiliated with _both_ of these groups. Some LDAP servers (especially Microsoft Active Directory) have support to automatically execute this type of deep search, even when the caller is doing what seems like a shallow search. That may be another method you can use to execute a deep search.


**Base DN** : Lets you narrow the search, and can be the same as the **Base DN** specified in the User Binding Settings section of this documentation page.
**Groups Object Class(es)** : This setting is optional. As noted in the User Binding Settings section, this allows the results that Looker returns to be constrained to a particular object type or set of types.
**Group Member Attr** : The attribute that, for each group, determines the objects (in this case, probably the people) that are a member.
**Group User Attr** : The name of the LDAP user attribute whose value we will search for in the Group entries to determine whether a user is part of the group. This defaults to `dn` (meaning that leaving it blank is the same as setting it to `dn`), which will result in LDAP using the full Distinguished Name, which is the exact case-sensitive string that would exist in the LDAP search itself, to search Group entries.
**Preferred Group Name/Roles/Group DN** : This set of fields lets you assign a custom group name and one or more roles that are assigned to the corresponding LDAP group in Looker.
  1. Enter the LDAP group DN in the **Group DN** field. This should include the full Distinguished Name, which is the exact case-sensitive string that would exist in the LDAP search itself. LDAP users who are included in the LDAP group will be added to the mirrored group within Looker.
  2. Enter a custom name for the mirrored group in the **Custom Name** field. This is the name that will be displayed on the **Groups** page of the **Admin** section of Looker.
  3. In the field to the right of the **Custom Name** field, select one or more Looker roles that will be assigned to each user in the group.
  4. Click `+` to add additional sets of fields to configure additional mirrored groups. If you have multiple groups configured and want to remove the configuration for a group, click `X` next to that group's set of fields.


If you edit a mirrored group that was previously configured in this screen, the configuration of the group will change but the group itself will remain intact. For example, you could change the custom name of a group, which would change how the group appears in Looker's **Groups** page but wouldn't change the assigned roles and group members. Changing the **Group DN** would maintain the group name and roles, but members of the group would be reassigned based on the users who are members of the external LDAP group that has the new LDAP group DN.
If you delete a group in this page, that group will no longer be mirrored in Looker and its members will no longer have the roles in Lookerr assigned to them through that group.
Any edits made to a mirrored group will be applied to users of that group when they next sign in to Looker.
### Advanced role management
If you have enabled the **Mirror LDAP Groups** switch, Looker displays these settings. The options in this section determine how much flexibility Lookeradmins have when configuring Looker groups and users who have been mirrored from Looker.
For example, if you want your Looker group and user configuration to strictly match your LDAP configuration, turn on these options. When all of the first three options are enabled, Looker admins cannot modify membership of mirrored groups and can only assign roles to users through LDAP mirrored groups.
If you want to have more flexibility to further customize your groups within Looker, turn off these options. Your Looker groups will still mirror your LDAP configuration, but you will be able to do additional group and user management within Looker, such as adding LDAP users to Looker groups or assigning Looker roles directly to LDAP users.
For new Looker instances, or Looker instances that have no previously configured mirrored groups, these options are off by default.
For existing Looker instances that have configured mirrored groups, these options are on by default.
The **Advanced Role Management** section contains these options:
**Prevent Individual LDAP Users from Receiving Direct Roles** : Turning this option on prevents Looker admins from assigning Looker roles directly to LDAP users. LDAP users will receive roles only through their group memberships. If LDAP users are allowed membership in built-in (not mirrored) Looker groups, they can still inherit their roles both from mirrored LDAP groups and from built-in Looker groups. Any LDAP users who were previously assigned roles directly will have those roles removed when they next sign in.
If this option is off, Looker admins can assign Looker roles directly to LDAP users as if they are users who were configured directly in Looker.
**Prevent Direct Membership in non-LDAP Groups** : Turning this option on prevents Looker admins from adding LDAP users directly to built-in Looker groups. If mirrored LDAP groups are allowed to be members of built-in Looker groups, LDAP users may retain membership in any parent Looker groups. Any LDAP users who were previously assigned to built-in Looker groups will be removed from those groups when they next sign in.
If this option is off, Looker admins can add LDAP users directly to built-in Looker groups.
**Prevent Role Inheritance from non-LDAP Groups** : Turning this option on prevents members of mirrored LDAP groups from inheriting roles from built-in Looker groups. Any LDAP users who previously inherited roles from a parent Looker group will lose those roles when they next sign in.
If this option is off, mirrored LDAP groups or LDAP users who are added as a member of a built-in Looker group will inherit the roles assigned to the parent Looker group.
**Auth Requires Role** : If this option is on, LDAP users are required to have a role assigned. Any LDAP users who don't have a role assigned won't be able to sign in to Looker at all.
If this option is off, LDAP users can authenticate to Looker even if they have no role assigned. A user with no assigned role won't be able to see any data or take any action in Looker, but they will be able to sign in to Looker.
### Disabling mirror LDAP groups
If you want to stop mirroring your LDAP groups within Looker, turn off the **Mirror LDAP Groups** switch. Any empty mirror LDAP groups will be deleted.
Non-empty mirror LDAP groups will remain available for use in content management and role creation. However, users cannot be added to or removed from mirror LDAP groups.
## Migration and integration options
### Alternate login for admins and specified users
  * Allow an alternate email-based login for admins and for users with the `login_special_email` permission (read more about setting this permission in the Roles documentation). This option will appear on the Looker login page if you've turned it on and the user has the appropriate permission.
  * This option is useful as a fallback during LDAP setup, if LDAP config problems occur later, or if you need to support some users who are not in your LDAP directory.
  * Looker email and password logins are always disabled for regular users when LDAP is enabled.


### Merge by email
  * This option allows Looker to merge first-time LDAP users with their existing Looker accounts, based on email address.
  * If Looker cannot find a matching email address, a new account will be created for the user.


## Save and apply settings
Once you are done entering your information, and the tests are all passing, check **I have confirmed the configuration above and want to enable applying it globally** and click **Update Settings** to save.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


