# Add Looker Studio content to your Google Slides presentation using Gemini assistance  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/add-looker-studio-slides-gemini

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Generate a Google Slides presentation from all visualizations in a Looker Studio report
  * Generate a Google Slides presentation from selected visualizations in a Looker Studio report
  * Add Looker Studio content to a Google Slides presentation
  * Update Looker Studio data in a Google Slides presentation
  * Troubleshooting and limitations
  * Provide feedback
  * Related resources




Send feedback 
#  Add Looker Studio content to your Google Slides presentation using Gemini assistance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Generate a Google Slides presentation from all visualizations in a Looker Studio report
  * Generate a Google Slides presentation from selected visualizations in a Looker Studio report
  * Add Looker Studio content to a Google Slides presentation
  * Update Looker Studio data in a Google Slides presentation
  * Troubleshooting and limitations
  * Provide feedback
  * Related resources


This documentation page describes how to use Gemini in Looker to help you generate Google Slides presentations from your Looker Studio reports. Looker Studio inserts the report charts as images, generates a textual summary of each chart, and inserts the summaries as text elements.
Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.
Learn how and when Gemini for Google Cloud uses your data.
This page is intended for users who are working with reports in Looker Studio.
## Before you begin
To use this Gemini in Looker feature, the following requirements must be fulfilled:
  * You must be a user under a Looker Studio Pro subscription. Looker Studio Pro licenses are available at no cost to Looker users.
  * Gemini in Looker must be enabled for your Looker Studio project.
  * You must be a viewer or an editor of the Looker Studio report that you want to generate Google Slides from.
  * If you are a viewer of the Looker Studio report, the **Disable viewers from generating Google Slides with Gemini in Looker** sharing option must not be selected.
  * You must be an editor of the Google Slides presentation that you want to import content into.
  * If you want to add Looker Studio content to an existing Google Slides presentation, you must install the Looker Studio add-on for Google Workspace.


## Generate a Google Slides presentation from all visualizations in a Looker Studio report
To create a Google Slides presentation that includes all the visualizations in a Looker Studio report, follow these steps:
  1. Open a Looker Studio report in either view mode or edit mode.
  2. In the panel manager, select the **Gemini** panel.
  3. Select **Generate Slides**.
  4. Select **All visualizations**.
  5. Looker Studio generates a Google Slides presentation and saves it to your Google Drive. The presentation contains the following slides: 
     * A title slide with the title of the Looker Studio report, your name, the date that the presentation was generated, and a link to the Looker Studio report
     * One slide for every chart including the chart title, if available, and a textual summary of the chart
     * A closing slide


After you generate a presentation using this method, you won't be able to edit it in Looker Studio. To view or edit the presentation, click the link in the **Gemini** panel. To finish, click **Done** or close the **Gemini** panel.
## Generate a Google Slides presentation from selected visualizations in a Looker Studio report
To create a Google Slides presentation that includes a subset of visualizations from a Looker Studio report, follow these steps:
  1. Open a Looker Studio report in either view mode or edit mode.
  2. In the panel manager, select the **Gemini** panel.
  3. Select **Generate Slides**.
  4. Select **Let me choose**.
  5. Click the component(s) that you want to add to the presentation. 
     * To select multiple components, either Shift-click each component, or click and drag a selection area over the canvas.
     * Charts, titles, and filters are all separate components. You may want to add each of them to the slide. However, Gemini in Looker only generates text summaries for visualizations.
  6. Select whether to add this set of components to a new slide or to the current slide.
  7. Click **Done** in the top banner.
  8. Looker Studio adds the selected component(s) to the **Gemini** panel. 
     * To disable the textual summary for a visualization, click the **Summary on** icon on the slide.
     * To remove a visualization from the **Gemini** panel, click the **Delete** icon on the slide.
  9. To add more components, repeat steps 5 through 8.
  10. Once you're finished adding components, select **Generate Slides** in the **Gemini** panel.
  11. Looker Studio generates a Google Slides presentation and saves it to your Google Drive. The presentation contains the following slides:
     * A title slide with the title of the Looker Studio report, your name, the date that the presentation was generated, and a link to the Looker Studio report
     * The slides that you created in steps 5 through 10
     * A closing slide


After you generate a presentation using this method, you won't be able to further edit it in Looker Studio. To view or edit the presentation, click the link in the **Gemini** panel. To finish, click **Done** or close the **Gemini** panel.
## Add Looker Studio content to a Google Slides presentation
To add Looker Studio content to an existing Google Slides presentation, follow these steps:
  1. Install the Looker Studio add-on for Google Workspace.
     * This add-on will work only if you are a Looker Studio Pro user and if Gemini in Looker is enabled for your Looker Studio project.
  2. In a Google Slides presentation, click the **Looker Studio** icon on the right-hand toolbar to open the **Looker Studio** panel.
  3. Click **Import**. Looker Studio opens in a new browser tab.
  4. In Looker Studio, select a report to import visualizations from.
  5. Click the component(s) that you want to add to the presentation.
     * To select multiple components, either Shift-click each component, or drag a selection area over the canvas.
     * Charts, titles, and filters are all separate components. You may want to add each of them to the slide. However, Gemini in Looker only generates text summaries for visualizations.
  6. Click **Done**. Looker Studio adds the selected component(s) to the **Gemini** panel.
     * To disable the textual summary for a visualization, click the **Summary on** icon on the slide.
     * To remove a visualization from the **Gemini** panel, click the **Delete** icon on the slide.
  7. To add more components, repeat steps 4-5.
  8. To add all the previewed slides to your presentation, click **Add to Slides**. The Looker Studio browser tab is closed, and you will be returned to the Google Slides browser tab. The components that you selected will appear in the **Looker Studio** panel.
  9. To add a slide preview to your presentation, click **Insert** under the slide preview.
  10. Looker Studio inserts the components into your presentation as images. Looker Studio then generates a text summary of each visualization and inserts the summaries into your presentation.


When you're finished adding components, click **Done** in the **Looker Studio** panel.
## Update Looker Studio data in a Google Slides presentation
To update Looker Studio data in an existing Google Slides presentation, follow these steps:
  1. In a Google Slides presentation, click the **Looker Studio** icon on the right-hand toolbar to open the **Looker Studio** panel.
  2. Select the components that you want to update data for.
  3. Click the **Update** icon. Looker Studio will refresh each of the selected components with updated data.


When you're finished, close the **Looker Studio** panel.
## Troubleshooting and limitations
The following limitations apply when adding Looker Studio content to Google Slides presentations:
  * Summaries won't be generated for non-visualization report components, such as filters, controls, or text boxes.
  * Summaries won't be generated for visualizations with fewer than three data rows, such as single-value visualizations.
  * Summaries won't be generated for visualizations that are based on blends.
  * Google Slides generation may time out if the Looker Studio report has more than 75 visualizations.
  * Google Slides generation is not supported in Looker reports.


If you encounter issues when adding Looker Studio content to Google Slides presentations, refer to the following table for potential solutions.
Error message  |  Possible cause  |  Possible solution   
---|---|---  
Connection to the data source was lost.  |  Looker Studio could not connect to your data source.  |  Try generating the presentation again.   
Not enough rows to generate summary.  |  Looker Studio requires at least four rows of data to generate a summary.  |  Add more rows to the visualization.   
Blended data sources aren't supported.  |  Looker Studio doesn't support generating summaries from visualizations that are based on blended data sources.  |  Try using a data source that is not blended.   
Slides generation failed due to an error.  |  Looker Studio encountered an unspecified error.  |  Wait for a few minutes and then try generating the presentation again.   
Slides generation timed out.  |  Summary generation may time out for reports with more than 75 visualizations.  |  Try removing some visualizations from the report.   
Slides generation timed out due to server error.  |  Looker Studio may be overloaded with requests.  |  Wait for a few minutes and then try generating the presentation again.   
## Provide feedback
You can provide feedback for the generated presentation in the **Gemini** panel of Looker Studio. If the generated presentation looks correct, click the thumb_upthumb_down
## Related resources
  * Gemini for Google Cloud overview
  * Gemini in Looker


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


