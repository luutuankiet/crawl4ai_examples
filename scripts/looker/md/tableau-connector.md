# Looker–Tableau BI Connector  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/tableau-connector

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Setting up Tableau Desktop to connect to Looker
    * Tableau connector (TACO) file
    * JDBC driver (looker.jar) file
  * Connecting to Looker data from Tableau Desktop
  * Identifying Looker–Tableau BI Connector queries in the Looker UI
  * Using the Looker–Tableau BI Connector on Tableau Server
    * Before you begin
    * Set up OAuth for the Looker–Tableau BI Connector
    * Install the Looker–Tableau BI Connector on Tableau Server
    * Complete the setup on Tableau Server
  * Things to consider




Was this helpful?
Send feedback 
#  Looker–Tableau BI Connector
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Setting up Tableau Desktop to connect to Looker
    * Tableau connector (TACO) file
    * JDBC driver (looker.jar) file
  * Connecting to Looker data from Tableau Desktop
  * Identifying Looker–Tableau BI Connector queries in the Looker UI
  * Using the Looker–Tableau BI Connector on Tableau Server
    * Before you begin
    * Set up OAuth for the Looker–Tableau BI Connector
    * Install the Looker–Tableau BI Connector on Tableau Server
    * Complete the setup on Tableau Server
  * Things to consider


The Looker–Tableau BI Connector lets you use a Looker Explore as a data source in Tableau. The Looker–Tableau BI Connector is built upon the Looker Open SQL Interface, which allows access to LookML models and Explores for applications that use JDBC to connect to data sources. See the Open SQL Interface documentation for more details.
The Looker–Tableau BI Connector supports Tableau Desktop and Tableau Server, but not Tableau Cloud.
## Before you begin
Your Looker instance must meet the following requirements to make use of the Looker–Tableau BI Connector:
  * Running Looker 24.14 or later.
  * Enabled for the **Tableau Desktop** BI connector. A Looker admin must enable the **Tableau Desktop** toggle on the Looker **BI Connectors** page.
  * Contains a LookML model that uses data from a Google BigQuery connection: 
    * The LookML project must include a model that is configured with at least one Google BigQuery connection in the **Allowed Connections** field. See the Accessing and editing project information documentation page for information on configuring a model and seeing the allowed connections for the model.
    * The LookML project must have a model file that specifies a BigQuery connection in its `connection` parameter.


In addition, each person using the Looker–Tableau BI Connector must have a Looker account with a user role that includes the `explore` permission on the LookML model that they want to access from Tableau.
## Setting up Tableau Desktop to connect to Looker
Once all of the requirements are satisfied, you can set up Tableau Desktop to connect to Looker data.
Each user who wants to access the Looker–Tableau BI Connector must download the `avatica-<release_number>-looker.jar` file and the packaged Tableau connector (TACO) file, and then save the files in specific directories on their computer. The following sections provide instructions for downloading these files and where to put them on your computer:
  * Download and save the Tableau Connector (TACO) file
  * Download and save the JDBC driver (`looker.jar`) file


### Tableau connector (TACO) file
The Tableau connector file is called `looker_v1.0.0.taco`. Each user must download the TACO file and save it to their computer by using the following steps:
  1. To download the Tableau connector file, click the following link: `looker_v1.0.0.taco`
  2. When the download is completed, move the `looker_v1.0.0.taco` file to the `Connectors` subdirectory of the `My Tableau Repository` directory. Here are the default directory paths:
     * **Windows** :
```
C:\Users\\Windows user\Documents\My Tableau Repository\Connectors

```

     * **MacOS** :
```
/Users/Mac user/Documents/My Tableau Repository/Connectors

```



### JDBC driver (`looker.jar`) file
The JDBC driver is called `avatica-<release_number>-looker.jar`. Each user must download the `looker.jar` file from GitHub and save the file to their computer by following these steps:
  1. Go to https://github.com/looker-open-source/calcite-avatica/releases.
  2. Download the latest version of the `avatica-<release_number>-looker.jar` file.
  3. Save the `avatica-<release_number>-looker.jar` file to each user's computer in the following location:
     * **Windows** : `C:\Program Files\Tableau\Drivers`
     * **MacOS** : `/Library/JDBC` or `~/Library/JDBC`


## Connecting to Looker data from Tableau Desktop
After you have downloaded and saved the `looker_v1.0.0.taco` and the `avatica-<release_number>-looker.jar` files, you can use Tableau Desktop to connect to data from your Looker instance by following these steps:
  1. In Tableau Desktop, from the left-side **Connect** pane, in the **To a Server** section, select the **More...** option.
  2. In the search box, enter **Looker by Google**.
  3. Select the **Looker by Google** option.
  4. In the dialog window, enter these parameters: 
     * **Server** : Enter your Looker instance URL without the `https://`. For example: `example.cloud.looker.com`
     * **Port** : `443`
     * **Authentication** : `OAuth`
     * **OAuth Instance Url** : Enter your full Looker instance URL with the `https://`. For example: `https://example.cloud.looker.com`
  5. Select **Sign In**. Tableau will open a browser window to connect to your Looker instance and authenticate your account with OAuth.
  6. If prompted, log in to Looker. If you are already logged in, you will see a message in the browser window that Tableau used the browser window to authenticate into Looker and that you can now close the browser window.
  7. After you have authenticated into Looker, Tableau will open a **Data Source** page with a connection to your Looker instance.
  8. Use the **Schema** drop-down menu to select a Looker model with the data that you want to view in Tableau Desktop. Tableau will populate the **Table** list with the Looker Explores from the Looker model that you selected.
  9. To start exploring the data, select and drag an object from the **Tables** list to the canvas.


## Identifying Looker–Tableau BI Connector queries in the Looker UI
Queries from Tableau are made through the Open SQL Interface. Looker admins can use the Looker UI to identify which queries originated from the Open SQL Interface, as described in the Open SQL Interface documentation.
Queries from the Looker–Tableau BI Connector have a **Source** value of "sql_interface" or "SQL Interface".
## Using the Looker–Tableau BI Connector on Tableau Server
The Looker–Tableau BI Connector is not available on the Tableau Exchange, but you can install the Looker–Tableau BI Connector on Tableau Server by performing the procedures in the following sections:
  * Set up OAuth for the Looker–Tableau BI Connector
  * Install the Looker–Tableau BI Connector on Tableau Server
  * Complete the setup on Tableau Server


### Before you begin
Your Looker instance must meet the following requirements to use the Looker–Tableau BI Connector on Tableau Server:
  * Running Looker 24.14 or later.
  * Contains a LookML project that uses data from a Google BigQuery connection: 
    * The LookML project must be configured so that the **Allowed Connections** field is set to the **Only these connections** option with at least one Google BigQuery connection selected. See the Accessing and editing project information documentation page for information on configuring a model and seeing the allowed connections for the model.
    * The LookML project must have a model file that specifies a BigQuery connection in its `connection` parameter.


In addition, each person who uses the Looker–Tableau BI Connector must have a Looker account with a user role that includes the `explore` permission on the LookML model that they want to access from Tableau.
### Set up OAuth for the Looker–Tableau BI Connector
To use the Looker–Tableau BI Connector for Tableau Server, you need to set up OAuth integration on your Looker instance.
You can use the Looker API Explorer to set up OAuth integration for the Looker–Tableau BI Connector:
  * If your Looker instance already has the API Explorer installed, you can access it with this URL format:
```
https://LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/

```

  * If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the Using the API Explorer page for information.


To use the API Explorer to set up OAuth integration on your Looker instance, follow these steps:
  1. Open the Looker API Explorer (see the Using the API Explorer page for information).
  2. In the API Explorer's **Search** field, enter **Register OAuth App**.
  3. In the search results, click **Register OAuth App**.
  4. On the **Register OAuth App** page, click the **Run It** button.
  5. In the **Request** tab of the **Run It** dialog, enter the following information into the corresponding fields:
     * **client_guid** :
```
tableau-server

```

     * **body** :
```
{
  "redirect_uri": TABLEAU_SERVER_INSTANCE_URL/auth/add_oauth_token,
  "display_name": "Looker-Tableau-Server (manual)",
  "description": "Client for Looker-Tableau Server integration (manually added)",
  "enabled": true,
  "group_id": ""
}

```

  6. Select the checkbox for **I understand that this API endpoint will change data.**
  7. Click **Run**.
  8. You can verify that you successfully set up authentication by using the `Get OAuth Client App` method in the API Explorer:
     * In the API Explorer's **Search** field, enter **Get OAuth Client App**.
     * Click **Run It**.
     * In the **client_guid** field, enter this value: `tableau-server`
If you set up OAuth successfully, the **Response** tab will return the values that you entered when you registered the app.


### Install the Looker–Tableau BI Connector on Tableau Server
To install Looker–Tableau BI Connector on Tableau Server, perform the following steps:
  1. Download the Tableau connector file by clicking the following link: `looker_v1.0.0.taco`
  2. Download the latest version of the `avatica-<release_number>-looker.jar` file from https://github.com/looker-open-source/calcite-avatica/releases.
  3. Install the TACO and JAR files on your Tableau Server host machine. The location for the files depends on the server's operating system. The default Tableau installation paths are shown in the following table:


Windows server More
TACO file location | JAR file location  
---|---  
```
/opt/tableau/connectors
```
| ```
/opt/tableau/tableau_driver/jdbc
```
  
TACO file location | JAR file location  
---|---  
```
C:\Program Files\Tableau\Connectors
```
| ```
C:\Program Files\Tableau\Drivers
```
  
### Complete the setup on Tableau Server
After you have set up OAuth for the Looker–Tableau BI Connector and installed the Looker–Tableau BI Connector, you can complete the setup by performing the following procedures on your Tableau Server host machine:
  * Register the OAuth client ID and the OAuth instance URL (the redirect URL) that you specified when you set up OAuth for the Looker–Tableau BI Connector. Refer to Tableau's documentation for an example using a similar connector.
  * Validate and update saved credentials. Refer to Tableau's documentation for an example using a similar connector.


## Things to consider
When you're exploring Looker data with Tableau Desktop, note the following considerations:
  * The Looker–Tableau BI Connector is built upon the Looker Open SQL Interface, and it has the same LookML limitations and SQL limitations as the Open SQL Interface. See the Open SQL Interface documentation for more details.
  * Tableau automatically queries the database whenever a change is made to the query, including when fields are added and removed using the Looker–Tableau BI Connector. You can turn off automatic updates in Tableau: Refer to the Tableau documentation for more information.
  * You cannot use Tableau to join two Looker Explores. If you want to join Explores, use Looker to create the joins in your Looker model. See the Looker documentation pages Working with joins in LookML and join parameters for information on using joins in Looker.
  * The Looker–Tableau BI Connector is designed to work with a live connection in Tableau. Tableau's data extract mode extracts Looker measures with a value of "null" and therefore won't produce accurate results. If you want to use extract mode, you can create aggregate fields in Tableau directly off the Looker dimension fields instead of using Looker measures.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


