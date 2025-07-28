# SAP HANA  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-sap-hana

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Creating the Looker user
    * Granting permissions
    * Setting up a PDT schema
  * Creating the Looker connection to your database
  * Feature support




Was this helpful?
Send feedback 
#  SAP HANA
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Creating the Looker user
    * Granting permissions
    * Setting up a PDT schema
  * Creating the Looker connection to your database
  * Feature support


This page contains information about connecting Looker to SAP HANA and SAP HANA 2+.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Creating the Looker user
Create a Looker database user with a secure password.
```
CREATE USER LOOKER PASSWORD <SOME_PASSWORD>

```

### Granting permissions
Grant read permissions on the schema(s) that you would like to use in Looker.
```
GRANT SELECT ON SCHEMA <YOUR_SCHEMA> TO LOOKER

```

### Setting up a PDT schema
If using PDTs, create a scratch schema for PDTs to be written into.
```
CREATE SCHEMA LOOKER_SCRATCH OWNED BY LOOKER

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Name** : The name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : **SAP HANA** or **SAP HANA 2+**.
  * **Port** : The database port. The default port is 30015.
  * **Host** : Hostname.
  * **Database** : The name of your database.
  * **Username** : The database username.
  * **Password** : The user password.
  * **Schema** : The default schema to use when none is specified. Entering a schema is optional.
  * **Enable PDTs** : Use this toggle to enable persistent derived tables (PDTs). This reveals additional PDT fields and the **PDT Overrides** section for the connection.
  * **Temp Database** : Schema to use for PDTs.
  * **Additional JDBC Parameters** : Any additional SAP HANA JDBC connection properties.
  * **Maintenance Schedule** : A `cron` expression that indicates when Looker should check datagroups and PDTs. Read more about this setting in the Maintenance Schedule documentation.
  * **SSL** : Check to enable SSL.
  * **Verify SSL** : Check to enforce strict hostname verification.
  * **Max connections per node** : The default is 25. This value can be left at the default value initially. Read more about this setting in the Max connections per node section of the **Connecting Looker to your database** documentation page.
  * **Connection Pool Timeout** : The default is 120 seconds.
  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting in the SQL Runner Precache documentation.
  * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the Using time zone settings documentation page for more information.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
Test the connection in SQL Runner. Navigate to SQL Runner, select your connection and schema, and then check if you can see your database tables.
## Feature support
For Looker to support some features, your database dialect must also support them. The following sections show the feature support for SAP HANA and SAP HANA 2+.
### SAP HANA
SAP HANA supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates | Yes  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views | Yes  
Query killing | Yes  
SQL-based pivots  
Timezones  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
### SAP HANA 2+
SAP HANA 2+ supports the following features as of Looker 25.10:
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
SQL-based pivots  
Timezones  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
## Next steps
After completing the database connection, configure authentication options.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


