# Create calculated fields with Gemini assistance  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/create-calculated-fields-gemini

Skip to main content 
  * Español – América Latina

Console  Sign in


  * On this page
  * Before you begin
  * Create a calculated field with Gemini assistance
    * Information used by Gemini in Looker
  * Provide feedback
  * Related resources




Send feedback 
#  Create calculated fields with Gemini assistance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Create a calculated field with Gemini assistance
    * Information used by Gemini in Looker
  * Provide feedback
  * Related resources


This documentation describes how to use Gemini in Looker to help you create calculated fields by letting you describe the kinds of fields that you want.
Looker Studio prompts you to describe the fields that you'd like to create. Based on your input, Looker Studio suggests a formula for a calculated field by using fields from your data source along with Looker Studio functions and operators.
Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.
Learn how and when Gemini for Google Cloud uses your data.
This page is intended for report editors in Looker Studio.
## Before you begin
To use this Gemini in Looker feature, you need to fulfill the following requirements:
  * You must be a user under a Looker Studio Pro subscription. Looker Studio Pro licenses are available at no cost to Looker users.
  * To be able to create chart-specific calculated fields, you must be an editor of the report.
  * Field Editing in Reports must be enabled in the data source.
  * Gemini in Looker must be enabled for your Looker Studio Pro project.


## Create a calculated field with Gemini assistance
To create a calculated field with Gemini assistance, follow these steps:
  1. When you're writing a calculated field, click the **Help me write a calculated field** icon in the bottom right of the field editor.
  2. If you have not begun writing a calculated field, Looker Studio prompts you to select a suggested prompt or to describe the kind of calculated field that you want to create. 
     * To select one of the suggested prompts, click the prompt.
     * To describe the kind of calculated field that you want to create, write a description and then click **Create**. See the **Sample prompts** section for examples of descriptions that you can write.
  3. If you have already begun writing a calculated field, Looker Studio will use that formula as context. Describe how you would like to change the calculated field, and then click **Create**. 
     * To edit your original prompt, hover over the prompt and click the **Edit** icon. Edit your prompt, and then click **Update.**
     * To remove the previous formula from Looker Studio's context, hover over the formula and click the **Reset** icon.
     * To refine your formula, click **Refine**. Next, provide Looker Studio with additional information about your formula, such as adding or removing a bucket, or adding another field to a concatenation. Finally, click **Create**.
  4. To add the generated formula to your calculated field definition, click **Apply**.
  5. To save your field definition, click **Save**.


To exit the formula generation dialog at any point without saving your changes, close the dialog by clicking the **X** in the top right corner or by clicking outside of the dialog.
### Limitations
Note the following limitations on calculated field creation:
  * Gemini in Looker can help you create only calculated fields that meet Looker Studio criteria of what you can do with calculated fields.
  * Looker Studio won't suggest parameters or a NATIVE_DIMENSION when it suggests a calculated field.
  * The Looker connector supports only some functions for calculated fields.


### Information used by Gemini in Looker
When you create a calculated field with Gemini assistance, Looker Studio uses the following information to generate formulas:
  * The prompt that you write to instruct Looker Studio to create or edit a field
  * The formula definition for any field that you change or refine
  * The schema of the underlying data source


## Sample prompts
To get you started, here are some sample prompts for different kinds of fields:
  * Try entering the following prompt:
```
Merge city and state like City, State

```

Looker Studio may return a field definition like the following:
```
CONCAT(Users City, ", ", Users State)

```

  * Try entering the following prompt:
```
bucket sale price in groups of 20

```

Looker Studio may return a field definition like the following:
```
CASE
    WHEN Order Items Sale Price < 20 THEN "0-20"
    WHEN Order Items Sale Price < 40 THEN "20-40"
    WHEN Order Items Sale Price < 60 THEN "40-60"
    WHEN Order Items Sale Price < 80 THEN "60-80"
    WHEN Order Items Sale Price < 100 THEN "80-100"
    WHEN Order Items Sale Price < 120 THEN "100-120"
    WHEN Order Items Sale Price < 140 THEN "120-140"
    WHEN Order Items Sale Price < 160 THEN "140-160"
    WHEN Order Items Sale Price < 180 THEN "160-180"
    WHEN Order Items Sale Price < 200 THEN "180-200"
    ELSE "200+"
END

```



## Troubleshooting
If you get an error while creating a calculated field with Looker Studio, make sure that you are asking for a result that you can achieve with calculated fields, rather than the results of a query or a chart.
## Provide feedback
After generating a calculated field, Looker Studio will prompt you to provide feedback on the field. If the generated field looks correct, click the thumb_up**Rate positive** thumbs-up icon. If the generated field looks incorrect, or if you'd like to provide other feedback on this feature, click the thumb_down**Rate negative** thumbs-down icon. Include the prompt that you entered as well as the formula that Looker Studio created. This feedback is collected for our development team and is not used to train the Gemini in Looker model.
## Related resources
  * Gemini for Google Cloud overview
  * Gemini in Looker


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


