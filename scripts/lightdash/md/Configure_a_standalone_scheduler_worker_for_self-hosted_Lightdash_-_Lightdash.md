# Configure a standalone scheduler worker for self-hosted Lightdash - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/configure-standalone-scheduled-worker

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure a standalone scheduler worker for self-hosted Lightdash
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
  * 1. Disable scheduler worker in the main server
  * 2. Run standalone schedule worker
  * Example docker-compose.yml


By default, the Lightdash server runs a scheduler worker. For more advanced infrastructure, we can run the scheduler worker separately from the main server.
###  1. Disable scheduler worker in the main server
Set the following environment variable value:
Copy
Ask AI
```
SCHEDULER_ENABLED=false

```

###  2. Run standalone schedule worker
Command to start scheduler worker:
Copy
Ask AI
```
yarn workspace backend scheduler

```

Note that it expects the same environment variables as the main server.
###  Example docker-compose.yml
Copy
Ask AI
```
version: "3.8"
x-environment: commonEnvironment
PGHOST=${PGHOST:-db}
PGPORT=${PGPORT:-5432}
PGUSER=${PGUSER:-postgres}
PGPASSWORD=${PGPASSWORD}
PGDATABASE=${PGDATABASE:-postgres}
SECURE_COOKIES=${SECURE_COOKIES:-false}
TRUST_PROXY=${TRUST_PROXY:-false}
LIGHTDASH_SECRET=${LIGHTDASH_SECRET}
PORT=${PORT:-8080}
SITE_URL=${SITE_URL}
EMAIL_SMTP_HOST=${EMAIL_SMTP_HOST}
EMAIL_SMTP_PORT=${EMAIL_SMTP_PORT}
EMAIL_SMTP_SECURE=${EMAIL_SMTP_SECURE}
EMAIL_SMTP_USER=${EMAIL_SMTP_USER}
EMAIL_SMTP_PASSWORD=${EMAIL_SMTP_PASSWORD}
EMAIL_SMTP_ALLOW_INVALID_CERT=${EMAIL_SMTP_ALLOW_INVALID_CERT}
EMAIL_SMTP_SENDER_NAME=${EMAIL_SMTP_SENDER_NAME}
EMAIL_SMTP_SENDER_EMAIL=${EMAIL_SMTP_SENDER_EMAIL}
HEADLESS_BROWSER_HOST=headless-browser
HEADLESS_BROWSER_PORT=3000
services:
  headless-browser:
    image: browserless/chrome
    restart: always
    ports:
"3001:3000"

    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: ${PGPASSWORD}
      POSTGRES_USER: ${PGUSER:-postgres}
      POSTGRES_DB: ${PGDATABASE:-postgres}
    volumes:
db-data:/var/lib/postgresql/data
  lightdash:
    image: lightdash/lightdash:latest
    depends_on:

    environment:
: *commonEnvironment
       SCHEDULER_ENABLED: 'false'
    volumes:
"${DBT_PROJECT_DIR}:/usr/app/dbt"
    ports:
${PORT:-8080}:${PORT:-8080}
  scheduler:
    image: lightdash/lightdash:latest
    entrypoint: ["yarn", "workspace", "backend", "scheduler"]
    depends_on:

    environment: *commonEnvironment
volumes:
  db-data:

```

SMTP for emailsHeadless browser
Assistant
Responses are generated using AI and may contain mistakes.


