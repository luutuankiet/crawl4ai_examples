# Creating connections tutorial  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/creating-connections

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * General steps for creating a connection




Was this helpful?
Send feedback 
#  Creating connections tutorial
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * General steps for creating a connection


## General steps for creating a connection
The exact steps you need to take depend on the database dialect you are using and the other choices you make. This page serves as an outline of the steps you need to take to create a connection, with links to the details you need.
The steps are:
  1. From your database administrator, get the contact details for your database such as hostname, database or schema name, username, and password.
  2. Enable secure access to your database. There are two ways to do this:
     * Using an IP address allowlist, optionally adding SSL encryption.
     * Using an SSH tunnel, which provides an encrypted connection and extra authentication. This is more secure but also is more time-consuming to set up.
  3. On your database, set it up to work with Looker. The instructions vary quite a bit from dialect to dialect. Typically the steps include adding permissions for Looker to access the database and possibly creating a scratch schema for Looker to create derived tables in the database. To see the instructions you need, go to the Looker dialects documentation page and click on your database dialect.
  4. In Looker, go to the **Admin** panel's **Connection** page. If you are in a trial, typically you won't have any connections on that page.
  5. Click **Add Connection** to set up the connection. Fill out the connection details. The majority of the settings are common to most database dialects. See the Connecting Looker to your database documentation page for information. In general, you specify the following values:
     * The name you want to use to refer to the connection
     * The database dialect
     * The connection information for reaching your database
     * Various options, including whether you'll let Looker write derived tables to the database and how you want the connection to behave
     * What time zone the database data is stored in
     * Additional JDBC connection string parameters, if needed by your database
  6. At the bottom of the **New Connections** page, click **Test** to verify the settings for Looker to reach the database. If any of the tests do not pass, try some of the troubleshooting steps on the Testing database connectivity documentation page. If you are still having trouble, double-check the database details with your database administrator, and then contact your Looker analyst or the Looker support team for assistance.
  7. When the testing is successful, click **Connect**. The connection now appears on the **Admin** panel's **Connection** page. If you are in a trial, this will be your first connection on that page.
  8. Next, it is a good practice to double-check that your connection is working properly. In Looker, use the **Develop** menu to go to SQL Runner, which lets you use a connection to do a variety of tasks such as directly typing and running SQL queries.
  9. In SQL Runner, select the name of the connection you created and the database or schema that you specified for the connection. Then check that the expected tables are listed. Clicking a table will show the columns in that table, verifying that Looker was able to use the connection to access your database tables.


You have now set up the database connection and verified that Looker can reach the database.
## Next steps
If you are in a trial, your Looker analyst typically will have performed the other project setup steps for you. If you have time before your trial kickoff meeting, consider reading through the Development Process tutorials, which begin with the Getting started developing in Looker documentation page, or consider the Looker courses on Google Cloud Skills Boost.
If you are not in a trial, the next steps for creating a new project are:
  * Creating a project to hold your data model
  * Configuring the project to accept your connection
  * Setting up and testing Git to manage changes to the data model


Then you are ready to start writing LookML and deploying your changes to production for your business users to do adhoc queries and create dashboards.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


