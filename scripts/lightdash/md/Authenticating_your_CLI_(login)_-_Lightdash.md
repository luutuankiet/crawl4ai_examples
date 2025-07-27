# Authenticating your CLI (login) - Lightdash

**Source:** https://docs.lightdash.com/guides/cli/cli-authentication

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
CLI quickstart
Authenticating your CLI (login)
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
  * Set active project
  * Now that you’ve logged in, you’re ready to use the CLI


##  Login
1. You can login on the CLI from your browser using OAuth2.
To log in to your Lightdash instance using OAuth2, run the following command:
Copy
Ask AI
```
lightdash login https://{{ lightdash_domain }} --oauth

```

where `{{ lightdash_domain }}` is the address for your running Lightdash instance. For example Lightdash cloud users in the US would type `lightdash login https://app.lightdash.cloud` if you’re in Europe you’d type`lightdash login https://eu1.lightdash.cloud`.This will open a new tab in your default browser. Log in to your Lightdash account (if you’re not already logged in), then authorize the lightdash-cli client.Once authorized, you’ll be logged in and ready to use the CLI.
2. If you use your email + password in the browser, login with your email and password.
To login to your Lightdash instance run the following command and provide your login email and password:
Copy
Ask AI
```
lightdash login https://{{ lightdash_domain }}

```

where `{{ lightdash_domain }}` is the address for your running Lightdash instance. For example Lightdash cloud users in the US would type `lightdash login https://app.lightdash.cloud` if you’re in Europe you’d type`lightdash login https://eu1.lightdash.cloud`.
3. If you use single sign-on (SSO) in the browser, login with a personal access token.
First, you’ll need to create a new personal access token in the UI by going to Settings > Personal Access Tokens. You can’t use an existing personal access token! You have to create a new one just for yourself. Then, run the following command in your project:
Copy
Ask AI
```
lightdash login https://{{ lightdash_domain }} --token

```

where `https://my-lightdash.domain.com` is the address for your running Lightdash instance. For example Lightdash cloud users in the US would type `lightdash login https://app.lightdash.cloud` if you’re in Europe you’d type`lightdash login https://eu1.lightdash.cloud`.
4. If you're running in a CI/CD pipeline, login with environment variables
You can use the following environment variables to authenticate yourself on each command:
  * **LIGHTDASH_API_KEY** a personal access token you can generate in the app under the user settings
  * **LIGHTDASH_URL** address for your running Lightdash instance
  * **LIGHTDASH_PROXY_AUTHORIZATION** if your Lightdash instance is behind a proxy like Cloud IAP you can set here `Proxy-Authentication` header value

Example:
Copy
Ask AI
```
LIGHTDASH_API_KEY=946fedb74003405646867dcacf1ad345 LIGHTDASH_URL="https://{{ lightdash_domain }}" LIGHTDASH_PROXY_AUTHORIZATION="Bearer <JWT_TOKEN>" lightdash preview

```

Where `{{ lightdash_domain }}` is your domain. For Lightdash Cloud users use `https://app.lightdash.cloud`
##  Set active project
When you login you’ll be asked to set an active project. Your active project is just the one that you’re working on/developing in. Your organization might just have one project, so that makes your decision easy! You can change your active project by running:
Copy
Ask AI
```
lightdash config set-project

```

Or you can use the `LIGHTDASH_PROJECT` environment variable to indicate what project UUID the command should use. Example:
Copy
Ask AI
```
LIGHTDASH_PROJECT="3675b69e-8324-4110-bdca-059031aa8da3" lightdash deploy

```

##  Now that you’ve logged in, you’re ready to use the CLI
You can see all of the actions available on the CLI by typing this in your terminal:
Copy
Ask AI
```
lightdash

```

Some of our favourites are:
  * Automatically generating .yml for your dbt models using lightdash generate
  * Testing your changes with developer previews using lightdash preview
  * Deploying your changes to production using lightdash deploy


How to install the Lightdash CLIUpgrading your Lightdash CLI
Assistant
Responses are generated using AI and may contain mistakes.


