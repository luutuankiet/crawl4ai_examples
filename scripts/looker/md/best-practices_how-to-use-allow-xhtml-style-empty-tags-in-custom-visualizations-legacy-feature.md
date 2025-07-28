# Allowing XHTML-style empty tags in custom visualizations  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-use-allow-xhtml-style-empty-tags-in-custom-visualizations-legacy-feature

Skip to main content 

Console 




Send feedback 
#  Allowing XHTML-style empty tags in custom visualizations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A cross-site scripting (XSS) vulnerability, CVE-2020-11022, exists in jQuery versions later than or equal to 1.2 and earlier than 3.5.0. This flaw allows an attacker with the ability to supply input to the `parseHTML()` function to inject JavaScript into the page when that input is rendered and to have it delivered by the browser. In Looker 21.18 and earlier, the version of jQuery that was provided as a global variable to a sandboxed custom visualization included this vulnerability. 
Starting in Looker 21.20, the built-in jQuery instance that is available to custom visualizations has been updated, and this vulnerability has been addressed. As a result of addressing this vulnerability, Looker will no longer recognize self-closing XHTML tags, such as `<div />` in custom visualizations. 
In Looker 21.20, a new legacy feature, **Allow XHTML-style Empty Tags in Custom Visualizations** , is included in the **Legacy Features** page in Looker's **Admin** section. Enabling this legacy feature disables protection against CVE-2020-11022, causing self-closing XHTML tags to be recognized in custom visualizations, but also exposing the jQuery vulnerability. If you enable this legacy feature, we strongly recommend that you audit your custom visualizations for self-closing tags, correct any self-closing tags, and disable the legacy feature. This legacy feature is scheduled to be disabled in Looker 22.20, and self-closing XHTML tags will not be allowed. 
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


