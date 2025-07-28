# Amazon Athena  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-amazon-athena

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic
  * Configuring an Amazon Athena connection
  * Specifying your S3 bucket for query results output and PDTs
    * S3 bucket considerations




Was this helpful?
Send feedback 
#  Amazon Athena
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic
  * Configuring an Amazon Athena connection
  * Specifying your S3 bucket for query results output and PDTs
    * S3 bucket considerations


Looker supports connections to Amazon Athena, an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Amazon Athena is serverless, so there is no infrastructure to manage. You are charged only for the queries that are run.
## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Configuring an Amazon Athena connection
This page describes how to connect Looker to an Amazon Athena instance.
  1. Ensure that you have the following:
     * A pair of Amazon AWS access keys.
     * The S3 bucket containing the data you want to query in Looker with Amazon Athena. The Amazon AWS access keys must have read-write access to this bucket.
> Amazon Athena must have access to this S3 bucket by either a role or a permission set, as well as by firewall rules. Do not add security rules to the S3 bucket for Looker's IP, since this can inadvertently block Amazon Athena's access to the S3 bucket. (For other dialects besides Amazon Athena, users may want to limit access to the data from the network layer with an IP allowlist, as described on the Enabling secure database access documentation page.)
     * Knowledge of where your Amazon Athena instance data is located. The region name can be found in the upper right-hand portion of the Amazon Console.
  2. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  3. Fill out the connection details:
     * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
     * **Dialect** : Select **Amazon Athena**.
     * **Host** and **Port** : Specify the name of the host and port as described in the Athena documentation on the JDBC URL format. The host should be a valid Amazon endpoint (like `athena.eu-west-1.amazonaws.com`), and the port should stay at `443`. An up-to-date list of endpoints that support Athena can be found on this AWS General Reference page.
     * **Database** : Specify the default database that you would like modeled. Other databases can be accessed, but Looker treats this database as the default database.
     * **Username** : Specify the AWS access key ID.
     * **Password** : Specify the AWS secret access key.
     * **Enable PDTs** : Use this toggle to enable persistent derived tables (PDTs). Enabling PDTs reveals additional PDT fields and the **PDT Overrides** section for the connection.
     * **Temp Database** : Specify the name of the output directory in your S3 bucket where you want Looker to write your PDTs. The full path to your output directory must be specified in the **Additional JDBC parameters** field; see the Specifying your S3 bucket for query results output and PDTs section on this page.
     * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the Connecting Looker to your database documentation page.
     * **Additional JDBC parameters** : Specify additional parameters for the connection: 
       * The `s3_staging_dir` parameter is the S3 bucket that Looker should use for query results output and PDTs; see the Specifying Your S3 bucket for query results output and PDTs section on this page.
       * Flag for streaming results. If you have the `athena:GetQueryResultsStream` policy attached to your Athena user, you can add `;UseResultsetStreaming=1` to the end of your additional JDBC parameterss to significantly improve the performance of large result set extraction. This parameter is set to `0` by default.
       * Optional additional parameters to add to the JDBC connection string.
     * **SSL** : Ignore; by default, all connections to the AWS API will be encrypted.
     * **Max connections per node** : By default, this is set to 5. You can increase this up to 20 if Looker is the main query engine running against Athena. See the Athena service limits documentation for more details about the service limits. See the Connecting Looker to your database documentation page for more information.
     * **Connection Pool Timeout** : Specify the connection pool timeout. By default, the timeout is set to 120 seconds. See the Connecting Looker to your database documentation page for more information.
     * **SQL Runner Precache** : Unselect this option if you prefer SQL Runner to load table information only when a table is selected. See the Connecting Looker to your database documentation page for more information.
     * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the Using time zone settings documentation page for more information.


To verify that the connection is successful, click **Test**. See the Testing database connectivity documentation page for troubleshooting information.
To save these settings, click **Connect**.
## Specifying your S3 bucket for query results output and PDTs
Use the **Additional JDBC parameters** field of the **Connections** page to configure the path to the S3 bucket that Looker will use for storing query results output, and to specify the name of the output directory in the S3 bucket where you want Looker to write PDTs. Specify this information using the `s3_staging_dir` parameter.
The `s3_staging_dir` JDBC parameter is an alternative way to configure the Amazon Athena `S3OutputLocation` property, which is required for Athena JDBC connections. See the Athena documentation on JDBC Driver Options for more information and a list of all available JDBC driver options.
In the **Additional JDBC parameters** field, specify the `s3_staging_dir` parameter using the following format:
```
`s3_staging_dir=s3://<s3-bucket>/<output-path>`

```

Where:
  * `<s3-bucket>` is the name of the S3 bucket.
  * `<output-path>` is the path where Looker will write query results output.


> The AWS access key pair must have write permissions to the `<s3-bucket>` directory.
To configure the directory where Looker will write PDTs, enter the _path of the directory in the S3 bucket_ in the **Temp Database** field. For example, if you want Looker to write PDTs into `s3://<s3-bucket>/looker_scratch`, then enter this in the **Temp Database** field:
```
`looker_scratch`

```

Only enter the _path of the directory_. Looker gets the S3 bucket name from the `s3_staging_dir` parameter that you enter in the **Additional JDBC Parameters** field.
### S3 bucket considerations
It is recommended that you configure Amazon S3 object lifecycles to periodically clean out unneeded files in your specified S3 bucket. There are reasons for this:
  * Athena stores query results for every query in an S3 bucket. See Athena Querying.
  * If you have PDTs enabled, when a PDT is built, metadata about the created table is stored in the S3 bucket.


## Resources
  * Amazon Athena documentation
  * Amazon Web Services Console for Athena (requires an AWS login)
  * Amazon Athena SQL and HiveQL reference


## Debugging
Amazon provides `LogLevel` and `LogPath` JDBC driver options for debugging connections. To use them, add `;LogLevel=DEBUG;LogPath=/tmp/athena_debug.log` to the end of the **Additional JDBC Parameters** field and test the connection again.
If Looker is hosting the instance, then Looker Support or your analyst will need to retrieve this file to continue debugging.
## Feature support
For Looker to support some features, your database dialect must also support them.
Amazon Athena supports the following features as of Looker 25.10:
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
List type | Yes  
Percentile | Yes  
Distinct percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain  
OAuth 2.0 credentials  
Context comments | Yes  
Connection pooling  
HLL sketches | Yes  
Aggregate awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds  
Materialized views  
Period-over-period measures  
Approximate count distinct | Yes  
## Next steps
After you have completed the database connection, configure authentication options.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


