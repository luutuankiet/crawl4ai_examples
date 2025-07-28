# LookML terms and concepts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/lookml-terms-and-concepts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * LookML project
    * Parts of a project
    * Where do LookML projects and files come from?
  * Major LookML structures
    * Dimension and measure fields
    * Project manifest files
  * Database connection
  * Case sensitivity




Was this helpful?
Send feedback 
#  LookML terms and concepts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * LookML project
    * Parts of a project
    * Where do LookML projects and files come from?
  * Major LookML structures
    * Dimension and measure fields
    * Project manifest files
  * Database connection
  * Case sensitivity


This page defines the following core terms and concepts, which you will likely encounter often during LookML development:
  * LookML projects
  * Major LookML structures (like models, views, and Explores)
  * Derived tables
  * Database connections
  * Case sensitivity


Looks and user-defined dashboards are not described on this page, as users create them without using any LookML. However, their queries rely on the underlying LookML elements that are discussed on this page.
See the Looker glossary for a comprehensive list of terms and definitions that are used throughout Looker. For a comprehensive overview of the LookML parameters you can use in a LookML project, see the LookML quick reference page.
See the Looker and Looker Studio shared terms and concepts documentation page for information about the nuances between similar terms and concepts in Looker and Looker Studio.
## LookML project
In Looker, a project is a collection of files that describe the objects, database connections, and user interface elements that will be used to carry out SQL queries. At the most basic level, these files describe how your database tables relate to each other and how Looker should interpret them. The files may also include LookML parameters that define or change the options that are presented in Looker's UI. Each LookML project resides in its own Git repository for version control.
Once you connect Looker to your database, you can specify the database connection to use for your Looker project.
You can access your projects from the **Develop** menu in Looker (see Accessing project files for details and other options).
See the Generating a model documentation page for information on creating a new project, and see the Accessing and editing project information documentation page for information on accessing and making changes to existing LookML projects.
### Parts of a project
As shown in the diagram, the following are some of the more common types of files in a LookML project:
  * A model contains information about which tables to use and how they should be joined together. Here you'll typically define the model, its Explores, and its joins.
  * A view contains information about how to access or calculate information from each table (or across multiple joined tables). Here you'll typically define the view, its dimensions and measures, and its field sets.
  * An Explore is often defined within a model file, but sometimes you need a separate Explore file for a derived table or to extend or refine an Explore across models.
  * A manifest file can contain instructions for using files imported from another project or for your project's localization settings.


In addition to model, view, Explore, and manifest files, a project can have other types of files related to things like built-in dashboards, documentation, localization, and more. See the LookML project files documentation page for more information about these types of files as well as the other types of files that you can have in your LookML project.
These files together make up one project. If you are using Git for version control, then each project is typically backed up by its own Git repository.
### Where do LookML projects and files come from?
The most common way to create LookML files is to generate a LookML project from your database. You can also create a blank project and manually create its LookML files.
When you generate a new project from your database, Looker creates a baseline set of files that you can use as a template for building out the project:
  * Multiple view files, one file for every table in the database.
  * One model file. The model file declares an Explore for every view. Each Explore declaration includes `join` logic to join any view that Looker can determine is related to the Explore.


From here, you can customize the project by removing unwanted views and Explores and by adding custom dimensions and measures.
## Major LookML structures
As shown in the parts of a project diagram, a project typically contains one or more model files, which contain parameters that define a model and its Explores and joins. In addition, projects typically contain one or more view files, each containing parameters that define that view and its fields (including dimensions and measures) and sets of fields. The project can also contain a project manifest file, which lets you configure project-level settings. This section describes those major structures.
### Model
A model is a customized portal into the database, designed to provide intuitive data exploration for specific business users. Multiple models can exist for the same database connection in a single LookML project. Each model can expose different data to different users. For example, sales agents need different data than company executives, and so you would probably develop two models to offer views of the database appropriate for each user.
A model specifies a connection to a single database. A developer also defines a model's **Explores** within the model file. By default, Explores are organized under the model name in which they are defined. Your users see models listed in the **Explore** menu.
See the Types of files in a LookML project documentation page for more information about model files, including the structure and general syntax of model files.
See the Model parameters documentation page for details about the LookML parameters that can be used in a model file.
### View
A view declaration defines a list of fields (dimensions or measures) and their linkage to an underlying table or derived table. In LookML a view typically references an underlying database table, but it can also represent a derived table.
A view may join to other views. The relationship between views is typically defined as part of an Explore declaration in a model file.
By default, view names appear at the beginning of dimension and measure names in the Explore data table. This naming convention makes it clear which view the field belongs to. In the following example, the view names **Orders** and **Users** are listed before the names of the fields in the data table:
See the Types of files in a LookML project documentation for more information about view files, including the structure and general syntax of view files.
See the View parameters documentation page for details about the LookML parameters that can be used in a view file.
### Explore
An Explore is a view that users can query. You can think of the Explore as a starting point for a query or, in SQL terms, as the `FROM` in a SQL statement. Not all views are Explores, because not all views describe an entity of interest. For example, a **States** view that corresponds to a lookup table for state names doesn't warrant an Explore, because business users never need to query it directly. On the other hand, business users probably want a way to query an **Orders** view, and so defining an Explore for **Orders** makes sense. See the Viewing and interacting with Explores in Looker documentation page for information on how users interact with Explores to query your data.
In Looker, your users can see Explores listed in the **Explore** menu. Explores are listed below the names of the models they belong to.
By convention, Explores are declared in the model file with the `explore` parameter. In this following example of a model file, the `orders` Explore for an ecommerce database is defined within the model file. The views `orders` and `customers` that are referenced within the `explore` declaration are defined elsewhere, in their respective view files.
```
connection: order_database
include: "filename_pattern"

explore: orders {
  join: customers {
    sql_on: ${orders.customer_id} = ${customers.id} ;;
  }
}

```

In this example, the `connection` parameter is used to specify the database connection for the model, and the `include` parameter is used to specify the files that will be available for the model to reference.
The `explore` declaration in this example also specifies join relationships between views. For details on `join` declarations, visit the section on joins on this page. Visit the Join parameters documentation page for more details about the LookML parameters that can be used with the `join` parameter.
### Dimension and measure fields
Views contain fields, mostly dimensions and measures, which are the fundamental building blocks for Looker queries.
In Looker, a dimension is a groupable field and can be used to filter query results. It can be any of the following:
  * An attribute, which has a direct association to a column in an underlying table
  * A fact or numerical value
  * A derived value, computed based on the values of other fields in a single row


In Looker, dimensions always appear in the `GROUP BY` clause of the SQL that Looker generates.
For example, dimensions for a **Products** view might include product name, product model, product color, product price, product created date, and product end-of-life date.
A measure is a field that uses a SQL aggregate function, such as `COUNT`, `SUM`, `AVG`, `MIN`, or `MAX`. Any field computed based on the values of other measure values is also a measure. Measures can be used to filter grouped values. For example, measures for a **Sales** view might include total items sold (a count), total sale price (a sum), and average sale price (an average).
The behavior and expected values for a field depend on its declared type, such as `string`, `number`, or `time`. For measures, types include aggregate functions, such as `sum` and `percent_of_previous`. For details, refer to dimension types and measure types.
In Looker, fields are listed on the **Explore** page in the field picker on the left side of the page. You can expand a view in the field picker to show the list of fields that are available to query from that view.
By convention, fields are declared as part of the view they belong to, stored in a view file. The following example shows several dimension and measure declarations. Notice the use of the substitution operator (`$`) to reference fields without using a fully scoped SQL column name.
Here are some example declarations of dimensions and measures:
```
view: orders {
  dimension: id {
    primary_key: yes
    type: number
    sql: ${TABLE}.id ;;
  }
  dimension: customer_id {
    sql: ${TABLE}.customer_id ;;
  }
  dimension: amount {
    type: number
    value_format: "0.00"
    sql: ${TABLE}.amount ;;
  }
  dimension_group: created {
    type: time
    timeframes: [date, week]
    sql: ${TABLE}.created_at ;;
  }
  measure: count {
    type: count           # creates sql COUNT(orders.id)
    sql: ${id} ;;
  }
  measure: total_amount {
    type: sum             # creates sql SUM(orders.amount)
    sql: ${amount} ;;
  }
}

```

You can also define a `dimension_group`, which creates multiple time-related dimensions at once, and `filter` fields, which have a variety of advanced use cases such as templated filters.
See the Field parameters documentation page for complete details on declaring fields and the various settings that can be applied to them.
### Joins
As part of an `explore` declaration, each `join` declaration specifies a view that can be joined into the Explore. When a user creates a query that includes fields from multiple views, Looker automatically generates SQL join logic to bring in all fields correctly.
Here is an example join in an `explore` declaration:
```
# file: ecommercestore.model.lookml

connection: order_database
include: "filename_pattern"   # include all the views

explore: orders {
  join: customers {
    sql_on: ${orders.customer_id} = ${customers.id} ;;
  }
}

```

For more details, visit the Working with joins in LookML documentation page.
### Project manifest files
Your project may contain a project manifest file, which is used for project-level settings such as those for specifying other projects to import into the current project, defining LookML constants, specifying model localization settings, and adding extensions and custom visualizations to your project.
Each project can have only one manifest file. The file must be named `manifest.lkml` and be located at the root level of your Git repository. When you're using folders in the IDE, make sure that the `manifest.lkml` file is kept at the root level of your project's directory structure.
To import LookML files from a different project, use the project manifest file to specify a name for your current project and the location of any external projects, which could be stored locally or remotely. For example:
```
# This project
project_name: "my_project"

# The project to import
local_dependency: {
  project: "my_other_project"
}

remote_dependency: ga_360_block {
  url: "https://github.com/llooker/google_ga360"
  ref: "4be130a28f3776c2bf67a9acc637e65c11231bcc"
}

```

After defining the external projects in the project manifest file, you can use the `include` parameter in your model file to add files from those external project to your current project. For example:
```
include: "//my_other_project/imported_view.view"
include: "//ga_360_block/*.view"

```

For more information, see the Importing files from other projects documentation page.
To add localization to your model, use the project manifest file to specify default localization settings. For example:
```
localization_settings: {
  default_locale: en
  localization_level: permissive
}

```

Specifying default localization settings is one step in localizing your model. For more information, see the Localizing your LookML model documentation page.
### Sets
In Looker, a **set** is a list that defines a group of fields that are used together. Typically, sets are used to specify which fields to display after a user drills down into data. Drill sets are specified on a field-by-field basis, so you get complete control over what data is displayed when a user clicks a value in a table or dashboard. Sets can also be used as a security feature to define groups of fields that are visible to specific users. The following example shows a set declaration in a view `order_items`, defining fields that list relevant details about a purchased item. Note that the set references fields from other views by specifying scope.
```
set: order_items_stats_set {
  fields: [
    id,  # scope defaults to order_items view
    orders.created_date,  # scope is "orders" view
    orders.id,
    users.name,
    users.history,  # show all products this user has purchased
    products.item_name,
    products.brand,
    products.category,
    total_sale_price
  ]
}

```

See the `set` parameter documentation page for complete usage details for sets.
### Drill down
In Looker, you can configure a field so that users can further drill down into the data. Drilling works both in query results tables and in dashboards. Drilling starts a new query that is restricted by the value that you click on.
Drill behavior is different for dimensions and measures:
  * When you drill on a dimension, the new query filters on the drilled value. For example, if you click the specific date in a query of customer orders by date, the new query will show orders only on that specific date.
  * When drilling on a measure, the new query will show the dataset that contributed to the measure. For example, when drilling on a count, the new query will show the rows to calculate that count. When drilling on max, min, and average measures, drilling still shows _all_ the rows that contributed to that measure. This means that drilling on a max measure, for example, shows _all_ the rows that were used to calculate the max value, not just a single row for the max value.


The fields to show for the new drill query can be defined by a set, or can be defined by the `drill_fields` parameter (for fields) or the `drill_fields` parameter (for views).
## Derived tables
A _derived table_ is a query whose results are used as if it were an actual table in the database. Derived tables are created by using the `derived_table` parameter in a `view` declaration. Looker accesses derived tables as though they were physical tables with their own set of columns. A derived table is exposed as its own view, and defines dimensions and measures in the same manner as conventional views. The view for a derived table can be queried and joined into other views, just like any other view.
Derived tables can also be defined as _persistent derived tables (PDTs)_, which are derived tables that are written into a scratch schema on your database and automatically regenerated on the schedule that you specify with a persistence strategy.
See the Derived tables in Looker documentation page for more information.
## Database connection
Another important element of a LookML project is the database connection that Looker uses to run queries on your database. A Looker admin uses the Connections page to configure database connections, and LookML developers use the `connection` parameter in a model file to specify which connection to use for the model. If you generate a LookML project from your database, Looker automatically populates the `connection` parameter in the model file.
## Case sensitivity
LookML is case-sensitive, so be sure to match the case when referring to LookML elements. Looker alerts you if you have referred to an element that doesn't exist.
For example, suppose you have an Explore called `e_flights_pdt`, and a LookML developer uses incorrect capitalization (`e_FLIGHTS_pdt`) to reference that Explore. In this example, the Looker IDE shows a warning that the Explore `e_FLIGHTS_pdt` does not exist. In addition, the IDE suggests the name of an existing Explore, which is `e_flights_pdt`:
However, if your project contained both `e_FLIGHTS_pdt` and `e_flights_pdt`, the Looker IDE would not be able to correct you, so you would have to be sure which version you intended. Generally, it's a good idea to stick with lowercase when naming LookML objects.
IDE folder names are also case-sensitive. You must match the capitalization of folder names whenever you specify file paths. For example, if you have a folder named `Views`, you must use this same capitalization in the `include` parameter. Again, the Looker IDE will indicate an error if your capitalization doesn't match an existing folder in your project:
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


