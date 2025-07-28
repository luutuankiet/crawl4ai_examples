# Developing a custom visualization for the Looker Marketplace  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/marketplace-develop-visualization

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Developing a visualization type
  * Creating a Looker project for the visualization
  * Pushing the project to Git
  * Testing the functionality of the visualization
  * Submitting the visualization for review




Was this helpful?
Send feedback 
#  Developing a custom visualization for the Looker Marketplace
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Developing a visualization type
  * Creating a Looker project for the visualization
  * Pushing the project to Git
  * Testing the functionality of the visualization
  * Submitting the visualization for review


This page describes how to create a custom visualization type that can be added to the Looker Marketplace and accessed by other Looker users. You can also create a custom visualization directly in your project without making it available to other Looker customers.
> Please note that you must be a member of the Looker Partner Network or a Looker customer to submit content to the Looker Marketplace.
The Looker Marketplace is a central location for finding, deploying, and managing many types of Looker content, such as Looker Blocks™, applications, visualizations, and other plug-ins.
> With the Looker **Marketplace** feature enabled, Looker customers can install Looker Marketplace **plug-ins**, which include visualization types to add to Looker's native visualization library.
To develop a custom visualization and make it available to all Looker customers through the Looker Marketplace, follow these steps:
  1. Develop a visualization.
  2. Create a Looker project for the visualization.
  3. Push the Looker project to a Git repository.
  4. Test the functionality of the visualization.
  5. Submit your visualization to Looker.


### Developing a visualization type
Identify a visualization type that you'd like to develop. (Confirm that this visualization is not already listed in the Marketplace or as a native Looker visualization.)
Develop your custom visualization in JavaScript using the Looker Visualization API with your Javascript environment.
### Creating a Looker project for the visualization
Create a Looker project to represent your custom visualization. The project should contain the following files:
  * LICENSE file: Lists the license or licenses with which the visualization is distributed, using the text:
`This Looker visualization is distributed with the following license:...`
  * `README.md` file: Provides a description of your visualization, how it works, and any additional information.
  * JavaScript (`.js`) file: Contains a condensed version of the JavaScript code that you used to produce your visualization. With the Marketplace, JS files are included within the project, which allows for proper versioning and package management.
  * Manifest (`manifest.lkml`) file: Specifies an `id` (a unique identifier) and a `label` (shown in the Looker UI for this visualization). For example:

```
    constant: vis_id {
        value: "default_id"
        export: override_optional
    }
    constant: vis_label {
        value: "default_label"
        export: override_optional
    }
    visualization: {
        id: "@{vis_id}"
        label: "@{vis_label}"
        file: "my_local.js"
        sri_hash: "my_sri_hash"
        dependencies: []
    }

```

  * Listing (`marketplace.json`) file: Configures the Marketplace listing for the custom visualization and includes a label for how the visualization will appear in the Marketplace, the location of the `image_uri`, a tagline that describes the use case for the visualization, and also defines the Marketplace field constants that users input during installation. For example:

```
{
  "label": "Gauge Visualization",
  "category_label": "plug-ins",
  "branding": {
    "image_uri": "https://marketplace-api.looker.com/visualization-screenshots/gauge_icon.png",
    "tagline": "Use the Gauge visualization to display a measure and progress to a goal."
  },
   "constants": {
        "vis_label": {
            "label": "Visualization Label",
            "description": "This label will appear in the visualization selector in the Looker Explore UI."
        },
        "vis_id": {
            "label": "Visualization Id",
            "description": "This must be a unique ID across all visualizations.",
            "value_constraint": "visualization"
        }
    }
}

```

### Pushing the project to Git
Host your visualization LookML on a publicly accessible GitHub repository. Assuming that you created the visualization in a Looker project, follow these steps to push it to a new repository:
  1. Create a publicly accessible GitHub repository.
  2. Set your Looker project's Repository URL to the URL of your GitHub repository.
  3. Follow the Git prompts in Looker to validate, commit, and deploy your code to production.


### Testing the functionality of the visualization
Test the new visualization by applying it to an appropriate Explore or Look on your Looker instance:
  1. Navigate to the Look or Explore.
  2. If on a Look, click **Edit** to edit the Look.
  3. Click the three-dot menu in the visualization type menu to open the drop-down list of visualizations.
  4. Select your custom visualization.
  5. Click **Save** to save the change to the Look. Note any dashboards that may be impacted by this change.


Looker requires these functions in the visualizations available from the Looker Marketplace:
Function | Required  
---|---  
Support for drilling into visualization | Yes  
Ability to inherit Looker's color palettes | Yes  
Responsiveness to browser and screen size | Yes  
Consistent font family: `font-family`: `Helvetica`, `Arial`, `sans-serif` | Yes  
Font sizing | Yes  
Ability to toggle **Value Labels** and **Axis Labels** in the visualization configuration panel | Yes  
Visualization of pivoted data | Yes (when applicable)  
Visualization updates based on user interactivity using the `updateAsync` function or `is update` function`` | Yes  
Clear error messages (for example, "This visualization requires 1 dimension and 2 measures") | Yes  
All options in visualization configuration panel make an apparent change to the visualization | Yes  
Use of field's `value` formatting by default | Yes (when applicable)  
Error is thrown when a query returns no results | Yes  
### Submitting the visualization for review
Once your visualization is ready for submission, follow the instructions at Submitting content to the Looker Marketplace to create supporting documentation for your visualization, submit your visualization to the Looker team for review, and publish your visualization to the Looker Marketplace.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


