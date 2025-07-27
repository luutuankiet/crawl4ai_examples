# Configure a Github integration for self-hosted Lightdash - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/configure-github-for-lightdash

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure a Github integration for self-hosted Lightdash
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
  * Create a new Github app
  * Generate Certificate and Secret
  * Adding credentials to your local environment


In this guide we will show you how you can enable the Github integration on your on self-hosted Lightdash server.
###  Create a new Github app
Go to app settings in Github, either organization or account developer settings and click `New Github App` **Settings:**
  1. Set the app name: must be unique across Github
  2. Add a description
  3. Homepage URL: e.g. `https://lightdash.com`
  4. Callback URL: `https://<your-domain>/api/v1/github/oauth/callback`
  5. Enable `Expire user authorization tokens`
  6. Enable `Request user authorization (OAuth) during installation`
  7. Deactivate webhooks

**Repository Permissions:**
  * Checks: `Read and write`
  * Contents: `Read and write`
  * Pull requests: `Read and write`
  * Workflows (optional): `Read and write`

**Account Permissions:** None **Where can this GitHub App be installed?** Any account
###  **Generate Certificate and Secret**
After creating your Github account you will need to generate a Client Secret. Copy it and keep it safe, this will get used for the `GITHUB_CLIENT_SECRET` environment variable. And a Private Key. Convert the contents of the private key file into `base64` , this will get used for the `GITHUB_PRIVATE_KEY` environment variable.
You should save both the Client Secret and the Private Key in a safe place as you might need them at a later time.
###  Adding credentials to your local environment
Now you need to add the following environment variables to your Lightdash server.
  * `GITHUB_PRIVATE_KEY` : This is the `base64` string of the Private Key generated for your Github app
  * `GITHUB_CLIENT_SECRET` : This is the client secret generated for your Github app
  * `GITHUB_CLIENT_ID`: Copy this from your Github app settings > General
  * `GITHUB_APP_ID`: Copy this from your Github app settings > General
  * `GITHUB_APP_NAME`: This is the name you set for your app, you can find it in app settings.


Slack IntegrationUse External Database
Assistant
Responses are generated using AI and may contain mistakes.


