# Admin settings - Visualizations  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-platform-visualizations

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing a list of custom visualizations
  * Sourcing a custom visualization
  * Adding a new custom visualization
  * Editing a custom visualization
  * Deleting a custom visualization




Was this helpful?
Send feedback 
#  Admin settings - Visualizations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing a list of custom visualizations
  * Sourcing a custom visualization
  * Adding a new custom visualization
  * Editing a custom visualization
  * Deleting a custom visualization


Looker includes a robust list of built-in visualization types, letting you chart your data in a variety of ways. If you need a type of chart that is not included in Looker's built-in visualization types, Looker provides several ways to add custom JavaScript visualizations to your Looker instance:
  1. Add a `visualization` parameter to your LookML project's manifest file to add custom visualizations directly to your LookML project. See the `visualization` parameter documentation page for more information.
  2. Install a visualization from the Looker Marketplace. With the **Marketplace** feature enabled, you can install Looker Marketplace visualization packages.
  3. Use the **Visualizations** page in the **Platform** section of Looker's **Admin** menu to install and administer custom JavaScript visualizations from Looker's custom visualizations repository.


This page describes how to add custom JavaScript visualizations using the **Visualizations** page in the Looker **Admin** panel.
## Viewing a list of custom visualizations
To obtain full functionality of downloaded visualizations, admins for customer-hosted deployments should make sure to install the appropriate version of the Chromium renderer.
The **Visualizations** page in the **Platform** section of Looker's **Admin** menu lists all the custom visualizations that have been added to your Looker instance.
The list includes the following columns:
  * **ID** : The unique ID assigned to the custom visualization. This value is assigned either in the JavaScript code, or when you add or edit a visualization using the **Admin** page, or in the visualization's parameter when you add a visualization using the LookML project manifest file.
  * **Label** : The name given to the visualization type in the Looker visualization menu. This value is assigned when you add or edit a visualization using the Admin page, or in the visualization's `label` parameter when you add a visualization using the LookML project manifest file.
  * **Main** : The URI of the visualization's main JavaScript code. This value is assigned when you add or edit a visualization using the Admin page, or in the visualization's `url` parameter when you add a visualization using the LookML project manifest file.
  * **Actions** : Buttons to edit or delete the visualization configuration. These buttons are not shown for visualizations added using the LookML project's manifest file. To edit these visualizations, go to the LookML project's manifest file and edit the `visualization` parameter directly.


## Sourcing a custom visualization
You can obtain visualizations to customize and add to your Looker instance from a variety of sources, including the following:
  * Looker maintains a library of custom visualizations for public use on this Looker GitHub page. You can find instructions for using Looker's Visualization API to create your own visualization types on this Looker GitHub page.
  * The standalone Looker Marketplace, where you can browse for visualizations — called "plug-ins" — and access their source code.
  * The Looker Marketplace that is accessible from your Looker instance. From this Marketplace, you can browse and install visualizations directly into your Looker instance. See the Using the Looker Marketplace documentation page for more information about installing visualizations from the Looker Marketplace.


## Adding a new custom visualization
Once you know which visualization you'd like to add to your instance, you can use the The **Visualizations** page in the **Platform** section of Looker's **Admin** menu to add a custom visualization by selecting the **Add Visualization** button.
Looker displays the **New Visualization:** page. To add a new visualization, perform the following steps:
  1. In the **ID** field, enter the unique ID of the visualization defined in the visualization JavaScript.
  2. In the **Label** field, enter the name of the visualization. Looker displays this name in the Looker visualization menu on an Explore.
  3. In the **Main** field, enter the URI of the visualization's main JavaScript file to point Looker to your JavaScript code repository.
  4. If the site that hosts your custom visualization code uses a subresource integrity (SRI) hash for verification purposes, enter the SRI hash in the **SRI Hash** field. This field can be found under **Advanced options**. Looker's custom visualization hosts don't use an SRI hash.
  5. In the **Dependencies** field, enter the URIs of any other files that the visualization JavaScript is dependent upon, and click **Add**. You can enter multiple URIs separated by commas, or you can add multiple URIs one at a time. The **Dependencies** field can be found under **Advanced options**.
  6. Select **Save**.


Once the visualization has been added, you will see it as you've labeled it in the visualization menu in an Explore. You can use the new visualization type like any of Looker's existing visualization types.
To view custom visualizations from the visualization menu:
  1. Select the **`...`**three-dot icon from thevisualization menu bar to access the custom visualization.
  2. Once the visualization is selected, the name of the visualization appears on the visualization menu bar.


## Editing a custom visualization
To edit an existing visualization, select the **Edit** button to the right of the visualization. Looker displays the same page that you use to add a visualization (described in Adding a new custom visualization), but with the relevant information already filled in. Make any preferred changes, and then click **Save**.
## Deleting a custom visualization
To delete a visualization, select the **Delete** button to the right of the visualization on the **Visualizations** page in the **Platform** section of Looker's **Admin** menu, and then click **OK** in the confirmation box.
Deleting a visualization removes it from Looker but won't affect anything in the visualization's external code repository.
Deleting a visualization disables any Looks or dashboards that use that visualization type. You can correct that by adding back the deleted visualization with the same visualization ID.
## Troubleshooting
Custom visualizations are a community-supported effort. Looker's support team does not troubleshoot issues relating to custom visualizations or your custom visualization code. For tracking and closing out bugs, use GitHub issues in the custom visualization's repository, or visit the Looker Community for how-to posts, conversations, and tips regarding custom visualizations.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


