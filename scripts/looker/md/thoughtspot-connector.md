# Looker–ThoughtSpot BI Connector  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/thoughtspot-connector

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Looker–ThoughtSpot BI Connector
Stay organized with collections  Save and categorize content based on your preferences. 
The Looker–ThoughtSpot BI Connector lets you use Thoughtspot Cloud to connect to data from a Looker Explore. The Looker–ThoughtSpot BI Connector is built upon the Looker Open SQL Interface, which allows access to LookML models and Explores for applications that use JDBC to connect to data sources. See the Open SQL Interface documentation for more details.
## Before you begin
Your Looker instance must meet the following requirements to make use of the Looker–ThoughtSpot BI Connector:
  * Running Looker 24.14 or later.
  * Has a LookML project that uses data from a Google BigQuery connection. (The LookML project must have a model file that specifies a Google BigQuery connection in its `connection` parameter.)


The user creating the Thoughtspot connection must meet the following requirements:
  * Has a Looker user role that includes the `explore` permission on the LookML model that you want to access from Thoughtspot.
  * Use the same email address for both Looker and Thoughtspot.


See the Add a Looker connection page in the Thoughtspot documentation for additional requirements to configure and use this connector.
## Setting up ThoughtSpot authentication to your Looker instance
The Looker–ThoughtSpot BI Connector requires that you set up authentication for your Looker instance.
Although we prefer using OAuth authentication, you can also use a service account to configure authentication. To learn how to set up service account authentication, see Connecting to Looker from Thoughtspot Cloud.
### Setting up OAuth for the Looker–ThoughtSpot BI Connector
You can use the Looker API Explorer to set up OAuth integration for the Looker–ThoughtSpot BI Connector.
If your Looker instance already has API Explorer installed, you can access it with this URL format:
```
https://LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/

```

If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the Using the API Explorer page for information.
To use the API Explorer to set up OAuth integration on your Looker instance, perform the following steps:
  1. Open the Looker API Explorer (see the Using the API Explorer page for information).
  2. In the API Explorer's **Search** field, enter **Register OAuth App**.
  3. In the search results, click **Register OAuth App**.
  4. On the **Register OAuth App** page, click the **Run It** button.
  5. In the **Request** tab of the **Run It** dialog, enter the following information into the corresponding fields:
     * **client_guid** :
```
looker-thoughtspot

```

     * **body** :
```
{
  "redirect_uri": THOUGHTSPOT_INSTANCE_URL/callosum/v1/connection/generateTokens,
  "display_name": "Looker-ThoughtSpot (manual)",
  "description": "Client for Looker-ThoughtSpot integration (manually added)",
  "enabled": true,
  "group_id": ""
}

```

  6. Select the checkbox for **I understand that this API endpoint will change data.**
  7. Click **Run**.
  8. You can verify that you successfully set up authentication by using the `Get OAuth Client App` method in the API Explorer:
     * In the API Explorer's **Search** field, enter **Get OAuth Client App**.
     * Click **Run It**.
     * In the **client_guid** field, enter the value: `looker-thoughtspot`
If you set up OAuth successfully, the **Response** tab will return the values you entered when you registered the app.


## Connecting to Looker from Thoughtspot Cloud
See the Looker connector pages in the ThoughtSpot documentation to learn more about how to perform the following tasks:
  * Add a connection to Looker
  * Edit a connection to Looker
  * Edit the source mapping of a connection to Looker
  * Delete a table from a connection to Looker
  * Delete a table with dependent objects
  * Delete a connection to Looker


When performing the steps to Add a connection to Looker, use the following values to set up OAuth authentication:
  * **Host** : `LOOKER_INSTANCE_URL`
  * **OAuth Client ID** : `looker-thoughtspot`
  * **Scope** : `thoughtspot`
  * **Auth Url** : `LOOKER_INSTANCE_URL/auth`
  * **Access token Url** : `LOOKER_INSTANCE_URL/token`


When performing the steps to Add a connection to Looker, use the following values to set up service account authentication:
  * **Host** : `LOOKER_INSTANCE_URL`
  * **Password** : `API_CLIENT_SECRET_ASSOCIATED_WITH_THE_LOOKER_USER_ACCOUNT`
  * **User** : `API_CLIENT_ID_ASSOCIATED_WITH_THE_LOOKER_USER_ACCOUNT`


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


