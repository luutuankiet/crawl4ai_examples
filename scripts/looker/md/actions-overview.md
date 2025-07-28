# Looker Actions Overview  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/actions-overview

Skip to main content 
  * Español – América Latina

Console  Sign in




Send feedback 
#  Looker Actions Overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Looker's Action API allows developers to define Actions, or custom destinations to which Looker can send query results, dashboard results, or user interactions.
Once an Action is developed, deployed as a web service, and then added to a Looker instance, Looker users will be able to send data via that Action from within Looker.
# Using Actions
The Action API supports a number of variations in use cases:
  * Actions support various levels of user interactivity. They may be designed for ad-hoc user interactions while a user is viewing a dashboard, or they may be intended to work with recurring or triggered schedules.
  * Actions can instruct Looker to collect form data from users, in order to parameterize the handling of the data.
  * Actions can even request user authentication to a third party service via OAuth, for example to implicitly deliver data to user-specific destinations.
  * Actions can also receive query results in various formats, from data oriented formats like CSV and Excel, to various JSON formats for programmatic use cases, to visualization-oriented formats like PNG or PDF.


While these use cases are diverse, the common thread between them is that Looker users are able to instruct Looker to reach out and send data to an Action.
As a result, implementing an Action involves deploying a web service to listen for these requests.
This can be achieved by simply adding a few new endpoints to an existing application server, deploying a simple web server exclusively for this purpose, or even using a serverless environment such as Google Cloud Functions. The Action API does not require the service to maintain any state between requests, so Action servers can benefit from scalable and flexible stateless deployment configurations.
Finally, since the Action API consists of simple JSON-formatted HTTP POST requests, any server side language can be readily used to implement an action. Looker provides several examples in TypeScript, including the open-source code for our ActionHub.
# Getting started
Get started with Looker Actions
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


