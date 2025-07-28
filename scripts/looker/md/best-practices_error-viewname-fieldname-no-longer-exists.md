# Error: view_name.field_name no longer exists on explore_name and will be ignored  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/error-viewname-fieldname-no-longer-exists

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Resolving the warning if fields that are referenced in the warning were deleted intentionally 
    * Resolving the warning for a Look
    * Resolving the warning for an Explore




Send feedback 
#  Error: view_name.field_name no longer exists on explore_name and will be ignored
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Resolving the warning if fields that are referenced in the warning were deleted intentionally 
    * Resolving the warning for a Look
    * Resolving the warning for an Explore


After you run an Explore or a Look, you might occasionally see the following warning: 
`⚠️ view_name.field_name no longer exists on explore_name and will be ignored.`
This warning indicates that fields that you had previously selected or saved in an Explore or a Look are now no longer available. There are several potential causes for this occurrence:
  * The field or fields that are referenced in the warning exist only in Development Mode, and you're viewing the Explore or Look in Production Mode (or vice versa). 
  * A join was removed from the `explore` file's LookML definition, which removed the field that is referenced in the warning. 
For example, if you see the warning `users.name no longer exists on Companies, and will be ignored`, this may indicate that the `users` view and its fields are no longer joined to the `companies` Explore and are therefore unavailable in the Look or Explore. 
> You can use the metadata panel in the IDE to see all `explore` definitions that reference a specific view.
  * A change was made to the view's name in its file, or the view reference in the `explore` LookML definition was changed with a parameter such as `view_name`. 
For example, an underlying view for an Explore called `users` was updated with a `view_name` parameter that references a view called `customers`: 
```
        explore: users {
            view_name: customers
        }
    
```



## Resolving the warning if fields that are referenced in the warning were deleted intentionally 
If a field that is referenced in a warning was _intentionally_ removed by a LookML developer, follow these steps to resolve the warning for either a Look or an Explore. 
### Resolving the warning for a Look
To resolve the `view_name.field_name no longer exists on explore_name and will be ignored` warning for a Look:
  1. Select the **Edit** button in the top right corner to edit the Look.
  2. Once in edit mode, select the **x** next to each error message to clear the warning.
  3. Make a change, such as adding any field from the field picker and then removing it, to activate the **Save** button. 
  4. Select **Save**.


This will update and save the Look to omit the deleted field or fields and the accompanying errors. 
### Resolving the warning for an Explore
To resolve the `view_name.field_name no longer exists on explore_name and will be ignored` warning for an Explore:
  1. Make a change, such as adding any field from the field picker and then removing it.
  2. Select **Run** to rerun the Explore query.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


