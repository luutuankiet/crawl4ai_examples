# Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-amazon-redshift

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
  * Setting the search_path
  * Optionally accessing data in S3 using Amazon Redshift Spectrum
  * Creating the Looker connection to your database
  * Feature support
    * Amazon Redshift 2.1+
    * Amazon Redshift Serverless 2.1+




Was this helpful?
Send feedback 
#  Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
  * Setting the search_path
  * Optionally accessing data in S3 using Amazon Redshift Spectrum
  * Creating the Looker connection to your database
  * Feature support
    * Amazon Redshift 2.1+
    * Amazon Redshift Serverless 2.1+


Looker supports connections with Amazon Redshift, Amazon Redshift 2.1+, and Amazon Redshift Serverless 2.1+. 
  * For Amazon Redshift connections, Looker uses the PostgreSQL JDBC driver.
  * For Amazon Redshift 2.1+ and Amazon Redshift Serverless 2.1+ connections, Looker uses the Redshift JDBC driver. 


Optionally, you can also access data from Amazon Redshift using Amazon Redshift Spectrum to access data stored in S3.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
If you're interested in using SSL encryption, see the Amazon Redshift documentation on configuring security options for connections.
## Users and security
First, create your Looker user. Change password to a unique, secure password:
```
CREATE USER looker WITH PASSWORD 'password';

```

See the Amazon Redshift documentation for information about password constraints.
Next, grant the appropriate privileges:
```
GRANT USAGE ON SCHEMA public TO looker;
GRANT SELECT ON TABLE public.table1 TO looker;
GRANT SELECT ON TABLE public.table2 TO looker;
...
GRANT SELECT ON TABLE public.tableN TO looker;

```

To give Looker access to the information schema data that it needs to generate LookML and that it needs for the SQL Runner side bar, run the following commands:
```
GRANT SELECT ON TABLE information_schema.tables TO looker;
GRANT SELECT ON TABLE information_schema.columns TO looker;

```

If you want to `GRANT SELECT` on all of your tables to the `looker` user, execute this query:
```
GRANT SELECT ON ALL TABLES IN SCHEMA public TO looker;

```

For acceptable Redshift performance, it is necessary to set the proper distribution and sort keys. See the Redshift documentation for details.
## Temp schema setup
While logged in to your Redshift database as an admin user, run:
```
CREATE SCHEMA looker_scratch AUTHORIZATION looker;

```

If the `looker_scratch` schema is already created or has bad permissions:
```
ALTER SCHEMA looker_scratch OWNER TO looker;

```

## Setting the search_path
Finally, you should set an appropriate `search_path`, which Looker SQL Runner uses to retrieve certain metadata from your database. Assuming that you have created a user called `looker`, and a temp schema called `looker_scratch`, the command is as follows:
```
ALTER USER looker SET search_path TO '$user',looker_scratch,schema_of_interest,public;
                                                            ^^^^^^^^^^^^^^^^^^
                                                            ^^^^^^^^^^^^^^^^^^
                                             include a comma-separated list of
                                            all schemas you'll use with Looker

```

## Optionally accessing data in S3 using Amazon Redshift Spectrum
You can take full advantage of Amazon Redshift Spectrum's performance from within Looker.
Spectrum significantly extends the functionality and ease of use for Redshift by letting users access data stored in S3, without having to load it into Redshift first. You can even join S3 data to data stored in Redshift, and the Redshift optimizer will take care of maximizing your query performance, optimizing both the S3 and Redshift portions of your query. For information on setting up access using Amazon Spectrum, see the Community post on Using Amazon Redshift's new Spectrum Feature.
## Creating the Looker connection to your database
After completing the database configuration, you can connect to the database by performing the following steps:
  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (You may have to click the back arrow if the **Explore** or **Develop** menu is displayed.)
  2. In the **Admin** menu, select **Connections** , and then click **Add Connection**.
  3. From the **Dialect** drop-down menu, select **Amazon Redshift** , **Amazon Redshift 2.1+** , or **Amazon Redshift Serverless 2.1+**.
  4. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
  5. To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
  6. To save these settings, click **Connect**.


## Feature support
For Looker to support some features, your database dialect must also support them. The following sections show the feature support for Amazon Redshift dialects:
  * Amazon Redshift
  * Amazon Redshift 2.1+
  * Amazon Redshift Serverless 2.1+


### Amazon Redshift
Amazon Redshift supports the following features as of Looker 25.10:
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
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views | Yes  
Period-over-period measures | Yes  
Approximate count distinct | Yes  
### Amazon Redshift 2.1+
Amazon Redshift 2.1+ supports the following features as of Looker 25.10:
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
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views | Yes  
Period-over-period measures | Yes  
Approximate count distinct | Yes  
### Amazon Redshift Serverless 2.1+
Amazon Redshift Serverless 2.1+ supports the following features as of Looker 25.10:
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
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized views | Yes  
Period-over-period measures | Yes  
Approximate count distinct | Yes  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


