# Business Intelligence Security Data Governance | Google Cloud

**Source:** https://cloud.google.com/looker/product/security

# Our shared security partnership
Looker can connect to your organization’s database. Because Looker connects to technology that you are responsible for maintaining, security when using the Looker application is a shared responsibility between Google and you. We publish our security posture and best practices publicly here. If you use embedded analytics functionality, Google has developed security best practices you can leverage to help mitigate security concerns.
#### Application data collected by Looker
While there is no permanent storage of Customer Data in your Looker instance, Looker utilizes a number of first- and third-party tools to provide and help improve the service. Unless stated, all data is located in the United States.
Application security includes:
Licensing data | Looker instances use a cloud service that gathers information about how the instance is being used to ensure that usage is in compliance with the customer’s licensing terms. This information includes metadata about users, roles, database connections, server settings, features used, API usage, and version.  
---|---  
Product usage | Looker uses services to gather pseudonymized usage data about how users are using the Looker product and how well it is performing.  
Configuration backups |  Looker (Google Cloud core) performs configuration backups daily. Users can also initiate a backup of their Looker (Google Cloud core) instance. Looker (original) uses a service that encrypts backups for Looker system’s configuration, which includes saved Looks, query history, encrypted user and database credentials, and Looker user settings. Configuration backups are stored in Google Cloud and retained for 180 days.   
Support access |  Optional Looker service that allows Looker technicians to troubleshoot problems. For Looker (Google Cloud core), customers can grant Support access to their instance for on a time-limited basis to resolve support issues. For Looker (original), customers can enable authentication into their Looker application.  
Data delivery to third-party integrations | The Looker Action Hub and LookML actions are optional Looker services that integrate with or perform tasks in third-party tools. Looker Action Hub forwards data, upon your instruction, to a variety of third-party services of your choosing. Unlike a connector, any data your users send using an action will be processed temporarily on Looker’s managed Action Hub rather than in your Looker instance. LookML actions are LookML parameters that perform field-level tasks in third-party tools, directly from Looker. The Looker Action Hub is available for Looker (Google Cloud core) instances that use a public network connection and for Looker (original) instances.  
Email notifications |  If available, this service transmits emails to provide new account welcome emails, forgotten password reset links, and scheduled data delivery for Looker users. You may configure your own STMP integration. Looker (original) as a hosted service uses Twilio Sendgrid to send SMTP notifications by default.  
LookML storage | Develop and store your LookML code in Looker’s first-party Git repository. Customers can use their own Git repo by updating this configuration.  
In-app guides | Optional third-party service (Pendo) that delivers notices and guides to users to help them more easily use the Looker product. This service collects basic pseudonymized usage data in order to personalize notices and guides. Administrators can disable this service for their instance.  
Support chat and tickets |  For Looker (original) only, optional third-party service (Zendesk) that provides an embedded chat client in order to facilitate product support.  
Licensing data
Looker instances use a cloud service that gathers information about how the instance is being used to ensure that usage is in compliance with the customer’s licensing terms. This information includes metadata about users, roles, database connections, server settings, features used, API usage, and version.
Product usage
Looker uses services to gather pseudonymized usage data about how users are using the Looker product and how well it is performing.
Configuration backups
Looker (Google Cloud core) performs configuration backups daily. Users can also initiate a backup of their Looker (Google Cloud core) instance.
Looker (original) uses a service that encrypts backups for Looker system’s configuration, which includes saved Looks, query history, encrypted user and database credentials, and Looker user settings. Configuration backups are stored in Google Cloud and retained for 180 days. 
Support access
Optional Looker service that allows Looker technicians to troubleshoot problems.
For Looker (Google Cloud core), customers can grant Support access to their instance for on a time-limited basis to resolve support issues.
For Looker (original), customers can enable authentication into their Looker application.
Data delivery to third-party integrations
The Looker Action Hub and LookML actions are optional Looker services that integrate with or perform tasks in third-party tools. Looker Action Hub forwards data, upon your instruction, to a variety of third-party services of your choosing. Unlike a connector, any data your users send using an action will be processed temporarily on Looker’s managed Action Hub rather than in your Looker instance. LookML actions are LookML parameters that perform field-level tasks in third-party tools, directly from Looker. The Looker Action Hub is available for Looker (Google Cloud core) instances that use a public network connection and for Looker (original) instances.
Email notifications
If available, this service transmits emails to provide new account welcome emails, forgotten password reset links, and scheduled data delivery for Looker users.
You may configure your own STMP integration.
Looker (original) as a hosted service uses Twilio Sendgrid to send SMTP notifications by default.
LookML storage
Develop and store your LookML code in Looker’s first-party Git repository. Customers can use their own Git repo by updating this configuration.
In-app guides
Optional third-party service (Pendo) that delivers notices and guides to users to help them more easily use the Looker product. This service collects basic pseudonymized usage data in order to personalize notices and guides. Administrators can disable this service for their instance.
Support chat and tickets
For Looker (original) only, optional third-party service (Zendesk) that provides an embedded chat client in order to facilitate product support.
NOTE: We regularly review both our internal services and third-party service providers to ensure that the data we collect is aligned with the service’s intent, and that the security measures employed meet our high security standards.
#### Google responsibilities
Google’s security responsibilities for Looker (Google Cloud core) are described in the Cloud Data Processing Addendum. For Looker (original), refer to the Data Processing Addendum for Looker Services.
#### Your responsibilities
Your security responsibilities for Looker (Google Cloud core)are described in the Cloud Data Processing Addendum. For Looker (original), refer to the Data Processing Addendum for Looker Services. Details are provided below:
**Cloud security**
You are responsible for configuring secure access between the Looker application and your database. Google provides multiple recommendations on how to configure this access, including:
  * Enabling secure database access using tools like IP allowlisting, SSL/TLS encryption, private network connections (available only for Looker (Google Cloud core)), SSH tunneling (available only for Looker (original)).
  * Setting up the least privileged database account permissions for Looker that still allows it to perform needed functions.


**Product security**
You are also responsible for controlling access and permissions for users of your Looker instance. Google recommends:
  * Setting up user authentication using either a username/password option or, preferably, using a more robust authentication mechanism like two-factor authentication, LDAP, OpenID Connect, Google OAuth, or SAML. Username/password, two-factor authentication and LDAP is available only for Looker (original) instances.
  * Setting up the most restrictive user permissions and content access that still allow people to carry out their work, paying special attention to who has admin privileges.
  * Keeping users in sync between Looker and Cloud Identity when authenticating Looker (Google Cloud core) through third-party identity providers (via SAML or OIDC), and maintaining required permissions.
  * Setting up any API usage in a secure way.
  * Regularly auditing any public access links your users create and restricting the permission to create them, as necessary.


#### Cloud security architecture
**Cloud infrastructure**  
---  
Public cloud facilities | Looker (Google Cloud core) is managed in Google datacenters and the Looker (original) application is managed in public cloud datacenters. These facilities implement various physical and environmental controls to help ensure that Looker customer data is well protected from possible theft or loss.  
Logical separation of data | Looker hosted is architected to logically separate and isolate customer data and reduce cross-tenant exposure risk.  
Data security architecture | Google follows best practices for security architecture. Proxy servers secure access to the Looker application by providing a single point to filter attacks through IP denylisting and connection rate limiting.  
Redundancy | Looker employs Cloud-based distributed services and backup frameworks for hosted customer deployments.  
Availability and durability | Looker (Google Cloud core) is hosted in Google Cloud. Looker (original) can be hosted in a variety of different public cloud data centers across the globe.  
**Monitoring & authentication**  
Access to a customer’s back-end servers | Access to a Looker-hosted back-end environment requires approval and multiple layers of authentication.  
Access to a customer’s Looker application | For Looker (original), customers that use technical support can enable support access.   
Monitored user access | Access to your Looker environment is uniquely identified, logged, and monitored.  
Network and application vulnerability scanning | The Looker front-end application and back-end infrastructure are scanned for known security vulnerabilities at least monthly.  
Centralized logging | Looker (Google Cloud core) stores customer logs within a tennant project of the customer’s Google Cloud project, separating them from any other customer log streams. Logs across the Looker (original) production and corporate environments are collected and stored centrally for monitoring and alerting on possible security events.  
Reputation monitoring/ threat intelligence | Collected logs and network activity are checked against commercial threat intelligence feeds for potential risks.  
Anomaly detection | Anomalous activity, like unexpected authentication activity, triggers alarms.  
**Data security encryption**  
Symmetric AES-256 encryption | Locally-stored sensitive application data, including database connection configurations and cached query data, is encrypted and secured using symmetric AES-256 encryption.  
Secure credential storage & encryption |  Looker (Google Cloud core) instances have an integration with Google Cloud’s Identity and Access Management (IAM) accounts; credential validation occurs via Google Cloud IAM API methods. For Looker (original) usernames and passwords are secured using a dedicated password-based key derivation function (bcrypt) with hashing and salting.  
TLS encryption | Data in transit is encrypted and secured from the user's browser to the application via TLS 1.2+.  
Database in-transit encryption | Looker enables you to configure database connections to your datasources via encrypted TLS 1.2+ or SSH tunnel.  
CMEK integration | The Customer Managed Encryption Keys (CMEK) integration enables Looker users to manage which keys are used to encrypt their sensitive data at rest. Customer-supplied keys are stored in Hashicorp Vault or in the AWS Key Management Service (KMS). CMEK integration is available only for Looker (Google Cloud core) instances.  
**Cloud infrastructure**
Public cloud facilities
Looker (Google Cloud core) is managed in Google datacenters and the Looker (original) application is managed in public cloud datacenters. These facilities implement various physical and environmental controls to help ensure that Looker customer data is well protected from possible theft or loss.
Logical separation of data
Looker hosted is architected to logically separate and isolate customer data and reduce cross-tenant exposure risk.
Data security architecture
Google follows best practices for security architecture. Proxy servers secure access to the Looker application by providing a single point to filter attacks through IP denylisting and connection rate limiting.
Redundancy
Looker employs Cloud-based distributed services and backup frameworks for hosted customer deployments.
Availability and durability
Looker (Google Cloud core) is hosted in Google Cloud. Looker (original) can be hosted in a variety of different public cloud data centers across the globe.
**Monitoring & authentication**
Access to a customer’s back-end servers
Access to a Looker-hosted back-end environment requires approval and multiple layers of authentication.
Access to a customer’s Looker application
For Looker (original), customers that use technical support can enable support access. 
Monitored user access
Access to your Looker environment is uniquely identified, logged, and monitored.
Network and application vulnerability scanning
The Looker front-end application and back-end infrastructure are scanned for known security vulnerabilities at least monthly.
Centralized logging
Looker (Google Cloud core) stores customer logs within a tennant project of the customer’s Google Cloud project, separating them from any other customer log streams. Logs across the Looker (original) production and corporate environments are collected and stored centrally for monitoring and alerting on possible security events.
Reputation monitoring/ threat intelligence
Collected logs and network activity are checked against commercial threat intelligence feeds for potential risks.
Anomaly detection
Anomalous activity, like unexpected authentication activity, triggers alarms.
**Data security encryption**
Symmetric AES-256 encryption
Locally-stored sensitive application data, including database connection configurations and cached query data, is encrypted and secured using symmetric AES-256 encryption.
Secure credential storage & encryption
Looker (Google Cloud core) instances have an integration with Google Cloud’s Identity and Access Management (IAM) accounts; credential validation occurs via Google Cloud IAM API methods.
For Looker (original) usernames and passwords are secured using a dedicated password-based key derivation function (bcrypt) with hashing and salting.
TLS encryption
Data in transit is encrypted and secured from the user's browser to the application via TLS 1.2+.
Database in-transit encryption
Looker enables you to configure database connections to your datasources via encrypted TLS 1.2+ or SSH tunnel.
CMEK integration
The Customer Managed Encryption Keys (CMEK) integration enables Looker users to manage which keys are used to encrypt their sensitive data at rest. Customer-supplied keys are stored in Hashicorp Vault or in the AWS Key Management Service (KMS). CMEK integration is available only for Looker (Google Cloud core) instances.
#### Product security
**Overview**  
---  
Code development | Code development is done through a documented SDLC process that includes guidance on how code is tested, reviewed, and promoted to production.  
Peer review and unit testing of code | Code is peer reviewed before being committed to a release version. Functional and unit tests are performed using automated tools.  
Routine developer training | Developers are regularly trained per Google secure coding practices.  
Code quality tests | Looker utilizes automated tests specifically targeting injection flaws, input validation, and proper CSRF token usage.  
Regular third-party penetration testing | Looker performs regular third-party penetration tests against the Looker application and hosted environment.  
Single sign-on (SSO) | Looker provides SAML-based single sign-on for users, offering support for SSO solutions from Google Apps, OneLogin, and SAML. SAML SSO options are available only for Looker (original) instances.  
LDAP authentication | Looker provides the ability to authenticate users based on Lightweight Directory Access Protocol (LDAP), enabling administrators to link LDAP groups to Looker roles and permissions. LDAP is available only for Looker (original) instances.  
Two-factor authentication | Looker provides the ability to use two-factor authentication via Google Authenticator.  
Responsible disclosure | Looker embraces the security community and operates a responsible disclosure program to facilitate security vulnerability reporting.  
Security due diligence of third-party service providers | All third-party service providers go through an annual security review. For in-app guides, Looker serves the third-party software (Pendo) Javascript. The individual guides are vetted and allowlisted by Looker. When fetching a guide from Pendo, Looker validates that the guide is unchanged using SHA-256 integrity hashes. If there are any changes to the guide after Looker’s review, Looker prevents use of the changed guide.  
VPC-SC integration | VPC-SC integration is available only for Looker (Google Cloud core) instances that have enabled Private IP network connections.  
**Overview**
Code development
Code development is done through a documented SDLC process that includes guidance on how code is tested, reviewed, and promoted to production.
Peer review and unit testing of code
Code is peer reviewed before being committed to a release version. Functional and unit tests are performed using automated tools.
Routine developer training
Developers are regularly trained per Google secure coding practices.
Code quality tests
Looker utilizes automated tests specifically targeting injection flaws, input validation, and proper CSRF token usage.
Regular third-party penetration testing
Looker performs regular third-party penetration tests against the Looker application and hosted environment.
Single sign-on (SSO)
Looker provides SAML-based single sign-on for users, offering support for SSO solutions from Google Apps, OneLogin, and SAML. SAML SSO options are available only for Looker (original) instances.
LDAP authentication
Looker provides the ability to authenticate users based on Lightweight Directory Access Protocol (LDAP), enabling administrators to link LDAP groups to Looker roles and permissions. LDAP is available only for Looker (original) instances.
Two-factor authentication
Looker provides the ability to use two-factor authentication via Google Authenticator.
Responsible disclosure
Looker embraces the security community and operates a responsible disclosure program to facilitate security vulnerability reporting.
Security due diligence of third-party service providers
All third-party service providers go through an annual security review. For in-app guides, Looker serves the third-party software (Pendo) Javascript. The individual guides are vetted and allowlisted by Looker. When fetching a guide from Pendo, Looker validates that the guide is unchanged using SHA-256 integrity hashes. If there are any changes to the guide after Looker’s review, Looker prevents use of the changed guide.
VPC-SC integration
VPC-SC integration is available only for Looker (Google Cloud core) instances that have enabled Private IP network connections.
#### Corporate security
Google has security protocols that are meant to secure Looker office spaces and materials that contain sensitive information.
#### Data security, privacy, & compliance
Google maintains a Compliance team to perform regular assessments, mitigate risks, and review that controls are designed and operating correctly.
**Data security & compliance**  
---  
HIPAA security | Looker customers include HIPAA Covered Entities and Business Associates. Since Looker doesn’t extract your data, we don’t categorize data as sensitive, personal health information, or according to other schemas. Instead, we handle all data according to the same security standards. To support HIPAA compliance, Looker engages with a third-party to perform HIPAA Security Rule audits annually. To assist you with your HIPAA-related security obligations, Looker maintains a Business Associate Agreement (BAA) available to execute as needed.  
Cloud Security Alliance (CSA) STAR assessment | Looker has completed the CSA's Consensus Assessments Initiative Questionnaire (CAIQ), which provides a set of questions a cloud consumer may wish to ask of Looker to ascertain their compliance with the Cloud Controls Matrix and CSA best practices. It is available for download here and will be updated periodically.  
Other security compliance initiatives | Looker (original) also provides options to help you with other compliance efforts. Ask your sales representative for more information.  
Security certifications | Looker products maintain several ISO, SOC, and other well-regarded security certifications through our ongoing compliance program. By maintaining our certifications through multiple annual audits, we demonstrate our commitment to identifying risks and putting in place strong, repeatable controls to ensure that our organization maintains a secure posture. Looker product certifications are listed here, and are available upon request for customers and prospects that have entered into an NDA with Google.  
**Data privacy**  
Determine where Looker is hosted | Looker provides a number of locations where your Looker application and configuration backups can be hosted. For Looker (Google Cloud core) instances, this includes the US, the UK, Hong Kong, and the Republic of Korea. For Looker (original) instances, this includes the US, Japan, Ireland, Germany, Australia, or Brazil.  
**Data security & compliance**
HIPAA security
Looker customers include HIPAA Covered Entities and Business Associates. Since Looker doesn’t extract your data, we don’t categorize data as sensitive, personal health information, or according to other schemas. Instead, we handle all data according to the same security standards. To support HIPAA compliance, Looker engages with a third-party to perform HIPAA Security Rule audits annually. To assist you with your HIPAA-related security obligations, Looker maintains a Business Associate Agreement (BAA) available to execute as needed.
Cloud Security Alliance (CSA) STAR assessment
Looker has completed the CSA's Consensus Assessments Initiative Questionnaire (CAIQ), which provides a set of questions a cloud consumer may wish to ask of Looker to ascertain their compliance with the Cloud Controls Matrix and CSA best practices. It is available for download here and will be updated periodically.
Other security compliance initiatives
Looker (original) also provides options to help you with other compliance efforts. Ask your sales representative for more information.
Security certifications
Looker products maintain several ISO, SOC, and other well-regarded security certifications through our ongoing compliance program. By maintaining our certifications through multiple annual audits, we demonstrate our commitment to identifying risks and putting in place strong, repeatable controls to ensure that our organization maintains a secure posture. Looker product certifications are listed here, and are available upon request for customers and prospects that have entered into an NDA with Google.
**Data privacy**
Determine where Looker is hosted
Looker provides a number of locations where your Looker application and configuration backups can be hosted. For Looker (Google Cloud core) instances, this includes the US, the UK, Hong Kong, and the Republic of Korea. For Looker (original) instances, this includes the US, Japan, Ireland, Germany, Australia, or Brazil.


