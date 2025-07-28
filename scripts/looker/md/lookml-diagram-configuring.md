# Configuring the LookML Diagram  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/lookml-diagram-configuring

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling required features
  * Installing the LookML Diagram
  * Granting permissions to use the LookML Diagram




Was this helpful?
Send feedback 
#  Configuring the LookML Diagram
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling required features
  * Installing the LookML Diagram
  * Granting permissions to use the LookML Diagram


The LookML Diagram is an extension — a web application built using Looker components — developed using the Looker extension framework and deployed through the Looker Marketplace. This documentation page describes the tasks that Looker admins must complete before Looker users can access and use the extension, including:
  1. Enable the appropriate features.
  2. Install the LookML Diagram extension.
  3. Grant permissions to access the LookML Diagram.


## Enabling required features
Before installing the LookML Diagram from the Marketplace, Looker admins must enable these features:
  * **Marketplace**: To access the Looker Marketplace (enabled by default)
  * **Extension Framework**: To deploy extensions developed using the Looker extension framework (enabled by default)


## Installing the LookML Diagram
Installing applications and tools — such as extensions — from the Marketplace requires `develop`, `manage_models`, and `deploy` permissions.
The LookML Diagram extension is listed in the **Applications** section of the Looker Marketplace. See the Using the Looker Marketplace documentation page for more detailed instructions on installing a tool from the Looker Marketplace.
After you've installed the extension, you can ensure that you always have the most updated version by going to the Looker Marketplace, clicking **Manage** , and clicking the **Update** button next to the extension.
## Granting permissions to use the LookML Diagram
After the LookML Diagram is installed, a model called `lookml-diagram` is automatically added to the list of available models on the **New Model Set** and **Edit Model Set** pages, accessible from the **Roles** page in the **Admin** panel.
Looker admins must enable users to perform certain tasks with the LookML Diagram extension by granting permissions to the `lookml-diagram` model and any models the user needs to work with in the LookML Diagram. To enjoy full functionality of the LookML Diagram, users must have `explore` and `deploy` permissions. Refer to the following table for details.
Permission | Depends on | Extension capabilities  
---|---|---  
None | Users can navigate to the extension but won't be able to interact with it.  
`see_looks`, `access_data` | Users can view and interact with the diagram and can access Explores. **Go to LookML** links are visible but not functional. Users cannot switch or select Git branches in the **Diagram Settings** panel.  
`see_lookml`, `see_looks`, `access_data` | Users can interact with the diagram and can access LookML project files. **Explore from Field** links are visible but the user is directed to a page that they are not authorized to access. Users cannot switch or select Git branches in the **Diagram Settings** panel.  
`develop`, `see_lookml`, `see_looks`, `access_data` | The same as with `develop` except that users _can_ switch or select Git branches in the **Diagram Settings** panel. Users can use the extension while in Development Mode.  
See the Setting permissions for Looker extensions documentation page for more information on granting users permissions to access and use extensions.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


