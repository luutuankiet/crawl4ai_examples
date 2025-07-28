# View instance logs for Looker (Google Cloud core)

**Source:** https://cloud.google.com/looker/docs/looker-core-logging

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  View instance logs for Looker (Google Cloud core)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


This page describes how to find and use Cloud Logging to view and query logs for your Looker (Google Cloud core) instance.
Looker (Google Cloud core) uses Cloud Logging. See the cloud logging documentation for complete information.
## Required roles
To understand the required roles for Cloud Logging, visit the Access control with IAM page of the Cloud Logging documentation.
## View logs
To view logs for your Looker (Google Cloud core) instance log entries, select one of the following options:
More
  1. In the Google Cloud console, go to **Logging > Logs Explorer**
  2. Select an existing Looker (Google Cloud core) project at the top of the page.
  3. In the Query builder, add the following:
     * Resource: Select **Looker instance**. In the dialog, select a Looker (Google Cloud core) instance ID.
     * Log names: Scroll to the Looker section and select appropriate log files for your instance. For example: 
       * looker.googleapis.com%2FContentAccess
       * looker.googleapis.com%2FUserLogin
     * Severity: Select a log level.
     * Time range: Select a preset or create a custom range.


Use the `gcloud logging` command to view log entries.
```
gcloudread"resource.type=looker.googleapis.com/Instance"\
--project=PROJECT_ID\
--limit=10\
--format=json
```

Replace the following:
  * PROJECT_ID: the ID of the Google Cloud project in which the Looker (Google Cloud core) instance resides.


You may also include the following flags:
  * The `limit` flag is an optional parameter that indicates the maximum number of entries to return.


## Troubleshoot
Issue | Troubleshooting  
---|---  
Log files are incomplete. | Check the severity level at which your logging is configured. Log messages below the level configured will be dropped.   
Operations information is not found in logs. | You want to find more information about an operation.For example, a user was deleted but you can't find out who did it. The logs show the operation started but don't provide any more information. You must enable audit logging for detailed and personal identifying information (PII) like this to be logged.  
Log files are hard to read. | You'd rather view the logs as JSON or text. You can use the  `gcloud logging read` command along with Linux post-processing commands to download the logs. To download the logs as JSON, use the following code: ```
gcloudread\
"resource.type=looker.googleapis.com/Instance \
AND logName=projects/PROJECT_ID \
/logs/looker.googleapis.com%2FLOG_NAME"\
--format\
--project=PROJECT_ID\
--freshness="1d"\
>
```
Replace the following:
  * `PROJECT_ID`: the ID of the Google Cloud project in which the Looker (Google Cloud core) instance resides
  * `LOG_NAME`: the resource name of the log

To download the logs as text, use the following code: ```
gcloudread\
"resource.type=looker.googleapis.com/Instance \
AND logName=projects/PROJECT_ID \
/logs/looker.googleapis.com%2FLOG_NAME"\
--format\
--project=PROJECT_ID\
--freshness="1d"|'fromstream(1|truncate_stream(inputs)) \
| .textPayload'\
--order=asc
>
```
Replace the following:
  * `PROJECT_ID`: the ID of the Google Cloud project in which the Looker (Google Cloud core) instance resides
  * `LOG_NAME`: the resource name of the log

  
## What's next
  * Looker (Google Cloud core) audit logging


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


