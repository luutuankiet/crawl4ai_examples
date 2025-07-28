# persist_for (for Explores)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-persist-for

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Things to consider
    * persist_for does not necessarily align with your data import
    * Scheduled Looks will cache results




Send feedback 
#  persist_for (for Explores)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Things to consider
    * persist_for does not necessarily align with your data import
    * Scheduled Looks will cache results


> This page refers to the `persist_for` parameter that is part of an Explore.
> `persist_for` can also be used as part of a model, described on the `persist_for` (for models) parameter documentation page.
> `persist_for` can also be used as part of a derived table, described on the `persist_for` (for derived tables) parameter documentation page.
## Usage
```

explore: explore_name {
  persist_for: "1 hour"
}

```

Hierarchy `persist_for` |  Default Value The `persist_for` setting of the modelAccepts A string containing an integer followed by a timeframe (seconds, minutes, or hours)Special Rules A `persist_for` setting at the `explore` level will override the `persist_for` setting at the model level   
---|---  
## Definition
> For more robust cache management, including synchronizing your Looker cache policy to your database's ETL (extract, transform, and load) process, consider using a `datagroup` and `persist_with`, as described on the Caching queries documentation page.
`persist_for` lets you modify the amount of time that cached query results are used for a given Explore. The default cache length in Looker is 1 hour. Cache results are stored in an encrypted file on your Looker instance.
The caching mechanism in Looker works as follows: Once a user runs a specific query, the result of that query is cached. If precisely the same query (_everything_ must be the same, including things such as the row limits, etc.) is run again, in less than the interval specified by `persist_for`, the cached results are returned. Otherwise, a new query is run against your database.
When the `persist_for` interval expires, data is deleted from the cache. See the Caching queries documentation page for information on how long data is stored in the cache.
If `persist_for` is set for both an Explore and its model, the value set for the Explore will take priority for queries based on that Explore.
> From an Explore, you can see whether a query was returned from cache or you can force new results to be generated from the database. See the Caching queries documentation page for more information.
## Examples
Adjust the cache length to 2 hours:
```
explore: my_explore {
  persist_for: "2 hours"
}

```

Adjust the cache length to 30 minutes:
```
explore: my_explore {
  persist_for: "30 minutes"
}

```

Turn off caching so that users never get cached results for a query:
```
explore: my_explore {
  persist_for: "0 seconds"
}

```

## Things to consider
When `persist_for` is set to `0 seconds`, your users' queries will not retrieve data from the cache. However, Looker requires the disk cache for internal processes, so your encrypted data will always be written to the cache, even when `persist_for` is set to `0 seconds`. Once written to the cache, the data will be flagged for deletion but may live up to 10 minutes on disk. See the Caching queries documentation page for details.
###  `persist_for` does not necessarily align with your data import
Many companies have a daily data import to their analytics database. Sometimes, they reason that there is no purpose running fresh queries if the data isn't constantly updated anyway, so they set the cache length to 24 hours (like `persist_for: 24 hours`). However, this will not prevent users from getting data that is older than the most recent refresh.
For example, a query is run at noon on January 1st, new data is imported the morning of January 2nd, and then the query is run again at noon on January 2nd. Since the query was run within the 24 hour window specified by `persist_for`, the data from January 1st will be returned, even though new data was loaded on January 2nd.
> If you want your caching to be aligned with data imports, use a datagroup and `persist_with`, as described in the documentation on caching queries.
### Scheduled Looks will cache results
When a scheduled Look is run, it creates a cached result set in the same way that a user run query would. To precache a certain Look, consider saving and scheduling it.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


