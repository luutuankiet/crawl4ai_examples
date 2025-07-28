# Looker (Google Cloud core) networking options

**Source:** https://cloud.google.com/looker/docs/looker-core-networking-options

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Public IP connections
  * Private IP connections
    * Private services access
    * Private Service Connect
  * Private IP and public IP configuration
  * How to choose a networking option




Was this helpful?
Send feedback 
#  Looker (Google Cloud core) networking options
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Public IP connections
  * Private IP connections
    * Private services access
    * Private Service Connect
  * Private IP and public IP configuration
  * How to choose a networking option


This page explains the network configuration options for Looker (Google Cloud core) instances.
You set an instance's network configuration during instance creation. It is a good idea to determine what networking options you want to use before beginning your instance creation process. This page also helps you determine which of these options is most appropriate for your organization's needs.
## Overview
The following network configuration options for Looker (Google Cloud core) are available:
  * **public IP**: An instance that uses an external internet accessible IP address.
  * **private IP only**: Private IP only connections use private networks for access to and from Looker (Google Cloud core) instances. There are two options for using private networks:
    * **private services access**: An instance enabled for private services access uses an internal, Google-hosted Virtual Private Cloud (VPC) IP address and uses private services access to connect privately to Google and third-party services.
    * **Private Service Connect**: An instance enabled for Private Service Connect uses an internal, Google-hosted Virtual Private Cloud (VPC) IP address and uses Private Service Connect to connect privately to Google and third-party services.
  * **private IP and public IP**: An instance that supports a public IP address for ingress and an internal, Google-hosted VPC IP address and private services access or Private Service Connect for egress.


When considering a network configuration for your Looker (Google Cloud core) instance, the following information may be helpful as you make your decision:
  * Network configuration must be set when the instance is created. Network configuration can't be changed after instance creation, with one exception: for an instance that uses private IP, public IP can be added or removed after the instance is created.
  * Feature availability varies by network option. See the Feature availability in Looker (Google Cloud core) documentation page for more information.
  * All connections to BigQuery are through Google's private network, regardless of the network configuration.
  * If a third-party identity provider is configured for single-sign on, the user's browser communicates to the identity provider and is then redirected to the Looker (Google Cloud core) instance. As long as the redirect URL is accessible over the user's network, third-party identity providers work for all networking configurations.


Also see the table in the How to choose a networking option section of this documentation page for more information about how to decide on the right networking configuration for your team.
## Public IP connections
Looker (Google Cloud core) deployed as a public IP instance is accessible from an external internet-accessible IP address. In this configuration, northbound (inbound) traffic to Looker (Google Cloud core) is supported in addition to Looker (Google Cloud core) southbound (outbound) access to internet endpoints. This configuration is similar to the configuration of a Looker (original) instance that is hosted by Looker.
Public IP network connections allow only HTTPS traffic into Looker (Google Cloud core). Google auto-provisions an SSL certificate when the CNAME is updated and Google can locate the DIG records. This certificate is automatically rotated every four months. To securely connect to external databases from a public IP Looker (Google Cloud core) instance, you can set up an encrypted SSL connection.
Public IP network connections are straightforward to set up and connect to and don't require advanced network configuration or expertise.
To create a Looker (Google Cloud core) public IP instance, see the Create a public IP Looker (Google Cloud core) instance documentation page.
## Private IP connections
A Looker (Google Cloud core) instance with a private IP network connection uses an internal, Google-hosted VPC IP address. You can use this address to communicate with other resources that can access the VPC. Private IP connections make services reachable without going through the public internet or using external IP addresses. Because they don't traverse the internet, connections over private IP typically provide lower latency and limited attack vectors.
In a private IP configuration, internal certificates are completely managed by Google and aren't exposed to anyone. If you are provisioning a private IP instance with custom certificates, you don't need to manage the internal private certificates. Instead, use your own custom certificate, and ensure that the rotation of that certificate is maintained.
In a private IP only configuration, Looker (Google Cloud core) doesn't have a public URL. You control all northbound (inbound) traffic, and all southbound (outbound) traffic will be routed through your VPC.
If your instance uses only a private IP connection, additional configuration is necessary to set up a custom domain and user access to the instance; use some Looker (Google Cloud core) features; or connect to external resources, such as Git providers. In-house networking expertise is helpful to plan and execute this configuration.
Looker (Google Cloud core) supports the following two options for private IP connections:
  * private services access
  * Private Service Connect


The use of private services access or Private Service Connect must be decided at the time of instance creation.
### Private services access
The use of private services access private IP with Looker (Google Cloud core) must be set at the time of instance creation. Looker (Google Cloud core) instances can optionally include a public IP connection with their private IP (private services access) connection. After creation of an instance that uses private services access, you can add or remove a private IP connection to that instance.
To create a private IP (private services access) connection, you must allocate a `/22` CIDR range in your VPC to Looker (Google Cloud core).
To set up user access to an instance that uses only a private IP (private services access) connection, you must set up a custom domain and configure access to the domain depending on your organization's needs. To connect to external resources, you will need to perform additional configuration. In-house networking expertise is helpful to plan and execute this configuration.
To create a Looker (Google Cloud core) private services access instance, see the Create a private IP instance documentation page.
### Private Service Connect
The use of Private Service Connect with Looker (Google Cloud core) must be set at the time of instance creation.
When used with Looker (Google Cloud core), Private Service Connect differs from private services access in the following ways:
  * Endpoints and backends support public or private access methods.
  * Looker (Google Cloud core) can connect to other Google services, such as Cloud SQL, that are accessible through Private Service Connect.
  * There is no need to allocate large IP blocks.
  * Direct connections allow for transitive communication.
  * There is no need to share a network with other services.
  * Supports multi-tenancy.


Private Service Connect backends can be used to access Looker (Google Cloud core) Private Service Connect instances.
Looker (Google Cloud core) (Private Service Connect) instances use endpoints to connect to Google Cloud or external resources. If a resource is external, a network endpoint group (NEG) and load balancer need to be set up as well. Additionally, each southbound connection to a unique service requires that the service be published using Private Service Connect. On the Looker (Google Cloud core) end, each unique egress connection must be created and maintained for each service that you want to connect to.
In-house networking expertise is helpful to plan and execute Private Service Connect configurations.
For an example of connecting to an external service, see the Looker PSC Southbound HTTPS Internet NEG codelab.
To learn more about Private Service Connect instances, see the Use Private Service Connect with Looker (Google Cloud core) documentation page.
## Private IP and public IP configuration
Looker (Google Cloud core) instances that use private services access or Private Service Connect for their private connection support a private IP and public IP configuration.
A Looker (Google Cloud core) instance that uses private services access and that has both a private IP connection and a public IP connection has a public URL, and all incoming traffic will go through the public IP connection using HTTPS. Outgoing traffic is routed through your VPC, which can be configured to allow only private IP traffic, using HTTPS or encryption. All traffic in transit is encrypted.
A Looker (Google Cloud core) instance that is enabled for Private Service Connect uses a customer-defined IP address accessible in a VPC for ingress. Communication to the VPC and on-premises or multi-cloud workloads use service attachments that you deploy for egress traffic.
A private IP and public IP configuration enables the use of some Looker (Google Cloud core) features that are not available for private IP only configurations, such as the Connected Sheets BI connector.
## How to choose a networking option
The following table shows the feature availability for different networking options.
Network requirements  
---  
**Feature** |  **Public IP** |  **Public and private (PSA)** |  **Private (PSA)** |  **Public and private (PSC)** |  **Private (PSC)**  
Requires IP range allocation for instance creation  | No  | Yes (`/22` per instance, per region)  | Yes (`/22` per instance, per region)  | No  | No   
Cloud Armor  | Yes. Looker (Google Cloud core) uses default Cloud Armor rules, which are managed by Google. These rules are not configurable.  | Yes. Looker (Google Cloud core) uses default Cloud Armor rules, which are managed by Google. These rules are not configurable.  | No  | Yes. Looker (Google Cloud core) uses default Cloud Armor rules, which are managed by Google. These rules are not configurable.  | Supported with customer-managed regional external Application Load Balancer, Private Service Connect backend, and customer-managed Google Cloud Armor   
Custom domain  | Yes  | Supported as a public URL  | Yes  | Supported as a public URL  | Yes   
Northbound access  
**Feature** |  **Public IP** |  **Public and private (PSA)** |  **Private (PSA)** |  **Public and private (PSC)** |  **Private (PSC)**  
Public internet  | Yes  | Yes  | No  | Supported with Google-managed regional external Application Load Balancer | Supported with customer-managed regional external Application Load Balancer, Private Service Connect backend, and custom domain  
VPC peering (private services access)  | No  | Yes  | Yes  | No  | No   
PSC-based routing  | No  | No  | No  |  Supported with the following: 
  * Regional external Application Load Balancer and Private Service Connect backend
  * Regional internal Application Load Balancer and Private Service Connect backend

Global access is supported by Private Service Connect backends, but not by Private Service Connect consumer endpoints.  
Hybrid networking  | No  | Yes  | Yes  | Yes  | Yes   
Southbound access  
**Feature** |  **Public IP** |  **Public and private (PSA)** |  **Private (PSA)** |  **Public and private (PSC)** |  **Private (PSC)**  
Internet  | Yes  | No  | No  | Supported with regional TCP proxy internal load balancer, internet NEG, and Cloud NAT gateway.   
VPC peering (private services access)  | No  | Yes  | Yes  | No  | No   
Private Service Connect-based routing  | No  | No  | No  | Supported with regional TCP proxy internal load balancer and hybrid NEG  
Hybrid networking (multi-cloud and on-premises)  | No  | Yes  | Yes  | Supported with regional TCP proxy internal load balancer, hybrid NEG, and Google Cloud networking products  
Application  
**Feature** |  **Public IP** |  **Public and private (PSA)** |  **Private (PSA)** |  **Public and private (PSC)** |  **Private (PSC)**  
GitHub  | Yes  | Supported with TCP proxy internal load balancer and internet NEG  | Yes. For an example, see the Looker PSC Southbound HTTPS Internet NEG codelab.   
GitHub Enterprise  | No  | Yes  | Yes  | Yes  | Yes   
Cloud SQL  | Yes  | Supported with Cloud SQL deployed in the same VPC as Looker (Google Cloud core)  | Yes  | Yes  | Yes   
BigQuery  | Yes  | Yes  | Yes  | Yes  | Yes   
Embed  | Yes  | Yes  | Yes  | Yes  | Yes   
Marketplace  | Yes  | No  | No  | No  | No   
Connected Sheets  | Yes  | Yes  | No  | Yes  | No   
SMTP  | Yes  | Yes  | Yes  | Yes. Requires southbound connectivity.   
Benefits  
**Feature** |  **Public IP** |  **Public and private (PSA)** |  **Private (PSA)** |  **Public and private (PSC)** |  **Private (PSC)**  
Benefits  | 
  * A publicly accessible URL means that it is straightforward to connect to Looker (Google Cloud core) from other services that need to access the instance or redirect to Looker.
  * No need for advanced network configuration.

| 
* Access Looker (Google Cloud core) through a public URL
* Southbound access to multi-cloud environments is achieved based on IP reachability
| 
  * Private instance for northbound and southbound access
  * Southbound access to multi-cloud environments is achieved based on IP reachability

| 
  * No shared constraints and no IP coordination required between the consumer and producer
  * Subnet allocation for Looker (Google Cloud core) instantiation is not required
  * Explicit access to Looker (Google Cloud core) and endpoints
  * Supports Google-managed external load balancer.

| 
  * No shared constraints and no IP coordination required between the consumer and producer
  * Subnet allocation for Looker (Google Cloud core) instantiation is not required
  * Explicit access to Looker (Google Cloud core) and endpoints
  * Supports public and private access to Looker (Google Cloud core) with the use of Private Service Connect backends

  
Considerations  
**Feature** |  **Public IP** |  **Public and private (PSA)** |  **Private (PSA)** |  **Public and private (PSC)** |  **Private (PSC)**  
Considerations  | If you want a custom URL, you have to configure a fully qualified domain name (for example, `looker.examplepetstore.com`). You cannot have a custom URL like `examplepetstore.looker.com`.  | 
  * Southbound access to on-premises and multi-cloud environment requires firewall updates
  * Deploying Looker (Google Cloud core) in a hub-and-spoke VPC architecture with VPC peering results in non-transitive routing to Looker if accessed over hybrid networking from on-premises or multi-cloud networks
  * Additional infrastructure to connect to public Git (proxy VM, internet NEG, and load balancer)

| 
  * Southbound access to on-premises and multi-cloud environment requires firewall updates
  * Deploying Looker (Google Cloud core) in a hub-and-spoke VPC architecture with VPC peering results in non-transitive routing to Looker if accessed over hybrid networking from on-premises or multi-cloud networks
  * Additional infrastructure to connect to public Git (proxy VM, internet NEG, and load balancer)

| 
  * Public access to Looker (Google Cloud core) is managed by Google.
  * Each southbound endpoint (IP address) requires a Private Service Connect published service.

| 
  * Public access to Looker (Google Cloud core) requires integration with an external Application Load Balancer and Private Service Connect backend
  * Each southbound endpoint (IP address) requires a Private Service Connect published service

  
## What's next
  * Create a public IP Looker (Google Cloud core) instance
  * Create a private IP Looker (Google Cloud core) instance
  * Use Private Service Connect with Looker (Google Cloud core)
  * Create a Looker (Google Cloud core) Private Service Connect instance
  * Follow a tutorial on how to perform a southbound HTTPS connection to GitHub from a PSC.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


