# Embed SDK Demo  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/embed-sdk-demo

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Step 1: Enable embedding in your Looker instance
  * Step 2: Customize the demo settings for your Looker instance
  * Step 3: Build and run the demo




Was this helpful?
Send feedback 
#  Embed SDK Demo
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Step 1: Enable embedding in your Looker instance
  * Step 2: Customize the demo settings for your Looker instance
  * Step 3: Build and run the demo


The Looker Embed SDK repository includes sample code and a demo of the Embed SDK. Because of Looker's security requirements, the demo requires a bit of setup. The demo also requires your Looker embed secret. The embed secret grants access to all of your data, so note the following:
  * Don't share your secret with anyone whom you don't want to have complete access to your instance.
  * Don't reset your secret if you already are using it in another context.
  * Don't set up your code to store the secret in the web browser.


## Step 1: Enable embedding in your Looker instance
This is documented in more detail on the Signed embedding documentation page.
  1. Navigate to **Admin > Platform Embed** on your Looker instance. This requires Admin privileges.
  2. The demo server runs by default at `http://localhost:8080`. By adding that address to the **Embedded Domain Allowlist**, you can enable the demo to receive messages from Looker.
  3. Turn on **Embed Authentication**.
  4. In order to view your embed secret you must reset it. Copy the secret to a secure place.


## Step 2: Customize the demo settings for your Looker instance
Provide your embed secret to the server. You can do this in the following ways:
  * Set it as `LOOKER_EMBED_SECRET` in your shell environment.
  * Create a file named `.env` in the root of the sdk directory. Add a line to that file: `LOOKER_EMBED_SECRET="YourLookerSecret"`


Provide your Looker instance host address to the server by using one of the following methods:
  * Set it as `LOOKER_WEB_URL` in your shell environment.
  * Add `LOOKER_WEB_URL="yourinstance.looker.com:yourport"` to the `.env` file.


Edit the ENV file to specify the IDs of the content that you want to embed.
```
#LookerEmbedDataConfiguration
#Setto-ifdemoneedstoignoreit

#DashboardIDs
LOOKER_DASHBOARD_ID=1
LOOKER_DASHBOARD_ID_2=2
#LookID
LOOKER_LOOK_ID=1
#ExploreID
LOOKER_EXPLORE_ID=model::explore
#ExtensionID
LOOKER_EXTENSION_ID=extension::my-great-extension
#ReportID
LOOKER_REPORT_ID=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
#QueryVisualizationID
LOOKER_QUERY_VISUALIZATION_ID=1234567890ABCDEF123456


```

Edit the `demo/demo_user.json` file to be appropriate for the type of user you want to embed.
```
{
// External embed user ID. IDs are not shared with regular users. Required
"external_user_id":"user1",
// First and last name. Optional
"first_name":"Pat",
"last_name":"Embed",
// Duration before session expires, in seconds. Required.
"session_length":3600,
// Enforce logging in with these permissions. Recommended.
"force_logout_login":true,
// External embed group ID. Optional.
"external_group_id":"group1",
// Looker Group IDs. Optional
"group_ids":[],
// Permissions. See documentation for details. Required.
// Can any combination of:
//   access_data
//   see_looks
//   see_user_dashboards
//   see_lookml_dashboards
//   explore
//   create_table_calculations
//   download_with_limit
//   download_without_limit
//   see_drill_overlay
//   see_sql
//   save_content
//   embed_browse_spaces
//   schedule_look_emails
//   send_to_sftp
//   send_to_s3
//   send_outgoing_webhook
//   schedule_external_look_emails
"permissions":[
"access_data",
"see_looks",
"see_user_dashboards",
"explore",
"save_content",
"embed_browse_spaces"
],
// Model access permissions. Required.
"models":["powered_by","thelook"],
// User attributes. Optional.
"user_attributes":{"locale":"en_US"},
}

```

## Step 3: Build and run the demo
To build and run the demo, follow the steps for the appropriate server.
### Node server
  1. Run `npm install`
  2. Run `npm start`


The server will print out what host and port it is running on. If it is different than `http://localhost:8080` then you will need to add it to your **Embedded Domain Allowlist**.
### Python server
  1. Run `npm install`
  2. Run `npm run python`


The server will print out what host and port it is running on.
You may need to `pip install six` to install the Python 2/3 compatibility layer.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


