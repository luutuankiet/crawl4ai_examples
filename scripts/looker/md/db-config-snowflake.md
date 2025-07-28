# Snowflake  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-snowflake

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Creating a Looker user on Snowflake
  * Creating the Looker connection to your database
  * Designating Snowflake warehouses on a per-group or per-user basis
  * Managing Snowflake's autosuspend feature
  * Configuring OAuth for Snowflake connections
    * Configuring a Snowflake database for OAuth with Looker
    * Testing the OAuth connection
    * Signing in to Snowflake to run queries




Was this helpful?
Send feedback 
#  Snowflake
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Creating a Looker user on Snowflake
  * Creating the Looker connection to your database
  * Designating Snowflake warehouses on a per-group or per-user basis
  * Managing Snowflake's autosuspend feature
  * Configuring OAuth for Snowflake connections
    * Configuring a Snowflake database for OAuth with Looker
    * Testing the OAuth connection
    * Signing in to Snowflake to run queries


To connect Looker to Snowflake, follow these steps:
  1. Create a Looker user on Snowflake and provision access.
  2. Set up a database connection in Looker.


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Creating a Looker user on Snowflake
We recommend the following commands for creating the Looker user. Make sure to run each line individually, or select the **All Queries** option in the Snowflake connection panel to ensure that all lines are run (by default, Snowflake runs only the lines that are selected):
We recommend adding the `ON FUTURE` keyword to each `GRANT` statement so that newly created objects will have the same permissions without further action being required.
```
-- change role to ACCOUNTADMIN
useroleACCOUNTADMIN;

-- create role for looker
createroleifnotexistslooker_role;
grantrolelooker_roletoroleSYSADMIN;
-- Note that we are not making the looker_role a SYSADMIN,
-- but rather granting users with the SYSADMIN role to modify the looker_role

-- create a user for looker
createuserifnotexistslooker_user
password=enterpasswordhere>;
grantrolelooker_roletouserlooker_user;
alteruserlooker_user
setdefault_role=looker_role
default_warehouse=looker_wh;

-- change role
useroleSYSADMIN;

-- create a warehouse for looker (optional)
createwarehouseifnotexistslooker_wh

-- set the size based on your dataset
warehouse_size=medium
warehouse_type=standard
auto_suspend=1800
auto_resume=true
initially_suspended=true;
grantallprivileges
onwarehouselooker_wh
torolelooker_role;

-- grant read only database access (repeat for all database/schemas)
grantusageondatabasedatabase>torolelooker_role;
grantusageonschemadatabase>.<schema>torolelooker_role;

-- rerun the following any time a table is added to the schema
grantselectonalltablesinschemadatabase>.<schema>torolelooker_role;
-- or
grantselectonfuturetablesinschemadatabase>.<schema>torolelooker_role;

-- create schema for looker to write back to
usedatabasedatabase>;
createschemaifnotexistslooker_scratch;
useroleACCOUNTADMIN;
grantownershiponschemalooker_scratchtoroleSYSADMINrevokecurrentgrants;
grantallonschemalooker_scratchtorolelooker_role;

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. The following setting descriptions contain notes that are specific to Snowflake:
**Database Settings - Host** : Enter the Snowflake hostname. It will look like `<account_name>.snowflakecomputing.com`. Check Snowflake account name examples by region to make sure you use the right value for your deployment.
**Database Settings - Authentication Method** : Select one of the following authentication methods:
  * **Database Account** should be used only by existing customers who need time to transition to a multi-factor authentication method before Snowflake's November 2025 deadline. Specify the **Username** and **Password** of the Snowflake user account that will be used to connect to Looker.
  * **Key Pair** should be used by customers who want to implement Snowflake's key-pair authentication to connect with their database. Specify the user account that will be used to connect to Snowflake in the **Username** field. Upload an unencrypted p8 formatted key file in the **Key Pair File** field; encrypted key files are not supported. Snowflake's documentation describes how to create a private key file.
  * **OAuth** should be used by customers who don't need persistent derived tables (PDTs) and want to configure OAuth for the connection.


**Optional Settings - Enable PDTs** : PDTs are not supported for Snowflake connections that use OAuth authentication. If PDTs are needed, use the **Key Pair** authentication option instead.
**Optional Settings - Additional JDBC parameters** : Add additional JDBC parameters from the Snowflake JDBC driver.
  * Add `warehouse=<YOUR WAREHOUSE NAME>`.
  * Additionally, by default, Looker will set the following Snowflake parameters on each session:
    * `TIMESTAMP_TYPE_MAPPING=TIMESTAMP_LTZ`
    * `JDBC_TREAT_DECIMAL_AS_INT=FALSE`
    * `TIMESTAMP_INPUT_FORMAT=AUTO`
    * `AUTOCOMMIT=TRUE`
You can override each of these parameters by setting an alternative value in the **Additional JDBC parameters** field, for example: `&AUTOCOMMIT=FALSE`


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Designating Snowflake warehouses on a per-group or per-user basis
You can use Looker user attributes to assign separate Snowflake warehouses to individual Looker users or groups. This is useful, for example, if you have users who require different levels of computing power. You can assign a warehouse with greater computing resources to just those users who need it, while assigning a warehouse with lesser resources to users with lesser needs.
To designate warehouses on a per-group or per-user basis, follow these steps:
  1. Add the groups or users in Looker.
  2. Define a user attribute in Looker where the Snowflake warehouse names will be stored. You can give this attribute any name, such as `snowflake_wh`.
  3. In the user attribute that you just defined, assign the warehouse name values to the groups or users that will need different warehouse access.
  4. In the **Additional JDBC parameters** field on the **Connection Settings** page, add the following, replacing `snowflake_warehouse` with the name of the user attribute that you defined:
```
warehouse={{ _user_attributes['snowflake_warehouse'] }}

```

  5. To test the individual connection settings, you can sudo as a user to whom you assigned a warehouse name value.


## Managing Snowflake's autosuspend feature
Snowflake warehouses have an autosuspend feature that is enabled by default. After a specified period, the warehouse will autosuspend. If the warehouse is suspended, all queries produce an error. This error is not visible on dashboards (normally these errors result in no data being shown), but it is visible to any user who queries with the Explore page.
Two methods are typically used to manage this:
  1. Snowflake has an auto-resume feature that will resume the warehouse when it is queried. However, resuming the warehouse can take up to five minutes, causing queries to stop responding for five minutes before being returned. Auto-resume cannot be configured in Looker. Enable this features on the **Warehouses** tab in the Snowflake UI:
  2. If persistent derived tables (PDTs) have been enabled, Looker's default setting is to check for derived table regeneration every 5 minutes. This check will keep Snowflake warehouses active. However, you may want Snowflake to suspend warehouses during non-work hours in order to reduce cost. This can be achieved by modifying the PDT regeneration schedule, as described in the maintenance schedule documentation.


## PDT support
> PDTs are not supported for Snowflake connections that use OAuth.
For persistent derived table support, create a Snowflake user account for PDTs that has write access to your database and the temp schema that Looker will use to create PDTs. On the Looker **Connections Settings** page, on the **Optional Settings** tab under the **Persistent Derived Table (PDT) Settings** section, turn on the **Enable PDTs** toggle. Then, in the **Temp database** field, enter the name of the temp schema that Looker will use to create PDTs.
Note that PDT Overrides are not available for Snowflake connections that use Key Pair authentication.
For Snowflake connections, Looker sets the value for Snowflake's `AUTOCOMMIT` parameter to `TRUE`, which is Snowflake's default value. `AUTOCOMMIT` is required for SQL commands that Looker runs to maintain its PDT registration system.
## Configuring OAuth for Snowflake connections
Looker supports OAuth for Snowflake connections, meaning that each Looker user authenticates to the database with their own OAuth user account.
OAuth lets database administrators perform the following tasks:
  * Audit which Looker users are running queries against the database
  * Enforce role-based access controls using database-level permissions
  * Use OAuth tokens for all processes and actions that access the database, instead of embedding database IDs and passwords in multiple places
  * Revoke authorization for a given user through the database directly


With Snowflake connections that use OAuth, users must sign in again periodically when their OAuth tokens expire. The maximum age of Snowflake OAuth tokens is set through Snowflake itself.
Note the following for database-level OAuth connections:
  * Persistent derived tables (PDTs) are not supported for Snowflake connections with OAuth.
  * If a user lets their OAuth token expire, any Looker schedules or alerts that they own will be affected. To guard against this, Looker will send a notification email to the owner of each schedule and each alert 14 days, 7 days, and 1 day before the token expires. The user can go to their Looker user page to reauthorize Looker to the database and avoid any interruption to their schedules and alerts. See the Personalizing user account settings documentation page for details.
  * Because database connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the Caching queries documentation page.
  * When using OAuth, you cannot switch to different roles in the Snowflake user account. As described in the Snowflake documentation, Snowflake uses the default role of the Snowflake user's account, unless the default role is ACCOUNTADMIN or SECURITYADMIN. Because these roles are blocked for OAuth, Snowflake will instead use the PUBLIC role. See the Snowflake documentation for information.
  * When a Looker admin sudos as another user, the admin will use that user's OAuth access token. If the user's access token is expired, the admin cannot create a new token on behalf of the sudoed user. See the Users documentation page for information on using the `sudo` command.


### Configuring a Snowflake database for OAuth with Looker
To create a Snowflake connection to Looker using OAuth, you must set up the OAuth integration in Snowflake. This requires a Snowflake user account with ACCOUNTADMIN permission.
  1. Run the following command in Snowflake, where `<looker_hostname>` is the hostname of your Looker instance:
```
CREATE SECURITY INTEGRATION LOOKER
  TYPE = OAUTH
  ENABLED = TRUE
  OAUTH_CLIENT = LOOKER
  OAUTH_REDIRECT_URI = 'https://<looker_hostname>/external_oauth/redirect';

```

  2. Get the OAuth client ID and secret by running the following command:
```
SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('LOOKER');

```

The response will have an `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` that you will need later in this procedure.
  3. In Looker, create a new connection to your Snowflake warehouse, as described in the Creating the Looker connection to your database section of this page. When you create the new connection, select the **OAuth** option in the **Authentication** field. When you select the **OAuth** option, Looker displays the **OAuth Client ID** and **OAuth Client Secret** fields.
  4. Paste in the `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` values that you got from your database earlier in this procedure.
  5. Complete the rest of the procedure for Connecting Looker to your database.


### Testing the OAuth connection
Once you configure the Looker connection to your database, you can test the connection itself by doing either of the following:
  * Select the **Test** button at the bottom of the **Connections Settings** page, as described on the Connecting Looker to your database documentation page.
  * Select the **Test** button by the connection's listing on the **Connections** admin page, as described on the Connections documentation page.


Additionally, you can test the connection and deploy it on a model by following these steps:
  1. In Looker, go into Development Mode.
  2. Navigate to the project files for a Looker project that uses your Snowflake connection.
  3. Open a model file and replace the model's `connection` value with the name of the new Snowflake connection, and then save the model file.
  4. Open one of the model's Explores or dashboards, and run a query. When you try to run a query, Looker will prompt you to sign in to Snowflake.
  5. Follow the sign in prompts for Snowflake and enter your Snowflake credentials.


Once you successfully sign in to Snowflake, Looker will return you back to your query. If your query runs correctly, you can commit the new connection value and deploy your changes to production.
### Signing in to Snowflake to run queries
Once the Snowflake connection is set up for OAuth, users will be prompted to sign in to Snowflake before running queries. This includes queries from Explores, dashboards, Looks, and SQL Runner.
Users can also sign in to Snowflake from the **OAuth Connection Credentials** section on their **Account** page.
To sign in to your Snowflake account using Looker, follow these steps:
  1. Click the Looker user menu.
  2. Select **Account**.
  3. In the **Account** page, go to the **OAuth Connection Credentials** section, and select the **Log In** button for the appropriate Snowflake database.


Selecting **Log In** will display a Snowflake login dialog. Enter your Snowflake credentials and select **Log In** , and then select **Allow** to give Looker access to your Snowflake account.
Once you sign in to Snowflake through Looker, you can sign out or re-authorize your credentials at any time through your **Account** page, as described on the Personalizing your user account documentation page.
## Feature support
For Looker to support some features, your database dialect must also support them.
Snowflake supports the following features as of Looker 25.10:
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
Connection pooling | Yes  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures | Yes  
Approximate count distinct  
## Next steps
After you have connected your database to Looker, configure sign-in options for your users.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


