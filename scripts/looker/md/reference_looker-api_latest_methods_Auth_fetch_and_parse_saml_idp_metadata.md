# Parse SAML IdP Url  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/fetch_and_parse_saml_idp_metadata

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Fetch the given url and parse it as a SAML IdP metadata document and return the result.




Was this helpful?
Send feedback 
#  Parse SAML IdP Url
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Fetch the given url and parse it as a SAML IdP metadata document and return the result.


Version 4.0.25.10 (latest) 
### Fetch the given url and parse it as a SAML IdP metadata document and return the result.
Note that this requires that the url be public or at least at a location where the Looker instance can fetch it without requiring any special authentication.
Calls to this endpoint may be denied by Looker (Google Cloud core).
## Request
POST /fetch_and_parse_saml_idp_metadata 
Datatype
Description
Request
HTTP Request 
body
HTTP Body 
Expand HTTP Body definition... 
body
string 
SAML IdP metadata public url
## Response
200: Parse result400: Bad Request403: Permission Denied404: Not Found429: Too Many Requests More
Datatype
Description
(object)
SamlMetadataParseResult
can
_lock_
object 
Operations the current user is able to perform on this object
idp_issuer
_lock_
string 
Identify Provider Issuer
idp_url
_lock_
string 
Identify Provider Url
idp_cert
_lock_
string 
Identify Provider Certificate
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


