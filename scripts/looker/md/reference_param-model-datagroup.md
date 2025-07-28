# datagroup  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-datagroup

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Definition
    * interval_trigger
    * label and description
  * Examples
    * Creating a caching policy to retrieve new results whenever there's new data available or at least every 24 hours
    * Creating a datagroup to schedule deliveries on the last day of every month
    * Using a datagroup with cascading PDTs
    * Sharing datagroups across model files




Was this helpful?
Send feedback 
#  datagroup
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Definition
    * interval_trigger
    * label and description
  * Examples
    * Creating a caching policy to retrieve new results whenever there's new data available or at least every 24 hours
    * Creating a datagroup to schedule deliveries on the last day of every month
    * Using a datagroup with cascading PDTs
    * Sharing datagroups across model files


## Usage
```
datagroup: datagroup_name {
  max_cache_age: "24 hours"
  sql_trigger: SELECT max(id) FROM my_tablename ;;
  interval_trigger: "12 hours"
  label: "desired label"
  description: "description string"
}

```

Hierarchy `datagroup` |  Default Value NoneAccepts An identifier for your datagroup, plus sub-parameters defining your datagroup properties.   
---|---  
## Definition
Use `datagroup` to assign a caching policy for Explores and/or to specify a persistence strategy for persistent derived tables (PDTs). If you want multiple policies for different Explores and PDTs, then use a separate `datagroup` parameter to specify each policy.
Provide a unique name for the datagroup using only letters, numbers and underscores. No other characters are allowed.
You can add a label and a description for the datagroup:
  * `label`: Specifies an optional label for the datagroup. See the `label` and `description` section on this page for details.
  * `description`: Specifies an optional description for the datagroup that can be used to explain the datagroup's purpose and mechanism. See the `label` and `description` section on this page for details.


Specify the details of the caching and persistence policy by using the `datagroup` subparameters:
  * `max_cache_age`: Specifies a string that defines a time period. When the age of a query's cache exceeds the time period, Looker invalidates the cache. The next time the query is issued, Looker sends the query to the database for fresh results. See the `max_cache_age` section on this page for details.
  * `sql_trigger`: Specifies a SQL query that returns one row with one column. If the value returned by the query is different than the query's prior results, then the datagroup goes into a triggered state. See the `sql_trigger` section on this page for details.
  * `interval_trigger`: Specifies a time schedule for triggering the datagroup, such as `"24 hours"`. See the `interval_trigger` section on this page for details.


Often the best solution is to use `max_cache_age` in combination with either `sql_trigger` or `interval_trigger`. Specify either a `sql_trigger` or an `interval_trigger` value that matches the data load (ETL) into your database, then specify a `max_cache_age` value that will invalidate old data if your ETL fails. The `max_cache_age` parameter ensures that if the cache for a datagroup isn't cleared by `sql_trigger` or `interval_trigger`, then the cache entries will expire by a certain time. That way, the failure mode for a datagroup will be to query the database rather than serve stale data from the Looker cache.
> A datagroup cannot have both `sql_trigger` and `interval_trigger` parameters. If you define a datagroup with both parameters, the datagroup will use the `interval_trigger` value and ignore the `sql_trigger` value, since the `sql_trigger` parameter requires using database resources when querying the database.
> For connections using user attributes to specify the connection parameters, you must create a separate connection using the PDT override fields if you want to define a datagroup caching policy using a SQL query trigger.
> `max_cache_age`, not `sql_trigger`.
### `max_cache_age`
The `max_cache_age` parameter specifies a string containing an integer followed by "seconds", "minutes", or "hours". This time period is the maximum time period for the cached results to be used by Explore queries that use the datagroup.
When the age of a query's cache exceeds the `max_cache_age`, Looker invalidates the cache. The next time the query is issued, Looker sends the query to the database for fresh results. See the Caching queries documentation page for information on how long data is stored in the cache.
The `max_cache_age` parameter defines only when the cache is invalidated; it does not trigger the rebuilding of PDTs. If you define a datagroup with only `max_cache_age`, you will get a LookML validation warning if any derived tables are assigned to the datagroup. If you leave a derived table assigned to a datagroup with only a `max_cache_age` parameter, the derived table will be built when the table is first queried, but the derived table will sit in the scratch schema indefinitely and never rebuild, even if it is queried again. If your intention is to have a PDT rebuild at a specific time interval, you should add a `interval_trigger` parameter to your datagroup to define a PDT rebuild schedule.
### `sql_trigger`
Use the `sql_trigger` parameter to specify a SQL query that returns exactly one row with one column. Looker runs the SQL query at intervals specified in the **Datagroup and PDT Maintenance Schedule** field of the database connection. If the query returns a different value than the previous result, the datagroup goes into a triggered state. Once the datagroup is triggered, Looker rebuilds any PDTs with that datagroup specified in their `datagroup_trigger` parameter. After the PDT rebuilding is complete, the datagroup goes into a ready state and Looker invalidates the cached results of any Explores using that datagroup.
Typically, `sql_trigger` specifies a SQL query that indicates when a new data load (ETL) has occurred, for example by querying the `max(ID)` in a table. You can also use `sql_trigger` to specify a certain time of day by querying the current date and adding additional hours to that timestamp as needed to reach the time you want, for example 4 AM.
Note the following important points about `sql_trigger`:
  * You cannot use `sql_trigger` if your database connection uses OAuth or user attributes and you have disabled PDTs for the connection. This is because Looker needs static credentials to access your database to run the query specified in the `sql_trigger` parameter. When PDTs are enabled, you can use the **PDT Overrides** fields to provide Looker with separate, static login credentials for PDT processes, even if your connection uses dynamic credentials such as OAuth or user attributes. But with PDTs disabled, if your connection uses OAuth or user attributes, you cannot provide Looker with the static user credentials that are required for `sql_trigger` queries.
  * Looker does not perform time zone conversion for `sql_trigger`. If you want to trigger your datagroup at a specific time of day, set the trigger in the time zone for which your database is configured.


See these examples from the `sql_trigger` parameter documentation for ideas about setting up SQL queries to trigger a datagroup.
### `interval_trigger`
You can use the optional `interval_trigger` subparameter to specify a time duration for rebuilding. In the `interval_trigger` parameter you pass a string containing an integer followed by "seconds", "minutes", or "hours".
###  `label` and `description`
You can use the optional `label` and `description` subparameters to add a customized label and a description of the datagroup. You can also localize these subparameters using locale strings files.
These subparameters are displayed on the **Datagroups** page in the **Database** section of the **Admin** panel. See the Admin settings - Datagroups documentation page for more information on how these are displayed.
## Examples
The following examples highlight the use cases of `datagroup`, including:
  * Creating a caching policy to retrieve new results
  * Creating a datagroup to schedule deliveries on the last day of every month
  * Using a datagroup with cascading PDTs
  * Sharing datagroups across model files


### Creating a caching policy to retrieve new results whenever there's new data available or at least every 24 hours
To create a caching policy that retrieves new results whenever there's new data available or at least every 24 hours, do the following:
  * Use the `orders_datagroup` datagroup (in the model file) to name the caching policy.
  * Use the `sql_trigger` parameter to specify the query that indicates that there is fresh data: `select max(id) from my_tablename`. Whenever the data has been updated, this query returns a new number.
  * Use the `max_cache_age` setting to invalidate the data if it has been cached for 24 hours.
  * Use the optional `label` and `description` parameters to add a customized label and a description of the datagroup.

```
datagroup: orders_datagroup {
  sql_trigger: SELECT max(id) FROM my_tablename ;;
  max_cache_age: "24 hours"
  label: "ETL ID added"
  description: "Triggered when new ID is added to ETL log"
}

```

To use the `orders_datagroup` caching policy as the default for Explores in a model, use the `persist_with` parameter at the model level, and specify the `orders_datagroup`:
```
persist_with: orders_datagroup

```

To use the `orders_datagroup` caching policy for a specific Explore, add the `persist_with` parameter under the `explore` parameter, and specify the `orders_datagroup`. If there is a default datagroup specified at the model level, you can use the `persist_with` parameter under an `explore` to override the default setting.
```
explore: customer_facts {
  persist_with: orders_datagroup
  ...
}

```

To use the `orders_datagroup` datagroup caching policy for rebuilding a PDT, you can add `datagroup_trigger` under the `derived_table` parameter, and specify the `orders_datagroup`:
```
view: customer_order_facts {
  derived_table: {
    datagroup_trigger: orders_datagroup
    ...
  }
}

```

### Creating a datagroup to schedule deliveries on the last day of every month
You may want to create a schedule that sends a content delivery at the end of every month. However, not all months have the same number of days. You can create a datagroup to trigger content deliveries at the end of every month — regardless of the number of days in a specific month.
  1. Create a datagroup using a SQL statement to trigger at the end of each month:
```
datagroup: month_end_datagroup {
sql_trigger: SELECT (EXTRACT(MONTH FROM DATEADD( day, 1, GETDATE()))) ;;
description: "Triggered on the last day of each month"
}

```

> This example is in Redshift SQL and may require slight adaptations for different databases.
This SQL statement returns the month that tomorrow is in — on the last day of the month, tomorrow is next month — so the datagroup will be triggered. For every other day, tomorrow is in the same month, so the datagroup is not triggered.
  2. Select the datagroup in a new or an existing schedule.


Schedules that are based on datagroups send only after the regeneration process has completed for all PDTs that are persisted with that datagroup parameter, ensuring that your delivery includes the latest data.
### Using a datagroup with cascading PDTs
In the case of persistent cascading derived tables, where one persistent derived table (PDT) is referenced in the definition of another, you can use a datagroup to specify a persistence strategy for the chain of cascading PDTs.
For example, here is part of a model file that defines a datagroup called `user_facts_etl` and an Explore called `user_stuff`. The `user_stuff` Explore persists with the `user_facts_etl` datagroup:
```
datagroup: user_facts_etl {
  sql_trigger: SELECT max(ID) FROM etl_jobs ;;
}

explore: user_stuff {
  persist_with: user_facts_etl
  from: user_facts_pdt_1
  join: user_facts_pdt_2 {
    ...
  }
  ...
}

```

The `user_stuff` Explore joins the `user_facts_pdt_1` view with the `user_facts_pdt_2` view. Both of these views are based on PDTs that use the `user_facts_etl` datagroup as a persistence trigger. The `user_facts_pdt_2` derived table references the `user_facts_pdt_1` derived table, so these are cascading PDTs. Here is some of the LookML from the view files for these PDTs:
```
view: user_facts_pdt_1 {
  derived_table: {
    datagroup_trigger: user_facts_etl
    explore_source: users {
      column: customer_ID {field:users.id}
      column: city {field:users.city}
      ...
    }
  }
}

view: user_facts_pdt_2 {
  derived_table: {
    sql:
      SELECT ...
      FROM ${users_facts_pdt_1.SQL_TABLE_NAME} ;;
  datagroup_trigger: user_facts_etl
  }
}

```

> If you have cascading PDTs, you must ensure that the PDTs don't have incompatible datagroup caching policies.
The Looker regenerator checks the status and initiates rebuilds of these PDTs as follows:
  * By default, the Looker regenerator checks the datagroup's `sql_trigger` query every five minutes (your Looker admin can specify this interval using the **Datagroup and PDT Maintenance Schedule** setting on your database connection).
  * If the value returned by the `sql_trigger` query is different from the result of the query in the prior check, the datagroup goes into the triggered state. In this example, if the `etl_jobs` table has a new `ID` value, the `user_facts_etl` datagroup is triggered.
  * Once the `user_facts_etl` datagroup is triggered, the Looker regenerator rebuilds all the PDTs that use the datagroup (in other words, all the PDTs that are defined with `datagroup_trigger: user_facts_etl`). In this example, the regenerator rebuilds `user_facts_pdt_1`, and then rebuilds `user_facts_pdt_2`.
> When PDTs share the same `datagroup_trigger`, the regenerator rebuilds the PDTs in order of dependency, first building tables that are referenced by other tables. See the Derived tables in Looker documentation page for more information on how Looker rebuilds cascading derived tables.
  * When the regenerator rebuilds all the PDTs in the datagroup, the regenerator takes the `user_facts_etl` datagroup out of the triggered state.
  * Once the `user_facts_etl` datagroup is no longer in the triggered state, Looker resets the cache for all models and Explores that use the `user_facts_etl` datagroup (in other words, all models and Explores that are defined with `persist_with: user_facts_etl`). In this example, that means that Looker resets the cache for the `user_stuff` Explore.
  * Any scheduled content deliveries that are based on the `user_facts_etl` datagroup will be sent. In this example, if there is a scheduled delivery that includes a query from the `user_stuff` Explore, the scheduled query will be retrieved from the database for fresh results.


### Sharing datagroups across model files
This example shows how to share datagroups with multiple model files. This approach is advantageous in that, should you need to edit a datagroup, you need to edit the datagroup in only one place to have those changes take affect across all your models.
To share datagroups with multiple model files, first create a separate file that contains only the datagroups, and then use the `include` parameter to `include` the datagroups file in your model files.
#### Creating a datagroups file
Create a separate `.lkml` file to contain your datagroups. You can create a `.lkml` datagroup file in the same way you can create a separate `.lkml` Explore file.
In this example, the datagroups file is named `datagroups.lkml`:
```
datagroup: daily {
 max_cache_age: "24 hours"
 sql_trigger: SELECT CURRENT_DATE();;
}

```

#### Including the datagroups file in your model files
Now that you've created the datagroups file, you can `include` it in both of your models and use `persist_with`, either to apply the datagroup to individual Explores in your models or to apply the datagroup to all Explores in a model.
For example, the following two model files both `include` the `datagroups.lkml` file.
This file is named `ecommerce.model.lkml`. The `daily` datagroup is used at the `explore` level so that it applies just to the `orders` Explore:
```
include: "datagroups.lkml"

connection: "database1"

explore: orders {
  persist_with: daily
}

```

This next file is named `inventory.model.lkml`. The `daily` datagroup is used at the `model` level so that it applies to all of the Explores in the model file:
```
include: "datagroups.lkml"
connection: "database2"
persist_with: daily

explore: items {
}

explore: products {
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


