# Enabling and disabling Looker reports  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/enabling-studio-in-looker

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  Enabling and disabling Looker reports
Stay organized with collections  Save and categorize content based on your preferences. 
This document provides guidance for enabling Looker reports on your Looker (original) or Looker (Google Cloud core) instance.
## Requirements and limitations
Before you enable Looker reports, verify that your Looker (original) or Looker (Google Cloud core) instance meets the following requirements:
  * Your Looker instance must be running Looker 24.18 or later and be Looker-hosted.
  * If your Looker instance uses Google OAuth for authentication, your instance must be running Looker 25.4 or later.
  * You must have the Admin Looker role within your Looker instance.


### Limitations
Looker reports are in preview, and the following limitations apply:
  * Looker reports aren't supported for Looker (Google Cloud core) instances that are configured to use CMEK, VPC-SC, or FIPS 140-2 validated encryption.
  * Looker (Google Cloud core) users who are granted the Admin via IAM role, but not the Looker Admin role, won't be able to create or view reports. To enable report usage, assign the Looker Admin role to these users on the Looker **Roles** page in the Admin panel.
  * Users won't be able to use Looker reports if they log in to their Looker instance by using secondary authentication.
  * Looker reports are not accessible using the Looker mobile application.


## Enabling Looker reports
To enable Looker reports, follow the instructions for Looker (original) or Looker (Google Cloud core):
  * Looker (original)
  * Looker (Google Cloud core)


### Looker (original)
To enable Looker reports for a Looker (original) instance, follow these steps:
  1. In Looker, navigate to **Admin** > **Labs** , and enable the **Access Studio in Looker** Labs feature.
  2. In Looker, navigate to **Admin** > **Reports** > **Reports setup**.
  3. On the **Reports** page, enable the **Enable Reports** option.


### Looker (Google Cloud core)
To enable Looker reports for a Looker (Google Cloud core) instance, follow these steps:
  1. In Looker, navigate to **Admin** > **Reports** > **Reports setup**.
  2. On the **Reports** page, enable the **Enable Reports** option.


## Using Looker reports with Gemini in Looker
When Looker reports and Gemini in Looker are enabled for a Looker instance, Looker users who have the appropriate permissions can query Looker Explore data in natural language by accessing Conversational Analytics.
  * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the Admin settings — Gemini in Looker documentation page.
  * For Looker (Google Cloud core), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the Administer Gemini on your Looker (Google Cloud core) instance documentation page.


## Disabling Looker reports
To disable Looker reports, follow these steps:
  1. Navigate to **Admin** > **Reports** > **Reports setup**.
  2. Disable the **Enable Reports** option.
  3. Confirm that you understand that you will lose all your report data after 30 days if you disable Looker reports by selecting the box.
  4. Click **Disable**.


## Restoring access to Looker reports
To restore access to existing Looker reports on your Looker instance, follow the steps to re-enable Looker reports within 30 days of disabling the feature.
After you re-enable Looker reports, some reports might appear in the **Recovered reports** folder. This typically occurs if the report's original folder was deleted or if the folder's permissions were changed. Admins can move these reports from the **Recovered reports** folder to another folder or delete the reports.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


