# create_process  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-create-process

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to consider
    * ${SQL_TABLE_NAME} substitution operator
    * Use sql_create to create a PDT in one step
    * Tables defined with create_process can't be used for incremental PDTs




Was this helpful?
Send feedback 
#  create_process
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to consider
    * ${SQL_TABLE_NAME} substitution operator
    * Use sql_create to create a PDT in one step
    * Tables defined with create_process can't be used for incremental PDTs


## Usage
See more code actions.
Light code theme
Dark code theme
```
derived_table: {
  create_process: {
    sql_step:
      CREATE TABLE ${SQL_TABLE_NAME}
      (customer_id int(11),
      lifetime_orders int(11)) ;;
    sql_step:
      INSERT INTO ${SQL_TABLE_NAME}
      (customer_id,
      lifetime_orders)
      SELECT customer_id, COUNT(*)
      AS lifetime_orders
      FROM order
      GROUP BY customer_id ;;
  }
}

```

Hierarchy `create_process` |  Default Value NoneAccepts One or more `sql_step` subparameters   
---|---  
## Definition
If your database dialect uses custom Data Definition Language (DDL) commands, you can use `create_process` to create persistent derived tables (PDTs). `create_process` defines a list of SQL statements that will be executed in the order listed. Each individual SQL statement is specified using the `sql_step` subparameter. Each `sql_step` subparameter can include any legal SQL query. You can define multiple `sql_step` subparameters, and they will be executed one at a time, in the order they are specified. Looker issues the statements in the `sql_step` subparameters as is, without Looker's usual error correction.
For example, some database dialects don't support `CREATE TABLE as SELECT` issued as a single SQL statement; they require separate SQL statements. As a result, traditional SQL-based persistent derived tables can't be created on these dialects. The `create_process` parameter provides an alternate way to create PDTs, by creating a list of separate SQL statements that are issued in sequence.
You can also use `create_process` to support dialects such as the Google predictive BigQuery ML machine learning models.
The `create_process` parameter indicates that you are writing the full `CREATE` statements for the derived table, including any indexes. To add an index for a derived table with `create_process`, use a `sql_step` parameter to specify the SQL for the index.
> For PDTs defined using `create_process`, you cannot use any of the following parameters: 
## Example
Create a `ctasless_customer_order_facts` persistent derived table on a MySQL database in two steps. First, issue the `CREATE TABLE` SQL statement, defined by the first `sql_step` subparameter. Second, issue the `INSERT INTO` SQL statement with a `SELECT` statement, defined by the second `sql_step` subparameter:
```
view: ctasless_customer_order_facts {
  derived_table: {
    datagroup_trigger: some_datagroup
    create_process: {
      sql_step: CREATE TABLE ${SQL_TABLE_NAME} (
                         customer_id int(11),
                         lifetime_orders int(11)
                       ) ;;
      sql_step: INSERT INTO ${SQL_TABLE_NAME}(customer_id, lifetime_orders)
                        SELECT customer_id, COUNT(*) AS lifetime_orders
                         FROM order
                         GROUP BY customer_id ;;
    }
  }
}

```

## Things to consider
###  `${SQL_TABLE_NAME}` substitution operator
You can use the `${SQL_TABLE_NAME}` substitution operator to substitute in the computed name of the PDT being created. This ensures the SQL statement will correctly include the PDT name given in the LookML `view` parameter.
> `create_process` must create a table with the name indicated by the `${SQL_TABLE_NAME}` substitution operator, or it will be rebuilt from scratch on every trigger check interval that is specified in a connection's **Datagroup and PDT Maintenance Schedule** setting (the default is five minutes). This can cause unexpected query traffic on your database or data warehouse.
### Use `sql_create` to create a PDT in one step
If your database dialect requires custom DDL commands, and you want to create a PDT in a single step, you can use `sql_create` to define a full `SQL CREATE` statement to execute and create a PDT in a single step.
### Tables defined with `create_process` can't be used for incremental PDTs
To be used as an incremental PDT, a SQL-based PDT must have a query defined using the `sql` parameter. SQL-based PDTs that are defined with the `sql_create` parameter or the `create_process` parameter cannot be incrementally built.
This is because Looker uses an INSERT or a MERGE command to create the increments for an incremental PDT. The derived table cannot be defined using custom Data Definition Language (DDL) statements, since Looker wouldn't be able to determine which DDL statements would be required to create an accurate increment.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


