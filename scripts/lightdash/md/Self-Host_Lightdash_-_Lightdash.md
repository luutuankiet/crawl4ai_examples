# Self-Host Lightdash - Lightdash

**Source:** https://docs.lightdash.com/self-host/self-host-lightdash

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Self-hosting and deployment
Self-Host Lightdash
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
  * Prerequisites for self-hosting
  * Self-host Lightdash on Kubernetes
  * 1. Add the Lightdash Helm repository
  * 2. Create a namespace for Lightdash
  * 3. Create a minimum configuration for Lightdash
  * 4. Install Lightdash with helm
  * 4 (alternative). Install Lightdash with kubectl
  * Configure Lightdash for production


Lightdash is MIT licensed and open source. You can self-host Lightdash on your own infrastructure. This guide is designed for DevOps Engineers that are familiar with Docker, Kubernetes, and are comfortable configuring environment variables, SMTP credentials, and database connections. If you’re unsure whether to self-host please read our guide on Lightdash Cloud vs. Self-Hosted.
##  Prerequisites for self-hosting
  * Access to a kubernetes cluster and kubectl installed
  * Docker


##  Self-host Lightdash on Kubernetes
The following steps will create a Lightdash instance and a postgres database to store your metadata (note: this is separate to your data warehouse with your analytics data). We recommend using kubernetes + helm but you can alternatively follow these guides for a minimum deployment without kubernetes:

To deploy Lightdash on your Kubernetes cluster you can use our community maintained Helm chart: https://github.com/lightdash/helm-charts. This will get you started with the simplest configuration possible. At the end of this guide you can find a list of configuration options to customise your Lightdash instance and make it production ready.
###  1. Add the Lightdash Helm repository
Copy
Ask AI
```
helm repo add lightdash https://lightdash.github.io/helm-charts

```

###  2. Create a namespace for Lightdash
Copy
Ask AI
```
kubectl create namespace lightdash

```

###  3. Create a minimum configuration for Lightdash
At minimum you should configure:
  * `secrets.LIGHTDASH_SECRET` - this variable is used by Lightdash to encrypt data at rest in the database. You must keep this secret. If this is lost, you will not be able to access your data in Lightdash.
  * `config.S3_REGION`, `config.S3_BUCKET`, `config.S3_ENDPOINT`, `secrets.S3_ACCESS_KEY` and `secrets.S3_SECRET_KEY` - These variables are for configuring external object storage with S3. For detailed information, refer to the external object storage documentation.
  * `service.type` - by default the Lightdash UI and API is exposed on a `ClusterIP` service. This means that it is only accessible from within the Kubernetes cluster. If you want to access Lightdash from outside the cluster, you can change this to `LoadBalancer` or `NodePort`. See the Kubernetes documentation for more information.
  * `config.SITE_URL` - if you know the URL that Lightdash will be accessible at, you can set this variable. This will ensure that all links in Lightdash are correct. If you don’t know the URL yet, you can leave this blank and update it later.

Example `values.yaml` file containing our configuration:
Copy
Ask AI
```
# values.yaml
secrets:
  LIGHTDASH_SECRET: notverysecret
  S3_ACCESS_KEY: secret # not required if using IAM role
  S3_SECRET_KEY: secret # not required if using IAM role
configMap:
  SITE_URL: https://lightdash.mycompany.com
  S3_REGION: us
  S3_BUCKET: lightdash
  S3_ENDPOINT: https://storage.provider.com
service:
  type: NodePort

```

###  4. Install Lightdash with helm
Create a new helm release called `lightdash` using the `lightdash/lightdash` helm chart. In this example we’re also using the namespace `-n lightdash`. Finally we apply our minimum configuration from above using `-f values.yaml`.
Copy
Ask AI
```
helm install lightdash lightdash/lightdash -n lightdash -f values.yaml

```

###  4 (alternative). Install Lightdash with kubectl
If you prefer not to manage your deployment with helm, you can generate the kubernetes manifests and apply them using `kubectl`.
Copy
Ask AI
```
helm template lightdash lightdash/lightdash -n lightdash -f values.yaml lightdash.yaml
kubectl apply -f lightdash.yaml

```

Visit your `SITE_URL` to access Lightdash!
##  Configure Lightdash for production
Now you have a working Lightdash instance, you can customise it to your needs. The following docs cover the most common configuration options, including those we recommend before going to production: **Required configuration**
  * Configure Lightdash to use external object storage

**Recommended for production usage**
  * Secure Lightdash with HTTPS
  * Configure Lightdash to use an external database
  * Configure SMTP for email notifications
  * Resource recommendations

**Optional configuration**
  * Use SSO login for self-hosted Lightdash
  * Enable scheduler in self-hosted Lightdash
  * Configure a Slack App for Lightdash
  * Configure environment variables for Lightdash
  * Enable headless browser for Lightdash
  * Configure Logging for Lightdash
  * Configure Prometheus metrics for Lightdash


React SDKLightdash Cloud vs. Self-Hosted
Assistant
Responses are generated using AI and may contain mistakes.


