# PrestoDB and Trino  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-prestodb-and-trino

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Creating the Looker connection to your database
  * Configuring PrestoDB or Trino for PDTs
  * Configuring OAuth for Trino connections
    * Registering an application
    * Configuring the database to use OAuth
    * Signing in to run queries




Was this helpful?
Send feedback 
#  PrestoDB and Trino
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Creating the Looker connection to your database
  * Configuring PrestoDB or Trino for PDTs
  * Configuring OAuth for Trino connections
    * Registering an application
    * Configuring the database to use OAuth
    * Signing in to run queries


This pages discusses how to connect Looker to PrestoDB or Trino.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Dialect** : Select **PrestoDB** or **Trino**.
> PrestoSQL has been rebranded as Trino. If you're using a Trino version earlier than 352, select **PrestoSQL** from the Looker dialect menu.
  * **Host** : The database hostname.
  * **Port** : The database port. The default port is 8080.
  * **Database** : The "catalog" or "connector," in Presto terms.
  * **Username** : The username of the user who will run queries.
> This information is only sent to the database server if SSL is enabled.
  * **Password** : Password for the user who will run queries.
> This information is only sent to the database server if SSL is enabled.
  * **Schema** : The default schema to use when no schema is specified.
  * **Authentication** : Select **Database Account** or **OAuth** :
    * Use **Database Account** to specify the **Username** and **Password** of the database user account that will be used to connect to Looker.
    * Use **OAuth** if you want to configure OAuth for the connection.
  * **Enable PDTs** : Use this toggle to enable persistent derived tables (PDTs). This reveals additional PDT fields and the **PDT Overrides** section for the connection.
  * **Temp Database** : The schema to write PDTs. (Version 3.50 added PDT support to Presto. See the Configuring PrestoDB or Trino for PDTs section on this page for more information about how to configure Presto for PDT support.)
  * **Additional JDBC parameters** : Any additional parameters from the PrestoDB JDBC driver, Trino JDBC driver, or Starburst JDBC driver.
  * **SSL** : Check to enable SSL connections.
  * **Verify SSL** : Ignore this field. All SSL connections will use the default Java Truststore unless directed to do otherwise with PrestoDB JDBC parameters, the Trino JDBC driver, or the Starburst JDBC driver. Enter these parameters in the **Additional JDBC parameters** field.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
For more information about connection settings, see the Connecting Looker to your database documentation page.
## Configuring PrestoDB or Trino for PDTs
> PDTs are not supported for connections that use OAuth.
PDT support depends on the connector that you're using with PrestoDB or Trino . This section explains the necessary configuration settings for a scratch database. This example assumes the connector you are using is `hive`.
The Hive catalog properties file should contain a few configuration properties, which are described in this section.
The following is required because Presto caches the Hive metastore results, and Looker needs to be able to see the tables right away:
`hive.metastore-cache-ttl = 0s`
These two properties are required because Looker needs to be able to drop and rename PDTs:
```
hive.allow-rename-table=true
hive.allow-drop-table=true

```

For reference, in our internal Presto testing servers we use the following `hive.properties` file, which is used for all Hive schemas:
```
hive.s3.connect-timeout=1m
hive.s3.max-backoff-time=10m
hive.s3.max-error-retries=50
hive.metastore-cache-ttl = 0s
hive.metastore-refresh-interval = 5s
hive.s3.max-connections=500
hive.s3.max-client-retries=50
connector.name=hive-hadoop2
hive.s3.socket-timeout=2m
hive.s3.staging-directory=/mnt/tmp/
hive.s3.use-instance-credentials=true
hive.config.resources=/etc/hadoop/conf/core-site.xml,/etc/hadoop/conf/hdfs-site.xml
hive.parquet.use-column-names=true
hive.allow-drop-table=true
hive.metastore.uri=thrift://<metastore-server>:9083
hive.storage-format=ORC
hive.allow-rename-table=true

```

## Configuring OAuth for Trino connections
Looker supports OAuth for Trino connections, meaning that each Looker user authenticates in to the database and authorizes Looker to run queries on the database with their own OAuth user account.
OAuth lets database administrators perform the following tasks:
  * Audit which Looker users are running queries against the database
  * Enforce role-based access controls using database-level permissions
  * Use OAuth tokens for all processes and actions that access the database, instead of embedding database IDs and passwords in multiple places
  * Revoke authorization for a given user through the database directly


With Trino connections that use OAuth, users must sign in again periodically when their OAuth tokens expire.
Note the following for database-level OAuth connections:
  * If a user lets their OAuth token expire, any schedules or alerts that they own will be affected. To guard against this, Looker will send a notification email to the owner of each schedule and each alert before the current active OAuth token expires. Looker will send these notifications emails 14 days, 7 days, and 1 day before the token expires. The user can go to their Looker user page to reauthorize Looker to the database and avoid any interruption to their schedules and alerts. See the Personalizing user account settings documentation page for details.
  * Because database connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that, instead of using cached results whenever the same query is run within the caching period, Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the Caching queries documentation page.
  * Persistent derived tables (PDTs) are not supported for Trino connections with OAuth.
  * When a Looker admin sudos as another user, the admin will use that user's OAuth access token. If the user's access token is expired, the admin cannot create a new token on behalf of the sudoed user. See the Users documentation page for information on using the `sudo` command.
  * When signing into Azure AD from Looker using OAuth, Looker doesn't display an explicit user consent dialog. By setting up OAuth with Looker, you implicitly consent to your Looker instance accessing your Trino data.


### Registering an application
To enable OAuth for Trino, first register an application using a supported identity provider. Looker only supports Microsoft Entra ID (formerly known as Azure AD) for OAuth with Trino.
**Prerequisites**
  * You must have an Azure subscription.
  * You must have administrative permissions in Microsoft Entra ID.


To register an application, follow these steps:
  1. Go to the Azure Portal and sign in with your credentials.
  2. In the Azure Portal search bar, search for "Microsoft Entra ID" and select it from the results.
  3. In the Microsoft Entra ID service, click **New registration** in the **App registrations** section of the **Manage** category.
  4. Fill out the registration form as follows: 
     * **Name** : Provide a descriptive name for the application, such as `Looker Trino Connection`.
     * **Supported account types** : Select the appropriate option based on how you want to restrict access. For an internal use case, you might select **Accounts in this organizational directory only**.
     * **Redirect URI** : Select the **Web** platform, and then enter your Looker redirect URI. It should look like `https://YOUR_LOOKER_HOSTNAME/external_oath/redirect`.
  5. Click **Register**.
  6. Gather the **Client ID** , **Tenant ID** , and **Client Secret** to enter into your Looker connection later. 
     * You can find the **Client ID** and **Tenant ID** on the **Overview** page.
     * If you don't know your **Client Secret** , you'll need to to create a new one. Click **Certificates & secrets** in the **Manage** section, and then click **New client secret**.
  7. Click **Expose an API** in the **Manage** section.
  8. Next to **Application ID URI** , click **Add**.
  9. Enter your **Client ID**. It should be in the following format: `api://CLIENT_ID`.


Next, follow these steps in the Azure Portal to create a new scope to use with Looker:
  1. Click **Add a scope** in the **Scopes defined by this API** section.
  2. Add a **Scope Name** for the new scope. Looker expects that your scope name will be: `TrinoUsers.Read.All`.
> The name `TrinoUsers.Read.All` implies read-only permissions, but the name itself doesn't actually set or enforce any permissions. Make sure you set up the scope to only allow read access to your database.
  3. Add a **Display name** and **Description**.
  4. In the **Who can consent?** selector, select **Admins and users**.
  5. Click **Add scope**.
  6. In the **Authorized client applications** section, click **Add a client application**.
  7. Enter your **Client ID** and your newly created scope.
  8. Click **Add application**.


Next, to grant Looker the necessary API permissions, follow these steps:
  1. In the **Manage** section, click **API Permissions**.
  2. Click **Add a permission**.
  3. Select the **My APIs** tab at the top.
  4. In the list of app registrations, select the registration that you just created, such as `Looker Trino Connection`.
  5. Select the **Delegated permissions** checkbox.
  6. Select the **TrinoUsers.Read.All** checkbox.
  7. Select **Add permission**.


### Configuring the database to use OAuth
Next, to configure your Trino database to use OAuth, add the following lines to your Trino `config.properties` file. (Replace the first five lines of capitalized variables with your own values.)
  * `YOUR_HTTPS_PORT`
  * `PATH_TO_YOUR_SSL_CERTIFICATE`
  * `YOUR_TENANT_ID`
  * `YOUR_CLIENT_ID`
  * `YOUR_SHARED_SECRET`

```
# enable SSL for OAuth
http-server.https.enabled=true
http-server.https.port=YOUR_HTTPS_PORT
http-server.https.keystore.path=PATH_TO_YOUR_SSL_CERTIFICATE

# enable OAuth 2.0
http-server.authentication.type=oauth2
http-server.authentication.oauth2.issuer=https://sts.windows.net/YOUR_TENANT_ID/
http-server.authentication.oauth2.client-id=NA_required_but_not_used
http-server.authentication.oauth2.client-secret=NA_required_but_not_used

# turn off oidc discovery - Trino will inspect tokens locally instead
http-server.authentication.oauth2.oidc.discovery=false

# URLs that Trino requires for OAuth
http-server.authentication.oauth2.jwks-url=https://login.microsoftonline.com/common/discovery/v2.0/keys
http-server.authentication.oauth2.auth-url=NA_required_but_not_used
http-server.authentication.oauth2.token-url=NA_required_but_not_used

# add audience that matches the Azure AD's Application ID URI
http-server.authentication.oauth2.additional-audiences=api://YOUR_CLIENT_ID

# set shared-secret required for internal Trino communication when authentication is enabled, see: https://github.com/trinodb/trino/issues/12397
# can be generated with the following Linux command: openssl rand 512 | base64
internal-communication.shared-secret=YOUR_SHARED_SECRET

# optionally, allow some insecure http traffic
# http-server.authentication.allow-insecure-over-http=true

```

### Signing in to run queries
Once the database connection is set up to use OAuth, users will be prompted to sign in to Microsoft Entra ID before running queries. This includes queries from Explores, dashboards, Looks, and SQL Runner.
Users can also sign in to Microsoft Entra ID from the **OAuth Connection Credentials** section on their **Account** page.
To sign in to Microsoft Entra ID using Looker:
  1. Click the Looker user menu.
  2. Select **Account**.
  3. On the **Account** page, click **Log In** in the **OAuth Connection Credentials** section.


This action will display a login dialog. Enter your Microsoft Entra ID credentials and select **Log In** to grant Looker access to your database account.
Once you sign in to Microsoft Entra ID through Looker, you can log out or reauthorize your credentials at any time through your **Account** page, as described on the Personalizing your user account documentation page.
### Reference
For more information about configuring your Hive connector, see PrestoDB Hive Connector, Trino Hive Connector, or Starburst Hive Connector.
## Feature support
For Looker to support some features, your database dialect must also support them.
PrestoDB supports the following features as of Looker 25.10:
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
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct | Yes  
Trino supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views  
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
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials | Yes  
Context comments | Yes  
Connection pooling  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct | Yes  
## Next steps
After you have connected your database to Looker, configure sign-in options for your users.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


