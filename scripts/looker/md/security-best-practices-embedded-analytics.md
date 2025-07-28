# Security best practices for embedded analytics  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/security-best-practices-embedded-analytics

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Public embedding
  * Private embedding
  * Signed embedding
    * Signed embed parameters
    * Managing signed embed access
  * Looker API
    * Managing embed access using the API
  * Embedded Javascript events
  * Customer-hosted deployments




Was this helpful?
Send feedback 
#  Security best practices for embedded analytics
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Public embedding
  * Private embedding
  * Signed embedding
    * Signed embed parameters
    * Managing signed embed access
  * Looker API
    * Managing embed access using the API
  * Embedded Javascript events
  * Customer-hosted deployments


With Looker embedded analytics, you can empower your users and customers to explore data embedded into an iframe in any HTML-formatted webpage, portal, or application. The iframe executes the whole Looker application, requesting only the data necessary to display your query. By design, an iframe is not allowed to read or write data from your external website or application.
Embedding data may sometimes present privacy or security concerns. To mitigate these concerns, we recommend that Looker admins follow these best practices:
  * If you are embedding Looker content to customers, set up customer content on a separate Looker instance from the instance you use for internal analytics.
  * Only connect data to the Looker embedded instance that _should_ be accessible by embed users, who may be the public.
  * Protect the random tokens within public embed URLs as if they were user credentials, and disable public URLs if they're not used.
  * An assigned `external_user_id` value must be unique for each given set of permissions, user attributes, and models. Ensure that you are not using the same `external_user_id` across different embed sessions for different interactive users, and ensure that you are not using the same `external_user_id` for a single user who has different permissions, user attribute values, or model access.
  * Enable a closed system.
  * Protect the signed embed secret as if they were admin credentials to your embedded Looker instance and keep signed embedding disabled if you're not using it.
  * Use strong authentication for your Looker embedded instances (signed embedding, SAML, Google OAuth, 2FA).
  * If you are using cookieless embed, protect the session reference token so that it is only accessible in the embed application host server. The session reference token should never be exposed in the browser.
  * If you are using cookieless embed and setting the allowed embed domain when acquiring the cookieless session, never trust the origin from the embed user's browser. Always maintain a mapping of the embed user to the embed user's trusted origin in the embed application server.


Looker offers different types of embedding methods depending on the level of authentication required of users accessing your data: public, private, and signed embedding. With any of these methods, you can interact with the iframe using JavaScript.
## Public embedding
With a Look's **Public Access** option enabled, you can embed a visualization or data table into an external website using an HTML iframe tag. You can also publicly share the Look URL, or import data into Google or Excel spreadsheet applications.
The URL and the embed URL within the `iframe` tag contain a random token and cannot be guessed, but anyone with the embed URL may access the data, and no additional filtering or restrictions are applied. We recommend considering the security implications of creating and sharing a public URL for a given Look before enabling **Public URLs**.
> Public URLs and public embed URLs never expire and can't be revoked. When you share a public URL, you are sharing the _query,_ not the actual _data._
## Private embedding
If you don't want to allow public access to your Look, you can also embed a Look — or an Explore or a dashboard — privately in an iframe, so that a Looker login is required to view the content.
Authenticated users can access only the content dictated by their assigned Looker permissions. If you change their permissions in Looker, the embed URL doesn't change but what the user is allowed to see when they access the URL may change.
If user is not authenticated, you can either show an error or a login screen in the iframe. However, enabling a login screen in the iframe is not compatible with Looker's same-origin protections.
> Private embed URLs never expire and can't be revoked. However, since the link works only for someone who has access to your Looker instance and that data, sending a link should not cause a security concern.
## Signed embedding
> Please contact a Google Cloud sales specialist to update your license for this feature.
Signed embedding takes private embedding one step further. Signed embedding doesn't require users to authenticate using a Looker user account. Instead, they can be authenticated through your own application using the URL in an iframe. Authentication creates a new browser session and issues a cookie to the browser.
User permissions, identifiers, and attributes are all passed as parameters within the URL, which is signed with a secret key. Anyone with access to the secret key may create a URL to access any model that Looker instance is connected to, as any user, with any permission. See our example code to learn how to generate signed URLs.
> Clickjacking is a browser security issue that can happen when embedded code or a script executes a function without the user's knowledge or consent, such as a button that appears to do something else. Clickjacking usually requires a static URL. The URL generated for an signed embed is secret, and only the user viewing the embed should have it. Using signed embedding doesn't increase the clickjacking risk to the external website.
### Signed embed parameters
The parameters included in the iframe URL are visible to embed users but are not editable. These may include:
  * `user_attributes`: These are used to further filter data. `user_attributes` are powerful, so consider how they may apply to your Looker instance.
  * `session_length`: Keep this to the minimum necessary time.


Some parameters, such as `user_attributes`, can be hidden in the UI but would still be encoded in the embed URL. This may be undesirable if, for example, a password is a value within a user's `user_attribute`. One way to get around this is to construct a temporary group, set the password as a group-level attribute, and then pass the group ID in the embed URL. You can delete the group after the embed session to avoid an excess of lapsed groups.
The signed part of the URL contains a timestamp. Once the URL is used to sign on, that time must be +/- 5 minutes from the current time. You can specify in `session_length` how long the embed session can last from when the URL is used to log in.
### Managing signed embed access
When building the URL for your embedded content:
  * Use the lowest level of permissions necessary.
  * Only assign access to the specific models that the user should be able to access.
  * Use `group_ids` to assign a user to a group and allow the embed user to control access to their Looker folder.


## Looker API
Using Looker's API, you can enable access to embedded content using a proxy application or a reverse proxy server. In this scenario, authentication is performed using API keys, which are tied to a specific user and have the same permissions as the user that generates them. API keys are composed of a client ID and a client secret key.
### Managing embed access using the API
When enabling access to embedded content using Looker's API, we recommend:
  * Creating dedicated services accounts for programmatic API access with the minimum set of necessary privileges.
  * Protecting the client ID and client secret that make up the API key (if authenticating with an SDK).


Any user attributes set for embed users using the API but not specified in the signed embed URL are reset to their default values when the signed embed URL is next accessed.
## Embedded Javascript events
After you've set up your embed iframe — publicly, privately, with signed embedding, or through the API — you can interact with that iframe using JavaScript. To validate that the information you're working with has actually come from Looker's iframe, you can listen to the JavaScript events.
When adding domains to the allowlist, use the wildcard to allow only specific subdomains to access your JavaScript events.
If using the JavaScript `eval` function, make sure the string value in the `eval` argument is from a trustworthy source, such as the Looker server or CDN and is under HTTPS transport.
No customer data ever goes through the Looker CDNs. Only Looker web application static assets — JavaScript code, HTML pages, CSS styles — are served from CDN.
## Customer-hosted deployments
Hosting your own Looker instance may seem like the fail-safe way to lock down access to data, especially embedded content. However, if your users need to access the embed URL over the internet, there are no special advantages to hosting Looker yourself.
Customer-hosted deployments may be most appropriate when:
  * Your users are not required to to access Looker using the internet.
  * You are front-ending Looker and accessing embedded content using the API.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


