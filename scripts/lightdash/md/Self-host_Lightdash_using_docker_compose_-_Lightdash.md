# Self-host Lightdash using docker compose - Lightdash

**Source:** https://docs.lightdash.com/self-host/self-host-lightdash-docker-compose

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Self-hosting and deployment
Self-host Lightdash using docker compose
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
  * Prerequisites
  * 1. Clone the Lightdash repository
  * 2. Update your ENV config
  * 3. Create containers


This guide will give you a minimal Lightdash instance running on your local machine. It will not be accessible from the internet, but it will be accessible from your local machine. This is a great way to get started with Lightdash for a proof-of-concept without needing access to kubernetes.
##  Prerequisites


##  1. Clone the Lightdash repository
Clone the Lightdash code to your local machine. This will create a new directory called `./lightdash` (the Lightdash directory).
Copy
Ask AI
```
# Clone the Lightdash repo
git clone https://github.com/lightdash/lightdash
cd lightdash

```

##  2. Update your ENV config
Edit all the ENV variables in `.env` to match your setup, eg:
Copy
Ask AI
```
PGHOST=db
PGPORT=5432
PGUSER=pg_user *OR* machine username if no prior postgres set up
PGPASSWORD=pg_password *OR* blank if no prior postgres set up
PGDATABASE=postgres
DBT_DEMO_DIR=/*path*/*to*/lightdash/project/examples/full-jaffle-shop-demo

```

##  3. Create containers
You must set the following two environment variables:
  * `PGPASSWORD` is the password used for the internal postgres database
  * `LIGHTDASH_SECRET` is the secret used to encrypt data at rest in the database. If you lose this secret, you will not be able to access your data in Lightdash.


Copy
Ask AI
```
export LIGHTDASH_SECRET="not very secret"
export PGPASSWORD="password"
docker compose -f docker-compose.yml --env-file .env up --detach --remove-orphans

```

If you have a Windows machine and get the error **Error response from daemon: i/o timeout**. Go to **Docker > Settings > General** and enable the option **Expose daemon on tcp://localhost:2375 without TLS**
Lightdash Cloud vs. Self-HostedRestack
Assistant
Responses are generated using AI and may contain mistakes.


