# Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-fips-mode

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Create a FIPS 140-2 compliant Looker (Google Cloud core) instance
  * FIPS and database dialects




Was this helpful?
Send feedback 
#  Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create a FIPS 140-2 compliant Looker (Google Cloud core) instance
  * FIPS and database dialects


The Federal Information Processing Standard Publication (FIPS) 140-2 is a US government computer security standard that is used to approve cryptographic modules. New Looker (Google Cloud core) instances that are created with either the **Enterprise** or the **Embed** edition option can be created to meet FIPS 140-2 Level 1 standards.
## Create a FIPS 140-2 compliant Looker (Google Cloud core) instance
To create a new FIPS 140-2 compliant Looker (Google Cloud core) instance, in the **FIPS 140-2 Validated Encryption** portion of the **Encryption** section, select the **Enable FIPS 140-2 Validated encryption** checkbox when you create the Looker (Google Cloud core) instance.
Only new instances can be placed into FIPS-compliant mode.
## FIPS and database dialects
Any database that was used by a Looker (Google Cloud core) instance that is in FIPS-compliant mode won't work with a Looker (Google Cloud core) instance that is not in FIPS-compliant mode.
Several database dialects that are otherwise supported by Looker (Google Cloud core) are not supported in FIPS-compliant mode. The following dialects are not supported in FIPS-compliant mode:
  * Denodo 8
  * Dremio 11+
  * IBM Netezza
  * Microsoft SQL Server (MSSQL)
  * PrestoSQL
  * Teradata
  * Trino


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


