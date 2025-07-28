# Using the Looker Marketplace  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/marketplace

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Looker Marketplace overview
    * Limitations of the Looker Marketplace
  * Enabling access to the Looker Marketplace and its content
  * Discovering Looker Marketplace content
  * Installing a tool from the Marketplace that is associated with your instance
    * Automatically installing Looker-built applications
  * Installing a tool from a Git URL
  * Installing a tool from the Marketplace instance
  * Using Looker Marketplace content
  * Managing installed tools
  * Related resources




Was this helpful?
Send feedback 
#  Using the Looker Marketplace
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Looker Marketplace overview
    * Limitations of the Looker Marketplace
  * Enabling access to the Looker Marketplace and its content
  * Discovering Looker Marketplace content
  * Installing a tool from the Marketplace that is associated with your instance
    * Automatically installing Looker-built applications
  * Installing a tool from a Git URL
  * Installing a tool from the Marketplace instance
  * Using Looker Marketplace content
  * Managing installed tools
  * Related resources


The Looker Marketplace is a central location for finding, deploying, and managing Looker Blocks, applications, custom visualizations, and actions. This page describes how to access the Looker Marketplace and how to install its content for use within a Looker instance.
## Looker Marketplace overview
You can browse content on the Looker Marketplace from the following locations:
  * From the standalone Looker Marketplace instance at `marketplace.looker.com`
  * From the **Marketplace** storefront icon in the menu bar of your Looker instance


The Marketplace homepage shows popular Looker applications, models, and visualizations.
The terminology of Looker Marketplace content differs between the two locations. See the following table for an overview of the different terms.
marketplace.looker.com | Looker instance Marketplace | Description  
---|---|---  
Applications | Applications | Applications, also referred to as "extensions" throughout the documentation, are built with Looker components that are developed through the Looker extension framework.  
Blocks | Models | Models, also referred to as "Blocks" throughout the documentation, are prebuilt LookML models, including dashboards and Explores, for a variety of popular data sources.  
Plug-ins | Visualizations | Plug-ins are visualization types that you can install and add to Looker's built-in visualization library.  
No permissions are needed to browse content on the standalone Marketplace instance; however, you won't be able to install Marketplace content for use with your Looker instance.
See the following table for an overview of the permissions that are required to perform the actions that are described on this page.
Task | Required role or permission  
---|---  
Enable Marketplace setting  
View the Marketplace icon  
Browse content from the Looker Marketplace that is associated with your Looker instance  
Install content from the Marketplace |  develop, manage_models, and deploy  
Install content from git URL |  develop, manage_models, and deploy  
Manage installed tools |  develop, manage_models, and deploy  
Use applications | Depends on the extension  
Use visualizations or plug-ins  
Use models or Blocks | Depends on the model or Block  
### Limitations of the Looker Marketplace
Looker (Google Cloud core) instances that use private IP networks or that use public IP and private IP networks don't support the Looker Marketplace.
Customer-hosted Looker instances may require additional configuration to access Marketplace data:
  * If your instance is on Looker 23.10 or later, the server that is running the Looker instance must be configured to access the public internet server that is running at the URL `https://static-a.cdn.looker.app/`.
  * If your instance is on Looker 23.8 or earlier, the server that is running the Looker instance must be configured to access the public internet server that is running at the URL `https://marketplace-api.looker.com/`.
  * The server that is running the Looker instance must also be configured to access the public internet server that is running at the URL `https://github.com/`.


Additionally, customer-hosted deployments that are using clustered instances must set up a shared (network) file system to install applications or tools from the Looker Marketplace.
## Enabling access to the Looker Marketplace and its content
To enable users to access and install content from the Looker Marketplace, a Looker admin must follow these steps:
  1. Navigate to the **Marketplace** page in the **Platform** section of the **Admin** panel.
  2. Turn on the **Marketplace** setting. This setting is enabled by default.
  3. Optionally, enable the **Auto Install** setting. When enabled, this setting causes some Looker-built applications to install and update automatically on your Looker instance.
  4. Optionally, enable the **Auto Update Looker applications** setting. When enabled, this setting causes some Looker-built applications to update automatically on your Looker instance.


See the Admin settings – Marketplace documentation page for more information on these settings.
Some Marketplace content requires additional features to be enabled. To install extensions, a Looker admin must follow these steps:
  1. Navigate to the **Extension Framework** page in the **Platform** section of the **Admin** panel.
  2. Turn on the **Extension Framework** setting. When enabled, this setting allows developers to build and run Looker-hosted applications as well as install and run extensions from the Looker Marketplace, such as the Data Dictionary.


See the **Admin settings – Extension Framework** documentation page for more information on this setting.
## Discovering Looker Marketplace content
You can browse content on the Looker Marketplace by selecting the **Marketplace** storefront on the Looker menu bar. (If you have the `develop`, `manage_models`, and `deploy` permissions, selecting **Marketplace** will open a menu of options; select **Discover**.)
To find content, use the search bar. You can use the **Applications** , **Models** , **Visualizations** , and **All** filters that appear near the search bar to filter for different types of content. Narrow your results by tag, category, industry, and author using the filter checkboxes on the left side.
Next, you can install the selected tool.
## Installing a tool from the Marketplace that is associated with your instance
The installation process varies depending on the tool you are installing. Applications and some models, for example, have the option to connect the tool to your source database. The following procedure shows all the possible installation options; however, depending on the tool you are installing, you may only see a subset of the following steps.
To install a tool from the Looker Marketplace, follow these steps:
  1. Make sure you have at least the `develop`, `manage_models`, and `deploy` permissions.
  2. From the Marketplace main menu, select the tool that you want to install, and then select its tile.
Looker displays the tool's installation page, which shows a short description of the tool and any needed information about installing and using the tool.
  3. Select **Install** or **Install Free Trial**.
  4. Looker displays pages asking you to accept the tool's license agreements and the Looker permissions that are required by the tool. If you want to accept the license agreements and permission requests, select **Accept** on these pages.
  5. Each tool requires some configuration information that is specific for that tool, such as a connection name or visualization label. Select or enter the configuration information, and then select **Install**. (After the installation is complete, you can change this configuration information at any time by using the **Manage** page.)
  6. Looker will complete the installation. You can now use the installed content.


See the Customizing Looker Marketplace Blocks documentation for information on customizing **Models** or Blocks that you have installed from the Marketplace.
### Automatically installing Looker-built applications
If your Looker admin has enabled the **Auto Install** option in the **Marketplace** page in the **Platform** section of Looker's **Admin** menu, some Looker-built applications will automatically install and update on your Looker instance. The API Explorer is the only extension that will automatically install, but more Looker-built applications may be added in the future.
For more information, see the Admin settings - Marketplace documentation page.
## Installing a tool from a Git URL
To install models and plug-ins directly from the Git repository, follow these steps:
  1. Select the **Marketplace** button on the Looker menu bar storefront.
  2. From the Marketplace menu, select the **Manage** option.
  3. On the **Manage** page, select the three-dot **Options** button more_vert.
  4. Click the **Install via Git URL** button.
  5. Looker shows the **Install via Git** page. Enter the URL and commit SHA of the repository and the version of the tool or visualization that you want to install.
  6. Select **Install**.


## Installing a tool from the Marketplace instance
To install a tool from the Marketplace instance, perform the following steps:
  1. Navigate to the Looker Marketplace Directory.
  2. Select an action, application, Block, or plug-in.
  3. Select **See Code** and navigate to the tool's `READ.ME` file.
  4. Follow the `READ.ME` file's installation instructions.


## Using Looker Marketplace content
Installed Marketplace content appears in the following places of a Looker instance:
  * Applications or extensions are listed in the **Applications** menu
  * Models or Blocks are listed in the **Blocks** menu — users will be able to access only the installed packages that are based on the models to which they have been granted access permissions
    * Any Explores built for the tool appear in Looker's **Explore** menu prepended with **Marketplace**
    * The tool's LookML appears in the **Develop** menu prepended with `marketplace_`
  * Visualizations or plug-ins appear in the **Visualization** menu in an Explore


See the Customizing Looker Marketplace Blocks documentation for information on customizing the blocks that you have installed from the Marketplace.
## Managing installed tools
If you have at least the `develop`, `manage_models`, and `deploy` permissions, you can use the **Manage** page to manage the tools that are installed on your Looker instance.
To navigate to the **Manage** page, follow these steps:
  1. Select the **Marketplace** button on the Looker menu bar storefront.
  2. From the Marketplace menu, select the **Manage** option.


The **Manage** page displays a list of all tools installed on your Looker instance. From the **Manage** page, you can also update tools, open tools, change a tool's configuration, or uninstall tools.
## Related resources
  * Customizing Looker Marketplace Blocks
  * Developing a custom visualization for the Looker Marketplace


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


