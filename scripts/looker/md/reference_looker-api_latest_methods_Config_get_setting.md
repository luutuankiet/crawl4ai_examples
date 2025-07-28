# Get Setting  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/get_setting

Skip to main content 


  * Español – América Latina

Console  Sign in
  * On this page
  * Get Looker Settings




Send feedback 
#  Get Setting
Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get Looker Settings


Version 4.0.25.10 (latest) 
### Get Looker Settings
Available settings are:
  * allow_user_timezones
  * custom_welcome_email
  * data_connector_default_enabled
  * dashboard_auto_refresh_restriction
  * dashboard_auto_refresh_minimum_interval
  * extension_framework_enabled
  * extension_load_url_enabled
  * instance_config
  * managed_certificate_uri
  * marketplace_auto_install_enabled
  * marketplace_automation
  * marketplace_terms_accepted
  * marketplace_enabled
  * marketplace_site
  * onboarding_enabled
  * privatelabel_configuration
  * timezone
  * host_url
  * email_domain_allowlist
  * embed_cookieless_v2
  * embed_enabled
  * embed_config


## Request
GET /setting 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields
## Response
### 200: Looker Settings
Datatype
Description
(object)
instance_config
_lock_
Externally available instance configuration information
Expand InstanceConfig definition... 
feature_flags
_lock_
object 
Feature flags enabled on the instance
license_features
_lock_
object 
License features enabled on the instance
extension_framework_enabled
boolean 
Toggle extension framework on or off
extension_load_url_enabled
boolean 
(DEPRECATED) Toggle extension load url on or off. Do not use. This is temporary setting that will eventually become a noop and subsequently deleted.
marketplace_auto_install_enabled
boolean 
(DEPRECATED) Toggle marketplace auto install on or off. Deprecated - do not use. Auto install can now be enabled via marketplace automation settings
marketplace_automation
_lock_
MarketplaceAutomation
Marketplace automation settings.
Expand MarketplaceAutomation definition... 
install_enabled
boolean 
Whether marketplace auto installation is enabled
update_looker_enabled
boolean 
Whether marketplace auto update is enabled for looker extensions
update_third_party_enabled
boolean 
Whether marketplace auto update is enabled for third party extensions
marketplace_enabled
boolean 
Toggle marketplace on or off
marketplace_site
_lock_
string 
Location of Looker marketplace CDN
marketplace_terms_accepted
boolean 
Accept marketplace terms by setting this value to true, or get the current status. Marketplace terms CANNOT be declined once accepted. Accepting marketplace terms automatically enables the marketplace. The marketplace can still be disabled after it has been enabled.
privatelabel_configuration
_lock_
PrivatelabelConfiguration
Private label configuration
Expand PrivatelabelConfiguration definition... 
logo_file
string 
Customer logo image. Expected base64 encoded data (write-only)
logo_url
_lock_
string 
Logo image url (read-only)
favicon_file
string 
Custom favicon image. Expected base64 encoded data (write-only)
favicon_url
_lock_
string 
Favicon image url (read-only)
default_title
string 
Default page title
show_help_menu
boolean 
Boolean to toggle showing help menus
show_docs
boolean 
Boolean to toggle showing docs
show_email_sub_options
boolean 
Boolean to toggle showing email subscription options.
allow_looker_mentions
boolean 
Boolean to toggle mentions of Looker in emails
allow_looker_links
boolean 
Boolean to toggle links to Looker in emails
custom_welcome_email_advanced
boolean 
Allow subject line and email heading customization in customized emails”
setup_mentions
boolean 
Remove the word Looker from appearing in the account setup page
alerts_logo
boolean 
Remove Looker logo from Alerts
alerts_links
boolean 
Remove Looker links from Alerts
folders_mentions
boolean 
Remove Looker mentions in home folder page when you don’t have any items saved
custom_welcome_email
_lock_
Custom welcome email configuration
Expand CustomWelcomeEmail definition... 
enabled
boolean 
If true, custom email content will replace the default body of welcome emails
content
string 
The HTML to use as custom content for welcome emails. Script elements and other potentially dangerous markup will be removed.
subject
string 
The text to appear in the email subject line. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.
header
string 
The text to appear in the header line of the email body. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.
onboarding_enabled
boolean 
Toggle onboarding on or off
timezone
string 
Change instance-wide default timezone
allow_user_timezones
boolean 
Toggle user-specific timezones on or off
data_connector_default_enabled
boolean 
Toggle default future connectors on or off
host_url
string 
Change the base portion of your Looker instance URL setting
override_warnings
boolean 
(Write-Only) If warnings are preventing a host URL change, this parameter allows for overriding warnings to force update the setting. Does not directly change any Looker settings.
email_domain_allowlist
string[] 
embed_cookieless_v2
boolean 
(DEPRECATED) Use embed_config.embed_cookieless_v2 instead. If embed_config.embed_cookieless_v2 is specified, it overrides this value.
embed_enabled
_lock_
boolean 
True if embedding is enabled https://cloud.google.com/looker/docs/r/looker-core-feature-embed, false otherwise
embed_config
_lock_
Embed configuration. Requires embedding to be enabled https://cloud.google.com/looker/docs/r/looker-core-feature-embed
Expand EmbedConfig definition... 
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
login_notification_enabled
_lock_
boolean 
Login notification enabled
login_notification_text
_lock_
string 
Login notification text
dashboard_auto_refresh_restriction
boolean 
Toggle Dashboard Auto Refresh restriction
dashboard_auto_refresh_minimum_interval
string 
Minimum time interval for dashboard element automatic refresh. Examples: (30 seconds, 1 minute)
managed_certificate_uri
string[] 
### 400: Bad Request
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
### 404: Not Found
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
### 422: Validation Error
Datatype
Description
(object)
message
_lock_
string 
Error details
errors
ValidationErrorDetail[] 
Expand ValidationErrorDetail definition... 
field
_lock_
string 
Field with error
code
_lock_
string 
Error code
message
_lock_
string 
Error info message
documentation_url
_lock_
string 
Documentation link
documentation_url
_lock_
string 
Documentation link
### 429: Too Many Requests
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
## Examples
### Python
https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/simple_sample.py   
---  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


