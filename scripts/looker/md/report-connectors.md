# Managing report connectors  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/report-connectors

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Managing report connectors
Stay organized with collections  Save and categorize content based on your preferences. 
Looker admins can manage which connectors can be used to create data sources for Looker reports. _Connectors_ are the mechanism by which Looker reports access data from a specific data platform, system, or product. When a Looker report connector is enabled on a Looker instance, users can create _data sources_ to add data from the data source's underlying dataset into their Looker reports.
Looker admins can enable all available report connectors or individual connectors. Google-authored connectors are enabled by default.
## Before you begin
To manage the connectors that are available to use to create data sources on Looker reports, note the following requirements:
  * The Looker instance must meet all requirements to support Studio in Looker.
  * A Looker admin must enable Studio in Looker.
  * Users must have the Looker Admin role to enable or disable report connectors.


## Enabling report connectors
To enable one or more report connectors, follow these steps:
  1. In your Looker instance's **Admin** panel, navigate to the **Reports (Studio in Looker)** section, and then open the **Report connectors** page: **Admin** > **Reports (Studio in Looker)** > **Report connectors**.
  2. To enable all of the connectors that are available for use in Studio in Looker, turn on **Select all**. Alternatively, to enable individual connectors, turn on each connector's corresponding toggle.


## Disabling report connectors
To disable one or more report connectors, follow these steps:
  1. In your Looker instance's **Admin** panel, navigate to the **Reports (Studio in Looker)** section, and then open the **Report connectors** page: **Admin** > **Reports (Studio in Looker)** > **Report connectors**.
  2. To disable all of the connectors that are available for use in Studio in Looker, turn off **Select all**. Alternatively, to disable individual connectors, turn off each connector's corresponding toggle.


### Effects of disabling report connectors
If a Looker admin disables a connector, the following changes take effect:
  * Users can no longer create Looker reports in the Studio in Looker environment using that connector.
  * Any existing reports that were built with that connector are still accessible from the Looker instance, but report editors can no longer edit the data source.
  * Any existing reports that were built with the disabled connector can no longer be copied.


Looker admins can still remove a data source from an existing report built with a disabled connector.
## Effects of disabling Studio in Looker
If a Looker admin disables Studio in Looker for a Looker instance, all report connectors are disabled automatically.
Re-enabling Studio in Looker restores the default report connector settings.
## Related resources
  * About Looker Studio data sources
  * Feature availability in Studio in Looker


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


