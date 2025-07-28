# Getting started with embedding — applying custom themes  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/getting-started-embed-themes

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Setting a default theme for embedded dashboards and Explores
  * Applying a theme to specific embedded dashboards and Explores
  * For more information




Was this helpful?
Send feedback 
#  Getting started with embedding — applying custom themes
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Setting a default theme for embedded dashboards and Explores
  * Applying a theme to specific embedded dashboards and Explores
  * For more information


You can use custom themes to customize the appearance of your embedded Looker dashboards and Explores. Use custom themes to customize font family, text color, background color, button color, tile color, and other visual elements.
> Custom themes are not supported on embedded Looks. Custom themes are available only for embedded dashboards and embedded Explores.
For example, you can select a **dark** theme to change the appearance of your embedded dashboard.
## Setting a default theme for embedded dashboards and Explores
To specify the default theme for the embedded dashboards and Explores on your instance, navigate to the **Themes** page in the **Platform** section of the **Admin** panel, and click on a theme's three-dot menu and select **Set as Default**.
The default theme is used for embedded dashboards and Explores on your Looker instance, unless you specify different settings for an individual dashboard or Explore.
## Applying a theme to specific embedded dashboards and Explores
If you want a dashboard or an Explore to use a theme other than the default theme, you can specify a different theme in the URL of the embedded dashboard or Explore. To do this, add the parameter `theme=` with the name of the theme to the end of the embed URL. For example, if you have a theme called "Red," you would add `theme=Red` at the end of your embed dashboard URL:
```
https://example.looker.com/embed/dashboards/246?theme=Red

```

For Explores, you would add `theme=Red` at the end of your embed Explore URL:
```
https://example.looker.com/embed/explore/model_name/explore_name?theme=Red

```

The theme element in the URL is not case-sensitive, so you can use either `theme=Red` or `theme=red`.
## For more information
  * For information about creating a custom theme, see the Admin settings - Themes documentation page.
  * For information about applying custom elements of a theme, see the "Using the _theme URL argument to apply individual dashboard theme elements" section of the Admin settings - Themes documentation page.
  * For information about applying and managing custom themes using the API, see the Theme method documentation.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


