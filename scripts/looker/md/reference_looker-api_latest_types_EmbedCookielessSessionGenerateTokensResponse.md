# EmbedCookielessSessionGenerateTokensResponse  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedCookielessSessionGenerateTokensResponse

Skip to main content 



Console 
  * On this page




Send feedback 
#  EmbedCookielessSessionGenerateTokensResponse
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
navigation_token
string 
Token used to load and navigate between Looker pages.
navigation_token_ttl
integer 
Navigation token time to live in seconds.
api_token
string 
Token to used to call Looker APIs. 
api_token_ttl
integer 
Api token time to live in seconds.
session_reference_token
string 
Token referencing the embed session and is used to generate new authentication, navigation and api tokens.
session_reference_token_ttl
integer 
Session reference token time to live in seconds. Note that this is the same as actual session.
## Related Methods
  * Auth/generate_tokens_for_cookieless_session


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


