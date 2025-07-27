# Embedding Overview - Lightdash

**Source:** https://docs.lightdash.com/references/embedding

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Embedding and SDKs
Embedding Overview
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Known limitations
  * Allowed dashboards
  * User attributes
  * Interactivity
  * Generate & Copy URL
  * Code snippet and demo
  * User metadata
  * PDF Export Functionality


Embedding is available to all Lightdash Cloud users, get in touch to have this feature enabled in your account.
Embedded Lightdash content is available to view by anyone (not just folks with a Lightdash login). So, for example, you could embed a dashboard in your product, and anyone who has access to your product would have access to that dashboard. No need to login to Lightdash. We make sure that the links are secure and have a set expiry time that you pick (more on that below). For more of a deep dive into setting up and using embedding in Lightdash, check out our How to embed content guide.
##  Known limitations
There are a couple of known limitations today with embedding:
  * Embedding only works for dashboards, not table explores or single charts (unless the single chart is pinned to a dashboard first).
  * The **Filter dashboard to** option when clicking on individual chart segments will not work on embedded dashboards.

If you’re interested in embedding and one or more of these items are blockers, please reach out - we can activate them quickly.
##  Embed secret
The embed secret is used to generate tokens for embedding dashboards. This secret is like a password that will help you encrypt the URLs so we know the access is valid. You can regenerate the secret by clicking on the `Generate new secret` button. If you do this, people with an old URL will automatically lose access to any previously shared embed URL.
##  Allowed dashboards
Only dashboards included in the `allowed dashboards` can be accessed using embed URLs. To embed a dashboard, you need to first add it to the `allowed dashboards` list. You can use the `Allow all dashboards` toggle to skip the dashboard selection process. When enabled, it overrides the `allowed dashboards` setting, allowing embed URLs to be generated for any dashboard in your project.
##  Configure
Configure the embed URL. Then preview your settings and copy it to your clipboard.
###  Dashboard
Select the dashboard that you want to embed. Only dashboards included in the `allowed dashboards` list appear here.
###  Expires in
Set the amount of time it takes before your embed token expires. Although you can generate URLs directly from Lightdash with a long expiration using generate and copy URL, it is recommended to generate your own JWT embed tokens in your backend (using the code snippet) with a short expiration using your `secret` to make sure people can’t be using embed URLs outside your app.
###  User attributes
Use user attributes to limit access to certain data in the embedded dashboard. You can use any user attribute that you’ve defined in your organization in the embedded dashboard. To learn about getting your embedded dashboard to show different values for different users in your app, check out the guide here.
###  Interactivity
There are options to enable certain dashboard interactivity features on your embedded dashboard in this section. By default, all interactivity is disabled on an embedded dashboard.
##### Allow users to change dashboard filters
You can choose which filters are displayed in your embedded dashboard. The filters shown in the embedded dashboard will act like they do in Lightdash. Users interacting with the embedded dashboard will be able to change the value and operator of your filters. They cannot add new filters, remove existing filters, change the field used in the filter, or change the tiles the filter is applied to.
  * **No filters** No filters will be shown in the embedded dashboard. All dashboard filters are still applied.


  * **Some filters**

Only the filters you select will be shown in the embedded dashboard. All dashboard filters are still applied.
  * **All filters** All dashboard filters will be shown in the embedded dashboard.


##### Can download CSV
Enabling this option allows users to download all chart results as CSV files. On the embedded dashboard, this `download button` is accessible from the `...` options menu located in the top right corner when hovering over the chart tile.
###  Preview
Clicking on `preview` allows you to preview the configuration for your embedded dashboard. This what people viewing your embedded dashboard will see.
###  Generate & Copy URL
Clicking `generate & copy url` will generate an embed URL based on the configuration that you’ve set. You can embed this one-off URL directly into your application, but you will manually need to update the URL each time the embed URL expires. Alternatively, you can add the code snippet to your app to automatically generate embed URLs in your application.
##  Code snippet and demo
Although you can generate URLs directly from Lightdash with a long expiration, it is recommended to generate your own JWT embed tokens in your backend with a short expiration using your `secret` to make sure people can’t be using embed URLs outside your app. To make this easier to integrate, we included some code snippets you can copy and use in your app to generate a valid embed URL. Here is a demo of how to add the code snippet to your app: You can find the source code here.
###  User metadata
You can pass user metadata (specifically, an external user ID) from your application so that anytime someone views your embedded dashboard and runs queries in Lightdash, these query logs are enriched with this user metadata. Specifcally, this user metadata gets added to the query tags for queries run in Lightdash. To assign an external ID, you can update the embed code snippet like this:
Copy
Ask AI
```
import jwt from 'jsonwebtoken';
const LIGHTDASH_EMBED_SECRET = 'secret'; // replace with your secret
const projectUuid = 'my-project-uuid';
const data = {
  user: {
    externalId: 'your_user_id_123', // Add this to assign an external ID

  content: {
    type: 'dashboard',
    dashboardUuid: 'your dashboard uuid',


const token = jwt.sign(data, LIGHTDASH_EMBED_SECRET, { expiresIn: '1 hour' });
const url = `https://analytics.lightdash.cloud/embed/${projectUuid}/#${token}`;

```

If you don’t assign an external ID in your embed code, then we will automatically generate and an assign an external ID based on the embed token.
##  PDF Export Functionality
In the embedded dashboard, you have the ability to export the current page as a PDF document. This feature can be accessed by clicking on the Print icon located in the upper right corner of the interface. Upon selecting the Print icon, a dialog box will emerge, presenting you with several print options. Within this dialog, you have the option to choose “Export as PDF” as your desired output format.
Embedding quickstartReact SDK
Assistant
Responses are generated using AI and may contain mistakes.


