# Quickstart: Model your data in LookML  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-core-qs-model-data

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Turn on Development Mode
  * Navigate to the sample LookML project in the Looker IDE
  * Create a new project folder
    * Additional information about IDE folders
  * Create a new LookML model file
    * Additional information about model files
  * Create a new LookML view file
    * Additional information about view files
  * Looker IDE Quick Help
  * Create Explores for your views
    * Additional information about Explores
  * Create a new field
    * Additional information about LookML fields
  * View and test your changes in the Looker UI
  * Validate your LookML
  * Commit your changes




Was this helpful?
Send feedback 
  * On this page
  * Before you begin
  * Turn on Development Mode
  * Navigate to the sample LookML project in the Looker IDE
  * Create a new project folder
    * Additional information about IDE folders
  * Create a new LookML model file
    * Additional information about model files
  * Create a new LookML view file
    * Additional information about view files
  * Looker IDE Quick Help
  * Create Explores for your views
    * Additional information about Explores
  * Create a new field
    * Additional information about LookML fields
  * View and test your changes in the Looker UI
  * Validate your LookML
  * Commit your changes


# Model your data in LookML
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Learn how to use LookML and the Looker IDE to model your data in a structured and reusable way.
The easiest way to model your data in Looker is to have Looker itself automatically generate LookML files that are based on the tables in your database. You can practice doing that with the Generate a model from sample data quickstart, and you can see the full procedure on the Generating a LookML model documentation page.
The point of this quickstart is to show you how to add LookML files manually to your project and how to manually create new LookML elements so that you can customize your LookML project to your specific data and needs. This quickstart will walk you through manually creating a LookML model file and a LookML view file, creating an Explore for your view, creating a new dimension in your view file, and testing your new measure in the Explore UI. This quickstart will also walk you through turning on Development Mode, navigating the Looker IDE, and using the Looker IDE Quick Help feature. This quickstart will also provide links to the relevant documentation for learning more about these topics.
As a starting point, this quickstart uses the sample LookML project that is automatically configured on Looker (Google Cloud core) instances.
## Before you begin
To follow along with this quickstart, you'll need the following:
  * Access to a Looker (Google Cloud core) instance: 
    * The instance must include the sample LookML project.
    * The instance's Google Cloud project must have the BigQuery API enabled. The **Looker Admin** IAM role is required to enable the BigQuery API. 
Enable the API
  * A Looker user account with either the **Looker Admin** role or the `develop` permission.


## Turn on Development Mode
Looker projects can exist in one of two modes: Production Mode and Development Mode. Development Mode lets you make changes to LookML files and preview how they will affect content on your instance without affecting the production environment (what other users see). See the Development Mode and Production Mode documentation page for more information.
For this quickstart, you will use Development Mode so that you can make changes to the LookML files and test your changes in an Explore.
To turn on Development Mode, follow these steps:
  1. On the Looker (Google Cloud core) homepage, click the Looker **Main menu** icon menu to expand the main navigation menu, if not already expanded.
  2. Select the **Development Mode** toggle at the bottom of the menu.


When Development Mode is enabled, Looker displays the **Development Mode** banner at the top of the screen.
## Navigate to the sample LookML project in the Looker IDE
A LookML project is a collection of LookML files that tell Looker how to connect to your database, how to query your data, and how to present the data in the user interface. In this quickstart, you will use the sample LookML project that is automatically configured on Looker (Google Cloud core) instances.
To navigate to the sample LookML project files in the Looker IDE, follow these steps:
  1. Click the Looker **Main menu** icon menu and select **Develop** , if the **Develop** menu isn't already displayed.
  2. From the **Develop** menu, select **sample_thelook_ecommerce**.


Looker will open the **File Browser** panel of the Looker IDE and display the sample LookML project files.
## Create a new project folder
To keep the files that you create in this quickstart separate from the rest of the files in the LookML sample project, you will create a new project folder for the quickstart files.
To create a folder in your project, follow these steps:
  1. In the **File Browser** panel of the Looker IDE, click the **Add file or folder** add icon at the top of the panel, and select the **Create Folder** option from the **Add file or folder** menu.
  2. For the name of the new folder, enter `quickstart`.
  3. Click **Create**.


Looker adds the new folder to the **File Browser** panel in the Looker IDE.
### Additional information about IDE folders
To learn more about using folders in your LookML project, see the following documentation pages:
  * To create your own folders and files in the future, and for considerations for creating folders in your project, see the Managing LookML files and folders documentation page.
  * To learn more about the Looker IDE file browser, see the Working with the IDE file browser documentation page.


## Create a new LookML model file
A LookML model file specifies a database connection and the set of Looker Explores that use that connection. An Explore is a starting place for your users to query your data in Looker once your data is modeled in LookML (see Viewing and interacting with Explores in Looker).
To create a new model file in your LookML project, follow these steps:
  1. In the **File Browser** panel of the Looker IDE, select the three-dot **Folder Options** menu for the `quickstart` folder that you created in the Create a new project folder procedure.
  2. From the **Folder Options** menu, select **Create Model**.
  3. In the **Create File** dialog, enter the name `quickstart_practice` for the new file, and then click **Create**. Looker creates the `quickstart_practice.model` file under the `quickstart` folder and opens the new file in the Looker IDE. The blue dot next to the file in the **File Browser** panel indicates that the file is new.
  4. In the **File Browser** panel, click the `quickstart` folder to expand it and see the `quickstart_practice.model` file.
  5. In the Looker IDE, click the `quickstart_practice.model` file to open it if it isn't already open.


The `quickstart_practice.model` file contains example LookML that you can use as a starting point for your project. For now, you can keep the file as it is. Later in the quickstart, you will create Explores in your model file.
### Additional information about model files
To create your own model files in the future, note the following resources:
  * For information about model files in general, see the Model files section of the LookML project files documentation page.
  * For the full procedure and other options for creating files in your project, see the Managing LookML files and folders documentation page.
  * For information about the naming conventions for LookML files, see the Before you begin: Important file and folder naming conventions section on the Managing LookML files and folders page.
  * For information about the LookML parameters that you can use in a model file, see the Model parameters documentation page.


## Create a new LookML view file
In LookML, a view corresponds to either a single table in your database or a single derived table. The view file specifies the table in your database to query and the fields (dimensions and measures) to include from that database table. Once you define a field in the view file, you can use the `$` substitution operator to reference the field in other parts of your LookML. This lets you define the field in a single location while using it in multiple places in your LookML project.
There are several ways to create a new view file, but the easiest way to get started is to have Looker itself automatically generate a view file based on an existing table in your database.
To have Looker generate a new view file, follow these steps:
  1. In the **File Browser** panel of the Looker IDE, select the three-dot **Folder Options** menu for the `quickstart` folder that you created in the Create a new project folder procedure.
  2. Select **Create View from Table** from the **Folder Options** menu.
  3. On the **Create Views from Tables** page, click the **Enter custom db** input field and type `bigquery-public-data`:
  4. Press **Enter** to see the BigQuery public datasets.
  5. Scroll through the list until you find the `thelook_ecommerce` dataset.
  6. Click the `thelook_ecommerce` dataset to expand it.
  7. Select the `order_items` table.
  8. Click the **Create Views** button at the bottom of the page.


Looker displays the `order_items` view file in the Looker IDE. In the File Browser panel, the `quickstart` folder is expanded and the `order_items` view file is displayed with a blue dot to indicate that it is a new file.
### Additional information about view files
To create your own view files in the future, note the following resources:
  * For information about view files in general, see the View files section of the LookML project files documentation page.
  * For the full procedure and other options for creating files in your project, see the Managing LookML files and folders documentation page.
  * For considerations specific to creating view files, see the Considerations for creating view files section on the Managing LookML files and folders page.
  * For information about the naming conventions for LookML files, see the Before you begin: Important file and folder naming conventions section on the Managing LookML files and folders page.
  * For information about the LookML parameters that you can use in a view file, see the View parameters documentation page.


## Looker IDE Quick Help
You have now created a LookML model file and a LookML view file. In the next steps of this quickstart, you will start editing these files. Before you start editing, you should familiarize yourself with the Looker IDE Quick Help feature. The **Quick Help** panel provides explanations and options for the current cursor location in your LookML files:
  * In the IDE editor panel, you can click the fields and parameters in your LookML files, and the **Quick Help** panel will display the supported options and subparameters for that LookML element.
  * In the **Quick Help** panel, you can click a parameter name to open the Looker documentation page for that parameter.


If the **Quick Help** panel is not already open, you can open it by clicking the **Quick Help** icon in the Looker IDE:
## Create Explores for your views
After you have performed the Create a new LookML model file procedure and the Create a new LookML view file procedure, you can define an Explore for your new view file so that you can use Looker to query the data that you have modeled in the view file.
Explores are typically defined in a model file. (You can create a separate Explore file, but for the purposes of this quickstart, you will create the Explore in the model file.)
In the LookML file where you define an Explore you must use the `include` parameter so that you can reference the view file in the Explore definition. This procedure walks you through these steps.
To create an Explore for the `order_items` view file, follow these steps:
  1. In the Looker IDE, open the `quickstart_practice.model` file.
  2. In the `quickstart_practice.model` file, replace the existing line that contains the `include` parameter with the following line:
```
include: "/quickstart/order_items.view"

```

  3. Add a new line under the `include` parameter, and enter the following LookML: alue, which you can select from the field `none explore: order_items {}`
  4. Click the **Save Changes** button at the top of the Looker IDE.


This Explore is the most basic example of an Explore that allows users to query the `order_items` view. From this starting point, you can build out your Explore in many ways.
### Additional information about Explores
To create your own Explores in the future and to build out your Explores, note the following resources:
  * For more information about creating Explores, see the Creating and editing Explores documentation page.
  * For information about joining in other views, see the Working with joins in LookML documentation page.
  * For information about the LookML parameters that you can use for an Explore, see the Explore parameters documentation page.
  * For information about querying data in an Explore page in the Looker UI, see the Viewing and interacting with Explores in Looker documentation page.


## Create a new field
After you have created the view files in the Create a new LookML view file section of this quickstart, you can see the fields that Looker created automatically. When you create a view file that is based on a database table, Looker automatically creates dimensions, dimension groups, and measures:
  * A dimension is a field that represents an attribute, fact, or value, which users can select from the field picker within an Explore and can be used to filter a query. If the field is not inside an aggregate function like SUM, COUNT, and the like, it is a dimension. Looker automatically creates a dimension for each column in your database table.
  * A dimension group is used to create a set of time-based or duration-based dimensions all at once. For example, the dimension group for a timestamp column will contain individual dimensions for date, month, quarter, time, week, and year. Looker automatically creates a dimension group for the time-based fields that Looker detects in your database table.
  * A measure is a field in an Explore that represents measurable information about your data, such as sums, counts, etc. A measure is declared in a view file and can be of an aggregate or non-aggregate type. Looker automatically creates a measure of `type:count` for your view file, which is the equivalent of a `COUNT(*)` in SQL.


In this section, you will learn how to manually add your own dimension to the `order_items` view file.
To manually create a new dimension in the `order_items` view file, follow these steps:
  1. Open the `quickstarts/order_items.view` file if it isn't already open: In the **File Browser** panel of the Looker IDE, click the **quickstart** folder to expand it, and then click the `order_items.view` file to open it.
  2. In the `quickstarts/order_items.view` file, create a new line before the first `dimension` parameter in the file.
  3. On the new line, start typing `dimension`. As you type, the Looker IDE will display a list of possible parameters that start with the text that you have typed.
     * Use the arrow keys to navigate the suggestion list to the `dimension` option.
     * Press **Enter** to insert the selected parameter into your LookML. Looker will insert a new `dimension` parameter on the new line that you created.
  4. To provide a name for the new dimension, click in the IDE before the `{}` and type `shipped_to_delivered_days`.
  5. Click inside the `{}` and press **Enter** to create a new line inside the `{}`.
  6. Complete the LookML for the new dimension (you can either copy and paste the following LookML or manually enter the LookML to see how the Looker IDE provides guidance):
```
dimension: shipped_to_delivered_days {
  group_label: "Other Dates"
  type: duration_day
  sql_start: ${shipped_raw} ;;
  sql_end: ${delivered_raw} ;;
}

```

  7. At the top of the Looker IDE, click the **Save Changes** button.


Looker will save the view file with your new dimension. For your new lines in the file, the Looker IDE will shade the line numbers in green.
### Additional information about LookML fields
To create your own fields in the future, note the following resources:
  * For information about LookML fields in general, see the LookML field reference documentation page.
  * For information about the types of dimensions, filters, and parameters that you can create in a view file, see the Dimension, filter, and parameter types documentation page.
  * For information about the types of measures that you can create in a view file, see the Measure types documentation page.


## View and test your changes in the Looker UI
If you performed the Create Explores for your views procedure to create an Explore for the `order_items` view file, you can see your new dimension in the Looker Explore UI.
To view and test your changes in the Explore in the Looker UI, follow these steps:
  1. From the `quickstarts/order_items.view` file in the Looker IDE, click the **See file actions** arrow icon by the name of the view file at the top of the file editor panel, and select the **Explore Order Items - quickstart_practice** option.
  2. In the **Order Items** Explore field picker, click the **Other Dates** group label to expand it, and then click the **Shipped to Delivered Days** dimension to add it to the Explore. (You can also search for the dimension by typing `Shipped to Delivered Days` in the field picker search box.)
  3. In the **Order Items** Explore field picker, click the **Shipped Date** group label to expand it, and then click the **Date** dimension to add it to the Explore.
  4. In the **Order Items** Explore field picker, click the **Delivered Date** group label to expand it, and then click the **Date** dimension to add it to the Explore.
  5. Click the **Run** button at the top of the Explore.


Looker will run the query and display the results in the **Data** section of the Explore. For each line, you can verify that the value in the **Order Items Shipped to Delivered Days** shows the correct number of days between the **Order Items Shipped Date** value and **Order Items Delivered Date** value.
## Validate your LookML
For the purposes of this quickstart, you don't need to validate your LookML. However, in the future, when you create your own projects to model your data, it is good to know about the Looker tools for validating your LookML.
As you edit your LookML, the Looker IDE will alert you to any unresolved syntax errors within a single file (see the Looker IDE overview documentation page). You can also perform a full model validation, which will check your LookML for any errors. See the Validating your LookML documentation page for more information.
## Commit your changes
In this quickstart, you are using a pre-configured Git connection that is set up for the sample LookML project. However, in the future, when you create your own projects to model your data, you will need to set up a Git connection for your project.
As you make changes to your LookML project files, the Looker IDE will display different operations for the Git button in the top right corner of the IDE. The button shows different operations to guide you through the process of validating your LookML and deploying your changes to production.
The LookML files and Explore that you've viewed in this quickstart are available only in your personal Git branch while in Development Mode. If you wanted to make this model available to other users in your Looker (Google Cloud core) instance, you would commit your changes, merge your branch, and deploy the production branch.
For the purposes of this quickstart, you won't deploy your changes to production. Instead, you will delete these files, as described in the Clean up procedure.
## Clean up
To maximize Looker performance, unnecessary models shouldn't be deployed to production. To maintain a clean personal Git branch and avoid accidentally deploying these files to production, complete the following steps to delete the files that you created in this quickstart:
  1. Click the Looker **Main menu** icon menu and select **Develop** , if the **Develop** menu isn't already displayed.
  2. From the **Develop** menu, select **sample_thelook_ecommerce**.
  3. In the **File Browser** panel of the Looker IDE, select the three-dot **Folder Options** menu for the `quickstart` folder that you created in the Create a new project folder procedure.
  4. Select **Delete** from the **Folder Options** menu.
  5. In the **Delete Folder** window, click **Delete**.


Looker deletes the `quickstart` folder and all of its contents.
## What's next
  * Generating a LookML model
  * Looker IDE overview
  * Managing LookML files and folders
  * Types of files in a LookML project
  * Model parameters
  * Common LookML patterns
  * Using version control and deploying
  * How Looker generates SQL
  * Incorporating SQL and referring to LookML objects


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


