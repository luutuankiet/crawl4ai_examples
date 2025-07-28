# Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023)  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * What has changed in Looker 23.6 and beyond?
  * Timeline of changes in earlier Looker versions
    * What changed in Looker 21.20?
    * What changed in Looker 22.20?
    * What changed in Looker 23.2?
  * What should you do?
  * How can you get help?




Was this helpful?
Send feedback 
#  Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * What has changed in Looker 23.6 and beyond?
  * Timeline of changes in earlier Looker versions
    * What changed in Looker 21.20?
    * What changed in Looker 22.20?
    * What changed in Looker 23.2?
  * What should you do?
  * How can you get help?


## Background
In Looker 21.20, we upgraded the default dashboard experience for all users to the new dashboard experience, and we announced that the legacy dashboard experience would be deprecated in Looker 22.20 (released in November 2022), and removed in Looker 23.6 (released in April 2023). 
**Starting in Looker 23.6 (released in April 2023), legacy dashboards are no longer available in Looker.**
## What has changed in Looker 23.6 and beyond?
In Looker 23.6, we removed the **Can use Legacy Dashboards** legacy feature. **Upon upgrade to Looker 23.6, all dashboards will only render using the new dashboard experience.**
Looker developers will not be able to use the `Update Dashboard` Looker API endpoint to revert a dashboard through the `preferred_viewer` property. The `preferred_viewer` property will no longer be honored and will default to the new experience. The `preferred_viewer` LookML parameter on LookML dashboards will also be ignored.
Looker users will not be able to view dashboards in the legacy style by using `/dashboards-legacy/` in the dashboard URL. All links that use `/dashboards-legacy/` will be automatically redirected to `/dashboards/` and will display dashboards in the new dashboard experience.
## Timeline of changes in earlier Looker versions
Changes in Looker 21.20, 22.20, and 23.2 made upgrades to the default dashboard experience in preparation for legacy dashboard removal.
### What changed in Looker 21.20?
In 21.20, as part of the dashboard upgrade process, we introduced a change to dashboard and legacy dashboard URL routing. As a result, any links or bookmarks that used `/dashboards-next/` were automatically redirected to `/dashboards/`. Any links or bookmarks to `/dashboards/` pointed to the new dashboard experience, as opposed to legacy dashboards. 
Looker also introduced two legacy features (**Use old dashboard routes** and **Revert to Legacy Dashboards**). These legacy features were provided so that customers could test and migrate their dashboards to the new experience before the legacy dashboard experience is completely deprecated. 
The **Use old dashboard routes** legacy feature let users use the older routing for dashboards. This means that URLs with `/dashboards/` opened legacy dashboards, and URLs with `/dashboards-next/` opened new dashboard experience dashboards. 
The **Revert to Legacy Dashboard** legacy feature let users downgrade their dashboard through the UI from new dashboard experience dashboards to legacy dashboards. 
### What changed in Looker 22.20?
In Looker 22.20, we removed the **Use old dashboard routes** and **Revert to Legacy Dashboards** legacy features.The removal of these legacy features re-routed all dashboard URLs that used `/dashboards/` to new dashboard experience dashboards and removed the ability to downgrade a dashboard to a legacy dashboard through the Looker UI.
In Looker 22.20 we also added a new legacy feature, **Can use Legacy Dashboards** , which allows users to still render a legacy dashboard by using `/dashboards-legacy/` in the dashboard URL.
Starting with Looker 23.6, we will remove the **Can use Legacy Dashboards** legacy feature, which removes the ability to render dashboards in the legacy experience.
**Note** : Starting with Looker 22.20, we no longer addressed any bugs or accepted new feature requests for legacy dashboards. Moving forward, any bug fixes that are related to dashboards only apply to the new dashboard experience. 
### What changed in Looker 23.2?
In Looker 23.2, the **Can use Legacy Dashboards** legacy feature began defaulting to off, turning off the ability to view dashboards in the legacy experience. Looker admins can manually enable the **Can use Legacy Dashboards** legacy feature to retain the ability to view dashboards in the legacy experience until **Can use Legacy Dashboards** is removed in Looker 23.6. 
## What should you do?
If you do not currently use legacy dashboards, you do not need to do anything. 
If you use legacy dashboards, **we recommend that you migrate the legacy dashboards to the new dashboard experience** as soon as possible. As a test of migration, Looker admins can disable the **Can use Legacy Dashboards** legacy feature to simulate the upgrade of all legacy dashboards to the new dashboard experience. The upgraded rendering of the dashboards can be reviewed, and adjustments can be made to achieve the desired rendering. The Upgrading the default dashboard experience for all Looker users Best Practices page provides more information about migrating. 
**Dashboards in the new experience should render as expected with some minor changes tofunnel, timeline, and table visualizations and an improved filter experience**. Test the changes that go into effect in Looker 23.6 beforehand. The Upgrading the default dashboard experience for all Looker users Best Practices page provides more information about migrating. 
We are prioritizing addressing any migration issues customers encounter. If you experience an issue that is preventing you from migrating your dashboards, fill out and submit this form.
## How can you get help?
During your migration or testing, if you come across any issues that block you from migrating to the new dashboard experience, or if you have existing identified blockers, you have few options. Looker is prioritizing these issues to ensure the migration goes smoothly. 
  1. Contact Looker Support.
  2. Contact your Looker account team.
  3. Connect to the Product Management team by filling out this form.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


