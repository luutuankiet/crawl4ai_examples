# Git command reference  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/git-command-reference

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Git command reference
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Git commands are accessed either from the button at the top right of the Looker IDE or by clicking the **Git Actions** button from the main navigation menu.
> The **Git Actions** panel is not available until you have configured your project for Git.
The following table shows the possible Git commands. Note that the commands that you see in the Looker IDE will depend on where you are in the process of making changes and deploying to production. The IDE shows only the Git commands that apply to your current status.
Function | Description | How to Access  
---|---|---  
Commit  |  After you have made and saved any changes to your LookML project, use the **Commit Changes & Push** button to commit these changes to your local branch and push them to production. See the Using version control and deploying documentation page for more information. |  **Git Actions** panel   
Commit Changes & Push  |  Button   
Commit & Resolve Conflict  | The **Commit & Resolve Conflict** button is displayed when you make changes after a merge conflict. Click **Commit & Resolve Conflict** to commit your changes and clear the merge conflict. |  Button   
Commit History  |  Shows the list of the commits to your branch, which includes all the commits that you have pulled into your development branch from the production branch (including commits from other users). Project Settings has GitHub Integration enabled, each of the commits will include a link to the commit on GitHub so you can view the exact changes. This functionality also works with other Git providers if your Git Project Settings has that Git provider's equivalent to GitHub Integration enabled. To open the links, you will need an account on your Git provider.  |  **Git Actions** panel   
Configure Git  | If you have just created a project, you will need to configure Git for the project. See the Setting up and testing a Git connection documentation page for more information.  |  Button   
Create Developer Copy  |  To increase performance, the first time you open a LookML project in Development Mode, the Looker IDE displays the Production Mode version of the project, along with the **Create Developer Copy** button. Once you click the **Create Developer Copy** button for the project, the Looker IDE creates your personal Git branch and loads the LookML project in Development Mode for you.  |  Button   
Deploy from Remote | For projects where the developer has read-only access, the **Deploy from Remote** button deploys from the remote production branch.  |  Button   
Deploy to Production  |  After you have committed changes, use the **Deploy to Production** option to update the production branch with the committed changes from your development branch. This option is not available if your project is configured for pull requests required. Also, if your project is enabled for advanced deploy mode, you won't see the **Deploy to Production** button. Instead, you will see **Merge to Primary Branch**.  |  Button, **Git Actions** panel   
Don't Resolve  | The **Don't Resolve** button appears when there is a merge conflict between one or more developers or development branches on the project. The **Don't Resolve** button pushes the current version of your branch, with all the merge conflict markers, to the remote. **This option should only be used by advanced Git users, since the merge conflict markers are likely to render your models unusable.** |  Button   
Merge to Primary Branch |  If your project is enabled with advanced deploy mode, the **Merge to Primary Branch** button is displayed after you make a commit. This prompts you to merge your changes to the primary branch. Once you merge your changes to the primary branch, a Looker developer with the `deploy` permission can deploy your changes to the production environment using a webhook, the API, or the deployment manager UI in the Looker IDE.  |  Button   
Open (Git provider)  |  The **Open (Git provider)** option opens a browser window to the project files on your Git provider's interface.  |  Button   
Open Pull Request  | For projects where pull requests are recommended or required, the **Open Pull Request** option will open a new browser window to your Git provider's new pull request page. From there you can create a pull request for your developer branch.**NOTE:** Until the pull request is approved and/or closed, all future commits on the branch will be included in the same pull request.  |  **Git Actions** panel   
Pull & Merge Other Changes  | The **Pull & Merge Other Changes** button has the same function as **Pull from (production branch)** , but the **Pull & Merge Other Changes** button is seen in different circumstances — when you have committed changes on your branch but have not deployed them, and there are also remote, undeployed, committed changes on the branch. In this case you need to pull the changes from the remote and merge them into your branch.  |  Button   
Pull from Primary Branch |  If your project is enabled with advanced deploy mode, the **Pull from Primary Branch** option is displayed when the primary branch has commits that are not on your developer branch.  |  Button   
Pull from (production branch)  |  The **Pull from (production branch)** option is not available when the current developer branch has uncommitted changes. You must commit changes on the branch before you will see the **Pull from (production branch)** option.  |  Button, **Git Actions** panel   
Pull Remote Changes  |  If other people have committed and pushed changes on a branch, the remote version of the branch will be ahead of your local version of the branch. The **Pull Remote Changes** button applies to the branch you're on. Click the **Pull Remote Changes** button to retrieve the most recent versions of any changed files on the branch from the remote end and sync them to your local files.  |  Button   
Push Branch to Remote |  If you have created a branch that does not exist on the remote end, you will see the **Push Branch to Remote** button. The **Push Branch to Remote** option creates the branch on the remote end, pushing all committed changes from your local files to the remote end. Note that this does not deploy your changes to the production branch.  | Button  
Push Changes to Remote  |  If you have committed changes to your current branch that are not yet pushed to the remote version of the branch, you will see the **Push Changes to Remote** option. The **Push Changes to Remote** operation applies to the branch you're on. Click the **Push Changes to Remote** button to push all committed changes from your local files and sync them to the remote end.  |  Button, **Git Actions** panel   
Revert to Remote |  The **Revert to Remote** option discards any changes in your local branch and syncs your local files to the current files on the remote branch. Note that this has two effects: 
  1. Discards any of your committed and uncommitted changes that have not been deployed to production
  2. Updates your local version of the branch with any changes that other users have made to the branch

|  Button   
Revert to Shared  |  The **Revert to Shared** option discards any changes in your local branch and syncs your local files to the current files on the remote branch. Note that this has two effects: 
  1. Discards any of your committed and uncommitted changes that have not been deployed to production
  2. Updates your local version of the branch with any changes that other users have made to the branch

|  Button   
Revert Uncommitted Changes  |  If you have saved changes that you have not yet committed, you can use the **Revert Uncommitted Changes** option to discard all the changes that have not been committed. See the Using version control and deploying documentation page for more information.  |  Button   
Run Tests  |  If your project is configured to require data tests to pass before it can be deployed to production, the IDE will present the **Run Tests** button after you commit changes to the project. You must pass the data tests before you can deploy your changes to production. You can also run the tests manually by clicking the **Run Data Tests** icon in the **Project Health** panel. See the Using version control and deploying documentation page for information on running data tests. See the `test` parameter documentation page for information on setting up data tests in your project.  |  Button   
Test Git Connection  | Once you have configured Git for your project, you can use the **Test Git Connection** option to run the Git Test Connection tool, which verifies that your Git connection is set up properly. See the Testing your Git connection documentation page for more information.  |  Button, **Git Actions** panel   
Up to Date |  If your local branch is in sync with the remote branch, you will see the **Up to Date** button.  |  Button   
Update Dependencies  |  For projects that use remote project import, the **Update Dependencies** option is displayed when you first add a remote project, or when your project already has an imported remote project that Looker detects has new commits for you to bring into your project. Use this option to bring in the remote project files. If you have just added a remote project, using this option will also create a manifest lock file, which Looker uses to track the version of the remote project. See the Automatically detecting new versions of a remote project section of the Importing files from other projects documentation page for more information.  |  Button, **Git Actions** panel   
Validate LookML  |  If you have saved changes to your files, you may see the **Validate LookML** button. (Whether or not you are required to validate your LookML depends on your project's setting for code quality.) Click the button to start LookML validation of your model. See the Validating your LookML documentation page for more information.  |  Button   
View Project on (Git provider)  | The **View Project on (Git provider)** option opens a browser window to the project files on your Git provider's interface.  |  **Git Actions** panel   
View Uncommitted Changes  | If you have saved changes that you have not yet committed, you can use the **View Uncommitted Changes** option to see all the changes that you have saved since your last commit. See the Using version control and deploying documentation page for more information.  |  **Git Actions** panel   
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


