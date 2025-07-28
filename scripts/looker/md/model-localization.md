# Localizing your LookML model  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/model-localization

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Localizing labels and descriptions in your model
  * Creating locale strings files
  * Adding localization settings to your project's manifest file
    * localization_level
  * Assigning users to a locale
  * Setting locale for signed embed users
  * Using locale in Liquid variables
  * Understanding how localization rules apply to extended and refined objects




Was this helpful?
Send feedback 
#  Localizing your LookML model
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Localizing labels and descriptions in your model
  * Creating locale strings files
  * Adding localization settings to your project's manifest file
    * localization_level
  * Assigning users to a locale
  * Setting locale for signed embed users
  * Using locale in Liquid variables
  * Understanding how localization rules apply to extended and refined objects


With model localization, you can customize how your model's labels and descriptions display according to a user's locale.
Localization doesn't have to be based on geographic location or language. You can use locales to represent other distinguishing factors, such as internal versus external users, or managers versus individual contributors, and customize your labels and descriptions accordingly.
This page describes the steps for localizing your project:
  1. Determine which elements will be localized by adding labels, group labels, and descriptions to your model.
  2. Provide the localization definitions for your project by creating locale strings files.
  3. Enable localization for your project by adding localization settings to the project's manifest file.
  4. Determine the display for different users by assigning users to locales.


Model localization often occurs in conjunction with an admin who specifies number format localization and user-interface language settings.
## Localizing labels and descriptions in your model
You can localize labels, group labels, and descriptions in your model, including the following:
  * `label` for field, model, Explore, or view
  * `label` for applications in the Looker extension framework
  * `group_label` for Explore and `group_label` for field
  * `group_item_label` for field
  * `description` for Explore and `description` for field


You can also create localized LookML dashboards in your project. The following LookML dashboard parameters can be localized:
  * `text` (which is a subparameter of the `note` parameter and can be applied to all dashboard element types, besides elements of `type: text`)


To see all fields in your project that can be localized, you can set your project's localization level to `strict`. With this setting, the Looker IDE returns a LookML validation error for any LookML elements that can be localized but that don't have labels, and for any strings in your LookML model that can be localized but that aren't defined in your locale strings files.
In the following sample LookML, labels are provided for the `flights` view and the `id`, `country`, and `number_of_engines` fields. A description is also provided for the `country` field.
```
view: flights {
  label: "flight_info"
  sql_table_name: flightstats.accidents ;;

  dimension: id {
    label: "id"
    primary_key: yes
    type: number
    sql: ${TABLE}.id ;;
  }

  dimension: country {
    label: "country"
    description: "country_of_departure"
    type: string
    map_layer_name: countries
    sql: ${TABLE}.country ;;
  }

  dimension: number_of_engines {
    label: "number_of_engines"
    type: string
    sql: ${TABLE}.number_of_engines ;;
  }

  dimension: location {
    type: string
    sql: ${TABLE}.location ;;
  }
}

```

In the examples that follow on this page, we'll localize these values in the strings files using a `permissive` localization level. Notice that the `location` dimension does not have a label, so we can demonstrate how a dimension with no localization is displayed.
## Creating locale strings files
The locale strings files use key-value pairs to define how the labels and descriptions in your model are displayed for each locale. On the left side of each key-value pair is the _localization key_ , which is a label or description string from your model. The right side of the key-value pair is where you define how you want that string to be displayed in the Looker UI.
For each locale that you want to use for your project, you need to create a dedicated strings file. Create only one strings file for each locale. You must have a strings file that is named to match the default locale. For example, if you have specified `default_locale: en` in your project's manifest file, you must have a file in your model called `en.strings.json`. Each string must be defined in the _default_ locale strings file or it won't be localized.
This example of an `en.strings.json` file will be utilized for all users who have the **Locale** value of `en`. In the following sample LookML, `en` is also specified as the default locale, so all strings must be defined in this file in order to be localized.
```
{
  "flight_info": "Flights",
  "id": "Identifier",
  "country_of_departure": "Country of Departure",
  "number_engines": "Number of Engines"
}

```

The following table shows what a user with their locale set to `en` would see in the data table of a Looker Explore:
Flights Identifier | Flights country | Flights Location | Flights Number of Engines  
---|---|---|---  
493 | Congo | Kisangani, Congo | 3  
2167 | Saudi Arabia | Riyadh, Saudi Arabia | 3  
2657 | Austria | Vienna, Austria | 2  
17992 | United States | Kansas City, MO | 2  
18893 | United States | Anchorage, AK | 4  
Note the following:
  * In the `flights` view sample LookML shown previously, we didn't provide a label at all for the `location` dimension, so Looker displays the dimension's name, capitalized: "Location".
  * We didn't define localization for the "country" label in our `en.strings.json` file, so Looker displays the label as it is defined in our view file, without capitalizing it: "country".


As another example, we can create an `es_ES.strings.json` file that is utilized for all users with a **Locale** value of `es_ES`:
```
{
  "flight_info": "Vuelos",
  "id": "Identificador",
  "country": "País",
  "country_of_departure": "País de Partida",
  "number_engines": "Número de Motores"
}

```

The following table shows what a user with their locale set to `es_ES` would see in Looker:
Vuelos Identificador | Vuelos country | Vuelos Location | Vuelos Número de Motores  
---|---|---|---  
493 | Congo | Kisangani, Congo | 3  
2167 | Saudi Arabia | Riyadh, Saudi Arabia | 3  
2657 | Austria | Vienna, Austria | 2  
17992 | United States | Kansas City, MO | 2  
18893 | United States | Anchorage, AK | 4  
Note the following:
  * As in the previous example, in the original view with labels and descriptions added, we didn't provide a label at all for the `location` dimension, so Looker displays the dimension's name, capitalized: "Location".
  * We didn't define localization for the "country" label in our `en.strings.json` file, which is our default locale strings file. So even though we _did_ define "country" in our `es_ES.strings.json` file, Looker does not localize this string, and displays the label as it is defined in our view file: "country".


## Adding localization settings to your project's manifest file
To enable localization for your project, add the `localization_settings` parameter to your project's manifest file.
In the manifest file, add your localization settings. Here's an example:
```
localization_settings: {
  default_locale: en
  localization_level: permissive
}

```

### `default_locale`
The `default_locale` parameter specifies the name of the default locale strings file in your project.
The default locale strings file determines which strings from your model are localized. Even if a label or description string is defined in another locale strings file, if it is not defined in the _default_ locale strings file then the Looker UI will display the unlocalized string.
The default locale _for your project_ is not to be confused with the default locale _for Looker users_. Your Looker admin can set a default locale for your instance. If no default is set, Looker will default to `en`. If your admin does not specifically enter a **Locale** value for a user or a user group the user belongs to, Looker assigns the user to the default instance locale. And, if the admin has not set a default instance locale, Looker assigns the user to the `en` locale.
For this reason, unless you are sure your Looker admin will be setting the **Locale** value for all your Looker users, you should set your project's `default_locale` parameter to the default locale for your instance (or to `en` if no default has been set), and define the localization for all your labels and descriptions in the `.strings.json` file for that locale.
### `localization_level`
The localization level of your project specifies whether unlocalized elements are allowed in your model:
  * Set the localization level to `strict` to require localized labels for all models, Explores, views, and fields in your project. The Looker IDE will return a LookML validation error for any of these elements that don't have labels, and for any labels and descriptions that aren't defined in the default locale strings file.
  * Set the localization level to `permissive` to allow elements without labels, and to allow labels and descriptions that aren't defined in the default localization strings file.


Even if you do want the `strict` localization level, it may be handy to set your project's localization level to `permissive` when you're developing your project to prevent validation errors. Once you've finished localizing all your labels and descriptions, you can set the localization level to `strict` to see any errors.
## Assigning users to a locale
Once you have your locale strings files set up, you can assign users to a locale that corresponds to one of the locale strings files. This can be done at the instance, user group, or individual user level, using the **Locale** field or `locale` user attribute.
For example, if you want a user to see the labels and descriptions defined in the `es_ES.strings.json` file, your Looker admin should set the user's **Locale** setting to `es_ES`.
Custom locales you create with string files can be entered in the **Locale** field by clicking the field and typing the string filename rather than selecting a built-in locale from the drop-down menu. For more information, see the Users documentation page.
## Setting locale for signed embed users
You can include a user's locale value in a signed embed URL just like any other user attribute. The exact format required for signed embeds depends on the programming language that is used to build your signed embed URL script, but the name of the user attribute is `locale`. See the Signed embedding documentation page for more information on signed embed URLs and tools for building your signed embed URL.
## Using locale in Liquid variables
As described previously, model localization lets you customize the display of your model's labels and descriptions for different locales. But you can also include localization keys in Liquid variables, which lets you localize your data values as well.
For example, in our default locale strings file named `en.strings.json`, we can create the localization keys `domestic` and `international` with the following entries:
```
{
  "domestic": "Domestic",
  "international": "International"
}

```

And then in our `es_ES.strings.json` file, we can provide Spanish versions of these localization keys: 
```
{
  "domestic": "Nacional",
  "international": "Internacional"
}

```

From there, we can use the `domestic` and `international` localization keys in Liquid variables to localize the output of a dimension:
```
dimension: from_US {
    label: "from_us"
    type: string
    sql: CASE
         WHEN ${TABLE}.country = 'United States' THEN '{{ _localization['domestic'] }}'
         ELSE '{{ _localization['international'] }}'
         END;;
  }

```

Users with the `en` locale will see the following results:
Flights Identifier | Flights country | Flights From the US?  
---|---|---  
289 | United States | Domestic  
400 | Canada | International  
493 | Congo | International  
936 | United States | Domestic  
Users with the `es_ES` locale will see the following results:
Vuelos Identificador | Vuelos País | Vuelos ¿De Los Estados Unidos?  
---|---|---  
289 | United States | Nacional  
400 | Canada | Internacional  
493 | Congo | Internacional  
936 | United States | Nacional  
The users with the `es_ES` locale see the "Domestic" and "International" data localized to "Nacional" and "Internacional", respectively.
You can also use Liquid in LookML dashboard filters and LookML dashboard element filters to localize the default value in a filter. For example, if a LookML dashboard has a tile using data from this localized model, and there is a filter on that tile defined in LookML as follows:
```
filters:
  flights.from_US: "{{ _localization['domestic'] }}"

```

When a user with the `en` locale explores from that tile on the dashboard, the Explore will be filtered on the value **Domestic** for the **Flights From the US?** field, and the data table in the Explore will include the following results:
Flights Identifier | Flights country | Flights From the US?  
---|---|---  
289 | United States | Domestic  
936 | United States | Domestic  
When a user with the `es_ES` locale explores from that tile on the dashboard, the Explore be filtered on the value **Nacional** for the **Vuelos ¿De Los Estados Unidos?** field, and the data table in the Explore will include the following results:
Vuelos Identificador | Vuelos País | Vuelos ¿De Los Estados Unidos?  
---|---|---  
289 | United States | Nacional  
936 | United States | Nacional  
## Understanding how localization rules apply to extended and refined objects
Be aware that localization rules apply when you are extending views, Explores, or LookML dashboards, and when you are refining views or Explores.
If you have extended or refined an object and then added new labels or descriptions, you should provide localization definitions in the locale strings files.
For example, if we have a `flights` view:
```

view: flights {
  label: "flight_info"
  sql_table_name: flightstats.accidents ;;
  ...
}

```

And then we create a new view that extends the `flights` view:
```
include: "/views/flights.view"

view: flights_enhanced {
  extends: [flights]
  label: "enhanced_flight_info"
}


```

In our locale strings files we would need to define both of the view label strings (`"flight_info"` and `"enhanced_flight_info"`). If the project's localization level is set to `strict`, we wouldn't be able to commit any updates until we defined the new labels or descriptions.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


