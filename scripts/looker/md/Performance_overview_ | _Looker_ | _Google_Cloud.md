# Performance overview  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-performance

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Component overview
  * Classifying slowness
  * Contact Looker Support




Was this helpful?
Send feedback 
#  Performance overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Component overview
  * Classifying slowness
  * Contact Looker Support


This page outlines the basic components that contribute to Looker's performance. This page is intended to outline basic Looker performance concepts so that you can find relevant resources and effectively communicate with Looker Support about your performance issues. This is not a troubleshooting guide, as every performance issue is specific. 
> If you are experiencing performance issues, contact Looker Support. Contact details are located in the last section of this page. 
## Component overview
At a basic level, Looker is a program running on a server. Looker uses the memory and CPU of that server to run. Every company that uses Looker has their own dedicated server or cluster — there is no "global" Looker server. When you log in to Looker from your browser, the browser sends requests to your server for information. The server returns the desired information, and your browser renders it for you. 
Looker also connects to your database. In this case, the Looker server requests information from the database and the database returns that information to the server. 
### Example:
When you go to your personal folder in Looker to open and interact with a dashboard, this is what happens behind the scenes: 
  1. You select the link that you expect will open your personal folder page. 
  2. Your browser asks your Looker server for information about that folder: "Are there Looks, dashboards, or other folders in here?" 
  3. Your Looker server returns that information to your browser: "Yes, there is dashboard A, which contains Looks 1 and 2." 
  4. Your browser displays the contents of your folder. 
  5. You select dashboard A. 
  6. Your browser asks the Looker server for info about dashboard A, which includes Look-linked tiles to Looks 1 and 2. 
  7. Your Looker server generates the SQL queries needed for Look 1 and 2 and sends them to your database. 
  8. Your database returns the result sets for those queries to your Looker server. 
  9. Your Looker server sends the data it received from those queries to your browser. 
  10. Your browser renders the dashboard using the data it received from your server. 


## Classifying slowness
There are three major elements described in the preceding example: your database, your Looker server, and your browser. Each contributes to Looker performance and executes a series of processes to deliver your data. The following four elements can impact the efficiency of the database, server, and browser processes: 
  * Database load 
  * Instance load 
  * Browser load 
  * Network latency 


These processes and their potential impact on performance are discussed in the following sections. 
### Database load
It takes time for a database to process a SQL query, especially if a query is large or if the database is processing several queries at once. If an Explore, a Look, or a dashboard is taking a long time to return results, the reason could be that the query is slow or that there are several queries running at once. You can check the **Queries** page in the **Admin** menu — or your database console — to get a better idea of your database's load at any given time. 
### Instance load
Your Looker server — commonly referred to as your _Looker instance_ — serves visualizations and pages for everyone who uses the instance. The level of usage at any given time can potentially strain instance resources. If the instance is under a heavy load, a simple non-query processing task — such as navigating folders — may take a while to load. 
### Browser load
Finally, your browser displays the data that Looker serves. The amount of data modern browsers can render is limited. It's possible to crash a browser just by opening an Explore with a large amount of data in it. 
Browser load for Looker content can be roughly measured as (`amount of data per cell`) * (`number of rows`) * (`number of columns`). It is possible for a large query to be fast — and for your instance to serve the results of the query quickly — but your browser may take a long time to render the results or may crash. In this example, only users that opened the large query would be impacted. No other pages in Looker would be affected. For browser performance, 50 or fewer columns is recommended. 
### Network latency
Because Looker is a web application, every Looker interaction sends and retrieves information through the internet. A poor internet network connection impacts your database, your instance, and your browser. You can confirm that you may be experiencing network latency either by consulting with a colleague who uses Looker on a different network or by asking Looker Support to visit the same page on your instance. 
## Contact Looker Support
Now that you have an idea of the basic performance concepts in Looker, you can perform a high-level investigation as to the cause of performance issues on your instance; then reach out to your Looker contact or Looker Support. When you contact Looker Support, please be as specific as possible and let us know which instance pages are slow and at what times the slowdown occurs. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


