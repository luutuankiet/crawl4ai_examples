# datagroup_trigger  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-datagroup-trigger

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges




Was this helpful?
Send feedback 
#  datagroup_trigger
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges


## Usage
See more code actions.
Light code theme
Dark code theme
```
view: my_view {
  derived_table: {
    datagroup_trigger: my_datagroup
    ...
  }
}

```

Hierarchy `datagroup_trigger` |  Default Value NoneAccepts The name of a datagroup defined in the model file   
---|---  
## Definition
`datagroup_trigger` lets you specify the datagroup to use as a caching policy for the derived table. The datagroup itself is defined in the model file using the `datagroup` parameter.
Adding the `datagroup_trigger` parameter to a derived table makes the derived table a persistent derived table (PDT). The table is written into a scratch schema on your database and regenerated as specified by the `datagroup` parameter.
If you use `datagroup_trigger` for your PDT, you don't need to use the `sql_trigger_value` or `persist_for` parameters. If you do, you will get a warning in the Looker IDE, and only the `datagroup_trigger` will be used.
## Examples
Create a persistent native derived table called `customer_orders` that is rebuilt when triggered by the datagroup named `order_datagroup`:
```
view: customer_orders {
  derived_table: {
    explore_source: order {
      column: customer_id { field: order.customer_id }
      column: lifetime_orders { field: order.lifetime_orders }
    }
    datagroup_trigger: order_datagroup
  }
}

```

Create a `customer_orders` persistent derived table based on a SQL query that is rebuilt when triggered by the datagroup called `etl_datagroup`:
```
view: customer_orders {
  derived_table: {
    sql:
      SELECT
        customer_id,
        COUNT(*) AS lifetime_orders
      FROM
        order
      GROUP BY 1 ;;
    datagroup_trigger: etl_datagroup
  }
}

```

## Common challenges
If you have PDTs that are dependent on other PDTs, be careful not to specify incompatible datagroup caching policies.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


