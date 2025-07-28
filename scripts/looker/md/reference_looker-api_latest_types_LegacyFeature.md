# LegacyFeature  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LegacyFeature

Skip to main content 


  * Español – América Latina

Console 
  * On this page




Was this helpful?
Send feedback 
#  LegacyFeature
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
name
_lock_
string 
Name
description
_lock_
string 
Description
enabled_locally
boolean 
Whether this feature has been enabled by a user
enabled
_lock_
boolean 
Whether this feature is currently enabled
disallowed_as_of_version
_lock_
string 
Looker version where this feature became a legacy feature
disable_on_upgrade_to_version
_lock_
string 
Looker version where this feature will be automatically disabled
end_of_life_version
_lock_
string 
Future Looker version where this feature will be removed
documentation_url
_lock_
string 
URL for documentation about this feature
approximate_disable_date
_lock_
string 
Approximate date that this feature will be automatically disabled.
approximate_end_of_life_date
_lock_
string 
Approximate date that this feature will be removed.
has_disabled_on_upgrade
_lock_
boolean 
Whether this legacy feature may have been automatically disabled when upgrading to the current version.
## Related Methods
  * Config/update_legacy_feature


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


