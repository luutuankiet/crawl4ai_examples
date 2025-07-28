# Static Map (Regions) chart options  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/map-regions-options

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Map menu options
    * TopoJSON Object Key
    * TopoJSON Property Key
    * TopoJSON Property Label Key
  * Style menu options
    * Empty Region Color
    * Outer Border Color
    * Inner Border Color
    * Outer Border Width
    * Inner Border Width
    * Show Full Field Name in Tooltips




Was this helpful?
Send feedback 
#  Static Map (Regions) chart options
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Map menu options
    * TopoJSON Object Key
    * TopoJSON Property Key
    * TopoJSON Property Label Key
  * Style menu options
    * Empty Region Color
    * Outer Border Color
    * Inner Border Color
    * Outer Border Width
    * Inner Border Width
    * Show Full Field Name in Tooltips


Static map (regions) charts are useful for plotting data **regionally**. To plot individual points, use static map (points) or the interactive map charts.
To select a static map (regions) chart, click the ellipses (...) on the Visualization menu bar and select **Static Map (Regions)**.
Static map (regions) charts plot a single dimension and a single measure:
  * Austin, New York City, San Francisco maps, and custom maps based on zip codes, require a dimension of `type: zipcode`.
  * A United States map requires a dimension of `type: string` that contains the names of US states.
  * A World map, and custom maps based on countries, require a dimension of `type: string` that contains either ISO 3166-1 alpha-3 three-letter country codes or ISO 3166-1 alpha-2 two-letter country codes.
If your data uses two-letter country codes, to ensure that Looker recognizes your data as country codes and does not incorrectly interpret them as state codes, ensure that your Looker developer includes the `map_layer_name` parameter in the definition for your country dimension. For example:

```
  dimension: country {
      type: string
      map_layer_name: countries
      sql: ${TABLE}.country ;;
  }

```

## Map menu options
To format your visualization, select **Edit** in the upper right corner of the visualization tab.
Some of the options that are listed on this documentation page may be grayed out or hidden when they conflict with other settings that you have chosen.
### Map
You can choose a map to display your data:
  * **Austin, Texas (ZIP Codes):** Use data grouped by Austin zip codes (for region or point maps) or lat/long locations (for point maps only)
  * **New York City (ZIP Codes)** : Use data grouped by NYC zip codes (for region or point maps) or lat/long locations (for point maps only)
  * **San Francisco Peninsula (ZIP Codes):** Use data grouped by San Francisco peninsula zip codes (for region or point maps) or lat/long locations (for point maps only)
  * **United Kingdom (Postcode Areas):** Use data grouped by UK postal codes (for region or point maps) or lat/long locations (for point maps only)
  * **United States:** Use data grouped by US states (for region maps only), zip codes (for point maps only), or lat/long locations (for point maps only)
  * **World:** Use data grouped by country (for region maps only) or lat/long locations (for point maps only)
  * **Custom:** lets you define your own map using TopoJSON


You can also use the **Map** field's **Auto** option if your Looker developer has set a `map_layer` parameter for the model. If a message indicates that the `map_layer` isn't set, choose another **Map** option.
### TopoJSON URL
For map charts set to **Map** Custom, **TopoJSON URL** sets the location of a TopoJSON file that defines your map boundaries.
### TopoJSON Object Key
For map charts set to **Map** Custom, **TopoJSON Object Key** selects which map from the TopoJSON file to plot, since TopoJSON can support multiple maps in a single file. Set this parameter to one of the map names defined in the file.
### TopoJSON Property Key
For map charts set to **Map** Custom, **TopoJSON Property Key** selects which property from the TopoJSON file to plot against. TopoJSON can support arbitrary metadata for each region. If there's a particular metadata property you want to plot against, specify it here. By default, the first matching property is used.
### TopoJSON Property Label Key
For map charts set to **Map** Custom, **TopoJSON Property Label Key** selects which property from the TopoJSON file to display in the tooltip label. TopoJSON can support arbitrary metadata for each region. If there's a particular metadata property you want to appear in the tooltip, specify it here. By default, the value of **TopoJSON Property Key** is used.
### Projection
For map charts set to **Map** Custom, you can choose which D3 projection to use to render your map. Many options examples are shown on this GitHub page.
## Style menu options
### Colors
You can define the colors to use to indicate the magnitude of each map region.
This parameter takes a comma-separated list of one or more color values. The color values can be formatted as RGB hex strings, such as `#2ca6cd`, or as CSS color names, such as `mediumblue`.
You can define every valid color that Looker is allowed to use to indicate magnitude. To do so, make sure you turn on **Quantize Colors**. You can also allow Looker to interpolate shades of colors between those that you define. For this behavior, make sure you turn off **Quantize Colors**.
### Quantize Colors
You can determine whether the colors of a map regions chart are shaded according to the magnitude of each region (turned off), or if only the specific colors you specify in **Colors** will be used (turned on).
### Empty Region Color
You can set the color of any region on the chart that does not show up in the underlying data.
This parameter takes a single color value. The color value can be formatted as a RGB hex string, such as `#2ca6cd`, or as a CSS named color string, such as `mediumblue`.
### Outer Border Color
You can set the color of the overall map border.
This parameter takes a single color value. The color value can be formatted as a RGB hex string, such as `#2ca6cd`, or as a CSS named color string, such as `mediumblue`.
### Inner Border Color
You can set the border color of each map region.
This parameter takes a single color value. The color value can be formatted as a RGB hex string, such as `#2ca6cd`, or as a CSS named color string, such as `mediumblue`.
### Outer Border Width
You can set the width of the overall map border, specified as a number of pixels.
### Inner Border Width
You can set the border width of each map region, specified as a number of pixels.
### Show Full Field Name in Tooltips
You can toggle whether to show the view name along with the field name when you hover over a map region.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


