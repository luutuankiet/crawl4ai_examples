# Looker API overview  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/api-overview

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  Looker API overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Looker's API provides access to the vast majority of Looker functionality over a convenient JSON-oriented REST API. It includes a diversity of endpoints, from simple running of queries in a variety of formats, to managing users, content, schedules, instance configurations, and more.
The API can be used as a part of many use cases. Some examples include internal operational tools, highly custom customer-facing embedded analytics, mobile app integrations, specialized Looker administrative tools, and more.
## Using the API
You can use the API either directly via HTTPS requests or through the convenience of a language-specific SDK.
In addition, the API provides for a few authentication modes, which may help inform your architectural choices. Backend services can authenticate with API credentials, can use the API with a service account, and can conveniently impersonate API requests on behalf of end users. Alternatively, frontend clients can leverage OAuth authentication (Authorization Code PKCE), without the need to handle sensitive client secrets.
Here is a sample of the most common ways that the API is used end-to-end:
  * Backend only 
    * Authenticate with API credentials: Common for command-line scripts, administrative tasks, or sandbox environments
  * Frontend and backend 
    * Provide an application server with single service account and credentials, and make API calls through the service account
    * Provide an application server with single service account and credentials, but use Looker's `sudo` or `login_as_user` functionality to make calls on behalf of the end user
    * Authenticate with an application server, use sudo/login_as_user, send the resulting token back to the user, and make frontend API calls with Cross-Origin Resource Sharing (CORS)
  * Frontend only 
    * Authenticate with OAuth, and make frontend API calls with CORS
    * Implicit authentication and invocation from within Looker extensions


## Try it out
Want to see the API in action before writing any code? These demos can help:
  * Atom Fashion is a demo data-driven web app (requires Google account to log in).
  * Explore API endpoints and make sample API calls against your Looker instance using the API Explorer.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


