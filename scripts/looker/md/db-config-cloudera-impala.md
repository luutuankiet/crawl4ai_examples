# Cloudera Impala 3.1+ and Cloudera Impala with Native Driver  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-cloudera-impala

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Dialects that use these instructions
  * Encrypting network traffic
  * Configuring Looker to connect to Cloudera Impala
    * Connecting to a cluster without Kerberos or user authentication
    * Connecting to a cluster requiring LDAP authentication
    * Connecting to a cluster secured with Kerberos, but not using Apache Sentry
  * Creating the Looker connection to your database
  * Permissions for PDTs
  * Feature support
    * Cloudera Impala with Native Driver
    * Cloudera Impala 3.1+
    * Cloudera Impala 3.1+ with Native Driver




Was this helpful?
Send feedback 
#  Cloudera Impala 3.1+ and Cloudera Impala with Native Driver
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Dialects that use these instructions
  * Encrypting network traffic
  * Configuring Looker to connect to Cloudera Impala
    * Connecting to a cluster without Kerberos or user authentication
    * Connecting to a cluster requiring LDAP authentication
    * Connecting to a cluster secured with Kerberos, but not using Apache Sentry
  * Creating the Looker connection to your database
  * Permissions for PDTs
  * Feature support
    * Cloudera Impala with Native Driver
    * Cloudera Impala 3.1+
    * Cloudera Impala 3.1+ with Native Driver


## Dialects that use these instructions
Looker connects to the following Impala databases:
  * Cloudera Impala 3.1+
  * Cloudera Impala 3.1+ with Native Driver
  * Cloudera Impala with Native Driver


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Configuring Looker to connect to Cloudera Impala
Looker connects to databases through a JDBC connection. For Impala databases, Looker connects by default to the server that is running the `impalad` daemon on port 21050. For more information, see the Configuring Impala to work with JDBC section of the documentation on the Cloudera website.
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
The Looker connection configuration depends on the security that is being used:
  * A cluster not using Kerberos or user authentication
  * A cluster requiring LDAP authentication
  * A cluster secured with Kerberos, but not using Apache Sentry


### Connecting to a cluster without Kerberos or user authentication
To configure a connection that isn't using Kerberos or user authentication, follow these steps:
  1. On the **Connection Settings** page, leave the **Username** and **Password** fields blank. (The `*` next to the field names implies that these fields are required, but they are not.)
  2. In the **Additional JDBC parameters** field, enter `;auth=noSasl`.


#### Verifying the connection string
To verify the JDBC connection string in the log files, in the Looker **Admin** panel, click **Log** in the left menu. Then filter the log on a term such as `jdbc` or `noSasl`. The log line may look something like this:
```
jdbc connect using: jdbc:hive2://<HOSTNAME>/<DATABASE_NAME>;auth=noSasl

```

For more information about configuring Impala databases to work with JDBC, see the documentation on the external Cloudera website.
### Connecting to a cluster requiring LDAP authentication
For a cluster that requires LDAP authentication, including a cluster with Apache Sentry and Kerberos, on the **Connection Settings** page, enter a **Username** and **Password** with access to the schemas Looker will access.
### Connecting to a cluster secured with Kerberos, but not using Apache Sentry
> The Looker analyst team may need to assist in configuring this connection correctly.
Usually, Kerberos authentication with Cloudera environments is handled through Apache Sentry. See the Cloudera documentation for more details.
If you want to configure Looker to connect directly to Impala databases using Kerberos authentication, follow the steps on this page.
#### Setting up the Kerberos client configuration
First, you need to ensure the installation of several pieces of software and the presence of several files on the Looker machine.
##### Kerberos client
Verify that the Kerberos client is installed on the Looker machine by trying to run `kinit`. If the Kerberos client is not installed, install the Kerberos client's binaries.
For example, on Redhat/CentOS, this would be:
`sudo yum install krb5-workstation krb5-libs krb5-auth-dialog`
##### Java 8
Java 8 must be installed on the Looker machine and in the `PATH` and `JAVA_HOME` of the Looker user. If necessary, install it locally in the `looker` directory.
##### Java Cryptography Extension
  1. Download and install the Java Cryptography Extension (JCE) for Java 8 from the Oracle website.
     * Locate the `jre/lib/security` directory for the Java installation.
     * Remove the following JAR files from this directory: `local_policy.jar` and `US_export_policy.jar`.
     * Replace these two files with the JAR files included in the JCE Unlimited Strength Jurisdiction Policy Files download.
It may be possible to use versions of Java prior to Java 8 with the JCE installed, but this is not recommended.
  2. Update `JAVA_HOME` and `PATH` in `~looker/.bash_profile` to point to the correct installation of Java and `source ~/.bash_profile` or log out and in again.
  3. Verify the Java version with `java -version`.
  4. Verify the `JAVA_HOME` environment variable with `echo $JAVA_HOME`.


##### `gss-jaas.conf`
Create a `gss-jaas.conf` file in the `looker` directory with these contents:
```
com.sun.security.jgss.initiate {
    com.sun.security.auth.module.Krb5LoginModule required
    useTicketCache=true
    doNotPrompt=true;
};

```

If necessary for testing, `debug=true` can be added to this file like this:
```
com.sun.security.jgss.initiate {
    com.sun.security.auth.module.Krb5LoginModule required
    useTicketCache=true
    doNotPrompt=true
    debug=true;
};

```

##### `krb5.conf`
The server that is running Looker should also have a valid `krb5.conf` file. By default, this file is in `/etc/krb5.conf`. If it is in another location, that must be indicated in the environment (`KRB5_CONFIG` in the shell environment).
You may need to copy this from another Kerberos client machine.
##### `lookerstart.cfg`
Point to the `gss-jaas.conf` and `krb5.conf` files by making a file in the `looker` directory (the same directory that contains the `looker` startup script) called `lookerstart.cfg` that contains the following lines:
```
  JAVAARGS="-Djava.security.auth.login.config=/path/to/gss-jaas.conf -Djavax.security.auth.useSubjectCredsOnly=false -Djava.security.krb5.conf=/etc/krb5.conf"
  LOOKERARGS=""

```

If the `krb5.conf` file is not at `/etc/krb5.conf` then it will also be necessary to add this variable:
```
  -Djava.security.krb5.conf=/path/to/krb5.conf

```

For debugging, add these variables:
```
  -Dsun.security.jgss.debug=true -Dsun.security.krb5.debug=true

```

Then restart Looker with `./looker restart`.
#### Authenticating with Kerberos
##### User authentication
  1. If `krb5.conf` is not in `/etc/`, then use the environment variable `KRB5_CONFIG` to indicate its location.
  2. Run the command `klist` to make sure there is a valid ticket in the Kerberos ticket cache.
  3. If there is no ticket, run `kinit username@REALM` or `kinit username` to create the ticket.
  4. The account that is used with Looker will likely be headless, so you can get a keytab file from Kerberos to store the credential for long-term use. Use a command like `kinit -k -t looker_user.keytab username@REALM` to get the Kerberos ticket.


##### Automatically renewing the ticket
Set up a cron job that runs every so often to keep an active ticket in the Kerberos ticket cache. How often this should run depends on the configuration of the cluster. `klist` should give an indication of how soon tickets expire.
## Creating the Looker connection to your database
In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
Fill out the connection details as follows (see the Connecting Looker to your database documentation page for more information):
  * **Name** : The name of the connection. This is how the connection will be referred to in the LookML model.
  * **Dialect** : **Cloudera Impala 3.1+** , **Cloudera Impala 3.1+ with Native Driver** , or **Cloudera Impala with Native Driver**.
  * **Host** : Hostname.
  * **Port** : Database port (21050 by default).
  * **Database** : The default schema/database that will be modeled. When no database is specified for a table, this will be assumed.
  * **Username** : Leave this blank.
  * **Password** : Leave this blank.
  * **Enable PDTs** : Use this toggle to enable persistent derived tables. When PDTs are enabled, the **Connection** window reveals additional PDT settings and the **PDT Overrides** section.
  * **Temp Database** : A temporary schema/database for storing PDTs. This must be created beforehand.
  * **Additional JDBC parameters** : Additional parameters for the JDBC string. Indicate the Kerberos principal here, for example `;principal=impala/impala.company.com@REALM`. Three-part principals are standard. The first (`impala`) is generally the name of the service, and the last (`REALM`) is generally the realm.
  * **SSL** : Check to use SSL connections. If your SSL certificate is not issued by a widely recognized Certificate Authority and you are using a custom certificate, you will need to:
    * Copy the certificate file to the Looker server. This is only available for customer-hosted Looker deployments.
    * Add the following parameters to the **Additional JDBC parameters** field:

```
  sslTrustStore=/path/to/your/trust_store.jks;trustStorePassword=yourpassword

```

> See the Cloudera documentation for more details about how to form the correct JDBC strings for Impala databases.
  * **Database Time Zone** : The time zone of data stored in your database. Usually this can be left blank or set to **UTC**.


It is a best practice to have the server name (`impala.company.com` in this example) be the canonical name for the server and its IP address's reverse DNS lookup results in that name. However, the server name should be whatever is listed in the Kerberos domain controller:
```
  nslookup servername  # get canonical server name and IP address

  nslookup ipaddress  # get the canonical name back

```

Sometimes the server name is set to be the hostname, and not the fully qualified domain name. In this case it may be necessary to modify the `/etc/hosts` and `/etc/nsswitch.conf` files to make sure that reverse lookups resolve as intended.
Test the connection to make sure that it is configured correctly.
#### Debugging
  * Cloudera's documentation about debugging Impala authentication issues.
  * When you add debugging to the configuration, the extra debugging information will wind up in `looker/logs/looker.log`.


#### Resources
  * Enabling Kerberos authentication for Impala (Cloudera documentation)
  * gss-jaas.conf documentation
  * Krb5LoginModule documentation


## Permissions for PDTs
The user connecting to the scratch schema for persistent derived tables (PDTs) must have read/write permissions.
## Feature support
For Looker to support some features, your database dialect must also support them.
### Cloudera Impala with Native Driver
Cloudera Impala with Native Driver supports the following features as of Looker 25.10:
Feature | Supported?  
---|---  
Support level | Supported  
Looker (Google Cloud core)  
Symmetric aggregates  
Derived tables | Yes  
Persistent SQL derived tables | Yes  
Persistent native derived tables | Yes  
Stable views | Yes  
Query killing | Yes  
SQL-based pivots | Yes  
Timezones | Yes  
SSL | Yes  
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
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
Approximate count distinct | Yes  
### Cloudera Impala 3.1+
Cloudera Impala 3.1+ supports the following features as of Looker 25.10:
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
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
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
Approximate count distinct | Yes  
### Cloudera Impala 3.1+ with Native Driver
Cloudera Impala 3.1+ with Native Driver supports the following features as of Looker 25.10:
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
Subtotals  
JDBC additional params | Yes  
Case sensitive | Yes  
Location type | Yes  
List type  
Percentile  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
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
Approximate count distinct | Yes  
## Next steps
After you have connected your database to Looker, configure sign-in options for your users.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


