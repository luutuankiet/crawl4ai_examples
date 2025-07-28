# Looker (Google Cloud core) release overview

**Source:** https://cloud.google.com/looker/docs/looker-core-release-process

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Development and release cycle
  * Update process
    * What if I need to skip a new release version?
    * Does maintenance downtime count toward the SLA?
    * Update your Looker (Google Cloud core) version following a deny maintenance period
  * Extended support release program




Was this helpful?
Send feedback 
#  Looker (Google Cloud core) release overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Development and release cycle
  * Update process
    * What if I need to skip a new release version?
    * Does maintenance downtime count toward the SLA?
    * Update your Looker (Google Cloud core) version following a deny maintenance period
  * Extended support release program


This guide explains the standard release and update processes for Looker (Google Cloud core), along with best practices and variations that may better fit your needs.
## Development and release cycle
A new minor version of Looker (Google Cloud core) is deployed over the course of roughly a couple of weeks. No new releases nor deployments happen in the month of December.
At times, small update patches will be released for fixes that should not wait for the next release. These are nearly always fixes for critical product or security issues. Ideally, no new features would ever be included in a patch release. The application of patch updates follows the same process as upgrading during a standard release.
### Release numbers
The release numbering scheme for Looker (Google Cloud core) uses the same release numbering as for Looker (original) instances, which is a three-number sequence: X.Y.Z, where X is the last two digits of the year of the release, Y is the monthly version (starting with 0 in January, and using even numbers for each subsequent month), and Z is the patch release version. For example, Looker (Google Cloud core) 23.10.1 would be the first patch of the Looker (Google Cloud core) release from June of 2023.
### Release notes
Stay current with any new features and issue fixes by checking out the release notes. See the Looker releases page for links to the release notes and changelog for the latest release.
## Update process
Looker (Google Cloud core) applies updates on a rolling basis over the course of a couple of weeks. If you have defined a preferred window for maintenance of your Looker (Google Cloud core) instance, the Looker (Google Cloud core) Release and Ops teams will apply updates during the maintenance window. If you have not set a maintenance window, you will receive the update within two weeks of the version rollout.
If you have set a maintenance window for your Looker (Google Cloud core) instance, you can opt in to receive notifications ahead of upcoming maintenance. Updates generally take around an hour within the maintenance window and may result in downtime.
### What if I need to skip a new release version?
You can defer scheduled maintenance of your Looker (Google Cloud core) instance by defining a deny maintenance period of up to 60 days in length.
### Does maintenance downtime count toward the SLA?
Downtime associated with maintenance does not apply towards the Looker (Google Cloud core) Service Level Agreement.
### Update your Looker (Google Cloud core) version following a deny maintenance period
Following a deny maintenance period, your Looker (Google Cloud core) instance will usually be updated during the first release that occurs after your deny maintenance period ends.
## Extended support release program
Looker (Google Cloud core) does not provide an extended support release (ESR) program.
## Getting support
If you have questions, see the Getting support for Looker (Google Cloud core) page for information on troubleshooting and contacting Google Cloud support.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


