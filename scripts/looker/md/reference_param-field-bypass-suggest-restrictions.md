# bypass_suggest_restrictions  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in




Send feedback 
#  bypass_suggest_restrictions
Stay organized with collections  Save and categorize content based on your preferences. 
> Use caution when using this parameter, as it can reveal sensitive data if used incorrectly.
## Usage
```
view: view_name {
  dimension: field_name {
    bypass_suggest_restrictions: yes
  }
}

```
Hierarchy `bypass_suggest_restrictions` |  Possible Field Types Dimension, Dimension Group, Filter, ParameterAccepts A Boolean (yes or no)  
---|---  
## Definition
Typically, when `sql_always_where` or `access_filter` is used, filter suggestions are restricted for that Explore. This prevents users from seeing a filter suggestion that does not apply to them.
For example, you might be using `access_filter` to limit users to their company's data. If one of those users added a **Project Name** filter, you might not want them to see the names of projects from other companies.
If you are certain that there are no possible values in a particular `dimension` or `filter` field that would reveal sensitive information, you can re-enable filter suggestions like this:
```
dimension: project_name {
  sql: ${TABLE}.project ;;
  bypass_suggest_restrictions: yes
}

```

-
If there _are_ values in a field that would reveal sensitive information, the `full_suggestions` parameter can enable you to get properly filtered suggestions.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


