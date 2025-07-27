# Admin settings - Extension Framework  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-extension-framework

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Extension Framework
  * Enhanced Extension Loading




Was this helpful?
Send feedback 
#  Admin settings - Extension Framework
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Extension Framework
  * Enhanced Extension Loading


The **Extension Framework** page in the **Platform** section of the **Admin** menu lets you enable or disable Looker extension framework options.
## Extension Framework
When enabled, the **Extension Framework** option lets developers build and run Looker-hosted applications as well as install and run extensions from the Looker Marketplace, such as the API Explorer and the Data Dictionary. This feature is enabled by default.
When this feature is disabled, any extensions that have been installed are hidden and unavailable to users.
Pricing, terms, and other details for Marketplace content and extensions such as the API Explorer and Data Dictionary are listed within the relevant store page. Before users can install and use Marketplace extensions, a Looker admin must enable the Marketplace feature.
## Enhanced Extension Loading
To address potential Content Security Policy (CSP) violations, there is a new, enhanced loading mechanism for the Looker extension framework, which includes the following changes:
  * To fix Content Security Policy (CSP) violations, HTML is generated to load an extension on the server rather than in the browser.
  * The `base` tag is removed, which potentially could impact custom code splitting.
  * The new loader uses a `<!DOCTYPE html>` preamble. This may impact components that use `height: 100%;`. You can mitigate this by using `height: 100vh`.


To use the enhanced loading mechanism, a Looker admin can enable **Enhanced Extension Loading**.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


