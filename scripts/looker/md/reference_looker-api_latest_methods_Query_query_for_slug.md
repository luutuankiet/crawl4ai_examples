# Get Query for Slug  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/query_for_slug

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get the query for a given query slug.




Was this helpful?
Send feedback 
#  Get Query for Slug
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get the query for a given query slug.


Version 4.0.25.10 (latest) 
### Get the query for a given query slug.
This returns the query for the 'slug' in a query share URL.
The 'slug' is a randomly chosen short string that is used as an alternative to the query's id value for use in URLs etc. This method exists as a convenience to help you use the API to 'find' queries that have been created using the Looker UI.
You can use the Looker explore page to build a query and then choose the 'Share' option to show the share url for the query. Share urls generally look something like 'https://looker.yourcompany/x/vwGSbfc'. The trailing 'vwGSbfc' is the share slug. You can pass that string to this api method to get details about the query. Those details include the 'id' that you can use to run the query. Or, you can copy the query body (perhaps with your own modification) and use that as the basis to make/run new queries.
This will also work with slugs from Looker explore urls like 'https://looker.yourcompany/explore/ecommerce/orders?qid=aogBgL6o3cKK1jN3RoZl5s'. In this case 'aogBgL6o3cKK1jN3RoZl5s' is the slug.
## Request
GET /queries/slug/{slug} 
Datatype
Description
Request
HTTP Request 
path
HTTP Path 
Expand HTTP Path definition... 
slug
string 
Slug of query
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
id
_lock_
string 
Unique Id
model
string 
Model
view
string 
Explore Name
fields
string[] 
pivots
string[] 
fill_fields
string[] 
filters
object 
Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.
filter_expression
string 
Filter Expression
sorts
string[] 
limit
string 
Row limit. To download unlimited results, set the limit to -1 (negative one).
column_limit
string 
Column Limit
total
boolean 
Total
row_total
string 
Raw Total
subtotals
string[] 
vis_config
object 
Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.
filter_config
object 
The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.
visible_ui_sections
string 
Visible UI Sections
slug
_lock_
string 
Slug
dynamic_fields
string 
Dynamic Fields
client_id
string 
Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.
share_url
_lock_
string 
Share Url
expanded_share_url
_lock_
string 
Expanded Share Url
url
_lock_
string 
Expanded Url
query_timezone
string 
Query Timezone
has_table_calculations
_lock_
boolean 
Has Table Calculations
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


