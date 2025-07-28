# Looker extension framework  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/intro-to-extension-framework

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Why use the extension framework?
  * Extension framework features
  * Extension framework requirements
  * Getting started developing with the Looker extension framework




Was this helpful?
Send feedback 
#  Looker extension framework
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Why use the extension framework?
  * Extension framework features
  * Extension framework requirements
  * Getting started developing with the Looker extension framework


The Looker extension framework is a development framework that significantly reduces the effort and complexity of building custom JavaScript data applications and tools, such as:
  * Internal platform applications for your company
  * External platforms for your customers, such as customer portals for Embedded Analytics applications built with data in Looker
  * Targeted internal tools
  * Applications for embedding in external applications


Current examples of Looker extensions that are available on the Looker Marketplace include the Looker Data Dictionary and the LookML Diagram.
## Why use the extension framework?
Some parts of building web applications are easy and fun, while others are obviously more time-consuming and not exactly fun. The extension framework helps you by streamlining many of these not-so-fun tasks.
The extension framework takes care of some of the more tedious aspects of building a web application so that you can focus on starting development right away. Custom applications and tools created with the extension framework can be accessed from within Looker, allowing Looker to handle the following kinds of functions, such as:
  * Authentication — Lets you use Looker's existing authentication options for sign-in (such as password login, LDAP, SAML, and OpenID Connect).
  * Access control and permission management.
  * API access — Lets you leverage other common developer resources, such as third-party API endpoints, within Looker.


## Extension framework features
The Looker extension framework includes the following features:
  * The Looker Extension SDK, which provides functions for Looker public API access and for interacting within the Looker environment.
  * Looker components, a library of pre-built React UI components you can use in your extensions.
  * The Embed SDK, a library you can use to embed dashboards, Looks, and Explores in your extension. See the kitchen sink extension for example code. You can also use the Embed SDK to embed your extension into third-party applications. Cookies must be enabled in the browser when you're embedding Explores, Looks, or dashboards into an extension.
  * The `create-looker-extension` utility, which creates a basic extension that includes all the necessary extension files and dependencies, and you can use as a starting point to build upon.
  * Our Looker extension framework examples repo, which includes templates and sample extensions to assist you in getting started quickly.
  * The ability to access third-party API endpoints and add third-party data to your extension.
  * The ability to create full-screen extensions within Looker. Full-screen extensions can be used for internal or external platform applications.
In a full-screen extension, you can prevent a set of users from navigating to other parts of Looker from your extension by adding users to an Extensions Only user group. You can also remove the Looker navigation bar by replacing `/extensions` with `/spartan` in the extension URL.
  * The ability to configure an access key for your extension so that users must enter a key to run the extension. This is useful if you want to charge for your extension, but you should use standard Looker permissions to gate access to those who should never be able to access an extension.
  * Starting in Looker 24.0, extensions can be developed to run in a tile in dashboards. Extensions that support being run as a tile or visualization can be added while the dashboard is in edit mode or saved to a dashboard as a visualization from an Explore. Extensions can also be configured as tiles in LookML dashboards.


## Extension framework requirements
To develop using the Looker extension framework:
  * You will need LookML developer permissions to your instance.
  * Your Looker admin must enable the **Extension Framework** feature.
  * We recommend familiarity with JavaScript or TypeScript.
  * We recommend development in React, although there is an extension SDK for raw JavaScript.


In order to run inside of Looker, every extension, regardless of its function, must include the following elements inside of Looker:
  * A LookML project that meets these requirements:
    * Includes a model file
    * Includes a project manifest file
    * Is connected to a Git repository
  * The LookML model file needs a `connection` parameter that points to a valid database connection on your instance.
  * The project manifest file requires an `application` parameter. The `application` parameter gives the extension a label, tells Looker where to find the extension JavaScript, and provides a list of entitlements for the extension. Entitlements define the Looker resources that the extension can access. The extension will not be able to access a Looker resource unless that resource is listed in the entitlements.
The following is an example project manifest file with an `application` parameter:
```
  project_name: "super_duper_extension"
  application: super_duper_extension {
    label: "Super Duper Extension"
    url: "http://localhost:8080/dist/bundle.js"
    mount_points: {
      standalone: no
    }
    entitlements: {
      local_storage: no
      navigation: no
      new_window: no
      new_window_external_urls: []
      use_form_submit: yes
      use_embeds: no
      use_downloads: no
      core_api_methods: []
      external_api_urls: []
      oauth2_urls: []
      scoped_user_attributes: []
      global_user_attributes: []
    }
  }

```

For details, see the `application` parameter documentation page.


## Getting started developing with the Looker extension framework
The easiest way to get started is to first generate a new starter extension from a template, and then customize and add functionality to that starter. This ensures that all configuration and packaging is correct, which can be difficult to do by hand. See the Building a Looker extension documentation page for instructions on how to create a new Looker project for your extension and generate a starter extension.
For more customized or advanced templates, you can browse the Looker Extension Framework Examples repository. Any extension in that repository can be cloned and repurposed as a starting point for your project.
Once you have created a simple extension and verified that everything is working, you can begin to add additional functionality and customizations:
  * You can see a list of common use cases with example code on the Looker extension framework code examples documentation page.
  * Reference the Looker UI Components site to use our components library for rapid UI and layout development.
  * The Looker Extension Kitchensink Template is an extension that provides examples of a large variety of extension functionality. You can use this template as an encyclopedia or a reference guide, but not as a starting point or an actual template. We recommend that you use our extension generator or clone one of the more simple examples to begin.
  * Examples of extensions that can be used as dashboard tiles are also available. The tile visualization extension shows how to build a custom visualization using the extension framework. The tile sdk extension shows the available API methods that are specific to tile extensions.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


