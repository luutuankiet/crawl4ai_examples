# Looker (Google Cloud core) overview

**Source:** https://cloud.google.com/looker/docs/looker-core-overview

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Looker (Google Cloud core) editions
    * Standard edition
    * Enterprise edition
  * Non-production instances
    * Characteristics of non-production instances
  * Looker (Google Cloud core) features
    * Looker (Google Cloud core) features versus Looker (original) features
  * Set up and administer the Looker (Google Cloud core) instance
  * Use the Google Cloud CLI
  * Use the Looker (Google Cloud core) API
    * Types of Looker (Google Cloud core) API calls
  * Release notes and process




Was this helpful?
Send feedback 
#  Looker (Google Cloud core) overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Looker (Google Cloud core) editions
    * Standard edition
    * Enterprise edition
  * Non-production instances
    * Characteristics of non-production instances
  * Looker (Google Cloud core) features
    * Looker (Google Cloud core) features versus Looker (original) features
  * Set up and administer the Looker (Google Cloud core) instance
  * Use the Google Cloud CLI
  * Use the Looker (Google Cloud core) API
    * Types of Looker (Google Cloud core) API calls
  * Release notes and process


Looker (Google Cloud core) provides simplified and streamlined provisioning, configuration, and management of a Looker instance from the Google Cloud console. Some instance administration tasks may also be performed from the console.
Looker (Google Cloud core) instances are hosted by Google in the Google Cloud. Looker (Google Cloud core) is not available for customer-hosted or multicloud environments.
## Looker (Google Cloud core) editions
Looker (Google Cloud core) is available in several editions. Each edition type offers different functionality and has different pricing. When you create a Looker (Google Cloud core) instance, you choose the edition that meets your needs. Once an instance has been created, you cannot change the edition type. You can also provision, configure, and manage non-production instances of the same edition types for staging and testing. See the Staging environments and testing section on this page for things to know about setting up a non-production instance.
### Standard edition
The **Standard** edition is tailored for small teams and small or medium-sized businesses with up to 50 internal platform users. In addition to many existing Looker (Google Cloud core) features, the **Standard** edition brings new functionality, which includes the following:
  * Google Cloud Identity access management and simplified BigQuery connectivity
  * Support for up to 1,000 Query-related Looker (Google Cloud core) API calls per month and 1,000 Admin-related Looker (Google Cloud core) API calls per month


A **Standard** edition can be purchased through an annual contract.
### Enterprise edition
The **Enterprise** edition includes all the features of the **Standard** edition as well as supporting:
  * Unlimited users
  * Additional security features such as VPC-SC, Private IP, and Private Service Connect
  * A private label option
  * More robust monitoring through the Elite System Activity feature
  * 100,000 Query-related Looker (Google Cloud core) API calls per month and 10,000 Admin-related Looker (Google Cloud core) API calls per month


An **Enterprise** edition can be purchased through an annual contract.
### Embed edition
The **Embed** edition includes all the features of the **Enterprise** edition as well as offering:
  * 500,000 Query-related Looker (Google Cloud core) API calls per month and 100,000 Admin-related Looker (Google Cloud core) API calls per month


An **Embed** edition can be purchased through an annual contract.
## Non-production instances
If you want to use a staging or testing instance, you can create a non-production instance by using the standard process for creating a Looker (Google Cloud core) instance, and selecting the appropriate non-production edition. The billing for this non-production instance will be the same as for any other Looker (Google Cloud core) instance. See the Looker (Google Cloud core) pricing page for more details.
The types of non-production instance editions are the same as the editions that are available for production instances, and include the following:
  * Standard edition
  * Enterprise edition
  * Embed edition


The functionalities that are available for each non-production edition are the same as the functionalities that are available for the production editions. Non-production Looker (Google Cloud core) instances also can have the same network connection types as production instances. Having the same functionalities in all environments lets you configure your staging environment to match your production environment, and test updates before deploying to your production instance.
### Characteristics of non-production instances
The following are things to know about non-production Looker (Google Cloud core) instances:
  * Non-production instances are not covered by any Google SLAs.
  * Horizontal scaling is not considered a non-production use case. If you need to spread instance load and offer specific geographical distribution across multiple Looker (Google Cloud core) instances for your production use case, you will need to purchase additional instances of the existing production Looker (Google Cloud core) edition.
  * Non-production Looker (Google Cloud core) instances cannot be used in lieu of a production instance or for production purposes.
  * All production and non-production Looker (Google Cloud core) instances adhere to the same release cycle. You can configure your non-production instance maintenance settings to match your production instance maintenance settings.


## Looker (Google Cloud core) features
Learn about Looker (Google Cloud core) features by edition and network connection.
Functionality that is specific to Looker (Google Cloud core) is documented in the Looker (Google Cloud core) documentation. All other Looker functionality, including functionality that is shared between Looker (Google Cloud core) and Looker (original), is documented in the Looker (original) documentation.
Most Looker (Google Cloud core) functionality is the same as Looker (original) functionality, with a few differences. The following section compares Looker (Google Cloud core) features with Looker (original) features.
### Looker (Google Cloud core) features versus Looker (original) features
The following table compares feature support for Looker (Google Cloud core) versus Looker-hosted Looker (original) and customer-hosted Looker (original) instance types.
Comparison Matrix
Filter the table on supported instance types:
Feature | Looker instance type  
---|---  
**Platform features** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
: Create and access reports in Looker | **Yes** | **Yes** | No | Not available for Looker (Google Cloud core) instances that use VPC Service Controls or CMEK. Not all Looker reports features are available on Looker (Google Cloud core) instances. See the Looker reports documentation for details.  
**Gemini in Looker** : Conversational Analytics, LookML assistance, Visualization Assistant | **Yes** | **Yes** | No | Some features may not be supported for Looker (Google Cloud core) instances that use CMEK or VPC Service Controls.  
: Connect to Google Sheets, Looker Studio, Tableau, Open SQL interface, PowerBI, ThoughtSpot, etc. | **Yes** | **Yes** | No |  Complimentary licenses to use Looker Studio Pro are not available for customer-hosted Looker (original) instances. Some BI connectors are not available for private IP only configurations in Looker (Google Cloud core). See the BI Connectors documentation for details.  
Looker Action Hub and Looker Marketplace | **Yes** | **Yes** | **Yes** |  This feature may have limitations for Looker (Google Cloud core) instances that use private IP. Additional configuration may also be necessary for Looker (Google Cloud core) instances that use private IP. Additional configuration may be necessary for customer-hosted Looker (original) instances.  
Schedule data to S3, SFTP, and webhook | **Yes** | **Yes** | **Yes** | This feature may have limitations for Looker (Google Cloud core) instances that use private IP. Additional configuration may also be necessary for Looker (Google Cloud core) instances that use private IP.  
Looker mobile application | **Yes** | **Yes** | **Yes**  
**Yes** | **Yes** | **Yes** | Custom themes are available only for **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
Custom extensions | **Yes** | **Yes** | **Yes** | Custom extensions are available only for **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
Private embedding | **Yes** | **Yes** | **Yes** |  Private embedding is available for all editions of Looker (Google Cloud core).  
Signed embedding | **Yes** | **Yes** | **Yes** |  Signed embedding is available only for the **Embed** edition of Looker (Google Cloud core).  
Labs and legacy pages | **Yes** | No | **Yes** | Some preview features are made available in Looker (Google Cloud core) through allowlists.  
**Security and authentication features** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Security features: private IP, CMEK, VPC Service Controls | No | **Yes** | No | Private IP and VPC Service Controls are available only for **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
No | **Yes** | No  
SAML authentication, OpenID authentication | **Yes** | **Yes** | **Yes**  
Username and password setting for login, LDAP authentication | **Yes** | No | **Yes**  
**IP Allowlist** setting | No | **Yes** | No | For Looker (Google Cloud core), access to the instance is controlled with private IP.  
Ability to sudo as another user | **Yes** | No | **Yes**  
No | **Yes** | **Yes** | FIPS encryption is available only in the **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
Compliance certifications (for example, FedRAMP High and other Assured Workloads products) | No | **Yes** | **Yes** | Compliance certifications are available only in the **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
**LookML development and database connections** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Dialect support | **Yes** | **Yes** | **Yes** | The documentation lists the dialects that are supported by Looker (Google Cloud core) and the dialects that are supported by Looker (original) and customer-hosted Looker (original).  
Customer hosted Git on the public internet | **Yes** | **Yes** | **Yes** | This feature may have limitations for Looker (Google Cloud core) instances that use private IP. Additional configuration may also be necessary for Looker (Google Cloud core) instances that use private IP.  
Looker Continuous Integration | **Yes** | **Yes** | No | Not available for Looker (Google Cloud core) instances that use private IP or CMEK.  
Service agent access to BigQuery | No | **Yes** | No  
SSH tunnels (for on-premises databases) | **Yes** | n/a | **Yes**  
**Logging** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Access to internal database and verbose logs  | No (see note) | No | **Yes** | For Looker-hosted Looker (original) instances, internal database and verbose logs are available only through a Google Cloud support request.  
No | **Yes** | No  
Elite System Activity | **Yes** | **Yes** | No |  Elite System Activity is available only as a paid feature in the Elite version of Looker (original). Elite Style Activity is available only in the **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
**Infrastructure and instance management** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Fully Google Cloud-managed Google service | No | **Yes** | No | Google Cloud support has a much greater ability to troubleshoot issues with the Looker (Google Cloud core) environment, because it is managed on Google Cloud.  
Self-service instance creation | No | **Yes** | No  
No | **Yes** | No  
Startup options | **Yes** | No | **Yes**  
Customer-defined maintenance windows | No | **Yes** | No  
Non-production instances | **Yes** | **Yes** | **Yes** |  Two non-production instances are available for the Elite version of Looker (original). No other Looker (original) versions offer non-production instances. Non-production instances are purchased separately for Looker (Google Cloud core).  
**Yes** | No | No |  This feature is required to migrate from Looker (original) to Looker (Google Cloud core).  
## Set up and administer the Looker (Google Cloud core) instance
Before you can explore data, you must create and configure a Looker (Google Cloud core) instance. The process for setting up a Looker (Google Cloud core) instance is as follows:
  1. Ensure that you have the proper Google Cloud console set up by checking the instance creation prerequisites.
  2. Create a Looker (Google Cloud core) instance.
  3. Set up a database connection.
  4. Write LookML.
  5. Prepare the instance for users.
  6. Add users.
  7. Retrieve and chart data.
  8. Administer the instance from the Google Cloud console and from the Looker (Google Cloud core) instance.


## Use the Google Cloud CLI
Throughout the Looker (Google Cloud core) documentation, there are instructions for using the Google Cloud CLI. Install the gcloud CLI to run gcloud CLI commands.
Additionally, refer to the gcloud CLI reference documentation for information about using these commands with Looker (Google Cloud core).
## Use Terraform
You can use Terraform to execute some Looker (Google Cloud core) administrative tasks. See the Terraform on Google Cloud documentation for more information about how to provision infrastructure on Google Cloud using Terraform. If you are provisioning resources through the Terraform Google Cloud provider, use version 4.75.0+.
## Use the Looker (Google Cloud core) API
View the Looker (Google Cloud core) Admin API reference for information on Looker (Google Cloud core) endpoints for Google Cloud console functionality.
View the Looker API documentation for information on using the API for functionality within a Looker (Google Cloud core) instance.
### Types of Looker (Google Cloud core) API calls
The types of API calls that are defined as **query API calls** are as follows:
  * Calls that are required for automated query pipelines
  * Calls that get data from the client database
  * Calls that run SQL queries or grab results for content


Examples include the following:
  * Run SQL Runner Query
  * Create Dashboard Render Task


The types of API calls that are defined as **admin API calls** are as follows:
  * Calls that are required to build applications, control content across instances, and perform administrative tasks
  * Calls that control the Looker (Google Cloud core) instance
  * Calls that perform content management, permission and user management, instance administration, or pulling content across folders


Examples include:


There are also other types of API calls, which are ignored for metering purposes, that include calls that perform login, logout, and user authentication tasks.
## Release notes and process
Release notes for Looker (Google Cloud core) can be found on the Looker release notes page. To learn about the Looker (Google Cloud core) release process, visit the Looker (Google Cloud core) release overview documentation page.
## Pricing
See the Looker (Google Cloud core) pricing page for details about pricing.
## Support
For support with your Looker (Google Cloud core) instance, see the Getting support for Looker (Google Cloud core) documentation page.
## What's next
  * Looker (Google Cloud core) quickstart overview
  * Create a Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


