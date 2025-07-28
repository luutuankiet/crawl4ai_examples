# Customer-hosted architecture solutions: Component walkthroughs  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/customer-hosted-component-walkthroughs

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Host configuration
    * OS and distribution
    * Cluster considerations
  * JVM configuration
    * Garbage collection
  * Looker startup options
    * High scheduling throughput options
    * High rendering throughput options
  * Internal (backend) database
    * System Activity queries
    * MySQL performance configuration
  * Git service
    * GitHub/GitHub Enterprise
    * GitLab/gitlab.com
    * Google Cloud Source
    * Bitbucket Server
    * Phabricator diffusion
  * Network
    * Inbound connections
    * Outbound connections
    * Internode communications
  * Related resource




Was this helpful?
Send feedback 
#  Customer-hosted architecture solutions: Component walkthroughs
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Host configuration
    * OS and distribution
    * Cluster considerations
  * JVM configuration
    * Garbage collection
  * Looker startup options
    * High scheduling throughput options
    * High rendering throughput options
  * Internal (backend) database
    * System Activity queries
    * MySQL performance configuration
  * Git service
    * GitHub/GitHub Enterprise
    * GitLab/gitlab.com
    * Google Cloud Source
    * Bitbucket Server
    * Phabricator diffusion
  * Network
    * Inbound connections
    * Outbound connections
    * Internode communications
  * Related resource


This page explores common practices for specific components of the Looker architecture and describes how to configure them within a deployment. 
Looker has a number of dependencies for hosting the server, servicing both ad hoc and scheduled workloads, tracking iterative model development, or the like. Such dependencies are referred to as _components_ on this page, and each component is covered in detail in the following sections: 
  * Host configuration
  * JVM configuration
  * Looker startup options
  * Internal (backend) database
  * Git service


## Host configuration
### OS and distribution
Looker runs well on the most common versions of Linux: RedHat, SUSE, and Debian/Ubuntu. Derivatives of these distributions that are designed and optimized to run in a particular environment are generally fine. For example, the Google Cloud or AWS distributions of Linux are compatible with Looker. Debian/Ubuntu is the most heavily used Linux variety in the Looker community, and these are the versions most familiar to Looker Support. It is easiest to use Debian/Ubuntu or an operating system for a specific cloud provider that is derived from Debian/Ubuntu. 
Looker runs in the Java virtual machine (JVM). When choosing a distribution, consider whether the versions of the OpenJDK 11 are up to date. Older distributions of Linux may be able to run Looker, but the Java version and libraries that Looker requires for specific features must be up to date. If the JVM does not contain all the recommended Looker libraries and versions, Looker won't function normally. Looker requires Java HotSpot 1.8 update 161+ or Java OpenJDK 11.0.12+. 
### CPU and memory
4x16 (4 CPUs and 16 GB of RAM) nodes are sufficient for a development system or a basic testing Looker instance used by a small team. For production use, however, this is not usually sufficient. In our experience, 16x64 nodes (16 CPUs and 64 GB of RAM) are a good balance between price and performance. More than 64 GB of RAM can impact performance, as garbage collection events are single threaded and halt all other threads to execute. 
### Disk storage
100 GB of disk space is typically more than sufficient for a production system. 
### Cluster considerations
Looker runs on a Java JVM, and Java can have difficulty managing memory greater than 64 GB. As a general rule, if more capacity is required you should add additional 16x64 nodes to the cluster rather than increase the size of the nodes beyond 16x64. We may also prefer to use a clustered architecture for increased availability. 
In a cluster, the Looker nodes need to share certain parts of the file system. The shared data includes the following: 
  * LookML models
  * The developer LookML models
  * Git server connectivity


Since the file system is shared and is hosting a number of Git repositories, the handling of concurrent access and file locking is critical. The file system must be POSIX compliant. Network file system (NFS) is known to work and is readily available with Linux. You should create an additional Linux instance and configure NFS to share out the disk. Default NFS is potentially a single point of failure, so consider a failover setup or high availability setup. 
The Looker metadata also needs to be centralized, so its internal database must be migrated to MySQL. This can be a MySQL service or a dedicated MySQL deployment. The Internal (backend) database section on this page goes into greater detail. 
## JVM configuration
The Looker JVM settings are defined inside the Looker startup script. After any updates, Looker must be restarted for changes to manifest. The default configurations are as follows: 
```
java \
  -XX:+UseG1GC -XX:MaxGCPauseMillis=2000 \
  -Xms$JAVAMEM -Xmx$JAVAMEM \
  -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps \
  -Xloggc:/tmp/gc.log ${JAVAARGS} \
  -jar looker.jar start ${LOOKERARGS}

```

### Resources
The resource settings are defined in the Looker startup script. 
```
JAVAMEM="2300m"
METAMEM="800m"

```

The memory allocation for the JVM needs to take into consideration the operating system overhead that Looker is running on. The general rule of thumb is the JVM can be allocated up to 60% of total memory, but there are caveats depending on the machine size. For machines with the bare minimum of 8 GB of total memory, we recommend an allocation of 4-5 GB to Java and 800 MBs for Meta. For larger machines, a lower proportion of memory can be allocated for the operating system. For example, for machines with 60 GB of total memory, we recommend an allocation 36 GB to Java and 1 GB to Meta. It's important to note that Java's memory allocation should typically scale with the total memory of the machine, but Meta should be sufficient at 1 GB. 
Moreover, since Looker shares system resources with other processes like Chromium for rendering, the amount of memory allocated to Java should be selected in context of the anticipated rendering load and the size of the machine. If rendering load is expected to be low, Java can be allocated a greater share of the total memory. For example, on a machine with 60 GB of total memory, Java could be safely allocated to 46 GB, which is higher than the general 60% recommendation. The exact resource allocations appropriate for each deployment vary, so use 60% as a baseline and adjust as usage dictates. 
### Garbage collection
Looker prefers using the most modern garbage collector available to its Java version. By default the garbage collection timeout is 2 seconds, but this can be changed by editing the following option in the startup configuration: 
```
-XX:MaxGCPauseMillis=2000
```

On a larger machine with multiple cores, the garbage collection timeout could be shortened. 
### Logs
By default, the Looker garbage collection logs are stored in `/tmp/gc.log`. This can be changed by editing the following option in the startup configuration: 
```
-Xloggc:/tmp/gc.log
```

### JMX
Managing Looker may need monitoring to help refine resourcing. We recommend using JMX to monitor JVM memory usage. 
## Looker startup options
The startup options are stored in a file called `lookerstart.cfg`. This file is sourced in the shell script that starts Looker. 
### Thread pools
As a multi-threaded application, Looker has a number of thread pools. These thread pools range from the core web server to specialized subservices like scheduling, rendering, and external database connections. Depending on your business workflows, these pools may need to be modified from the default configuration. In particular, there are special considerations for the cluster topologies mentioned in the Customer-hosted infrastructure architecture patterns and practices page. 
### High scheduling throughput options
For all non-scheduler nodes, add `--scheduler-threads=0` to the `LOOKERARGS` environment variable in `lookerstart.cfg`. Without scheduler threads, no scheduled jobs will run on these nodes. 
For all dedicated scheduler nodes, add `--scheduler-threads=<n>` to the `LOOKERARGS` environment variable in `lookerstart.cfg`. Looker starts with 10 scheduler threads by default, but this can be increased to <n>. With <n> scheduler threads, each node will be capable of executing <n> concurrent schedule jobs. It's generally recommended to keep <n> less than 2x the number of CPUs. The largest recommended host is one with 16 CPUs and 64 GB of memory, so the upper bound of scheduler threads should be less than 32. 
### High rendering throughput options
For all non-render nodes, add `--concurrent-render-jobs=0` to the `LOOKERARGS` environment variable in `lookerstart.cfg`. Without renderer nodes, no render jobs will run on these nodes. 
For all dedicated render nodes, add `--concurrent-render-jobs=<n>` to the `LOOKERARGS` environment variable in `lookerstart.cfg`. Looker starts with two render threads by default, but this can be increased to <n>. With <n> render threads, each node will be capable of executing <n> concurrent render jobs. 
Each render job can use a significant amount of memory. Budget about 2 GB per render job. For example, if the core Looker process (Java) is allocated 60% of the total memory and 20% of the remaining memory is reserved for the operating system, that leaves the last 20% for render jobs. On a 64 GB machine, that leaves 12 GB, which is enough for 6 concurrent render jobs. If a node is dedicated to rendering and is not included in the load balancer pool that is handling interactive jobs, the core Looker process memory can be reduced to allow for more render jobs. On a 64 GB machine, one might allocate approximately 30% (20 GB) to the Looker core process. Reserving 20% for general OS use, that leaves 50% (32 GB) for rendering, which is enough for 16 concurrent render jobs. 
## Internal (backend) database
The Looker server maintains information about its own configuration, database connections, users, groups, and roles, folders, user-defined Looks and dashboards, and various other data in an internal database. 
For a standalone Looker instance of moderate size, this data is stored within an in-memory HyperSQL database embedded in the Looker process itself. The data for this database is stored in the file `<looker install directory>/.db/looker.script`. Although convenient and lightweight, this database experiences performance issues with heavy usage. Therefore, we recommend starting with a remote MySQL database. If this isn't feasible, we recommend migration to a remote MySQL database once the `~/looker/.db/looker.script` file reaches 600 MB. Clusters must use a MySQL database. 
The Looker server makes many small reads and writes to the MySQL database. Every time a user runs a Look or an Explore, Looker will check the database to verify that the user is still logged in, the user has privileges to access the data, the user has privileges to run the Look or Explore, and the like. Looker will also write data to the MySQL database, such as the actual SQL that was run and the time the request started and ended. A single interaction between a user and the Looker application could result in 15 or 20 small reads and writes to the MySQL database. 
### MySQL
The MySQL server should be version 8.0.x, and must be configured to use utf8mb4 encoding. The InnoDB storage engine must be used. The setup instructions for MySQL, as well as instructions for how to migrate data from an existing HyperSQL database to MySQL, are available on the Migrating the Looker backend database to MySQL documentation page. 
When configuring Looker to use MySQL, a YAML file must be created containing the connection information. Name the YAML file `looker-db.yml` and add the setting `-d looker-db.yml` in the `LOOKERARGS` section of the `lookerstart.cfg` file. 
### MariaDB
MySQL is dual-licensed, available both as open source and as a commercial product. Oracle has continued to enhance MySQL, and MySQL is forked as MariaDB. The MariaDB equivalent versions of MySQL are known to work with Looker, but they aren't developed for or tested by the Looker engineering teams; therefore, functionality is not supported or guaranteed. 
### Cloud versions
If you host Looker in your cloud infrastructure, it is logical to host the MySQL database in the same cloud infrastructure. The three major cloud vendors — Amazon AWS, Microsoft Azure, and Google Cloud. The cloud providers manage much of the maintenance and configuration for the MySQL database and offer services like help managing backups and providing rapid recovery. These products are known to work well with Looker. 
### System Activity queries
The MySQL database is used to store information about how users are using Looker. Any Looker user who has permission to view the System Activity model has access to a number of prebuilt Looker dashboards to analyze this data. Users can also access Explores of Looker metadata to build additional analysis. The MySQL database is primarily used for small, fast, "operational" queries. The large, slow, "analytic" queries generated by the System Activity model can compete with these operational queries and slow Looker down. 
In these cases, the MySQL database can be replicated to another database. Both self-managed and certain cloud-managed systems provide basic configuration of replication to other databases. Configuring replication is outside the scope of this document. 
In order to use the replica for the System Activity queries, you will create a copy of the `looker-db.yml` file, for example named `looker-usage-db.yml`, modify it to point to the replica, and add the setting `--internal-analytics-connection-file looker-usage-db.yml` to the `LOOKERARGS` section of the `lookerstart.cfg` file. 
The System Activity queries can run against a MySQL instance or a Google BigQuery database. They are not tested against other databases. 
### MySQL performance configuration
In addition to the settings required to migrate the Looker backend database to MySQL, highly active clusters may benefit from additional tuning and configuration. These settings can be made to the `/etc/my.cnf` file, or through the Google Cloud console for cloud-managed instances. 
The `my.cnf` configuration file is divided into several parts. The following setting changes discussed in this section are made in the `[mysqld]` part. 
#### Set the InnoDB buffer pool size
The InnoDB buffer pool size is the total RAM that is used to store the state of the InnoDB data files in memory. If the server is dedicated to running MySQL, the `innodb_buffer_pool_size` should be set to 50%-70% of total system memory. 
If the total size of the database is small, it is allowable to set the InnoDB buffer pool to the size of the database rather than 50% or more of memory. 
For this example, a server has 64 GB of memory; therefore, the InnoDB buffer pool should be between 32 GB and 45 GB. Bigger is typically better. 
```
[mysqld]
...
innodb_buffer_pool_size=45G

```

#### Set the InnoDB buffer pool instances
When multiple threads attempt to search a large buffer pool, they could contend. To prevent this, the buffer pool is divided into smaller units that can be accessed by different threads without conflict. By default, the buffer pool is divided into 8 instances. This creates the potential for an 8 thread bottleneck. Increasing the number of buffer pool instances reduces the chance of a bottleneck. The innodb_buffer_pool_instances should be set so that each buffer pool gets at least 1 GB of memory. 
```
[mysqld]
...
innodb_buffer_pool_instances=32

```

#### Optimize the InnoDB log file
When a transaction is committed, the database has the option to update the data in the actual file, or it can save details about the transaction in the log. If the database crashes before the data files have been updated, the log file can be "replayed" to apply the changes. Writing to the log file is a small append operation. It is efficient to append to the log at commit time, then batch up multiple changes to the data files and write them in a single IO operation. When the log file is filled, the database has to pause processing new transactions and write all the changed data back to disk. 
As a general rule of thumb, the InnoDB log file should be large enough to contain 1 hour of transactions. 
There are typically two InnoDB log files. They should be about 25% of your InnoDB buffer pool. For an example database with a 32 GB buffer pool, the InnoDB log files should total 8 GB, or 4 GB per file. 
```
[mysqld]
...
innodb_log_file_size=8GB

```

#### Configure InnoDB IO capacity
MySQL will throttle the speed at which writes are recorded to the disk so as not to overwhelm the server. The default values are conservative for most servers. For best performance use the `sysbench` utility to measure the random write speed to the data disk, then use that value to configure the IO capacity so that MySQL will write data more quickly. 
On a cloud-hosted system, the cloud vendor should be able to report the performance of the disks used for data storage. For a self-hosted MySQL server, measure the speed of random writes to the data disk in IO operations per second (IOPS). The Linux utility `sysbench` is one way to measure this. Use that value for the `innodb_io_capacity_max`, and a value one-half to three-quarters of that for `innodb_io_capacity`. So, in the following example, we would see the values if we measured 800 IOPS. 
```
[mysqld]
...
innodb_io_capacity=500
innodb_io_capacity_max=800

```

#### Configure InnoDB threads
MySQL will open at least one thread for each client being served. If many clients are connected simultaneously, that can lead to a huge number of threads being processed. This can cause the system to spend more time swapping than processing. 
Benchmarking should be done to determine the ideal number of threads. To test, set the number of threads between the number of CPUs (or CPU cores) on the system and 4x the number of CPUs. For a 16-core system, this value is likely between 16 and 64. 
```
[mysqld]
...
innodb_thread_concurrency=32

```

#### Transaction durability
A transaction value of 1 forces MySQL to write to disk for every transaction. If the server crashes, the transaction won't be lost, but database performance will be impacted. Setting this value to 0 or 2 can improve performance, but it will come at the risk of losing a couple of seconds' worth of data transactions. 
```
[mysqld]
...
innodb_flush_log_at_trx_commit=1

```

#### Set the flush method
The operating system normally does buffering of writes to the disk. Since MySQL and the OS are both buffering, there is a performance penalty. Reducing the flush method one layer of buffering can improve performance. 
```
[mysqld]
...
innodb_flush_method=O_DIRECT

```

#### Enable one file per table
By default, MySQL will use a single data file for all data. The `innodb_file_per_table` setting will create a separate file for each table, which improves performance and data management. 
```
[mysqld]
...
innodb_file_per_table=ON

```

#### Disable stats on metadata
This setting disables the collection of stats on internal metadata tables, improving read performance. 
```
[mysqld]
...
innodb_stats_on_metadata=OFF

```

#### Disable the query cache
The query cache is deprecated, so setting the `query_cache_size` and `query_cache_type` to 0 disables it. 
```
[mysqld]
...
query_cache_size=0
query_cache_type=0

```

#### Enlarge the join buffer
The `join_buffer` is used to perform joins in memory. Increasing it can improve certain operations. 
```
[mysqld]
...
join_buffer_size=512KB

```

#### Enlarge the temporary table and max heap sizes
The `tmp_table_size` and `max_heap_table_size` set reasonable defaults for temporary in-memory tables, before they are forced to disk. 
```
[mysqld
...
tmp_table_size=32MB
max_heap_table_size=32MB

```

#### Adjust the table open cache
The `table_open_cache` setting determines the size of the cache that holds the file descriptors for open tables. The `table_open_cache_instances` setting breaks the cache into a number of smaller parts. There is a potential for thread contention in the `table_open_cache`, so dividing it into smaller parts helps increase concurrency. 
```
[mysqld]
...
table_open_cache=2048
table_open_cache_instances=16

```

## Git service
Looker is designed to work with a Git service to provide version management of the LookML files. Major Git hosting services are supported, including GitHub, GitLab, and Bitbucket. Git service providers offer additional value adds such as a GUI to view code changes and support for workflows like pull requests and change approvals. If required, Git can be run on a plain Linux server. 
If a Git hosting service is not appropriate for your deployment because of security rules, many of these service providers offer versions that can be run in your own environment. GitLab, in particular, is commonly self-hosted and can be used as an open source product with no license cost or as a supported licensed product. GitHub Enterprise is available as a self-hosted service and is a supported commercial product. 
The following sections list nuances for the most common service providers. 
### GitHub/GitHub Enterprise
The Setting up and testing a Git connection documentation page uses GitHub as an example. 
### GitLab/gitlab.com
Refer to the Using GitLab for version control in Looker Looker Community post for detailed setup steps for GitLab. If your repository is contained within subgroups, these can be added to the repository URL using either the HTTPS or SSH format: 
```
https://gitlab.com/accountname/subgroup/reponame

```

Additionally, there are three different ways you can store Looker-generated SSH keys in GitLab: as a user SSH key, as a repository deploy key, or as a global shared deploy key. A more in-depth explanation can be found in the GitLab documentation. 
### Google Cloud Source
Refer to the Using Cloud Source Repositories for version control in Looker Community Post for steps to set up Git with Cloud Source Repositories. 
### Bitbucket Cloud
Refer to the Using Bitbucket for version control in Looker Community Post for steps for setting up Git with Bitbucket Cloud. As of August 2021, Bitbucket Cloud does not support secrets on deploy webhooks. 
### Bitbucket Server
To use pull requests with Bitbucket Server, you may need to complete the following steps: 
  1. When you open a pull request, Looker will automatically use the default port number (7999) in the URL. If you are using a custom port number, you will need to replace the port number in the URL manually. 
  2. You will need to hit the project's deploy webhook to sync the production branch in Looker with the repository's main branch. 


### Phabricator diffusion
Refer to the Setting up Phabricator and Looker for version control Community Post for steps on setting up Git with Phabricator. 
## Network
### Inbound connections
#### Looker web application
By default, Looker listens for HTTPS requests on port 9999. Looker uses a self-signed certificate with a CN of `self-signed.looker.com`. The Looker server can alternately be configured to do the following: 
  1. Accept HTTP connections from an SSL-termination load balancer/proxy, with the `--ssl-provided-externally-by=<s>` startup flag. The value should either be set to the IP address of the proxy, or to a hostname that can be locally resolved to the IP address of the proxy. Looker will accept HTTP connections only from this IP address.
  2. Use a customer supplied SSL certificate, with the `--ssl-keystore=<s>` startup flag.


#### Looker API
The Looker API listens on port 19999. If the installation requires access to the API, then the load balancer should have the requisite forwarding rules. The same SSL considerations apply as with the main web application. We recommend using a distinct port from the web application. 
#### Load balancers
A load balancer is often used to accept an HTTPS request at port 443 using the customer's certificate, then forward the request to the Looker server node at port 9999 using the self-signed certificate or HTTP. If load balancers are using the Looker self-signed certificate, they must be configured to accept that certificate. 
#### Idle connections and timeouts
When a user starts a large request in Looker, that could result in a query that could be expensive to run on the database. If the user abandons that request in any way — such as by shutting the lid on their laptop, disconnecting from the network, or killing that tab in the browser — Looker wants to know and terminate that database query. 
To handle this situation, when the client web application makes a request to run a database query, the browser will open a socket connection using a long-lived HTTP request to the Looker server. This connection will sit open and idle. This socket will get disconnected if the client web application is killed or disconnected in any way. The server will see that disconnect and cancel any related database queries. 
Load balancers often notice these open idle connections and kill them. In order to run Looker effectively, the load balancer must be configured to allow this connection to remain open for as long as the longest query a user might run. A timeout of at least 60 minutes is suggested. 
### Outbound connections
Looker servers can have unrestricted outbound access to all resources, including the public internet. This simplifies many tasks, such as installing Chromium, which requires access to the package repositories for the Linux distribution. 
The following are outbound connections that Looker may need to make. 
#### Internal database connection 
By default, MySQL listens for connections on port 3306. The Looker nodes must be able to initiate connections to MySQL on this port. Depending on how the repository is hosted, you may need to traverse a firewall. 
#### External services
The Looker telemetry and license servers are available using HTTPS on the public internet. Traffic from a Looker node to `ping.looker.com:443` and `license.looker.com:443` may need to be added to an allowlist. 
#### Data warehouse connections
Cloud-hosted databases may require a connection using the public internet. For example, if you are using BigQuery, then `accounts.google.com:443` and `www.googleapis.com:443` may need to be added to an allowlist. If the database is outside of your own infrastructure, consult with your database host for network details. 
#### SMTP services
By default, Looker sends outgoing mail using SendGrid. That may require adding `smtp.sendgrid.net:587` to an allowlist. The SMTP settings can be changed in the configuration to use a different mail handler as well. 
#### Action hubs, action servers, and webhooks
Many scheduler destinations, in particular webhooks and the ones that are enabled in the Looker Admin panel, involve sending data using HTTPS requests. 
  * For webhooks, these destinations are specified at runtime by users, and may be contrary to the goal of firewalling outbound connections.
  * For an action hub, these requests are sent to `actions.looker.com`. Details can be found in our Looker Action Hub configuration documentation.
  * For other action servers, these requests are sent to the domains specified in the action server's configuration by administrators in the Looker **Admin** panel.


#### Proxy server
If the public internet cannot be reached directly, Looker can be configured to use a proxy server for HTTP(S) requests by adding a line like the following to `lookerstart.cfg`: 
```
JAVAARGS="-Dhttp.proxyHost=myproxy.example.com
  -Dhttp.proxyPort=8080
  -Dhttp.nonProxyHosts=127.0.0.1|localhost
  -Dhttps.proxyHost=myproxy.example.com
  -Dhttps.proxyPort=8080"
```

Note that internode communications happen over HTTPS, so if you use a proxy server and your instance is clustered, you will usually want to add the IPs/host names for all the nodes in the cluster to the `Dhttp.nonProxyHosts` argument. 
### Internode communications
#### Internal host identifier
Within a cluster, each node must be able to communicate with the other nodes. To allow this, the hostname or IP address of each node is specified in the startup configuration. When the node starts up, this value will be written into the MySQL repository. Other members of the cluster can then refer to those values to communicate with this node. To specify the hostname or IP address in the startup configuration, add `-H node1.looker.example.com` to the `LOOKERARGS` environment variable in `lookerstart.cfg`. 
Since the hostname must be unique per node, the `lookerstart.cfg` file needs to be unique on each instance. As an alternative to hardcoding the hostname or IP address, the command `hostname -I` or `hostname --fqdn` can be used to find these at runtime. To implement this, add `-H $(hostname -I)` or `-H $(hostname --fqdn)` to the `LOOKERARGS` environment variable in `lookerstart.cfg`. 
#### Internal ports
In addition to the ports 9999 and 19999, which are used for the web and API servers, respectively, the cluster nodes will communicate with each other through a message broker service, which uses ports 1551 and 61616. Ports 9999 and 19999 must be open to end-user traffic, but 1551 and 61616 must be open between cluster nodes. 
## Related resource
  * Customer-hosted infrastructure architecture patterns


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


