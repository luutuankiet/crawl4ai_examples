# Greenplum  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-greenplum

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Greenplum
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
If you're interested in using SSL encryption, see this official Greenplum security configuration guide.
## Users and security
Change `some_password_here` to a unique, secure password:
```
CREATE USER looker WITH ENCRYPTED PASSWORD 'password';
GRANT CONNECT ON DATABASE database_name to looker;
\c database_name
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO looker;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO looker;

```

To grant Looker the necessary permissions to cancel its queries, run the following command:
```
CREATE OR REPLACE FUNCTION pg_kill_connection(integer) RETURNS boolean AS 'select pg_terminate_backend($1);' LANGUAGE SQL SECURITY DEFINER;

```

## Temp schema setup
Create a schema owned by the Looker user:
```
CREATE SCHEMA looker_scratch AUTHORIZATION looker;

```

## Creating the Looker connection to your database
Follow these steps to create the connection from Looker to your database:
  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Greenplum** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them.
Greenplum supports the following features as of Looker 25.10:
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
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type | Yes  
Percentile | Yes  
Distinct percentile | Yes  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling | Yes  
HLL sketches  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views  
Period-over-period measures  
Approximate count distinct  
## Next steps
After completing the database configuration, you can connect to the database from Looker.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


