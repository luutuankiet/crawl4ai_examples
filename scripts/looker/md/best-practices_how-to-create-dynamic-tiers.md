# Creating dynamic tiers  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-create-dynamic-tiers

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Creating dynamic tiers
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Tiers can be a great way to bucket values. However, with LookML `type: tier` dimensions, those buckets are predefined and static. Sometimes you may want to create a dynamic tier that lets users change the bucket size. You can do this in Looker using filter-only fields (called `parameter` parameters) in conjunction with a templating language (called Liquid). 
You can also use custom binning to create dynamic tiers natively in Explores when you have permission to create or edit custom fields. 
To create a dynamic tier: 
  1. Create a parameter of `type: number` to serve as the frontend filter field where the user can enter the numerical bucket size they would like. 
  2. Create a dimension that references the parameter value with the Liquid variable `{% parameter parameter_name %}`. This dimension determines the various buckets and will dynamically change the bucket size to the value entered by the user in the frontend filter field (the `parameter` parameter). 


For example, a developer creates a dynamic age tier that lets users bucket age values by custom ranges: 
> The SQL syntax for the following example may need to be adapted to suit your database dialect. 
```
  parameter: age_tier_bucket_size {
    type: number
  }

  dimension: dynamic_age_tier {
    type: number
    sql: TRUNCATE(${TABLE}.age / {% parameter age_tier_bucket_size %}, 0)
          * {% parameter age_tier_bucket_size %} ;;
  }

```

A user can now choose tier values for the **Age** column in an Explore. For example, a user might want to see ages grouped into 10-year buckets and so enter the value **10** in the **Age Tier Bucket Size** filter: 
The SQL expression in the `dynamic_age_tier` dimension divides an age value from the underlying `${TABLE}.age` column — for example, 25 — by the parameter value of 10, resulting in 2.5. The value 2.5 is truncated to 2 by the `TRUNCATE` function and is multiplied by the parameter value 10, resulting in 20. 20 becomes the bucket; any age value between 20 and 29 is included in the **20** bucket. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


