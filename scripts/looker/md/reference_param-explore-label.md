# label (for Explores)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-label

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * label has no effect other than changing the Explore menu appearance
  * Things to know
    * Avoid label when possible by naming Explores properly




Was this helpful?
Send feedback 
#  label (for Explores)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * label has no effect other than changing the Explore menu appearance
  * Things to know
    * Avoid label when possible by naming Explores properly


> This page refers to the `label` parameter that is part of an Explore.
> `label` can also be used as part of a model, described on the `label` (for models) parameter documentation page.
> `label` can also be used as part of a view, described on the `label` (for views) parameter documentation page.
> `label` can also be used as part of a field, described on the `label` (for fields) parameter documentation page.
> `label` can also be used as part of a reference line, described on the Dashboard reference line parameters documentation page.
## Usage
```

explore: explore_name {
  label: "desired label"
}

```

Hierarchy `label` |  Default Value The name of the `explore`, with each word capitalized and underscores replaced by spacesAccepts A string   
---|---  
## Definition
`label` helps make Explores more user-friendly by allowing you to set the Explore titles in the Explore menu and in the Explores themselves.
If you do not explicitly add a `label` to an Explore definition, the label defaults to the name of the `explore`, but nicely formatted. Underscores are changed to spaces, and each word is capitalized.
## Examples
Make the Explore menu option appear as **Users** instead of **User** :
```
explore: user {
  label: "Users"
}

```

Make the Explore menu option appear as **Product ID Info** instead of **Product Id Information** :
```
explore: product_id_information {
  label: "Product ID Info"
}

```

## Common challenges
###  `label` has no effect other than changing the Explore menu appearance
When you change the `label` of an Explore, only the Explore menu is affected.
The way that fields should be referenced in the LookML goes unchanged. The way that fields will appear within the Explore UI is also unchanged. If you prefer the LookML references and field names to change, use the `from` parameter instead.
## Things to know
### Avoid `label` when possible by naming Explores properly
If you know that you always want an Explore to appear in a certain manner to your business users, consider giving that name to the `explore` in your LookML. Then you won't need to use `label`.
Typically `label` is only used when you want to:
  * Change the way that an Explore name is formatted. For example, you can make the Explore name "abc_info" appear as "ABC Info" instead of "Abc Info".
  * Create two different Explores that are based on the same view.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


