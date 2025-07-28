# Sharing data from URLs  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sharing-urls

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Sharing a query's URL
  * Sharing a dashboard's URL




Was this helpful?
Send feedback 
#  Sharing data from URLs
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Sharing a query's URL
  * Sharing a dashboard's URL


From within Looker, you can grab any one of a series of URLs with which other Looker users or users outside your Looker instance can open a query or Look. To send data from Looker to other destinations outside Looker, you can publish a Look with a public URL and then send and share the URL through one of the methods described on this page.
## Sharing a query's URL
After you've run a query, you can share the query's URL with another Looker user. They will arrive at the same query and visualization, if any.
When sharing URLs, keep the following things in mind:
  * When you share a URL with someone, you are sharing the _query_ , not the actual _data_. This means that the data could change between the time you pull a query and the time your colleague runs a query. For example, if you set up a query to look at "today," the data might change if the user accesses the URL the day after you send it.
  * The URLs never expire and can't be revoked. However, since the link works only for someone who has access to your Looker instance and that data, sending a link should not cause a security concern.


### Browser URL
The easiest way to share a URL is to copy it from your browser's URL bar.
### Short URL
Sometimes it's preferable to share a shorter URL when you want to direct a colleague to your Explore query. To do so, select the gear drop-down near the upper right of the page, select **Share** , and then copy the **Short URL** :
The **Short URL** contains the Explore slug. A slug is a randomly chosen short string that takes the place of the content ID value in a URL. For example, in this short URL, `https://docserver.cloud.looker.com/x/79WcoBSRqh8YVglvYe6mHL`, the string `79WcoBSRqh8YVglvYe6mHL` is the slug.
### Expanded URL
The **Share URLs** window also provides the **Expanded URL** option. An expanded URL shows all the details for the query, including fields and filters. This information can be useful for developers who want to modify a parameterized URL. This is often useful in a custom LookML field or an external tool.
## Sharing a dashboard's URL
Selecting the **Get link** option from the dashboard's three-dot menu reveals a pop-up that contains a link to the dashboard, which can be copied and shared.
By default, the **Include current filter values in URL** switch is enabled, and the link contains the URL parameters for the filter values as they currently appear on the dashboard. This means that if you have temporarily changed the filter values away from the default values, the link displays the dashboard with the changed filter values. If you have not temporarily changed any filter values, the link displays the dashboard with default filter values. The link also displays any cross-filters that are currently applied to the dashboard, if cross-filtering is enabled.
You can also view the dashboard slug by selecting **Get link**. The slug is a randomly chosen short string that takes the place of the content ID value in a URL. For example, in this dashboard URL, `https://docserver.cloud.looker.com/dashboards/CQ1fu99Z9Y1ggq2wcHDfMm`, the string `CQ1fu99Z9Y1ggq2wcHDfMm` is the slug.
If you disable the **Include current filter values in URL** switch, the pop-up contains a shorter link, which displays the dashboard with default filter values and no cross-filters applied.
To view the dashboard, anyone with the link must have access to the Looker instance on which the dashboard is saved, as well as access to the dashboard and models that the tiles are based on.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


