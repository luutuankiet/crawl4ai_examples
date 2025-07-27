# Configure Lightdash to use an external database - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/configure-lightdash-to-use-an-external-database

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure Lightdash to use an external database
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
  * Configuration options for external database
  * Required pg extensions for external database


Lightdash requires a **PostgreSQL** database (version 12 or greater).
In production, we recommend using a managed database service (depending on your cloud provider). This ensures that your database is highly available and secure. You can also use a self-hosted database, but you will need to manage the database yourself. The following configuration shows an example of how to configure Lightdash to use an external database. You can use this as a starting point for your own configuration.
##  Configuration options for external database
Copy
Ask AI
```
# values.yaml
# Disable the internal database
postgresql:
  enabled: false
# Configure Lightdash to use an external database
externalDatabase:
  host: lightdash-db.mycompany.com
  port: 5432
  user: lightdash
  password: lightdash
  database: lightdash

```

Optionally you can pass any of the PostgreSQL Environment Variables to the `configMap`
##  Required pg extensions for external database
Lightdash requires the following extensions to be installed on the database:
  * `uuid-ossp` - used for generating unique IDs


##  Migrations
Migrations are ran automatically on starting the Lightdash server or workers. When upgrading Lightdash, migrations will be ran automatically. If migrations fail due to a pg_lock error, check for a table called`knex_migrations_lock` to manually release the lock.
Github IntegrationExternal storage
Assistant
Responses are generated using AI and may contain mistakes.


