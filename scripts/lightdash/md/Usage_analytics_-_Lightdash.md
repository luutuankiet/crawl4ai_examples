# Usage analytics - Lightdash

**Source:** https://docs.lightdash.com/references/usage-analytics

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Reference
Usage analytics
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference
    * Roles and permissions
    * Personal access tokens


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Usage analytics dashboards
  * User Activity dashboard


There are two ways of understanding user activity:
  1. **Usage Analytics dashboards** - these are dashboards created by Lightdash which give you an overview of your project’s content and user activity.
  2. **Query tags** - this is metadata which is added to your data warehouse queries and gives you information about who is querying data and what they are querying.


##  Usage analytics dashboards
Each project has usage analytics dashboards created by Lightdash giving you an overview of your project’s content and user activity. To see your usage analytics dashboards for a project, just click on the `settings` icon, `project settings`, then `usage analytics`. Or you can also use our search bar to get direct access to the different analytics dashboards by typing the name of the dashboard (eg: User activity)
###  User Activity dashboard
This dashboard gives you an overview of the users in your project and the activity of your users. Here’s an overview of the fields used in the dashboard:
  * **Number of users** : the total number of users that have access to the project.
  * **Number of viewers** : the number of users with the `viewer` role that have access to the project.
  * **Number of editors** : the number of users with the `editor` role that have access to the project.
  * **Number of admins** : the number of users with the `admin` role that have access to the project.
  * **% of weekly querying users** : the % of users which have run at least one query in the project in the last 7 days (out of all users in your project). Queries include viewing existing charts and dashboards.
  * **Number of weekly querying users** : the number of users which have run at least one query in the project in the last 7 days.
  * **Weekly average number of queries per user** : the rolling 7 day average number of queries that each user is running in your project.
  * **Users that have run the most queries in the last 7 days** : a list of the users that have run the most queries in your project in the last 7 days.
  * **Users that have updated the most charts in the last 7 days** : a list of users that have updated (including created) the most charts in the project in the last 7 days.
  * **Users that have not run a query in the last 90 days** : a list of users that have not run a query in the project in the last 7 days. This includes viewing charts and dashboards.


##  Query tags
Query tags are metadata which is added to your data warehouse queries and gives you information about each query executed. The following query tags are sent: Query Tag | Detail  
---|---  
organization_uuid | Lightdash organization unique identifier.  
project_uuid | Lightdash project unique identifier.  
user_uuid | User unique identifier.  
dashboard_uuid | Dashboard unique identifier.  
chart_uuid | Chart unique identifier.  
explore_name | Name of the explore.  
query_context | Which context the query was executed in. For queries in: - dashboards use `dashboardView` - explore use `exploreView`- chart use `chartView`- sql chart use `sqlChartView`  
Query tags are stored differently in each data warehouse: Data Warehouse | Query Tag  
---|---  
BigQuery | Persists in the labels parameter in your job history.  
Snowflake | Persists in the comment parameter in your query history.  
Trino | Appends to the SQL in your query history.  
Redshift | Appends to the SQL in your query history.  
Databricks | Appends to the SQL in your query history.  
Postgres | Appends to the SQL in your query history.  
Customizing the appearance of your projectRoles and permissions
Assistant
Responses are generated using AI and may contain mistakes.


