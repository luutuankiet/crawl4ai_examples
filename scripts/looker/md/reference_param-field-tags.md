# tags (for fields)  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-tags

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Using tags with integrated services




Was this helpful?
Send feedback 
#  tags (for fields)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Using tags with integrated services


> This page refers to the `tags` parameter that is part of a field.
> `tags` can also be used as part of an Explore, described on the `tags` (for Explores) parameter documentation page.
## Usage
```
view: view_name {
  dimension: field_name {
    tags : ["string1","string2", ...]
  }
}

```

Hierarchy `tags` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, ParameterAccepts Square brackets containing a comma-separated list of strings  
---|---  
## Definition
The `tags` parameter lets you add text strings to a field. These strings are not used by the Looker model but can be passed to other applications using:
  * Integrated services enabled on the **Action** panel. Some services require one or more fields containing certain types of data, such as a phone number. Use the `tags` parameter to identify those fields that can be used by a service.
  * API calls. For API calls, `tags` can be useful for providing arbitrary metadata about a field to an outside application.


## Examples
Adds two text tags, "Important Data" and "Customer Data", to the `customer_count_distinct` measure.
```
measure: customer_count_distinct {
  tags: ["Important Data", "Customer Data"]
  type: count_distinct
  sql: ${customer.id} ;;
}

```

## Using `tags` with integrated services
Some integrated services in the Action panel require that you identify a specific field in your LookML model using the `tags` parameter. This will be a field or fields that provide identifying data to that service.
For example, the **Twilio Send Message** service sends a message to phone numbers. It requires a query that includes a phone number field, and that you identify the phone number field in LookML using `tags: ["phone"]`. Looker uses the `tags` parameter to identify which field in the query contains phone numbers that should be sent to Twilio. Your LookML for the phone number field could look like this:
```
measure: phone {
  tags: ["phone"]
  type: string
  sql: ${TABLE}.phone ;;
}

```

Some integrated services can be called from a row in an Explore, a dashboard tile, or a Look. In this case, Looker marks the tagged field with three dots to indicate that there is a drop-down list. Select the three dots to see the actions available for that link:
Other integrated services can be used when delivering Looker content to various destinations. If a query's results contain the required tagged fields for an enabled service, then the **Where should this data go?** field of the Scheduler displays the service and the required field. Looker also displays the service as a destination if the service does not require a tagged field.
For more information about the integrated services that are available in the Looker Action Hub, see the Admin settings — Actions section of the **Actions** page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


