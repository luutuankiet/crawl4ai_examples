# Testing database connectivity for customer-hosted instances  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/testing-db-connectivity

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Installing Telnet
  * Connecting to your database with Telnet
  * Other troubleshooting tips




Was this helpful?
Send feedback 
#  Testing database connectivity for customer-hosted instances
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Installing Telnet
  * Connecting to your database with Telnet
  * Other troubleshooting tips


When you're troubleshooting a new environment, it is often helpful to isolate the various components in play and test them in isolation as simply as possible.
For customer-hosted Looker instances, you can test the connectivity between your Looker server and your database using Telnet on your Looker server to create a TCP connection. The advantage of using Telnet is that there are no configuration files to modify and no authentication is required. Telnet either makes the connection or it does not.
Once you know that the database is accessible, you can move on to testing using applications such as your database's built-in client, or Looker.
### Installing Telnet
Some hosts may come with Telnet pre-installed. To test this, run this command on your Looker server:
```
telnet ?

```

You should see something like this:
```
usage: telnet [-l user] [-a] [-s src_addr] host-name [port]

```

If you get a "command not found" error, you will need to install Telnet.
On Ubuntu:
```
sudo apt-get install telnet

```

On Redhat/CentOS:
```
yum install telnet

```

### Default ports
You will need to know on which port your database is running. The following table lists the default ports for a number of platforms, although your database may be configured to run on a different port. Consult your database administrator.
Platform | Port  
---|---  
Amazon Redshift | 5439  
GreenPlum | 5432  
Microsoft SQL Server (MSSQL) | 1433  
MySQL | 3306  
Oracle | 1521  
PostgreSQL | 5432  
Vertica | 5433  
### Connecting to your database with Telnet
To test the connection to your database, run the `telnet hostname port` on your Looker server. For example, if you're running MySQL on the default port and your database name is **mydb** , the command would be `telnet mydb 3306`.
If the connection is working, you will see something similar to this:
```
Trying 10.10.10.10...
Connected to mydb.
Escape character is '^]'.

```

If the connection is NOT working, you will see something like one of these:
```
Trying 10.10.10.10...
telnet: Unable to connect to remote host: Connection timed out

```
```
Trying 127.0.0.1...
telnet: Unable to connect to remote host: Connection refused

```
```
telnet: could not resolve mydb/telnet: Name or service not known

```

If you're able to Telnet from your Looker server to your database server's port, you can rule out basic connectivity issues.
## Other troubleshooting tips
If the Telnet check is not successful, consider the following:
  * Is the hostname correct?
  * Are the database and Looker server configured to allow the network traffic between them? Check any installed firewall software on both hosts.
  * Are all the networks between the Looker server and the database hosts configured to allow the network traffic? Check firewalls and network Access Control Lists (ACLs).
  * Are all the networks between the Looker server and the database hosts configured correctly to route traffic between the hosts?
  * Is the database server running, is it listening on the correct port, and is it configured to allow connections from the Looker server?


If you're still having trouble, contact Looker Support for assistance.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


