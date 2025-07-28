# map_layer  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-map-layer

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Definition
    * Built-in map layers
    * Specifying a map layer
  * Things to know
    * Static map (regions) charts
    * Using map_layer with IDE folders




Was this helpful?
Send feedback 
#  map_layer
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Definition
    * Built-in map layers
    * Specifying a map layer
  * Things to know
    * Static map (regions) charts
    * Using map_layer with IDE folders


## Usage
```
map_layer: company_regions {
  feature_key: "ISO_A3"
  file: "/map_folder/regions.json"
  format: topojson
  label: "desired label for chart visualization"
  max_zoom_level: 12
  min_zoom_level: 2
  projection: airy
  property_key: "ISO_A3"
  property_label_key: "NAME"
}

```

Hierarchy `map_layer` |  Default Value NoneAccepts An identifier for your map layer, plus subparameters defining your map layer properties.   
---|---  
## Definition
The `map_layer` parameter lets you define a custom map layer that can then be used to plot regional data, such as counties or zip codes, in Looker and create map charts.
When a map layer exists, typically the interactive map visualization is chosen as the default map visualization. The one exception is the US States map, where Looker uses the Static Map Region chart by default because it uses insets for Alaska and Hawaii.
Map layers can accept TopoJSON or GeoJSON files.
For more information about creating a custom map layer file, see the Creating custom map regions Best Practices page.
> Looker recommends that you keep custom map layer files smaller than 5 MB to avoid overwhelming the user's browser tab.
### Built-in map layers
Looker includes several built-in map layers. Before creating your own map layers, check whether you can use one of the built-in map layers:
> The `countries` and `us_states` built-in map layers use proper capitalization for the names of countries and states. Data is plotted to the map layer in a case-sensitive fashion, so your data must also use proper capitalization in order to use these built-in map layers. For example, if your dataset uses lower case "new delhi," the data would not correctly plot on the built-in map layers, which use "New Delhi."
  * `countries` — Accepts full country names, ISO 3166-1 alpha-3 three-letter country codes, or ISO 3166-1 alpha-2 two-letter country codes. Note that you must use only one of these three options in your dataset; you cannot use a mix of these options.
If your data uses ISO 3166-1 alpha-2, include the `map_layer_name` parameter in the definition for your country dimension to ensure that Looker recognizes your data as country codes and does not incorrectly interpret the data as state codes. For example:

```
  dimension: country {
      type: string
      map_layer_name: countries
      sql: ${TABLE}.country ;;
  }

```

  * `uk_postcode_areas` — Accepts UK postcode areas (for example, `L` for Liverpool, `RH` for Redhill, or `EH` for Edinburgh).
  * `us_states` — Accepts full state names and two-letter state abbreviations.
  * `us_counties_fips` — Works on string fields that are five-character FIPS county codes for a US county. This layer works only on the interactive map.
  * `us_zipcode_tabulation_areas` — Works on string fields that are five-character US zip codes. Dimensions of `type: zipcode` automatically use the `us_zipcode_tabulation_areas` map layer.
> Zip code regions are based on the 2010 zip code tabulation areas (ZCTAs), so this map layer does not include many zip codes, such as those assigned to P.O. boxes, that do not map directly to regions.


### Specifying a map layer
The location of the map can be specified using either the name of a file or a URL.
When using a GeoJSON file, you only need to reference the `file` subparameter. The general syntax for adding a GeoJSON map layer is:
```
map_layer: identifier {
  file: "/file_path/file_name.geojson"
}

```

The general syntax for adding a TopoJSON map layer is:
```
map_layer: identifier {
  extents_json_url: "string"
  feature_key: "string"
  file: "/file_path/file_name.json" # or use the url subparameter
  format: topojson | vector_tile_region
  label: "string"
  max_zoom_level: number
  min_zoom_level: number
  projection: airy  # or one of many other choices
  property_key: "string"
  property_label_key: "string"
  url: "string" # or use the file subparameter
}

```

Where:
Parameter | Type | Description  
---|---|---  
`identifier` | String | Name of the map as you will refer to it in LookML.  
`file` | String | Location of the map, specified by the name of a JSON file from your LookML project. The file must be in TopoJSON or GeoJSON format and have a `.json`, `.geojson`, or `.topojson` file extension. `"/maps/countryobjects.json"` for a file in the `/maps/` directory. If the JSON file is in the root directory and not in a folder, you can indicate the root directory with a single forward slash, like this: `"/countryobjects.json"` **Data** section of the LookML IDE's file list. See the Examples section later on this page for the LookML for each of these scenarios.  
`extents_json_url` | String | The URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by `property_key`) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of `property_key`. For example, `extents_json_url: "https://mycompany.com/mapserver/json-extent.js"`. If using this parameter, you must specify your map location using the `url` parameter.  
`feature_key` | String | Name of the TopoJSON object that the map layer references. If not specified, the first object will be used.  
`format` | Keyword `topojson` or `vector_tile_region` | Data format of the region information. Typically people use `topojson`.  
`label` | String | Displayed in the chart configuration UI.  
`max_zoom_level` | Number | Maximum zoom level for zooming in the map layer, for visualizations that support zooming.  
`min_zoom_level` | Number | Minimum zoom level for zooming in the map layer, for visualizations that support zooming.  
`projection` | Keyword | Preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections. The LookML editor lists the many available projections when you add a projection parameter.  
`property_key` | String | Property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. By default, the first matching property is used. If there's a particular metadata property you want to plot against, specify it here.  
`property_label_key` | String | Property from the TopoJSON data to use to label the region. This is useful when the mapping value (defined by `property_key`) is not very human-readable.  
`url` | String | Location of the map, specified by a URL that contains your map file.  
## Examples
When possible, add your map file into your project and then use the `file` parameter to point to the map file.
You must use the full file path for the JSON file. If your project is not enabled for folders, Looker displays JSON files in the **Data** section of the LookML IDE's file list.
For example, if your project is enabled for folders and you have a custom map of neighborhoods called `my_neighborhoods.json` in a directory called `maps`, you would use the full file path like this:
```
map_layer: neighborhoods {
  file: "/maps/my_neighborhoods.json"
}

```

If your project doesn't use folders, uploaded map files are displayed in the project's **Data** section. In this case, you can just provide the name of the `my_neighborhoods.json` file:
```
map_layer: neighborhoods {
  file: "my_neighborhoods.json"
}

```

Alternatively, you could specify that a custom `neighborhoods` map is hosted elsewhere, such as at `https://wherever.com/my_neighborhoods.json`:
```
map_layer: neighborhoods {
  url: "https://wherever.com/my_neighborhoods.json"
}

```

After the map layer is defined (by specifying a file or using the `url` parameter) you can specify that a dimension's values should be associated with a geographic region on your custom map. In the dimension, use the `map_layer_name` parameter to specify the name you used in the `map_layer` parameter.
```
dimension: neighborhood {
  type: string
  map_layer_name: neighborhoods    # this is your map layer
  sql: ${TABLE}.neighborhood_code
}

```

When you query this dimension and open the visualization section, Looker charts the data using the `neighborhoods` JSON file, as defined in the `map_layer` parameter in your model file.
## Things to know
### Static map (regions) charts
Setting **Map** to **Auto** in Static Map (Regions) charts relies on having `map_layer` specified in the LookML model specifying a map layer. Without that parameter set, users get an error if they select **Auto** but can still use Looker's built-in maps.
### GeoJSON files
Similar to TopoJSON files, GeoJSON files can have either the `.geojson` or the `.json` file extension but must contain geographic data in GeoJSON format. When using a GeoJSON file, you only need to reference the `file` subparameter.
### Using `map_layer` with IDE folders
If you have IDE folders enabled for your project, you need to use the file path when you specify a project file for `map_layer`:
```
map_layer: neighborhoods {
  file: "/maps/my_neighborhoods.json"
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


