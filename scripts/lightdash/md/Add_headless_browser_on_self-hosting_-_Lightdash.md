# Add headless browser on self-hosting - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/enable-headless-browser-for-lightdash

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Add headless browser on self-hosting
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
  * Configure headless browser on lightdash


Images can be requested on `Slack unfurl` or using our `Scheduler` If you are running Lightdash on self-hosting, you will also have to run this headless browser on your infrastructure.
##  How it works
When Lightdash needs to generate an image, it will open a new socket connection to the headless browser on `ws://HEADLESS_BROWSER_HOST:HEADLESS_BROWSER_PORT` Then using `playwright` we will browse the chart/dashboard on lightdash on `SITE_URL` We load the chart/dashboard on the browser and then a screenshot when it finishes loading Then we store that image in S3 (if enabled) or locally and then return the image URL. If the image was requested by Slack unfurl, we will unfurl the image using the Slack API. If the image was requested by Scheduler, we will send the image to the destination(s) (email or Slack)
##  Configure headless browser on lightdash
In order to make this work, there are a few key ENV variables that need to be configured correctly.
  * `HEADLESS_BROWSER_HOST` : If you’re running docker, this could be `headless-browser`, or `localhost` if you’re running it locally (or with network:host)
  * `HEADLESS_BROWSER_PORT` : Optional port for headless browser, defaults to 3001
  * `SITE_URL` : The URL for your Lightdash instance.


This SITE_URL variable (eg: https://eu1.lightdash.cloud) needs to be accessible from this headless browser service, either by a local connection, or via Internet. Otherwise it will not be able to open a page and generate the image.This means that if you are using docker locally, make sure the headless browser pod can reach the lightdash pod. Or follow the docker documentation to enable `network:host`
Standalone scheduler workerScheduler
Assistant
Responses are generated using AI and may contain mistakes.


