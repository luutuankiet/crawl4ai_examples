# EmbedConfig  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedConfig

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  EmbedConfig
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
domain_allowlist
string[] 
alert_url_allowlist
string[] 
alert_url_param_owner
string 
Owner of who defines the alert/schedule params on the base url
alert_url_label
string 
Label for the alert/schedule url
sso_auth_enabled
boolean 
Is SSO embedding enabled for this Looker
embed_cookieless_v2
boolean 
Is Cookieless embedding enabled for this Looker
embed_content_navigation
boolean 
Is embed content navigation enabled for this looker
embed_content_management
boolean 
Is embed content management enabled for this Looker
strict_sameorigin_for_login
boolean 
When true, prohibits the use of Looker login pages in non-Looker iframes. When false, Looker login pages may be used in non-Looker hosted iframes.
look_filters
boolean 
When true, filters are enabled on embedded Looks
hide_look_navigation
boolean 
When true, removes navigation to Looks from embedded dashboards and explores.
embed_enabled
_lock_
boolean 
True if embedding is licensed for this Looker instance.
## Related Types


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


