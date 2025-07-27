# Using visualization components and the dashboard property to render a simple visualization  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/components-vis-dashboard-id

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Step 1: Build a query and add it to a dashboard
  * Step 2: Embed the query into a React application using the dashboard ID
  * Step 3: Modify the visualization if necessary




Was this helpful?
Send feedback 
#  Using visualization components and the dashboard property to render a simple visualization
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Step 1: Build a query and add it to a dashboard
  * Step 2: Embed the query into a React application using the dashboard ID
  * Step 3: Modify the visualization if necessary


Using the `dashboard` property of the `Query` visualization component allows you to render an embeddable visualization that can respond to changes to the Looker UI. Using the `dashboard` property offers the following benefits:
  * The visualization can be updated by any Looker user with edit access to the dashboard.
  * Updates to the embedded visualization don't require any changes to your deployed extension or React application.


To render an embeddable visualization using Looker visualization components and a numeric dashboard ID, make sure your setup meets the requirements, and then perform the following steps:
  1. Build a query and add it to a dashboard.
  2. Embed the query into a React application using the dashboard ID.
  3. Modify the visualization if necessary.


## Requirements
Before you start, a few elements are needed:
  * You must have access to a Looker instance.
  * Whether you're building in the extension framework or your own stand-alone React application, it is important to authenticate with Looker's API and have access to the Looker SDK object. Read about Looker API authentication or our extension framework for more information.
  * Make sure you have installed the Looker Visualization Components NPM package and the `@looker/components-data` NPM package. Information on installing and using the visualization components package can be found in the README document, available in GitHub and NPM.


## Step 1: Build a query and add it to a dashboard
Use an Explore to build a query within the Looker UI. Add a supported visualization to the Explore and, optionally, configure its settings in the visualization's **Settings** menu.
Create a new dashboard using this query. Alternatively, you can add the query to a blank dashboard that you have already created.
The `Query` component will always load the visualization from the first tile that was added chronologically to the associated dashboard, regardless of where the tile appears in the dashboard layout. For this reason it is good practice to use only single-tile dashboards as the query reference.
The `Query` component will only display the tile visualization. It will not display the tile title, dashboard title, or other dashboard elements. Any dashboard filters applied to the tile will have no effect on the embedded visualization.
Once your dashboard is created, view the dashboard.
A numeric dashboard ID appears in the dashboard URL after `dashboards/`. Copy this ID for use in the next step.
> The `dashboard` property of the `Query` component accepts only numeric IDs. It does not accept the string IDs of LookML dashboards.
## Step 2: Embed the query into a React application using the dashboard ID
Now, you can embed the query into your React application by passing the dashboard ID in the `dashboard` property of the `Query` component:
```
import React, { useContext } from 'react'
import { ExtensionContext } from '@looker/extension-sdk-react'
import { DataProvider } from '@looker/components-data'
import { Query, Visualization } from '@looker/visualizations'

export const MyReactApp = () => {
  const { core40SDK } = useContext(ExtensionContext)

export const MyReactApp = ({ sdk: core40SDK }: Props) => {
  return (
    <DataProvider sdk={core40SDK}>
      <Query dashboard={61}>
        <Visualization />
      </Query>
    </DataProvider>
  )
}

```

## Step 3: Modify the visualization if necessary
Now, any Looker users with edit access to the dashboard are free to make changes to the visualization embedded within your dashboard, and the changes will appear within your React application without requiring any changes to the code.
For edit access, users must have the **Manage Access, Edit** access level for the folder the dashboard is in, model access to the model the query is based on, and the appropriate Looker permissions to edit dashboards.
There are two ways to modify the embedded visualization:
  * Edit the query tile on the dashboard, or
  * Add a new query tile to the dashboard and delete the original tile.


To edit the query tile, follow the instructions for editing tiles on the Editing user-defined dashboards documentation page, and save your changes to exit edit mode on the dashboard.
To add a new tile and delete the original one, follow the instructions for adding query tiles to add your new tile. Then follow the instructions for deleting tiles to delete the unwanted visualization. For your changes to apply, make sure there is only one tile on your dashboard, and then save your changes to exit edit mode on the dashboard.
Once you modify and save your dashboard, the visualization changes will appear in your extension or React application without requiring any changes to the code.
## Next steps
  * Using visualization components to render custom visualizations
  * Using visualization components to build a custom visualization
  * Visualization and Query property tables


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


