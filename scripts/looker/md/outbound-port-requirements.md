# Looker outbound port requirements  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/outbound-port-requirements

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
#  Looker outbound port requirements
Stay organized with collections  Save and categorize content based on your preferences. 
By default, Looker tries to connect to specific outbound ports to support various features. Blocking or disabling these connections on customer-hosted instances may prevent full use of the Looker application. To learn more about what tools and services Looker uses and what their outbound port requirements are, see the following table.
> In addition to those listed on this page, Looker needs ports opened to communicate with your databases. You may also need to open additional ports if you have migrated your internal configuration to a MySQL database or if you have clustered Looker (so the cluster nodes can communicate with each other).
Service | Purpose | Port Requirement  
---|---|---  
Licensing data* | A Looker service that gathers information about how the service is being used to ensure that usage is in compliance with the customer's licensing terms. This information includes metadata about users, roles, database connections, server settings, features used, API usage, and version. | `license.looker.com:443`  
Product usage | A Looker service (Pinger) that gathers pseudonymized usage data about how users are using the Looker product and how well it is performing. This data is analyzed and used to improve the Looker product. Administrators can disable this service for their instance by contacting Looker Support. | `ping.looker.com:443`  
System error reports* | A Looker service that transmits runtime exceptions to Looker internal systems in order for Looker technicians to diagnose issues with the product. These messages are first sent as HTTPS requests, but will fail over to email via a customer's Looker's SMTP settings, if necessary. | `errorssentry.looker.com:9000`  
Looker Marketplace* | The Looker Marketplace is a central location for finding, deploying, and managing many types of Looker content, such as Looker Blocks™, applications, visualizations, and plug-ins. | 
  * For Looker 23.10 and later, `static-a.cdn.looker.app:443` (`https`) 
  * For Looker 23.8 and earlier, `marketplace-api.looker.com:443` (`https`)
  * `*.github.com:22` (`ssh`)
  * `*.github.com:9418` (`git`)

  
Actions* | You can use actions to deliver content to third-party services integrated with Looker via an action hub server. Any data your users send using an action will be processed temporarily on Looker's action server (known as the Action Hub) rather than in your Looker instance. |  `actions.looker.com:443` (if using Looker-hosted Action Hub)  
Looker CDN | Looker-hosted instances load assets from the CDN, a network of servers that stores content in multiple geographic locations to reduce page load time for users. Your data is never stored on these servers; only items that are specific to Looker (such as images) are stored on the CDN. Customer-hosted instances have the option to disable the Load Assets from CDN setting. | 
  * `static-a.lookercdn.com`
  * `static-b.lookercdn.com`

  
Email notifications | A third-party service (SendGrid) that transmits emails from noreply@looker.com and noreply@lookermail.com in order to provide new account welcome emails, forgotten password reset links, and scheduled data delivery for Looker users. If you prefer, you can alter this configuration to use your own SMTP integration instead. |  `smtp.sendgrid.net` on port 587  
LookML storage | A third-party service (GitHub) that allows for the development and storage of a customer's LookML code. If you prefer, you can alter this configuration to use your own Git integration instead. |  `*.github.com:22` (`ssh`)  
In-app guides and in-product messaging | A third-party service (Pendo) that delivers personalized messages to users to help them more easily use the Looker product. This service collects basic pseudonymized usage data in order to personalize messages and guides. Administrators can disable this service for their instance. |  `*.app.pendo.io:80` (from users' browsers)`*.app.pendo.io:443` (from users' browsers)  
Support access | A Looker service that lets Looker technicians troubleshoot problems by permitting authentication into a customer's Looker application. This access is limited to Support use cases and can be disabled when not needed by customers. |  `<instance_name>.looker.com:9999` `auth.looker.com:443`  
* In-Product (cloud-based) Services
Learn more about Looker's product security and privacy policy.
## Next steps
After you have ensured that Looker can access necessary services, you're ready to enable secure database access.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


