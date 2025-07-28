# Embed cookieless authentication deprecation  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/embed-cookieless-auth-deprecation

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Why does this matter?
  * What do I need to do?
  * Which solution is better for me?




Was this helpful?
Send feedback 
#  Embed cookieless authentication deprecation
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Why does this matter?
  * What do I need to do?
  * Which solution is better for me?


Starting in Looker 24.14, scheduled to release on August 7, 2024, to address security considerations, the experimental Labs feature **Embed Cookieless Authentication** will be deprecated in favor of the cookieless embedding feature.
If you have enabled the **Embed Cookieless Authentication** Labs feature, and you don't implement one of the following solutions for ensuring that your embed use case continues to work for all your embed users, when your instance is upgraded to Looker 24.14, all embedded iframes will automatically default to using cookies for authentication.
## Why does this matter?
Looker uses cookies for user authentication. If the Looker instance is on a different domain than the embedded iframe, the cookies are considered third-party cookies. Some browsers default to a cookie policy that blocks third-party cookies. When third-party cookies are blocked, it's not possible to authenticate the embedded iframe across different domains.
Matching the domains of the Looker instance and the embedded iframe causes the cookies to become first-party cookies, which are not blocked. For example, if you want to embed information on `https://mycompany.com`, Looker would have to share the same domain, such as `https://analytics.mycompany.com`.
## What do I need to do?
Implement one of the following solutions to ensure that your embed use case continues to work for all your embed users:
  * **Set up a custom domain for your Looker instance**.
You can set up a custom domain for your Looker instance that shares the same domain as your embed application. Configuring a custom domain causes the cookies that Looker uses to become first-party cookies, since the Looker domain matches the embed application domain. For example, if you are embedding on `analytics.mycompany.com`, you can set up a custom domain that changes your Looker URL from `mycompany.cloud.looker.com` to `looker.mycompany.com`.
To set up a custom domain on a Looker (original) instance that is hosted by Looker, contact Looker Support.
To set up a custom domain on a Looker (Google Cloud core) instance, follow the instructions on the Set up a custom domain for a Looker (Google Cloud core) instance documentation page.
  * **Switch to usingcookieless embedding**.
Cookieless embedding uses a token-based approach for embed user authentication that bypasses Looker's dependency on browser cookies. This feature is generally available, but it requires embed application code changes to implement. For more information, see the Cookieless embedding documentation page.


If you have any questions or need assistance, contact Looker Support.
## Which solution is better for me?
For most embed use cases, setting up a custom domain is a simpler way to address third-party cookies. Cookieless embedding requires embed application code changes to implement.
One use case for cookieless embedding is for customers who host their embed application on different domains for each of their customers. In this case, implementing cookieless embedding prevents the need to set up and maintain dozens or even hundreds of separate custom domains to allow third-party cookies.
If you have any questions or need assistance, contact Looker Support.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


