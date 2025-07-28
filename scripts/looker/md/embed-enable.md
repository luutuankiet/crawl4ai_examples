# Getting started with embedding — enabling signed embedding  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/embed-enable

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Getting started with embedding — enabling signed embedding
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Signed embedding is a way to present private embedded Looks, visualizations, Explores, dashboards, or LookML dashboards to your users without requiring them to have a separate Looker login. Instead, users will be authenticated through your own application.
Before you can use signed embedding on your Looker instance, you must enable signed embedding in the Looker Admin panel and then create an embed secret. The embed secret validates that a signed embedding request is legitimate and hasn't been forged by someone else. To enable signed embedding, follow these steps:
  1. In the **Admin** section of Looker, navigate to the **Embed** page.
  2. In the **Embed SSO Authentication** drop-down, if the option is set to **Disabled** select **Enabled** and then click **Update**.
Looker will display additional **Embed** options.
  3. ​​To generate your embed secret key, select the **Set Secret** button in the **Embed Secret** section.
  4. If your application will be using JavaScript events passing to communicate between the iframe where Looker is embedded and the parent application, add the domain name of your parent application to the **Embedded Domain Allowlist** field.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


