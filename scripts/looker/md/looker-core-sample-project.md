# Use the sample LookML project on a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-sample-project

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin: Enable the BigQuery API
  * View and interact with the sample LookML project
    * Access and edit the LookML project files
  * Build queries using the sample Explores
  * View and edit the sample dashboards
  * Run through a series of quickstarts using the sample LookML project
  * Change user access to the project
  * Remove the sample LookML project




Was this helpful?
Send feedback 
#  Use the sample LookML project on a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin: Enable the BigQuery API
  * View and interact with the sample LookML project
    * Access and edit the LookML project files
  * Build queries using the sample Explores
  * View and edit the sample dashboards
  * Run through a series of quickstarts using the sample LookML project
  * Change user access to the project
  * Remove the sample LookML project


Looker (Google Cloud core) provides a sample LookML project that can help you achieve the following:
  * Learn to write LookML
  * Use the Explore interface to query data
  * View existing analyses with dashboards


The sample LookML project is provided on Looker (Google Cloud core) instances of all edition types.
The sample LookML project on Looker (Google Cloud core) instances includes curated LookML models that are based on the public BigQuery dataset `the Look eCommerce`. This project is a good starting point for learning to build your own LookML models and modify existing models to customize the user experience.
When you create a Looker (Google Cloud core) instance, the sample LookML project is already configured on your instance as a bare repository using application default credentials (ADC) to connect to a BigQuery database managed by Google.
## Before you begin: Enable the BigQuery API
Before you can modify the LookML, query the Explores, and view the sample dashboards from the sample LookML project, someone with the **Looker Admin** IAM role must enable the BigQuery API for the Google Cloud project that contains your Looker (Google Cloud core) instance. After enabling the API, refresh the console page to confirm that the API has been enabled.
Enable the API
## View and interact with the sample LookML project
You can view the sample LookML project by navigating to the project called `sample_thelook_ecommerce` in the Looker IDE. The `sample_thelook_ecommerce` project includes four folders: `0_start_here`, `1_basic_lookml`, `2_intermediate_lookml`, and `3_advanced_lookml`. These folders include the following elements:
  * `README.md` files with instructions and explanations of basic, intermediate, and advanced LookML concepts
  * Predefined LookML models with a connection to the sample BigQuery connection `sample_bigquery_connection`
  * Predefined LookML Explores and views that you can customize


By following the instructions in the project's `README.md` files, you can learn to make changes to the sample LookML and see how those changes affect the Explore interface. The sample LookML project also includes prebuilt dashboards that you can add to and modify to create sample analyses.
### Access and edit the LookML project files
To access the LookML files within the sample LookML project, follow these steps:
  1. In the left navigation panel, select **Develop** to open the **Develop** menu.
  2. Select the `sample_thelook_ecommerce` project. By default, navigating to the sample project opens the `START_HERE_README.md` file.
  3. Read the instructions in the `START_HERE_README.md` files, or navigate to a different project file.
  4. If you want to start testing out changes to the LookML, enter Development Mode and follow the instructions in the `README.md` file.


## Build queries using the sample Explores
By default, the sample LookML project has the following Explores defined:
  * **1) Basic Ecommerce**
  * **2) Intermediate Ecommerce**
  * **3) Intermediate Ecommerce (Valid Orders only)**
  * **4) Advanced Ecommerce (Valid Orders only)**


To access the sample Explores, follow these steps:
  1. In the left navigation panel, select **Explore** to open the **Explore** menu.
  2. In the **Explore** menu, select one of the sample Explores.


For more information about querying data with Explores, follow the instructions in the `README.md` files or visit Viewing and interacting with Explores in Looker.
## View and edit the sample dashboards
By default, when you create your instance, the instance contains the following sample user-defined dashboards from the sample project:
  * **Business Pulse - Basic visualization examples**
  * **Business Pulse - Intermediate visualization examples**
  * **Business Pulse - Advanced visualization examples**


While the instance contains no other content, such as user-created Looks or dashboards, these sample dashboards appear on the pre-built homepage for the instance.
Additionally, these sample dashboards appear in the **Shared folders** folder (called **Your organization's folder**) in your instance.
To access the sample dashboards in the **Shared folders** folder, follow these steps:
  1. In the left navigation panel, select **Folders**.
  2. On the **All folders** page, select **Shared folders**.
  3. On the **Your organization's folders** page, select one of the sample dashboards.


You can then view and make changes to the dashboards. For more information, see Viewing dashboards and Editing user-defined dashboards.
## Run through a series of quickstarts using the sample LookML project
If your Looker (Google Cloud core) instance is set up with the sample LookML project, you can use the following series of quickstart guides to walk through the different steps you need to get started using Looker (Google Cloud core), from connecting to your data warehouse to creating and sharing dashboards with rich visualizations. The quickstarts walk you through common Looker procedures using the sample LookML project. Once you are familiar with the procedures, you can apply the steps to your own data connections and datasets.
The following quickstarts are shown in the order that is generally required to set up and use a Looker instance from scratch. But because the quickstarts use the sample LookML project, you can do these quickstarts independently of each other, in whatever order you prefer:
  1. Create a connection for a public IP instance — Learn how to create a database connection for a Looker (Google Cloud core) public IP instance to use as the basis for any LookML project, or for a specific LookML project.
  2. Generate a model from sample data — Learn how to use Looker (Google Cloud core) to automatically generate a basic data model from a connection that is included in each instance.
  3. Model your data — Learn how to add additional dimensions, measures, and filters to the model that was generated from sample data.
  4. Build a dashboard with sample data — Learn how to create a dashboard with sample data from the **Intermediate Ecommerce** Explore in the sample LookML project on your Looker (Google Cloud core) instance.
  5. Build a Look with sample data — Learn how to query and visualize data in Looker and to save your query results as a Look that you can share and reuse.


## Change user access to the project
By default, users who have any of the default Looker roles will have the **All** model set on your Looker (Google Cloud core) instance. Therefore, by default, all users will be able to access all the models that are defined in the `sample_thelook_ecommerce` project.
If you want to exclude specific users from viewing or interacting with one or more models from the project, you can create a model set that doesn't include the models in `sample_thelook_ecommerce`. Then, create a new role or update an existing role that is linked to the new, more limited model set.
## Remove the sample LookML project
You can remove the sample project and connection from your instance. To remove the project, follow the instructions in Accessing and editing project information.
You can also delete the `sample_bigquery_connection` connection by following the instructions on the Connections documentation page.
## What's next
  * Introduction to LookML
  * LookML terms and concepts
  * Generating a new model
  * Accessing LookML project files
  * Looker (Google Cloud core) quickstart overview


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


