# extension (for views)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-view-extension

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page




Send feedback 
#  extension (for views)
Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page


> This page refers to the `extension` parameter that is part of a view.
> `extension` can also be used as part of an Explore, described on the `extension` (for Explores) parameter documentation page.
> `extension` can also be used as part of a LookML dashboard, described on the Dashboard parameters documentation page.
## Usage
```
view: view_name {
  extension: required
}

```

Hierarchy `extension` |  Default Value NoneAccepts The value "required"   
---|---  
## Definition
The `extension: required` parameter flags a view as requiring extension, which means that the view cannot be used on its own. The contents and settings of the view will only be used when the view is extended using the `extends` parameter in another view.
A view with `extension: required` is not visible to users on its own; it is intended only to act as a starting point to be extended by other views.
The `extension` parameter accepts only the value `required`. If you don't want to require extension for a view, leave out the `extension` parameter entirely.
See Reusing code with extends for more information on using `extends` for LookML objects.
## Example
The following `looker_events` view has the `extension: required` parameter, so the view itself won't be visible to users:
File: `events.view`
```
view: looker_events {
  extension: required
  sql_table_name: looker_db.events ;;
  # The normal contents of the view follow
}

```

If we want to make use of the `looker_events` view, we can create another view that extends it, like this:
File: `new_events.view`
```
include: "events.view"
view: name_of_the_new_view {
  extends: [looker_events]

  measure: additional_measure {
    type: count
  }
  # Additional things you want to add or change
}

```

Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


