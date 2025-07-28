# Static Map (Points) chart options  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/map-points-options

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Map menu options
    * TopoJSON Object Key
  * Style menu options
    * Outer Border Color
    * Inner Border Color
    * Outer Border Width
    * Inner Border Width
    * Show Full Field Name in Tooltips




Was this helpful?
Send feedback 
#  Static Map (Points) chart options
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Map menu options
    * TopoJSON Object Key
  * Style menu options
    * Outer Border Color
    * Inner Border Color
    * Outer Border Width
    * Inner Border Width
    * Show Full Field Name in Tooltips


Static map (points) charts are useful for plotting data represented by **points** on a map. To plot regions, use static map (regions). Static map (points) charts plot a single dimension of `type: location` or `type: zipcode`, and a single measure. Additional dimensions appear in the tool-tip on hover.
Your data must be grouped appropriately for the visualization type (regions map or points map) and the specific map (US, UK, World) that you choose. See the Map section later on this page for guidance.
To select a static map (points) chart, click the ellipses (...) on the Visualization menu bar and select **Static Map (Points)**.
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


### TopoJSON URL
For map charts set to **Map** Custom, **TopoJSON URL** sets the location of a TopoJSON file that defines your map boundaries.
### TopoJSON Object Key
For map charts set to **Map** Custom, **TopoJSON Object Key** selects which map from the TopoJSON file to plot, since TopoJSON can support multiple maps in a single file. Set this parameter to one of the map names defined in the file.
### Projection
For map charts set to **Map** Custom, you can choose which D3 projection to use to render your map. Many options examples are shown on this GitHub page.
## Style menu options
### Point Color
You can set the color to use for each point on a map points chart.
This parameter takes a single color value. The color value can be formatted as a RGB hex string, such as `#2ca6cd`, or as a CSS named color string, such as `mediumblue`.
### Map Color
You can set the background color of regions on a map points chart.
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
### Point Radius
You can set the radius of each point on a map points chart, specified as a number of pixels. When left unset, Looker scales the radius of each point according to its magnitude.
### Show Full Field Name in Tooltips
You can toggle whether to show the view name along with the field name when you hover over a map region.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


