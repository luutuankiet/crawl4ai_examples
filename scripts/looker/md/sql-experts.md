# LookML for SQL experts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/sql-experts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Related resources




Was this helpful?
Send feedback 
#  LookML for SQL experts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Related resources


This guide provides a focused introduction to LookML, Looker's modeling language, and is specifically intended for those who are already proficient in SQL.
LookML lets you define SQL logic in a structured and reusable way. From the SQL fragments defined in your LookML, Looker assembles relevant SQL statements. Once you've set up your LookML model and connected Looker to your database, Looker automatically generates the necessary SQL queries to retrieve data from your database.
Because you use LookML to define your SQL, you don't need to repeat SQL logic in multiple places. LookML helps you adhere to the "Don't Repeat Yourself (DRY)" principle, a key concept in programming that promotes code reusability and reduces errors. For example, imagine that you need to decode transaction codes by using a SQL `CASE` statement across multiple queries. Instead of declaring the `CASE` statement in multiple queries, you can define it once in LookML and reuse it throughout your data model.
In this guide, you'll deconstruct SQL queries and reassemble them into reusable LookML elements such as dimensions, measures, views, and Explores.
The following pages explain LookML elements by using concepts familiar to SQL experts:
  * SQL concepts for views: Define and customize LookML views, which are based on database tables, and map your SQL fields to LookML dimensions and measures.
  * SQL concepts for joins: Define and customize joins between views in LookML to mirror SQL join logic, and manage relationships between tables to avoid data duplication.
  * SQL concepts for derived tables: Define and customize derived tables in LookML by using either SQL or LookML's built-in syntax to define and reuse complex data logic without repeating yourself.


## Related resources
  * Using Looker's SQL Generator (Community article)
  * How Looker generates SQL
  * Looker cookbook: Maximizing code reusability with DRY LookML


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


