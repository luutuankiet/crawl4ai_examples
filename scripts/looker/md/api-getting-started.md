# Getting started with the Looker API  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/api-getting-started

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Looker API path and port
  * Interactive API documentation




Was this helpful?
Send feedback 
#  Getting started with the Looker API
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Looker API path and port
  * Interactive API documentation


The Looker API is a secure, "RESTful" application programming interface for managing your Looker instance and fetching data through the Looker data platform. With the Looker API, you can write applications or automation scripts to provision new Looker user accounts, run queries, schedule data deliveries, etc. Just about anything you can do in the Looker application you can do via the Looker API.
## Looker API path and port
Access your Looker instance's API through its API URL.
Your Looker admin can specify an API path by entering it in the **API Host URL** field on the **Admin > API** page in the following format:
```
https://<instance_name>.cloud.looker.com

```

Your Looker admin may also use the **API Host URL** field to assign an API path that is different from your Looker server machine name. This is common when your Looker installation is behind a load balancer, for example. In this case, contact your Looker admin for your API path.
If your Looker admin has not specified the **API Host URL** field, Looker uses the default API path. For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Service (AWS) that were created on or after 07/07/2020, the default Looker API path uses port `443`. For Looker instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port `19999`. The default API URL is in the following format:
```
https://<instance_name>.cloud.looker.com:<port>

```

## Client SDKs
You can use the Looker API with any programming language or application environment that can make HTTPS requests and process JSON responses. You can construct Looker API HTTPS requests manually by using curl (or equivalent), by using the Looker Ruby SDK, or by generating a client SDK library for your language of choice. We recommend using an SDK because it takes care of the details of authentication and HTTPS requests for you, so that you can call the Looker API using simple function calls.
You'll find SDK details on our Looker API SDKs documentation page.
## Authentication
Looker authenticates API requests by using an OAuth 2.0 bearer access token in the HTTP authorization header of the request. All Looker API endpoints require a secure HTTPS connection so that the access token will be secure in transit.
The steps for achieving this depend upon whether or not you are using an SDK. Detailed instructions can be found on our Looker API authentication documentation page.
## Interactive API documentation
For API reference documentation, the API Explorer extension is available from the Looker Marketplace. For more information, see the Using the API Explorer documentation page. If you are a Looker admin, you can also access the API Explorer by clicking the **Use API Explorer** link on Looker's **API** Admin page.
## Versioning
API stability is an important consideration when building applications. In order to help you understand which endpoints may be changed in the future, and which should remain stable, we mark certain endpoints as being in beta. For more details, see the Looker API versioning documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


