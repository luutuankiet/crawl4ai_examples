# Model parameters  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Parameter definitions




Was this helpful?
Send feedback 
#  Model parameters
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Parameter definitions


A model file specifies a database connection, defines the set of Explores that use that connection, and defines the Explores' relationships to other views. Unlike other LookML elements, a model is not declared with a specific "model" parameter. Instead, a LookML developer defines a model by creating a LookML project file that has the `.model.lkml` file extension. The model name is taken from the filename and must be unique across your instance, even within different projects.
A model file typically contains any `explore` declarations, along with a number of model-level settings.
This page links to the model-level LookML parameters. They are typically written at the top of the model file and shouldn't be nested within other parameters.
## Example usage
Hold the pointer over a parameter name to see a quick description. Click a parameter to visit its reference page. When a parameter can be set to one of several specific options, the default value is listed first.
```
## STRUCTURAL PARAMETERS
:"filename_or_pattern"
## Possibly more include declarations

: explore_name {
  # Desired explore parameters (described on Explore Parameters page)
}
## Possibly more explore declarations

: access_grant_name{
  : user_attribute_name
  : ["value_1", "value_2", ...]
}
## Possibly more access_grant declarations

: test_name{
  : explore_name {
    # Desired subparameters (described on test page)
  }
  : assert_statement {
    :Looker expression ;;
  }
  # Possibly more assert declarations
}
## Possibly more test declarations

## DISPLAY PARAMETERS
: "desired label"

## FILTER PARAMETERS
: yes | no

## QUERY PARAMETERS
: "connection_name"
: datagroup_name{
  : "desired label"
  : "desired description"
  : "N (minutes | hours | days)"
  : SQL query ;;
}
## Possibly more datagroup declarations
: N
: "N (seconds | minutes | hours)"
: datagroup_name
: monday | tuesday | wednesday | thursday | friday | saturday | sunday

## VISUALIZATION AND FORMATTING PARAMETERS
: map_name{
  : "URL to JSON extents file"
  : "Name of TopoJSON object"
  : "TopoJSON or GeoJSON filename" # or use the url subparameter
  : topojson | vector_tile_region
  : "desired label"
  : number indicating max zoom
  : number indicating min zoom
  : Preferred geographic projection
  : "TopoJSON property"
  : "Label for TopoJSON property"
  : "URL that contains map file" # or use the file subparameter
}
## Possibly more map layer declarations

: desired_name {
  : "excel formatting string"
  : yes | no
 }
## Possibly more named value format declarations

```

## Parameter definitions
Parameter Name | Description  
---|---  
Structural Parameters  
Creates an access grant that limits access of LookML structures to only those users who are assigned an approved user attribute value. This parameter has the `user_attribute` and `allowed_values` subparameters.  
Exposes a view in the Explore menu. For more information about Explores and their parameters, see the Explore Parameter Reference page.  
Adds files to a model  
Creates a data test to verify your model's logic. The project settings include an option to require data tests. When this is enabled for a project, developers on the project must run data tests before deploying their changes to production. This parameter has the `explore_source` and `assert` subparameters.  
Display Parameters  
`label` (for model) | Changes the way a model appears in the Explore menu  
Filter Parameters  
`case_sensitive` (for model) | Specifies whether filters are case-sensitive for a model  
Query Parameters  
Changes the database connection for a model  
Creates a datagroup-caching policy for a model. This parameter has the `label`, `description`, `max_cache_age`, and `sql_trigger` subparameters.  
Specifies the month your fiscal year begins (if it differs from the calendar year)  
`persist_for` (for model) | Changes the cache settings for a model  
`persist_with` (for model) | Specifies the datagroup to use for the model's caching policy  
Specifies the day of the week on which week-related dimensions should start  
Visualization and Formatting Parameters  
`map_layer` (for model) | Creates custom maps to be used with `map_layer_name`  
Creates a custom value format to be used with `value_format_name`. This parameter has the `value_format` and `strict_value_format` subparameters.  
Parameters to Avoid  
Removed 3.52  No longer required  
Removed 3.30  No longer required  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


