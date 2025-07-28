# Amazon Aurora MySQL  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-amazon-aurora-mysql

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Alternate failover and load balancing modes
  * Configuring Amazon Aurora MySQL for PDTs
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  Amazon Aurora MySQL
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Alternate failover and load balancing modes
  * Configuring Amazon Aurora MySQL for PDTs
  * Creating the Looker connection to your database


To connect Looker to Amazon Aurora MySQL, follow the instructions found on the documentation page for connecting to Amazon RDS for MySQL.
In addition to the steps in the Amazon RDS instructions, Amazon Aurora may need further setup, depending on your configuration. If you have a redirected read-only endpoint for Amazon Aurora, or if you want to use persistent derived tables (PDTs), see the following sections.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Alternate failover and load balancing modes
Amazon Aurora MySQL can be configured to use alternate failover and load balancing modes to choose the appropriate JDBC connection behavior you want. Check the linked documentation to see how these alternative parameters change the behavior.
You can set the `lookerFailover` parameter in the **Additional JDBC parameters** field to control these modes.
The options can be used to change the JDBC string as follows:
  * `lookerFailover=false`: `jdbc:mysql:hostname...`
  * `lookerFailover=sequential`: `jdbc:mysql:sequential:hostname...`
    * You can do the same with `lookerFailover=loadbalance`, `lookerFailover=replication`, and `lookerFailover=aurora`
  * If `lookerFailover` is not included, the default behavior is: `jdbc:mysql:aurora:hostname...`
  * If `cluster-ro` is in the hostname, the default behavior is: `jdbc:mysql:hostname...`


## Configuring Amazon Aurora MySQL for PDTs
In order to use persistent derived tables (PDTs) with Aurora, you must use MySQL replication, not Amazon Aurora's default replication, which is read-only. You must set the `read_only` parameter to `0` to make the MySQL replica writable, as described in our documentation on RDS and temporary tables.
If you _don't_ want to grant write access to the database, you can copy and paste the derived table SQL into the `sql_table_name` parameter of a `view` file as shown here. This creates a subquery that is used at query time:
```
view: my_name {
sql_table_name: (sql_of_derived_table_goes_here) ;;
}

```

For more details on Aurora replication, see the AWS documentation.
## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information.
To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Feature support
For Looker to support some features, your database dialect must also support them.
Amazon Aurora MySQL supports the following features as of Looker 25.10:
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


