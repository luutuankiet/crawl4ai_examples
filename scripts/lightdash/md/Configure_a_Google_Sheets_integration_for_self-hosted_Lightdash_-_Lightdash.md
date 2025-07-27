# Configure a Google Sheets integration for self-hosted Lightdash - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/google-sheets-integration

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure a Google Sheets integration for self-hosted Lightdash
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
    * Standalone scheduler worker
    * Environment variables
    * Resource recommendations
    * Secure Lightdash with HTTPS


##### Contact


On this page
  * Enable Google SSO
  * Create an API key for Google file picker


###  Enable Google SSO
To authenticate Google users, first you need to enable Google SSO on your server. If you still want to keep users to login via email/password or another SSO provider, you can set this `AUTH_GOOGLE_ENABLED` variable to `false`
###  Create an API key for Google file picker
We use Google Drive picker API to allow you to select your spreadsheet files on `Syncs` To create a Google Drive picker API you need to add a new API key in APIs and services in Google Cloud. Your Google project must have the following API’s enabled:
  * Google Drive API
  * Google Picker API
  * Google Sheets API

Save the API key in a new environment variable `GOOGLE_DRIVE_API_KEY`
Environment variablesResource recommendations
Assistant
Responses are generated using AI and may contain mistakes.


