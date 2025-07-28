# Looker startup options  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/startup-options

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Startup options list
  * Credentials file format
  * Making startup options permanent




Was this helpful?
Send feedback 
#  Looker startup options
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Startup options list
  * Credentials file format
  * Making startup options permanent


There are a number of Looker startup settings that can optionally be configured on customer-hosted instances. If you do not need to change these options, you may start Looker without them.
## Startup options list
The following table provides a list of current startup options in alphabetical order. You can also display a list of startup options by running the Looker startup script with the option `--help`.
Option | Description  
---|---  
`--alerts-scheduler-threads=<i>` | Number of simultaneous scheduled alerts (default: 3).  
`--ami` | Deprecated. Use `--marketplace=aws` instead.  
`--api-server-max-threads=<i>` | Maximum threads count for Puma API Server.  
`--api-server-min-threads=<i>` | Minimum threads count for Puma API Server.  
`--application-server-max-threads=<i>` | Maximum threads count for Puma Application Server.  
`--application-server-min-threads=<i>` | Minimum threads count for Puma Application Server.  
`--apply-db-migrations` | Apply DB migrations on startup. Only disable if you're applying migrations separately (default: `true`).  
`--async-results-cache-time=<i>` | Length of time to keep async results cached (default: 300).  
`--byoid-studio-load-url=<s>` | URL to load BYOID Studio in to an iframe.  
`--cdn-hosts=<s>` | Comma separated hostnames for CDN pool (default: `static-a.lookercdn.com,static-b.lookercdn.com`).  
`--cipher-key-file=<s>` | Path to file containing cipher key (legacy encryption only).  
`--cloud-trace-enabled` | Enable tracing using default credentials or json credentials if provided via `cloud_trace_json_file` (default: `false`).  
`--cloud-trace-json-file=<s>` | JSON file containing the service account credentials to upload trace data to Google Cloud Trace.  
`--cloud-trace-project-id=<s>` | Google project ID to upload trace data to.  
`--cloud-trace-sample-rate=<f>` | The rate (0-1) with which to sample traces (default: 0.0).  
`--clustered` | Whether this server is part of a cluster (default: `false`).  
`--concurrent-render-caching-jobs=<i>` | Number of simultaneous render caching processes (default: 3).  
`--concurrent-render-jobs=<i>` | Number of simultaneous PhantomJS or Chromium rendering processes (default: 2).  
`--core-on-loopback` | Exposes Core API on loopback interface (default: `false`).  
`--core-port=<i>` | Port to run core on (default: 19999).  
`--customer-artifact-maxsize=<i>` | Maximum size in MB of the customer artifact store.  
`-d, --internal-db-creds=<s>` | Path to YAML file with DB credentials.  
`--daemonize` | Runs as daemon (default: true).  
`--default-mailer-domain=<s>` | Default mailer domain.  
`--default-mailer-fromemail=<s>` | Email address that default mailer emails come from (default: `Looker <noreply@lookermail.com>`).  
`--default-mailer-host=<s>` | Default mailer hostname (default: `smtp.sendgrid.net`).  
`--default-mailer-password=<s>` | Default mailer password (password on command line not recommended).  
`--default-mailer-port=<i>` | Default mailer port (default: 587).  
`--default-mailer-username=<s>` | Default mailer username.  
`--disable-db-log` | Disables logging of internal DB queries (default: `false`).  
`--dogstatsd-host-ip=<s>` | Datadog statsd server host IP.  
`--dogstatsd-host-port=<i>` | Datadog server host port.  
`-e, --help` | Displays this list of startup options.  
`--enable-blobstore-recryption` | Enable Persistent Blobstore recryption on rekey operations (default: `false`).  
`--error-emails-to=<s>` | Error emails to `<email address>`.  
`--experimental-features=<s>` | Comma separated list of allowed experimental features.  
`--experimental-routes=<s>` | Comma separated list of allowed experimental routes that generate routes with the suffix of `-next`.  
`--extension-load-url=<s>` | URL to load extensions into a secure iframe.  
`--external-solr-enabled` | Enable external Solr (as opposed to the default — embedded Solr) (default: `false`).  
`--fips` |  Enable FIPS-140 encryption (default: `false`).  
`--force-cdn` | Forcibly enable CDN (default: `false`).  
`--force-cipher-key` | Disregards safeguards for the cipher key settings (legacy encryption only, default: `false`).  
`--force-enable-pendo` | Enables Pendo guides on private label instances or in embed contexts (default: `false`).  
`--force-error-emails` | Forces Looker to report errors via email (default: `false`).  
`--force-gcm-encryption` | DEPRECATED (this option is no longer necessary).  
`--force-mismatched-internal-db` | Allows use of out-of-sync Looker internal DB (default: `false`).  
`--force-no-cdn` | Forcibly disable CDN (default: `false`).  
`--git-hooks-use-local-path` | Use a local path for the `git_hooks` directory instead of shared storage.  
`--git-performance-logging` | Enables logging of JGit performance (default: `false`).  
`--google-analytics-tracker-id=<s>` | Tracking ID to use for sending pageviews to additional Google Analytics trackers.  
`-h, --hosted` | Hosted by Looker.  
`-H, --hostname=<s>` | Hostname for node-to-node communication.  
`--hosted-action-hub-disabled` | Turn off hosted action hub.  
`--in-memory-cache-size=<i>` | Size (in MB) of in memory cache (default: 200).  
`--integration-proxy-cert=<s>` | Path to Integration Proxy PKI cert file.  
`--integration-proxy-key=<s>` | Path to Integration Proxy PKI key file.  
`--internal-analytics-connection-file=<s>` | YAML file describing the internal analytics connection that hosts data for the `system__activity` model. This option is for use with a read replica backend database only.  
`--internal-analytics-connection-pool-size=<i>` | The number of simultaneous DB connections that may run system activity model queries. This option is for use with a read replica backend database only.  
`--internal-analytics-retention-days=<i>` | The number of days to retain history data in the internal database. This does not affect any ETL process. The default is 90. This option is for use with a read replica backend database only.  
`--k8s-deployment-api-s3bucket-url=<s>` | URL where this Looker process can write S3 bucket credentials to be persisted as Kubernetes secrets.  
`--log-format=<s>` | Log format that is either `text` or `json` (default: `text`).  
`--log-level=<s>` | Log level (default: `info`).  
`--log-to-file` | Sends log output to Looker log file (default: `true`).  
`--lookml-runtime-cache-size=<i>` | Size (in MB) of LookML runtime cache (default: 200).  
`--loose-cipher-key-file` | Don't require `0600` permissions for cipher key file (legacy encryption only, default: `false`).  
`--marketplace=<s>` | Running in a Looker Marketplace instance.  
`--max-async-threads=<i>` | Maximum number of async query threads (default: 200).  
`--max-configurable-db-connections=<i>` | Maximum connection count allowed for a customer DB connection in the UI.  
`--max-db-connections-records=<i>` | Maximum number of connection records allowed in `db_connection` table (default: 10000).  
`--max-pdt-regen-threads=<i>` | Maximum number of PDT regenerator threads.  
`--max-scheduled-plans=<i>` | Maximum number of active recurring scheduled plans (default: `unlimited`).  
`--max-scheduler-jitter-in-seconds=<i>` | Flag to smear schedule runs randomly over the given number of seconds.  
`--max-unstreamed-limit=<i>` | Sets the maximum number of rows that can be returned for all queries that are not streamed (default: 100,000).  
`--min-pdt-regen-threads=<i>` | Minimum threads count for PDT Regenerator.  
`--monitoring-port=<i>` | Port for hosting monitoring (Prometheus, ...) (default: 1552).  
`-n, --node-to-node-port=<i>` | Port for node-to-node communication (default: 1551).  
`--new-cipher-key-file=<s>` | Path to file containing new cipher key (legacy encryption only).  
`--on-disk-cache-size=<i>` | Size (in MB) of disk cache (default: 2000).  
`-p, --port=<i>` | Port to run on (default: 9999).  
`--per-user-query-limit=<i>` | Limits number of concurrent queries per user (default: 15).  
`--per-user-query-timeout=<i>` | Length of per-user timeout to wait for connection (default: 600).  
`--prefer-ipv4` | Prefer IPv4.  
`--public-embed-auth-param-file=<s>` | Authentication parameter file for public auth.  
`--public-host-url=<s>` |  If the `public_host_url` license feature is enabled, this option enables admins to specify a `public_host_url` hostname so that the Looker Action API callback URIs are constructed with the `public_host_url` rather than the default host URL in Looker. The input for the startup option should be `https://<my.host.name>` with no trailing slash in the URL. If using this method, Looker admins must also allowlist the static egress IP addresses listed on the Sharing data through an action hub documentation page.  
`-q, --queue-broker-port=<i>` | Port for queue broker (default: 61616).  
`--qm-long-poll-max-sleep-interval-in-seconds=<f>` | Max sleep interval before the long poll API is going to check if results are available (default: 1).  
`--qm-long-poll-sleep-interval-in-seconds=<i>` | Initial sleep interval before the long poll API is going to check if results are available (default: 0.1).  
`--qm-long-poll-timeout-in-seconds=<i>` | Maximum server side timeout for the long poll API before it returns to the client (default: 30).  
`--query-manager-max-threads=<i>` | Maximum threads count for Query Manager.  
`--query-manager-min-threads=<i>` | Minimum threads count for Query Manager.  
`--query-metrics-retention-hours=<i>` | The number of hours to retain `query_metrics` data in the internal database (default: 336).  
`--queue-startup-timeout-in-seconds=<i>` | How long in seconds to allow connection to the queue on startup (default: 180).  
`--query-task-cleanup-interval-seconds=<i>` | Interval between query task table cleanup jobs (default: 600).  
`--query-task-persistence-duration-minutes=<i>` | Amount of time after query completion to keep rows in the query task table (default: 360).  
`-r, --root` | Allows running as root.  
`--redis-cache-config-file=<s>` | File containing redis configuration.  
`--report-backend-errors, --no-report-backend-errors` | Reports errors from the backend (default: `false`).  
`--report-frontend-errors, --no-report-frontend-errors` | Reports errors from the frontend (default: `false`). NOTE: This startup option is obsolete. Use the `client_monitor` feature flag instead.  
`-S, --ssh-tunnel-sidecar-url=<s>` | The base URL used to connect to the SSH Tunnel Server Sidecar.  
`--scheduled-job-attempt-limit=<i>` | Max number of scheduled job attempts (default: 10).  
`--scheduled-job-max-age-days=<i>` | Maximum age of a scheduled job before it is deleted (default: 60).  
`--scheduler-query-limit=<i>` | Limits number of concurrent scheduled queries (default: 10).  
`--scheduler-query-timeout=<i>` | Length of scheduler timeout to wait for connection (default: 1200).  
`--scheduler-start-delay=<i>` | Number of seconds to delay task runner startup (default: 60).  
`--scheduler-threads=<i>` | Number of simultaneous scheduled tasks (default: 10).  
`--search-result-comparison` | Compare **Search Service** results to legacy results (default: `false`).  
`--search-service` | Enables **Search Service** (default: `false`).  
`--search-service-ab-test` | Enable AB test for **Search Service** (default: `false`).  
`--self-signup` | Allows anyone to create an account for themselves.  
`--shared-storage-dir=<s>` | Path to network file system shared storage.  
`--snowplow-host=<s>` | Extra Snowplow collector.  
`--solr-basic-auth=<s>` | Basic auth credentials for calls to Solr (default: `solr:SolrRocks`).  
`--ssl` | Uses SSL (default: `true`).  
`--ssl-ca-cert=<s>` | Deprecated. Use `--ssl-keystore` instead.  
`--ssl-cert=<s>` | Deprecated. Use `--ssl-keystore` instead.  
`--ssl-key=<s>` | Deprecated. Use `--ssl-keystore` instead.  
`--ssl-keystore-pass-file=<s>` | Path to file containing `ssl-keystore` password.  
`--ssl-keystore-pass=<s>` | Password for `ssl-keystore` file.  
`--ssl-keystore=<s>` | Path to keystore file for SSL.  
`--ssl-provided-externally-by=<s>` | Provides the host:port for an external SSL provider as accessible from the server that is running Looker. When not specified, the Looker app server provides SSL.`--ssl-provided-externally-by=192.168.123.13:443``--ssl-provided-externally-by=localhost:443`  
`--ssl-provided-externally` | Deprecated. Use `--ssl-provided-externally-by` instead.  
`--staging` | Runs server as staging. This option will prevent your staging instance from sending out scheduled reports. However, the staging instance will still continue to run scheduled tasks and will send out error emails to scheduled plan owners if the scheduled task has any issues.  
`--staging-override-email=<s>` | Sends emails on a staging instance to this address instead of their normal destination.  
`--stereo-data-search-enabled` | Enable the stereo data search feature (default: `false`).  
`--studio-load-url=<s>` | URL to load Studio in to an iframe.  
`--studio-one-platform-endpoint=<s>` | Endpoint for Studio One Platform API.  
`--task-monitor-abandoned-query-in-seconds=<i>` | Duration elapsed since the last access for a task to consider the query task abandoned.  
`--task-monitor-query-startup-interval-in-seconds=<i>` | Duration used as a grace period when queries start execution until the first long poll occurs. It helps give more room for callers before starting polling.  
`--task-monitor-sleep-interval-in-seconds=<i>` | Sleep interval before task tracking thread can check whether tasks are abandoned.  
`--unification-jwt-service-account=<s>` | Unification JWT service account.  
`--unlimited-scheduler-threads=<i>` | Number of simultaneous unlimited scheduled tasks (default: 3).  
`--use-custom-jdbc-config` | Whether to use custom JDBC driver config (default: `false`).  
`--user-db-credentials` | Restricted usage. Connections can use per-user credentials (default: `false`).  
`-v, --version` | Prints version and exits.  
## Credentials file format
If you have changed the application database to MySQL, you'll need a credentials file named `looker-db.yml` that includes these settings:
```
dialect: mysql
host: YOUR_HOSTNAME
username: YOUR_USERNAME
password: YOUR_PASSWORD
database: YOUR_DBNAME
port: YOUR_PORT

```

If your MySQL database requires an SSL connection, the `looker-db.yml` file also requires the following:
```
ssl: true

```

## Making startup options permanent
The preferred method for making startup configuration settings permanent is to create a file named **lookerstart.cfg** in the Looker application directory. This file will be executed by the Looker startup script that was provided with your **looker.jar**. The **lookerstart.cfg** file is the recommended place to set environment variables for `JAVAARGS` and `LOOKERARGS` because they will not be overwritten when new versions of the Looker startup script are installed.
Here is an example **lookerstart.cfg** , which disables Looker's SSL and sets it to run on port 8080:
```
LOOKERARGS="--no-ssl --port 8080"

```

Looker will need to be restarted after making changes to **lookerstart.cfg**.
## Next steps
After you have configured Looker startup options, you're ready to configure your SSL certificate for proper HTTPS.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


