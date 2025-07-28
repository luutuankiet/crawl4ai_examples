# Choosing a hosting option for a Looker (original) instance  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/choosing-hosting-option

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Comparative advantages of each hosting option
  * Benefits and limits of the Looker-hosted option
    * Benefits of Looker-hosted deployments
    * Limits of Looker-hosted deployments
  * Benefits and limits of the customer-hosted option
    * Benefits of customer-hosted deployments
    * Limits of customer-hosted deployments
  * Sample use cases for customer-hosted deployments
  * Support for Looker features across hosting options




Was this helpful?
Send feedback 
#  Choosing a hosting option for a Looker (original) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Comparative advantages of each hosting option
  * Benefits and limits of the Looker-hosted option
    * Benefits of Looker-hosted deployments
    * Limits of Looker-hosted deployments
  * Benefits and limits of the customer-hosted option
    * Benefits of customer-hosted deployments
    * Limits of customer-hosted deployments
  * Sample use cases for customer-hosted deployments
  * Support for Looker features across hosting options


You have the option to host your own Looker (original) instance or deployment, or Looker can host it for you. Throughout our documentation, we refer to instances or deployments that are hosted by Looker as "Looker-hosted" and to instances or deployments that are hosted on-premises as "customer-hosted" or "self-hosted."
When Looker hosts your deployment, Looker manages all necessary IT functions that are related to the Looker application on your behalf, based on resource utilization and business requirements, greatly reducing the effort required to install, configure, and maintain the Looker application. Conversely, when you host your own deployment, you are responsible for managing many of these processes and functions. A customer-hosted deployment includes the in-product services, meaning the services that are hosted by Looker and accessible through the product, specifically licensing data, configuration backups, system error reports, data actions, and support tickets, as further described in the **Application Data Shared by Looker** section of Looker's security page.
Choosing between the two hosting options is a trade-off between convenience and control. Opting for Looker-hosted lets you focus on integrating Looker into your business workloads without the demands of infrastructure administration. Conversely, hosting your own Looker deployment gives you complete control over the infrastructure administration, but increases your overhead for the initial launch and ongoing maintenance.
This page presents the following information to assist you in choosing the most appropriate hosting option for your needs:
  * Comparative advantages of each hosting option
  * Benefits and limits of the Looker-hosted option
  * Benefits and limits of the customer-hosted option
  * Sample use cases for customer-hosted deployments


## Comparative advantages of each hosting option
The following table compares the advantages of each hosting option.
**Benefit** |  **Looker-hosted** |  **Customer-hosted**  
---|---|---  
Default access to all Looker features  
No hardware setup or maintenance required  
Automatic software updates and maintenance (monthly or quarterly)  
Scale hardware at no additional cost:
  * Vertical scaling (more CPU)
  * Horizontal scaling (more nodes)

  
Application and host monitoring  
Automatic Looker instance backups  
Backend database migration, if necessary  
Uptime SLA 99.9% (Advanced & Elite)  
S1 Response SLA 1 hour  
Use of the Looker API  
Multi-instance migrations  
Direct access to and export of servers and logs  
## Benefits and limits of the Looker-hosted option
The following tables list the benefits and limits of using a Looker-hosted deployment.
### Benefits of Looker-hosted deployments
The following table lists the benefits of using a Looker-hosted deployment.
Leave the performance monitoring to the Looker team and focus on making decisions with actionable data insights from Looker.  
---  
Always get the latest features and updates |  You will never have to manually download another update. Your Looker instance is tested, updated, and optimized by Looker.  
Consistent performance |  Looker monitors performance and adjusts capacity as needed. You don't have to decide how many servers you need to support your users.   
Deployment security |  Looker manages your platform infrastructure. Your Looker deployment is discrete, secure, and monitored continuously to keep your data safe.  
Connected services |  Every Looker deployment includes essential connected services that allow you to access more relevant data, increase insights, simplify and scale data modeling, and integrate with third-party systems, all while Looker provides support.  
Secure database connections |  Connect Looker to your database using SSH.  
SAML/LDAP integration |  Looker can integrate with your existing authentication methods.  
### Limits of Looker-hosted deployments
Before you opt to use a Looker-hosted deployment, consider the limits that are listed in the following table.
Specific security/compliance requirements |  The Looker-hosted environment infrastructure may not align with your company's individual security/compliance requirements.   
---|---  
Requirement to have ability to export logs/monitoring information |  Because Looker manages the infrastructure for your instance, you cannot export logs for your instance's usage. Looker manages all monitoring.  
Custom SLAs |  Looker updates and maintenance take place during the pre-defined maintenance windows. Some customers may require additional control over when this maintenance occurs.  
Custom JDBC Drivers |  Custom JDBC drivers must be installed to connect to databases that have lower levels of support.  
## Benefits and limits of the customer-hosted option
The following tables list the benefits and limits to using a customer-hosted deployment.
### Benefits of customer-hosted deployments
The following table lists the benefits of using a customer-hosted deployment.
Direct control over infrastructure and scaling decisions |  You are able to implement infrastructure and architecture configurations that may not be offered with a Looker-hosted deployment.  
---|---  
Access to logging/monitoring |  By managing your own infrastructure, you can directly access and export Looker application logs and set up instance monitoring that suits your individual requirements.   
Bespoke security model |  Hosting Looker in your own deployment allows you complete control over the security of the application environment, which you can align to your company/industry specific security standards.   
### Limits of customer-hosted deployments
Before you opt to use a customer-hosted deployment, consider the limits that are listed in the following table.
Support limitations |  Troubleshooting issues can be challenging when the Looker support team is unfamiliar with custom deployment architecture. Certain issues may require more involvement from your organization.  
---|---  
Monthly update requirements |  You are responsible for creating and maintaining processes that ensure that users are getting the latest features and security patches from Looker.  
Human capital requirements |  Looker deployments can require significant headcount and site reliability engineering expertise. Your organization must manage the various components of a Looker deployment.  
Cost |  Your organization must manage time, human capital, and cloud/datacenter costs.  
Challenges using connected services |  Looker has the benefit of connected services, which allow you to to access relevant industry data, increase insights, simplify and scale data modeling, and integrate with third-party systems. In a self-hosted Looker deployment, you may need to deploy ancillary services in your cloud to access these features.  
Disaster recovery and elasticity |  You will be responsible for maintaining uptime and service resilience.  
Some Looker features are not available |  See the Support for Looker features across hosting options section of this page for a comparison of feature support across Looker's hosting options.  
Additional feature configuration |  Customer-hosted instances may require additional configuration to use certain Looker features.  
## Sample use cases for customer-hosted deployments
A customer-hosted option may be right for your deployment if it aligns with any of the following use cases:
  * Your organization has bespoke security requirements: Some organizations' security policies mandate that they cannot use cloud services. Looker (original) is designed to be multi-cloud, and Looker-hosted Looker (original) deployments reside on various Cloud providers such as Google Cloud, AWS, and Azure. If your security policy is incompatible with using Cloud services with your data, customer-hosting is designed to be the alternative.
  * Your organization prefers a fully customizable deployment model: When Looker hosts your environments, Looker assumes that these environments are intended to be stable. Your organization's requirements may not be compatible with this assumption, such as in the following situations: 
    * Your deployment landscape is a large expanse of numerous instances for each of your user groups or customers, which may only be required for an ephemeral period.
    * Your organization requires the ability to frequently build new environments or tear down existing environments.
    * Your organization requires multiple Looker instances, each requiring custom configurations for the startup flags, model, or connection information.
  * Your organization requires more direct access to integration and configuration capabilities: In a Looker-hosted environment, your direct access to your deployment is limited. Customer-hosted deployments allow for full access to the file system, metadata database, and JVM configurations of your instance. Direct access may be beneficial in the following situations: 
    * Your LookML models and configurations for each instance are frequently updated by using scripts that are synchronized with your development process.
    * Your organization is unable to use certain core technologies that Looker uses to deploy, such as Git. With full control of your instance's backend, you can substitute any core component of Looker with your preferred solution.


## Support for Looker features across hosting options
The following table compares feature support for Looker-hosted Looker (original), Looker (Google Cloud core), and customer-hosted Looker (original) instance types.
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


