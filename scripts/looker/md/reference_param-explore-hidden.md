# hidden (for Explores)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-explore-hidden

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Common challenges
    * hidden does not hide LookML or prevent Explore access via the URL
  * Things to know
    * hidden is useful for dashboard-only Explores




Was this helpful?
Send feedback 
#  hidden (for Explores)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Common challenges
    * hidden does not hide LookML or prevent Explore access via the URL
  * Things to know
    * hidden is useful for dashboard-only Explores


> This page refers to the `hidden` parameter that is part of an Explore.
> `hidden` can also be used as part of a field, described on the `hidden` (for fields) parameter documentation page.
## Usage
```
explore: explore_name {
  hidden: yes
}

```

Hierarchy `hidden` |  Default Value `no`Accepts A Boolean (`yes` or `no`)  
---|---  
## Definition
`hidden` lets you hide an Explore from the Explore menu. By default, `hidden` is off and the Explore will be displayed.
## Examples
Hide the **Order** Explore from the Explore menu:
```
explore: order {
  hidden: yes
}

```

## Common challenges
###  `hidden` does not hide LookML or prevent Explore access via the URL
Depending upon permissions, some business users are able to see LookML. Even if an Explore is hidden from the Explore menu, such business users can see its existence in the LookML.
A business user could also gain access to the Explore if they were savvy enough to manually modify the URL.
For these reasons, `hidden` is not meant as a security feature, but rather as a presentation feature.
## Things to know
###  `hidden` is useful for dashboard-only Explores
The most common use case for `hidden` is to create Explores that are only used to populate specific dashboard tiles, but are uninteresting for exploration.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


