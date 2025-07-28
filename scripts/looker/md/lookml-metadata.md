# Metadata for LookML objects  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/lookml-metadata

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Metadata for models
  * Metadata for views
  * Metadata for Explores
  * Metadata for fields
  * Metadata for extensions
  * Metadata for refinements
  * Metadata for imported projects




Was this helpful?
Send feedback 
#  Metadata for LookML objects
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Metadata for models
  * Metadata for views
  * Metadata for Explores
  * Metadata for fields
  * Metadata for extensions
  * Metadata for refinements
  * Metadata for imported projects


Users who have `develop` permission can view contextually relevant information about the objects in the Looker IDE metadata panel.
To view the metadata panel in the Looker IDE:
  1. Navigate to your project files.
  2. To open the quick help panel, select the **Quick Help** icon info.
  3. In the LookML code editor, place your cursor on the object that you want more context about in the metadata panel.
  4. In the quick help panel, select the **Metadata** tab to open the metadata panel.


The metadata panel identifies the object with a name and an icon that represents the object type (see the Navigating projects with the object browser panel documentation page for all the possible object type icons).
If a LookML objects is used in multiple models, the metadata panel provides a drop-down menu that lets you select the model for which you want to see metadata.
The information that displayed in the metadata panel depends on the type of LookML object that you selected, as well as how the selected object is used in your project. You can use metadata to better understand many aspects of your project, as described in the following sections.
## Metadata for models
If you select a model file, the metadata panel displays the following sections:
  * **Dashboards** : Lists any LookML dashboards that are included in the model, with links to their definitions within your LookML project
  * **Explores** : Lists any Explores that are included in the model, with links to their definitions within your LookML project
  * **Views** : Lists any views that are included in the model, with links to their definitions within your LookML project


The heading for each section also displays the number of each type of object.
## Metadata for views
If you select a view parameter, the metadata panel displays the following information about how the view is used in your project:
  1. **View name and details** : The view name and an icon that represents the view's object type (see the Navigating projects with the object browser panel documentation page for all the possible object type icons). The metadata panel also provides the filename and the line number where the view is defined in the file's LookML (and a link to the view in your project).
  2. **Used in [number] models menu** : Displays a list of models that include this view, where **[number]** represents the count of models that include the view. For example, if a view is used within two models, the metadata panel displays the text **Used in 2 models**.
  3. **Primary key** : The view's primary key.
  4. **Base view of** : Explores that use this view as their base view.
  5. **Joined in** : Explores into which this view is joined.


If the view has extensions or refinements, these will also be displayed in the metadata panel.
## Metadata for Explores
If you select an `explore` parameter, the metadata panel shows you the following information about how the Explore is used in your project:
  1. **Explore name and details** : The Explore name and an icon that represents its object type (see the Navigating projects with the object browser panel documentation page for all the possible object type icons). The metadata panel also provides the filename and the line number where the Explore is defined in the file's LookML (and a link to the Explore in your project).
  2. **Base view** : The base view for the Explore (the view that is used as the starting point for building the Explore).
  3. **Joined views** : Other views that are joined into the base view.


If the Explore has extensions or refinements, these will also be displayed in the metadata panel.
## Metadata for fields
If you select a field, the metadata panel shows you the following information about how the field is used in your project:
  1. **Field name and details** : The field name and an icon that represents its object type (see the Navigating projects with the object browser panel documentation page for all the possible object type icons). The metadata panel also shows the field's type and provides the filename and the line number where the field is defined in the file's LookML (and a link to the field in your project).
  2. **Used in [number] models menu** : Displays a list of models that include the view for this field.
  3. **Exists in view** : Views that use this field.


## Metadata for extensions
When you select a `view` or an `explore` parameter in the LookML code editor, the **Extended by** section of the metadata panel shows any extensions of that object.
For example, consider the following sample LookML code for a model file in which the `aircraft_extended` Explore extends the `aircraft` Explore:
```
explore: aircraft {
  view_name: aircraft
  join: aircraft_types {
    type: left_outer
    sql_on: ${aircraft.aircraft_type_id} = ${aircraft_types.aircraft_type_id} ;;
    relationship: many_to_one
  }

  join: aircraft_engine_types {
    type: left_outer
    sql_on: ${aircraft.aircraft_engine_type_id} = ${aircraft_engine_types.aircraft_engine_type_id} ;;
    relationship: many_to_one
  }
}

explore: aircraft_extended {
  extends: [aircraft]
  label: "Aircraft Extended"
}

```

If you select the LookML definition for the `aircraft` Explore, the metadata panel lists `aircraft_extended` in the **Extended by** section. Click the link in the **Extended by** section to navigate directly to the LookML where `aircraft_extended` is defined.
If you click in the definition of the `aircraft_extended` Explore, the metadata panel provides the following information about the extended `aircraft` Explore:
  * **Joined views** : Lists any views that are joined to the `aircraft` Explore.
  * **Extends** : Lists the object that the selected Explore extends. In this case, this is the `aircraft` Explore.


In these examples, the extending and extended `explore` parameters are next to each other in the same file, but this is not always the case. It's not obvious by looking a parameter if it is extended, especially since the extended and extending objects can be in different LookML files. The metadata panel gives you context about the related objects, no matter where the objects are defined.
## Metadata for refinements
The metadata panel makes it easy to see when a view or an Explore has refinements that have been added to the object. The **Refinements** section of the metadata panel displays the number of refinements that have been added to the object, and you can use the links to navigate to the LookML for each refinement.
As with extensions, you can't tell if an object is refined just by looking at the LookML, especially because the refinement LookML can be in a different file. The metadata panel lets you see if an object has been refined and, if it has, lets you navigate directly to the LookML for the refinement.
## Metadata for imported projects
The metadata panel includes information about objects from imported projects, including links to navigate to the imported file where the object is defined. For example, selecting the LookML for an Explore that is based on an imported view file will show the imported view file's information in the metadata panel.
From the metadata panel, you can click the link to navigate to the imported file where the object is defined.
In addition, you can click the objects that are in the imported projects folder in the IDE file browser to see metadata about the imported files.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


