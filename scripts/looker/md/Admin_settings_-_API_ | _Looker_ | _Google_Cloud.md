# Admin settings - API  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-api

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Accessing the API page
  * API Documentation




Was this helpful?
Send feedback 
#  Admin settings - API
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Accessing the API page
  * API Documentation


The **API** page in the **Platform** section of the **Admin** menu lets you manage access to the Looker API server endpoint. The page also provides a link to the API Explorer documentation.
## Accessing the API page
To access the API page:
  1. Click the Looker **Main menu** icon menu.
  2. Click **Admin** to open the **Admin** menu.
  3. Select **API**.
  4. View the **API Host URL**.


## API Host URL
The **API Host URL** is the user-facing domain name (and port) that users need to reach the Looker API server endpoint. To specify a URL, enter your API path in the **API Host URL** field in the following format:
```
https://<instance_name>.cloud.looker.com

```

For Looker installations behind a load balancer (for example, a cluster configuration) or other proxy, the user-facing domain name may be different from the actual Looker server machine name. If this is the case, the **API Host URL** must indicate the user-facing API host name and port.
If the **API Host URL** field is empty, Looker uses the default API path. For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Service (AWS) that were created on or after 07/07/2020, the default Looker API path uses port `443`. For Looker instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port `19999`. The default API URL is in the following format:
```
https://<instance_name>.cloud.looker.com:<port>

```

## API Documentation
If you have installed the API Explorer extension from the Looker Marketplace, you can click **Use API Explorer** to open the API Explorer and view current API documentation.
If you have not installed the API Explorer extension, you can click **Install API Explorer from the Marketplace** to install the API Explorer on your Looker instance.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


