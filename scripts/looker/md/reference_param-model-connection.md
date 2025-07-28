# connection  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-connection

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * connection must reference a connection name from Looker's admin settings
    * If a model configuration exists, then connection can only reference an allowed connection
    * If a model configuration does not exist, then only certain people can query




Was this helpful?
Send feedback 
#  connection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * connection must reference a connection name from Looker's admin settings
    * If a model configuration exists, then connection can only reference an allowed connection
    * If a model configuration does not exist, then only certain people can query


## Usage
See more code actions.
Light code theme
Dark code theme
```

connection: "connection_name"

```

Hierarchy `connection` |  Default Value NoneAccepts A string containing the name of a connection   
---|---  
## Definition
`connection` specifies the database connection from which a model will retrieve data. Database connections are defined and named on the **Connections** page in the **Database** section of Looker's **Admin** panel.
When a Looker developer defines a connection in a model file using the `connection` parameter, the Looker IDE displays a drop-down that suggests database connections that are available on the instance.
## Example
In the `ecommerce.model.lookml` file, specify that the model should retrieve data from the `ecommerce_events` connection:
```
connection: "ecommerce_events"

```

## Common challenges
###  `connection` must reference a connection name from Looker's admin settings
The connection name that is referenced by `connection` does not take the name of an actual database or schema. The name must be one of the connections that is available when you're configuring a model or on the **Connections** page in Looker's **Admin** panel.
### If a model configuration exists, then `connection` can only reference an allowed connection
If a Looker developer specifies a connection in the model file that is not allowed in the model configuration, then any query on that model will not run.
### If a model configuration does not exist, then only certain people can query
If you have not been given the `manage_models` permission (which is included in the admin role) then the model must be configured before you can run queries on the model.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


