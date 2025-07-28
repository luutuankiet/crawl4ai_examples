# Private embedding  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/embedding-dashboards

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Generating an embed URL
  * Previewing the embedded content
  * Viewing the embedded content in an iframe
    * Changing the embedded appearance of a dashboard
  * Enable login screen for private embeds




Was this helpful?
Send feedback 
#  Private embedding
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Generating an embed URL
  * Previewing the embedded content
  * Viewing the embedded content in an iframe
    * Changing the embedded appearance of a dashboard
  * Enable login screen for private embeds


In addition to public embedding, you can also embed Looks, Explores, and dashboards privately. With private embedding, you can require a user to authenticate using a Looker login, Google OAuth, or OpenID Connect. If a user is not authenticated, you have the option to show an error message or display a login screen.
Users who are logged in and accessing privately embedded content are subject to the settings in the **Sessions** **Admin** panel, which determine how long they can stay logged in, if they can log in from multiple browsers, and if they will be logged out after a period of inactivity.
If you require a more advanced or customizable embedded solution, check out our Signed embedding documentation page.
## Generating an embed URL
To generate and copy a private embed URL for a dashboard, a Look, or an Explore visualization, select **Get embed URL** from a dashboard three-dot menu, or from the Explore action gear menu on an Explore or a Look.
The **Private Embed** screen includes the following elements:
  1. The **Content URL** field shows the full private embed URL.
  2. The **Apply theme to dashboard URL** field lets you select a theme to be added to the embed URL if you are generating a dashboard or an Explore embed URL and your instance has custom themes enabled. The theme will be applied when the embedded dashboard or Explore is viewed.
  3. The **Include current params in URL** switch lets you choose whether to apply current parameters, such as filter values, to the embed URL. If enabled, those parameters will be applied when the embedded content is viewed.
  4. Select the **Copy Link** button to copy the full embed URL to your clipboard.


Once you've generated and copied the embed URL, you can paste the URL into a new browser window or tab to preview the embedded content. You can also use this URL to embed the content in an iframe.
## Previewing the embedded content
Paste your embed URL in your browser to preview your embed content's behavior and appearance.
## Viewing the embedded content in an iframe
Place the embed URL into an iframe. For example:
```
  <iframe
      src="https://instance_name.cloud.looker.com/embed/dashboards/1"
      width="1000"
      height="2000"
      frameborder="0">
  </iframe>

```

And then embed the iframe as desired.
### Changing the embedded appearance of a dashboard
Viewing a dashboard with `/embed` in the URL shows you how the dashboard will appear when it's embedded.
By default, an embedded dashboard is displayed using the default theme for your Looker instance. You can change the appearance of your embedded dashboard in several ways, depending on the type of dashboard you are using:
  * For any type of dashboard, you can specify a different theme name in the embed URL to change the theme used to display the dashboard.
  * For any type of dashboard, you can use the `_theme` URL argument to change individual dashboard theme elements.
  * For a LookML dashboard, you can also modify the embedded appearance of a dashboard through the `embed_style` parameter.


Using the `theme` URL argument, the **Edit Embed Settings** option, or the `embed_style` parameter makes changes only to the dashboard the argument, option, or parameter is applied to. If you want to customize the appearance of multiple embedded dashboards, use a theme instead.
Some display settings override others. For more information, see the Creating and applying themes for embedded dashboards and Explores documentation page.
## Enable login screen for private embeds
You can add the parameter `allow_login_screen=true` to your embed URL if you want to display a login screen to users who haven't logged in already. For example:
```
<iframe src="https://instance_name.cloud.looker.com/embed/looks/4?allow_login_screen=true"></iframe>
                                                            ^^^^^^^^^^^^^^^^^^^^^^^

```

If you do not add this parameter, a 401 error will be displayed to users who are not already logged in.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


