# Filtering a Dashboard in the URL - Lightdash

**Source:** https://docs.lightdash.com/guides/filtering-dashboard-in-url

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Guides
Filtering a Dashboard in the URL
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
    * Lightdash semantic layer
    * Adding and managing Tables
    * How to create dimensions
    * How to create metrics
    * How to join tables
    * Multiple tables from one dbt model
    * Filtering a Dashboard in the URL
    * How to set up Lightdash YAML validation for VS Code
    * Renaming models, metrics, and dimensions
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Example of dashboard URL Filtering
  * Setting up dashboard URL filtering


In this guide you’ll learn how to format a dashboard URL to apply dynamic values to saved filters on that dashbaord. You can even set up a dimension so when you click on it you are sent to a dashboard that gets filtered based on the dimension you clicked! For example, you might have a sales dashbaord that shows your most profitable Partners, then use a URL so that when you click on a specific partner name it brings you to a new dashboard that is filtered to show KPIs filtered to that partner.
##  Example of dashboard URL Filtering
Here’s a quick walk through video that shows what it looks like once it’s complete:
##  Setting up dashboard URL filtering
This is the process for setting it up:
###  Setup steps
  1. Open the dashboard you want to dynamically filter.
  2. Add a value to the filter you want to filter dynamically.
  3. Copy the URL shown after applying the filter. It should look something like the image below.


You’ll notice there’s a `?filters=` key in the URL. Everything after that is a JSON object that has been URL encoded. If you want to see the JSON you can find a URL decoder online to reformat it.
  1. Replace the filter value that you chose in step 2 with `${ value.formatted | url_encode }` to make it dynamic. In the example the value is `Plant+Paradise` (highlighted in the image).
  2. Paste that URL into the YAML file for the model you’re working in. See an example in our demo project here.


Multiple tables from one dbt modelHow to set up Lightdash YAML validation for VS Code
Assistant
Responses are generated using AI and may contain mistakes.


