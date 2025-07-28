# Looker extension overview  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/extension-overview

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Using extensions




Was this helpful?
Send feedback 
#  Looker extension overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using extensions


> These extensions are different from LookML extends/extensions, the code organization syntax used when modeling data in LookML.
Looker extensions allow you to provide highly customized and integrated experiences to your Looker instance's users.
A dedicated Looker page becomes your canvas, with a wide array of tools at your disposal, including the ability to:
  * Run JavaScript code 
  * Access the Looker APIs through a pre-authenticated client
  * Leverage Looker components for seamless UI
  * Make HTTP calls from the client or through a convenient server proxy
  * Authenticate with third-party services via OAuth
  * Use additional extension framework features


Simultaneously, detailed sandboxing controls and built-in user permissioning allow your instance's administrators to be confident about what data is accessible to application developers and end users.
## Using extensions
The first step to using a Looker extension is authoring a JavaScript-based client-side application that uses the APIs that are exposed by Looker's extension framework.
The quickest way to get up and running with such an application is with our `create-looker-extension` command line tool, which will set you up with a boilerplate codebase, including the necessary build tooling to bundle your application code via webpack. The tool lets you choose between either JavaScript or TypeScript, and lets you select whether to use React.
Once your codebase is ready to go, you can load it into your Looker instance in one of three ways:
  * During development, you can use a URL to reference a locally hosted web server for quick and convenient development.
  * You can build a JS bundle and load the file through your LookML project.
  * You can deploy the JS file to a remote server or content delivery network (CDN) and then reference it by URL. This option is often the most convenient when used together with continuous deployment automation from your extension's codebase.


## Try it out
Want to see Looker extensions in action before writing any code? Several Looker-published extensions can be installed with one click into your Looker instance from the Looker Marketplace.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


