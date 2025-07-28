# Looker Marketplace Overview  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/marketplace-overview

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Blocks
    * What are blocks?
  * Visualizations
    * What are visualizations?
    * Using visualizations
  * Applications
    * What are applications?
    * Using Applications
  * Actions
    * What are actions?




Was this helpful?
Send feedback 
#  Looker Marketplace Overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Blocks
    * What are blocks?
  * Visualizations
    * What are visualizations?
    * Using visualizations
  * Applications
    * What are applications?
    * Using Applications
  * Actions
    * What are actions?


The Looker Marketplace is a central location for finding, deploying, and managing Looker models (blocks), visualizations, applications, and actions.
This page summarizes the Looker Marketplace development process and provides an overview of the different types of Marketplace content that you can create.
## Overview
Developers can contribute to the Marketplace by creating content such as blocks, visualizations, and applications. To get started, follow these high-level steps:
  1. Create your Marketplace content. Use one of the following guides to help you get started, depending on which type of content you'd like to build: 
     * Developing a custom block for the Looker Marketplace
     * Developing a visualization for the Looker Marketplace
     * Building a Looker application with the Extension Framework
     * Building a custom action
  2. Host the code for your Marketplace content on a public Git repository. (For actions, instead submit a pull request to Looker's action repository.)
  3. Submit your Marketplace content for review. See Submitting content to the Looker Marketplace for more details.


The following sections summarize the different types of Marketplace content that you can create.
## Blocks
### What are blocks?
Looker Blocks are pre-built pieces of LookML that Looker customers can use as a starting point for quick and flexible data modeling.
You can create a block that models a common third-party dataset, such as Google Analytics 360, or models a common analytical pattern, such as Retail Analytics.
### Using blocks
Blocks are designed to be plug-and-play, as long as you have the appropriate dataset in an existing Looker connection. You can install a block from the Marketplace, customize the LookML, and begin exploring.
To develop a block for submission to the Marketplace, create a new LookML project in your Looker instance and back up the LookML in a public GitHub repository. See Developing a custom block for the Looker Marketplace for detailed instructions and guidelines.
### Examples
Most blocks on the Looker Marketplace Directory can be one-click installed onto your Looker instance. For examples, see:
  * Google Analytics 360 block
  * Retail Analytics block


### Getting Started
Developing a LookML block 
## Visualizations
### What are visualizations?
In addition to Looker's default visualization library, you can create custom visualization types in JavaScript. using the Looker Visualization API, the Looker visualization testbed, or your own environment.
### Using visualizations
Visualizations are designed to be plug-and-play. You can install a visualization from the Marketplace and immediately select the new visualization type when exploring, building a new dashboard, and editing a dashboard.
To develop a visualization for submission to the Marketplace, start by using the Looker Visualization API or your own Javascript environment. See Developing a visualization for the Looker Marketplace for detailed instructions and guidelines.
### Examples
Most visualizations on the Looker Marketplace Directory can be one-click installed onto your Looker instance. For examples, see:
  * Aster Plot visualization
  * Force-Directed Graph
  * Gauge visualization


### Getting started
Developing a visualization 
## Applications
### What are applications?
Looker Applications allow you to provide highly customized and integrated experiences to your Looker instance's users.
A dedicated Looker page becomes your canvas, with a wide array of tools at your disposal, including the ability to:
  * run Javascript code
  * access the Looker APIs through a pre-authenticated client
  * leverage Looker Components for seamless UI
  * make HTTP calls from the client or through a convenient server proxy
  * authenticate with third-party services via OAuth


### Using Applications
Applications are designed to be plug-and-play. You can install an application from the Marketplace and immediately begin using it.
To develop an application for submission to the marketplace, the first step is to is author a Javascript-based client-side application that uses the APIs exposed by Looker's Extension Framework. Looker's `create-looker-extension` command line tool can get you started with a template codebase, including the necessary build tooling to bundle your application code via webpack. See the Building a Looker extension page for detailed instructions and guidelines.
### Examples
Several Looker-published applications can be one-click installed into your Looker instance from the Looker Marketplace. For examples, see:
  * API Explorer application
  * Data Dictionary application


### Getting started
Building a Looker extension 
## Actions
### What are actions?
Actions, also called integrations, deliver Looker data to third-party services. Expand on Looker's action destination library by creating an action to a new destination, such as Airtable or Azure Storage.
### Using actions
Looker customers enable actions from the Admin settings - Actions page in their Looker instance, rather than by installing actions from the Marketplace.
To develop a new action, write a Javascript method that sends either one cell of a Looker data table, one Looker query, or one Looker dashboard to the destination. See the Building a custom action page for detailed instructions and guidelines.
### Examples
To try out an action, enable an action from the Admin settings - Actions page in your Looker instance. Then, select the action when sending or scheduling data. For examples, see:
  * Airtable action
  * Azure Storage action


### Getting Started
Building a custom action 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-24 UTC.


