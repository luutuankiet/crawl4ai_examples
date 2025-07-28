# Private northbound access to a Looker (Google Cloud core) instance using Private Service Connect

**Source:** https://cloud.google.com/looker/docs/looker-core-psc-access

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Create a custom domain
  * Set up a custom domain
    * Before you begin
    * Create a custom domain
    * Update the OAuth credentials
  * Private access to Looker (Google Cloud core)




Was this helpful?
Send feedback 
#  Private northbound access to a Looker (Google Cloud core) instance using Private Service Connect
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create a custom domain
  * Set up a custom domain
    * Before you begin
    * Create a custom domain
    * Update the OAuth credentials
  * Private access to Looker (Google Cloud core)


To use Private Service Connect with Looker (Google Cloud core), the Looker (Google Cloud core) instance must be enabled to use Private Service Connect during instance creation.
This documentation page explains how to use Private Service Connect to configure routing from clients to Looker (Google Cloud core), also called _northbound traffic_.
Private Service Connect lets consumers access managed services privately from inside their VPC network, over hybrid networking, or publicly when it's deployed with an external regional application load balancer. It allows managed service producers to host these services in their own separate VPC networks and offer a private or public connection to their consumers.
When you use Private Service Connect to access Looker (Google Cloud core), you are the service consumer, and Looker (Google Cloud core) is the service producer. Northbound access to Looker (Google Cloud core) requires that the consumer VPC be added as an allowed VPC for the Looker (Google Cloud core) Private Service Connect instance.
This documentation describes setting up and configuring a custom domain, and it provides guidance on accessing Looker (Google Cloud core) using an endpoint for private connectivity.
The recommended deployment for accessing Looker (Google Cloud core) is through an application load balancer with a backend. This setup also allows for custom domain certificate authentication, adding an extra layer of security and control for user access.
## Create a custom domain
The first step after the Looker (Google Cloud core) instance is created is to set up a custom domain and update the OAuth credentials for the instance. The next sections walk you through the process.
When you create a custom domain for private IP (Private Service Connect) instances, the custom domain must meet the following requirements:
  * The custom domain must consist of at least three parts, including at least one subdomain. For example, `subdomain.domain.com`.
  * The custom domain must not contain any of the following: 
    * looker.com
    * google.com
    * googleapis.com
    * gcr.io
    * pkg.dev


## Set up a custom domain
After your Looker (Google Cloud core) instance has been created, you can set up a custom domain.
### Before you begin
Before you can customize the domain of your Looker (Google Cloud core) instance, identify where your domain's DNS records are stored, so that you can update them.
#### Required roles
To get the permissions that you need to create a custom domain for a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project the instance resides in. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
### Create a custom domain
In the Google Cloud console, follow these steps to customize the domain of your Looker (Google Cloud core) instance:
  1. On the **Instances** page, click the name of the instance for which you would like to set up a custom domain.
  2. Click the **CUSTOM DOMAIN** tab.
  3. Click **ADD A CUSTOM DOMAIN**.
This opens the **Add a new custom domain** panel.
  4. Using only letters, numbers, and dashes, enter the hostname of up to 64 characters for the web domain that you would like to use — for example: `looker.examplepetstore.com`.
  5. Click **DONE** on the **Add a new custom domain** panel to return to the **CUSTOM DOMAIN** tab.


Once your custom domain is set up, it is displayed in the **Domain** column on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) instance details page in the Google Cloud console.
After your custom domain has been created, you can view information about it, or delete it.
### Update the OAuth credentials
  1. Access your OAuth client by navigating in the Google Cloud console to **APIs & Services > Credentials** and selecting the OAuth client ID for the OAuth client that is used by your Looker (Google Cloud core) instance.
  2. Click the **Add URI** button to update the **Authorized JavaScript origins** field in your OAuth client to include the same DNS name that your organization will use to access Looker (Google Cloud core). For example, if your custom domain is `looker.examplepetstore.com`, you enter `looker.examplepetstore.com` as the URI.
  3. Update or add the custom domain to the list of **Authorized redirect URIs** for the OAuth credentials that you used when you created the Looker (Google Cloud core) instance. Add `/oauth2callback` to the end of the URI. For example, if your custom domain is `looker.examplepetstore.com`, you enter `looker.examplepetstore.com/oauth2callback`.


## Private access to Looker (Google Cloud core)
After you have set up the custom domain, to access the instance from on-premises or from another cloud provider environment (in other words, through hybrid networking), the following network components are required:
  * Hybrid networking products, such as HA-VPN, Cloud Interconnect, and SD-WAN
  * On-premises or Cloud DNS
  * Proxy-only subnet
  * Internal application load balancer
  * SSL certificate resource


Looker (Google Cloud core) deployed with Private Service Connect supports Private Service Connect network endpoint groups, called _backends_ , that are integrated with Cloud Load Balancing. See the Looker PSC Northbound Regional Internal L7 ALB codelab for instructions on how to privately access a Looker (Google Cloud core) instance that is enabled for Private Service Connect by using a backend.
An example of a Private Service Connect backend network setup is displayed in the following diagram:
### Set up DNS
When setting up DNS, you can use one of the following two options:
  * Update the on-premises DNS to be authoritative for the Looker (Google Cloud core) custom domain that is mapped to the Private Service Connect endpoint IP address.
  * Create a Cloud DNS private zone, create a record set using the IP address allocated for the Private Service Connect endpoint, and enable inbound DNS forwarding to allow your VPC to be authoritative for the Looker (Google Cloud core) custom domain that is mapped to the Private Service Connect endpoint IP address.


## What's next
  * Connect Looker (Google Cloud core) to your database
  * Prepare a Looker (Google Cloud core) instance for users
  * Manage users within Looker (Google Cloud core)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


