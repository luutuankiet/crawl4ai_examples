# project_name  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/2510/reference/param-manifest-project-name

Skip to main content 
  * Español – América Latina

Console 


  * On this page


You are viewing documentation for Looker 25.10. Click this link to see the most recent documentation. 


Was this helpful?
Send feedback 
#  project_name
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


## Usage
See more code actions.
Light code theme
Dark code theme
```

project_name: "my_project_name"

```

Hierarchy Project Manifest File `project_name` |  Default Value NoneAccepts A string specifying the current project name   
---|---  
## Definition
`project_name` specifies the current project name in a manifest file. This is required when using a manifest file to import files from other projects.
## Example
In a manifest file, specify the current project name as "thelook":
```
project_name: "thelook"

local_dependency: {
   project: "other_project"
}

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-23 UTC.


