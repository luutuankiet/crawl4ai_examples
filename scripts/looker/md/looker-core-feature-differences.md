# Feature availability in Looker (Google Cloud core)

**Source:** https://cloud.google.com/looker/docs/looker-core-feature-differences

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Feature availability by instance type
    * Administrative compatibility by instance type
    * Database connection compatibility by instance type
  * Feature compatibility by edition type
  * Feature compatibility by network configuration




Was this helpful?
Send feedback 
#  Feature availability in Looker (Google Cloud core)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Feature availability by instance type
    * Administrative compatibility by instance type
    * Database connection compatibility by instance type
  * Feature compatibility by edition type
  * Feature compatibility by network configuration


On this page, you will learn about Looker (Google Cloud core) features. Features vary by edition and network configuration.
## Feature availability by instance type
The interface and functionality of a Looker (Google Cloud core) instance is virtually indistinguishable from a Looker (original) instance, but the two instance types are not identical. Some differentiating characteristics include the following:
  * The administrative functions that are available in the instance Admin section
  * The database dialects that the instance can connect to


### Administrative compatibility by instance type
All administrative functions and settings for Looker (original) instances are managed in the Admin section of the Looker (original) instance. However, for Looker (Google Cloud core) instances, these settings are divided between the Admin section of the Looker (Google Cloud core) instance and the Google Cloud console.
### Database connection compatibility by instance type
The list of supported database dialects that you can connect to your instance differs between Looker (original) and Looker (Google Cloud core).
For a list of database dialects that are supported by Looker (original) instances, see the Looker dialects documentation page.
For a list of database dialects that are supported by Looker (Google Cloud core) instances, see the Connecting Looker (Google Cloud core) to your database documentation page.
## Feature compatibility by edition type
Some Looker (Google Cloud core) features vary depending on the instance edition. See the Looker (Google Cloud core) features and entitlements documentation page for more information.
## Feature compatibility by network configuration
Looker (Google Cloud core) instances can be configured with one of several network configurations. The following table shows feature compatibility for each network configuration. Select the checkboxes to filter the table.
Feature | Network configuration support | Notes  
---|---|---  
  * Public IP
  * Public IP and Private IP

| Enabled by default.  
Continuous Integration |  Public IP  
Conversational Analytics, Conversational Analytics Code Interpreter | 
  * Public IP
  * Private IP
  * Public IP and Private IP

|  Conversational Analytics does not support Looker (Google Cloud core) instances that use CMEK or VPC Service Controls. Connecting a private IP Looker (Google Cloud core) instance that is within a VPC Service Controls perimeter to Conversational Analytics in Looker Studio Pro is not supported and does not meet VPC Service Controls compliance requirements.  
  * Public IP
  * Private IP
  * Public IP and Private IP

|  Available for the **Enterprise** and **Embed** editions. Not available for the **Standard** edition.  
Deliver content to S3, SFTP, Webhook | 
  * Public IP
  * Private IP
  * Public IP and Private IP

| For private IP only instances, your Google Cloud project must be configured to route traffic to the selected destination.  
  * Public IP
  * Private IP
  * Public IP and Private IP

| See the list of supported database dialects for Looker (Google Cloud core).  
Elite System Activity | 
  * Public IP
  * Private IP
  * Public IP and Private IP

|  Available for the **Enterprise** and **Embed** editions. Not available for the **Standard** edition.  
Extension Framework | 
  * Public IP
  * Private IP
  * Public IP and Private IP

  
  * Public IP
  * Private IP
  * Public IP and Private IP

|  You can connect a Looker (Google Cloud core) instance with any network configuration to customer-hosted Git repositories on the public internet. If your instance uses a private IP network connection or a public and private IP connection, you must configure the Google Cloud project to connect to Git.  
Not supported | For private IP only instances, control access with your VPC settings.  
LDAP, email/password authentication |  Not supported  
Local project import | 
  * Public IP
  * Private IP
  * Public IP and Private IP

  
Looker Action Hub |  Public IP |  Custom actions can also be developed for a private action hub server. Data that your users send by using an action will be passed temporarily from your Looker (Google Cloud core) instance through the Looker Action Hub server. The Looker Action Hub is disabled by default. To enable an individual action, see the instructions in Admin settings - Actions.  
Looker Labs and Legacy features | Not supported | All Looker Labs and Legacy features are disabled on Looker (Google Cloud core).  
Looker **Log** Admin panel page | Not supported | Google Cloud uses Cloud Logging. See View instance logs for Looker (Google Cloud core) for more information.  
Looker support access | 
  * Public IP

| If your instance uses a private IP network connection or a public and private IP connection, see Getting support for Looker (Google Cloud core).  
Looker Usage dashboard | Not supported | Use System Activity dashboards and Explores to view usage information.  
  * Public IP
  * Private IP
  * Public IP and Private IP

  
Mobile application | 
  * Public IP
  * Private IP
  * Public IP and Private IP

| Available through the Looker Studio mobile app.  
Private embedding | 
  * Public IP
  * Private IP
  * Public IP and Private IP

| Available for all editions.  
Restrict TLS cipher suites | Public IP  
SAML, OpenID Connect authentication | 
  * Public IP
  * Private IP
  * Public IP and Private IP

  
Sample LookML project | 
  * Public IP
  * Private IP
  * Public IP and Private IP

| To use the sample LookML project, the BigQuery API must be enabled for your Google Cloud project.  
  * Public IP
  * Private IP
  * Public IP and Private IP

|  Available for the **Embed** edition. Not available for the **Standard** and **Enterprise** editions.  
Not supported  
VPC Service Controls |  Private IP  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


