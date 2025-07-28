# Set Default Theme  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Theme/set_default_theme

Skip to main content 


  * Español – América Latina

Console  Sign in
  * On this page
  * Set the global default theme by theme name




Send feedback 
#  Set Default Theme
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Set the global default theme by theme name


Version 4.0.25.10 (latest) 
### Set the global default theme by theme name
Only Admin users can call this function.
Only an active theme with no expiration (`end_at` not set) can be assigned as the default theme. As long as a theme has an active record with no expiration, it can be set as the default.
Create Theme has detailed information on rules for default and active themes
Returns the new specified default theme object.
**Note** : Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or https://console.cloud.google.com/support/cases/ to update your license for this feature.
## Request
PUT /themes/default 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
name
string 
Name of theme to set as default
## Response
### 200: Theme
Datatype
Description
(object)
can
_lock_
object 
Operations the current user is able to perform on this object
begin_at
string 
Timestamp for when this theme becomes active. Null=always
end_at
string 
Timestamp for when this theme expires. Null=never
id
_lock_
string 
Unique Id
name
string 
Name of theme. Can only be alphanumeric and underscores.
settings
Hash of name/value pairs for theme settings. These names get validated.
Expand ThemeSettings definition... 
background_color
string 
Default background color
base_font_size
string 
Base font size for scaling fonts (only supported by legacy dashboards)
color_collection_id
string 
Optional. ID of color collection to use with the theme. Use an empty string for none.
font_color
string 
Default font color
font_family
string 
Primary font family
font_source
string 
Source specification for font
info_button_color
string 
(DEPRECATED) Info button color
primary_button_color
string 
Primary button color
show_filters_bar
boolean 
Toggle to show filters. Defaults to true.
show_title
boolean 
Toggle to show the title. Defaults to true.
text_tile_text_color
string 
Text color for text tiles
tile_background_color
string 
Background color for tiles
text_tile_background_color
string 
Background color for text tiles
tile_text_color
string 
Text color for tiles
title_color
string 
Color for titles
warn_button_color
string 
(DEPRECATED) Warning button color
tile_title_alignment
string 
The text alignment of tile titles (New Dashboards)
tile_shadow
boolean 
Toggles the tile shadow (not supported)
show_last_updated_indicator
boolean 
Toggle to show the dashboard last updated indicator. Defaults to true.
show_reload_data_icon
boolean 
Toggle to show reload data icon/button. Defaults to true.
show_dashboard_menu
boolean 
Toggle to show the dashboard actions menu. Defaults to true.
show_filters_toggle
boolean 
Toggle to show the filters icon/toggle. Defaults to true.
show_dashboard_header
boolean 
Toggle to show the dashboard header. Defaults to true.
center_dashboard_title
boolean 
Toggle to center the dashboard title. Defaults to false.
dashboard_title_font_size
string 
Dashboard title font size.
box_shadow
string 
Default box shadow.
page_margin_top
string 
Dashboard page margin top.
page_margin_bottom
string 
Dashboard page margin bottom.
page_margin_sides
string 
Dashboard page margin left and right.
show_explore_header
boolean 
Toggle to show the explore page header. Defaults to true.
show_explore_title
boolean 
Toggle to show the explore page title. Defaults to true.
show_explore_last_run
boolean 
Toggle to show the explore page last run. Defaults to true.
show_explore_timezone
boolean 
Toggle to show the explore page timezone. Defaults to true.
show_explore_run_stop_button
boolean 
Toggle to show the explore page run button. Defaults to true.
show_explore_actions_button
boolean 
Toggle to show the explore page actions button. Defaults to true.
show_look_header
boolean 
Toggle to show the look page header. Defaults to true.
show_look_title
boolean 
Toggle to show the look page title. Defaults to true.
show_look_last_run
boolean 
Toggle to show the look page last run. Defaults to true.
show_look_timezone
boolean 
Toggle to show the look page timezone Defaults to true.
show_look_run_stop_button
boolean 
Toggle to show the look page run button. Defaults to true.
show_look_actions_button
boolean 
Toggle to show the look page actions button. Defaults to true.
tile_title_font_size
string 
Font size for tiles.
column_gap_size
string 
The vertical gap/gutter size between tiles.
row_gap_size
string 
The horizontal gap/gutter size between tiles.
border_radius
string 
The border radius for tiles.
### 400: Bad Request
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
### 404: Not Found
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
### 422: Validation Error
Datatype
Description
(object)
message
_lock_
string 
Error details
errors
ValidationErrorDetail[] 
Expand ValidationErrorDetail definition... 
field
_lock_
string 
Field with error
code
_lock_
string 
Error code
message
_lock_
string 
Error info message
documentation_url
_lock_
string 
Documentation link
documentation_url
_lock_
string 
Documentation link
### 429: Too Many Requests
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


