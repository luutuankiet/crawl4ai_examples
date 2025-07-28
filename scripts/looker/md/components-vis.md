# Looker visualization components  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/components-vis

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Creating visualizations with Looker visualization components
  * Why use visualization components?
  * Installing visualization components




Was this helpful?
Send feedback 
#  Looker visualization components
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Creating visualizations with Looker visualization components
  * Why use visualization components?
  * Installing visualization components


Looker visualization components are a suite of React-based components that are available in the open source `@looker/visualizations` package.
Visualization components accept a `Query.client_id` value or a query ID from a Looker Explore or a dashboard ID from a Looker dashboard and render a client-side visualization without an iframe.
These components can be used out of the box, customized, or treated as pure data formatters to pass cleaned data from a Looker Explore to facilitate building your own customized visualizations.
Looker visualization components are designed to be used in a React environment that has been authenticated with Looker's API using the TypeScript/JavaScript SDK. That step is handled automatically when you build with the Looker extension framework.
## Creating visualizations with Looker visualization components
Looker's visualization components suite provides two high-level components for working with your data:
  * `Query` — Handles the data fetching and loads the response into React context
  * `Visualization` — Accepts the data that is returned by `Query` and uses configuration adapters to render the appropriately customized chart on a page


Currently, data can be rendered as the following chart types:
  * Line
  * Area
  * Scatter
  * Sparkline
  * Single value
  * Bar
  * Column
  * Table
  * Pie


More chart types are in development.
To view the property tables for each chart type, visit the Visualization and Query property tables documentation page.
To view the available configuration options for each chart type, view the visualization playground.
## Why use visualization components?
Visualization components improve and simplify the process of rendering a visualization from Looker within an application, free up developer time, and give developers more options to customize and extend their visualizations from Looker.
  * **Improved embedding** — Visualization components allow developers to embed a Looker visualization in an application without an iframe. This can improve performance, monitoring, and the ability to customize.
  * **Easy integration** — Visualization components can then be combined with other components from `@looker/components` to create entirely new compositions and front-end experiences.
  * **Customization** — It is easier to customize embedded visualizations when using visualization components than when using iframes. Additionally, with visualization components, developers can create highly customized applications much faster, without having to create a visualization layer from scratch.
  * **Simplification** — Visualization components improve the portability of Looker visualizations and simplify interactions with the Looker API.


## Installing visualization components
To get started, add the Looker Visualization Components NPM package:
  * **NPM:** `npm install @looker/visualizations`
  * **YARN:** `yarn add @looker/visualizations`


You'll also need to satisfy a few peer dependencies — Looker/components, React, and Styled Components:
  * **NPM:** `npm install @looker/components react react-dom styled-components`
  * **YARN:** `yarn add @looker/components react react-dom styled-components`


Information on installing and using the visualization components package can be found in the README document, available in GitHub and NPM.
## Next steps
  * Using visualization components and the `dashboard` property to render a simple visualization
  * Using visualization components to render custom visualizations
  * Using visualization components to build a custom visualization
  * Visualization and Query property tables


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


