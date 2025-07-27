# Looker API authentication  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/api-auth

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Authentication with an SDK
  * Authentication without an SDK
  * API interaction with user login settings
  * Managing API credentials
  * HTTPS authentication
  * Authentication using OAuth




Was this helpful?
Send feedback 
#  Looker API authentication
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Authentication with an SDK
  * Authentication without an SDK
  * API interaction with user login settings
  * Managing API credentials
  * HTTPS authentication
  * Authentication using OAuth


To do anything with the Looker API, you'll first need to authenticate to it. The steps you'll need to take depend on whether or not you're using an SDK.
## Authentication with an SDK
This is the recommended method for API authentication:
  1. Create API credentials on the Users page in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to create the API credentials for you.
API credentials are always bound to a Looker user account. API requests execute "as" the user associated with the API credentials. Calls to the API will only return data that the user is allowed to see, and modify only what the user is allowed to modify.
  2. The API credentials that you generated include a client ID and a client secret. You'll need to provide these to the SDK. The instructions for doing so can be found in the SDK documentation.


The SDK will then take care of obtaining the necessary access tokens and inserting them into all subsequent API requests.
## Authentication without an SDK
API authentication with an SDK is the recommended method. To authenticate without an SDK:
  1. Create API credentials on the Users page in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to create the API credentials for you.
API credentials are always bound to a Looker user account. API requests execute "as" the user associated with the API credentials. Calls to the API will only return data that the user is allowed to see, and modify only what the user is allowed to modify.
  2. Obtain a short-term, OAuth 2.0 access token by calling the `login` endpoint of the API. You'll need to provide the API credentials that you generated in step 1, which include a client ID and a client secret.
  3. Place that access token into the HTTP authorization header of Looker API requests. An example Looker API request with an authorization header might look like this:
```
GET /api/4.0/user HTTP/1.1
Host: test.looker.com
Date: Wed, 19 Oct 2023 12:34:56 -0700
Authorization: token mt6Xc8jJC9GfJzKBQ5SqFZTZRVX8KY6k49TMPS8F

```



The OAuth 2.0 access token can be used on multiple API requests, until the access token expires or is invalidated by calling the `logout` endpoint. API requests that use an expired access token will fail with a `401 Authorization Required` HTTP response.
## API interaction with user login settings
Looker API authentication is completely independent of Looker user login. User authentication protocols such as one-time passcodes (OTP, 2FA) and directory authentication (LDAP, SAML, and so on) don't apply to Looker API authentication.
Because of this, deleting a user's information from a user authentication protocol does not delete their API credentials. Using the procedures on the Deleting Personal User Information documentation page removes all of a user's personal data from Looker, preventing them from logging in at all, including through the API.
## Managing API credentials
  * Multiple sets of API credentials can be bound to a single Looker user account.
  * API credentials can be created and deleted without affecting the state of the user account.
  * Deleting a Looker user account invalidates all API credentials bound to the user account.
  * The API client secret must be kept private. Avoid storing API client secrets in source code or other places that can be seen by a lot of people.
  * In production, avoid using API credentials bound to Looker admin accounts. Create minimal privilege user accounts specifically for API activities (often called "service accounts") and create API credentials on those accounts. Grant only the permissions needed for the intended API activities.


## HTTPS authentication
Even if you're using a client SDK to take care of the authentication details for you, you may still be curious about how Looker API authentication works. For low-level details about authentication, see How to Authenticate to the Looker API on GitHub.
## Authentication using OAuth
Looker can use the Cross-Origin Resource Sharing (CORS) protocol to let web applications make calls to the Looker API from outside a Looker instance's domain. See the Looker API authentication using OAuth documentation page for information about configuring CORS authentication.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


