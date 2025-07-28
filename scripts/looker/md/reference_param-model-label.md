# label (for models)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-model-label

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * label doesn't change the model name everywhere
  * Things to know
    * Avoid label when possible by naming models thoughtfully




Send feedback 
#  label (for models)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * label doesn't change the model name everywhere
  * Things to know
    * Avoid label when possible by naming models thoughtfully


> This page refers to the `label` parameter that is part of a model.
> `label` can also be used as part of an Explore, as described on the `label` (for Explores) parameter documentation page.
> `label` can also be used as part of a view, as described on the `label` (for views) parameter documentation page.
> `label` can also be used as part of a field, as described on the `label` (for fields) parameter documentation page.
> `label` can also be used as part of a reference line, described on the Dashboard reference line parameters documentation page.
## Usage
```

label: "desired label"

```

Hierarchy `label` |  Default Value The name of the model file, capitalized with spaces instead of underscoresAccepts A string   
---|---  
## Definition
`label` helps make Explores more user-friendly by allowing you to set the model names that appear in the Explore menu.
If you do not explicitly add a `label` to a model definition, the label defaults to the name of the model, but nicely formatted. Underscores are changed to spaces, and each word is capitalized.
## Examples
If your model file is called `user_data.model`, by default the Explore menu will use the filename, capitalized and with spaces instead of underscores. So the model's entry in the Explore would be rendered as **User Data**.
You can use the `label` parameter to change the model's entry in the Explore menu to **Market Research** :
```
label: "Market Research"

```

The `label` parameter goes at the top level of the model file. For example:
```
connection: "faa"
label: "Market Research"

include: "/views/states.view.lkml"
include: "/views/users.view.lkml"


explore: states {}
explore: users {}

```

In this example, Looker would now display the model in the Explore menu as **Market Research**.
## Common challenges
###  `label` doesn't change the model name everywhere
Changing the `label` of a model affects the Explore menu and the way the model is displayed in listings of Looks and dashboards. Explore URLs, the Looker IDE, and SQL Runner still show the actual model name. Consequently, you should still use the model's filename to reference the model in LookML and Admin settings.
## Things to know
### Avoid `label` when possible by naming models thoughtfully
A model does not need a `label` parameter if the name already appears and is formatted the way you want your users to see it in the Explore menu. If you know how you want a model to appear to your users, you can often consider this when naming it, allowing you to avoid the need to use `label`.
You can use the `label` parameter to change the way a model name is formatted. For example, you can make the model name "abc_info" appear as "ABC Info" instead of "Abc Info".
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


