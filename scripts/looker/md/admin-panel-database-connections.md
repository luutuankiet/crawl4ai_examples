# Admin settings - Connections  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-database-connections

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing connections
  * Testing connections
  * Adding connections
  * Editing connections
  * Actions available for all connections
  * Actions available for some connections




Was this helpful?
Send feedback 
#  Admin settings - Connections
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing connections
  * Testing connections
  * Adding connections
  * Editing connections
  * Actions available for all connections
  * Actions available for some connections


To access the **Connections** page, open the **Admin** menu and, under **Database** , choose **Connections**.
## Viewing connections
On the **Connections** page, you can view your database connections and the IP addresses that are needed to allow network traffic. If the ability to create a new database has been enabled for your instance, you can also add a new connection.
### Databases tab
The **Databases** tab shows basic information about the database connections that you've defined. It also shows any Looker-managed connections that you've created, if the ability to create a new database has been enabled for your instance. You can also test the status of and edit the configuration of those connections from the **Databases** tab.
You can click **Public IP Addresses** to view the list of IP addresses that are needed to allow network traffic from your Looker instance. All network traffic from Looker will come from one of the listed IP addresses, based on the region where your Looker instance is hosted. Prohibiting traffic to your database, except from these and other trusted IP addresses, is a way to limit data access.
The following table describes the elements on the **Databases** tab:
Column | Description  
---|---  
Name | The name of the connection, chosen by you, that is used in the `connection` LookML parameter. When you test the connection, Looker displays the list of status checks under the connection name.  
Database | The name of the database that Looker will query when using this connection.  
Scope | Whether the connection can be used with all projects or only one specific project.  
SSH Server | The name of the SSH server configuration used to create an SSH tunnel to your database. This column shows only if the **SSH Servers** tab is enabled on your Looker instance.  
SSL | Whether or not you are using SSL encryption to protect the data traveling between Looker and your database (there are other secure options besides SSL).  
Type | The SQL dialect of the database connection.  
Actions | Actions that you can take for a connection: test a connection, edit a connection, view other information about a connection, jump to a list of links to the connection's Explores, or delete a connection. If the ability to create a new database has been enabled for your instance, you can also add data from an additional data source to any Looker-managed connections.  
### SSH Servers tab
> The **SSH Servers** tab isn't available for Looker (Google Cloud core) instances.
> The **SSH Server** option is available if a Looker (original) instance is deployed on Kubernetes infrastructure, and only if the ability to add SSH server configuration information to your Looker instance has been enabled. If this option is not enabled on your Looker instance and you would like to enable it, contact a Google Cloud sales specialist or open a support request.
> Looker automatically chooses the localhost port for you when creating SSH tunnels; you cannot specify the localhost port.
> SSH connections to PrestoDB or Trino databases may require additional database configuration. When SSL is enabled, the PrestoDB or Trino database defaults to listening on port 443. To establish the SSH tunnel, Looker must set the localhost port to 443, which is already in use by Looker. This will cause the SSH tunnel setup to fail. To correct the issue, configure your PrestoDB or Trino database to listen on a port other than port 443 when SSL is enabled.
The **SSH Servers** tab lists the SSH server configurations that you have added, indicates the status of connections to the SSH servers, and lists the database connections using each SSH server. From the **SSH Servers** tab, you can also test a connection to an SSH server, and add or edit SSH server configurations.
The following table describes the elements on the **SSH Servers** tab:
Column | Description  
---|---  
Server Name | The name of the SSH server configuration, chosen by you, that is used to connect to your database.  
Connections | A list of the database connections that connect to the SSH server. Clicking a database connection opens the **Edit Connection** page for that database connection.  
Three-dot **Options** menu more_vert | Actions that you can take for an SSH server configuration: test connections to an SSH server, add a database connection to an SSH server, edit an SSH server configuration, or delete an SSH server configuration.  
#### Adding or editing an SSH server configuration
To add a new SSH server configuration:
  1. In the **SSH Server** tab, click **Add Server**
  2. In the **Unnamed Server** field in the top right corner, enter a name for the SSH server configuration.
  3. Click **Download Key** to download the public key to a text file. Be sure to save this file for later use.
  4. In the **Server Username** field, enter the username that Looker will use to connect to the SSH server.
  5. In the **Server IP Address or Hostname** field, enter the SSH server IP address or hostname.
  6. In the **Server Port** field, enter the port number used to connect to the SSH server.
  7. Add the downloaded public key to the authorized key file on your SSH server. See the Using an SSH server documentation page for more information and an example.
  8. Ensure that the appropriate Looker IP addresses are added to the allowlist on your SSH server so that Looker can connect to the SSH server.
  9. Click **Test & Request Fingerprint** to verify your connection to the SSH server.
  10. View the new SSH configuration. On this screen, you can also download or view the public key and view the unique fingerprint of the SSH server configuration.


To edit an existing SSH server configuration, click the three-dot **Options** menu in the row of the selected SSH server, and choose **Server Details**.
#### Testing the connections to an SSH server
To test all database connections to an SSH server:
  1. Click the three-dot **Options** menu in the row of the chosen SSH server.
  2. Choose **Test Connections**.


Looker will test all database connections using that SSH server and display a green checkmark next to the server name and all connections where the connection test passes. A red exclamation point icon indicates that the connection failed the test.
#### Adding a database connection to an SSH server
To add a new database connection using an SSH server:
  1. Click the three-dot **Options** menu in the row of the chosen SSH server.
  2. Choose **Add Connection**.


Looker displays the **Connection Settings** page, with the SSH server listed in the **SSH Server** field.
#### Deleting an SSH server configuration
To delete an SSH server configuration:
  1. Click the three-dot **Options** menu in the row of the SSH server to delete.
  2. Choose **Delete Server**.


## Testing connections
Looker lets you test your existing connections to make sure they are functioning properly. You can also test connections as you add them, as described on the Connecting Looker to your database documentation page.
Each connection test includes a list of status checks to tell you whether Looker can successfully use the database connection.
Potential issues are shown in yellow; errors are shown in red. If a connection "passes", it appears in green.
> Database connections that use OAuth, such as Snowflake and Google BigQuery, require a user login. If you are not logged in to your OAuth user account when you test one of these connections, Looker will show a warning with a **Log In** link. Click the link to enter your OAuth credentials or to allow Looker access to your OAuth account information.
You can check the status of:
  * A single connection by clicking **Test** to the far right of that connection
  * All connections by clicking the **Test All Connections** button at the top of the page


Two checks are common cause for confusion:
  * Can find temp schema
  * Can use persistent derived tables


These checks don't need to pass for Looker to function. However, you do need them to pass to use persistent derived tables, which are a very valuable modeling feature.
## Adding connections
To add a new database connection, follow the steps described on the Connecting Looker to your database documentation page.
## Editing connections
To edit an existing connection, open the **Connections** page by selecting the **Admin** menu, and then, under **Database** , choose **Connections**. Click the **Edit** button for the connection. The same page that you use to create a connection will appear (described on the Connecting Looker to your database documentation page), but with the relevant information already filled out. Make any needed changes, and then click **Update Connection**.
## Actions available for all connections
All connections offer these options from the gear drop-down menu to the far right of each connection:
Option | Description  
---|---  
SQL Runner | This option brings you to Looker's SQL Runner, with the proper connection and schema already selected.  
Explore | This option brings you to a list of basic, automatically-generated Explore options for your connection. These are not based on your customized data models, but they enable some quick reporting on the raw data in your connection's tables. This is typically only useful for getting an idea of table contents before modeling, rather than for the purposes of actual data analysis.  
Delete | To delete an existing connection, click the gear drop-down menu to the far right of a connection and select **Delete**. You'll be given the opportunity to confirm the deletion but, once you do so, it cannot be undone. Accidentally deleting a connection will disable any queries that use it. However, if you re-create a new connection with the same name, functionality will be restored.  
## Actions available for some connections
Depending on the connection dialect, the gear drop-down menu to the right of the connection may offer the following additional options:
Option | Description  
---|---  
Show Tables | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the metadata of your connection. Although this option begins with the schema name, table name, and column count selected, you can manipulate it like any other Looker Explore.  
Show Databases | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the metadata of your connection. Although this option begins with the schema name, catalog name, table count, and column count selected, you can manipulate it like any other Looker Explore.  
Show Processes | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the processes running on this connection, the state they are in, how long they have been running, and other info. This can be useful in helping determine the cause if Looker is running slow, or if a query is not running at all.  
Show PDT Event Log | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the derived table activity for this connection. The available fields are described in more detail on our Persistent derived tables documentation page.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


