# Admin settings - OpenID Connect authentication  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-authentication-openid-connect

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  Admin settings - OpenID Connect authentication
Stay organized with collections  Save and categorize content based on your preferences. 
Companies use different OpenID Connect providers (OPs) to coordinate with OpenID Connect (for example, Okta or OneLogin). The terms used in the following setup instructions and in the Looker UI may not directly match those used by your OP.
The **OpenID Connect** page in the **Authentication** section of the Admin menu lets you configure Looker to authenticate users using the OpenID Connect protocol. This page describes that process and includes instructions for linking OpenID Connect groups to Looker roles and permissions.
## Requirements
Looker displays the **OpenID Connect** page in the **Authentication** section of the **Admin** menu only if the following conditions are met:
  * You have the Admin role.
  * Your Looker instance is enabled to use OpenID Connect.


If these conditions are met, and you don't see the **OpenID Connect** page, open a support request to enable OpenID Connect on your instance.
## Planning considerations
  * Consider using the **Alternate Login for Specified Users** option to allow Looker admins to access Looker without OpenID Connect.
  * Don't disable OpenID Connect authentication while you are logged in to Looker using OpenID Connect unless you have an alternate account login set up. **Otherwise, you could lock yourself out of the app.**
  * Looker can migrate existing accounts to OpenID Connect using email addresses that come from either current email and password setups, LDAP, SAML, or Google Auth. You will be able to configure this in the setup process.
  * Looker only supports OpenID Connect authentication using OpenID Connect's Authorization Code Flow. Other code flows are not supported.
  * The OpenID Connect specification includes an optional Discovery mechanism. Looker does not support this mechanism — so you must provide explicit URLs in the **OpenID Connect Auth Settings** section, as described in Configuring OpenID Connect auth settings.


## Setting up OpenID Connect
To set up the connection between Looker and OpenID Connect, perform the following tasks:
  1. Give your Looker URL to your OpenID Connect Provider (OP).
  2. Get required information from your OP.


### Setting up Looker on your OP
Your OpenID Connect Provider (OP) will need the URL of your Looker instance. Your OP may call this the _Redirect URI_ or _Login Redirect URI_ , among other names. On your OP's website, provide your OP with the URL where you typically access your Looker instance in a browser, followed by `/openidconnect`. For example, `https://instance_name.looker.com/openidconnect`.
### Getting information from your OP
To configure Looker for OpenID Connect authentication, you need the following information from your OP:
  * A client identifier and client secret. These are usually supplied by the OP on their website when you configure the Redirect URI.
  * During the OpenID Connect authentication process, Looker will connect to three different endpoints, an Authentication endpoint, an ID Token endpoint, and a User Information endpoint. You will need the URLs your OP uses for each of these endpoints.
  * Each OP will provide user information in sets called _scopes_. You need to know the names of the scopes your OP uses. The OpenID Connect requires the `openid` scope, but your OP will likely include other scopes, such as `email`, `profile`, and `groups`.
  * In OpenID Connect, attributes that store user data are called _claims_. You need to know which claims your OP passes to Looker to provide the user information you want on your Looker instance. Looker requires claims that contain email and name information, but if you have any other user attributes, such as time zone or department, Looker will also need to identify which claims contain that information. Claims can be included in the response from either the User Information endpoint or the ID Token endpoint. Looker can map claims returned by either endpoint to Looker user attributes.


Many OPs provide information about configuring OpenID Connect in the form of a discovery document, allowing you to gather some or all of the information that you will need to configure Looker for OpenID Connect. If you don't have access to a discovery document, you need to obtain the necessary information from your OP or internal authentication team.
The following section is from an example of a discovery document:
```
{
  "issuer": "https://accounts.google.com",
  "authorization_endpoint": "https://accounts.google.com/o/oauth2/v2/auth",
  "token_endpoint": "https://www.googleapis.com/oauth2/v4/token",
  "userinfo_endpoint": "https://www.googleapis.com/oauth2/v3/userinfo",
  "revocation_endpoint": "https://accounts.google.com/o/oauth2/revoke",
  "jwks_uri": "https://www.googleapis.com/oauth2/v3/certs",
  "response_types_supported": [
    "code",
    "token",
    "id_token",
    "code token"
    "code id_token",
    "token id_token",
    "code token id_token",
    "none"
  ],
  "subject_types_supported": [
    "public"
  ],
  "id_token_signing_alg_values_supported": [
    "RS256"
  ],
  "scopes_supported": [
    "openid",
    "email",
    "profile"
  ],
  "token_endpoint_auth_methods_supported": [
    "client_secret_post",
    "client_secret_basic"
  ],
  "claims_supported": [
    "aud",
    "email",
    "email_verified",
    "exp",
    "family_name",
    "given_name",
    "iat",
    "iss",
    "locale",
    "name",
    "picture",
    "sub"
  ],


```

## Configuring OpenID Connect auth settings
Use the configuration information you obtained from your OP's discovery document, your OP, or your internal authentication team to enter connection settings in the following fields:
**Identifier** : The client identifier unique to your Looker instance. This should be provided by your OP.
**Secret** : The client secret key unique to your Looker instance. This should be provided by your OP.
**Issuer** : The secure URL that identifies your OP.
**Audience** : An identifier indicating to your OP who the client is. This is often the same as your **Identifier** value, but may be a different value.
**Authorization URL** : The URL of the OP where the authentication sequence begins. Often called `authorization_endpoint` in a discovery document.
**Token URL** : The URL where Looker retrieves an OAuth token after Looker has been authorized. Often called `token_endpoint` in a discovery document.
**User Info URL** : The URL where Looker will retrieve detailed user information. Often called `userinfo_endpoint` in a discovery document.
**Scopes** : A comma-separated list of scopes used by the OP to provide user information to Looker. You must include the `openid` scope and any scopes that include the information Looker requires, which includes email addresses, user names, and any user attributes configured on your Looker instance.
## Configuring user attribute settings
In this section, you will map your OP's claims to Looker user attributes.
In the **User Attribute Settings** section, enter the name of your OP's claim that contains the corresponding information for each field. This tells Looker how to map those claims to Looker user information at login time. Looker isn't particular about how claims are constructed, it's just important that the claim information entered here matches the way that the claims are defined in your OP.
### Standard claims
Looker requires username and email information for user authentication. Enter your OP's corresponding claim information in this section:
**Email Claim** : The claim your OP uses for user email addresses, such as `email`.
**First Name Claim** : The claim your OP uses for user first names, such as `given_name`.
**Last Name Claim** : The claim your OP uses for user last names, such as `family_name`.
Note that some OPs use a single claim for names, rather than separating first and last names. If this is the case with your OP, enter the claim that stores names in both of the **First Name Claim** and **Last Name Claim** fields. For each user, Looker will use the contents up to the first space as the First Name and everything afterwards as the Last Name.
### Attribute pairings
Optionally, you can use the data in your OpenID Connect claims to automatically populate values in Looker user attributes when a user logs in. For example, if you have configured OpenID Connect to make user-specific connections to your database, you could pair your OpenID Connect claims with Looker user attributes to make your database connections user-specific in Looker.
To pair claims with corresponding Looker user attributes:
  1. Enter the claim as identified by your OP in the **Claim** field and the Looker user attribute you want to pair it with in the **Looker User Attributes** field.
  2. Check **Required** if you want to block login by any user account that is missing a value in that claim field.
  3. Click **+** and repeat these steps to add more claim and attribute pairs.


Note that some OPs can have "nested" claims. For example:
```
"zoneinfo": "America/Los Angeles",
"phone_number": "555-1235",
"address": {
  "street_address": "1234 Main Street",
  "locality": "Anyton",
  "region": "IL",
  "postal_code": "60609",
  "country": "US"
},

```

In the previous example, the `locality` claim is nested within the `address` claim. For nested claims, specify the parent and nested claims, separated by a slash ( `/` ) character. To configure Looker for the `locality` claim in the example, you would enter `address/locality`.
## Groups and roles
You have the option for Looker to create groups that mirror your externally managed OpenID Connect groups, and then assign Looker roles to users based on their mirrored OpenID Connect groups. When you make changes to your OpenID Connect group membership, those changes are automatically propagated into Looker's group configuration
Mirroring OpenID Connect groups lets you use your externally defined OpenID Connect directory to manage Looker groups and users. This, in turn, lets you manage your group membership for multiple software as a service (SaaS) tools, such as Looker, in one place.
If you turn on **Mirror OpenID Connect Groups** , then Looker will make one Looker group for every OpenID Connect group that is introduced into the system. Those Looker groups can be viewed on the **Groups** page of the **Admin** section of Looker. Groups can be used for assigning roles to group members, setting content access controls and assigning user attributes.
### Default groups and roles
By default, the **Mirror OpenID Connect Groups** switch is off. In this case, you can set a default group for new OpenID Connect users. In the **New User Groups** and **New User Roles** fields, enter the names of any Looker groups or roles to which you want to assign new Looker users when they first sign in to Looker:
These groups and roles are applied to new users on their initial login. They are not applied to pre-existing users, and are not reapplied if they are removed from users after their initial login.
### Enabling mirror OpenID Connect groups
If you are using a Looker (Google Cloud core) instance, we recommend that you enable group mirroring for only the primary authentication method and don't enable group mirroring for the backup OAuth authentication. If you enable group mirroring for both the primary and secondary methods of authentication, the following behaviors will occur:
  * If a user has merged identities, group mirroring will match the primary authentication method regardless of the actual authentication method used to sign in.
  * If a user doesn't have merged identities, group mirroring will match the authentication method used to sign in.


#### Steps to enable mirrored groups
To mirror your OpenID Connect groups within Looker, turn on the **Mirror OpenID Connect Groups** switch:
**Groups Claim** : Enter the claim that your OP uses to store group names. Looker will make one Looker group for every OpenID Connect group that is introduced into the system by the Groups claim. Those Looker groups can be viewed on the **Groups** page of the **Admin** section of Looker. Groups can be used for setting content access controls and assigning user attributes.
**Preferred Group Name / Roles / OpenID Connect Group Name** : This set of fields lets you assign a custom group name and one or more roles that are assigned to the corresponding OpenID Connect group in Looker:
  1. Enter the OpenID Connect group name in the **OpenID Connect Group Name** field. OpenID Connect users who are included in the OpenID Connect group will be added to the mirrored group within Looker.
  2. Enter a custom name for the mirrored group in the **Custom Name** field. This is the name that will be displayed in the **Groups** page of the **Admin** section of Looker.
  3. In the field to the right of the **Custom Name** field, select one or more Looker roles that will be assigned to each user in the group.
  4. Click `+` to add additional sets of fields to configure additional mirrored groups. If you have multiple groups configured and want to remove the configuration for a group, click `X` next to that group's set of fields.


If you edit a mirrored group that was previously configured in this screen, the configuration of the group will change but the group itself will remain intact. For example, you could change the custom name of a group, which would change how the group appears in Looker's **Groups** page but wouldn't change the assigned roles and group members. Changing the **OpenID Connect Group ID** would maintain the group name and roles, but members of the group would be reassigned based on the users who are members of the external OpenID Connect group that has the new OpenID Connect group ID.
If you delete a group in this page, that group will no longer be mirrored in Looker and its members will no longer have the roles in Looker assigned to them through that group.
Any edits made to a mirrored group will be applied to users of that group when they next sign in to Looker.
### Advanced role management
If you have enabled the **Mirror OpenID Connect Groups** switch, Looker displays these settings. The options in this section determine how much flexibility Looker admins have when configuring Looker groups and users who have been mirrored from OpenID Connect.
For example, if you want your Looker group and user configuration to strictly match your OpenID Connect configuration, turn on these options. When all of the first three options are enabled, Looker admins cannot modify membership of mirrored groups and can only assign roles to users through OpenID Connect mirrored groups.
If you want to have more flexibility to further customize your groups within Looker, turn off these options. Your Looker groups will still mirror your OpenID Connect configuration, but you will be able to do additional group and user management within Looker, such as adding OpenID Connect users to Looker-specific groups or assigning Looker roles directly to OpenID Connect users.
For new Looker instances, or instances that have no previously configured mirrored groups, these options are off by default.
For existing Looker instances that have configured mirrored groups, these options are on by default.
The **Advanced Role Management** section contains these options:
**Prevent Individual OpenID Connect Users from Receiving Direct Roles** : Turning this option on prevents Looker admins from assigning Looker roles directly to OpenID Connect users. OpenID Connect users will receive roles only through their group memberships. If OpenID Connect users are allowed membership in built-in (not mirrored) Looker groups, they can still inherit their roles both from mirrored OpenID Connect groups and from built-in Looker groups. Any OpenID Connect users who were previously assigned roles directly will have those roles removed when they next sign in.
If this option is off, Looker admins can assign Looker roles directly to OpenID Connect users as if they are users who were configured directly in Looker.
**Prevent Direct Membership in non-OpenID Connect Groups** : Turning this option on prevents Looker admins from adding OpenID Connect users directly to built-in Looker groups. If mirrored OpenID Connect groups are allowed to be members of built-in Looker groups, OpenID Connect users may retain membership in any parent Looker groups. Any OpenID Connect users who were previously assigned to built-in Looker groups will be removed from those groups when they next sign in.
If this option is off, Looker admins can add OpenID Connect users directly to built-in Looker groups.
**Prevent Role Inheritance from non-OpenID Connect Groups** : Turning this option on prevents members of mirrored OpenID Connect groups from inheriting roles from built-in Looker groups. Any OpenID Connect users who previously inherited roles from a parent Looker group will lose those roles when they next sign in.
If this option is off, mirrored OpenID Connect groups or OpenID Connect users who are added as a member of a built-in Looker group will inherit the roles assigned to the parent Looker group.
**Auth Requires Role** : If this option is on, OpenID Connect users are required to have a role assigned. Any OpenID Connect users who don't have a role assigned won't be able to sign in to Looker at all.
If this option is off, OpenID Connect users can authenticate to Looker even if they have no role assigned. A user with no assigned role won't be able to see any data or take any action in Looker, but they will be able to sign in to Looker.
### Disabling mirror OpenID Connect groups
If you want to stop mirroring your OpenID Connect groups within Looker, turn off the **Mirror OpenID Connect Groups** switch. Any empty mirror OpenID Connect groups will be deleted.
Non-empty mirror OpenID Connect groups will remain available for use in content management and role creation. However, users cannot be added to or removed from mirror OpenID Connect groups.
## Configuring migration options
As explained in this section, Looker recommends that you enable **Alternate Login** and provide a merging strategy for existing users.
### Alternate login for specified users
Looker email and password logins are always disabled for regular users when OpenID Connect authentication is enabled. The **Alternate Login for Specified Users** option enables alternate email-based login using `/login/email` for admins and for specified users with the `login_special_email` permission.
Turning this on is useful as a fallback during OpenID Connect setup should OpenID Connect configuration problems occur later, or if you need to support some users who do not have accounts in your OpenID Connect directory.
### Specify the method used to merge OpenID Connect users to a Looker account
In the **Merge Users Using** field, specify the method to be used to merge a first-time Open ID Connect login to an existing user account. You can merge users from the following systems:
  * **Looker Email/Password** (not available for Looker (Google Cloud core))
  * **Google**
  * **LDAP** (not available for Looker (Google Cloud core))
  * **SAML**


If you have multiple authentication systems in place, you can specify more than one system to merge by in this field. Looker will look up users from the systems listed _in the order that they are specified_. For example, assume you created some users using Looker email/password, then you enabled LDAP, and now you want to use OpenID Connect. In the previous example, Looker would merge by email and password first and then LDAP.
When a user logs in for the first time with OpenID Connect, this option will connect the user to their existing account by finding the account with a matching email address. If there is no existing account for the user, a new user account will be created.
#### Merging users when using Looker (Google Cloud core)
When you're using Looker (Google Cloud core) and OpenID Connect, merging works as described in the previous section. However, it is only possible when one of the following two conditions is met:
  * **Condition 1** : Users are authenticating into Looker (Google Cloud core) using their Google identities through the OpenID Connect protocol.
  * **Condition 2** : Before selecting the merge option, you have completed the following two steps:
    1. Federated users' identities in Google Cloud using Cloud Identity.
    2. Set up OAuth authentication as the backup authentication method using the federated users.


If the setup does not meet one of these two conditions, the **Merge Users Using** option will be unavailable.
When merging, Looker will search for user records that share the exact same email address.
## Testing user authentication
While specifying this configuration, click the **Test** button to test your OpenID Connect configuration.
Tests will redirect out to the endpoints and will open a new browser tab. The tab displays:
  * Whether Looker was able to talk to the various endpoints and validate
  * A trace of the authentication endpoint response
  * The user info Looker gets from the user info endpoint
  * Both decoded and raw versions of the ID token received


You can use this test to verify the information received from the various endpoints is correct, and to troubleshoot any errors.
**Tips** :
  * You can run this test at any time, even if OpenID Connect is partially configured. Running a test can be helpful during configuration to see which parameters need configuration.
  * The test uses the settings entered on the **OpenID Connect Authentication** page, even if those settings have not been saved. The test won't affect or change any of the settings on that page.


## Save and apply settings
Once you are done entering your information, and all tests are passing, check **I have confirmed the configuration above and want to enable applying it globally** and click **Update Settings** to save.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


