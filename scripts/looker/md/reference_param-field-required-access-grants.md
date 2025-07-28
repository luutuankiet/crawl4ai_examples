# required_access_grants (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-required-access-grants

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  required_access_grants (for fields)
Stay organized with collections  Save and categorize content based on your preferences. 
> This page refers to the `required_access_grants` parameter that is part of a dimension, dimension group, measure, filter, or parameter.
> `required_access_grants` can also be part of an Explore, described on the `required_access_grants` (for Explores) parameter documentation page.
> `required_access_grants` can also be part of a join, described on the `required_access_grants` (for joins) parameter documentation page.
> `required_access_grants` can also be part of a view, described on the `required_access_grants` (for views) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    required_access_grants: [access_grant_name, access_grant_name, ...]
  }
}

```

Hierarchy `required_access_grants` |  Possible Field Types Dimension, dimension group, measure, filter, parameterAccepts Square brackets containing a comma-separated list of access grant names  
---|---  
## Definition
`required_access_grants` pairs with the model-level `access_grant` parameter to limit access for a field to only those users who have a specific user attribute value assigned to them.
`required_access_grants` works like this:
  1. You define an access grant using the `access_grant` parameter. As part of the definition, you associate the access grant with a user attribute. You also specify which user attribute values provide access to the access grant.
  2. Next, you use `required_access_grants` to restrict the field to only those users who have access to every access grant listed.


For example, the following LookML requires that users have access to both the `can_view_financial_data` and the `view_payroll` access grants to see the `salary` dimension:
```
dimension: salary {
  ...
  required_access_grants: [can_view_financial_data, view_payroll]
}

```

Users who don't have access to _all_ of the access grants assigned to the field won't have access to the field. They won't see the field in the field picker while exploring. If users view a Look that includes the restricted field, they will see a warning message saying, "`<view.field>` no longer exists on `<view>`, or you don't have access to it, and it will be ignored." The warning message is suppressed on dashboard tiles.
For more information on how to define an access grant, see the `access_grant` documentation page.
## Example
Expose the `salary` dimension to only those users who have access to the `payroll` access_grant:
```
dimension: salary {
  type: number
  required_access_grants: [payroll]
}

```

## Additional considerations
### Viewing restricted views with calculated fields on saved looks and dashboards
Since users who don't have access to a restricted field cannot access that field, this can cause changes in viewed data in a saved Look or dashboard tile.
For example, a query that uses a restricted dimension won't have access to the data in the restricted dimension, so the measure aggregation occurs without that data. Thus, users who don't have access to the restricted dimension will see different results in the measure than users who do have access to the restricted dimension.
Table calculations based on a restricted field display an error for users who don't have access to the restricted field, since the table calculation does not have access to the restricted field.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


