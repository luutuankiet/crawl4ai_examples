# Looker API versioning  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/api-versioning

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How Looker makes changes to the API
    * Breaking and additive changes to the API
  * Flags for API endpoints
  * Migrating to a new API version
    * Auditing your code




Was this helpful?
Send feedback 
#  Looker API versioning
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How Looker makes changes to the API
    * Breaking and additive changes to the API
  * Flags for API endpoints
  * Migrating to a new API version
    * Auditing your code


Most applications are written using some form of a client SDK, or possibly an API URL. The client SDK and API URLs are bound to a specific Looker API version. Your application will continue to function even as Looker makes changes to new API versions. Your application won't be affected by changes in other API versions until you choose to upgrade your client SDK (or modify the API URL) to use the new Looker API version.
## How Looker makes changes to the API
The Looker API is architected to provide stability for Looker API endpoints, and therefore stability for your applications.
As we add more features and capabilities to Looker, we also update the Looker REST API to access or manage those new features. For each Looker release, we add new API functions, parameters, and response type properties to the current version of the Looker API. In most cases, additions to the API are not breaking changes, so we can keep the existing version of the API without affecting any existing application code that is built on the API. Your existing application code may simply be unaware of new functions, parameters, or features that appear in subsequent Looker releases.
For changes to the API that would break existing application code, we bundle those breaking changes into a new API version. This means that the old API version will continue to work the same as before, while a new API version runs alongside it with the changes and updates. Multiple API versions can exist side by side in a single Looker instance so that you can choose when to upgrade to the new API version. Your existing code that was built to call the old endpoint will continue to call the old endpoint. New code should call the new version of the endpoint in the most recent API version level.
One exception to this is for critical security issues. If we discover a critical security issue related to a particular part of the API, we will do whatever is necessary to mitigate that security issue as soon as possible, which may include disabling the vulnerable functionality until a proper solution is available).
If we need to retire a feature, function, or property to make way for a better implementation or solution, we normally leave the current API as it is, but mark the associated API endpoints as "deprecated" to indicate that you should move away from the endpoint in your application code.
### Breaking and additive changes to the API
A _breaking_ change is something that deletes or renames an existing artifact of an API endpoint. It might include:
  * Changing or deleting a parameter name or type
  * Adding a new required parameter
  * Changing the base URL
  * Changing or deleting an existing property in a response


An _additive_ change, on the other hand, may be made to stable endpoints. They might include:
  * New, optional parameters
  * New properties in responses (we do not consider this breaking because we assume that your code will ignore unknown properties in responses, which is common practice in the REST API community)


If a stable Looker API endpoint needs a significant change to move forward with new architecture or functionality, the change is usually added to a new endpoint and bundled into a new API version so that the existing API endpoint remains unchanged.
## Flags for API endpoints
Most API endpoints are considered _stable_ , meaning they are not expected to change. Looker will not release breaking changes to stable endpoints except in extreme cases, such as to fix a security problem.
Other API endpoints may be flagged as _beta_ or _deprecated_ :
  * **Beta endpoints** are in active development and may change in the future. They are not protected from breaking changes. When using beta endpoints, consider whether a change to the Looker API would be particularly disruptive to your app or development cycle. Please read Looker's release notes if you plan to use a beta endpoint so that you will be aware of any changes.
  * **Deprecated endpoints** are endpoints that are still supported and can still be used at the moment, but will be deleted in a future release. Old code that uses a deprecated endpoint should be updated to stop using the deprecated endpoint. When a future release of Looker removes support for that endpoint, any code that is still using it will break. In most cases, a deprecated endpoint will be replaced by improved functionality. If you find that your application is using a deprecated function or property, it's a good idea to refactor your code to replace the deprecated element as soon as you can.


Beta and deprecated endpoints are marked as such in the API Explorer and in the 4.0 API Reference. Endpoints that aren't marked are considered stable.
## Migrating to a new API version
When you choose to upgrade your client SDK or API URL to a new API version, you will need to review your application code to see if you're relying on something that has changed with the new API version. Be sure to do the following:
  1. Search your application code for the updated function, value, and property names.
  2. Verify that your application code supports any changes in types (such as integer to string).
  3. Audit your code (see the Auditing your code section).


### Auditing your code
For some languages, breaking changes in the API can be discovered at build time as compile errors:
  * If your application is written in a compiled, strongly-typed language, structural changes to parameter or response types in a new API version that are at odds with your existing code should be readily apparent thanks to compile type checking and compiler error messages.
  * If your application is written in a loosely-typed dynamic language (such as JavaScript, Ruby, and Python), it may be harder to locate the parts of your application that will be affected by breaking changes in a new API version. These types of languages might require runtime unit tests to find any issues related to changes in types.


In all cases, the best practice is to have unit tests that exercise your application code, including calls to the Looker API (not mocked calls).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


