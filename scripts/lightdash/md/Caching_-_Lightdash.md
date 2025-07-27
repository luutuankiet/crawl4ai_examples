# Caching - Lightdash

**Source:** https://docs.lightdash.com/references/caching

Lightdash home page
Search...
⌘KAsk AI
Search...
Navigation
Reference
Caching
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
    * Lightdash CLI reference
    * Feature Maturity Levels
    * SQL Runner


##### Workspace and user management
  * Guides
  * Reference


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
  * Filter value caching
  * Chart and dashboard results caching
  * Scope of the cache
  * Cache Mechanism
  * Cache Expiry and Invalidation


Lightdash supports two types of caching:
  1. Cached Filter values - enabled for every cloud user without requiring any configuration.
  2. Cached results for Charts and Dashboards - must be enabled by the Lightdash team. This feature is only available for Pro, Enterprise, and on-prem users since it requires a dedicated Lightdash instance.


##  Filter value caching
This type of caching works without any configuration for cloud users. You’ll see a message in your filter values that tells you when the cached filter values were loaded from (usually within the last day). If you want to refresh the filter values, you can click on that message and the values will be refreshed. If you search filter values by starting to type, Lightdash will also cache those values so the next time you need the same search the values will be shown much faster.
##  Chart and dashboard results caching
Popular charts and dashboards will load faster when caching is enabled. The first user to visit a chart or dashboard each day will load fresh results from the warehouse, which get cached. After that, all following visits to the same chart or dashboard will load from the cached results. Any changes to the chart query or dashboard queries (user attributes, filters, limit, date zoom) will trigger new queries to the warehouse and create a separate cached results entry. Caching popular charts and dashboards will reduce warehouse costs to the organization by reducing the number of queries; it also improves server performance and makes the user experience much faster in Lightdash.
###  Scope of the cache
These Lightdash features use caching (if it’s enabled on your instance):
  * **Saved Charts** are cached based on the last refresh in any context (edit mode, view mode, dashboard refresh, etc.), but queries made while editing are NOT cached or pulled from cache.
  * **Dashboard tiles** (internal and embedded) will use the cache from saved charts they reference. If charts only exist on a single dashboard, they will refresh whebnever you click the Refresh button on the dashboard.
  * **Scheduled Deliveries** generate and use cached results for the saved chart or dashboard they belong to.

These Lightdash features DO NOT use caching:
  * **Creating a new query from tables or editing a saved chart** are NOT cached because they are typically one-off explorations that don’t benefit from caching.
  * **Metrics Catalog and Spotlight** do not use caching yet, but likely will in the future.
  * **Charts built in SQL runner** do not use caching.


###  Cache Mechanism
The cache is stored in S3 and the cache identifier is based on the project ID and the generated SQL. This means that any change to the selected columns, filters, joins, user attributes, etc. will trigger a new query to the warehouse and add a new cache entry for that query.
###  Cache Expiry and Invalidation
Cached results automatically expire after 24 hours. The expiry time is configurable at the organization level, but you’ll need to reach out to the Lightdash team. The dashboard header displays the date and time of the chart with the oldest cache. If no time is displayed, then no charts are cached. You can invalidate and refresh cached dashboard results by pressing the dashboard refresh button.
There is currently no way to invalidate cached results for individual Saved Charts.
SQL VariablesAdd the Slack integration
Assistant
Responses are generated using AI and may contain mistakes.


