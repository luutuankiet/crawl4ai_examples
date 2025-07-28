# How Looker integrates with Google  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-google-integrations

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Gmail/Google mail
  * Google Ads Customer Match
  * Google Analytics
    * Google Analytics 4
    * Google Analytics 360
    * Google Analytics Data Import
  * Google authentication
  * Google Authenticator mobile app
  * Google Sheets
    * Exporting to Google Sheets
    * Sending to Google Sheets with the Looker Action Hub
  * Check back for updates!




Was this helpful?
Send feedback 
#  How Looker integrates with Google
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Gmail/Google mail
  * Google Ads Customer Match
  * Google Analytics
    * Google Analytics 4
    * Google Analytics 360
    * Google Analytics Data Import
  * Google authentication
  * Google Authenticator mobile app
  * Google Sheets
    * Exporting to Google Sheets
    * Sending to Google Sheets with the Looker Action Hub
  * Check back for updates!


Looker is a Google Cloud product that offers integrations with several Google products and services. These Looker connections maximize opportunities for customizing your Google ecosystem and let you customize everything from your user authentication to how you import and export data. This guide lists all the Google products and services that Looker integrates with and describes the benefits of the integrations for Looker and Google users alike. The following sections describe how Looker integrates with each Google product or service:
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Cloud Storage
  * Gmail/Google mail
  * Google Ads Customer Match
  * Google Analytics
  * Google authentication
  * Google Authenticator mobile app
  * Google Sheets


## BigQuery
Looker can connect to both the BigQuery Standard SQL and the BigQuery Legacy SQL databases for scalable and flexible data exploration. Key features of this connection include machine learning, query cost estimator, and nested tables. To learn more about features of the BigQuery integration with Looker and how to set up the connection, see the documentation on connecting Looker to Google BigQuery.
## Spanner
Spanner, an externalized version of the database service Spanner for Google Cloud users, now integrates with Looker. Through Spanner, you can utilize product features of the database, such as symmetric aggregates, derived tables, and location type. To acquire connection credentials for Spanner and access the complete list of supported features, see the documentation on connecting Looker to Google Spanner.
## Cloud SQL for MySQL
Cloud SQL for MySQL is another relational database service that integrates with Looker. Benefits of Cloud SQL for MySQL include integration with existing apps and Google Cloud services, like BigQuery. For detailed instructions about connecting the database, see the documentation on connecting Looker to Google Cloud SQL for MySQL.
## Cloud SQL for PostgreSQL
Cloud SQL for PostgreSQL is a SQL database dialect that integrates with Looker. This dialect shares database setup requirements with other PostgreSQL dialects. With Cloud SQL for PostgreSQL, you can include features such as the following:
  * Symmetric aggregates


For a complete list of supported features in Cloud SQL for PostgreSQL, see the documentation on connecting Looker to PostgreSQL.
## Cloud Storage
Through reliable and secure object storage, Cloud Storage manages and retrieves stored data. This cloud technology also deploys data at a faster rate compared to on-premises environments. Through the Looker Action Hub, you can send Looker content and data snapchats directly to your Cloud Storage account. Looker admins can enable the Cloud Storage integration through the **Actions Page** in the the Looker **Admin** panel. Learn more about this action through the Send to Google Cloud Storage Marketplace article.
## Gmail/Google mail
Through email, Looker instances not only send account notifications and password resetting options but also Looker-generated content like dashboards and Looks. You can modify Looker's default Simple Mail Transfer Protocol (SMTP) settings from the Looker **Admin** panel. Custom mail settings can be configured for SMTP servers that support the PLAIN and LOGIN authentication protocols, including the Google proprietary email service, Gmail. With custom SMTP servers, you can preview and curate delivery settings through sending test emails and modifying the "From" sender. These custom servers also allow for greater network control. For custom SMTP setup specifics, see the How to set up a custom Gmail/Google mail SMTP settings Community post.
## Google Ads Customer Match
**This integration requires Looker 7.4 or later.**
Google Ads, Google's personalized advertising creation platform, integrates with Looker. Once Google Ads has been enabled through the Looker **Admin** panel and you've authenticated with your Google credentials, you can send Looker insights directly to Google Ads to create data-driven advertising. To learn more about setting up this connection, see the Looker integration: Google Ads Customer Match Best Practices page.
## Google Analytics
The Google Analytics platform provides information about user interaction, web traffic, and site functionality. You can use Looker to model and visualize the collected data and distribute it to select audiences. You can also use data-driven decisions to build marketing, advertising, and design initiatives. To connect Google Analytics and Looker, choose one of the following connection methods, based on what would work best with your analytic goals:
  * Google Analytics 4
  * Google Analytics 360
  * Google Analytics Data Import


### Google Analytics 4
Google Analytics 4 is an analytics service that lets you measure traffic and engagement across your websites and apps. Google Analytics 4 is available for instances with the Marketplace feature enabled and connected to BigQuery databases. Through Looker Blocks, Google Analytics 4 enables further customization of data collected for in-depth and specific analysis. With Google Analytics 4, even individuals without Google Analytics access can view reports that are generated through collaboration with Looker.
### Google Analytics 360
Through the Google Analytics 360 Looker Block, Looker accesses Google Analytics information to visualize and analyze user and site data. The premium offering of this block enables further customization of Google Analytics data in Looker, such as curating goals and strategizing techniques for further user engagement. Google Analytics 360 is available for instances with the Marketplace feature enabled and connected to BigQuery databases.
### Google Analytics Data Import
A Looker admin must enable the Google Analytics Data Import action through the Looker Action Hub. This action combines existing user information in Looker and imports it to the Google Analytics platform. This import feature connects the data collection and analysis structure of Google analytics with the modeling layer and self-service analytics of Looker. After enablement, users can select **Send** in the Scheduler to upload data.
## Google authentication
Looker offers users the option to authenticate to a Looker instance using their Google Workspace account and Google OAuth authentication. Enabled through the Looker **Admin** panel, Google OAuth provides a simple way to authenticate your Looker users, prioritizing both usability and security. For more information about enabling Google OAuth, see the Google authentication documentation page.
## Google Authenticator mobile app
Looker's integration with the Google Authenticator app provides an additional layer of security when you log in to the Google ecosystem. Admins can enable two-factor authentication (2FA), allowing you to connect the Authenticator app to your Looker account. With 2FA enabled, every user who logs in must authenticate with a one-time code generated by their mobile device. For more details about setting up the Google Authenticator app, see the Two-factor authentication documentation page.
## Google Drive
**This integration requires Looker 7.4 or later and Google OAuth authentication when delivering content.**
Google Drive, a cloud-based storage platform, integrates with Looker through the Looker Action Hub. This integration leverages Google OAuth authentication to enable you to share Looks, Explores, and dashboards to folders and Drives associated with your Google Drive account. The collaborative nature of Google Drive allows for sharing of your Looker-generated content to a wide audience. For more information about enabling the Google Drive action in Looker through the Looker **Admin** panel, see the Looker Actions - Google Drive Best Practices page.
## Google Maps
**This integration requires Looker 22.12 or later.**
Google Maps connects to Looker as an available visualization type. This visualization shows interactive geographic data with options to customize the map settings and styles. This includes chart settings like Density Heatmaps and Automagic Heatmaps, which can be added through the **Plot** menu. The **Plot** menu also includes options for customizing the map with points, lines, and areas. To see a complete list of chart options and learn more about this integration, see the Google Maps chart options documentation page.
## Google Sheets
In Looker, there are multiple methods of connecting with Google Sheets, Google's spreadsheet editor. This includes connecting to Looker from within Google Sheets using the Connected Sheets feature, exporting content to Google Sheets, and sending Looks and Explores to Google Sheets. To find a connection that works best with your Looker content and Google Sheets usage, select one of the following methods:
  * Using Connected Sheets for Looker
  * Exporting to Google Sheets
  * Sending to Google Sheets with the Looker Action Hub


### Exporting to Google Sheets
You can send data directly from Looker to Google Sheets by pasting the Google Spreadsheet formula, generated by a Look, into a cell. This method requires an admin to enable **Public URLs** in the **General Settings** page. To learn more about this process, see the Exporting to Google Sheets section on the **Public sharing, importing, and embedding of Looks** documentation page.
### Sending to Google Sheets with the Looker Action Hub
**This integration requires Looker 7.4 or later and Google OAuth authentication when delivering content.**
Through the Looker Action Hub, and secured by Google OAuth, you can send Looks and Explores directly to Google Sheets. You can enable the Google Sheets action through the Looker **Admin** panel. For more information about enabling the sending to Google Sheets Action in Looker, see the Looker actions - Google Sheets Best Practices page.
## Check back for updates!
We are focused on continuing to explore opportunities to integrate more Google products and services with Looker to take advantage of the strengths of both platforms. These integrated products and services will offer enhanced customization, access, and security. This page will be updated as more Looker/Google integrated products and services are released.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


