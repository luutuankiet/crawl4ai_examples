# Looker Blocks  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/blocks

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Types of Looker Blocks
  * Installing a Looker Block
  * Standardization and customization
  * Using data blocks
    * Accessing datasets on Google BigQuery
    * Accessing datasets on other databases
    * Accessing the LookML model
    * Adding data blocks to projects
    * Example setup of the demographic dataset




Was this helpful?
Send feedback 
#  Looker Blocks
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Types of Looker Blocks
  * Installing a Looker Block
  * Standardization and customization
  * Using data blocks
    * Accessing datasets on Google BigQuery
    * Accessing datasets on other databases
    * Accessing the LookML model
    * Adding data blocks to projects
    * Example setup of the demographic dataset


Looker Blocks are prebuilt data models for common analytical patterns and data sources. Reuse the work others have already done rather than starting from scratch, then customize the blocks to your exact specifications. From optimized SQL patterns to fully built-out data models, Looker Blocks can be used as a starting point for quick and flexible data modeling in Looker.
You can obtain Blocks to customize and add to your Looker instance from a variety of sources, including the following:
  * The standalone Looker Marketplace, where you can browse for Blocks and access their source code.
  * The Looker Marketplace that is accessible from your Looker instance. From this Marketplace, you can browse and install Looker Blocks — called "models" — directly into your Looker instance. See the Using the Looker Marketplace documentation page for more information about installing tools from the Looker Marketplace.


## Types of Looker Blocks
Looker Blocks offer a variety of capabilities, such as the following:
  * Data blocks, which include both public datasets and full LookML models, require copying the LookML model from a GitHub repository to access the modeled tables. These blocks are not customizable. See Using data blocks on this page for detailed instructions.
  * Data collection applications, such as Segment and Snowplow, track events in a relatively standardized format. This makes it possible to create templatized design patterns — capable of data cleaning, transformation, and analytics — that can be used by any customer using these applications.
  * Other web applications — such as Salesforce — let you add custom fields for your internal users. Naturally, this creates data in a less standardized format. As a result, we can templatize some of the data model to get the analytics up and running, but you'll need to customize the non-standardized portion.
  * There are also blocks for general business insights. These blocks are optimized SQL or LookML design patterns that are independent from the data source. For example, many companies will want to analyze the lifetime value of a customer over time. There are some assumptions baked into these patterns, but they can be customized to match your specific business needs. These patterns reflect Looker's point of view on the best way to conduct certain types of analysis.


Looker Blocks are browseable in the directory of the public instance of the Looker Marketplace at `marketplace.looker.com`.
## Installing a Looker Block
To install a Looker Block from the Marketplace that is associated with your Looker instance, follow the instructions about installing a tool from the Marketplace.
To install a Looker Block from `marketplace.looker.com`, follow the instructions in the block's source code.
Each Looker Block has specific usage instructions.
## Standardization and customization
The degree to which you may need to customize your block may depend on how standardize your database schema is. Most Looker Blocks require some customization to fit your data schema.
Some blocks demonstrate both Explores and views in the same file. This is for ease of viewing, but in general you'll want to copy the appropriate sections of LookML into the appropriate places in your data model. See the Types of files in a LookML project documentation page for more information.
In some cases you may need to create new LookML files in your data model to house the examples.
## Using data blocks
Data blocks are a special type of Looker Block that provide the dataset as well as the data model. Data blocks include public data sources, such as:
  * **Demographic data** : Common demographic metrics from the American Community Survey at the state, county, zip code tabulation area, and even census block group level.
  * **Weather data** : Weather reporting in the United States at the zip code level from 1920 through the previous day. This block is updated nightly.


The procedure for accessing a data block's dataset varies depending on your database schema. The following sections contain instructions for accessing datasets on these databases:
  * Additional databases


### Accessing datasets on Google BigQuery
If you have an existing Google BigQuery account, you can access Looker's BigQuery-hosted datasets. Skip ahead to the Adding data blocks to projects section on this page.
If you don't already have a Google BigQuery account, you can set up a free trial and then access Looker's public datasets on BigQuery.
### Accessing datasets on other databases
Transformed data for Amazon Redshift, MySQL, PostgreSQL, or Oracle datasets is publicly available in both Google Cloud Service and S3 so that you can directly import them into the database of your choice.
We've also made the Data Definition Language (DDL) available for each of the datasets in the GitHub Repo. The DDL statements might need to be modified for the datatypes in your selected database, but should provide an idea of the column types for each table.
Download data directly from one of these locations:
  * **Google Cloud Service** : `_gs://looker-datablocks/_`
  * **S3** : `_s3://looker-datablocks/_`
  * **S3 Bucket Web Link** : http://looker-datablocks.s3-website-us-east-1.amazonaws.com/


### Accessing the LookML model
Fork one of our GitHub repositories into a new GitHub repository (either hosted by Looker or by your company) that you can then extend or refine within your instance:
  * Demographic Data (American Community Survey) - https://github.com/llooker/datablocks-acs
  * Weather (GSOD) - https://github.com/llooker/datablocks-gsod


### Adding data blocks to projects
In addition to the method described in this section, you can also use LookML refinements to build on the LookML of views and Explores in your projects.
To add a data block to your project:
  1. Add a new project to your Looker instance.
  2. Fork or copy the GitHub repositories mentioned previously to access prebuilt LookML. Be sure to create a new GitHub repo.
  3. Remove other database dialect files from the repo. Looker Blocks will typically contain files for Google BigQuery, Amazon Redshift, and Snowflake. For example, if you are setting up data blocks on Google BigQuery, you will _only_ need the Google BigQuery view files, Google BigQuery Explore file, and Google BigQuery model file.
  4. Replace the connection name in your model file with your database connection where the data for data blocks lives. If you are using Google BigQuery or Snowflake, use the database connection from which you will be extending or refining.
All join logic exists in an `.explore` file in each of the repositories. This is the file you will be including in the following steps, after you have set up your project manifest.
  5. In your main Looker project where you will be extending or refining data blocks, create a project manifest file.
  6. Add the following LookML to the project manifest file to reference data blocks in your main Looker project:

```
    project_name: "<your_project_name\>"

    local_dependency: {
      project: "<project_name_of_datablock\>"
    }

```

#### Setup considerations and options
**Google BigQuery** : Be sure to use the correct set of modeled files. If you are on Google BigQuery, you may want to reference all files with `_bq_` in the filename. You may have to adapt our Google BigQuery model dialects to your own database dialect.
**Extensions** : All our projects have been set up to allow for extensions from Explore files, since model extensions could cause issues with multiple connections.
**Joining Derived Tables** : You may want to take a look at our documentation for native derived tables. You can let Looker write SQL for you at different levels of aggregation on our publicly available datasets and join them into your model.
**Merging Result Sets** : You can also choose to merge result sets from our datasets with your data by combining query result sets.
### Example setup of the demographic dataset
  1. Get access to data by either downloading raw data from our S3 or Google Cloud Service buckets or by connecting to a Looker database.
  2. Import the **Demographic Data Block** model from LookML as a separate project in your Looker instance.
  3. Use the `include` parameter to bring in the view file.
  4. Then either extend or refine the view file, or make use of native derived tables to get data at the level of aggregation that is necessary for Explores.
In our example, since the demographic data is at a different level of aggregation than our e-commerce dataset (block group versus zip code) we use built-in derived tables to aggregate stats up to the zip code level. This eliminates messy many-to-many joins:
```
  include: "/american_community_survey/bq.explore"

  view: zipcode_income_facts {
    derived_table: {
      persist_for: "10000 hours"
      explore_source: fast_facts {
        column: ZCTA5 { field: tract_zcta_map.ZCTA5 }
        column: income_household { field: bg_facts.avg_income_house }
        column: total_population { field: bg_facts.total_population }
      }
    }
    dimension: ZCTA5 {}
    dimension: income_household {
      hidden: yes
    }

```

  5. Join view files into the model:
```
  include: "acs*.view"

  explore: order_items {
    join: users {
      sql_on: ${users.id} = ${order_items.user_id} ;;
      type: left_outer
      relationship: many_to_one
    }

    join: zipcode_income_facts {
      sql_on: ${users.zip} = ${zipcode_income_facts.ZCTA5} ;;
      type: left_outer
      relationship: many_to_one
    }
  }

```

  6. Explore and visualize the data.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


