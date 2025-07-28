# Self-service migration from Looker (original) to Looker (Google Cloud core)

**Source:** https://cloud.google.com/looker/docs/looker-core-self-service-migration

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Ensure that your Looker (original) instance is ready for migration
  * Export the data from your Looker (original) instance
    * Create a place to store the migration data
    * Request the export
  * Import the data into the new "empty" Looker (Google Cloud core) instance
  * Finalize the setup of the Looker (Google Cloud core) instance
  * Decommission the Looker (original) instance
  * Troubleshooting
    * Issues during export
    * Issues during import




Was this helpful?
Send feedback 
#  Self-service migration from Looker (original) to Looker (Google Cloud core)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Ensure that your Looker (original) instance is ready for migration
  * Export the data from your Looker (original) instance
    * Create a place to store the migration data
    * Request the export
  * Import the data into the new "empty" Looker (Google Cloud core) instance
  * Finalize the setup of the Looker (Google Cloud core) instance
  * Decommission the Looker (original) instance
  * Troubleshooting
    * Issues during export
    * Issues during import


This document outlines the technical steps for migrating your existing Looker instance from the Looker (original) environment to Looker (Google Cloud core).
Looker (Google Cloud core) is a deployment environment that deeply integrates with the Google Cloud platform. Looker (Google Cloud core) is hosted on Google Cloud infrastructure; you can manage it directly through the Google Cloud console; and it has deep integrations with many of the other products, services, and capabilities of Google Cloud.
## Before you begin
  1. Familiarize yourself with Google Cloud principles and tools by reviewing the following documentation:
     * Google Cloud overview
     * Looker (Google Cloud core) overview
     * Cloud Billing overview
  2. Speak to your account representative about migration and whether your Looker (original) instance is eligible. If your instance is eligible, and if you have upgraded your existing Looker (original) contract to cover Looker (Google Cloud core), you can complete the steps in this document to migrate your instance.
  3. To get the permissions that you need to prepare for migration, ask your administrator to grant you the following IAM roles on the Google Cloud project in which the Looker (Google Cloud core) instance will reside: 
     * Create a Looker (Google Cloud core) instance: Looker Admin (`roles/looker.admin`). 
     * Assign IAM roles within your Google Cloud project: Project IAM Admin (`roles/resourcemanager.projectIamAdmin`). 
     * Create a Cloud Storage bucket: Storage Admin (`roles/storage.admin`). 
For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
  4. To manage the Looker (original) instance in preparation for migration, you must have the Admin Looker role in that instance.
  5. Create a new "empty" Looker (Google Cloud core) instance.
Make sure to select the proper edition, network connection type (public IP or private IP), and other configuration attributes (CMEK, VPC-SC) for your new Looker (Google Cloud core) instance to ensure that it has the necessary capabilities. Some of the features in Looker (Google Cloud core) depend on the selected edition or selected network type.
Leave the instance "empty"; don't populate it with any data such as model files, users, connections, Explores, dashboards, or folders. During the import step, any settings or content will be wiped out and replaced with data from the migration.
However, the configuration attributes of Looker (Google Cloud core) that are specified through the Google Cloud console, or that can only be specified during instance creation, are not overwritten during the migration process.


## Overview
At a high level, the migration process consists of the following steps.
  1. Ensure that your Looker (original) instance is ready for migration.
  2. Export the data from your Looker (original) instance.
  3. Import the data into the new "empty" Looker (Google Cloud core) instance.
  4. Finalize the setup of the Looker (Google Cloud core) instance.
  5. Decommission the Looker (original) instance.


The following sections provide details on each of these steps.
## Ensure that your Looker (original) instance is ready for migration
Your Looker (original) instance must meet the following prerequisites to be eligible for migration:
  * Your Looker (original) instance must be managed by Google (in other words, not customer hosted) and hosted on Google Cloud or Amazon Web Services.
  * Your Looker (original) instance must use a version within one monthly release of the current Looker (Google Cloud core) version. To find the current Looker (Google Cloud core) version, see the Looker release notes and find the most recent deployment announcement.


In addition, perform the following activities prior to migration:
  * There is a small set of feature differences between Looker (original) and Looker (Google Cloud core). Review these differences to ensure that the features in Looker (Google Cloud core) meet your ongoing needs.
  * Migration copies all _Production Mode_ projects and the model files that they contain, but not _Development Mode_ projects that belong to individual users. To ensure that Development Mode files are transferred through the migration, you must commit all files in all Development Mode projects to Git repositories before you initiate the migration.
  * Looker (Google Cloud core) supports only the Google OAuth, SAML, and OpenID Connect authentication methods.
    * If your Looker (original) instance uses a different authentication method (for example, email and password, LDAP, etc.), you will need to convert all users to an authentication method supported by Looker (Google Cloud core).
    * If your Looker (original) instance already uses Google OAuth, all user records will be transferred, but you must still manually create IAM permissions for the users in the project of your Looker (Google Cloud core) instance.
    * If your Looker (original) instance uses SAML, the **Merge users using** setting on the **SAML authentication** Admin panel page must be set to **Google** or **OIDC** to avoid an error when you test the SAML authentication.
    * If your Looker (original) instance uses OIDC, the **Merge users using** setting on the **OpenID Connect authentication** Admin panel page must be set to **Google** or **SAML** to avoid an error when you test the OpenID Connect authentication.
    * If you are using an external identity provider, you must update the callback URL in your identity provider to the Looker (Google Cloud core) URL to allow authentication into the new Looker (Google Cloud core) instance.
    * If your Looker (Google Cloud core) instance will use SAML or OpenID Connect as an authentication method, it is recommended to also set up Google OAuth, which acts as the backup authentication method for Looker (Google Cloud core).
    * If you are going to use a custom domain with your Looker (Google Cloud core) instance, don't set up SAML or OpenID Connect for the instance until the custom domain is enabled.
  * During migration, two Looker instances—one Looker (original), one Looker (Google Cloud core)—will run in parallel for some period of time. Any automatic activity that takes place (such as alerts and scheduled data deliveries, as well as background activity that accesses backend databases) may be duplicated. To avoid duplicate activity, delete automatic alerts and schedules in either the Looker (original) or the Looker (Google Cloud core) instance.


## Export the data from your Looker (original) instance
Exporting the data from your Looker (original) instances requires two steps:
  1. Create a place to store the migration data.
  2. Initiate the export.


### Create a place to store the migration data
Perform all of the following operations in the same Google Cloud project where you created the Looker (Google Cloud core) instance.
  1. Create a new Cloud Storage bucket (for example, `<bucket-name>`). 
     * This bucket will be used to store the migration data.
     * Follow the instructions on the Create buckets documentation page.
     * Note that the `<bucket-name>` must be unique across all of Google Cloud. We recommend prefixing the bucket name with a unique identifier, such as your project ID.
  2. Decide on a name for a folder inside the Cloud Storage bucket (for example, `<folder-name>`). Don't create the folder now. Specify the folder name during the export request. It will be created automatically during the export process.
  3. Create a key ring and key in the Cloud KMS (for example, `<kms_keyring_id>` and `<kms-key-id>`). 
     * This key will be used to encrypt the migration data. Since it is a KMS key, you need to disclose only the key name, not the key itself, to the **Export** page in the Looker (original) **Admin** panel.
     * Follow the instructions on the Create a key ring and Create a key documentation pages.
  4. Create a new service account specifically for the migration (for example, `<export-service-account>`). 
     * This is not the same service account as the Looker service account.
     * Follow the instructions on the Create service accounts documentation page.
  5. Grant the `<export-service-account>` two specific IAM roles:
     * `Storage Object Creator` on the Cloud Storage bucket
     * `Cloud KMS CryptoKey Encrypter` on the KMS key
     * Follow the instructions on the Use IAM permissions (Cloud Storage) and Access control with IAM (KMS) documentation pages.
  6. Create a service account key that is associated with `<export-service-account>`, and download the JSON key file.
     * Follow the instructions on the Create and delete service account keys documentation page.


### Request the export
Once you have ensured that your instance is ready for migration, created an "empty" Looker (Google Cloud core) instance, and created a place to store migration data, enter the following information into the **Export** page in your Looker (original) instance's **Admin** panel:
  * The name of the Cloud Storage bucket that you created.
  * The Cloud Storage folder name - a folder of this name will be automatically created during export. When the export is complete, the export files will appear in a timestamped sub-folder within this folder in the Cloud Storage bucket that you created.
  * The KMS key name.
  * The JSON text that contains the service-account key.


Once you have entered the information on the **Export** page, click **Request Export** to initiate the export.
The export process takes minutes to hours. Once the export is complete, you will see several export files (in non-human readable format) in your Cloud Storage bucket and folder. These files are input for the following import step.
## Import the data into the new "empty" Looker (Google Cloud core) instance
Once your instance data is exported, you can import it into your Looker (Google Cloud core) instance.
Follow the instructions on the Importing your data from a Cloud Storage to a Looker (Google Cloud core) instance page, pointing the commands to the bucket and folder in which the export files were placed.
In a nutshell, this entails the following:
  1. Granting the following roles for access to the bucket and the KMS key to the Looker service account (not the `<export-service-account>`): 
     * `Storage Object User` on the Cloud Storage bucket
     * `Cloud KMS CryptoKey Decrypter` on the KMS key
  2. Triggering the import through the Google Cloud console or gcloud CLI


The import operation takes minutes to hours. When it is completed, your Looker (Google Cloud core) instance will restart, with all the migrated data.
## Finalize the setup of the Looker (Google Cloud core) instance
At this point, Looker admins can navigate to the instance URL and log in to the instance to finalize setup.
The migration process copies as much of the Looker (original) instance configuration as possible. However, some items cannot be migrated, or function somewhat differently in Looker (Google Cloud core), and must be adjusted.
Some items that are known to require special attention include the following:
**General Settings** (in the Looker **Admin** panel) | Most of the options for **General Settings** (and other settings throughout the **Admin** panel) are not automatically copied, because they tend to be different or don't exist in the same form in Looker (Google Cloud core). You should carefully review and configure all settings in the context of your chosen Looker (Google Cloud core) configuration. Refer to the Administer a Looker (Google Cloud core) instance from Looker and the Administer a Looker (Google Cloud core) instance from the Google Cloud console documentation pages for more information about the settings in Looker (Google Cloud core).  
---|---  
Users |  Looker (Google Cloud core) supports only the Google OAuth, SAML, and OpenID Connect authentication methods. If the Looker (original) instance was also configured for Google OAuth, the user records and their attributes will be copied (as long as they are associated with the same Google ID and email address in both instances). A Project IAM Admin must grant each user the Looker Admin or the Looker Instance User IAM role on the Google Cloud project in which the instance is located. If the Looker (original) instance was configured for SAML or OpenID Connect, be sure the **Merge users using** field for the authentication method indicates only authentication methods that are supported by Looker (Google Cloud core). If some users of the Looker (original) instance were authenticating through a mechanism that is not supported in Looker (Google Cloud core) (such as LDAP or email/password), those user accounts will need to be re-created and converted to a supported authentication method.  
Database connections | Looker (Google Cloud core) supports a slightly different set of database dialects than Looker (original). All the configuration properties for database connections (including connection string and password, if applicable) are copied. However, the different network topology in Looker (Google Cloud core) may prevent the database connections from working immediately. For example, if the databases are accessed through firewalls or tunnels that are specific to the Looker (original) instance, you may need to reconfigure the firewalls or tunnels. You should test each connection and re-establish it if necessary.  
Database connections using OAuth | The migration from Looker (original) to Looker (Google Cloud core) doesn't retain OAuth access or refresh tokens for individual users' database connections to BigQuery or Snowflake. After migration, Looker (Google Cloud core) users will be prompted to re-authenticate OAuth when they view an Explore or a dashboard that references an OAuth database connection. Users can also re-authenticate to their databases by going to their Account page and selecting **Log in** for each database under the **OAuth Connection Credentials** heading. Any automated schedules or alerts that are owned by a single user and reference an OAuth connection will break until that user logs in with their OAuth credentials.  
Git repository connections | If the instance is using bare Git repositories, they should work without modification (copied, but not shared). But if the instance connects to remote repositories, these connections may need to be verified and re-enabled, similarly to the database connections.  
Other network configuration | The Looker instance may have other types of network connections, both inbound and outbound (for example, in the context of private IP, Action Hub, Marketplace, email, etc.). These network connections must also be verified.  
URL for accessing the Looker (Google Cloud core) instance | The Looker (Google Cloud core) instance comes with a primary URL that is randomly assigned. If the instance needs to be accessed through a specific URL, you can configure a custom domain.  
Schedules and alerts |  If both the Looker (original) and Looker (Google Cloud core) instances are active simultaneously, they may generate duplicate scheduled actions and alerts, and perform duplicate background operations that access connected databases. These activities should be disabled in one of the instances as soon as practical. Any automated schedules or alerts that are owned by a single user and reference that user's individual OAuth connection will break until that user logs in with their OAuth credentials.  
Maintenance windows | Unlike in Looker (original), a maintenance policy can be specified for Looker (Google Cloud core).  
Elite System Activity | Elite System Activity data is not copied as part of the migration. The Looker (Google Cloud core) instance will start with a fresh history.  
Custom domain  |  You can create a custom domain for your Looker (Google Cloud core) instance. You must set the DNS records to ensure the SSL certificate deployment. Additionally, be sure to update the callback URL in your authentication client to the custom domain once your custom domain is enabled and your authentication method is set up. Custom domains cannot be created for Looker (Google Cloud core) using a `looker.com` domain. If you want to create a custom domain for your Looker (Google Cloud core) instance using the custom URL of your Looker (original) instance, the custom domain should be set up after migration has been completed and after you've confirmed that the Looker (Google Cloud core) instance is ready to be used. Once the custom domain is enabled, your users will see the Looker (Google Cloud core) instance and not the Looker (original) instance when they visit the instance URL. Don't set up SAML or OpenID Connect for the Looker (Google Cloud core) instance until the instance is ready to be used, the DNS records have been updated, and the custom domain has been enabled.  
Bookmarks |  If you are using a custom URL in your Looker (original) instance (that doesn't use the `looker.com` domain), this migration process should maintain users' bookmarks if you create a custom domain for your Looker (Google Cloud core) instance using the same URL as your Looker (original) instance. Once the custom domain is enabled, bookmarks to Looker (original) content such as `https://www.yourcustomdomain.com/dashboard/123` will point to the piece of content within the Looker (Google Cloud core) instance. (Note: **Enterprise** and **Embed** editions of Looker (Google Cloud core) use alphanumeric content slugs in their URLs instead of numeric content IDs, but a bookmark with a content ID will still redirect correctly to the same content.) This process cannot be used with Looker (original) URLs that use the domain `looker.com`.  
This list is not exhaustive. Test all the aspects of the instance that are most important to you, before considering the migration to be complete.
Once the migration is complete and you are sure that you won't require another export, you may delete the `<export-service-account>` that you created earlier, which renders useless the JSON key that was shared for it.
## Decommission the Looker (original) instance
Once the migrated Looker (Google Cloud core) instance is functioning satisfactorily, you can send your users the URL for the instance and instruct them to start accessing it and stop accessing the Looker (original) instance.
## Troubleshooting
The following sections may help you resolve issues during import or export.
### Issues during export
If there is an issue with the export of your Looker (original) data, a status of **ERROR** will appear on the **Export** page of the **Admin** panel. Clicking the **ERROR** status reveals an error message.
Common sources of errors are the following:
  * The Cloud Storage bucket, KMS key, or `<export-service-account>` is invalid.
  * The `<export-service-account>` lacks the necessary permissions.


It is helpful to confirm the status of these objects before submitting your export request.
### Issues during import
If the import operation does not finish after four hours (or possibly more if the source instance was very large), or if it exits in error, you may need to open a ticket with Cloud Customer Care to resolve the issue. There are relatively few diagnostics that are directly customer visible for this operation.
## What's next?
  * Admin settings - Export
  * Connect Looker (Google Cloud core) to your database
  * Set up the Looker (Google Cloud core) instance
  * Manage user access to the Looker (Google Cloud core) instance
  * Administer a Looker (Google Cloud core) instance from the Google Cloud console
  * Administer your Looker (Google Cloud core) instance from Looker


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


