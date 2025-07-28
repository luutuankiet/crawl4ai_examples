# Setting up and testing a Git connection  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/2510/setting-up-git-connection

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Integrating Looker with Git
    * Connecting to Git using HTTPS
    * Connecting to Git using SSH
    * Configuring a bare Git repository
    * Connecting a new LookML project to a non-empty Git repository
  * Testing your Git connection


You are viewing documentation for Looker 25.10. Click this link to see the most recent documentation. 


Send feedback 
#  Setting up and testing a Git connection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Integrating Looker with Git
    * Connecting to Git using HTTPS
    * Connecting to Git using SSH
    * Configuring a bare Git repository
    * Connecting a new LookML project to a non-empty Git repository
  * Testing your Git connection


When you create a new project, it exists only in Development Mode to let you develop your model in a safe environment that won't impact other users. Once you're ready to publish your project, the next step is to configure a Git connection.
Configuring a Git connection for your project lets you deploy your LookML to Production Mode, which lets other users explore your data model, build dashboards, and add LookML to your model. For a quicker setup, use a bare repository. For a more robust Git integration, create your own Git repository and follow the instructions on this page to connect it to your Looker instance.
## Integrating Looker with Git
Looker uses Git to record changes and manage file versions. Each LookML project corresponds to a Git repository. Any time a user is in Development Mode that user is on their own Git branch.
For LookML source file management, Looker can be configured with any Git provider that uses an SSH key or HTTPS for authentication. The general steps are the same no matter which platform you use. This page uses GitHub as an example for connecting a Looker project to Git once you have created a Git repository.
To access Git integration options, you must have Development Mode turned on.
You can configure Git integration using one of the following protocols:
  * **HTTPS** : HyperText Transfer Protocol Secure. With HTTPS, Looker accesses your Git repository with a username and password (or access token) that you provide, as described in Connecting to Git Using HTTPS.
  * **SSH** : Secure Shell. With SSH, Looker accesses your Git repository using a deploy key that you generate through your Git provider's website, as described in Connecting to Git Using SSH.


### Connecting to Git using HTTPS
For LookML projects that are configured with HTTPS authentication, Looker connects to your Git provider with one or more user accounts that you set up with your Git provider. Looker uses a username and password (or access token) to sign in to your Git provider and perform Git operations on behalf of your LookML developers.
If your Git account uses two-factor authentication, you can go to your Git provider and create access tokens to use instead of passwords. Go to the Setting up HTTPS git connection with 2FA Enabled Community post to see instructions for creating personal access tokens for common Git providers.
With HTTPS authentication, you can configure your LookML project to use a single Git account for the entire project, or you can configure the project to use your developers' individual Git accounts to perform their Git operations.
Note the following for GitHub HTTPS authentication:
  * GitHub doesn't accept account passwords for authenticating Git operations on github.com. See GitHub's blog post for more information. To connect a Looker project to GitHub by using HTTPS, use the developer settings in GitHub to create a personal access token.
  * Looker doesn't support GitHub's fine-grained personal access tokens. To connect your Looker project to GitHub by using HTTPS, use GitHub's **Tokens (classic)** option when you create a personal access token.


#### Single account HTTPS authentication
If you set up your LookML project with a single Git account, Looker uses that Git account to sign in to your Git provider to commit changes on behalf of the developers. Looker makes these commits by using the developer's Looker username so that you can tell which developer made each commit. You can see your project's commit history on your Git provider's interface or by selecting the **History** option from the Git menu of the Looker IDE. See Executing Git commands in Looker for more information on the Git menus in Looker.
For single account HTTPS authentication, the Git user account that you specify must have read and write access to your Git repository. Your LookML developers themselves don't need to have their own Git user accounts.
#### Multiple account HTTPS authentication with user attributes
If you set up your LookML project with multiple accounts, your LookML project will use each Looker developer's individual Git account to perform Git operations. You also need to configure one generic Git user account, with at least read access, that Looker will use to pull the production version of the files.
The following tasks and requirements are needed for Git authentication with user attributes:
  * Each of your LookML developers must have their own user account with your Git provider. Each Git user account must have read and write access to the project's repository.
  * Your Looker admin must set up Looker user accounts with user attributes that correspond to Git username and Git password (or access token if the Git user accounts have two-factor authentication).
  * User attributes for Git account passwords (or access tokens) must be hidden. When you create the password or access token attribute, select **Yes** under the **Hide Values** option and enter the Git provider URL in the **Domain Allowlist** field.
  * The user attributes for Git name and password (or access token) must be filled in for each Looker developer. User attributes can be configured by a Looker admin or by the Looker user.


The following example shows the **User Attributes** Admin page, where a Looker admin has set up user attributes for the Git username and the user access token.
The following example shows a Looker user's **Account** page where the user has entered their Git credentials into the user attribute fields.
#### Configuring HTTPS Git authentication
To configure a LookML project with HTTPS Git authentication, follow these steps:
  1. Get the HTTPS URL for your Git repository. In the case of GitHub, for new repositories (repositories that don't yet contain any files), GitHub will show you the URL as part of the initial setup. Be sure to select the **HTTPS** button on the **Code** tab so that you get the HTTPS URL, and then select the **Copy URL to clipboard** icon to copy it to your clipboard.
For existing GitHub repositories (repositories that already contain files), you can see the HTTPS URL by going to the repository's **Code** tab and selecting the **Code** button. Be sure to select the **HTTPS** link. You can select the **Copy URL to clipboard** icon to copy the HTTPS URL to your clipboard.
  2. Navigate to your LookML project, and select the **Settings** icon from the navigation bar.
  3. In the **Project Configuration** page, on the **Configuration** tab, go to the **Configure Git** button (for new projects) or the **Reset Git Connection** button (for existing projects that have been connected to Git previously).
  4. Select the **Configure Git** or the **Reset Git Connection** button to open the **Configure Git** page.
> Resetting your Git connection will preserve Git history for the main branch. It will also preserve the history of each Looker developer's personal branch once they pull, merge, and deploy. To preserve history for all branches, see the Migrating to a new Git repository Best Practices page.
  5. In the Looker **Configure Git** page, paste the HTTPS URL for your Git repository in the **Repository URL** field, and then select **Continue**.
Looker will detect your Git provider and update the window with information about your Git repository.
If Looker does not successfully detect your Git provider, it will ask you to choose from a drop-down.
  6. Select your Git login option:
     * **Use a single, constant username and password/token combination** (see Single account HTTPS authentication).
     * **Use user attributes for username and password/token** (see User attribute HTTPS authentication).
  7. In the **Username** and **Password** /**Personal Access Token** fields, enter the credentials that your LookML project will use to access Git. This is required regardless of your Git login setting:
     * If you selected **Use a single, constant username and password/personal access token combination** , this is the Git username and password (or access token) that your Looker instance will use for all Git operations. This Git user account must have read and write access to your Git repository.
     * If you selected **Use user attributes for username and password/personal access token** , this is the Git username and password (or access token) that your Looker instance will use to pull the production version of the repository. This Git user account must have at least read access to your Git repository.
> If your Git account uses two-factor authentication, or if you're using GitHub (which requires a personal access token instead of a password), you can go to your Git provider and create access tokens to use instead of passwords. Go to the Setting up HTTPS git connection with 2FA Enabled  Community post to see instructions for creating personal access tokens for common Git providers.
  8. If you selected **Use user attributes for username and password/personal access token** , Looker displays the **Username User Attribute** and **Personal Access Token User Attribute** drop-down menus in the **Development Mode Credentials** section. Use the drop-down menus to select the user attributes for an individual developer's Git credentials.
(Looker users can edit the values for their user attribute fields on their Account page, or Looker admins can edit the user attribute values for a user on the Users admin page.)
  9. Select the **Continue Setup** button.


Git is now configured for your LookML project. From here you can validate your LookML, and then create your initial commit and deploy to production to make your project available in Production Mode. You can also:
  * Use the Git menu to access the Git commands.
  * Use the Git menu to test your Git connection.
  * If you're a Looker admin, go to the project settings to require LookML validation and to configure Git integration options.


### Connecting to Git using SSH
With SSH authentication, you create a deploy key for your Git provider. Looker generates the SSH key pair and displays the public key in the UI, as seen in step 4. Looker uses that deploy key to sign in to your Git provider to commit changes on behalf of the Looker developers. Looker makes commits using a developer's Looker username so you can tell which developer made each commit. You can see your project's commit history on your Git provider's interface or by selecting the **History** option from the Git menu of the Looker IDE. See Executing Git commands in Looker  for more information on the Git menus in Looker.
To configure a LookML project with SSH Git authentication, follow these steps:
  1. Open your project or create a new LookML project.
  2. In your project, select the **Settings** icon from the left-hand icon menu to open the **Project Configuration** page.
  3. In the **Project Configuration** page, perform one of the following actions to open the **Configure Git** page:
     * For a project with no Git connection, select the **Configure Git** button.
     * For a project that is already configured with a Git connection, select the **Reset Git Connection** button.
> Resetting your Git connection will preserve Git history for the main branch. It will also preserve the history of each Looker developer's personal branch once they pull, merge, and deploy. To preserve history for all branches, see the Migrating to a new Git repository Best Practices page.
  4. Get the SSH URL for your Git repository. Here are the formats for common Git providers:
     * GitHub: `git@github.com:<organization-name>/<repository-name>.git`
     * GitHub Enterprise: `git@example.com:<organization-name>/<repository-name>.git`
     * Cloud Source Repositories: `ssh://username@example.com@source.developers.google.com:2022/p/<project-id>/r/<repository-name>`
     * GitLab: `git@gitlab.com:<organization-name>/<repository-name>.git`
     * Bitbucket: `git@bitbucket.org:<organization-name>/<repository-name>.git`
     * Phabricator: `ssh://username@example.com/diffusion/MYCALLSIGN/<repository-name>.git`
In the case of GitHub, for new repositories (repositories that don't yet contain any files), GitHub will display the SSH URL on the **Code** tab as part of the initial setup. Be sure to select the **SSH** button so you get the SSH URL, and then select the clipboard icon to copy it to your clipboard.
For existing GitHub repositories (repositories that already contain files), you can see the SSH URL by going to the repository's **Code** tab and selecting on the **Code** button. Be sure to select the **Use SSH** link. You can select the clipboard icon to copy to your clipboard.
  5. In the Looker **Configure Git** page, paste the SSH URL for your Git repository in the **Repository URL** field, and then select **Continue**.
> URLs with custom or non-standard Git ports can be used with Looker by adding the non-standard port number to the Git URL. For example: `ssh://git@corporate.git.server.com:22/myorganization/myproject.git`
> You must include the `ssh://` for this to work properly.
  6. Looker will detect your Git provider and display a deploy key for your repository. (If Looker doesn't successfully detect your Git provider, it will prompt you to choose from a drop-down.) Copy the deploy key to your clipboard, and then select the **Deploy Key settings for your repository** link to open the GitHub **Deploy keys** page for your GitHub repository.
  7. In the GitHub **Settings** tab, on the **Deploy keys** page, select the **Add deploy key** button:
GitHub displays the **Deploy keys / Add new** page.
  8. Add a title for the deploy key. The name isn't important, but you might want to include "Looker" and your project title to keep track of it in the future.
  9. Paste the deploy key that you copied from Looker .
  10. Select the **Allow write access** option.
  11. Select the **Add key** button. (At this point, your Git provider may prompt you to enter your password. If so, enter your password and then select **Confirm password**.)
  12. GitHub will show all the deploy keys that have been added for your repository.
  13. Go back to your Looker window, and, in the **Configure Git** page, select **Test and Finalize Setup**.


From here, you can try again to set up the deploy key, or you can select **Skip Tests and Finalize Setup** to keep your current settings.
Git is now configured for your LookML project. From here you can validate your LookML, and then create your initial commit and deploy to production to make your project available in Production Mode. You can also:
  * Use the Git menu to access the Git commands.
  * Use the Git menu to test your Git connection.
  * If you're a Looker admin, go to the project settings to require LookML validation and to configure Git integration options.


### Configuring a bare Git repository
When you configure a project with a bare Git repository, Looker creates a local Git repository on your Looker server and starts the Git history for the repository, rather than connecting to a repository on a remote Git provider. Configuring a bare repository is useful if you haven't yet created a remote Git repository to connect to, or if you want to get set up quickly so others can benefit from your LookML. For example, when you create a new project during the process of generating a model, the project is automatically configured with a bare repository.
When you configure a project with a bare Git repository, you can later reset your project's Git connection from your project's **Project settings** page and create a connection to a remote Git provider using either HTTPS or SSH.
Note the following limitations with bare repositories:
  * Projects that are configured with a bare repository don't support Git integration options, such as creating a pull request and showing links to the Git repository.
  * Once you create a bare repository, you can't create another bare repository with the same name. For more information, see the related Community article, Error - "Project already Exists" for bare repo.


To configure a LookML project with a bare Git repository:
  1. Open your project or create a new LookML project.
  2. In your project, select the **Settings** icon from the left-hand icon menu to open the **Project Configuration** page.
  3. In the **Project Configuration** page, perform one of the following actions to open the **Configure Git** page:
     * For a project with no Git connection, select the **Configure Git** button.
     * For a project that is already configured with a Git connection, select the **Reset Git Connection** button.
> Resetting your Git connection will preserve Git history for the main branch. It will also preserve the history of each Looker developer's personal branch once they pull and merge and then deploy. To preserve history for all branches, see the Migrating to a new Git repository Best Practices page.
  4. Select **Set up a bare repository instead** at the bottom of the **Configure Git** page.
  5. In the **Configure Bare Git Repository** dialog, select **Create Repository**.
After the Git repository is created, Looker will display a **Bare Repository Created** dialog.


Git is now configured for your LookML project. From here you can validate your LookML, and then create your initial commit and deploy to production to make your project available in Production Mode. You can also:
  * Use the Git menu to access the Git commands.
  * Use the Git menu to test your Git connection.
  * If you're a Looker admin, go to the project settings to require LookML validation and to configure Git integration options.


For projects that are configured with a bare repository, you can subsequently use the **Reset Git Connection** if you want to connect the project to a Git provider (see the procedures for using HTTPS or SSH). However, don't connect to a Git repository that already has a Git history. If you have set up your LookML project with a bare repository, Looker creates a repository on your Looker server and starts the Git history for the repository. If you subsequently connect your LookML project to a Git repository that has a Git history, Looker will be unable to reconcile the two Git histories and you will be unable to perform any Git actions.
### Connecting a new LookML project to a non-empty Git repository
Configuring Git for version control is a key step in creating a new LookML project. Typically, each project should have its own repository. However, you may need to configure a project with a Git repository that contains existing LookML, such as in the following situations:
  * When you're moving an existing LookML project between instances
  * When you're resurrecting the code from a broken or defunct LookML project for use in a new project


This section describes best practices for configuring a new LookML project with an existing, non-empty Git repository for further LookML development.
  1. Create a new LookML project by selecting **Blank Project** as the starting point. A blank project is the starting point because it will be populated with LookML objects from an existing repository, rather than from a database schema or SQL query.
  2. Configure Git for your project using either HTTPS or SSH, using the URL for the non-empty project in the **Repository URL** section of the **Configure Git** page.
  3. Once you have configured Git for your project, pull from production from the **Git Actions** panel.
  4. Once you have pulled from production, select **Deploy to Production**.


Changes that you make to the LookML in your project won't affect the original repository; rather, the changes will be saved in your local version of the repository.
If you want to to use a specific public repository as the basis of a blank LookML project but you don't have write access to that repository, follow the instructions that are outlined in the Cloning a public Git repository section of the **Creating a new LookML project** documentation page.
If you're setting up a Git workflow using one repository across multiple instances, see the Community post on Git workflow using one repository across multiple instances — development, staging, and production for more information.
## Testing your Git connection
Looker provides a Git connection test to verify your Git connection. The Git connection test verifies that you've set up the correct Git URL and that the Git host is reachable by Looker . The Git connection test also verifies that you have provided a valid Git deploy key and that the deploy key has write access to your Git repository.
If Looker is unable to connect to your Git repository, the Git button will display the text **Test Git Connection** to prompt you to troubleshoot your connection.
You can also access the Git connection test tool by selecting **Test Git Connection** in the **Git actions** panel:
The Git connection test tool then displays the steps it is taking to test the Git connection:
  1. **Examine git remote**
  2. **Host name for git service will resolve**
  3. **Networking to the git service is operational**
  4. **Verify authorization credentials**
  5. **Ensure credentials allow write access**


If a step is successful, Looker displays a green checkmark to the left of the step. If a step is unsuccessful, Looker displays a red checkmark to the left of the step and also displays an error message.
The following example shows a successful test:
In the following example, the Git repository does not have a deploy key configured for the Looker connection. The green checkmarks to the left of the first three steps indicate that these steps were successful:
  * `Examine git remote`
  * `Host name for git service will resolve`
  * `Networking to the git service is operational`


The red checkmarks to the left of the last two steps indicate that these steps failed:
  * `Verify authorization credentials`
  * `Ensure credentials allow write access`


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


