# 2.x Release Notes  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-2-release-notes

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
#  2.x Release Notes
Stay organized with collections  Save and categorize content based on your preferences. 
## Looker 2.4 2014-07-14
### LookML / Projects
  * New field parameter `format:` for printf-style formatting


### Explore
  * Totals working in all dialects, implemented as a separate SQL query


### Data Visualization
  * New element parameter `show_applied_filters: false` to turn off dynamic filters in title of a dashboard element
  * New dashboard parameter `refresh: N minutes` to refresh data every N minutes if the page is open


### Enterprise, Platform, and Security
  * LDAP authentication
  * Two-factor authentication


### Bug Fixes and Tweaks
  * Add/delete projects moved to admin panel


## Looker 2.2 2014-06-09
### Data Visualization
  * Custom map visualizations
  * Dimensional scatter plot
  * Automatic x_axis_scale detection
  * x_padding_left and x_padding_right option for charts
  * Specify colors, series_colors, series_labels, reference lines, and more in looker_type charts
  * Plot geo coordinates (lat/long) on world map


### LookML / Projects
  * Redesigned Projects experience
  * LookML project search with regular expressions & find and replace
  * JGit bundled with Looker (replaces server-based git)
  * Liquid templating (replaces ERB)
  * More flexible join syntax
  * Top nav menus update upon LookML file save (instead of after page reload)
  * Declare a base_view as hidden: true
  * Table Calculations: type: running_total
  * Line-by-line git diffs in LookML editor (yellow for modified, green for added, red for deleted)


### Explore
  * Jump to LookML error link from Explore page
  * Improved and more flexible number filter syntax (e.g. >, <, != operators)
  * SQL Runner moved to Explore menu
  * SQL tab updates live as query is constructed in UI (with EXPLAIN)


### Enterprise, Platform, and Security
  * Improved admin audit and Looker usage panels
  * Embeddable iframe code added to public URL box


### Bug Fixes and Tweaks
  * Lots of looker_ (area, column, etc.) and reference line bug fixes. Thanks to the beta testers!
  * Improved login and auto logout flow
  * Convert "yyyymmdd" format to valid time field
  * Year filters now use date syntax (instead of integer)
  * Dozens of other bug fixes and tweaks!


## Looker 2.0 2014-04-28
### Data Visualization (Beta)
  * Maps (US & World) chart types: Coordinates Plot, Choropleth
  * New Cartesian chart types: Single Record, Donut, Donut Multiples
  * Updated Cartesian chart types: looker_column, looker_line, looker_area, looker_pie
  * Reference Lines: static, median, mean, min, max, ranges, standard deviation, variance
  * Additional formatting parameters (interpolation, colors, hide_points, hide_legend)
  * Automatically detect and format date axes


### LookML
  * Developer vs. Production Mode SQL option in PDTs
  * Field name validation before query run
  * Generate files as .model.lookml, .view.lookml, .dashboard.lookml
  * When on, user access filters block filter suggestions
  * select_filter aliased to suggest_filter in dashboard filters


### Enterprise and Security
  * Auto user log out (with warning) unless trusted computer


### SQL Dialects
  * Support for Teradata Aster 6.0
  * (Beta) Support for Oracle Database 11g


### Bug Fixes and Tweaks
  * Persistent derived table fixes
  * Drilling into a dashboard chart keeps filters applied
  * Timezone conversion in Redshift
  * Warn when changing timezone that it affects all users
  * Show conditional filters in dashboard URL
  * Return 401 error as JSON API responses when authentication fails
  * Add link to SQL Runner from connections page
  * MS SQL Server suggest fix


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


