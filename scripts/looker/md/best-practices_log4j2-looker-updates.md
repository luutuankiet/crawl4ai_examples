# Log4j 2 Looker updates  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/log4j2-looker-updates

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 




Was this helpful?
Send feedback 
#  Log4j 2 Looker updates
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 
  * December 28 & 29, 2021 


**What happened / What is the Apache Log4j vulnerability?**
Multiple security vulnerabilities in Apache Log4j 2.X, including CVE-2021-44228,CVE-2021-45046,CVE-2021-44832,CVE-2021-45105, CVE-2021-44832, have been disclosed starting on December 10, 2021. The vulnerabilities range from a critical 0-day exploit in the library that can allow attackers to perform Remote Code Execution (RCE) to potential DOS concerns, all with varying levels of CVSS scores. 
**Is Looker impacted? How did Looker respond?**
Looker uses Log4j in its application and the team has addressed the vulnerability by reviewing Looker's usage and configuration of the Log4j libraries and upgrading the Log4j libraries with a patch that includes at least version 2.17.0 released by Apache as indicated in the Apache Log4j Security Vulnerabilities website. 
Looker-hosted instances have been updated with a Looker version that uses Log4j 2.17.0. Third party driver dependencies have been updated to the most up-to-date version provided by the third parties. Customers on customer hosted instances should update their instance as soon as possible to a version listed at the bottom of this page which contains these updated versions of Log4j 2 for Looker and third party drivers. 
Looker product and security teams have determined that Looker is not vulnerable to CVE-2021-44832 due to our usage and configuration of the library. 
**How has Looker mitigated the Log4j vulnerability?**
Looker has updated or released patched versions with updated Log4j libraries. Looker will continue to follow a remediation process to monitor and update our Log4j libraries as new updates become available and as our third parties update their libraries. Looker has set up monitoring and alerting in response to the known Log4j vulnerabilities and, if needed, we will communicate on issues through our standard incident response process. 
**How can I see what version my instance is on?**
Click on the question mark icon in the upper-right section of your Looker instance. Your version number will be shown to the right of the Release Notes section. 
**Release Version** |  **Current recommended version** |  **Date of Update for Looker Hosted Instances**  
---|---|---  
##  21.20
| 
##  21.20.30+
| 
##  December 28 & 29, 2021  
##  21.18
| 
##  21.18.40+
| 
##  December 28 & 29, 2021  
##  21.16
| 
##  21.16.43+
| 
##  December 28 & 29, 2021  
##  21.14
| 
##  21.14.51+
| 
##  December 28 & 29, 2021  
##  21.12
| 
##  21.12.72+
| 
##  December 28 & 29, 2021  
##  21.10
| 
##  21.10.54+
| 
##  December 28 & 29, 2021  
##  21.8
| 
##  21.8.55+
| 
##  December 28 & 29, 2021  
##  21.6
| 
##  21.6.76+
| 
##  December 28 & 29, 2021  
##  21.4
| 
##  21.4.66+
| 
##  December 28 & 29, 2021  
##  21.0
| 
##  21.0.92+
| 
##  December 28 & 29, 2021  
##  7.20
| 
##  7.20.77+
| 
##  December 28 & 29, 2021  
##  7.18
| 
##  7.18.77+
| 
##  December 28 & 29, 2021  
##  7.16
| 
##  7.16.85+
| 
##  December 28 & 29, 2021  
##  7.14
| 
##  7.14.57+
| 
##  December 28 & 29, 2021  
##  7.12
| 
##  N/A
| 
##  N/A  
##  7.10
| 
##  7.10.77+
| 
##  December 28 & 29, 2021  
##  7.8
| 
##  7.8.55+
| 
##  December 28 & 29, 2021  
##  7.6
| 
##  N/A
| 
##  N/A  
##  7.4
| 
##  7.4.78+
| 
##  December 28 & 29, 2021  
##  7.2
| 
##  7.2.64+
| 
##  December 28 & 29, 2021  
##  7.0
| 
##  7.0.58+
| 
##  December 28 & 29, 2021  
##  6.24
| 
##  6.24.76+
| 
##  December 28 & 29, 2021  
##  1.0-6.22
| 
##  N/A
| 
##  N/A  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


