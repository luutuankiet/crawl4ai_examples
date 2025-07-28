# Best practice: What to do and what not to do with LookML  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/best-practices-lookml-dos-and-donts

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Best practice: What to do and what not to do with LookML
Stay organized with collections  Save and categorize content based on your preferences. 
These best practices reflect recommendations that were shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations, but — as always — use your best judgment when implementing any of the recommendations that are shared on this page. 
## Do this with LookML
  * **Do** : Define the `relationship` parameter for all joins. `many_to_one` join relationship for any joins in which a relationship is not defined. For additional information on defining the `relationship` parameter correctly, see the Best Practices page on getting the `relationship` parameter right. 
  * **Do** : Define a primary key within each and every view, including derived tables. _unique value_ to enable Looker to uniquely identify any given record. This primary key can be a single column or a concatenation of columns — it simply needs to be a unique identifier for the table or derived table. 
  * **Do** : Name dimensions, measures, and other LookML objects, using all lowercase letters and underscores for spaces. `label` parameter can be used for additional formatting of a name field, and can also be used to customize the appearance of view names, Explore names, and model names. For example, in the following LookML, the `label` parameter is used to assign the label **Number of Customers** to the `customer_count_distinct` measure. ```
      measure: customer_count_distinct {
        label: "Number of Customers"
        type: count_distinct
        sql: ${customer.id} ;;
      }
```

  * **Do** : Use datagroups to align generation of persistent derived tables (PDTs) and Explore caching with underlying ETL processes. Datagroups can also be used to trigger deliveries of dashboards or Looks to ensure that up-to-date data is sent to recipients. 


## Don't do this with LookML
  * **Don't** : Use the `from` parameter for renaming views within an Explore. `view_label` parameter instead. For more on the difference between `from` and `view_label`, check out the `from` (for Explores) parameter documentation page. The `from` parameter should primarily be used in the following situations: 
    * Polymorphic joins (joining the same table multiple times) 
    * Self-joins (joining a table to itself) 
    * Re-scoping an extended view back to its original view name 
  * **Don't** : Use the word "date" or "time" in a dimension group name. `created_date` results in fields called, for example, `created_date_date` and `created_date_month`. Simply use `created` as the dimension group name, because this results in fields that are named, for example, `created_date` and `created_month`. 
  * **Don't** : Use formatted timestamps within joins. raw timeframe option for joining on any date or time fields. This will avoid the inclusion of casting and timezone conversion in join predicates. 


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


