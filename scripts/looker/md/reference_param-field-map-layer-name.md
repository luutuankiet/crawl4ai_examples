# map_layer_name  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-map-layer-name

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  map_layer_name
Stay organized with collections  Save and categorize content based on your preferences. 
## Usage
```
view: view_name {
  dimension: field_name {
    map_layer_name: name_of_map_layer
  }
}

```
Hierarchy `map_layer_name` |  Possible Field Types DimensionAccepts A map name specified in the model-level `map_layer` parameter  
---|---  
## Basics
The `map_layer_name` parameter lets you associate a dimension with a TopoJSON or GeoJSON map layer. This lets users create map charts by charting the values in the dimension on the map layer. For example, to be able to chart data by US state, you could associate a dimension called "State" to the built-in map layer `us_states`. You could also chart data in a dimension called "Neighborhood" to a custom map of New York City neighborhoods.
If you are using a custom TopoJSON or GeoJSON map, you must specify the map layer in the LookML model by using the `map_layer` parameter.
Dimensions of `type: zipcode` automatically receive a `map_layer_name` of `us_zipcode_tabulation_areas`.
### Built-in map layers
Looker includes the following built-in map layers:
  * `countries` — Accepts full country names, ISO 3166-1 alpha-3 three-letter country codes, and ISO 3166-1 alpha-2 two-letter country codes. If your data includes ISO 3166-1 alpha-2 country codes, using `map_layer_name` with the `countries` map is recommended to ensure that Looker interprets your data as country codes and not as state codes.
  * `uk_postcode_areas` — Accepts UK postcode areas (for example, `L` for Liverpool, `RH` for Redhill, or `EH` for Edinburgh).
  * `us_states` — Accepts full state names and two-letter state abbreviations.
  * `us_counties_fips` — Works on string fields that are five-character FIPS county codes for a US county. This layer works only on the interactive map.
  * `us_zipcode_tabulation_areas` — Works on string fields that are five-character US zip codes. Dimensions of `type: zipcode` automatically use the `us_zipcode_tabulation_areas` map layer.
> Zip code regions are based on the 2010 zip code tabulation areas (ZCTAs), so this map layer does not include many zip codes, such as those assigned to P.O. boxes, that do not map directly to regions.


## Example
```
dimension: state {
  map_layer_name: us_states
  sql: ${TABLE}.state ;;
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


