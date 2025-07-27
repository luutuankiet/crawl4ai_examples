# How to install the Lightdash CLI - Lightdash

**Source:** https://docs.lightdash.com/guides/cli/how-to-install-the-lightdash-cli

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
CLI quickstart
How to install the Lightdash CLI
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
  * Once you’ve installed the CLI tool, you’ll want to authenticate it


Before installing Lightdash CLI, you need to have NodeJS/NPM installed on your machine. To check that, run the following command in your terminal:
Copy
Ask AI
```
node -v; npm -v;
# it should print something like:
# v20.8.0
# 8.15.0

```

Don't have NodeJS/NPM installed in your system?
We recommend installing NodeJS/NPM using NVM (Node Version Manager) which works for POSIX-compliant shells (sh, dash, ksh, zsh, bash on these platforms: unix, macOS, and windows WSL)Open your terminal and run the command below to install NVM (Node Version Manager) to your system.
Copy
Ask AI
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
# or
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash

```

Restart terminal and install NodeJS by running
Copy
Ask AI
```
nvm install --lts

```

Check that NodeJS is installed by running
Copy
Ask AI
```
node -v

```

Running the command above should output something like `20.8.0` which means you’ve succesfully installed NodeJS/NPM  Alternatively, you can install NodeJS/NPM via your preferred package manager.
Run the following on your terminal to install the Lightdash CLI.
Copy
Ask AI
```
npm install -g @lightdash/cli

```

If you get an `npm ERR! code EACCES` error while installing the Lightdash CLI, follow this guide to resolve it.
##  Once you’ve installed the CLI tool, you’ll want to authenticate it
Check out the guide on authenticating your CLI tool (login and setup an active project).
OverviewAuthenticating your CLI (login)
Assistant
Responses are generated using AI and may contain mistakes.


