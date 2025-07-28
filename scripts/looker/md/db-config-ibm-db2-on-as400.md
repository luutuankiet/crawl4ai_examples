# IBM DB2 on AS400  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/db-config-ibm-db2-on-as400

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Encrypting network traffic




Was this helpful?
Send feedback 
#  IBM DB2 on AS400
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Encrypting network traffic


## Encrypting network traffic
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the Enabling secure database access documentation page.
## Feature support
For Looker to support some features, your database dialect must also support them.
IBM DB2 for AS400 and System i supports the following features as of Looker 23.12:
Feature | Supported?  
---|---  
Support Level | Integration  
Looker (Google Cloud core)  
Symmetric Aggregates  
Derived Tables | Yes  
Persistent SQL Derived Tables | Yes  
Persistent Native Derived Tables | Yes  
Stable Views | Yes  
Query Killing | Yes  
SQL-based Pivots  
Timezones  
SSL | Yes  
Subtotals  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type  
Percentile  
Distinct Percentile  
SQL Runner Show Processes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain  
Oauth Credentials  
Context Comments | Yes  
Connection Pooling  
HLL Sketches  
Aggregate Awareness | Yes  
Incremental PDTs  
Milliseconds | Yes  
Microseconds | Yes  
Materialized Views  
Approximate Count Distinct  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


