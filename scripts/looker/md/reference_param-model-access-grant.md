# access_grant  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-access-grant

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  access_grant
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
See more code actions.
Light code theme
Dark code theme
```
access_grant: access_grant_name {
  user_attribute: user_attribute_name
  allowed_values: [ "value_1", "value_2" , ... ]
}

```

Hierarchy `access_grant` |  Default Value NoneAccepts The name of a user attribute with the `user_attribute` subparameter and a list of user attribute values with the `allowed_values` subparameter   
---|---  
## Definition
An access grant is a LookML structure defined in a model file that controls access to other LookML structures, specifically Explores, joins, views, and fields. The `access_grant` parameter defines an access grant.
`access_grant` takes the name of a user attribute with the `user_attribute` subparameter and a list of acceptable values for the user attribute with the `allowed_values` subparameter. Only those users who are assigned one of the allowed values in the specified user attribute can access structures to which the access grant is required.
Once defined, you can use the `required_access_grants` parameter at the Explore, join, view, or field level to require the access grant to access those structures.
For example, the following LookML creates an access grant called `can_view_financial_data`, which is based on the `department` user attribute. Only those users who are assigned the values `"finance"` or `"executive"` in the `department` user attribute are given access to the `can_view_financial_data` access grant:
```
access_grant: can_view_financial_data {
  user_attribute: department
  allowed_values: [ "finance", "executive" ]
}

```

You then associate the `can_view_financial_data` access grant with a LookML structure using the `required_access_grants` parameter:
```
dimension: financial_data_field
  ...
  required_access_grants: [can_view_financial_data]
}

```

In this example, only users who have the proper user attribute value for the `can_view_financial_data` access grant will see the `financial_data_field` dimension.
You can define multiple access grants in a model, and you can assign multiple access grants to a LookML structure with the `required_access_grants` parameter. In that case, a user must have access to _all_ of the specified access grants to have access to the LookML structure.
For example, the following LookML defines two different access grants:
```
access_grant: can_view_financial_data {
  user_attribute: department
  allowed_values: [ "finance", "executive" ]
}

access_grant: can_view_payroll_data {
  user_attribute: view_payroll
  allowed_values: [ "yes" ]
}

```

Then, in the view file, the `required_access_grants` parameter specifies both access grants:
```
view: payroll {
  ...
  required_access_grants: [can_view_financial_data, can_view_payroll_data]
}

```

In this case, only users that have either the value `"finance"` or the value `"executive"` assigned to their `department` user attribute _and_ have the value `"yes"` assigned to their `view_payroll` user attribute can access the view.
## Examples
Define an access grant that requires users to have either the value `"product_management"` or the value `"engineering"` in the `department` user attribute to have access to the `engineering` access grant:
```
access_grant: engineering {
  user_attribute: department
  allowed_values: [ "product_management", "engineering" ]
}

```

You can also define access grants with user attributes that take numeric or date/time data. To do this, you must enclose the allowed values in double quotes, just as you would with a string. For example, the following access grant references the `id` user attribute, which has a data type of **number**. Only users with the `id` value of 1, 2, 3, 4, or 5 will be granted access:
```
access_grant: user_id {
  user_attribute: id
  allowed_values: ["1", "2", "3", "4", "5"]
}

```

The following example references the user attribute `start_date`, which has the data type **Date/Time**. Only users who have the value `2020-01-01` in the user attribute will be granted access:
```
access_grant: start_date {
  user_attribute: start_date
  allowed_values: ["2020-01-01"]
}

```

## Things to consider
### User-editable user attributes are not allowed with access grants
Access grants cannot accept user attributes that have a **User Access** level of **Edit**. Users can see and edit the values of user attributes that have a **User Access** level of **Edit** on their account page. For security purposes, only user attributes that have a **User Access** level of **None** or **View** are allowed with `access_grant`.
### Values listed in `allowed_values` must match user attribute values exactly
`access_grant` will work with user attributes that have the **String Filter (advanced)** , **Number Filter (advanced)** , or **Date/Time Filter (advanced)** data type. But, in order to grant access, the values listed in the `allowed_values` parameter must match the value in the user attribute _exactly_.
For example, if you created a user attribute called `numeric_range` with the data type **Number Filter (advanced)** , you could use a Looker filter expression to enter a range of numbers, such as `[1, 20]`. In that example, the Looker filter expression in the user attribute will return a range of numbers between 1 and 20, inclusive. Since `access_grant` requires an exact match, however, using the parameter `allowed_values: ["10"]` would _not_ grant access. To grant access, you would have to use `allowed_values: ["[1, 20]"]`.
This is also true for user attributes that have multiple values. For example, a user attribute with the data type **Number Filter (advanced)** given the value `1, 3, 5` would _only_ match an access grant with the parameter `allowed_values: ["1, 3, 5"]`. Likewise, an access grant with the parameter `allowed_values: ["1"]` would not grant access to the user with multiple values in the user attribute. Nor would an access grant with the parameter `allowed_values: ["1", "3", "5"]` grant access to this user, because, while the `allowed_values: []` parameter can accept multiple values, none of the three values in the `allowed_values: ["1", "3", "5"]` parameter matches the user attribute value `1, 3, 5` exactly. In this case, a user with a user attribute value of `1` or `3` or `5` _would_ be granted access, since each of those values matches one of the options in the `allowed_values: ["1", "3", "5"]` parameter.
Similarly, `access_grant` requires an exact match with user attributes of data type **String Filter (advanced)**. Unlike typical Looker filter expressions, using the parameter `allowed_values: [ "Ca%" ]` does _not_ not match a user attribute with the values `Canada` or `California`. Only a user attribute value of exactly `Ca%` would be matched and granted access.
### Users who are not granted access experience different behavior depending on LookML structure
A user who does not have access to an access grant will experience different behavior depending on which LookML structure they are trying to access. See the `required_access_grants` documentation pages at the Explore, join, view, or field level for information about how access to those structures is restricted.
### Access grants at multiple levels are added together
If you nest access grants, the access grants are _additive_. For example, you can create `required_access_grants` for a view and create `required_access_grants` for a field inside the view. In order to see the field, a user must have access grants to both the field _and_ the view. Likewise for joins: If you create `required_access_grants` for the views in a join and also create `required_access_grants` for the join of these two views, a user must have access grants to both views and the join in order to see the joined view.
### Accessing structures that reference restricted structures
Users can have access to Looks or dashboards that contain LookML objects they don't have access to. In these situations the Look or dashboard will display as if those LookML objects have been removed from the model.
Suppose we have an Explore A, which contains join A, view A, and field A. Next, we place an access restriction on Explore A. As expected, join A, view A, and field A will inherit that restriction, but only when users are interacting with Explore A. If join A, view A, or field A is used in a different Explore B, they will not necessarily have any access restrictions. Therefore, if you plan to re-use LookML elements, we suggest you apply access restrictions at the lowest level possible.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


