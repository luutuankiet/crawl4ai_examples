# Admin settings - Themes  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Default theme
    * Dashboard Controls
    * Example of a dashboard with the Looker theme
    * Example of a dashboard tile edit window with the Looker theme
    * Example of an Explore page with the Looker theme
  * How themes and embed settings are applied
  * Creating a custom theme
    * Dashboard controls
  * Deleting a theme
  * Setting a default theme for embedded dashboards and Explores
  * Applying a theme to specific embedded dashboards and Explores
  * Using the _theme URL argument to apply individual dashboard theme elements




Was this helpful?
Send feedback 
#  Admin settings - Themes
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Default theme
    * Dashboard Controls
    * Example of a dashboard with the Looker theme
    * Example of a dashboard tile edit window with the Looker theme
    * Example of an Explore page with the Looker theme
  * How themes and embed settings are applied
  * Creating a custom theme
    * Dashboard controls
  * Deleting a theme
  * Setting a default theme for embedded dashboards and Explores
  * Applying a theme to specific embedded dashboards and Explores
  * Using the _theme URL argument to apply individual dashboard theme elements


You can use custom themes to customize the appearance of your embedded Looker dashboards, Looks, and Explores. You can use themes to customize font family, text color, background color, button color, tile color, and other visual elements.
For example, you can create a "dark" theme to change the appearance of your embedded dashboard.
For information about setting a default theme for your dashboards and Explores, or for applying a theme to a specific dashboard or Explore, see the Getting started with embedding — applying custom themes documentation page.
You can define themes for embedded dashboards, embedded Explores, and the edit window for tiles in an embedded dashboard from the **Themes** page in the **Platform** section of the **Admin** panel.
This page describes the following:
  * The Looker default theme
  * How themes are applied to embedded dashboards and Explores
  * How to create, copy, edit, and delete a custom theme
  * How to set a default theme for dashboards and Explores
  * How to apply a theme other than the default to selected dashboards and Explores
  * How to apply the `_theme` URL argument to select dashboard theme elements


## Requirements
To manage themes on your Looker instance, you must meet the following requirements:
  * If your instance is a Looker (original) instance, the feature that lets you customize themes for embedded dashboards, Looks, and Explores must be enabled by Looker. Contact a Google Cloud sales specialist to update your license for this feature.
  * If your instance is a Looker (Google Cloud core) instance, embedded themes are available for the **Enterprise** and **Embed** editions, but not for the **Standard** edition.
  * Your Looker user must have the Admin role or the `manage_themes` permission.


## Default theme
The **Looker** default theme is created automatically on your instance, and it cannot be deleted or edited. The **Looker** theme is used as the default theme unless a Looker admin specifies another theme as the default.
The **Looker** theme settings, which you can see by selecting the **View** button next to the theme or by creating a copy of the theme, are grouped into the following sections:
  * Dashboard page
  * Dashboard Tiles
  * Dashboard Controls


### Theme
Setting Name | Value  
---|---  
Name | Looker  
### General
The settings in this section apply both to embedded dashboards and to embedded Explores.
Setting Name | Value | Notes  
---|---|---  
Key Color | `#1A73E8` |  Dashboards use this color for primary buttons and filter controls.Explores use this color for primary buttons, banners, and accents.   
Text Color | `#3e3f40`  
Background Color | `#f6f8fa`  
Font Family | Roboto, Noto Sans JP, Noto Sans CJK KR, Noto Sans Arabic UI, Noto Sans Devanagari UI, Noto Sans Hebrew, Noto Sans Thai UI, Helvetica, Arial, sans-serif | These fonts are served by the Looker application and are recommended because they will be available both in browsers and when images are rendered. Looker uses the first font in the font family list that supports a character, so the higher priority or specialized fonts should be listed first. Looker uses the "UI" variations of fonts when they're available so that characters are slightly modified to better fit within the boundaries of visual components.  
Font Source | None  
### Dashboard page
Setting Name | Value  
---|---  
Color Collection | None  
Background Color | `#f6f8fa`  
### Dashboard Tiles
Setting Name | Value  
---|---  
Title Color | `#3a4245`  
Text Color | `#3a4245`  
Text Body Color | None  
Background Color | `#ffffff`  
Title Alignment | Center  
### Dashboard Controls
Setting Name | Value  
---|---  
Display Dashboard Title | Yes  
Display Filters Bar | Yes  
### Explore page
Setting Name | Value  
---|---  
Display Header | Yes  
Display Title | Yes  
Display Last Run | Yes  
Display Timezone | Yes  
Display Run Button | Yes  
Display Settings Button | Yes  
### Look page
Setting Name | Value  
---|---  
Display Header | Yes  
Display Title | Yes  
Display Last Run | Yes  
Display Timezone | Yes  
Display Run Button | Yes  
Display Settings Button | Yes  
Following are examples of a dashboard, a dashboard tile's edit window, and an Explore with the **Looker** theme.
### Example of a dashboard with the Looker theme
### Example of a dashboard tile edit window with the Looker theme
### Example of an Explore page with the Looker theme
## How themes and embed settings are applied
You can change the appearance of an embedded dashboard or Explore from the default theme by using custom themes and URL arguments. When displaying an embedded dashboard or Explore, Looker applies settings in the following order:
  1. Begins with the settings from the default theme
  2. Applies settings from the custom theme that is specified in the `theme` argument of the URL, if any
  3. Applies properties that are specified in the `_theme` URL argument, if any (for dashboards only)


Each item overrides the previous items, meaning that the embed settings override the default theme settings, and custom themes override the embed settings and the default themes.
However, in the case of the `_theme` URL argument, only the elements that are specified in the `_theme` argument override elements from the other themes or from the embed settings. The rest of the custom theme settings and embed settings will still be used. For example, if you add the `_theme={"show_filters_bar":false}` argument in an embedded dashboard's URL, the filters bar will not be displayed, even if you have turned on **Show Filters** in the embed settings or in a custom theme. But the other settings from the custom theme or embed settings will still be used.
Downloads of dashboards will show any applied custom theme.
## Creating a custom theme
To create a custom theme, select **Add Theme** :
Next, add style and color specifications for each desired setting on the **New Theme** page.
Except for the theme's title, which must be unique, all the fields are automatically filled in with the values from the default theme. You can change any of the settings, which are described in the following sections. Select **Save Theme** to keep your changes and save your new theme.
### Theme
**Name** : The name for the theme must be unique and can contain only alphanumeric characters and underscores. If you enter spaces in the theme name, the spaces will be replaced with underscores when you save the theme.
### General
The settings in this section apply both to embedded dashboards and to embedded Explores.
**Key Color** : Dashboards use this color for primary buttons and filter controls. Explores use this color for field picker links and icons, primary buttons, banners, and accents.
**Text Color** : The hexadecimal color code for the text on Explores and dashboards.
**Background Color** : The hexadecimal color code for the background of Explore and dashboard pages.
**Font Family** : The name of the font family. This font will be used for all the text on the dashboard, including tile titles, text tiles, and legends in visualizations. This font will also be used for all the text in an Explore. If there is a space in the name of the font, use quotes around the name, such as "Open Sans".
  * If you are using a common web-safe font, you can just type the font name in the **Font Family** field and leave the **Font Source** field blank. If you want to use a less common font, enter the font name in the **Font Family** field and then use the **Font Source** field, described next, to provide a URL to the definition of the font that you want to use.


**Font Source** : Leave this field blank unless you want to use a custom font — a font that is not a common web-safe font. The **Font Source** must be a complete URL that starts with `https` and points to the `url` value that is specified in the `src` argument of `@font-face`. We recommend using a web open font format (`.woff`) file, since `.woff2` files aren't supported by Internet Explorer 11.
  * For example, for PT Sans Narrow, you could enter "PT Sans Narrow" in the **Font Family** field and then enter `https://fonts.gstatic.com/s/ptsansnarrow/v7/UyYrYy3ltEffJV9QueSi4RdbPw3QSf9R-kE0EsQUn2A.woff` in the **Font Source** field.


#### Example of an embedded Explore with a custom theme
The following example shows an embedded Explore that has a custom theme. The **Key Color** is set to `#e82042`, and the **Font Family** is set to Verdana.
When you're running an Explore in an embedded setting, the text in the Explore appears in the specified **Font Family** font, Verdana. Accent colors, buttons, and links appear in the specified **Key Color** , `#e82042`:
After an Explore is run, the **Run** button outline and text appears in the specified **Key Color** , `#e82042`:
#### Example of an embedded dashboard tile edit window with a custom theme
In addition to the Explore elements described in the previous section, when you're editing a dashboard tile, the banner appears in the shade that is specified in the **Key Color** setting (`#e82042`), and the font that is specified in the **Font Family** setting (Verdana):
### Dashboard page
**Color Collection** : Optionally, you can choose a color collection, which is a set of coordinating palettes that work well together. When you assign a color collection to a dashboard, all the data series in all the dashboard's tiles are colored according to the palettes in the collection, ensuring that the data series' colors are coordinated over the entire dashboard.
  * When you assign a color collection to an embedded theme, the theme's color collection will override any color collection that was previously assigned to a tile. However, a theme's color collection will not override customized colors assigned to a data series, nor will it override conditional formatting applied to a table visualization.


**Background Color** : The hexadecimal color code for the background of the dashboard and the background of text tiles.
**Margin Top** : Optionally set a specific value for the margin at the top of a dashboard. Choose from predefined options in a drop-down menu. Margins are measured in pixels (px).
**Margin Bottom** : Optionally set a specific value for the margin at the bottom of a dashboard. Choose from predefined options in a drop-down menu. Margins are measured in pixels (px).
**Margin Sides** : Optionally set a specific value for the margin on the sides of a dashboard. Choose from predefined options in a drop-down menu. Margins are measured in pixels (px).
### Dashboard tiles
**Title Color** : The hexadecimal color code for the following elements:
  * Dashboard title
  * Titles of dashboard tiles
  * Titles and header level 1 text of Markdown tiles
  * Text color of single value visualizations


**Text Color** : The hexadecimal color code for the following elements:
  * Text on the dashboard, including legends in visualizations
  * Subtitles and body text, with the exception of header level 1 text, of Markdown tiles
  * Header level 1, header level 2, and normal text on text tiles
  * Tile icons in single value visualizations


**Text Body Color** : The hexadecimal color code for the following elements:
  * Body text, with the exception of header level 2 and header level 3 text, in Markdown tiles.
  * Body text in text tiles


**Background Color** : The hexadecimal color code for the background of all tiles except text tiles. (Text tiles use the same background color as the dashboard, which is set using the **Background Color** in the **Dashboard Page** section.)
**Title Alignment** : Set the alignment of tile titles to left, right, or center.
**Title Font Size** : Optionally adjust the font size of dashboard tiles from a set of predefined sizes in pixels.
**Box Shadow** : Create a shadow around dashboard tiles using CSS syntax. You can select from a predefined box shadow or create a custom one. To create a custom box shadow, enter your desired `horizontal-offset vertical-offset blur-radius spread-radius color `, and select **Enter Custom Styling** to apply your settings. A preview of the box shadow settings is shown to the right.
**Column Gap Size** : Optionally adjust the size of the space between columns of dashboard tiles from a set of predefined sizes in pixels.
**Row Gap Size** : Optionally adjust the size of the space between rows of dashboard tiles from a set of predefined sizes in pixels.
**Border Radius** : Optionally adjust the border radius of dashboard tiles to create square or rounded corners.
### Dashboard controls
**Display Dashboard Header** : Disable this option to hide the entire dashboard header, including all dashboard filters and controls. When this option is disabled, all other dashboard control options are deselected and disabled.
**Display Dashboard Title** : Select the checkbox to display the title of the dashboard.
**Center Dashboard Title** : Select this checkbox to display the dashboard title center aligned on the dashboard. When this option is not enabled, the dashboard title is left aligned. This option is available only if the **Display Dashboard Title** option has been enabled.
**Display Filters Bar** : Select the checkbox to display the filters bar at the top of the dashboard. When this option is not selected, the **Display Filters Toggle** option is deselected and disabled, hiding the dashboard filters icon.
**Display Filters Toggle** : Select the checkbox to display the dashboard filters icon.
**Display Dashboard Last Updated Indicator** : Select the checkbox to display the dashboard last updated indicator.
**Display Reload Data Icon** : Select the checkbox to display the dashboard reload data icon.
**Display Dashboard Menu** : Select the checkbox to display the three-dot dashboard menu. When this option is deselected, dashboard menu options are unavailable.
### Explore page
Within a custom theme you can adjust the following elements on embedded Explore pages:
**Display Header** : Disable this option to hide the entire header of an embedded Explore, including the title, the last run indicator, the timezone of the data, the **Run** button, and the **Explore actions** gear menu.
**Display Title** : Disable this option to hide the title of an embedded Explore.
**Display Last Run** : Disable this option to hide how long ago the Explore was run.
**Display Timezone** : Disable this option to hide the timezone of the data on an embedded Explore.
**Display Run Button** : Disable this option to hide the **Run** button on an embedded Explore.
**Display Actions Button** : Disable this option to hide the Explore actions gear menu on an embedded Explore.
### Look page
Within a custom theme you can adjust the following elements on embedded Looks:
**Display Header** : Disable this option to hide the entire header of an embedded Look, including the title, the last run indicator, the timezone of the data, the **Run** button, and the **Explore actions** gear menu.
**Display Title** : Disable this option to hide the title of an embedded Look.
**Display Last Run** : Disable this option to hide how long ago the Look was run.
**Display Timezone** : Disable this option to hide the timezone of the data on an embedded Look.
**Display Run Button** : Disable this option to hide the Run button on an embedded Look. When Show Filters on Embedded Looks is disabled, this toggle does not display the **Run** button.
**Display Actions Button** : Disable this option to hide the Explore actions gear menu on an embedded Look.
## Copying a theme
You can copy an existing theme by selecting the theme's menu and selecting **Copy Theme**.
When you make a copy of a theme, the new theme's name defaults to the name of the copied theme, followed by "(copy)". Be sure to manually change this name to a new, unique name with only alphanumeric characters and underscores, and be sure to remove the parentheses.
You can edit the rest of the settings just as you would when you create a new theme. For a description of the settings, see the theme settings described previously. Be sure to select **Save** to keep all your theme settings.
## Editing a theme
The **Looker** theme is created automatically on your instance, and it cannot be edited. (If you want to modify the **Looker** theme, you can instead create a copy of the theme and then edit the copy.)
For all other themes, you can select the associated **Edit** button to update theme settings.
You can edit the settings just as you would when you create a new theme. For a description of the settings, see the theme settings described previously. Be sure to select **Save** to keep your updates.
## Deleting a theme
You can delete any theme except the **Looker** theme or the theme that is set as the default. To delete a theme, select the theme's menu and select **Delete Theme**.
After you delete a theme, any embedded dashboard that has that theme specified in its URL will use the default theme.
## Setting a default theme for embedded dashboards and Explores
> Custom themes are not supported on embedded Looks. Custom themes are available only for embedded dashboards and embedded Explores.
To specify the default theme for the embedded dashboards and Explores on your instance, select a theme's menu and select **Set as Default**.
The default theme is used for embedded dashboards and Explores on your Looker instance, unless you specify different settings for an individual dashboard or Explore. See the How themes and embed settings are applied section on this page for more information on how themes and embed settings are applied to an embedded dashboard or Explore.
## Applying a theme to specific embedded dashboards and Explores
> Custom themes are not supported on embedded Looks. Custom themes are available only for embedded dashboards and embedded Explores.
If you want a dashboard or an Explore to use a theme other than the default theme, you can specify a different theme in the URL of the embedded dashboard or Explore. To do this, add the parameter `theme=` with the name of the theme to the end of the embed URL. For example, if you have a theme called "Red," you would add `theme=Red` at the end of your embed dashboard URL:
```
https://example.cloud.looker.com/embed/dashboards/246?theme=red

```

For Explores, you would add `theme=Red` at the end of your embed Explore URL: `none https://example.cloud.looker.com/embed/explore/model_name/explore_name?theme=red`
The theme element in the URL is not case-sensitive, so you can use either `theme=Red` or `theme=red`.
## Using the `_theme` URL argument to apply individual dashboard theme elements
You can use the `_theme` URL argument to customize individual theme elements for your embedded dashboard, such as `tile_background_color` and `show_title`.
Here is the format for the `_theme` URL argument:
```
_theme={"<property>":value}

```

For example, you can use `_theme={"show_filters_bar":false}` to hide the filters bar of your embedded dashboard. The full URL might look like this:
```
https://example.cloud.looker.com/embed/dashboards/236?_theme={"show_filters_bar":false}

```

Use a comma to specify multiple theme properties:
```
_theme={"show_title":false,"show_filters_bar":false,"text_tile_text_color":"blue"}

```

Color values must be in quotes, and can be expressed with the color name, or with the hexadecimal color code. If using a hex code, be sure to use URL encoded version of the `#` sign, which is `%23`. For example, both of these URL arguments specify the color red:
```
_theme={"title_color":"red","text_tile_text_color":"%23FF0000"}

```

Here are some things to consider when using the `_theme` object for an embedded dashboard:
  * Any element that is specified in the `_theme` URL argument will override the settings for that element in any other theme. This makes the `_theme` argument a handy way to refine themes or embed settings. For example, let's say you have a custom theme that hides the filters bar, but you have one dashboard where having the filters bar show would make sense. You can use the custom theme for your dashboard and then add the `_theme={"show_filters_bar":true}` argument in the embedded dashboard's URL to show the filters bar on that dashboard but keep all the other custom theme settings. See the How themes and embed settings are applied section on this page for more information on how themes and embed settings are applied to an embedded dashboard.
  * For programming scripts, you must URL-encode the `_theme` argument.
  * The `_theme` argument is not applied when delivering embedded dashboards in PDF format.
  * The `_theme` argument is applied if you download the dashboard as a PDF.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


