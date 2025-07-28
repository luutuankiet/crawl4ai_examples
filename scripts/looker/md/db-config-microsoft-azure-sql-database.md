# Microsoft Azure SQL Database  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-microsoft-azure-sql-database

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
#  Microsoft Azure SQL Database
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Users and security
  * Temp schema setup
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
To learn more about using SSL encryption, see the Microsoft documentation.
## Users and security
Looker authenticates to your database using SQL Database Authentication. Using a domain account is not supported.
To create an account, run the following commands, changing `some_password_here` to a unique, secure password:
```
CREATELOGINlooker
WITHPASSWORD='some_password_here';
USEMyDatabase;
CREATEUSERlookerFORLOGINlooker;
GO

```

Looker must be authorized to detect and stop currently running queries, which requires the following permissions:
```
KILLDATABASECONNECTION
VIEWDATABASESTATE

```

To grant these permissions, run the following command:
```
GRANTKILLDATABASECONNECTIONTOlooker;
GRANTVIEWDATABASESTATEtolooker;

```

## Temp schema setup
Create a schema owned by the Looker user:
```
CREATESCHEMAlooker_scratchAUTHORIZATIONlooker;

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. The following fields have additional information that applies to Microsoft Azure SQL Database:
  * **Dialect** : Select **Microsoft Azure SQL Database**.
  * **Remote Host** and **Port** : Enter the hostname and port (the default port is 1433).
If you need to specify a non-default port other than 1433 and your database requires the use of a comma instead of a colon, you can add `useCommaHostPortSeparator=true` in the **Additional JDBC parameters** field further down in the connection settings, which will allow you to use a comma in the **Remote Host:Port** field. For example:
`jdbc:sqlserver://hostname,1434`


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Feature support
For Looker to support some features, your database dialect must also support them.
Microsoft Azure SQL Database supports the following features as of Looker 25.10:
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
Case sensitive  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes | Yes  
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
Last updated 2025-07-22 UTC.


