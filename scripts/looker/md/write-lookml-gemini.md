# Write LookML with Gemini assistance  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/write-lookml-gemini

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Use Gemini in the Looker IDE
  * Tips for using Gemini in the Looker IDE
  * Sample prompts
    * Create a dimension using longitude and latitude
    * Create a measure for today's total sales
  * Provide feedback
  * Related resources




Was this helpful?
Send feedback 
#  Write LookML with Gemini assistance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Before you begin
  * Use Gemini in the Looker IDE
  * Tips for using Gemini in the Looker IDE
  * Sample prompts
    * Create a dimension using longitude and latitude
    * Create a measure for today's total sales
  * Provide feedback
  * Related resources


This documentation page describes how to use Gemini assistance to create dimensions, dimension groups, and measures, in a LookML project. Generating LookML code suggestions in response to written prompts is a Gemini in Looker feature that is available in Looker (original) and Looker (Google Cloud core) instances.
Gemini in Looker provides generative AI-powered assistance to help you work with your data.
Learn how and when Gemini for Google Cloud uses your data.
This page is intended for Looker developers.
## Before you begin
To use Gemini in the Looker IDE, note the following requirements:
  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the Admin settings — Gemini in Looker documentation page.
    * For Looker (Google Cloud core) the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the Administer Gemini on your Looker (Google Cloud core) instance documentation page.
  * You must be assigned a Looker role that contains the `develop` permission for at least one model in a LookML project.
  * You must be assigned the Looker **Gemini** role.


## Use Gemini in the Looker IDE
To use Gemini for creating LookML in your Looker project, follow these steps:
  1. On your Looker instance, enable Development Mode.
  2. Open your project in the Looker IDE.
  3. Use the IDE file browser to open a LookML view file in which you want to insert LookML.
  4. Select the **Help me code** icon from the side panel selector.
  5. With the the **Help me code** panel open, click to place your cursor on a line in your LookML view file. Based on the type of LookML file and where your cursor is placed in the file, Gemini provides appropriate options to guide you, such as **Create a dimension** or **Create a measure**.
  6. Select one of the following options from the **Help me code** panel:
     * **Create adimension group**
     * **Create adimension**
     * **Create ameasure**
     * **Other code suggestion** : You can use the **other code suggestion** option if you want to try out different LookML elements. Remember that Gemini is an early-stage technology, so validate and test all output before deploying it.
  7. In the **Help me code** panel text field, use conversational language to describe the dimension, dimension group, or measure that you want to create. See the Tips for using Gemini in the Looker IDE and Sample prompts sections on this page for guidance.
  8. Press **Enter** or click the **Submit** icon to send your request to Gemini. Gemini will respond with suggested code.
  9. With the suggested code, you can do the following:
     * Hold your pointer over the **Insert** button to preview the suggested LookML in your file. You can move your cursor to a different line in your file to preview it in a different location before inserting the LookML in the file.
     * Click the **Edit** button to manually change the suggested LookML.
     * Click the **Insert** button to insert the LookML into your file at the location of your cursor.
     * Provide feedback about the suggested code by selecting the thumbs up icon (**This response was helpful**) or thumbs down icon (**This response was not what I expected**).
     * Click the **New code suggestion** link to start over and enter a new prompt for Gemini.
  10. Click **Save Changes** in your LookML file.
  11. Verify the LookML by doing the following:
     * Use the LookML Validator to verify your LookML.
     * Test your LookML in an Explore.


## Tips for using Gemini in the Looker IDE
Here are some tips for using Gemini in the Looker IDE:
  * For best results, write your prompts in American English. See the Gemini for Google Cloud limitations documentation for more information.
  * The **Help me code** panel does not retain context from a previous prompt in the conversation and does not retain prompts across logins and refreshes.
  * When you use LookML that was suggested by Gemini, always validate your LookML with the LookML Validator, and test your new fields in an Explore.
  * Depending on your request, Gemini may suggest LookML that references fields in other view files. When you add suggested LookML to your file, save the file and run the LookML Validator. The LookML Validator will display errors if you need to add `include` statements to your model file.


## Sample prompts
To give you some ideas, here are some example prompts and their results:
  * Create a dimension using longitude and latitude
  * Create a measure for today's total sales


### Create a dimension using longitude and latitude
Here is a prompt using the **Create a dimension** option that asks Gemini to create a new dimension based on the `longitude` and `latitude` fields that are defined in the view file:
`show coordinates with longitude and latitude`
Gemini returns this suggested code:
```
   dimension: coordinates {
      type: location
      sql_latitude: ${TABLE}.latitude ;;
      sql_longitude: ${TABLE}.longitude ;;
   }

```

You can verify this LookML in an Explore by selecting the new `coordinates` field, along with the `longitude` and `latitude` fields it's based on. Because Gemini created the dimension using `type:location`, the Explore results include a hyperlink to view the coordinates on a map:
### Create a measure for today's total sales
Here is a prompt using the **Create a measure** option that asks Gemini to create a new measure for the sum of all of today's orders:
`show the total sale price of today's orders`
Gemini returns this suggested code:
```
   measure: todays_orders {
      type: sum
      sql: ${basic_order_items.sale_price} ;;
      filters: [basic_order_items.created_at_date: "today"]
  }

```

## Provide feedback
You can provide feedback for the generated LookML in the **Help me code** panel. If the generated LookML looks correct, click the thumb_upthumb_down
## Related resources
  * Learn more about Gemini for Google Cloud
  * Learn more about Gemini in Looker


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


