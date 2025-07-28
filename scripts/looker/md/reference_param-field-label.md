# label (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-label

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  label (for fields)
Stay organized with collections  Save and categorize content based on your preferences. 
> This section refers to the `label` parameter that is part of a field.
> `label` can also be used as part of a model, described on the `label` (for models) parameter documentation page.
> `label` can also be used as part of an Explore, described on the `label` (for Explores)  parameter documentation page.
> `label` can also be used as part of a view, described on the `label` (for views) parameter documentation page.
> `label` can also be used as part of a reference line, described on the Dashboard reference line parameters documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    label: "desired label name"
  }
}

```
Hierarchy `label` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, ParameterAccepts A string  
---|---  
## Definition
`label` helps make Explores more user-friendly by allowing you to choose how field names appear in the field picker and in the data table of an Explore. If no label is specified, the label defaults to the name of the field.
### Liquid variables with `label`
You can use Liquid variables with the `label` parameter. Liquid variables let you access data such as information about a model or Explore, filters applied to a field, and user attribute values. You can use Liquid variables to dynamically change the `label` value, thus changing the field's appearance in the field picker and data visualizations.
> Liquid variables that return a value based on a filter, such as `_filters`, or require that a query be run first, such as `in_query`, will not change the name of the field in the field picker. In those cases, the field name will only be changed in the resulting visualization.
For example, the Liquid variable `{{ _user_attributes['name_of_attribute'] }}` replaces the Liquid variable with the value of the specified user attribute. If a user had a user attribute called **name** with a value of "John Smith", the following `label` syntax would change the name of the field in the field picker to **John Smith** :
```
label: "{{ _user_attributes['name'] }}"

```

In the next example, the `name` dimension uses the Liquid `{% if %} {% else %} {% endif %}` structure with the `_user_attributes['name_of_attribute']` Liquid variable to change its `label` value depending on a **company** user attribute:
```
dimension: name {
  label: "{% if _user_attributes['company'] == 'Looker' %} Employee Name {% else %} Customer Name {% endif %}"
  sql: ${TABLE}.name ;;
}

```

You can see additional examples of using `label` with Liquid variables to define dynamic labels in the Interesting ways to use Liquid in labels Best Practices page.
## Example
Make this measure appear as **# of Customers** instead of **Customer Count Distinct** in the field picker.
```
measure: customer_count_distinct {
  label: "# of Customers"
  type: count_distinct
  sql: ${customer.id} ;;
}

```

## Things to consider
### The IDE flags duplicate labels in a view
To prevent duplicate field labels in the same view, the Looker IDE presents an information icon by the line number of any duplicate field labels in a LookML view file. If you hover over the information icon by the line number, the tooltip indicates that there is already a field with the label in the view.
The Looker IDE will show this same information in the **Quick Help** panel if you select the text of the `label` statement in the IDE:
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


