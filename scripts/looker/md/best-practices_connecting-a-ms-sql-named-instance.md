# Connecting an MS-SQL named instance  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/connecting-a-ms-sql-named-instance

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How MS-SQL named instances connect
  * How to connect an MS-SQL named instance with Looker




Was this helpful?
Send feedback 
#  Connecting an MS-SQL named instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How MS-SQL named instances connect
  * How to connect an MS-SQL named instance with Looker


Microsoft SQL Server (MS-SQL) has a feature called **named instances**. This feature lets you run multiple databases on the same host (or clustered hosts) with separate settings. Each database instance runs on its own port. However, when using MS-SQL–aware clients running on Windows, you can connect by name instead of by port number. For example, if your hostname is `dbserver` and your instance is named `proddb`, you would connect using the hostname `dbserver\proddb`. 
## How MS-SQL named instances connect
  1. Your client contacts the host, named on the default MS-SQL port (1433). 
  2. MS-SQL responds with the named instance's port. 
  3. The client then connects to that port. 


Looker will be unable to find the port number of a named instance in this way. Once Looker connects to a port, it expects to be able to run queries and will not connect with any other port. 
## How to connect an MS-SQL named instance with Looker
MS-SQL chooses a random port at startup. For Looker to connect to an MS-SQL named instance, you will need to find the port the named instance is running on:
  * The article SQL Server — Finding TCP Port Number SQL Instance Is Listening On details the method for finding the port. Although the article is from 2012, the procedure is similar across the various versions of MS-SQL. 
  * Once you've found the port, you can enter the port name in the `Host:Port` field in Looker's database connection configuration. For example, if the port is `61499` and the host is named `dbserver`, the connection in Looker will look like this: ```
  host: dbserver
  port: 61499
```

> _**NOTE:** The database hostname will **not** take the form `dbserver\proddb`, as it would if you were connecting by the instance name._
  * it is important to note that MS-SQL may choose a different port for the named instance whenever the server is rebooted. This could require MS-SQL to change firewall rules and reconfigure Looker to use the new port. To avoid ports changing, you can choose to assign a static port to your named instance; see How to Assign a Static Port to a SQL Server Named Instance — and Avoid a Common Pitfall for details on the process.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


