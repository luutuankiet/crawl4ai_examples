# Best practice: Writing sustainable, maintainable LookML  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-write-sustainable-maintainable-lookml

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Use substitution operators
  * Define field sets
  * Avoid repeating code
  * Consolidate items like map layers and value formats
  * Create development guidelines




Was this helpful?
Send feedback 
#  Best practice: Writing sustainable, maintainable LookML
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Use substitution operators
  * Define field sets
  * Avoid repeating code
  * Consolidate items like map layers and value formats
  * Create development guidelines


> _These best practices reflect recommendations shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations; but, as always, please use your best judgment when implementing any of the suggestions on this page._
This page provides recommendations for writing sustainable, maintainable LookML. These recommendations are described in further detail in the following sections: 
  * Use substitution operators
  * Define field sets
  * Avoid repeating code
  * Consolidate items like map layers and value formats
  * Create development guidelines


## Use substitution operators
Substitution operators should be used throughout all LookML files. A LookML model should have only a single reference point to any object in the physical data model. Any subsequent definitions that need to reference that object should do so by pointing to the already defined LookML object. 
Use the syntax `${TABLE}.field_name` when referencing the underlying database table, for all base dimensions that are pulling data directly from underlying database columns. If a schema or table name changes, this enables a developer to update the schema or the table name in one place (within the `sql_table_name` parameter) and have it propagate through the rest of the code. 
Use the syntax `${field_name}` when referencing dimensions or measures that have already been defined within the LookML. If a column name changes, that change will only need to be updated in the `sql` parameter of the base dimension or measures. That change will then automatically propagate to all other fields that reference the column. For example, if a column name in your database changes from `usersid` to `users_id`, you will need to change the reference in Looker. Using `${field_name}` means you only need to update one line. 
When multiple dimensions and measures reference an existing LookML field with `${TABLE}.field_name`, many changes are needed. For example, consider the `this_week_count` and `this_month_count` measures in the following example LookML code: 
```
dimension: usersid {
  type: number
  sql: ${TABLE}.usersid ;; # Change here
}

measure: this_week_count {
  type: count_distinct
  sql: ${TABLE}.usersid ;; # Change here
  filters: [created_date: "7 days"]
}

measure: this_month_count {
  type: count_distinct
  sql: ${TABLE}.usersid ;; # Change here
  filters: [created_date: "1 month"]
}

```

Since both `this_week_count` and `this_month_count` use the syntax `${TABLE}.usersid` in the `sql` parameter, it will be necessary to update the `sql` parameter for all three fields. 
With the reference `${field_name}`, only one change is needed: 
```
dimension: usersid {
  type: number
  sql: ${TABLE}.usersid ;; # Change here
}

measure: this_week_count {
  type: count_distinct
  sql: ${usersid} ;;       #Using ${field_name} to reference the LookML field `usersid`
  filters: [created_date: "7 days"]
}

measure: this_month_count {
  type: count_distinct
  sql: ${usersid} ;;       #Using ${field_name} to reference the LookML field `usersid`
  filters: [created_date: "1 month"]
}

```

For more uses of substitution operators, check out our Incorporating SQL and referring to LookML objects documentation page. 
## Define field sets
Use sets for maintaining reusable field lists within the model. Any lists of fields that are repeated, whether with the `fields` parameter or within drill fields, should be incorporated into sets in order to create a single place in the model where that field list can be updated or field references changed. You can find more about sets on the documentation page for the `set` parameter. 
## Avoid repeating code
Think of LookML objects as building blocks, and use the `extends` parameter to combine objects together in different ways without repeating code. You can find detailed information and examples of reusing code on the Reusing code with extends documentation page. You can see additional examples on the `extends` (for views) and `extends` (for Explores) parameter documentation pages as well as in the Using extensions to define joins Community post. 
Maintain consistency across Explores by not repeating code in multiple places. For additional ideas on how to accomplish this, see the Looker Community post on avoiding inconsistencies across Explores. 
## Consolidate items like map layers and value formats
Define custom map layers centrally in a LookML file called `map_layers.lkml`, which you can create by following Looker's documentation on project files. This file can then be included as needed across models. Alternatively, add JSON files directly to the repository by dragging and dropping data files into your LookML project, and reference them within the model. 
For example, suppose you have a map layers file, `map_layers.base.lkml`, containing the following LookML code: 
```
map_layer: example_africa {
  file: "africa_file_name.json"
  property_key: "geounit"
}

map_layer: example_asia {
  file: "asia_file_name.json"
  property_key: "geounit"
}

map_layer: example_europe {
  file: "europe_file_name.json"
  property_key: "geounit"
}

```

You can include the map layers file `map_layers.base.lkml` in any model in the project by adding the LookML code `include: "map_layers.base.lkml"` to the desired model file. 
Set any custom value formats centrally within the model. Use the `named_value_format` parameter to set any custom formats within the model, and then reference those using the `value_format_name` parameter in dimensions and measures. 
## Create development guidelines
Define development guidelines to make it easier to develop and scale a LookML model. See the Looker Community post on example LookML development guidelines for a walkthrough of a sample development guideline list. Common guidelines include requirements for: 
  * Clearly organizing LookML files so they are consistent and easy to navigate
  * Using comments throughout the views and models to add context to the LookML that is written
  * Creating documentation within Looker using Markdown files


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


