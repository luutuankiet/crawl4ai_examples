# Updating Lightdash to the latest version - Lightdash

**Source:** https://docs.lightdash.com/self-host/update-lightdash

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Self-hosting and deployment
Updating Lightdash to the latest version
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


##### Contact


On this page
  * Local deployments
  * Kubernetes/helm deployments


##  Local deployments
If you’re running Lightdash on your own laptop using Docker, you just need to instruct Docker to pull the latest version of Lightdash:
Copy
Ask AI
```
docker pull lightdash/lightdash

```

Now restart Lightdash and you’ll be upgraded to the latest version.
##  Kubernetes/helm deployments
If you install Lightdash into kubernetes using our community helm chartsyou need to update your helm chart repository and upgrade your deployment.
Copy
Ask AI
```
helm repo update lightdash
helm upgrade -f values.yml lightdash lightdash/lightdash

```

Assistant
Responses are generated using AI and may contain mistakes.


