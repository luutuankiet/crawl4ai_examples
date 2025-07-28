# Customer-hosted installation steps  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/customer-hosted-installation-steps

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Features that require additional configuration




Was this helpful?
Send feedback 
#  Customer-hosted installation steps
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Features that require additional configuration


This page explains how to install the Looker application for customers who are hosting an on-premises Looker deployment. Throughout our documentation, we refer to these as "customer-hosted" deployments.
We also offer the option for Looker to host your Looker deployment. Throughout our documentation we refer to these as "Looker-hosted" deployments. Using a Looker-hosted instance greatly reduces the effort required to install, configure, and maintain the Looker application, because Looker handles all necessary IT functions that are related to the Looker application for you.
Complete the following steps:
  1. Install Looker:
     * Add Looker to your server.
     * Configure Looker startup options.
     * Configure your SSL certificate for proper HTTPS.
     * Consider port forwarding for a cleaner URL.
     * Allow Looker support to access your instance.
     * Set up Looker monitoring.
     * Set up a MySQL backend database.
     * Set up Looker backups.
     * Ensure that Looker can access necessary services.
     * Install rendering software.
     * Determine if your Looker instance can accommodate the Looker Action Hub.
  2. Enable secure database access.
  3. Configure your database for Looker.
  4. Connect Looker to your database.
  5. Test your database connectivity.
  6. Configure Looker sign-in options.


Once your instance is set up, you're ready to get started with development.
## Features that require additional configuration
The following Looker features require additional configuration or software to use:
Feature | Additional configuration or alternative  
---|---  
Install Chromium renderer  
Sending, scheduling, downloading: 
  * Dashboards in PDF or Visualization format
  * Looks in Visualization or HTML format
  * Explores in PNG (Image of Visualization) or HTML format

  
Downloading custom visualizations  
Maintenance tasks: 
  * Updating an instance to a new Looker release
  * Auto-provisioning a new Looker instance
  * Moving to a new host
  * Clustering
  * Configuration management
  * Java memory settings
  * Archiving log files
  * Restoring backups
  * Migrating Looker backend database to MySQL
  * Migrating to AES-256 encryption
  * Changing Looker's encryption keys
  * Enabling Redis cache

  
Elite System Activity | Set up a read replica of the Looker backend database  
Looker Action Hub | To address the potential issue of the Looker Action Hub not being able to communicate with the Looker instance, Looker admins can implement one of the following solutions. The appropriate solution or combination of solutions will depend on the architecture of the Looker instance: 
  1. Enable the `public_host_url` license feature
  2. Allowlist the egress IP address for the Looker Action Hub
  3. Set up a customer-hosted action hub server

  
Unpackaged JDBC drivers | Install JDBC driver  
Load Assets from CDN | Enable the **Load Assets from CDN** admin setting to load assets from the CDN  
Enabling secure database access | If your customer-hosted Looker instance is not on the same private network as its connected database, be sure to secure your data as well, perhaps using one of the following options: 
  1. Configure an IP address allowlist. Add to the allowlist the IP address or addresses where your Looker instance is hosted
  2. Configure SSL encryption
  3. Configure an SSH tunnel

  
Create a backup of a Looker instance | Generate a keystore-independent backup  
Installing tools from the Looker Marketplace | Set up a shared (network) file system  
Auto Install assets from the Looker Marketplace / API Explorer |  If you are installing the API Explorer on a customer-hosted Looker instance, for users to view API examples, the server running the Looker instance must be configured to access the public internet server running at the URL `https://githubusercontent.com`.  
Upgrading from OpenJDK 8 to OpenJDK 11  
Allowing Looker Support to access a customer-hosted deployment | Allowlist the IP address for Looker Support  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


