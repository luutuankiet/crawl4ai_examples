# Admin settings - Legacy features  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/legacy-feature-schedule

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Learning about new legacy features
  * Enabling and disabling legacy features
  * Migrating away from legacy features
    * Planning your migration
  * Legacy feature schedule
    * Current legacy features
    * Previously removed legacy features




Was this helpful?
Send feedback 
#  Admin settings - Legacy features
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Learning about new legacy features
  * Enabling and disabling legacy features
  * Migrating away from legacy features
    * Planning your migration
  * Legacy feature schedule
    * Current legacy features
    * Previously removed legacy features


Looker will occasionally make updates to product design and functionality that render an existing feature's functionality obsolete. In some cases, the feature may be designated as a _legacy_ feature — a feature that remains backward compatible for existing workflows. A legacy feature provides the option for existing users to continue to use the feature's functionality. When a legacy feature is enabled, the Looker instance cannot support the old and new functionality simultaneously.
After you learn about a new legacy feature, you should start planning to migrate to the new functionality before you disable the legacy feature.
See the Legacy feature schedule section on this page for version information about when each legacy feature is introduced, disabled, and removed from Looker.
## Learning about new legacy features
Looker announces new legacy features in the release notes. See the Looker releases page for links to the release notes for the latest Looker release.
The Current legacy features section later on this page provides a timeline showing when current legacy features will be disabled and formally removed from the Looker product. See the Previously removed legacy features table on this page for Information about legacy features that have already been removed from Looker.
## Enabling and disabling legacy features
New features that replace legacy features are often simpler, more reliable, more performant, and/or more useful than the features they replace. To take advantage of the improved functionality of a new feature that replaces a legacy feature, migrate away from the legacy feature. Once that transition is complete, a Looker admin can disable the legacy feature on the Legacy Features page in the **Admin** panel.
The **Legacy Features** page appears in the **Admin** panel only if there are legacy features available for that Looker instance. The number located next to the **Legacy Features** admin menu item indicates the number of legacy features that are enabled.
When Looker is updated, some legacy features are enabled by default, which means that the old feature is still active. When you're ready to move to the new feature, you can turn the legacy feature off.
> If your Looker instance is created after a legacy feature is disallowed, that feature won't appear on the **Legacy Features** page, and admins won't be able to turn it on. The **Legacy Features** page won't appear in the **Admin** panel if there are no legacy features available to your instance for your current Looker version.
> If you update your existing Looker instance to a version in which a legacy feature is disabled by default, your instance will use the new feature behavior automatically.
## Migrating away from legacy features
Eventually, all legacy features are removed from Looker, so Looker strongly recommends moving away from their use. Start planning your migration as early as possible to avoid disruptions to your workflows.
### Planning your migration
Looker announces new legacy features in the release notes. When needed, Looker provides transition guidelines for migrating away from legacy features. The Legacy feature schedule on this page provides a timeline that shows when current legacy features have been or will be formally removed from the Looker product. The schedule also notes when the features will be disabled by default.
Leave the legacy feature enabled while you implement any necessary transition guidelines. Once these guidelines have been implemented, disable the legacy feature. Be mindful of migrating away from the legacy feature before updating your Looker instance to the version in which the legacy feature is disabled by default. If you have any issues implementing the improved replacement feature, open a support request.
## Legacy feature schedule
  * **Introduced** indicates the version or date in which the feature becomes a legacy feature and appears in the **Legacy Features** page in the **Admin** panel.
  * **Disabled** indicates the version or date in which the legacy feature is turned off for all instances that update to the release. The legacy feature toggle remains available in the **Legacy Features** page for the purposes of remediation, if required.
  * **Disallowed** indicates the version or date in which the legacy feature is removed from the **Legacy Features** page for newly created Looker instances. If you update your existing Looker instance to this version, the legacy feature toggle remains available.
  * **Removed** indicates the version or date in which the legacy feature is removed from the **Legacy Features** page for all Looker instances.


### Current legacy features
**Use Legacy LookML Runtime**  
---  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When this legacy feature is enabled, all LookML projects will use the legacy LookML runtime by default rather than the new LookML runtime. To enable new LookML runtime for a LookML project while this legacy feature is on, add a `new_lookml_runtime: yes` LookML statement to the LookML project's manifest file. | 22.6 | 22.14 | 24.2 | TBD | **Active**  
**Use Legacy Project Creation Page**  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When this legacy feature is enabled, it enables the deprecated **New Project** (`/projects/new`) page in Looker and replaces the **Create a Model** (`/projects/generator`) page in Looker. Enable this feature if you don't want to use the new model creation workflow. | 24.20 | 26.4 | 26.18 | 26.18 | **Active** | Creating a new LookML project  
**Use Legacy Connections Page**  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When this legacy feature is enabled, it enables the legacy **Connections** page in Looker. Enable this feature if you don't want to use the new **Connections** workflow for creating database connections in Looker. | 25.4 | 25.8 | 25.10 | 25.18 | **Active** | Connecting Looker to your database  
### Previously removed legacy features
Legacy Feature | Introduced | Disabled | Removed | Status | Resources  
---|---|---|---|---|---  
Old field chooser | 3.18 | 3.38 | **Removed in Looker 3.38**  
Field labels can override view label | 3.16 | 3.44 | 3.46 | **Removed in Looker 3.46**  
Leading period in field names | 3.16 | 3.44 | 3.46 | **Removed in Looker 3.46**  
Uppercase labels in download and chart configurations | 3.16 | 3.44 | 3.46 | **Removed in Looker 3.46**  
Send email from looker@looker.com | 3.32 | 3.44 | 3.46 | **Removed in Looker 3.46**  
Default Redshift PDT distribution style EVEN | 3.36 | 3.44 | 3.46 | **Removed in Looker 3.46**  
$$ substitution | 3.46 | 3.48 | 3.50 | **Removed in Looker 3.50**  
Joins declared in views | 3.46 | 3.48 | 3.50 | **Removed in Looker 3.52**  
LookML "scoping" parameter | 3.46 | 3.48 | 3.50 | **Removed in Looker 3.52**  
Legacy drill behavior | 3.42 | 4.8 | 4.22 | **Removed in Looker 4.22**  
Add unscoped field name alias | 3.52 | 3.54 | 3.56 | **Removed in Looker 4.6**  
Unsafe Liquid functions | 3.48 | 4.20 | 5.0 | **Removed in Looker 5.0**  
Non-symmetric aggregates | 3.16 | 4.20 | 5.0 | **Removed in Looker 5.0**  
Row limit only | 3.16 | 4.20 | 5.0 | **Removed in Looker 5.0**  
LookML `decimals` parameter and `int` field type | 3.38 | 5.0 | 5.4 | **Removed in Looker 5.4**  
Deprecated LookML parameters | 3.16 | 5.0 | 5.4 | **Removed in Looker 5.4**  
Legacy Oracle security settings | 3.50 | 5.0 | 5.4 | **Removed in Looker 5.4**  
Single row table headers | 3.52 | 5.0 | 5.4 | **Removed in Looker 5.4**  
JSON numbers as strings | 3.52 | 4.0 & 5.0 | 5.4 | **Removed in Looker 5.4**  
Coerce dimensions to measures | 3.54 | 5.0 | 5.4 | **Removed in Looker 5.4**  
Default query result persistence is five minutes | 4.2 | 5.0 | 5.4 | **Removed in Looker 5.4**  
YAML-based LookML for modeling  | 4.4 | 4.10 & 5.0 | 5.4 | **Removed in Looker 5.4**  
Implicit dashboard default timezone  | 4.10 | 5.0 | 5.4 | **Removed in Looker 5.4**  
Allow unlimited downloads that might crash Looker  | 4.14 | 5.0 | 5.4 | **Removed in Looker 5.4**  
User-based dev mode  | 4.16 | 4.16 & 5.0 | 5.4 | **Removed in Looker 5.4**  
Allow creating legacy API-only users | 4.0 | 4.0 & 4.20 | 5.12 | **Removed in Looker 5.12**  
Allow calling legacy query API  | 5.2 | 5.6 | 5.12 | **Removed in Looker 5.12**  
Allow the `access_filter_fields` parameter  | 4.14 | 5.22 | 6.0 | **Removed in Looker 3.38**  
Native derived tables convert dates and yesnos to strings  | 5.22 | 6.0 | 6.6 | **Removed in Looker 6.6**  
Legacy visualizations  | 6.0 | 6.0 | 6.6 | **Removed in Looker 6.6**  
Show full field name  | 6.8 | 6.8 | 6.12 | **Removed in Looker 6.12**  
Legacy rendering  | 6.4 | 6.6 | 6.18 | **Removed in Looker 6.18**  
Legacy .strings files for localization | 7.2 | 7.8 | 7.12 | **Removed in Looker 7.12** | Transition guidelines   
IDE Folders Toggle | 7.0 | 7.10 | 7.12 | **Removed in Looker 7.12** | Migrating to IDE folders  
Snowflake Unquoted Database Name | 7.8 | 7.12 | 7.16 | **Removed in Looker 7.16** | Snowflake connection documentation  
Treat the Datatype Datetime as a Timestamp | 7.14 | 7.20 | 21.4 | **Removed in Looker 21.4** | `datatype` parameter documentation  
Unsafe Custom Visualizations | 7.20 | 21.6 | 21.6 | **Removed in Looker 21.6** | Admin Settings – Visualizations documentation  
Revert to Legacy Explore Field Picker | 21.12 | 21.12 | 21.16 | **Removed in Looker 21.16** | Legacy field picker documentation  
Legacy Branding | 7.18 | 7.20 | 21.18 | **Removed in Looker 21.18**  
Syntax Tolerant Liquid | 21.6 | 21.14 | 22.2 | **Removed in Looker 22.2**  
Use old navigation and legacy routing | 21.20 | 22.0 | 22.2 | **Removed in Looker 22.2** | New navigation documentation  
Require authentication to retrieve API specifications | 21.14 | 21.18 | 22.4 | **Removed in Looker 22.4**  
Save to shared space with `external_group_id` | 21.4 | 21.16 | 22.4 | **Removed in Looker 22.4**  
Legacy Value Formatting | 21.4 | 21.4 | 22.6 | **Removed in Looker 22.6**  
Legacy Query Streaming | 21.8 | 21.8 | 22.8 | **Removed in Looker 22.8**  
Add Looks to dashboards | 21.12 | 21.10 | 22.12 | **Removed in Looker 22.12** | Adding saved content to dashboards  
Save as look keyboard shortcut | 22.0 | 22.0 | 22.14 | **Removed in Looker 22.14**  
Allow double-click to select text in textarea in table visualizations | 22.0 | 22.14 | 22.14 | **Removed in Looker 22.14**  
Popular fields in Explore search | 22.0 | 22.0 | 22.20 | **Removed in Looker 22.20**  
Allow XHTML-style Empty Tags in Custom Visualizations | 21.20 | 22.20 | 22.20 | **Removed in Looker 22.20** | Allowing XHTML-style empty tags in custom visualizations  
Use old dashboard routes | 21.18 | 21.20 | 22.20 | **Removed in Looker 22.20**  
Revert to Legacy Dashboards | 7.18 | 21.0 | 22.20 | **Removed in Looker 22.20**  
Legacy Render Card Height | 22.0 | 22.10 | 23.0 | **Removed in Looker 23.0**  
Can use Legacy Dashboards | 22.20 | 23.2 | 23.6 | **Removed in Looker 23.6** | Transition guidelines  
Use Legacy Hosted Action Hub | 22.6 | 22.6 | 22.20 | **Removed in Looker 23.12**  
Use Legacy Internal Query API | 23.0 | 23.2 | 23.8 | **Removed in Looker 23.12**  
Deny API 3.x Requests | 23.10 | 23.14 | 23.14 | **Removed in Looker 23.14**  
Use Legacy Homepage Sidebar | 23.8 | 23.12 | 23.16 | **Removed in Looker 23.16**  
Allow API 3.x requests | 23.14 | 23.14 | 23.18 | **Removed in Looker 23.18**  
Always hide Row Totals series from stacked charts | 23.0 | 23.0 | 23.20 | **Removed in Looker 23.20**  
Disallow Numeric Query IDs | 24.2 | 24.10 | 24.10 | **Removed in Looker 24.10**  
Allow Legacy Maps | 23.10 | 24.8 | 24.18 | **Removed in Looker 24.18**  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


