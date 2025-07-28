# Understanding PDT log actions  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/pdt-log-actions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing PDT log actions
  * Understanding PDT log actions and their corresponding PDT log action data pairs
    * Regenerate events
    * Drop and publish task events
    * Datagroup trigger events




Was this helpful?
Send feedback 
#  Understanding PDT log actions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing PDT log actions
  * Understanding PDT log actions and their corresponding PDT log action data pairs
    * Regenerate events
    * Drop and publish task events
    * Datagroup trigger events


The **PDT Event Log** Explore in System Activity provides information about historical events related to PDTs, including PDT rebuilds and errors.
For example, the **PDT Event Log** Explore can help you troubleshoot PDT build failures or stuck triggers, or it can be useful when you are trying to identify when a specific table was built and what process built it.
For more information about the Explores available in System Activity, see the Monitoring Looker usage with System Activity Explores documentation page.
## Viewing PDT log actions
PDT log actions are visible in the System Activity **PDT Event Log** Explore. You must be a Looker admin or have the `see_system_activity` permission to view the **PDT Event Log** Explore.
To view a list of PDT log actions and their associated log action data, select the **Action** and **Action Data** fields, along with any other desired fields, from the **PDT Event Log** view in the **PDT Event Log** Explore, which you can navigate to from the **Explore** menu.
## Understanding PDT log actions and their corresponding PDT log action data pairs
The following tables break down the different log actions in the **PDT Event Log** Explore, along with the corresponding data values for each log action, for the following types of events:
  * Drop and publish task
  * Datagroup trigger


The following tables use **Action** and **Action Data** fields in the **PDT Event Log** view of the **PDT Event Log** Explore.
### Create events
Log Action | Log Action Description | Log Action Data | Log Action Data Description  
---|---|---|---  
`create begin` | Occurs when the regenerator thread has picked up the PDT. | `prod-user-x` | Indicates that the user queried the PDT from the Explore and the table didn't exist, so Looker has had to rebuild the PDT.  
`create begin` | Occurs when the regenerator thread has picked up the PDT. | `prod` | Indicates that the PDT was triggered by a datagroup or SQL trigger (built by the regenerator).  
`create begin` | Occurs when the regenerator thread has picked up the PDT. | `dev-user-x` | Indicates that a new Development Mode PDT has been built.  
`create regen requires` | Typically indicates that a user has queried a PDT that references another PDT that hasn't been built yet, triggering a rebuild. | `null`  
`create user rebuild` | Indicates that a user has manually rebuilt the PDT using the **Rebuild Derived Tables & Run** option in an Explore. | `null`  
`create ready` | Once the PDT actually begins building, the difference between the `create ready` event and the `create begin` event indicates the amount of time it takes for children to rebuild.`create ready` event occurs right after the `create begin` event, then it is likely that no tables needed to be rebuilt. | `null`  
`create complete` | Occurs when the PDT has finished building. | `production trigger` | Indicates that the PDT has been built because of a trigger check (that is, the PDT has been built by the regenerator).  
`create incremental complete` | Occurs when the PDT has finished building (for incremental PDT builds). | `increment generation` | Contains the sequential number of the increment.  
`create incremental rows` | Shows the number of affected rows in the last increment. | `rows delta` | Contains a positive value for the number of rows added and a negative value for the number of rows removed.  
`create sql error` | Indicates that the PDT build has failed with a SQL error. | `sql error` | Contains the SQL error message that was returned from the database.  
`create child error` | Occurs when there has been an error while creating the dependent PDT. | `sql error` | Contains the SQL error message that was returned from the database.  
`create cancelled error` | Indicates that the PDT build has failed because of a query cancellation. | `query killed` | Indicates that the query has been killed. This can happen if a user cancels a query from Looker, if a user cancels a query from the database, or if the query times out on the database.  
`create trigger old value` | Indicates the old trigger value upon check. | `trigger value` | Returns the old trigger's returned value.  
`create trigger new value` | Indicates the new trigger value upon check. | `trigger value` | Returns the new trigger's returned value.  
`create trigger missing` | Occurs on trigger check for a given PDT when the PDT no longer exists or has been dropped. | `null`  
`create trigger datagroup` | Occurs on trigger check if the PDT was triggered by a datagroup. | `null`  
### Regenerate events
Log Action | Log Action Description | Log Action Data | Log Action Data Description  
---|---|---|---  
`regenerate begin` | Indicates that the regenerator is beginning a process, such as checking a trigger or building a table.`regenerate begin` event has no end event and a PDT is not currently being built or a trigger is not being checked, this log action indicates a hung regenerator. | `connection name` | Shows the connection name for which the regenerator thread is running.  
`regenerate end` | Indicates that the regenerator has finished a process, such as checking a trigger or rebuilding a PDT, or that an error has occurred. | `success` | Indicates that the trigger has been checked and the PDT has been rebuilt.  
`regenerate end` | Indicates that the regenerator has finished a process, such as checking a trigger or rebuilding a PDT, or that an error has occurred. | `error_in_regen` | Indicates that an error has occurred in this table regeneration cycle.  
`regenerate end` | Indicates that the regenerator has finished a process, such as checking a trigger or rebuilding a PDT, or that an error has occurred. | `datagroup_error` | Indicates that an error has occurred in checking the datagroup trigger.  
`regenerate trace` | Indicates regenerator thread tracing. | `hex id` | Represents the Java thread that is running the process.  
### Drop and publish task events
Log Action | Log Action Description | Log Action Data | Log Action Data Description  
---|---|---|---  
`drop table` | Indicates that the PDT or temp table has been dropped from the database. | `unreferenced` | Indicates that the table has been dropped because its associated trigger value has changed.  
`drop table` | Indicates that the PDT or temp table has been dropped from the database. | `zombie` | Indicates that the registration key for the table is not a part of the active registration key sets (in `connection_reg3`), so it has been marked as a zombie table to be dropped.  
`drop table` | Indicates that the PDT or temp table has been dropped from the database. | `pdt_build_failure_cleanup` | When a build fails or is detected as being canceled, Looker drops the table that may have been partially created.  
`drop table failed` | Occurs when the attempt to drop the PDT or temp table has failed. | `zombie` | Indicates that the attempt to drop the zombie table has failed.  
`drop table failed` | Occurs when the attempt to drop the PDT or temp table has failed. | `unreferenced` | Indicates that the attempt to drop the unreferenced table has failed.  
`drop view` | Indicates that the `publish_as_db_view` table has been dropped. | `expired` | Indicates that the table life length has expired, and the table has been dropped.  
`drop view failed` | Indicates that the attempt to drop the `publish_as_db_view` table has failed. | `zombie` | Indicates that the attempt to drop the `publish_as_db_view` zombie table has failed.  
`drop view failed` | Indicates that the attempt to drop the `publish_as_db_view` table has failed. | `unreferenced` | Indicates that the attempt to drop the `publish_as_db_view` unreferenced table has failed.  
`publish task complete` | Indicates that the previous view has been dropped, and the new view has been published. | X succeeded, X failed | Indicates whether the publish task succeeded or failed.  
### Datagroup trigger events
Log Action | Log Action Description | Log Action Data | Log Action Data Description  
---|---|---|---  
`datagroup_triggers begin` | Indicates that the datagroup triggers have begun checking for a connection.`datagroup_triggers begin` line for a connection and there is no `datagroup_triggers end`, this could mean that the regenerator got hung up while checking triggers. | `connection name` | Shows the connection name for which the triggers are checking.  
`datagroup_triggers end` | Indicates that the datagroup triggers have finished checking. | `null`  
### Reap events
Log Action | Log Action Description | Log Action Data | Log Action Data Description  
---|---|---|---  
`reap begin` | Indicates that the reaper has begun checking the connection to see which non-active derived tables it should drop from the scratch schema. | `connection name` | Shows the name of the connection that the reaper is checking.  
`reap end` | Indicates that the reaper has finished its cycle for the given connection. | `connection name` | Shows the name of the connection that the reaper has checked.  
### Trigger events
Log Action | Log Action Description | Log Action Data | Log Action Data Description  
---|---|---|---  
`trigger value` | Indicates the value of the trigger when computed. | `trigger value` | Shows the actual trigger value.  
`trigger value compute` | Indicates the SQL that was used to compute the trigger value. | `trigger sql` | Shows the actual SQL that was used to compute the trigger value.  
`trigger value error` | Indicates that there has been a SQL error in computing the trigger value or in running the trigger SQL. | `sql error` | Shows the database SQL error that was returned for the trigger query.  
`trigger datagroup check` | Indicates whether the regenerator ran the SQL trigger query against the database. | A Boolean (`true` or `false`) | 
* `true`: Indicates that the trigger query has been run.
* `false`: Indicates that the SQL trigger query has not been run.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


