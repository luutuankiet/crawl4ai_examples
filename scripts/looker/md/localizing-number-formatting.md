# Localizing number formatting  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/localizing-number-formatting

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Setting number formats for users
  * The Number format setting with other methods of number formatting
  * Overriding the Number format setting with strict_value_format




Was this helpful?
Send feedback 
#  Localizing number formatting
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Setting number formats for users
  * The Number format setting with other methods of number formatting
  * Overriding the Number format setting with strict_value_format


Looker's default number format setting for numbers that appear in data tables and visualizations is **1,234.56**. However, the number format can be set to any of the following:
  * **1,234.56** : Thousands separated with commas; decimals separated with a period
  * **1.234,56** : Thousands separated with periods; decimals separated with a comma
  * **1 234,56** : Thousands separated with spaces; decimals separated with a comma


### Setting number formats for users
You can set a number format through one of the following methods:
  * **To set a number format for individual users:** Select the desired format from the **Number format** drop-down menu on the **Edit User** page in the **Admin** panel and click **Save** at the bottom of the page.
  * **To set a number format for a user group:** Assign the desired format to the `number_format` user attribute for a particular user group. If users within the group have set a custom value for `number_format`, the custom value will override any value that you assign to the group. To prevent the `number_format` that you assign from being overriden, ensure that the **User Access** setting for the `number_format` user attribute is _not_ set to **Edit**.
  * **To set a number format for an entire instance:** Assign one of the codes in the previous table to the **Number format** field on the **Localization** page of the **Admin** panel.


The default number format in Looker — **1,234.56** — displays numbers in thousands separated with commas, and decimals separated with a period.
For example, suppose you have an Explore with a column chart and data table that displays values for **Orders Order Count** , **Order Items Average Sale Price** , and **Order Items Total Sales Price** grouped by **Orders Created Month**. Values with the default setting will take the format **x,xxx.xx**.
If you change the **Number format** setting to **1.234,56** , the values in visualizations and data tables will take the format **x.xxx,xx** :
### The Number format setting with other methods of number formatting
If you use the LookML parameters `value_format_name` or `value_format` to format fields in your models, the number format selected in the **Number format** setting or `number_format` user attribute is applied on top of the format given in the LookML parameters. For example, suppose you have a measure that represents the count of pies with a specified `value_format` defined in LookML:
```
measure:count{
type:count
value_format:"####.0\"pies\""
drill_fields:[detail*]
}

```

With the **Number format** setting set to **1.234,56** , and the LookML `value_format: "####.0\"pies\""`, visualizations and data tables display values in the format **xxxx,xx pies**. The **Number format** setting swaps a comma for the period for the `value_format: "####.0\"pies\""`. A **Count** of 9,849 pies will display as 9849,0 pies.
Similarly, if you use the **Value Format** field in a visualization's **Edit** menu, the number format that is set in the **Number format** setting or the `number_format` user attribute will be applied on top of the format that is specified in the visualization **Value Format** field.
For example, if a user inputs the format `###0.000` in the **Value Format** field for a column chart, and the **Number format** is set to **1.234,56** , the visualization will display values in the format **xxxx,xxxx**. The **Number format** setting swaps a comma for the period for the visualization **Value Format** setting `###0.000`. A **Count** of 8,474 orders in the visualization will appear as **8474,000**.
### Overriding the Number format setting with `strict_value_format`
Typically, the number formatting set in the **Number format** setting or `number_format` user attribute is applied on top of formats applied by LookML parameters.
However, if you want to create a number format that is not affected by the **Number format** setting or the `number_format` user attribute, you can use the `named_value_format` model parameter to create a number format and set its `strict_number_format` subparameter to `yes`. You can apply that format to fields by using the `value_format_name` parameter, and those fields will not be affected by the **Number format** setting or the `number_format` user attribute.
For example, suppose that a custom format called `dollar_formatting` is defined in a model file. The custom format has a `strict_value_format` subparameter that is set to `yes`:
```
named_value_format: dollar_formatting {
  value_format: "$#,###.00"
  strict_value_format: yes
}

```

The `order_items` view file in the project has two measures, `average_sale_price` and `average_spend_per_user`. The `dollar_formatting` custom format is applied to the `average_sale_price` measure, but not to the `average_spend_per_user`:
```
measure: average_sale_price {
  type: average
  value_format_name: dollar_formatting
  sql: ${sale_price} ;;
}

measure: average_spend_per_user {
    type: average
    sql: ${user_order_total_price} ;;
}

```

The number formatting in the **Number format** setting is set to **1.234,56**.
In data tables and visualizations, the values for the **Order Items Average Sale Price** measure will appear in the format **$x,xxx.xx** and will _not_ be affected by the **Number format** setting. For example, an **Average Sale Price** of 45.63 will appear as **$45.63** in visualizations and data tables.
In data tables and visualizations, the values for the **Order Items Average Spend per User** measure _will_ be affected by the **Number format** setting and will appear in the format **$x.xxx,xx**. For example, an **Average Spend per User** of 47.64 will appear as **$47,64** in visualizations and data tables.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


