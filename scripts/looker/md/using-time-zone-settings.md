# Using time zone settings  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/using-time-zone-settings

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * System time zone
  * Database Time Zone
  * User Specific Time Zones
    * Things to consider with User Specific Time Zones
  * Application Time Zone
  * convert_tz LookML parameter
  * sql LookML parameter
    * MySQL dialect notes
    * Postgres dialect notes
  * Database dialect support for time zone conversion




Was this helpful?
Send feedback 
#  Using time zone settings
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * System time zone
  * Database Time Zone
  * User Specific Time Zones
    * Things to consider with User Specific Time Zones
  * Application Time Zone
  * convert_tz LookML parameter
  * sql LookML parameter
    * MySQL dialect notes
    * Postgres dialect notes
  * Database dialect support for time zone conversion


Looker can make time-based data easier to understand by converting it to different time zones. Users can see query results and create filters with time-based data that is converted to their local time zones. For example, a user in New York viewing data created in California doesn't have to manually subtract three hours to filter or interpret their queries.
Looker converts time-based data when it generates SQL during a query for a Look, an Explore, or a dashboard. The underlying data is not affected; rather, the query results are converted using Looker's time zone settings. This also means that queries run using SQL Runner do not convert time-based data.
Several settings within Looker specify how to convert time-based data:
  * **System time zone**
  * **Database Time Zone**
  * **User Specific Time Zones**
  * **Application Time Zone**
  * **`convert_tz`LookML parameter**
  * **`sql`LookML parameter**


## System time zone
The system time zone is the time zone for which the server running Looker is configured. Looker's internal database, which stores the information available in the System Activity Explores, stores time-based data in the system time zone.
The system time zone is not configurable through the Looker application. For Looker-hosted instances, the system time zone is always set to UTC. Customer-hosted instances may be in a different system time zone. Changing the system time zone is not trivial and is not recommended. If you need to adjust timestamps in a System Activity Explore, use table calculations to create time-adjusted columns. For example, to convert from UTC to EST, you could create a column with the table calculation `add_hours(-5, ${time})`.
## Database Time Zone
When you add a connection to a database, you set the value for the **Database Time Zone** on the **Connection Settings** page.
This setting represents the time zone that your database is in, which is typically Coordinated Universal Time (UTC). Setting this value to anything other than the time zone that your database is in may lead to unexpected results.
## User Specific Time Zones
The most significant setting for time-based data conversion is the **User Specific Time Zones** option, which is on the **General Settings** page in the **Admin** section of Looker.
You can enable or disable **User Specific Time Zones** :
  * When enabled, each Looker user is assigned to a time zone, and that time zone specifies the appearance of their query results.
  * When disabled, users don't have individual time zones assigned to their accounts. Rather, all queries run using the **Query Time Zone** value.


With **User Specific Time Zones** enabled, a user can set their time zone on their **Account** page, or Looker admins can assign time zones to users on the **Users** page. If a time zone isn't set for a user, their account defaults to the Looker **Application Time Zone** setting.
Whenever a user creates a query, that query is created in the user's time zone. As a result, when a query returns time-based data, Looker converts the data from the **Database Time Zone** to the user's time zone. When a user uses time-related filter values in a query, Looker converts the filter values to the **Database Time Zone**.
In addition, when you enable this option, Looker displays a **Time Zone** drop-down menu in Explores and Looks.
Options in this drop-down are:
  * **Each Tile's Time Zone (dashboards only):** All queries run in the time zone they were saved with.
  * **Viewer Time Zone** : All queries run in the user's current time zone setting.
  * A list of every individual time zone, which users may manually choose if they like.


All queries default to the time zone the query was created with. In other words, if Alice creates a query with time zone "America/Los Angeles" and sends it to Bob, Bob will see the query with time zone "America/Los Angeles," even if Bob's time zone is set to "America/New York." Similarly, drilling always defaults to whatever time zone the query was created with.
Whenever viewing a query, users can use the drop-down to override the time zone, picking their **Viewer Time Zone** or any different time zone for that query or that dashboard's set of queries.
### Things to consider with User Specific Time Zones
When you enable **User Specific Time Zones** , users in different time zones may see data differently.
For example, the exact hours making up the time period `last month` would differ between time zones, so users may see different data values if they are in different time zones but are both filtering on `last month`.
## Application Time Zone
The **Application Time Zone** setting can be configured on the **General Settings** page in the **Admin** section of Looker.
The **Application Time Zone** is the default time zone for content deliveries. The time zone used for content deliveries does not affect time-based data returned by a query; it affects only the time a data delivery is sent.
If you enable the **User Specific Time Zones** option, the **Application Time Zone** is the default time zone for users that do not have a time zone value set for their accounts.
## Query Time Zone
The **Query Time Zone** option is displayed only if you have disabled **User Specific Time Zones**. In that case, you set the **Query Time Zone** value when you add a connection to a database on the **Connection Settings** page.
If you disable **User Specific Time Zones,** all queries of time-based data use the **Query Time Zone** and Looker converts all time-based data from the **Database Time Zone** to the **Query Time Zone**.
##  `convert_tz` LookML parameter
Looker does time zone conversion by default. To disable time zone conversion for an individual field, you can use the `convert_tz` LookML parameter. For example:
```
dimension_group: created {
  type: time
  timeframes: [time, date]
  convert_tz: no
}

```

For more information, see the `convert_tz` parameter documentation page.
##  `sql` LookML parameter
You can also manually define time zone conversion using your database dialect's functions within the `sql` parameter in a LookML dimension. For example, to manually define time zone conversion in MySQL, you could use the following LookML:
```
dimension_group: created {
 type: time
 timeframes: [time, date]
 sql: CONVERT_TZ(${TABLE}.created_at,'UTC','PST') ;;
}

```

### MySQL dialect notes
MySQL requires a time zone table before its time zone conversion function will work. This can be run by an admin. You can read more in the MySQL documentation.
### Postgres dialect notes
Looker uses the driver setting to select the target time zone. This may affect how queries are processed in SQL Runner as compared with pgAdmin, because Looker will use the current datetime in the time zone selected.
## Database dialect support for time zone conversion
For Looker to convert time zones in your Looker project, your database dialect must support time zone conversion. The following table shows which dialects support time zone conversion in the latest release of Looker:
Dialect | Supported?  
---|---  
Actian Avalanche  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Amazon Redshift 2.1+ | Yes  
Amazon Redshift Serverless 2.1+ | Yes  
Apache Druid  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality  
Databricks | Yes  
Denodo 7  
Denodo 8  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol  
Firebolt  
Google BigQuery Legacy SQL  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | Yes  
Greenplum | Yes  
HyperSQL  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+  
Microsoft SQL Server 2012+  
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
SAP HANA  
SAP HANA 2+  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata  
Trino | Yes  
Vector  
Vertica | Yes  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


