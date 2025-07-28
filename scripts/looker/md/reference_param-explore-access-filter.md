# access_filter  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-access-filter

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * access_filter requires fully scoped field names
    * Even admins must have filter values set in the UI
  * Things to know
    * When an Explore includes access_filter, the default value of full_suggestions switches to yes




Was this helpful?
Send feedback 
#  access_filter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * access_filter requires fully scoped field names
    * Even admins must have filter values set in the UI
  * Things to know
    * When an Explore includes access_filter, the default value of full_suggestions switches to yes


Disable comment: 
## Usage
```

explore: explore_name {
  access_filter: {
    field: fully_scoped_field
    user_attribute: user_attribute_name
  }
}

```

Hierarchy `access_filter` |  Default Value NoneAccepts A LookML field name and the associated user attributeSpecial Rules You may apply multiple `access_filter` parameters in the same Explore   
---|---  
## Definition
`access_filter` lets you apply user-specific data restrictions. Unlike most LookML parameters, it needs to be used in conjunction with other settings in Looker in order to work properly. An `access_filter` parameter is specific to a single Explore, so you need to make sure you apply an `access_filter` parameter to each Explore that needs a restriction.
> Please do not forget to add `access_filter` to every Explore that needs it. If you forget to add `access_filter` to an Explore that should have it, the data will not be restricted and users will be able to see all the data in that Explore.
The behavior of `access_filter` would be similar to you sitting with a user and requiring them to apply one or more filters in the Explore UI before they run any query. For example, the user might only deal with a subset of your customers, so you would require that user to apply a customer name filter.
There are several steps you should take to implement an access filter:
  1. Decide which field or fields need to have a restriction. In the example of requiring users to apply a customer name filter, your users might have a **Customer** Explore with a dimension called **Name**. The way that field would be referenced is `customer.name`.
  2. Every user who interacts with the Explore in question will need a value for the access filter. In our example, every user will need the list of customer names that they are allowed to see. You apply these values to each user or user group by utilizing Looker's user attributes feature, which you can read about on the User attributes documentation page. Suppose we create an **allowed_customers** user attribute.
  3. Finally, connect the user attribute you created with the field that should use its value as a filter. In our example, we'll want to connect the **allowed_customers** user attribute with the `customer.name` field, like this:

```
explore: customer {
  access_filter: {
    field: customer.name
    user_attribute: allowed_customers
  }
}

```

## Examples
Limit users to seeing information about their sales region:
```
explore: customer {
  access_filter: {
    field: sales.region
    user_attribute: sales_region
  }
}

```

Limit users to seeing information about specific departments within their customers:
```
explore: customer {
  access_filter: {
    field: customer.name
    user_attribute: allowed_customers
  }
  access_filter: {
    field: product.department
    user_attribute: allowed_departments
  }
}

```

## Common challenges
###  `access_filter` requires fully scoped field names
If you write a field name without a view name, most parameters in Looker will use a view name that is based on the place that the parameter is used. However, `access_filter` does not work this way and requires you to write both the view name and the field name.
For example, you might think this would work, and that `name` would be interpreted as the customer name:
```
explore: customer {
  access_filter: {
    field: name
    user_attribute: allowed_customers
  }
}

```

However, this is not the case, and you will receive an error. Instead you must write:
```
explore: customer {
  access_filter: {
    field: customer.name
    user_attribute: allowed_customers
  }
}

```

### Even admins must have filter values set in the UI
Every user who accesses an Explore that uses `access_filter` must have a value in the referenced user attribute. This even applies to those with the admin role, despite the fact that they can see all data. Users who don't have a user attribute value set will receive an error when trying to view the Explore.
  * To give an admin or another user access to all values of a string field, set the user attribute data type to **String Filter (advanced)** , and use a value of `%, NULL`.
  * To give an admin or another user access to all values of a number field, set the user attribute data type to **Number Filter (advanced)** , and use a value of `<0, >=0, NULL`.


## Things to know
### When an Explore includes `access_filter`, the default value of `full_suggestions` switches to `yes`
When an Explore includes the `access_filter` parameter, the default value of `full_suggestions` switches to `yes`. This causes the suggestions query to run using the Explore logic, which means that `access_filter` will be applied to narrow the suggestions that come back, limiting the list of suggestions to only the data that the user is intended to have access to.
If you manually set `full_suggestions` to `no`, the filter suggestion query won't run.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


