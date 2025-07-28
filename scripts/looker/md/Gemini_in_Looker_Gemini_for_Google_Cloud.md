# Gemini in Looker  |  Gemini for Google Cloud

**Source:** https://cloud.google.com/gemini/docs/looker/overview

Skip to main content 
  * Español – América Latina

Console 
  * Gemini for Google Cloud 


  * On this page
  * Available features in Looker
  * Enable features in Looker
  * Use features in Looker
  * Available features in Looker Studio
  * Enable features in Looker Studio
  * Use features in Looker Studio
  * Use Gemini in Looker with both Looker Studio and Looker
    * Use Gemini in Looker as part of a complimentary Looker Studio Pro subscription
  * Where to interact with Gemini in Looker
    * Looker: Main navigation menu
    * Looker: Create menu
    * Looker: Visualization chart configuration
    * Looker Studio: Left navigation
    * Looker Studio: Calculated field editor
    * Looker Studio: Gemini panel
    * Slides: Looker Studio Pro panel


  * Gemini for Google Cloud 


Was this helpful?
Send feedback 
#  Gemini in Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Available features in Looker
  * Enable features in Looker
  * Use features in Looker
  * Available features in Looker Studio
  * Enable features in Looker Studio
  * Use features in Looker Studio
  * Use Gemini in Looker with both Looker Studio and Looker
    * Use Gemini in Looker as part of a complimentary Looker Studio Pro subscription
  * Where to interact with Gemini in Looker
    * Looker: Main navigation menu
    * Looker: Create menu
    * Looker: Visualization chart configuration
    * Looker Studio: Left navigation
    * Looker Studio: Calculated field editor
    * Looker Studio: Gemini panel
    * Slides: Looker Studio Pro panel


Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data. Gemini in Looker can provide assistance for tasks in Looker (original) instances, in Looker (Google Cloud core) instances, and in Looker Studio.
Learn how and when Gemini for Google Cloud uses your data.
## Available features in Looker
When Gemini in Looker is enabled, Looker users can perform the following tasks in a Looker (Google Cloud core) instance or a Looker (original) instance:
  * **Ask questions about and converse with your data using Conversational Analytics**. Gemini in Looker lets you ask questions about your data source by using natural language. Gemini returns Looker Studio charts or data tables that are based on your query. You can learn more about how your response was generated and save your conversation for future reference.
  * **Generate custom Looker visualizations**Gemini in Looker lets you customize formatting options for Looker visualizations by using natural language. Gemini generates JSON formatting options from text-based prompts, which you can apply to your visualization. You can also use prompts as a starting point for creating templates and patterns for more complex customizations and then manually update the visualization formatting options.
  * **Generate LookML**. Gemini in Looker assists you in generating LookML parameters. Gemini suggests LookML parameters based on a natural language prompt, which you can add to your project files.


## Enable features in Looker
To access these features in a Looker (original) instance, a Looker admin must enable Gemini in Looker in the Looker (original) instance settings. The instance must be on Looker 25.2 or later and be Looker hosted. Conversational Analytics is available on Looker instances on 25.0 or later.
To access these features in a Looker (Google Cloud core) instance, a user with the Looker Admin (`roles/looker.admin`) IAM role must enable Gemini in Looker in the Looker (Google Cloud core) instance settings in the Google Cloud console.
## Use features in Looker
To use any of the aforementioned Gemini in Looker features in a Looker instance, users must be granted a Looker role that contains the `gemini_in_looker` permission for the models that they're applying Gemini assistance to. This permission is available as part of the default Gemini role.
The following Gemini in Looker features require additional permissions:
  * To create custom visualizations with Gemini assistance, you must be assigned a Looker role that contains the `can_override_vis_config` permission.
  * To write LookML with Gemini assistance, you must be assigned a Looker role that contains the `develop` permission for at least one model in a LookML project.
  * To query data or create a data agent with Conversational Analytics, you must be assigned a Looker role that contains the `access_data` permission for the model that you are querying.


## Available features in Looker Studio
When Gemini in Looker is enabled for a Looker Studio Pro subscription, users under that subscription can perform the following tasks in Looker Studio:
  * **Ask questions about and converse with your data using Conversational Analytics**. Gemini in Looker lets you ask questions about your data source by using natural language. Gemini returns Looker Studio charts or data tables that are based on your query. You can learn more about how your response was generated and save your conversation for future reference.
  * **Create calculated fields by using natural language**. Gemini in Looker lets you create calculated fields in Looker Studio by prompting you to describe the kinds of fields that you'd like to create. Based on your input, Gemini suggests a formula for a calculated field by using fields from your data source along with Looker Studio functions and operators.
  * **Add Looker Studio content to your Slides presentation**. Gemini in Looker lets you import components from your Looker Studio Pro reports into your Slides presentations. Gemini inserts report charts as images, generates a textual summary of each image, and inserts the summary as a text element. You can generate a new Slides presentation by using all or selected visualizations in a Looker Studio report, or you can add or update Looker Studio content to an existing Slides presentation. You can also update the Looker Studio data that has been imported in a Slides presentation.


Some Gemini in Looker capabilities require access to your data through a Looker database connection or connected data sources in Looker Studio. Looker Studio Pro licenses are available at no cost to Looker users on instances that meet offer requirements.
## Enable features in Looker Studio
A user with the appropriate IAM or Google Workspace role must enable Gemini in Looker in Looker Studio.
## Use features in Looker Studio
To use any of the aforementioned Gemini in Looker features in Looker Studio, users must be granted the following roles or privileges:
  * To create calculated fields, users must be assigned an Editor role.
  * To add Looker Studio content to your Slides presentation, users must be assigned a Viewer or Editor role in Looker Studio and have the Editor or Owner permission level for the Slides presentation.
  * To use Conversational Analytics with a Looker data source in Looker Studio users must be granted the `gemini_in_looker` permission for the Looker models that they're applying Gemini assistance to.


## Use Gemini in Looker with both Looker Studio and Looker
Looker users can also interact with the Gemini in Looker features that appear in Looker Studio as part of a Looker Studio Pro subscription.
### Use Gemini in Looker as part of a complimentary Looker Studio Pro subscription
If your Looker admin has accepted the complimentary Looker Studio Pro licenses for your Looker (Google Cloud core) instance or Looker (original) instance, as a Looker user, you can access the Gemini in Looker features that appear in Looker Studio when Gemini in Looker is enabled for your Looker Studio Pro subscription.
## Where to interact with Gemini in Looker
After you enable Gemini in Looker for the assistants that appear in your Looker product, you can seek Gemini assistance in the places that are described in the following sections.
### Looker: Main navigation menu
To access Conversational Analytics, follow these steps:
  1. Navigate to the main navigation menu.
  2. Select chat_spark**Conversations**.


### Looker: Create menu
To access Conversational Analytics, follow these steps:
  1. Navigate to the Looker instance homepage.
  2. Select the **Create** menu.
  3. Select chat_spark**Conversation**.


### Looker: Explore
To access Conversational Analytics, follow these steps:
  1. Navigate to the Looker Explore that contains the data you would like to chat with.
  2. Select **Start a conversation**.


### Looker: Visualization chart configuration
The **Visualization Assistant** is available for visualizations that use the HighCharts API, which includes most Cartesian charts, such as the column chart, bar chart, and line chart.
To access the **Visualization Assistant** , follow these steps:
  1. View a supported visualization in an Explore, or edit a visualization in a Look or dashboard.
  2. Open the **Edit** menu in the visualization.
  3. Click **Visualization Assistant** to open the prompt menu.


For more information, see Create visualizations with Gemini assistance.
### Looker: IDE
To use Gemini to create LookML in your Looker project, follow these steps:
  1. On your Looker instance, enable Development Mode.
  2. Open your project in the Looker IDE.
  3. Use the IDE file browser to open a LookML view file in which you want to insert LookML.
  4. Select the **Help Me Code** icon from the side panel selector.


For more information, see Write LookML with Gemini assistance.
### Looker Studio: Left navigation
To use Gemini assistance to query your data in natural language, select **Conversational Analytics** from the left navigation in Looker Studio.
To create a custom data agent, select **Conversational Analytics** from the left navigation in Looker Studio, and then select **Manage agents**.
If you want to query data within your personal sandbox, follow these steps:
  1. From the left navigation, select the **Sandbox** project.
  2. Click **Create**.
  3. Select **Conversation**.


For more information about querying your data in natural language, see Conversational Analytics: Query your data in natural language with Gemini assistance. For more information about creating and managing a custom data agent, see Conversational Analytics: Data Agents.
### Looker Studio: Calculated field editor
To use Gemini assistance to write formulas for calculated fields, follow these steps from a Looker Studio report:
  1. Edit the data source.
  2. Click **Add a field**.
  3. Select **Add calculated field**.
  4. Click the **Help me write** icon.


For more information, see Create calculated fields with Gemini assistance.
### Looker Studio: Gemini panel
To use Gemini assistance to create a Slides presentation that includes all or selected visualizations in a Looker Studio report, follow these steps:
  1. Open a Looker Studio report in either view or edit mode.
  2. Select the Gemini panel in the panel manager.
  3. Select **Generate Slides**.


For more information, see Adding Looker Studio content to your Slides presentation with Gemini assistance.
### Slides: **Looker Studio Pro** panel
To use Gemini assistance to add Looker Studio content to an existing Slides presentation, follow these steps:
  1. Open a Slides presentation.
  2. Click the Looker Studio icon on the right-hand toolbar to open the Looker Studio Pro panel.


For more information, see Adding Looker Studio content to your Slides presentation with Gemini assistance.
## What's next
  * See the latest enhancements and fixes in release notes.
  * Assign the Gemini role to Gemini in Looker users
  * Learn how Gemini for Google Cloud uses your data.
  * Learn more about Google Cloud compliance. 


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


