# Quickstart: Generate a model from sample data  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-core-qs-model-generation

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Navigate to the Create a Model page
  * Define your model
  * View your model
    * View the model files in the Looker IDE
    * View the model on the LookML Projects page
    * View the Explore that was created by the model




Was this helpful?
Send feedback 
  * On this page
  * Before you begin
  * Navigate to the Create a Model page
  * Define your model
  * View your model
    * View the model files in the Looker IDE
    * View the model on the LookML Projects page
    * View the Explore that was created by the model


# Generate a model from sample data
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Learn how to use Looker (Google Cloud core) to automatically generate a basic data model from a connection that is included in each instance.
Each Looker (Google Cloud core) instance comes with the sample LookML project that is installed by default on the instance. The sample LookML project includes curated LookML models that are based on the public BigQuery dataset `the Look eCommerce`. The sample LookML project uses a connection, `sample_bigquery_connection`. You can use this connection to generate a new data model that is based on one of the sample project's tables. Since this quickstart is for instructional purposes only, you'll delete the data model at the end of the process.
## Before you begin
To follow along with this quickstart, you'll need the following:
  * Access to a Looker (Google Cloud core) instance that includes the sample LookML project.
  * Someone with the **Looker Admin** IAM role must enable the BigQuery API for the Google Cloud project that contains your Looker (Google Cloud core) instance. 
Enable the API
  * You must have either the **Looker Admin** role or the `develop` permission.


## Navigate to the Create a Model page
  1. On the Looker (Google Cloud core) homepage, click the Looker **Main menu** icon menu and enable Development Mode by selecting the **Development Mode** toggle at the bottom of the menu.
  2. On the Looker (Google Cloud core) homepage, click the **Create** button in the main navigation menu to open the drop-down menu.
  3. From the drop-down menu, select **LookML Model** to open the **Create a Model** page.


## Define your model
On the **Create a Model** page, follow these steps:
  1. In the **Select Database Connection** section, select `sample_bigquery_connection` from the drop-down menu.
  2. Select the radio button to add the model to the `sample_thelook_ecommerce` project, and click **Next**.
  3. In the **Select Tables** section, leave the default Google Cloud project in the **Select GCP project** field.
  4. In the **Datasets** field, select `bq_dataset`.
  5. Click the arrow to the right of `bq_dataset` to get to the **Tables** field.
  6. In the **Tables** field, select `bq_table`.
  7. Click the arrow to the right of `bq_table` to get to the **Fields** field.
  8. In the **Fields** field, select all the fields, and click **Next**.
  9. In the **Select Primary Keys** section, select **Name** as the primary key, and click **Next**.
  10. In the **Select Explores to Create** section, select the `bq_table.view` file, and click **Next**.
  11. In the **Enter Model Name** section, enter a unique model name.
  12. Click the **Complete and View Model** button. This action takes you to the Looker IDE.


## View your model
Once you've completed all fields in the **Create a Model** page, view the model that Looker generated.
### View the model files in the Looker IDE
  1. After clicking the **Complete and View Model** button, you will be in the Looker IDE. In the IDE file browser, you see the folders for the pre-existing sample LookML models, which are `0_start_here`, `1_basic_lookml`, `2_intermediate_lookml`, and `3_advanced_lookml`. You also see the folders created for the generated model, `models` and `views`.
  2. Expand the `models` and `views` folders to see the LookML files that Looker created for the model that you defined on the **Create a Model** page. The blue dot next to each file indicates that they are new files and not yet deployed to production. 
     * The `.model` file defines the model. In the model file, you can see the connection that you selected, the `bq_table` view, as well as other default configurations.
     * The `bq_table.view` file defines the view. In the view file, you can see the `birthdate`, `name`, and `rating` fields that you selected and how they are defined in the BigQuery database table, as well as a default `count` measure that Looker added.
  3. You also see the `README.md` file that Looker generated because the **Generate a Readme file that gives more information about using LookML** checkbox on the **Create a Model** page was selected by default.


### View the model on the LookML Projects page
  1. From the IDE, open the main navigation menu by clicking the **Main menu** icon.
  2. If you aren't already in the **Develop** menu, click **Develop**.
  3. From the **Develop** menu, select **Projects** to navigate to the **LookML Projects** page.
  4. View your model in the **Models** column of the **sample_thelook_ecommerce** row. It appears along with the `advanced_ecomm`, `basic_ecomm`, and `intermediate_ecomm` models from the sample LookML project.


### View the Explore that was created by the model
  1. From the **Projects** page, click the name of your model to return to the model file in the IDE.
  2. With the model file open in the IDE, click the **See file actions** arrow next to the filename at the top of the IDE.
  3. Select **Explore Bq Table- your_model_name** from the drop-down menu. This selection takes you to the **Bq Table** Explore that was created by your model.
  4. In the field picker, note the **Birthdate Date** , **Name** , and **Rating** dimensions that you selected on this **Create a Model** page, as well as the default **Count** measure.


The model files, model configuration, and Explore that you've viewed are available only in your personal Git branch while in Development Mode. If you wanted to make this model available to other users in your Looker (Google Cloud core) instance, you would commit your changes, merge your branch, and deploy the production branch. However, for the purposes of this quickstart, you will delete this model, as described in the next section.
## Clean up
To maximize Looker performance, unnecessary models shouldn't be deployed to production. To maintain a clean personal Git branch and avoid accidentally deploying this model to production, complete the following steps to delete the model:
  1. From the Explore, click the **Go to LookML** link in the field picker. This action takes you to the Looker IDE.
  2. In IDE, select the **Git Actions** icon.
  3. In the **Git Actions** menu, click **Revert to**.
  4. In the **Revert to** window, make sure that the **Revert uncommitted changes** option is selected, and click **Confirm**.
  5. In the IDE, you should no longer see your model files.
  6. To delete the model configuration, navigate to the **Projects** page by clicking **Projects** in the **Develop** menu.
  7. Locate your model in the table, and click the **Configure** button in its row.
  8. Make sure you are in the window for your model by checking the name in the **Model** field, and click **Delete Model Configuration**.


## What's next
  * Generating a LookML model
  * Looker IDE overview
  * Managing LookML files and folders
  * Common LookML patterns
  * Using version control and deploying


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


