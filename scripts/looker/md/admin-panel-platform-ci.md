# Admin settings - Continuous Integration  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-ci

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enable Continuous Integration
  * Continuous Integration users




Was this helpful?
Send feedback 
#  Admin settings - Continuous Integration
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enable Continuous Integration
  * Continuous Integration users


The **Continuous Integration** page in the **Platform** section of the **Admin** menu lets you configure settings for the Looker Continuous Integration (CI) feature.
## Enable Continuous Integration
The Looker Continuous Integration (CI) feature lets you run tests on your LookML project to deliver more reliable, efficient, and user-friendly data experiences. You can use the CI validators to catch issues with SQL, data tests, content, and LookML before they hit production to verify your LookML and prevent query errors for your users. You can also configure the CI validators to run automatically when a pull request is submitted to your LookML repository.
A Looker admin can use the **Enable Continuous Integration** toggle to enable Continuous Integration on your instance.
## Continuous Integration users
A _Continuous Integration (CI) user_ is a Looker user account that is set aside for Continuous Integration use only; it is used to authenticate CI runs. Looker supports a maximum of three CI users.
To add a Continuous Integration user, follow these steps:
  1. Create a Looker user account with `develop` permissions. This account must be used for Continuous Integration only. 
  2. Generate API keys for the account, and copy the API's **Client ID** and **Client Secret**.
  3. On the **Continuous Integration** admin page in Looker, add the user: 
     * Click the **Add user** button.
     * Paste in the **Client ID** and **Client Secret** values from the API keys you generated.
     * Click the **Test connection** button. 
     * If the test is successful, click the **Add user** button to add the Continuous Integration user.


The Looker user that you've set aside for Continuous Integration is now associated with Continuous Integration, and the Client ID of the user account is now displayed in the **Continuous Integration users** section.
## Integrations
If you use GitHub as a remote repository for your LookML project, you can configure Continuous Integration to automatically run CI suites when LookML developers submit pull requests to your LookML repository. To automatically run CI suites on your repository, Continuous Integration needs the following permissions:
  * Read access to your repository's metadata and pull requests
  * Read and write access to your repository's commit statuses, repository hooks, and workflows


These permissions are not set up when you set up a Git connection for your LookML project in the Looker IDE. If you want to use pull request triggering for CI runs, your LookML project must be set up with a Git connection (as described on the Setting up and testing a Git connection page), and you must also configure the CI GitHub app as described in this section.
To configure the CI GitHub app, follow these steps:
  1. On the **Continuous Integration** admin page in Looker, click the **Configure GitHub App** button. This will open a browser window to the GitHub apps webpage.
  2. Select the GitHub account where your LookML is stored.
  3. In the **Repository access** section, select **All repositories** to allow CI integrations for all of the Git repositories owned by the resource owner, or select **Only select repositories** to choose the repositories with which you want to use Continuous Integration.
  4. Click **Save**.


If the connection is successful, the **GitHub** section of the **Continuous Integration** admin page in Looker will display a green **Connected** box.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


