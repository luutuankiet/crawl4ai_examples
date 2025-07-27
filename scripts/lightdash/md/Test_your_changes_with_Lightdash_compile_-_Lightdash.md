# Test your changes with Lightdash compile - Lightdash

**Source:** https://docs.lightdash.com/guides/cli/how-to-compile-your-lightdash-project

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
CLI quickstart
Test your changes with Lightdash compile
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
    * How to install the Lightdash CLI
    * Authenticating your CLI (login)
    * Upgrading your Lightdash CLI
    * Autogenerate Lightdash-ready .yml files for your models
    * Sync your changes with Lightdash deploy
    * Test your changes with Lightdash compile
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
  * Step 1: add the credentials to Github secrets
  * Step 2: Create deploy.yml workflow in Github


Adding this Lightdash compile action will compile your dbt project’s .yml files and check to see if there are any errors that will break your Lightdash project. For example, a metric that references a dimension that doesn’t exist.
###  Step 1: add the credentials to Github secrets
We are going to add some secrets and config to GitHub actions, but you don’t want those to be public, so the best way to do this is to add them as secrets on Github.
If you already have a GitHub action for Lightdash, then you can use the same Lightdash secrets you created for your other action.
Go to your repo, click on `Settings` , on the left sidebar, click on `Secrets` under `Security`. Now click on the `New repository secret` We need to add the following secrets:
##### `LIGHTDASH_API_KEY`
Create a new personal access token, by going to `Settings` > `Personal Access Tokens`. This is the token you’ll put in for `LIGHTDASH_API_KEY`.
##### `LIGHTDASH_PROJECT`
The UUID for your project. For example, if your URL looks like `https://eu1.lightdash.cloud/projects/3538ab33-dc90-aabb-bc00-e50bba3a5f69/tables`, then `3538ab33-dc90-45f0-aabb-e50bba3a5f69` is your `LIGHTDASH_PROJECT`
##### `LIGHTDASH_URL`
This is either `https://eu1.lightdash.cloud` or `https://app.lightdash.cloud` for Lightdash Cloud users (check the URL to your Lightdash project). If you self-host, this should be your own custom domain.
##### `DBT_PROFILES`
Some tips for this bit:
  * You might be able to copy a bunch of the information from your local `profiles.yml` file. You can see what’s in there by typing `cat ~/.dbt/profiles.yml` in your terminal.
  * If you have a separate `prod` and `dev` profile, you probably want to use the information from your `prod` profile for your GitHub action.
  * If you want to have different connection settings depending on the user that opened the pull request (dev profiles), then check out this guide.

Find your data warehouse from the list below to get a profiles.yml file template. Fill out this template, and this is your `DBT_PROFILES` secret.
BigQuery
BigQuery OAuth:Step 1: create a secret called `GOOGLE_APPLICATION_CREDENTIALS`Add the service account credentials (the JSON file) that you want to use for your GitHub action. It should look something like this:
Copy
Ask AI
```

  "type": "service_account",
  "project_id": "jaffle_shop",
  "private_key_id": "12345",
  "private_key": "-----BEGIN PRIVATE KEY----- ... -----END PRIVATE KEY-----\n",
  "client_email": "jaffle_shop@jaffle_shop.iam.gserviceaccount.com",
  "client_id": "12345",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/jaffle_shop"


```

Step 2: create another secret called `DBT_PROFILES`Copy-paste this template into the secret and fill out the details.This will always use this project connection in your GitHub actions. If you want your preview projects to have different connection settings depending on the user that opened the pull request (dev profiles), then see what you need to add to your secret in this guide.
Copy
Ask AI
```
[my-bigquery-db]: # this is the name of your project
  target: dev
  outputs:

      type: bigquery
      method: oauth
      keyfile: keyfile.json # no need to change this! We'll automatically use the keyfile you created in the last step.
      project: [GCP project id]
      dataset: [the name of your dbt dataset]

```

More info in dbt’s profiles docs: https://docs.getdbt.com/reference/warehouse-profiles/bigquery-profile#service-account-file
Postgres
Postgres profile configuration:
Copy
Ask AI
```
company-name:
  target: dev
  outputs:

      type: postgres
      host: [hostname]
      user: [username]
      password: [password]
      port: [port]
      dbname: [database name]
      schema: [dbt schema]
      threads: [1 or more]
      keepalives_idle: 0
      connect_timeout: 10
      retries: 1

```

More info in dbt’s profiles docs: https://docs.getdbt.com/reference/warehouse-profiles/postgres-profile#profile-configurationThis will always use this project connection in your GitHub actions. If you want your preview projects to have different connection settings depending on the user that opened the pull request (dev profiles), then see what you need to add to your secret in this guide.
Redshift
Redshift password-based authentication:
Copy
Ask AI
```
company-name:
  target: dev
  outputs:

      type: redshift
      host: [hostname.region.redshift.amazonaws.com]
      user: [username]
      password: [password]
      port: 5439
      dbname: analytics
      schema: analytics
      threads: 4
      keepalives_idle: 240
      connect_timeout: 10
      ra3_node: true # enables cross-database sources

```

More info in dbt’s profiles docs: https://docs.getdbt.com/reference/warehouse-profiles/redshift-profile#password-based-authenticationThis will always use this project connection in your GitHub actions. If you want your preview projects to have different connection settings depending on the user that opened the pull request (dev profiles), then see what you need to add to your secret in this guide.
Snowflake
User / Password authentication:
Copy
Ask AI
```
my-snowflake-db:
  target: dev
  outputs:

      type: snowflake
      account: [account id]
      # User/password auth
      user: [username]
      password: [password]
      role: [user role]
      database: [database name]
      warehouse: [warehouse name]
      schema: [dbt schema]
      threads: [1 or more]
      client_session_keep_alive: False
      query_tag: [anything]

```

More info in dbt’s profiles docs: https://docs.getdbt.com/reference/warehouse-profiles/snowflake-profile#user—password-authenticationThis will always use this project connection in your GitHub actions. If you want your preview projects to have different connection settings depending on the user that opened the pull request (dev profiles), then see what you need to add to your secret in this guide.
DataBricks
Set up a DataBricks target:
Copy
Ask AI
```
your_profile_name:
  target: dev
  outputs:

      type: databricks
      catalog:

          optional catalog name,
          if you are using Unity Catalog,
          only available in dbt-databricks>=1.1.1,

      schema: [schema name]
      host: [yourorg.databrickshost.com]
      http_path: [/sql/your/http/path]
      token: [dapiXXXXXXXXXXXXXXXXXXXXXXX] # Personal Access Token (PAT)
      threads: [1 or more]

```

More info in dbt’s profiles docs: https://docs.getdbt.com/reference/warehouse-profiles/bigquery-profile#service-account-jsonThis will always use this project connection in your GitHub actions. If you want your preview projects to have different connection settings depending on the user that opened the pull request (dev profiles), then see what you need to add to your secret in this guide.
###  Step 2: Create deploy.yml workflow in Github
Go to your repo, click on `Actions` menu. If you don’t have any GitHub actions, you’ll just need to click on `Configure` If you have some GitHub actions in your repo already, click on `New workflow`, then select `setup a workflow yourself`. Now copy this file from our cli-actions repo.
If you only use a subset of your dbt models in Lightdash, then you’ll want to specify that subset in your file here.For example, to only compile models with the tag `lightdash`, you would change this line to: `run: lightdash compile --select tag:lightdash --project-dir "$PROJECT_DIR" --profiles-dir . --profile prod || lightdash compile --select tag:lightdash --project-dir "$PROJECT_DIR" --profiles-dir .`
Give it a nice name like `compile-lightdash.yml` And commit this to your repo by clicking on `Start commit`.
###  You’re done!
Everytime you open a new pull request on the repository that contains your Lightdash project, `lightdash compile` will run and check to see if any of the changes you made will break your Lightdash instance. You can see the log on the `Github actions` page
Sync your changes with Lightdash deployLightdash Validate
Assistant
Responses are generated using AI and may contain mistakes.


