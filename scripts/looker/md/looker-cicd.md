# Creating a Looker CI/CD workflow  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-cicd

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Process overview
  * Installation and configuration
  * Usage and workflow




Was this helpful?
Send feedback 
#  Creating a Looker CI/CD workflow
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Process overview
  * Installation and configuration
  * Usage and workflow


Advanced users may want to create a CI/CD workflow in Looker so that they can manage LookML in a formal software development manner. These guides explain how to configure such a setup so that LookML may be developed, QAed, validated, and deployed.
The examples given explain a three-tier system that comprises development, QA, and production. However, you can apply the same principles to a two-tier or four-tier system.
Once enabled, all Looker developers must use the CI/CD workflow.
## Process overview
In this process, developers write LookML in their development environment, using Git pull requests. The pull requests are configured to require that code reviews are completed and that the code is evaluated with automatic processes.
When LookML is ready for testing, it is tagged in Git with a release candidate version number and promoted to QA. When QA approves, the LookML is promoted to production based on a Git tagged version number.
If needed content like Looks and User Defined Dashboards can be migrated between the CI/CD tiers through the use of Gazer.
## Installation and configuration
Find installation and configuration steps on the Looker CI/CD Installation and Configuration page.
## Usage and workflow
Find details for using this setup after installation on the Looker CI/CD Usage and Workflow page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


