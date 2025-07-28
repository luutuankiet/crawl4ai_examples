# sql_create  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-sql-create

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to consider
    * ${SQL_TABLE_NAME} substitution operator
    * Use create_process to create a PDT in multiple steps
    * Tables defined with sql_create can't be used for incremental PDTs




Was this helpful?
Send feedback 
#  sql_create
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to consider
    * ${SQL_TABLE_NAME} substitution operator
    * Use create_process to create a PDT in multiple steps
    * Tables defined with sql_create can't be used for incremental PDTs


## Usage
See more code actions.
Light code theme
Dark code theme
```
derived_table: customer_order_facts {
  sql_create: {
      SQL statement ;;
  }
}

```

Hierarchy `sql_create` |  Default Value NoneAccepts A SQL statement   
---|---  
## Definition
`sql_create` enables custom Data Definition Language (DDL) commands for building persistent derived tables (PDTs). `sql_create` will issue a statement as is, without Looker's usual error checking. The only requirement is that the statement results in the creation and execution of a PDT. This lets you, for example, create PDTs that support the Google BigQuery ML machine learning models.
> For PDTs defined using `sql_create`, you cannot use any of the following parameters: 
## Examples
Create a PDT for BigQuery ML queries that predict likelihood of future purchases:
```
view: future_purchase_model {
  derived_table: {
    datagroup_trigger: bqml_datagroup
    sql_create:
      CREATE OR REPLACE MODEL ${SQL_TABLE_NAME}
      OPTIONS(model_type='logistic_reg'
        , labels=['will_purchase_in_future']
        , min_rel_progress = 0.005
        , max_iterations = 40
        ) AS
      SELECT
         * EXCEPT(fullVisitorId, visitId)
      FROM ${training_input.SQL_TABLE_NAME};;
  }
}

```

## Things to consider
###  `${SQL_TABLE_NAME}` substitution operator
You can use the `${SQL_TABLE_NAME}` substitution operator to substitute in the computed name of the PDT being created. This ensures the SQL statement will correctly include the PDT name given in the LookML `view` parameter.
> `sql_create` must create a table with the name indicated by the `${SQL_TABLE_NAME}` substitution operator, or it will be rebuilt from scratch on every trigger check interval specified in a connection's **PDT and Datagroup Maintenance Schedule** setting (the default is five minutes). This can cause unexpected query traffic on your database or data warehouse.
### Use `create_process` to create a PDT in multiple steps
If your database dialect requires custom DDL commands, and you want to issue multiple commands to create a PDT, you can use `create_process` to issue multiple custom DDL commands in a specific order.
### Tables defined with `sql_create` can't be used for incremental PDTs
To be used as an incremental PDT, a SQL-based PDT must have a query defined using the `sql` parameter. SQL-based PDTs that are defined with the `sql_create` parameter or the `create_process` parameter cannot be incrementally built.
This is because Looker uses an INSERT or a MERGE command to create the increments for an incremental PDT. The derived table cannot be defined using custom Data Definition Language (DDL) statements, since Looker wouldn't be able to determine which DDL statements would be required to create an accurate increment.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


