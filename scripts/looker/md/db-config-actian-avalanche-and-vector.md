# Actian Avalanche and Vector  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-actian-avalanche-and-vector

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Installing the Ingres JDBC driver
  * Creating the Looker connection to your database
  * Enabling PDT support
  * Feature support
    * Actian Avalanche




Was this helpful?
Send feedback 
#  Actian Avalanche and Vector
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Installing the Ingres JDBC driver
  * Creating the Looker connection to your database
  * Enabling PDT support
  * Feature support
    * Actian Avalanche


To use Looker with Actian Avalanche or Vector, you will need to configure an Ingres driver. These instructions describe that process, assuming use of a startup script that is similar to the examples that are provided on the looker-open-source GitHub page.
You will need to acquire an Ingres driver JAR, include it as part of the startup process, and add an option to tell Looker to access it.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Installing the Ingres JDBC driver
Follow the steps on the Unpackaged JDBC drivers documentation page using the following values:
**driver symbol** : `ingres`
**driver entry** :
```
- name: ingres
  dir_name: ingres
  module_path: com.ingres.jdbc.IngresDriver

```

For the step to put the driver in your dialect's directory, the path to this file will look like this: `looker/custom_jdbc_drivers/ingres/iijdbc.jar`.
## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Actian Avalanche** or **Vector** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Enabling PDT support
It is possible to use persistent derived tables (PDTs) on your database using the **PDT Overrides** section in the **Connection Settings** page.
To enable PDTs:
  1. Create a PDT user in your database for use with the scratch schema, for example `looker_scratch`.
  2. Create a group in your database such as `looker_pdt_group`.
  3. Add both the regular Looker user and the Looker PDT user to the new group.
  4. GRANT SELECT on all tables in the regular Looker user's schema to the PDT user.
  5. In the Looker **Connection Settings** page, in the **PDT Overrides** section, enter the PDT user information.
  6. The PDT user then runs a GRANT SELECT to the `looker_pdt_group` for every table it creates.


## Feature support
For Looker to support some features, your database dialect must also support them.
### Actian Avalanche
Actian Avalanche supports the following features as of Looker 25.10:
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
SQL-based pivots | Yes  
Timezones  
SSL  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
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
### Vector
Vector supports the following features as of Looker 25.10:
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
SQL-based pivots | Yes  
Timezones  
SSL  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


