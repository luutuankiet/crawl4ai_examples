# Databricks  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-databricks

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Create a Looker user
  * Server information
  * Setting up persistent derived tables
  * Creating the Looker connection to your database
  * Looker functionality with Databricks Unity Catalog
  * Configuring OAuth for Databricks connections
    * Enabling a custom OAuth application in Databricks
    * Configure the connection in Looker




Was this helpful?
Send feedback 
#  Databricks
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Create a Looker user
  * Server information
  * Setting up persistent derived tables
  * Creating the Looker connection to your database
  * Looker functionality with Databricks Unity Catalog
  * Configuring OAuth for Databricks connections
    * Enabling a custom OAuth application in Databricks
    * Configure the connection in Looker


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Create a Looker user
Looker authenticates to Databricks by personal access tokens. Follow the Databricks documentation to create a personal access token for a Databricks user to use in Looker.
Add permissions to this user with `GRANT`.
At a minimum, the Looker user should have the `SELECT` and `READ_METADATA` permissions.
```
GRANTSELECTONDATABASEYOUR_DATABASE>TO`<looker>@<your.databricks.com>`
GRANTREAD_METADATAONDATABASEYOUR_DATABASE>TO`<looker>@<your.databricks.com>`

```

## Server information
Follow the Databricks documentation to find the **HTTP Path** for your Databricks cluster. This will be referred to as `<YOUR_HTTP_PATH>` on this page.
## Setting up persistent derived tables
To use persistent derived tables, create a separate database.
```
CREATEDATABASEYOUR_SCRATCH_DATABASE>

```

This will also require additional write-based user permissions to be granted.
```
GRANTSELECTCREATEMODIFYONDATABASEYOUR_SCRATCH_DATABASE>TO`<looker>@<your.databricks.com>`
GRANTREAD_METADATAONDATABASEYOUR_SCRATCH_DATABASE>TO`<looker>@<your.databricks.com>`

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : Specify the dialect **Databricks**.
  * **Host** : Specify the Databricks workspace URL. For example, `dbc-yyyyyyyy.cloud.databricks.com/`.
  * **Port** : Specify the database port. The default is 443.
  * **Database** : Specify the name of the database to use for Looker queries. The default value is `default`.
  * **Catalog** : For Databricks databases with Unity Catalog enabled, specify the name of the catalog to use for Looker queries. If you don't specify a catalog, Looker will access schemas from the default catalog only. See Looker functionality with Databricks Unity Catalog for more information.
  * **Authentication** : Select **Database Account** or **OAuth** : 
    * Use **Database Account** to specify a Databricks personal access token that will be used to connect to Looker (see the Create a Looker user section for instructions). 
      * For **Username** , enter the value `token` (do not enter the Databricks user email in this field).
      * For **Password** , enter the Databricks personal access token.
    * Use **OAuth** to configure OAuth for the connection. See the Configuring OAuth for Databricks connections section for more information.
  * **Enable PDTs** : Use this toggle to enable persistent derived tables. When PDTs are enabled, the **Connection** window reveals additional PDT settings and the **PDT Overrides** section. Note: PDTs are not supported for Databricks connections that use OAuth.
  * **Temp Database** : Enter the database you would like to use to store PDTs.
  * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the Connecting Looker to your database documentation page.
  * **Additional JDBC parameters** : Add any additional Spark JDBC parameters.
  * **Maintenance Schedule** : A `cron` expression that indicates when Looker should check datagroups and persistent derived tables. Read more about this setting in the Maintenance Schedule documentation.
  * **SSL** : Check to use SSL connections.
  * **Verify SSL** : Check to enforce strict SSL certificate verification.
  * **Max connections per node** : You can leave this setting at the default value initially. Read more about this setting in the Max connections per node section of the **Connecting Looker to your database** documentation page.
  * **Connection Pool Timeout** : You can leave this setting at the default value initially. Read more about this setting in the Connection Pool Timeout section of the **Connecting Looker to your database** documentation page.
  * **SQL Runner Precache** : To cause SQL Runner to not preload table information and to load table information only when a table is selected, clear this checkbox. Read more about this setting in the SQL Runner Precache section of the **Connecting Looker to your database** documentation page.
  * **Database Time Zone** : Specify the time zone to be used in the database. Leave this field blank if you don't want time zone conversion. See the Using time zone settings documentation page for more information.


Click **Test** to test the connection and make sure that it is configured correctly. If you see **Can Connect** , then press **Connect**. This runs the rest of the connection tests to verify that the service account was set up correctly and with the proper roles. See the Testing database connectivity documentation page for troubleshooting information.
## Looker functionality with Databricks Unity Catalog
Looker supports connections to Databricks databases with Unity Catalog enabled. You can specify the catalog name in the **Catalog** field of the Looker **Connection** window when you create a Looker connection to your database, or when you edit an existing Looker connection to a Databricks database.
If your Databricks database is enabled for Unity Catalog, you can specify a Databricks catalog in the **Catalog** field of the Looker connection. When you specify a Databricks catalog, Looker uses the catalog in the following scenarios:
  * When generating a new LookML project from your database, Looker will create the project files based on the tables in your connection's configured catalog.
  * For existing projects, when using the Looker IDE to create a view from a table, Looker will create view files only from the tables in your connection's configured catalog.
  * When using SQL Runner, you can select only schemas from your connection's configured catalog.


If your Databricks database is enabled for Unity Catalog and the Looker connection doesn't have a value in the **Catalog** field, most Looker functionality will access schemas from the default catalog only, such as in the following scenarios:
  * When generating a new LookML project from your database, Looker will create the project files based on the tables in the Unity Catalog default catalog.
  * For existing projects, when using the Looker IDE to create a view from a table, Looker can create view files only from the tables in the Unity Catalog default catalog.
  * When using SQL Runner, you can select only schemas from the Unity Catalog default catalog.


## Configuring OAuth for Databricks connections
Looker supports OAuth for Databricks connections, meaning that each Looker user authenticates in to the database and authorizes Looker to run queries on the database with the user's own OAuth user account.
OAuth lets database administrators perform the following tasks:
  * Audit which Looker users are running queries against the database
  * Enforce role-based access controls by using database-level permissions
  * Use OAuth tokens for all processes and actions that access the database, instead of embedding database IDs and passwords in multiple places
  * Revoke authorization for a given user through the database directly


With Databricks connections that use OAuth, users must sign in again periodically when their OAuth tokens expire.
Note the following for database-level OAuth connections:
  * If a user lets their OAuth token expire, any Looker schedules or alerts that the user owns will be affected. To guard against this, Looker will send a notification email to the owner of each schedule and each alert before the current active OAuth token expires. Looker will send these notifications emails 14 days, 7 days, and 1 day before the token expires. The user can go to their Looker user page to reauthorize Looker to the database and avoid any interruption to their schedules and alerts. See the Personalizing user account settings documentation page for details.
  * Because database connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that, instead of using cached results whenever the same query is run within the caching period, Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the Caching queries documentation page.
  * Persistent derived tables (PDTs) are not supported for Databricks connections with OAuth.
  * When a Looker admin sudos as another user, the admin will use that user's OAuth access token. If the user's access token is expired, the admin cannot create a new token on behalf of the sudoed user. See the Users documentation page for information on using the `sudo` command.
  * When a user signs in to Databricks from Looker using OAuth, Looker doesn't display an explicit user consent dialog. By setting up OAuth with Looker, you implicitly consent to your Looker instance accessing your Databricks database.
  * To use OAuth for a Databricks connection, you must have Databricks users or service principals that can be used for Looker queries, and you must provide the users and service principals with the Databricks permissions that Looker will need to access the data sources and perform the required actions within Databricks.


To create a Databricks connection to Looker using OAuth, you must perform these general steps, which are detailed in the following sections:
  1. Enable a custom OAuth application in Databricks
  2. Configure the connection in Looker


### Enabling a custom OAuth application in Databricks
To use OAuth for a Looker connection to Databricks, you must enable Looker as a custom OAuth application for your Databricks database by following these steps:
  1. Sign in to the Databricks account console.
  2. Click the **Settings** icon in the side panel.
  3. Click the **App Connections** tab in the **Settings** window.
  4. In the **App Connections** tab, click **Add connection**.
  5. Enter the following values in the Databricks **Add connection** dialog:
     * **Application Name** : Provide a descriptive name, such as "Looker Integration".
     * **Redirect URLs** : Enter the Looker URL where Databricks will redirect users after successful authorization, using this format (replace `example.looker.com` with the URL of your Looker instance):
```
https://example.looker.com/external_oauth/redirect

```

     * **Access scopes** : Select **SQL** to allow Looker to query data through SQL.
     * **Generate a client secret** : Enable this option.
  6. Click **Add** in the Databricks **Add connection** dialog.
  7. Copy and securely store the **Client ID** and **Client Secret** that Databricks generates.


Registering an OAuth application may take up to 30 minutes to process on the Databricks database. For more information, see the official Databricks documentation.
### Configure the connection in Looker
After you have configured Looker as a custom OAuth application on your Databricks database, you can configure a Looker connection to Databricks that uses OAuth.
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details, as described in the Creating the Looker connection to your database section of this page.
  3. Select the **OAuth** option in the **Authentication** field.
  4. When you select the **OAuth** option, Looker displays the **OAuth Client ID** and **OAuth Client Secret** fields. For these values, enter the **Client ID** and **Client Secret** that was generated by Databricks when you enabled Looker as a custom OAuth application in Databricks.
  5. Select the **Test** button at the bottom of the **Connections Settings** page to ensure that Looker can successfully establish the OAuth flow and connect to your Databricks instance.


## Feature support
For Looker to support some features, your database dialect must also support them.
Databricks supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views | Yes  
Query killing | Yes  
SQL-based pivots | Yes  
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials | Yes  
Context comments | Yes  
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


