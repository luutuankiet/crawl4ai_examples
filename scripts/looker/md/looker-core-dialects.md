# Connecting Looker (Google Cloud core) to your database

**Source:** https://cloud.google.com/looker/docs/looker-core-dialects

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Set up a database connection
  * Using Application Default Credentials to connect to a BigQuery database
    * Service account impersonation
    * Using Application Default Credentials with a BigQuery database in a different Google Cloud project
  * Using Application Default Credentials to connect to a Cloud SQL database
    * Add the impersonated service account to your Cloud SQL database
    * Set up service account impersonation on your Cloud SQL database
    * Additional configuration commands for Cloud SQL for MySQL
    * Additional configuration commands for Cloud SQL for PostgreSQL
    * Create the connection from Looker (Google Cloud core) to your Cloud SQL database
  * Configuring OAuth authentication with BigQuery
  * Supported dialects for Looker (Google Cloud core)
  * Database configuration instructions




Was this helpful?
Send feedback 
#  Connecting Looker (Google Cloud core) to your database
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Set up a database connection
  * Using Application Default Credentials to connect to a BigQuery database
    * Service account impersonation
    * Using Application Default Credentials with a BigQuery database in a different Google Cloud project
  * Using Application Default Credentials to connect to a Cloud SQL database
    * Add the impersonated service account to your Cloud SQL database
    * Set up service account impersonation on your Cloud SQL database
    * Additional configuration commands for Cloud SQL for MySQL
    * Additional configuration commands for Cloud SQL for PostgreSQL
    * Create the connection from Looker (Google Cloud core) to your Cloud SQL database
  * Configuring OAuth authentication with BigQuery
  * Supported dialects for Looker (Google Cloud core)
  * Database configuration instructions


Once your Looker (Google Cloud core) instance has been provisioned, it is listed on the **Instances** page of your Google Cloud project. Click the instance URL to access and authenticate in to the instance.
Once you have logged in to your Looker (Google Cloud core) instance, you can set up a database connection to your Looker (Google Cloud core) instance.
## Set up a database connection
Looker (Google Cloud core) must be connected to a database to enable data exploration. See the list of supported dialects to learn which dialects are supported by Looker (Google Cloud core).
You can create a database connection within a Looker (Google Cloud core) instance if you have one of the following permissions:
  * the Looker Admin role
  * the `manage_project_connections` Looker permission


You can follow the **Set up Looker** guide that appears dynamically within the Looker (Google Cloud core) instance to connect your database, or follow the steps listed on the dialect-specific documentation pages. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information on common fields in the Looker connection setup window.
There are additional steps if you want to set up your Looker (Google Cloud core) connection with any of the following options:
  * **Private IP connection** : If your Looker (Google Cloud core) instance uses a private IP connection, you must configure Private Service Connect or private services access (depending on which connection type the instance uses) to connect it to any of the following types of databases:
    * A database in a different network within Google Cloud
    * A database that is hosted by another cloud service provider
    * An on-premises database
To set up a private connection to databases that are hosted by other cloud service providers, your Google Cloud project must be configured to route traffic to those cloud service providers to allow for data exchange. Learn more about connecting cloud environments on the Patterns for connecting other cloud service providers with Google Cloud documentation page.
  * **Authenticate with Application Default Credentials for BigQuery and Cloud SQL databases** : Looker (Google Cloud core) instances can use Application Default Credentials (ADC) to authenticate into your database, as described in the following sections:
    * Using Application Default Credentials to connect to a BigQuery database
    * Using Application Default Credentials with a BigQuery database in a different Google Cloud project
    * Using Application Default Credentials to connect to a Cloud SQL database
  * **Authenticate to a BigQuery database using OAuth** : For BigQuery connections, Looker (Google Cloud core) can use the OAuth application credentials that your Looker admin used when they created the Looker (Google Cloud core) instance. See the Configuring OAuth authentication with BigQuery section of this page for more information.


## Using Application Default Credentials to connect to a BigQuery database
Looker (Google Cloud core) instances can use Application Default Credentials (ADC) to authenticate when you're setting up a connection to a BigQuery Standard SQL database. When you use ADC, the connection will authenticate to the database by using the credentials of the Looker (Google Cloud core) project's service account.
To use ADC with a BigQuery database, select **Application Default Credentials** in the **Authentication** field of the **Connection Settings** page of the Looker instance. For the full procedure, see the documentation for connecting Looker to a BigQuery database.
If your Looker (Google Cloud core) instance uses persistent derived tables with a BigQuery dataset, you must also grant the Looker service account the BigQuery Data Editor IAM role.
If you're connecting to a BigQuery database that is in a different project from your Looker (Google Cloud core) instance, some additional setup is required. See the Using Application Default Credentials with a BigQuery database in a different Google Cloud project section.
### Service account impersonation
If you want to authenticate to the BigQuery database by using a service account other than the Looker (Google Cloud core) project's service account, you can create a delegated request flow by entering another service account, or a comma-separated chain of service accounts, into the **Impersonated Service Account** field. The Looker (Google Cloud core) service account is automatically used as the first service account in the chain and does not need to be added to the field. The last service account in the chain (also known as the impersonated service account) is the one that authenticates with the database.
When using service account impersonation, do the following:
  * Enable the Service Consumer Management API. 
Enable the API
  * Make sure that all service accounts in the chain, including the Looker (Google Cloud core) project's service account, have the appropriate IAM permissions.
  * Make sure that the impersonated service account has the Service Usage Consumer role, the BigQuery Job User role, and the BigQuery Data Viewer role.


### Using Application Default Credentials with a BigQuery database in a different Google Cloud project
The steps for using ADC for a BigQuery Standard SQL database that is outside the project that houses your Looker (Google Cloud core) instance are the same as those for setting up a connection inside the same project. However, prior to setting up the connection in your Looker (Google Cloud core) instance, your Looker (Google Cloud core) project's service account must have the following IAM roles:
  * BigQuery Data Viewer role for the project that contains the BigQuery dataset.
  * BigQuery Job User role and the Service Usage Consumer role on the billing project listed on the **Connection Settings** page.
  * If your Looker (Google Cloud core) instance uses persistent derived tables with a BigQuery dataset, the service account must also have the BigQuery Data Editor role for the project that contains the BigQuery dataset.


If the Looker (Google Cloud core) service account doesn't already have IAM roles in the project that contains the BigQuery dataset, use the service account's email address when granting roles in that project. To find the service account's email address, go to the **IAM** page in the Google Cloud console and select the **Include Google-provided role grants** checkbox. The email will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. Use that email to grant the proper roles to the service account.
Once the proper roles are granted, follow the steps to use ADC.
You can now use ADC with this BigQuery Standard SQL database. The project attached to the service account that is specified in the **Connection Settings** page will be used for billing and also act as the default project.
## Using Application Default Credentials to connect to a Cloud SQL database
Looker (Google Cloud core) instances can use ADC to authenticate a connection to a Cloud SQL database (either Cloud SQL for PostgreSQL or Cloud SQL for MySQL). When you use ADC to authenticate into your Cloud SQL database, the Google Cloud project where the Cloud SQL database is running is the project that is billed for Looker queries.
For Looker connections to Cloud SQL that use ADC, ADC impersonates a service account or a chain of service accounts to access your database. When you create the Looker connection to your database, you use the **IAM database username(s)** field to specify the service account, or the chain of service accounts, that ADC will impersonate. The Looker service account that was created automatically when you created the Looker (Google Cloud core) instance is automatically used as the first service account in the chain and does not need to be added to the field.
If you want to authenticate to your Cloud SQL database by using a service account other than the Looker service account, you can create a delegated request flow by entering another service account, or a comma-separated chain of service accounts, into the **IAM database username(s)** field.
The last service account in the chain (also known as the _impersonated service account_) is the one that authenticates with the database, and this account must be added as a user on your Cloud SQL database. If you are using the Looker service account as the last service account in the chain (by leaving the **IAM database username(s)** field blank), you must add the Looker service account as a user on your Cloud SQL database.
The following are the general steps for connecting a Cloud SQL for PostgreSQL or Cloud SQL for MySQL database to Looker using ADC:
  1. Add the impersonated service account to your Cloud SQL database.
  2. Set up service account impersonation on your Cloud SQL database.
  3. Connect to your database to run additional configuration commands for Cloud SQL for PostgreSQL or Cloud SQL for MySQL.
  4. Create the Looker connection to your database.


### Add the impersonated service account to your Cloud SQL database
When you create the Looker connection to your database, you use the **IAM database username(s)** field to specify the service account, or the chain of service accounts, that ADC will impersonate to perform actions on your database. The last service account in the impersonation chain is considered the _impersonated service account_.
To use ADC with Cloud SQL, you must add the impersonated service account to your Cloud SQL database:
  * In the default case, if you leave the **IAM database username(s)** field blank, ADC will impersonate the Looker service account. In this case, the Looker service account is the impersonated service account, so you need to add the Looker service account to your Cloud SQL database. See the Create a Looker (Google Cloud core) instance documentation page for information about the Looker service account and for the procedure for viewing the Looker service account email address.
  * If you specify a service account other than the Looker service account, or if you specify a chain of service accounts in the **IAM database username(s)** field, you must add the last service account in the impersonation chain to your Cloud SQL database.


To add a service account to your Cloud SQL database, you must have the Cloud SQL Admin IAM role.
Follow the "Add an IAM user or service account to your database instance" procedure for your database dialect to add the impersonated service account to your Cloud SQL database:
  * Cloud SQL for PostgreSQL


### Set up service account impersonation on your Cloud SQL database
Once you have created the Cloud SQL user on your database, you must set up your Cloud SQL database for service impersonation by performing the following steps:
  1. Follow the procedure to enable the Cloud SQL Admin API.
  2. Make sure that all service accounts in the chain, including the Looker service account, have the appropriate IAM permissions.
  3. Follow the procedure for granting a single role in the Google Cloud console. Grant the following Cloud SQL roles to the impersonated service account that you added to your Cloud SQL database:
     * Cloud SQL Instance User
     * Service Usage Consumer
If you specify a service account other than the Looker service account, or if you specify a chain of service accounts in the **IAM database username(s)** field, grant every service account in the chain the following permission:
     * Service Account Token Creator


### Additional configuration commands for Cloud SQL for MySQL
For Cloud SQL for MySQL, you must connect to your database instance and run the following command on the Cloud SQL for MySQL database:
```
GRANT ALL on DATABASE_NAME.* to 'DATABASE_USER'@'%'

```

Replace the following:
  * DATABASE_NAME: The name of your database.
  * DATABASE_USER: The truncated service account username for the impersonated service account that you added to your Cloud SQL database. The service account will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. Truncate the username by removing the `@` and everything that follows. After truncating, the username would look like `service-<project number>`.


For example, if the service account username is `service-12345678901@gcp-sa-looker.iam.gserviceaccount.com` and the database name is `looker-test`, the command would be as follows:
```
GRANT ALL on looker-test.* to 'service-12345678901'@'%'

```

### Additional configuration commands for Cloud SQL for PostgreSQL
For Cloud SQL for PostgreSQL, you must connect to your database instance and run some configuration commands on the Cloud SQL for PostgreSQL database:
  * Grant the user permissions on your database as described in the Users and security section of the PostgreSQL documentation page.
  * Set the search path for the Looker SQL Runner to use to retrieve metadata from your database, as described in the Setting the `search_path` section of the Looker documentation PostgreSQL page.


### Create the connection from Looker (Google Cloud core) to your Cloud SQL database
To create the connection from Looker to your database, follow these steps:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select **Google Cloud PostgreSQL** or, for Cloud SQL for MySQL, select **Google Cloud SQL**.
  3. In the **Authentication** section, click the **Application Default Credentials** option.
  4. In the **IAM database username(s)** field, specify the service account, or the chain of service accounts, that you want ADC to impersonate to perform actions on your database:
     * If you want Looker to authenticate to the Cloud SQL database by using the Looker (Google Cloud core) project's service account, leave this field blank.
     * If you want Looker to authenticate to the Cloud SQL database by using a service account other than the Looker (Google Cloud core) project's service account, you can create a delegated request flow by entering another service account, or a comma-separated chain of service accounts.
  5. Fill out the rest of the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  6. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  7. To save these settings, click **Connect**.


Once a database connection is set up, you are ready to set up a LookML project.
## Configuring OAuth authentication with BigQuery
To configure OAuth authentication for connections to a BigQuery database on a Looker (Google Cloud core) instance, follow these steps:
  1. Under **Authentication** , select **OAuth**. Looker (Google Cloud core) defaults to using the OAuth application credentials that your Looker admin used when they created the Looker (Google Cloud core) instance. You don't need to manually create or enter a client ID and secret.
  2. Add an additional redirect URI to the **Authorized redirect URIs** field in the instance's OAuth client (or create a new OAuth client with the credentials and add a redirect URI). The redirect URI must use the Looker instance's URL followed by `/external_oauth/redirect`. For background information, see the generating OAuth credentials for BigQuery documentation.


If you want to manually enter different OAuth credentials for this connection, enable the **Manually configure OAuth credentials** toggle, and then fill out the **OAuth Client ID** and **OAuth Client Secret** fields. If you manually enter OAuth credentials, that won't change or update the credentials that were used when the Looker (Google Cloud core) instance was created. Follow the steps in the Configuring a BigQuery database project for OAuth documentation to create and use different credentials.
## Supported dialects for Looker (Google Cloud core)
The following table shows the Looker (Google Cloud core) support for database dialects:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver  
Cloudera Impala with Native Driver  
DataVirtuality  
Databricks | Yes  
Denodo 7  
Denodo 8 | Yes  
Dremio  
Dremio 11+ | Yes  
Exasol  
Firebolt  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | Yes  
Greenplum  
HyperSQL  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+  
Microsoft SQL Server 2012+  
Microsoft SQL Server 2016  
Microsoft SQL Server 2017+ | Yes  
MongoBI  
MySQL  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA  
SAP HANA 2+ | Yes  
SingleStore  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector  
Vertica | Yes  
## Database configuration instructions
Instructions are available for these SQL dialects:
  * Amazon Aurora MySQL
  * Apache Druid 0.18+
  * Apache Hive 3.1.2+
  * Cloudera Impala 3.1+

| 
  * Google BigQuery Standard SQL
  * Google Cloud SQL for MySQL
  * Google Cloud SQL for PostgreSQL
  * Microsoft Azure PostgreSQL
  * Microsoft Azure SQL Database
  * Microsoft Azure Synapse Analytics
  * Microsoft SQL Server 2017+

| 
  * Presto (formerly PrestoDB)
  * Trino (formerly PrestoSQL)

  
---|---|---  
## What's next
  * Configure a Looker (Google Cloud core) instance
  * Manage users within Looker (Google Cloud core)
  * Administer a Looker (Google Cloud core) instance from the Google Cloud console
  * Looker (Google Cloud core) admin settings
  * Use the sample LookML project on a Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


