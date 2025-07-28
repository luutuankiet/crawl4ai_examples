# Using visualization components to render custom visualizations  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/components-vis-render-custom-vis

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Adding a new chart type




Was this helpful?
Send feedback 
#  Using visualization components to render custom visualizations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Adding a new chart type


> This example renders a custom visualization that is local to an app being developed, not a custom visualization that is available from the Looker Marketplace.
Looker visualization components have an adapter system that allows developers to override existing chart types or add entirely new chart type options.
This option can be useful in the following circumstances:
  * You have built custom React visualizations that you'd like to use with Looker components.
  * You want to replace an existing default Looker visualization with a visualization that is built on a different library.


The ability to override or add charts can be especially relevant if you're building an application that allows users to change the type of chart visualization during a session.
## Background
After rendering a query in Looker's Explore interface and passing its `Query.client_id` into Looker's visualization components, you can modify the chart type by updating the `config` property's `type` property.
Each value accepted by the `type` property is mapped to a specific React component. So, when `type` is set to `line`, a `Line` component is rendered; when `type` is set to `area`, an `Area` component is rendered; and so on.
The `chartTypeMap` property of the `Visualization` component allows you to add a new entry to, or replace existing entries in, the type/component map that associates each `type` value with a particular component.
## Requirements
You must begin by importing the `DataProvider` component and providing an authenticated SDK instance. The following example is built within Looker's extension framework, and the SDK comes from `ExtensionContext`.
Within `DataProvider`, you can render the `Query` and `Visualization` components to request data from the Looker SDK and render the expected visualization within your application.
The setup is as follows (in the `query` property, replace the value with the `Query.client_id` from your query):
```
import React, { useContext } from 'react'
import { ExtensionContext } from '@looker/extension-sdk-react'
import { DataProvider } from '@looker/components-data'
import { Query, Visualization } from '@looker/visualizations'

const App = () => {
    const { core40SDK } = useContext(ExtensionContext)
    return (
        <DataProvider sdk={core40SDK}>
            <Query query="z8klgi4PJKAl7TXgTw1opS">
                <Visualization />
            </Query>
        </DataProvider>
    )
}

```

## Adding a new chart type
You can modify the rendered chart type by passing a config override to the `Query` component.
```
<Query query="z8klgi4PJKAl7TXgTw1opS" config={{ type: 'pie' }}>
    <Visualization />
</Query>

```

In this case, `type` was set to `pie`: a chart that Looker components offer by default. But what if you would like to use a chart that isn't offered by default? In that situation, you can use the `chartTypeMap` property of `Visualization` to add or replace the chart components in the type/component map in the adapter system.
If, for example, you want to add a new radar chart to the type/component map, add it to the `chartTypeMap` like this:
```
import React, { useContext } from 'react'
import { ExtensionContext } from '@looker/extension-sdk-react'
import { DataProvider } from '@looker/components-data'
import { Query, Visualization } from '@looker/visualizations'
import { MyCustomRadar } from '../MyCustomRadar'

const App = () => {
    const { core40SDK } = useContext(ExtensionContext)
    return (
        <DataProvider sdk={core40SDK}>
            <Query query="z8klgi4PJKAl7TXgTw1opS" config={{ type: 'radar'}}>
                <Visualization chartTypeMap={{ radar: MyCustomRadar }} />
            </Query>
        </DataProvider>
    )
}

```

This code does the following things:
  * Imports the `MyCustomRadar` React component
  * Assigns the `radar` key to the `config.type` property
  * Updates the `chartTypeMap` property so that the type mapping system knows what to render for a `type` of `radar`


This is how it renders in the Looker visualization playground:
Similarly, you can replace existing charts if you'd like to render your own version. In the following example, the default Looker components' line chart is overridden with a custom line chart component:
```
import React, { useContext } from 'react'
import { ExtensionContext } from '@looker/extension-sdk-react'
import { DataProvider } from '@looker/components-data'
import { Query, Visualization } from '@looker/visualizations'
import { MyCustomLine } from '../MyCustomLine'

const App = () => {
    const { core40SDK } = useContext(ExtensionContext)
    return (
        <DataProvider sdk={core40SDK}>
            <Query query="z8klgi4PJKAl7TXgTw1opS">
                <Visualization chartTypeMap={{ line: MyCustomLine }} />
            </Query>
        </DataProvider>
    )
}

```

Now, whenever the `Query` component encounters a query where the visualization type is set to `line`, it will render the custom implementation in place of the Looker default.
## Next steps
  * Using visualization components and the `dashboard` property to render a simple visualization
  * Using visualization components to build a custom visualization
  * Visualization and Query property tables


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


