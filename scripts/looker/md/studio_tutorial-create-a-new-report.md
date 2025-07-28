# Tutorial: Create a new report  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/tutorial-create-a-new-report

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Step 1: Create a new blank report
  * Step 2: Add another chart to the report
  * Step 3: Style the report
  * Step 4: Add a banner
  * Step 5: Add a title to the report




Was this helpful?
Send feedback 
#  Tutorial: Create a new report
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Step 1: Create a new blank report
  * Step 2: Add another chart to the report
  * Step 3: Style the report
  * Step 4: Add a banner
  * Step 5: Add a title to the report


In this tutorial, you'll learn how to create a new report in Looker Studio.
## Step 1: Create a new blank report
  1. Sign in to Looker Studio.
  2. Click **Create** and then select **Report**.
  3. You'll see the report editor tool, with the _Add data to report_ panel open. This panel has two tabs: _Connect to data_ and _My data sources_.
> You'll learn more about connectors and data sources in the Connect to your data topic.
    1. In the _Connect to data_ tab, select a connector, create a new data source, and add that to your report:
      1. Select the type of data that you want to visualize.
      2. Provide your account or other details.
      3. In the bottom right, click **Add**.
    2. Use _My data sources_ to add an existing data source to your report:
> The **My data sources** tab includes a number of sample data sources.
> To follow along with this tutorial, select the `[Sample] GA4 - Google Merchandise Store` data source. If you add a different data source, your results may vary from the steps described in this tutorial.
      1. Locate the data source that you want.
      2. In the bottom right, click **Add**.
      3. The data source is added to your report.
  4. A table appears with fields from that data source.
Use the properties panel on the right to change the data and style of the table.
  5. By default, the layout type is set to **Freeform layout**. To use a responsive report instead, select the **Responsive layout** type. You can change the layout setting later.
     * A freeform report is tailored for desktop screens. Choose this report type if you want pixel-perfect control over the placement and sizing of each report component.
     * A responsive report scales well across many different screen sizes. Choose this report type if you expect your users to regularly view the report on a tablet or other mobile device.
  6. In the top left, name your report by clicking _Untitled Report_ and then entering a new name.
  7. (Optional) Add a description to your report by clicking the three-dot menu and selecting **Details**. Then add a description to the **Description** field.


### Add more data
To add more data sources to a report, in the toolbar, click **Add data**.
## Step 2: Add another chart to the report
The time series chart plots data over the course of time.
  1. In the toolbar, click **Add a chart**.
  2. Select a **Time series** chart .
  3. Click the canvas where you want the chart to appear.
  4. Looker Studio automatically adds the _Date_ dimension and the _Views_ metric (assuming you're using an Analytics data source).
  5. To adjust the chart's position, drag it, or select the chart and move it by using your keyboard arrow keys.
  6. To adjust the chart's size, select it, and then drag a corner or mid-line point.
  7. Break down the chart by _Device Category_ :
    1. Make sure that the time series chart is selected.
    2. On the right, in the **Data** panel, use the search tool to find the _Device Category_ dimension.
    3. Drag the field and drop it on the **Breakdown Dimension** target.


Your chart should now display data series for the different device categories (Mobile, Desktop, and Tablet).
## Step 3: Style the report
Preset themes let you apply color and style options to your entire report.
  1. Edit the report.
  2. In the toolbar, click **Theme and layout**.
  3. In the THEME tab, click the theme that you want to apply.


You can customize any of the preset themes. For example, you can select a different background color that better matches your brand:
  1. In the _Theme and Layout_ panel, click **Customize**.
  2. Scroll down to the _Background and Border_ section.
  3. Use the color picker to set the **Background** color to your favorite color. Something in a mauvy-peach, perhaps?


## Step 4: Add a banner
Use a colored rectangle as a background banner for your report header.
  1. Select the Page component by clicking anywhere in the grid area.
  2. Select the **Rectangle** tool from the toolbar. 
  3. Draw a rectangle across the top of the page.
  4. On the right, in the _Rectangle Properties_ panel, set the rectangle background color to blue.


####  Extra credit! Add a gradient to the banner. 
When one color fades into another, the effect is called a gradient. Gradients are an option of the background color property. 
  1. Click the background color control: 
  2. Click **Gradient**. 


The left and right color swatches determine the starting and ending colors. Enter the specific color hex values, choose from the palette, or use the vertical sliders to select the color. 
The orientation arrow controls the flow of the gradient. 
## Step 5: Add a title to the report
The text tool lets you annotate your reports and charts.
  1. Select the **Text** tool from the toolbar. 
  2. Draw a textbox inside the banner rectangle.
  3. Type `Google Analytics Demo Dashboard` in the field.
  4. Highlight the text. Use the _Text Properties_ panel on the right to change the font color and the font size to something that looks nice to you.


> #### Hey! Where's the SAVE button?
> Looker Studio automatically saves every change you make, so there's no need to click **Save** when editing a report. Pretty sweet!
## Next steps
Add more charts to your report.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


