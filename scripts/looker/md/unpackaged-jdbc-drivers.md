# Unpackaged JDBC drivers  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/unpackaged-jdbc-drivers

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Configuring Looker to use unpackaged JDBC drivers
  * Prerequisites
    * Driver entries in the YAML configuration file
  * Installing unpackaged JDBC drivers
    * Multiple unpackaged JDBC drivers




Was this helpful?
Send feedback 
#  Unpackaged JDBC drivers
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Configuring Looker to use unpackaged JDBC drivers
  * Prerequisites
    * Driver entries in the YAML configuration file
  * Installing unpackaged JDBC drivers
    * Multiple unpackaged JDBC drivers


## Configuring Looker to use unpackaged JDBC drivers
For some of Looker's supported dialects, the JDBC driver cannot be packaged in the Looker JAR file for licensing-related reasons. In these cases, you must install the JDBC driver on your Looker server and then configure Looker to register the unpackaged driver as described on this page.
All dialects with a value of "No" under "Supported?" require unpackaged JDBC driver installations:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver  
Cloudera Impala with Native Driver  
DataVirtuality  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | Yes  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata  
Trino | Yes  
Vector  
Vertica | Yes  
## Prerequisites
To connect Looker to a database that requires an unpackaged JDBC driver, you will need the following:
  * Command line access to your Looker server.
  * The JDBC driver as a JAR file. The dialect's specific documentation may have instructions on where to download this file; otherwise, it is assumed that you have access to the JAR file needed.
  * The **driver symbol** for your dialect. A driver symbol is a string value that Looker uses internally to match the dialect to the driver. The examples on this page use the generic value `driver_symbol`. See the Looker documentation for each dialect for the symbols that Looker uses to register JDBC drivers to dialects.
  * The YAML **driver entry** for your dialect to be added to the `custom_jdbc_config.yml` configuration file. See the Driver entries in the YAML configuration file section on this page for more information.


### Driver entries in the YAML configuration file
Here is an example driver entry in the `custom_jdbc_config.yml` file:
```
  - name: driver_symbol
    dir_name: driver_symbol
    module_path: com.dialect.jdbc.DialectDriver
    override_jdbc_url_subprotocol: driver_subprotocol  # optional

```

When writing the driver entry for your dialect:
  * The file `custom_jdbc_config.yml` is YAML-based, which means that indentation and spacing matter.
  * The `name` and `dir_name` attributes must be the driver symbol that Looker uses for your dialect when registering JDBC drivers.
  * It is possible to use the attribute `file_name` instead of `dir_name` containing the relative path from `custom_jdbc_drivers` to the JDBC driver JAR file. `dir_name` is recommended because it promotes keeping multiple drivers isolated to their own directories and reduces the chance of Java classes colliding.
  * The `module_path` property will depend on the specific JDBC driver. It should be the fully qualified path to the Java _driver class_. This example uses a generic value, but to find the specific `module_path` the driver uses consult its documentation on how to _register_ the driver class.
  * The `override_jdbc_url_subprotocol` is an optional argument that is used to override the subprotocol that is used in the JDBC string that Looker sends to the database. A typical JDBC string will look like this:

```
jdbc:mysql://localhost:3306/database_name[?propertyName1][=propertyValue1]

```

Where `mysql` is the JDBC subprotocol being used.
If you specify `override_jdbc_url_subprotocol: driver_subprotocol`, then this JDBC string will become:
```
jdbc:driver_subprotocol://localhost:3306/database_name[?propertyName1][=propertyValue1]

```

This option is required if you need to use an unpackaged JDBC driver that requires a URL subprotocol other than Looker's default URL subprotocol. For the most part, this is not necessary unless the dialect's documentation explicitly says that it is. MongoBI is an example of a dialect that requires this option.
## Installing unpackaged JDBC drivers
  1. Change to the Looker application base directory. This example uses `looker` the as the base directory.
```
cd looker

```

  2. Create a directory called `custom_jdbc_drivers`. This is the top-level directory for all unpackaged JDBC driver installations. The path to this directory should be `looker/custom_jdbc_drivers`
```
mkdir custom_jdbc_drivers

```

  3. In the `custom_jdbc_drivers` directory, create a subdirectory named with your dialect's driver symbol. This example uses the generic value `driver_symbol`. The resulting path to the directory will look like `looker/custom_jdbc_drivers/driver_symbol`
```
cd custom_jdbc_drivers
mkdir driver_symbol

```

  4. Place the JDBC driver files for your dialect into this directory. The method for this depends on where your dialect's driver can be found and uploaded onto the server, but be sure that the relevant JAR file(s) are inside the `driver_symbol` directory: `looker/custom_jdbc_drivers/driver_symbol/`
For example: `looker/custom_jdbc_drivers/driver_symbol/DialectDriver.jar`
> How you move the necessary files onto the Looker server will vary based on where you get the driver files and your preference for file transferring. Examples of commands for transferring files into this directory include `wget`, `scp`, and `curl`.
  5. Change the directory to the Looker application directory, and create a configuration file named `custom_jdbc_config.yml`. The path to this file should be `looker/custom_jdbc_config.yml`. This file will contain the information that Looker needs to locate and register the custom JDBC driver.
```
cd looker
vim custom_jdbc_config.yml

```

  6. Add a new entry for your dialect into the `custom_jdbc_config.yml` configuration file. See the Driver entries in the YAML configuration file section on this page for information on driver entries.
```
- name: driver_symbol
  dir_name: driver_symbol
  module_path: com.dialect.jdbc.DialectDriver

```

  7. Create or update the file `lookerstart.cfg` so that the Looker application starts up with the unpackaged JDBC driver configuration. The path to this file should be `looker/lookerstart.cfg`. Add the option `--use-custom-jdbc-config`. If there are other options, append this to the end of the Looker startup options:
```
LOOKERARGS="--use-custom-jdbc-config"

```

> If you have `LOOKERARGS` set somewhere other than `lookerstart.cfg`, like in an environment variable, you may add this startup flag there. Alternatively, you can set `LOOKERARGS="${LOOKERARGS} --use-custom-jdbc-config"` so that the existing values will be expanded into this file.
  8. Restart the Looker application. In this command, use the name of your Looker startup script, such as `./looker` or `./looker.sh`
```
./looker restart

```

or `none ./looker stop ./looker start`


### Multiple unpackaged JDBC drivers
If you need to configure more than one dialect to use unpackaged JDBC drivers, the process described in the Installing unpackaged JDBC drivers section still applies. The `custom_jdbc_drivers` directory will have multiple `dialect` subdirectories with their own driver JARs, and the `custom_jdbc_config.yml` file will have multiple entries:
```
ls looker/custom_jdbc_drivers

driver_symbol_1 driver_symbol_2

```
```
ls looker/custom_jdbc_drivers/driver_symbol_1

Dialect1Driver.jar

```
```
- name: driver_symbol_1
  dir_name: driver_symbol_1
  module_path: com.dialect.jdbc.Dialect1Driver

- name: driver_symbol_2
  dir_name: driver_symbol_2
  module_path: com.dialect.jdbc.Dialect2Driver

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


