# Prepare a Looker (Google Cloud core) instance for users

**Source:** https://cloud.google.com/looker/docs/looker-core-instance-setup

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Create a LookML model
  * Set a Looker homepage
  * Set up announcements for your users
  * Understand Looker roles and permissions
  * Configure an email domain allowlist
  * Configure business user features
  * Add and manage Looker (Google Cloud core) users
  * Share performance recommendations




Was this helpful?
Send feedback 
#  Prepare a Looker (Google Cloud core) instance for users
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create a LookML model
  * Set a Looker homepage
  * Set up announcements for your users
  * Understand Looker roles and permissions
  * Configure an email domain allowlist
  * Configure business user features
  * Add and manage Looker (Google Cloud core) users
  * Share performance recommendations


Once a Looker (Google Cloud core) instance is created, those with the Admin Looker role can set up the instance for users as described in the following sections on this page:
  * Create a LookML project
  * Set a Looker homepage
  * Set up announcements for your users
  * Understand Looker roles and permissions
  * Configure an email domain allowlist
  * Configure business user features
  * Add and manage Looker (Google Cloud core) users
  * Share performance recommendations


## Create a LookML model
Once an instance contains a database connection, you are ready to set up a LookML model.
LookML models are located inside LookML projects. A LookML project contains collections of LookML files that describe how your database tables are related to each other and how Looker should interpret those tables. Once a model is set up, users can interact with the data, including exploring data, creating dashboards, and setting up alerts, among other things.
You can set up a LookML model within a Looker (Google Cloud core) instance if you have one of the following roles:
  * Developer Looker role


The steps for creating LookML models and projects are listed on the Generating a LookML model documentation page. Alternatively, you can follow the **Set up Looker** guide that appears dynamically within the Looker (Google Cloud core) instance.
If you want to customize the LookML in your model, you can access your project files in two ways:
  * from the **Develop** menu in the main navigation panel
  * by expanding **Edit project files** and clicking **edit project** in the **Set up Looker** guide


Click the name of your project to open its LookML files. See the Introduction to LookML documentation page to learn more about LookML development.
Additionally, the Best practice: Create a positive experience for Looker users article provides recommendations on how to use LookML to improve the experiences of Looker (Google Cloud core) users.
Looker (Google Cloud core) also provides a sample LookML project that can help you learn to write LookML, query data, and view dashboards. The sample LookML project is provided on Looker (Google Cloud core) instances of all edition types. See the Use the sample LookML project on a Looker (Google Cloud core) instance documentation page for more information about accessing and using the sample LookML project on your instance.
## Set a Looker homepage
The homepage appears when users log in to Looker (Google Cloud core), navigate to the homepage by clicking **Home** in the main navigation panel, or click the Looker logo in the instance. By default, the homepage for your instance is the prebuilt Looker homepage, which displays a user's favorite content, that user's recently viewed content, and the recently viewed content at the organization. However, those with the Admin Looker role can change this default to a URL within Looker (Google Cloud core). Learn more about homepage settings on the Admin settings - Homepage documentation page.
## Set up announcements for your users
If your instance uses the prebuilt Looker homepage, admins and users who have the `manage_homepage` permission can customize announcements to users with the announcement sidebar. See the Making announcements to your users documentation page for more information about the announcement sidebar.
## Understand Looker roles and permissions
Looker roles govern what users can do within a Looker (Google Cloud core) instance, and they are not the same as Google IAM roles. For example, in order to explore data within a Looker (Google Cloud core) instance, users must have a role that contains the `explore` Looker permission. Learn more about roles and permissions on the Admin settings - Roles documentation page.
Looker roles can be granted by default during first log in (see the documentation for Google OAuth, SAML, or OIDC), through group mirroring with SAML or OIDC, or manually by an Admin on the **Users** or **Groups** pages.
## Configure an email domain allowlist
The **Email Domain Allowlist for Scheduled Content** setting in the Google Cloud console defines the email domains to which your Looker (Google Cloud core) users can deliver Looker content — Looks, dashboards, queries with visualizations — or alert notifications through email. By default, there are no domains in the allowlist at the time of instance creation and Looker (Google Cloud core) users who have the appropriate Looker permissions to email content can email content to any domain.
To limit content deliveries and alert notifications to email addresses with a specific domain, edit the Looker (Google Cloud core) instance configuration to restrict the domain(s) to which users can send emails. Users who have the `schedule_external_look_emails` permission can send emails to any domain regardless of the **Email Domain Allowlist for Scheduled Content** settings. To learn more about the email domain allowlist and how it interacts with permissions and user attributes, see the Email domain allowlist for scheduled content documentation.
## Configure business user features
Some features in Looker (Google Cloud core) can be configured by an admin to allow or restrict their usage to certain users. See the Managing business user features documentation page to understand how you can set up features for your users.
## Add and manage Looker (Google Cloud core) users
Once your instance is configured, you can choose an authentication method and add and manage users. See the Manage users within Looker (Google Cloud core) documentation page for more information.
## Share performance recommendations
Looker (Google Cloud core) performance can be enhanced through Admin settings, LookML developer patterns, and business user practices. See the Looker performance documents page for a list of documentation pages that contain tips and best practices for each kind of user. Share this information with your users to keep your Looker (Google Cloud core) instance as performant as possible.
## What's next
  * Authentication methods for Looker (Google Cloud core)
  * Manage users within Looker (Google Cloud core)
  * Administer a Looker (Google Cloud core) instance from the Google Cloud console


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


