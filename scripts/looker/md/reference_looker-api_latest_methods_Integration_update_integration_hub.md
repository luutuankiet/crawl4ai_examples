# Update Integration Hub  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Integration/update_integration_hub

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Update a Integration Hub definition.




Was this helpful?
Send feedback 
#  Update Integration Hub
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Update a Integration Hub definition.


Version 4.0.25.10 (latest) 
### Update a Integration Hub definition.
This API is rate limited to prevent it from being used for SSRF attacks
## Request
PATCH /integration_hubs/{integration_hub_id} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
integration_hub_id
string 
Id of integration_hub
body
HTTP Body 
Expand HTTP Body definition... 
body
Integration Hub
Expand IntegrationHub definition... 
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
ID of the hub.
url
string 
URL of the hub.
label
_lock_
string 
Label of the hub.
official
_lock_
boolean 
Whether this hub is a first-party integration hub operated by Looker.
fetch_error_message
_lock_
string 
An error message, present if the integration hub metadata could not be fetched. If this is present, the integration hub is unusable.
authorization_token
string 
(Write-Only) An authorization key that will be sent to the integration hub on every request.
has_authorization_token
_lock_
boolean 
Whether the authorization_token is set for the hub.
legal_agreement_signed
_lock_
boolean 
Whether the legal agreement message has been signed by the user. This only matters if legal_agreement_required is true.
legal_agreement_required
_lock_
boolean 
Whether the legal terms for the integration hub are required before use.
legal_agreement_text
_lock_
string 
The legal agreement text for this integration hub.
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: Integration Hub400: Bad Request404: Not Found422: Validation Error429: Too Many Requests More
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
ID of the hub.
url
string 
URL of the hub.
label
_lock_
string 
Label of the hub.
official
_lock_
boolean 
Whether this hub is a first-party integration hub operated by Looker.
fetch_error_message
_lock_
string 
An error message, present if the integration hub metadata could not be fetched. If this is present, the integration hub is unusable.
authorization_token
string 
(Write-Only) An authorization key that will be sent to the integration hub on every request.
has_authorization_token
_lock_
boolean 
Whether the authorization_token is set for the hub.
legal_agreement_signed
_lock_
boolean 
Whether the legal agreement message has been signed by the user. This only matters if legal_agreement_required is true.
legal_agreement_required
_lock_
boolean 
Whether the legal terms for the integration hub are required before use.
legal_agreement_text
_lock_
string 
The legal agreement text for this integration hub.
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
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


