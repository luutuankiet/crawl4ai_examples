# Secure Lightdash with HTTPS - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/secure-lightdash-with-https

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Secure Lightdash with HTTPS
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
  * Configuration options for HTTPS


##  Configuration options for HTTPS
Copy
Ask AI
```
# values.yaml
configMap:
  # Ensures all Lightdash links use https
  SITE_URL: https://lightdash.mycompany.com
  # Only allow cookies to be sent over HTTPS
  SECURE_COOKIES: 'true'
  # (optional) allow http traffic behind a https enabled proxy
  TRUST_PROXY: 'true'
# Depending on your ingress implemantation you may need to set the following
service:
  type: NodePort
# Example ingress controller configuration
ingress:
  enabled: true
  annotations: {}
  hosts:
host: lightdash.mycompany.com
      paths:
path: /*
          pathType: ImplementationSpecific

hosts:
lightdash.mycompany.com
      secretName: lightdash-tls

```

Resource recommendationsSSO and auth
Assistant
Responses are generated using AI and may contain mistakes.


