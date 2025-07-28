# Development Mode and Production Mode  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/dev-mode-prod-mode

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Development Mode
  * Switching in and out of Development Mode




Was this helpful?
Send feedback 
#  Development Mode and Production Mode
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Development Mode
  * Switching in and out of Development Mode


Your Looker data model exists in two states: Production Mode and Development Mode.
## Production Mode
Production Mode is the production version of Looker. Everyone using a Looker instance in Production Mode accesses their projects in the same state. Project files are read-only in Production Mode.
Use Production Mode when you are exploring data in Looker for your own analyses or to create saved content (Looks and dashboards) for other users.
## Development Mode
Development Mode lets you make changes to LookML files and preview how they will affect content on your instance. The changes you make to LookML files in Development Mode don't affect the production environment, until they are pushed to the production environment. (If you are familiar with Git, Development Mode uses a separate branch.)
In Development Mode, you can see the effects of your changes to project files in the Explore area of Looker. Once you're happy with your changes, you can save and merge them into production, where they then will be viewable by everyone.
To increase performance, the first time you open a LookML project in Development Mode, the Looker IDE displays the Production Mode version of the project, along with the **Create Developer Copy** button. Once you click the **Create Developer Copy** button for the project, the Looker IDE creates your personal Git branch and loads the LookML project in Development Mode for you.
## Switching in and out of Development Mode
You can switch Development Mode on and off by either of these methods:
  * Use the keyboard shortcut Control-Shift-D (Mac) or Ctrl+Shift+D (Windows).
  * Click the Looker **Main menu** icon menu and click the **Development Mode** toggle at the bottom of the menu.


While in Development Mode, you will notice the following changes:
  * The LookML and Explore sections of Looker are populated by your development version of the model.
  * There is a **Development Mode** banner at the top of the screen with the text "You are in **Development Mode**."


To exit Development Mode, you can use any of these methods:
  * Use the keyboard shortcut Ctrl-Shift-D (Windows) or Control+Shift+D (Mac).
  * Select **Exit Development Mode** in the banner.
  * Click the Looker **Main menu** icon menu, and then click the **Development Mode** toggle at the bottom of the menu.


## Version control
The Looker IDE is integrated with Git for version control. This lets you edit a private copy of the LookML files in Development Mode. Looker automatically manages the Git workflows for committing, pulling, and pushing changes. To access Git commands, you can use the Looker IDE's **Git Actions** panel or the Git button.
For details on setting up Git version control with Looker, see the Setting up and testing a Git connection documentation page. For details on using version control options in the Looker IDE, see the Using version control and deploying documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


