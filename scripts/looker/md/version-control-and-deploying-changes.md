# Using version control and deploying  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/version-control-and-deploying-changes

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Working with Git branches
    * Personal branches
    * Creating a new Git branch
    * Switching to another Git branch
    * Managing Git branches
    * Deleting Git branches
  * Executing Git commands in Looker
  * Getting your changes to production
    * Viewing uncommitted changes
    * Committing changes
    * Checking for unbuilt PDTs
    * Running data tests
    * Deploying to production
  * Advanced deploy mode
  * Checking the impact of your changes
  * Handling typical issues
    * Reverting uncommitted changes
    * Resolving merge conflicts
  * Git garbage collection




Was this helpful?
Send feedback 
#  Using version control and deploying
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Working with Git branches
    * Personal branches
    * Creating a new Git branch
    * Switching to another Git branch
    * Managing Git branches
    * Deleting Git branches
  * Executing Git commands in Looker
  * Getting your changes to production
    * Viewing uncommitted changes
    * Committing changes
    * Checking for unbuilt PDTs
    * Running data tests
    * Deploying to production
  * Advanced deploy mode
  * Checking the impact of your changes
  * Handling typical issues
    * Reverting uncommitted changes
    * Resolving merge conflicts
  * Git garbage collection


> This page assumes that your project has already been set up for version control. If you see a **Configure Git** button instead of the choices described on this page, you need to first set up Git for your project.
Looker uses Git to record changes and manage file versions. Each LookML project corresponds to a Git repository, and each developer branch correlates to a Git branch.
Looker can be configured to work with many Git providers, such as GitHub, GitLab, and Bitbucket. See the Setting up and testing a Git connection documentation page for information on setting up Git for your Looker project.
## Working with Git branches
One of the main benefits of Git is that a Looker developer can work in a _branch_ , an isolated version of a file repository. You can develop and test without affecting other users. As a developer in Looker, you are using a Git branch whenever you are in Development Mode.
Another major feature of Git is the ease of collaborating with other developers that it provides. You can create a branch and (if desired) make changes, and then other developers can switch to that branch to review or make changes to the branch. If another developer has committed changes to the branch, Looker displays the **Pull Remote Changes** button. You should pull those committed changes to the branch before making additional changes.
You can also delete a branch other than the master branch, your current branch, or a developer's personal branch.
### Personal branches
To increase performance, the first time you open a LookML project in Development Mode, the Looker IDE displays the Production Mode version of the project, along with the **Create Developer Copy** button. Once you click the **Create Developer Copy** button for the project, the Looker IDE creates your personal Git branch and loads the LookML project in Development Mode for you.
Your personal branch starts with `dev-` and includes your name.
Your personal branch is specific to you, and it _cannot_ be deleted. Your personal branch is read-only to all other developers. If you are collaborating with other developers on a project, you may want to create a new branch so that others can switch to that branch and contribute changes as well.
### Creating a new Git branch
If you are working on a simple fix and not collaborating with other developers, your personal branch is usually a good place to work. You can use your personal branch to make quick updates, and then commit the changes and push them to production.
However, you may also want to create new Git branches in addition to your personal branch. A new Git branch makes sense in these situations:
  * **You are working with other developers**. Since your personal branch is read-only to other developers, if you want to collaborate with others, you should create a new Git branch so that other developers can write to the branch. When you're collaborating with others, be sure to pull changes each time you resume work. That way, you'll have the latest updates from all developers before continuing work.
  * **You are working on multiple sets of features at once**. Sometimes you may be in the middle of a major project, but want to resolve a minor issue or make a quick fix. In this case, you can commit your changes to the branch you're on and then create or switch to another branch to work on a separate set of features. You can make your fix in the new branch, and then deploy that branch's changes to production — before resuming work in your original branch.


Before creating a new branch:
  * If you have a merge conflict on your current branch, you must resolve the conflict before you can create a new branch.
  * If you have any uncommitted changes on the current branch, you must commit the changes on your current branch before creating a new branch.
  * If you want to create a branch starting from an existing development branch (and not the production branch), first get the latest version of the development branch by switching to that development branch, and then pull remote changes to sync your local version of that branch.


To create a new Git branch:
  1. Verify that you have Development Mode turned on.
  2. Navigate to your project files in the **Develop** menu.
  3. Select the **Git** icon in the left-hand icon menu to open the **Git Actions** panel.
  4. Select the **View Branches** drop-down menu.
  5. Select **New Branch**.
  6. In the **New Branch** window, enter a name for your branch. Note that there are limitations for Git branch names; for naming requirements, see Rules for naming a Git branch on this page.
  7. Select the **Create From** drop-down menu and select an existing branch to use as the starting point for your new branch.
  8. Select **Create** to create your branch.


Alternatively, you can create Git branches from the **Branch Management** tab of the project's settings.
#### Rules for naming a Git branch
Looker uses the branch-naming-convention requirements specified by Git.
Git branch names must _not_ :
  * Contain a space character
  * Contain a double period: `..`
  * Contain a backslash: `\`
  * Contain the sequence: `@{`
  * Contain a question mark: `?`
  * Contain an opening square bracket: `[`
  * Contain an ASCII control character: `~` or `\^` or `:`
  * Begin with a period: `.`
  * Begin with the prefix: `dev-` (reserved for the personal branches of Looker developers)
  * End with a forward slash: `/`
  * End with the extension: `.lock`


In addition, the branch name can only contain an asterisk (`*`) if the asterisk represents an entire path component (for example, `foo/*` or `bar/*/baz`), in which case it is interpreted as a wildcard and not as part of the actual branch name.
### Switching to another Git branch
> If you have a merge conflict on your current branch, you must resolve the conflict before you can switch to a different branch. 
> commit the changes on your current branch.
To switch to a different Git branch, follow these steps:
  1. In the project, navigate to the **Git Actions** panel by selecting the **Git** icon in the left-hand icon menu.
  2. In the **Git Actions** panel, select the Git branch drop-down menu to the right of your current Git branch name.
  3. Select the branch you want to switch to by selecting it in the menu, or by typing the branch name into the search box. Branch name search is case-insensitive. For example, you can search for "DEV" and see all branches with names that include "dev", "DEV", "Dev", and so on.


### Managing Git branches
The **Branch Management** tab of the project settings shows a table of all the Git branches for the Looker project. To open the **Branch Management** tab, first navigate to the project settings by selecting the **Settings** icon from the left-hand icon menu. Next, select the **Branch Management** tab.
On the **Branch Management** tab, you can:
  1. Create a new branch by selecting the **New Branch** button. See the Creating a new Git branch section on this page for more information.
  2. Search for branch names in the **Search Bar**.
  3. Refresh the table by selecting the **Refresh** button.
  4. Sort the table by selecting a column name.


The table includes the following information:
  * **Name** : Name of the Git branch. Looker developers' personal branches start with `dev-` and include the first and last name of the developer.
  * **Status** : The difference between your local version of the branch and the remote version of the branch. For example, a status of `3 commits behind` means that your local version of the branch is behind the remote version of the branch by three commits. Because Looker always uses the remote version of master, the **Branch Management** tab doesn't show the status of the local version of the master branch. The master branch can always be considered to be up to date.
  * **Last Updated** : Amount of time since a Looker developer made a commit to the branch.
  * **Actions** : A button to delete the branch, or the reason that the branch is not eligible for deletion.


### Deleting Git branches
From the **Branch Management** tab, you can delete branches that have a **Delete** button in the table. You cannot delete the following branches:
  * The master branch
  * Your current branch
  * A Looker developer's personal branch


In the table, these branches don't have a **Delete** button. Instead, the **Action** column of the table shows the reason that the branch can't be deleted.
> You cannot restore a branch once it's been deleted. When you delete a branch, Looker removes both your local version of the branch and the remote version of the branch. 
> _do_ want to restore the branch. Otherwise, when you delete a branch, all other Looker developers should delete the same branch to ensure that it can't be accidentally resurfaced by someone pushing it to remote.
To delete one or more Git branches from your project, first navigate to the project settings by selecting the **Settings** icon from the left-hand icon menu. Then select the **Branch Management** tab. In the **Branch Management** tab, you can delete branches in two ways:
  1. Delete multiple branches by first selecting the branch checkboxes and then selecting **Delete Selected Branches**.
  2. Delete a single branch by selecting **Delete** next to the branch name.


## Executing Git commands in Looker
Looker has a built-in interface that integrates with your Git service. Looker displays the **Git button** in the upper right corner of the LookML IDE.
The Git button shows different options depending on where you are in the process of making changes and deploying to production. In general, the option shown on the button is the best guide for your next action.
If your developer branch is in sync with the production branch, the Git button displays the **Up to Date** message and is not selectable.
Once your project is configured for Git, you can select the **Git Actions** button to open the **Git Actions** panel.
The commands available on the **Git Actions** panel depend on where you are in the process of making changes and deploying to production.
## Getting your changes to production
With the default Looker Git integration, Looker prompts developers through the following Git workflow:
  * Committing changes to the developer's current development branch (and running data tests if your project is set up to require tests before deploying)
  * Merging the development branch into the production branch, which by default is called `master`
  * Deploying the production branch to the Looker production environment that will be presented to your Looker end users


This means that, with the default Git integration, all developers merge their changes into a branch called `master`, and the latest commit on the `master` branch is what is used for the production environment of Looker.
For advanced Git implementations, you can customize this workflow:
  * You can have your developers submit pull requests for your Git production branch, instead of allowing developers to merge their changes through the Looker IDE. See the Configuring project version control settings documentation page for details.
  * You can use the **Git Production Branch Name** field to specify which branch from your Git repository Looker should use as the target branch into which your Looker developers' branches are merged. See the Configuring project version control settings documentation page for details.
  * You can use advanced deploy mode for specifying a different commit SHA or tag name to deploy to your Looker production environment, instead of using the latest commit on the production branch. (If you want to deploy a commit from a different branch, you can use the advanced deploy mode webhook or API endpoint.) See the Advanced deploy mode documentation page for details.


> If you see a **Configure Git** button instead of the choices described in this section, you need to first set up Git for your project.
### Viewing uncommitted changes
The LookML IDE has several indicators that are displayed when you are in Development Mode and have uncommitted changes, as described in the Marking additions, changes, and deletions section of the Looker IDE overview documentation page.
You can get a difference summary for all files by selecting the **View Uncommitted Changes** option from the **Git Actions** panel.
In the **Uncommitted Changes to Project** window, Looker displays a summary of all the uncommitted, saved changes in all the project's files. For each change, Looker shows the following:
  * The name of the replaced file and the name of the added file. 
    * The name of the replaced file (indicated with `---`) and the name of the added file (indicated with `+++`). In many cases, this may show different versions of the same file, with revisions identified by `--- a/` and `+++ b/`.
    * Deleted files are shown as replacing a null file (`+++ /dev/null`).
    * Added files are shown as replacing a null file (`--- /dev/null`).
  * The line number where the change begins.`-101,4 +101,4` indicates that, at the 101st line in the file, 4 lines were removed and 4 lines were added. A deleted file with 20 lines would show `-1,20 +0,0` to indicate that, at the first line in the file, 20 lines were removed and replaced by zero lines.
  * The text that was updated: 
    * Deleted lines are displayed in red.
    * Added lines are displayed in green.


To display a difference summary for a single file, select the **View Changes** option from the file's menu.
### Committing changes
After you have made and saved any changes to your LookML project, the IDE may require you to validate your LookML. The Git button displays the text **Validate LookML** in this scenario.
Whether this is required depends on your project's setting for code quality. For more information on the Content Validator, see the Validating your LookML documentation page.
If another developer has made changes to the production branch since you last updated your local branch, Looker requires you to pull those updates from the production branch. The Git button displays the text **Pull from Production** in this scenario.
> If your project is enabled for advanced deploy mode, the Git button instead displays the text **Pull from Primary Branch**.
Once you save your changes (and fix any LookML warnings or errors, if required) and pull from production (if required), the Git button displays the text **Commit Changes & Push**.
If desired, you can first review your uncommitted changes before committing.
When you are ready to commit the changes, use the Git button to commit these changes to your current branch. Looker displays the **Commit** dialog box, which lists the files that have been added, changed, or deleted.
Enter a message that briefly describes your changes, and clear the checkboxes next to any files that you don't want to include in the sync. Then select **Commit** to commit the changes.
### Checking for unbuilt PDTs
If you have made changes to any PDTs in your project, it is optimal that all of your PDTs be built when you deploy to production so that the tables can be used immediately as the production versions. To check the status of PDTs in the project, select the **Project Health** icon to open the **Project Health** panel, and then select the **Validate PDT Status** button.
See the Derived tables in Looker documentation page for more information about checking for unbuilt PDTs in your LookML project and about working with derived tables in Development Mode.
### Running data tests
Your project may include one or more `test` parameters that define data tests to verify the logic of your LookML model. See the `test` parameter documentation page for information on setting up data tests in your project.
If your project contains data tests and you are in Development Mode, you can initiate your project's data tests in several ways:
  1. If your project settings are configured to require data tests to pass before deploying your files to production, the IDE will present the **Run Tests** button after you commit changes to the project to run all the tests for your project, no matter which file defines the test. You must pass the data tests before you can deploy your changes to production.
  2. Select the **Run Data Tests** button in the **Project Health** panel. Looker will run all data tests in your project, no matter which file defines the test.
  3. Select the **Run LookML Tests** option from the file's menu. Looker will run only the tests defined in the current file.


Once you run the data tests, the **Project Health** panel will display the progress and results.
  * A data test passes when the test's assertion is true for every row in the test's query. See the `test` parameter documentation page for details on setting up test assertions and queries.
  * If a data test fails, the **Project Health** panel will provide information about why the test failed, whether the test found errors in your model's logic or if it was the test itself that was invalid.
  * From the data test results, you can select the name of a data test to go directly to the LookML for the data test, or you can select the **Explore Query** button to open an Explore with the query defined in the data test.


### Deploying to production
Once you have committed changes to your branch, the Looker IDE will prompt you to merge your changes to the primary branch. The type of prompt you'll see in the IDE will depend on your project's configuration:
  * If your project is configured for advanced deploy mode, the IDE will prompt you to merge your changes into the primary branch. Once you merge your commit, a Looker developer with the `deploy` permission can deploy your commit to production by using the Looker IDE deployment manager, or by using a webhook or an API endpoint.
  * If your project is configured for Git integration using pull requests, you will be prompted to open a pull request using your Git provider's interface.
  * Otherwise, with the default Looker Git integration, if you have `deploy` permission, the Looker IDE will prompt you to merge your changes to the production branch and deploy your changes to the production version of your Looker instance.


## Advanced deploy mode
With the default Looker Git integration, Looker developers commit their changes to their development branch, then merge their development branch into the production branch. Then, when you deploy to the Looker environment, Looker uses the latest commit on the production branch. (See the Getting your changes to production section on this page for the default Git workflow and other options for advanced Git implementations.)
For cases where you don't want the to always use the latest commit on the production branch for your Looker environment, a developer with `deploy` permission can use advanced deploy mode to specify the exact commit to be used for your Looker environment. This is useful in multi-environment developer workflows, where each environment points to a different version of a codebase. It also gives one or several developers or administrators greater control over the changes that are deployed to production.
When advanced deploy mode is enabled, the Looker IDE does not prompt developers to deploy their changes to production. Instead, the IDE prompts developers to merge their changes into the production branch. From there, changes can be deployed only in the following ways:
  * Using the deployment manager in the Looker IDE
  * Triggering a webhook
  * Using an API endpoint


See the Advanced deploy mode documentation page for details.
## Checking the impact of your changes
After making your changes available to the organization, you can use content validation to make sure you have not invalidated any dashboards or saved Looks. You'll have the opportunity to fix them if you have.
## Handling typical issues
While working on your model, you may need to:
  * Abandon your changes
Occasionally you may want to abandon your data-modeling changes. If they are not yet saved, you can simply refresh or navigate away from the page and then accept the warning prompt. If you have saved the changes, you can revert the uncommitted changes as described in the Reverting uncommitted changes section.
  * Handle merge conflicts with other developers' work
If you have more than one developer working on your data model, Git typically handles the situation. However, occasionally Git needs a human to resolve merge conflicts.


Some changes, such as changing the name of a field, can affect existing dashboards and Looks. As mentioned earlier, after making your changes available to the organization, you can use content validation to check your content and fix any issues.
### Reverting uncommitted changes
When working on your personal development branch, you can revert uncommitted changes that you have saved if you do not want to deploy them. You can revert all the uncommitted changes for all files in the project or just the changes in a single file.
To revert uncommitted changes for _all files_ :
  1. Select the **Revert to...** option in the **Git Actions** panel.
  2. Select a revert option: 
     * To revert only _uncommitted_ changes, select **Revert uncommitted changes**. You can also select the **View changes** link to view the changes that would be reverted.
     * To revert all changes, including uncommitted and committed changes, select **Revert to Production**
  3. To complete the revert process, select **Confirm**.


To revert any additions or deletions in the contents of a single file, select the **Revert Changes** option from that file's menu:
> When you rename a file, you are essentially deleting the original file and creating a new file with a new name. Because this involves more than one file, you can't use the **Revert File** option to undo the renaming of a file. If you want to undo a file rename, use the **Revert to...** option from the **Git Actions** panel.
> Also, if you have deleted a file, the file is no longer displayed in the IDE file browser. If you want to revert the deletion of a file, use the **Revert to...** option from the **Git Actions** panel.
### Resolving merge conflicts
Typically, Git can automatically merge your new changes with the production version of your LookML files. A merge conflict occurs when Git encounters conflicting changes and cannot identify which changes should be kept, usually when another developer has made changes since you last pulled and you have made changes in the same area. If you have a merge conflict in your code, Looker displays a **Merge conflicts** warning after you commit changes and pull from production.
When Looker shows the merge-conflict warning, we recommend that you resolve the merge conflict before making any further changes. Pushing a merge conflict to production will cause parse errors that may prevent exploration of your data. If you are an advanced Git user and you want to move forward with pushing changes, select the **Don't Resolve** button.
In the LookML file itself, the lines with conflicts are marked like this:
```
<<<<<<< HEAD
Your code
&#61;&#61;&#61;&#61;&#61;&#61;&#61;
Production code
>>>>>>> branch 'master'

```

Looker shows the following _merge markers_ to indicate the merge conflicts:
  * **< <<<<<< `HEAD`** marks the beginning of the conflicting lines.
  * **> >>>>>> `branch 'master'`** marks the end of the conflicting lines.
  * **=======** separates each version of the code so you can compare them.


In the preceding example, `your code` represents the changes you committed, and `production code` represents the code into which Git could not automatically merge your changes.
To resolve a merge conflict:
  1. Find the files with merge conflicts. Looker marks these files in red, or you can also search your project for merge markers, such as <<<< or `HEAD`, to find all the conflicts in your project. You can also find affected files by selecting the **files** link in the merge warning that appears in the **Git Actions** panel.
  2. In the file, go to the lines with merge conflicts and delete the version of the text that you do **NOT** want to keep, and also delete all the merge conflict markers.
  3. Save the file, and repeat the preceding steps for any other files marked with merge conflicts.
  4. After you have resolved all merge conflicts and deleted all merge markers from your project, commit the changes and deploy them to production.


Now that you have resolved the merge conflict and pushed your resolution to production, other developers can pull from production and continue work as usual.
## Git garbage collection
Git garbage collection cleans up unnecessary files and compresses file revisions to optimize your Git repository. Git garbage collection (`git gc`) is run automatically when your Looker instance is updated or rebooted. To keep from running `git gc` too often, Looker waits 30 days since the last `git gc` and then runs `git gc` on the next reboot.
In rare cases, you might try to **Push Changes to Remote** or **Push Branch to Remote** while `git gc` is running. If Looker displays an error, wait for a minute or two and then try again to push your changes.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


