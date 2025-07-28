# Quickstart: Create a database connection for a public IP instance  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-core-qs-create-connection

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Navigate to the Connect your database to Looker page
  * Create your database connection




Was this helpful?
Send feedback 
  * On this page
  * Before you begin
  * Navigate to the Connect your database to Looker page
  * Create your database connection


# Create a database connection for a public IP instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Looker (Google Cloud core) must be connected to a database to let users explore data and create content. Learn how to create a database connection for a Looker (Google Cloud core) public IP instance to use as the basis for any LookML project, or for a specific LookML project.
See the Connecting Looker (Google Cloud core) to your database documentation page for instructions on creating a database connection for a private IP connection. See the BigQuery default connection for Looker (Google Cloud core) quickstart to use the BigQuery Quickstart Connection to create a default BigQuery connection that can use Application Default Credentials.
## Before you begin
To follow along with this quickstart, you'll need the following:
  * Access to a Looker (Google Cloud core) instance.
  * You must have the **Looker Admin** role or have the `manage_project_connections` Looker permission.
  * A database dialect that is compatible with Looker (Google Cloud core). For a list of compatible dialects, see Supported dialects for Looker (Google Cloud core).


## Navigate to the Connect your database to Looker page
  1. On the Looker (Google Cloud core) homepage, click the **Create** button in the main navigation menu to open the drop-down menu.
  2. From the drop-down menu, select **Connection** to open the **Connect your database to Looker** page.


## Create your database connection
On the **Connect your database to Looker** page, complete the following steps:
  1. In the **Name** section, enter a name for your connection. This name will appear in the **Connection** field of the **Create a Model** page, as well as the **Connections** page.
  2. In the **Connection Scope** section, select **All Projects** to create a connection that will be used for all LookML projects in your Looker (Google Cloud core) instance, or select **Selected Project** to create a connection that will be used only for the LookML project that you specify.
  3. If you chose **Selected Project** in the **Connection Scope** section, select the project that you want to use this connection for.
  4. In the **Dialect** section, choose the appropriate dialect for your database. You can also begin typing the dialect name and Looker will display suggestions for the dialect names that match what you've typed.
  5. Once you select a dialect for the connection, Looker displays the connection settings fields that apply to your database dialect. Fill in the subsequent settings that Looker displays:
     * The majority of the connection settings are common to most database dialects. For descriptions of common database settings, see the Connecting Looker to your database documentation page.
     * For instructions for your specific dialect, see the Connecting Looker (Google Cloud core) to your database documentation page.
  6. In the **Optional Settings** section, expand or collapse the sections to see and configure the available options for your database connection. You can also click **Expand all** to expand all the sections.
  7. To test your connection configuration settings, click **Test**. If your connection is configured correctly, you'll see a green check mark.
  8. To create your connection, click **Create**.


You can view and manage the connection on the **Connections** admin page.
## What's next
  * Generate a model from sample data quickstart
  * Looker IDE overview
  * Managing LookML files and folders
  * Common LookML patterns
  * Using version control and deploying


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


