# Configure SMTP for Lightdash email notifications - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/configure-smtp-for-lightdash-email-notifications

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure SMTP for Lightdash email notifications
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


This is a reference to all the SMTP environment variables that can be used to configure a Lightdash email client. Variable | Description | Required? | Default  
---|---|---|---  
EMAIL_SMTP_HOST | Hostname of email server  
EMAIL_SMTP_PORT | Port of email server | 587  
EMAIL_SMTP_SECURE | Secure connection | true  
EMAIL_SMTP_USER | Auth user  
EMAIL_SMTP_PASSWORD | Auth password | [1]  
EMAIL_SMTP_ACCESS_TOKEN | Auth access token for Oauth2 authentication | [1]  
EMAIL_SMTP_ALLOW_INVALID_CERT | Allow connection to TLS server with self-signed or invalid TLS certificate | false  
EMAIL_SMTP_SENDER_EMAIL | The email address that sends emails  
EMAIL_SMTP_SENDER_NAME | The name of the email address that sends emails | Lightdash  
[1] `EMAIL_SMTP_PASSWORD` or `EMAIL_SMTP_ACCESS_TOKEN` needs to be provided
Prometheus metricsStandalone scheduler worker
Assistant
Responses are generated using AI and may contain mistakes.


