# required_access_grants (for views)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-required-access-grants

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Additional considerations
    * Viewing restricted views with calculated fields on saved Looks and dashboards
    * Restricting access to underlying LookML structures




Send feedback 
#  required_access_grants (for views)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * Additional considerations
    * Viewing restricted views with calculated fields on saved Looks and dashboards
    * Restricting access to underlying LookML structures


> This page refers to the `required_access_grants` parameter that is part of a view.
> `required_access_grants` can also be part of an Explore, described on the `required_access_grants` (for Explores)  parameter documentation page.
> `required_access_grants` can also be part of a join, described on the `required_access_grants` (for joins)  parameter documentation page.
> `required_access_grants` can also be part of a dimension, dimension group, measure, filter, or parameter, described on the `required_access_grants` parameter documentation page.
## Usage
```
view: view_name {
  required_access_grants: [access_grant_name, access_grant_name, ...]
}

```

Hierarchy `required_access_grants` |  Default Value NoneAccepts Square brackets containing a comma-separated list of access grant names  
---|---  
## Definition
`required_access_grants` pairs with the model-level `access_grant` parameter to limit access for a view to only those users who have a specific user attribute value assigned to them.
`required_access_grants` works like this:
  1. You define an access grant using the `access_grant` parameter. As part of the definition, you associate the access grant with a user attribute. You also specify which user attribute values provide access to the access grant.
  2. Next, you use `required_access_grants` to restrict a view to only those users who have access to every access grant listed.


For example, the following LookML requires that users have access to both the `can_view_financial_data` and the `view_payroll` access grants to see the `payroll` view:
```
view: payroll {
  ...
  required_access_grants: [can_view_financial_data, view_payroll]
}

```

Users who don't have access to _all_ of the access grants assigned to the view will not see any of the fields in the restricted view. They will not see those fields in the field picker while exploring. If the user views a Look that includes fields from the restricted view, they will see a warning message saying, "`<view.field>` no longer exists on `<view>`, or you do not have access to it, and it will be ignored." The warning message is suppressed on dashboard tiles.
For more information on how to define an access grant, see the `access_grant` parameter documentation page.
## Example
Expose the `payroll` dimension to only those users who have access to the `accounting` access grant:
```
view: payroll {
  ...
  required_access_grants: [accounting]
}

```

## Additional considerations
### Viewing restricted views with calculated fields on saved Looks and dashboards
Since users who do not have access to a restricted view cannot access the fields in the view, this can cause changes in viewed data in a saved Look or dashboard tile.
For example, a measure that uses a dimension from a restricted view will not have access to the data from that view, so the measure aggregation occurs without that data. Thus, users who do not have access to the restricted view sees different results than users who do have access to the restricted view.
Table calculations based on a field in a restricted view display an error for users who do not have access to the restricted view, since the table calculation does not have access to the field in the restricted view.
### Restricting access to underlying LookML structures
Restricting access to a view does not restrict access to its underlying LookML structures. So an unrestricted field that is part of other views will still be available if those views are unrestricted. Use the `required_access_grants` parameter at the field level level to restrict fields individually.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


