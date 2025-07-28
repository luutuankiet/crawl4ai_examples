# Getting started with embedding — administering users  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/gs-admin-for-app-devs

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  Getting started with embedding — administering users
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


To create a signed embed URL, you are required to identify the models and permissions that are available to each embed user and, optionally, supply user attribute data for embed users. This document provides a quick overview of what these elements are in Looker.
## Models
Models determine which data your embed users can access.
Each LookML model consists of a single database connection, and one or more Explores. Each Explore determines which database tables and fields are available to the model, how they are joined, and how they are presented to the user. It is common for multiple models to connect to a single database, which determines which data different sets of users can access. For example, users in the Sales department might need access to different data than users in the Purchasing department. In that case, you could provide two models, each one curated for a single use case.
In a signed embed URL, or when using the `create_sso_embed_url` API endpoint, you specify which models an embed user can access by listing them by name. For example:
```
[
"model_one",
"model_two"
]

```

At least one model value is required in a signed embed URL.
## Permissions
Permissions determine what your embed users can do in Looker.
Every function in Looker requires permission to perform. For example, a user who does not have the `access_data` permission will not be able to view any data. A user who has the `access_data` permission, but not the `save_content` permission, will be able to view content but will not be able to make and save changes to content.
In a signed embed URL, or when using the `create_sso_embed_url` API endpoint, you specify which permissions an embed user has by listing them by name. For example:
```
[
"access_data",
"see_looks"
]

```

At least one permission is required in a signed embed URL. You can view the list of permissions that are supported by signed embed on the Signed embedding documentation page.
## User attributes
User attributes are a method to provide metadata about your embed users. They consist of name and value pairs.
Every user in Looker has several default user attributes, such as `first_name`, `last_name`, and `locale`. Looker admins can also create custom user attributes in various data types. For example, you may have an application where the data presented to the embed user varies based on the company they are associated with. In that case, you might create a custom `company` user attribute that accepts various values that grant or limit data access. You'd next assign the appropriate value to each embed user to limit data access at the user level.
In a signed embed URL, or when using the `create_sso_embed_url` API endpoint, you specify which user attributes are assigned to an embed user by listing each name and value pair. For example:
```
{
"vendor_id":"17",
"company":"altostrat.com"
}

```

User attributes are optional in a signed embed URL.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


