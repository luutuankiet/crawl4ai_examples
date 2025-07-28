# Creating required filters with LookML  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/creating-required-filters-with-lookml

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Creating filters that users can change
  * Creating filters that users cannot change
  * Preventing users from filtering on a field




Was this helpful?
Send feedback 
#  Creating required filters with LookML
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Creating filters that users can change
  * Creating filters that users cannot change
  * Preventing users from filtering on a field


You can help curate the filter experience for your users by specifying filter behavior directly in your LookML. For example, you can add helpful filters that most users would expect to use on an Explore, or you can add a default filter to minimize the risk of queries straining your database resources.
This page provides an overview of each LookML parameter that affects filtering for all users.
## Creating filters that users can change
This table lists LookML parameters that set visible Explore-level filters for all users. Users can see the filters and change the values of the filters while exploring and viewing Looks, but they cannot remove the filters. These filters also apply to dashboards, although users cannot see or change the values of the filters from the dashboard unless you also create a dashboard filter.
LookML parameter | Scope | Visible to users? | Editable by users? | Description  
---|---|---|---|---  
Explore | Yes | Yes | Use the `always_filter` LookML parameter to set an Explore-level filter for all users. Users can see the filter and change its default value, but they cannot remove it from the Explore.  
`conditionally_filter` | Explore | Yes | Yes | Use the `conditionally_filter` LookML parameter to set an Explore-level filter for all users. Similar to `always_filter`, users can see the filter and change its default value. However, in contrast to `always_filter`, users can remove a filter that is specified with `conditionally_filter` if a specific field is filtered on instead.  
## Creating filters that users cannot change
This table lists LookML parameters that set hidden Explore-level filters for all users. Users cannot change the filter conditions, and the filtering is applied in the SQL of each query. These filters also apply to Looks and dashboards.
LookML parameter | Scope | Visible to users? | Editable by users? | Description  
---|---|---|---|---  
Explore | Sometimes | No | Use the `sql_always_where` LookML parameter to set an Explore-level query restriction into the `WHERE` clause of all SQL queries generated from the Explore. Users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL.  
Explore | Sometimes | No | Use the `sql_always_having` LookML parameter to set an Explore-level query restriction into the `HAVING` clause of all SQL queries generated from the Explore. As with `sql_always_where`, users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL.  
Join | Sometimes | No | Use the `sql_where` LookML parameter to set an Explore-level query restriction into the `WHERE` clause of all SQL queries generated from the Explore when the specified join is included in the query. As with `sql_always_where`, users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL.  
Explore | Sometimes | No | Use the `access_filter` LookML parameter to set an Explore-level, user-specific query restriction into the `WHERE` clause of all SQL queries generated from the Explore. As with `sql_always_where`, users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL. However, in contrast to `sql_always_where`, the filter condition is determined by each user's user attribute values.  
## Preventing users from filtering on a field
This table lists LookML parameters that prevent individual fields from being filtered on.
LookML parameter | Scope | Visible to users? | Editable by users? | Description  
---|---|---|---|---  
Field | Yes | No | Use the `can_filter` LookML parameter to specify whether a field can be filtered on. To prevent filtering on a field, add the line `can_filter: no` to that field. This also prevents the field from being filtered on in drill menus.  
Field | Yes | No | Use the `skip_drill_filter` LookML parameter to specify whether a field can be filtered on in drill menus. To prevent filtering on a field in drill menus, add the line `skip_drill_filter: yes` to that field. The field will still be filterable in other locations.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


