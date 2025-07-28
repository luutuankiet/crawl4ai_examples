# Formatting data values with LookML  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/formatting-data-values

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Modifying formatting for data values
  * Modifying clickable actions for data values




Was this helpful?
Send feedback 
#  Formatting data values with LookML
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Modifying formatting for data values
  * Modifying clickable actions for data values


This page provides an overview of the LookML parameters that modify the appearance and behavior of the data values that are displayed in data tables and visualizations. For example, you can specify currency formatting so that a data value such as `1234` renders as `$1,234.00` in data tables and visualizations. You can also specify clickable behaviors for fields so that users can click the fields to trigger actions or follow links.
## Modifying formatting for data values
This section describes LookML parameters that change how data values appear to users.
Parameter | Description | Example  
---|---|---  
Use `value_format` to format the output of a `type: number` field using Excel-style options.`value_format` has no effect on fields that are not `type: number`. |  ```
measure: total_order_amount {
  type: sum
  sql: ${order_amount} ;;
  value_format: "$#,##0.00"
 }

```
  
Use `value_format` to format the output of a `type: number` field using a built-in or custom `named_value_format`.`value_format` and `value_format_name` have no effect on fields that are not `type: number`.  |  ```
measure: total_order_amount {
  type: sum
  sql: ${order_amount} ;;
  value_format_name: usd
}

```
  
Use the `style` parameter to change the formatting of fields of `type: tier`.`style` is the only LookML parameter that affects the formatting of `type: tier` fields.  |  ```
dimension: age_tier {
  type: tier
  tiers: [0, 10, 20, 30, 40, 50, 60, 70, 80]
  style: classic
  sql: ${age} ;;
}
  
```
  
Use the `html` parameter to apply HTML formatting to your field. |  ```
dimension: status {
  sql: ${TABLE}.status ;;
  html: {% if value == 'Shipped' or value == 'Complete' %}
      <p>✅ {{value}}</p>
    {% elsif value == 'Processing' %}
      <p>⏳ {{value}}</p>
    {% else %}
      <p>❌ {{value}}</p>
    {% endif %}
   ;;
}

```
  
Use the `sql` parameter to change your data values using SQL. |  ```
dimension: status {
  sql: CASE WHEN (${TABLE}.status = 'Shipped' OR ${TABLE}.status = 'Complete') ;;
     THEN CONCAT('✅ ', ${TABLE}.status)
   WHEN ${TABLE}.status = 'Processing'
     THEN CONCAT('⏳ ', ${TABLE}.status)
   ELSE
     CONCAT('❌ ', ${TABLE}.status)
   END ;;
}

```
  
## Modifying clickable actions for data values
This section describes LookML parameters that determine a field's behavior when clicking on data values in the data table or visualization. 
Parameter | Description | Example  
---|---|---  
Use `drill_fields` to specify which fields are displayed when the user drills into the data. Note that dimensions and measures have different drilling behavior.More powerful data drilling.  |  ```
dimension: country {
  sql: ${TABLE}.country ;;
  drill_fields: [state, city]
}

```
  
Use `action` to create a data action on a field, which lets users perform tasks in other tools directly from Looker.`...`) will appear next to the field in data tables. Clicking on the field or the ellipses will bring up a menu from which users can select an action or drill into the data.  |  ```
dimension: action_example {
  action: {
    label: "Send a Thing"
    url:
      "https://example.com/ping/{{value}}"
    form_url:
      "https://example.com/ping/{{value}}/form.json"
  }
}

```
  
Use `link` to create a link on a field.`...`) will appear next to the field in data tables. Clicking on the field or the ellipses will bring up a menu from which users can select a link or drill into the data.  |  ```
dimension: artist_name {
  link: {
    label: "Google"
    url: "http://www.google.com/search?q={{value}}"
    icon_url: "http://google.com/favicon.ico"
   }
}

```
  
Use `html` to write custom HTML formatting for a field. With HTML tags such as the `<a>` tag, you can specify one or more hyperlinks in your field.`...`) will appear next to the field in data tables, regardless of the `html` definition. Clicking on the field or the ellipses will bring up a menu from which users can select any available links or actions.  |  ```
dimension: artist_name {
  html: <p>{{value}}
    <a href="#drillmenu">Drill menu</a>,
    <a href="http://www.google.com/search?q={{value}}">
      Google search
    </a></p>;;
    sql: ${TABLE}.artist_name ;;
    type: string
}

```
  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


