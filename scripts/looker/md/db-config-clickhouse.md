# ClickHouse  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-clickhouse

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Users and security
  * Creating the Looker connection to your database




Was this helpful?
Send feedback 
#  ClickHouse
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Users and security
  * Creating the Looker connection to your database


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
To enable SSL encryption on the server side, see the ClickHouse Global Server Settings documentation.
## Users and security
First, configure your Looker user on the ClickHouse server. ClickHouse database users are not created with the `CREATE USER` command. Follow the ClickHouse access rights documentation to configure the `users` section in the `users.xml` file. Here is a basic example:
```
<!-- Users and ACL. -->
<users>
    <looker>
        <password>CHANGEIT</password>
        <networks incl="networks" />
        <profile>default</profile>
        <quota>default</quota>
    </looker>

    <web>
        <password></password>
        <networks incl="networks" />
        <profile>web</profile>
        <quota>default</quota>
        <allow_databases>
           <database>test</database>
        </allow_databases>
        <allow_dictionaries>
           <dictionary>test</dictionary>
        </allow_dictionaries>
    </web>
</users>

```

Also within this file, configure the appropriate database access.
```
<allow_databases>
    <database>database_1</database>
    <database>database_2</database>
    <database>database_3</database>
</allow_databases>

```

## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. Some of the settings are described next:
  * **Dialect** : ClickHouse.
  * **Host** : Reachable hostname.
  * **Port** : Port on which the ClickHouse service is reachable over HTTP(S). 
    * By default, HTTP connections will use 8123, and HTTPS will use 8443.
    * Port 9000 and 9440 are by default used by the ClickHouse command line client, but these ports cannot be used by Looker to connect to ClickHouse.
    * Your ClickHouse administrator may have chosen alternate ports with the `http_port/https_port` settings in the ClickHouse configuration. Ask your ClickHouse admin for the settings appropriate to your local configuration.
  * **Database** : Database name (must be one of the databases allowed in the `users.xml` file).
  * **Username** : Database username.
  * **Password** : Database password.
  * **Additional JDBC parameters** : (Optional) Additional JDBC string parameters.
  * **Maintenance Schedule** : ClickHouse does not support PDTs, so this setting can be ignored.
  * **SSL** : Check to connect to ClickHouse over SSL.
  * **Verify SSL** : (Optional) Check to enforce strict hostname verification on the ClickHouse server. Check this only if you are using an SSL certificate that is signed by a generally trusted Certificate Authority. If you are using a self-signed SSL certificate, leave it unchecked.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Feature support
For Looker to support some features, your database dialect must also support them.
ClickHouse supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric aggregates  
Derived tables | Yes  
Persistent SQL derived tables  
Persistent native derived tables  
Stable views  
Query killing | Yes  
SQL-based pivots  
Timezones  
SSL | Yes  
Subtotals  
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
SQL Explain  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches  
Aggregate awareness  
Incremental PDTs  
Milliseconds  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


