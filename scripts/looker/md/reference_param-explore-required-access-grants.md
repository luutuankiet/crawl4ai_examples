# required_access_grants (for Explores)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-required-access-grants

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Additional considerations




Was this helpful?
Send feedback 
#  required_access_grants (for Explores)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Additional considerations


> This page refers to the `required_access_grants` parameter that is part of an Explore.
> `required_access_grants` can also be part of a join, described on the `required_access_grants` (for joins) parameter documentation page.
> `required_access_grants` can also be part of a view, described on the `required_access_grants` (for views) parameter documentation page.
> `required_access_grants` can also be part of a dimension, dimension group, measure, filter, or parameter, described on the `required_access_grant` parameter documentation page.
## Usage
```
explore: explore_name {
  required_access_grants: [access_grant_name, access_grant_name, ...]
}

```

Hierarchy `required_access_grants` |  Default Value NoneAccepts Square brackets containing a comma-separated list of access grant names  
---|---  
## Definition
`required_access_grants` pairs with the model-level `access_grant` parameter to limit access of an Explore to only those users who have a specific user attribute value assigned to them.
`required_access_grants` works like this:
  1. You define an access grant using the `access_grant` parameter. As part of the definition, you associate the access grant with a user attribute. You also specify which user attribute values provide access to the access grant.
  2. Next, you use `required_access_grants` to restrict an Explore to only those users who have access to every access grant listed.


This LookML requires that users have access to both the `can_view_financial_data` and the `view_payroll` access grants to see the `payroll` Explore:
```
explore: payroll {
  ...
  required_access_grants: [can_view_financial_data, view_payroll]
}

```

Users who don't have access to _all_ of the access grants assigned to the Explore will not see the Explore at all. They are restricted from viewing any Looks or dashboard tiles based on the Explore and they will not see the Explore in the Explore menu.
For more information on how to define an access grant, see the `access_grant` parameter documentation page.
## Example
Expose the `financial` Explore to only those users who have access to the `accounting` access grant:
```
explore: financial {
  ...
  required_access_grants: [accounting]
}

```

## Additional considerations
Restricting access to an Explore does not restrict access to its underlying LookML structures. So an unrestricted join, view, or field that is part of other Explores will still be available if those Explores are unrestricted. Use the `required_access_grants` parameter at the join, view, or field level to restrict those items individually.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


