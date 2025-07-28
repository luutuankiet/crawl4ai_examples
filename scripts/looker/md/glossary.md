# Glossary  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/glossary

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  Glossary
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


This page lists terms used in the Looker product and user documentation.
See the Looker and Looker Studio shared terms and concepts documentation page for information about the nuances between similar terms and concepts in Looker and Looker Studio.
## Symbol/Numeric     
$ is a substitution operator that lets you reference previously defined objects in LookML.
_see also_ **substitution operator**
## A 

access, access level
    
Admins have a variety of options for limiting what users can view and interact with in Looker.
_see also_ **content access**, **data access**, **feature access** 

action
    
A data action lets users perform tasks in other tools, directly from Looker. For example, the action can cause an email to be sent or can set values in other applications — or it can do anything else that you can configure a receiving server to do. The receiving server must be able to accept a JSON POST. 

Action Hub
    
Looker's Action Hub is a multi-tenant service that forwards data to Looker's integrated services. Any data your users send using an action will be processed temporarily on the Action Hub server rather than in your Looker instance. When your Looker admin or developer has set up an integrated service and a field tag to provide access to that service, you can select that service as an action when you drill into data and interact with that service. The Looker documentation often uses "action" and "integration" interchangeably. 

advanced deploy mode
    
Advanced deploy mode lets Looker developers with `deploy` permission select any Git commit on their LookML project and deploy it to the production version of their Looker instance. This is opposed to the default Git integration, where only the latest commit on the remote production branch can be deployed to the production version of a Looker instance. 

advanced filter
    
An advanced filter lets users create a dashboard filter with a field from an Explore that is not represented on the dashboard itself. 

advanced filter control
    
An advanced filter control is a type of dashboard filter control that provides some additional flexibility in the filter conditions dashboard creators can set up. To create an advanced control, select **Advanced** in the **Control** field in the filter configuration window. 

alert
    
Alerts enable users to specify conditions in the data of a dashboard tile that, when met or exceeded, trigger a notification to be sent at a desired frequency to specific recipients. Alerts are set on query-based or Look-linked tiles on user-defined dashboards or LookML dashboards; and they can be sent through email or with Looker's Slack or Slack Attachment (API Token) integrations. 

Application Time Zone
    
Application Time Zone is an admin setting for the default time zone in which scheduled Looks and queries run, where supported. When User Specific Time Zones are enabled, the Application Time Zone becomes the default time zone for users who do not have a time zone value set for their accounts.
_see also_ **time zone settings**, **User Specific Time Zones** 

asynchronous query
    
An asynchronous (or async) query is a data request that makes one call to start the request, one or more calls to check the completion status of the query, and one call to fetch the results of the completed query. Async queries can help avoid freezing apps, connection timeouts and long dashboard load times.
## B 

base view (of an Explore)
    
A base view is the view used as the starting point for building an Explore. From there, you can join other views into the base view to be used in the Explore. Typically, Explores are named after the base view, but you can also use the `from` parameter to name the Explore's base view if you don't want to name the Explore after its base view.
_see also_ **view**, **Explore** 

block, Looker Block
    
Looker Blocks are prebuilt pieces of LookML that you can use and customize to your exact specification. From optimized SQL patterns to fully built-out data models, blocks can be used as a starting point for quick and flexible data modeling in Looker. 

board
    
A board holds a collection of manually curated dashboards, Looks, and links. Dashboards and Looks, which are stored in folders, can be pinned to multiple boards. Boards may include links and descriptions to provide context and can make it easier for users to find the information that is most relevant to them. 

browse, browsing
    
Browsing involves viewing, sharing, sending, and downloading data from dashboards, Looks, and Explores.
## C 

closed system
    
Also called a multitenant installation, a closed system silos content to specific groups and prevents users from different groups from knowing about each other. 

code splitting
    
A technique for lazy loading of JavaScript until it is actually needed. Ideally, you want to keep the initially loaded JavaScript bundle as small as possible. This can be achieved by utilizing code splitting. Any functionality that is not immediately required is not loaded until it is actually needed. 

Community
    
Formerly known as Discourse, the Looker Community is a user forum featuring posts, discussions, questions, and ideas shared among Looker users and experts. 

component
    
Looker components are the technical implementation of the Looker Design System, built with React, TypeScript, and Styled Components. They consist of UI components, filter components, and visualization components. 

connection
    
In the **Admin** section of Looker, you establish the database connection from which a model will retrieve data. 

constant
    
Constants, which are defined with the LookML `constant` parameter in a project manifest file, let you specify a value that can be reused throughout a project. You can reference constants anywhere in your model where strings are accepted. 

content
    
In Looker's documentation, the term **content** typically refers to Looks and dashboards. 

content access
    
Content access controls whether a user or group can view or make changes to a board, or to a folder (called a Space prior to Looker 6.20) and its contents. The two content access levels are **View** and **Manage Access, Edit**. 

Content Validator
    
Looker's Content Validator searches your LookML for references to model, Explore, and field names. Developers can use the Content Validator after making changes to a project to check that their changes did not impact any of their users' saved Looks or query-based dashboard tiles. The Content Validator can also be used to find and replace LookML elements to fix errors due to changes. 

cross-filtering
    
Cross-filtering lets users apply ad hoc filters to dashboards. With cross-filtering, users can click a data point in one dashboard tile to have all dashboard tiles automatically filter on that value. Specific cross-filters cannot be saved to a dashboard, but they can be shared by sharing a cross-filtered dashboard's URL. 

customer-hosted (deployment, instance, installation, environment)
    
A "customer-hosted" deployment — also referred to as "self-hosted" or "on-prem" throughout this documentation — means that the product is installed by or for the customer at the customer's premises or on a customer-controlled server within a third-party data center. A customer-hosted deployment includes the in-product services, meaning the services that are hosted by Looker and accessible through the product, specifically licensing data, configuration backups, system error reports, data actions, and support tickets, as further described in the **Application Data Shared by Looker** section of Looker's security webpage. Looker support generally has no access to these instances for support or deployment purposes, and the customer must execute their own version updates.
To learn more about the comparative advantages of each hosting option, see the Choosing a hosting option for a Looker (original) instance documentation page.
All Looker (Google Cloud core) instances are Looker hosted.
_see also_ **Looker-hosted**
## D 

dashboard
    
A dashboard is essentially a collection of one or more saved queries, displayed as visualization or text tiles together on one page.
_see also_ **LookML dashboard**, **user-defined dashboard** 

dashboard element, element
    
An element is a tile or visualization on a LookML dashboard, created using the `element` parameter. 

dashboard file
    
A LookML dashboard is defined in a LookML project file with the extension `.dashboard.lookml`.
_see also_ **LookML dashboard** 

data access
    
Data access controls which data a user or group is allowed to view. This type of access can be restricted or granted either at the user level or at the data level.  

Database Time Zone
    
Database Time Zone is an admin setting for the time zone Looker uses to interpret your raw data.
_see also_ **Query Time Zone**, **time zone settings** 

datagroup
    
You can use one or more datagroup parameters to define a caching policy, to specify when to rebuild persistent derived tables (PDTs), and to trigger schedules. 

derived table
    
Derived tables let you create new tables that do not already exist in your database. A derived table is defined in a Looker view file and lets the user treat the output of a query as if it were a table in the database (typically used for "fact" tables). "Derived table" is a generic term for any type of derived table, including LookML-based (native) derived tables, SQL-based derived tables, temporary derived tables, and persistent derived tables (PDTs).
_see also_ **native derived table**, **persistent derived table**, **SQL-based derived table**, **temporary derived table** 

Development Mode
    
A developer can enter Development Mode to make and test LookML changes. The changes won't affect other users until they are deployed to production. 

development table
    
A development table is a persisted derived table that is built when you query the table during development. In some cases, the development table can be used in production when you deploy your changes. 

dialect
    
The SQL "flavor" of a database. Examples of supported dialects are Amazon Redshift, PostgreSQL, MySQL, and Google BigQuery Standard SQL or Legacy SQL. 

dimension
    
A dimension is a field that represents an attribute, fact, or value, which can be selected from the field picker within an Explore and can be used to filter a query. Common dimensions include such attributes as dates, names, and IDs, and often correspond to columns in your underlying data table. A dimension can also be created within a view file. 

dimension fill
    
Dimension fill is a feature that lets you instruct Looker to fill in missing dates or values for a given dimension, such as a **date** dimension with some years missing. You can avoid misleading graphs by preventing Looker from connecting the values in an incomplete set. The dimension fill option can be turned on or off with the `allow_fill` parameter. 

dimension group
    
Using a dimension group, you can create multiple dimensions for a single underlying date or time column in the database. For example, you could split a `duration`-type dimension group into intervals of days, weeks, months, and so on. 

drill
    
Looker makes it possible to drill into the data on a visualization or an Explore to get more specific information about a specific data point. To drill into data on a visualization, select the part of the visualization about which you'd like more information. For the **Data** section of an Explore, select the value of a measure, or select the value of a dimension that can be drilled into.
## E 

embed, embedding
    
Embedding involves using `iframe` code to place an object (for example, Looker charts or tables) into a website, a spreadsheet, or another location outside of Looker. An embed user is a user who is interacting with a Looker object that is embedded in a location outside of Looker. Embedded content can be public or private (requiring either a Looker login or a signed URL). 

Embed edition
    
An **Embed** edition is a Looker (Google Cloud core) edition type that includes all the features of the **Enterprise** edition as well as offering signed embedding; a private label option; custom themes; 500,000 Query API calls per month; and 100,000 Admin API calls per month. 

Enterprise edition
    
An **Enterprise** edition is a Looker (Google Cloud core) edition type that includes all the features of the **Standard** edition, supports unlimited users, includes additional security features such as VPC-SC and Private IP, and provides more robust monitoring through the Elite System Activity feature. 

entitlement
    
Entitlements define the Looker resources that a Looker extension can access. The extension will not be able to access a Looker resource unless that resource is listed in the entitlements. Entitlements are defined as part of an `application` parameter included in a LookML project manifest file. 

ephemeral derived table
    
An ephemeral derived table — more commonly called a temporary derived table — is a derived table that is not written to your database. A temporary derived table can be either a LookML-based (native) derived table or an  SQL-based derived table.
_see also_ **derived table**, **temporary derived table** 

Explore (_n._)
    
An Explore is the starting point for queries. An Explore shows a specified set of fields from its associated view file, and these fields can be selected from the field picker to construct a query, which can be saved as a Look or dashboard tile. Explore URLs can also be shared. 

explore, exploring (_v._)
    
Exploring involves using data to answer questions in Looker. 

Explore file
    
An Explore file is a LookML project file with the extension `.explore.lkml`. Can be used for extending Explores across models and for defining native derived tables. 

`explore` parameter
    
The `explore` parameter adds a view to Looker's menu of Explores. As a best practice, an Explore should be defined inside of a model file. Explores reference views and each Explore can contain joins to other views. An Explore can also be defined in an Explore file that is then included in a model file.
_see also_ **Explore file** 

extension
    
Extensions are web applications built with Looker components that are developed through the **Looker extension framework**. Some extensions, like the **Looker Data Dictionary**, are deployed through the Looker Marketplace and are available for all customers. See the extension-examples repository for examples. Some parts of the Looker UI refer to extensions as "applications." 
_see also_ **Looker Data Dictionary,** **Looker extension framework**
## F 

fanout (_n._), fan out (_v._)
    
A fanout occurs when one row of a primary data table can correspond to more than one row of a joined table, resulting in duplicated records and incorrectly calculated aggregations. In Looker, the fanout problem is avoided through the use of symmetric aggregates and by correctly defining the dataset's primary key. 

feature access
    
Feature access controls the types of actions a user is allowed to take in Looker. This type of access is managed by permission sets. 

field
    
Explores and views contain fields, mostly dimensions and measures, which are the fundamental building blocks for Looker queries. 

field picker
    
The field picker displays the dimensions and measure applicable to the data shown in an Explore. The Looker developer or admin configures these dimension and measure options. The field picker may also display filter-only fields. 

filter component
    
Filter components are React-based, pre-built pieces of Looker's application that can provide Looker's filter functionality for custom-built data applications and customized embedded Looker dashboards. 

filter expression
    
Filter expressions are an advanced way to filter Looker queries. You can use them in the Explore section of Looker by adding a filter and choosing the **matches (advanced)** option. They are also used in LookML for elements that take a `filter` parameter. You can write filter expressions to filter on a string or to partially match strings, date and time, Boolean values, numbers, and location fields. 

folder
    
  1. In the Looker UI, a folder is a place where dashboards, Looks, and other folders (subfolders) are stored. Each user has a personal folder, and a Looker instance can also have various kinds of shared folders. Access to content in Looker is allocated at the folder level. Folders were called "Spaces" prior to Looker 6.20.
  2. In the Looker IDE, a folder is an organizational structure for your LookML files.



function
    
Looker functions let you transform your data or reference data in complex ways. They are similar in nature to Excel functions.
## G 

group, user group
    
Users can be added to one or more groups. Groups are useful for managing users' access to particular data, features, and content within Looker, as well as for assigning roles to users in bulk.
## H 

hybrid networking
    
Networking that occurs between Google Cloud and on-premises or other cloud provider environments. For a summary of hybrid networking connection options, visit the Network segmentation and connectivity for distributed applications in Cross-Cloud Network documentation page.
## I 

IDE
    
Integrated development environment. Looker's internal LookML editor, or an editor used to create and modify an extension. Examples of the latter are Visual Studio Code, Intellij, and WebStorm. 

incremental persistent derived table
    
An incremental persistent derived table is a type of persistent derived table (PDT) that is built incrementally, meaning that Looker appends fresh data to the table in specified increments, instead of rebuilding the entire table. This can lead to faster build times for your PDTs and less strain on your database. The increment is defined using the `increment_key` parameter. Incremental PDTs can be LookML-based (native) derived tables, SQL-based derived tables, or aggregate tables.
_see also_ **persistent derived table** 

instance
    
The server (or cluster of servers) that hosts Looker. Each client uses a production server (and, potentially, a staging server).
## J 

join
    
  * **(_n._)** The `join` parameter lets you define the join relationship between an Explore and a view, so that you can combine data from multiple views. You can join in as many views as you like for any given Explore.
  * **(_v._)** Combine data from multiple views by defining the relationship between an Explore and a view through a `join` parameter.


## L 

Labs feature
    
The **Labs** panel under the **Admin** menu lists Looker's new under-development features. These must be enabled by a Looker admin. 

legacy feature
    
Some product features have a **legacy feature** option that allows for the continued use of the legacy feature for a period of time (which may be useful for developing and implementing a migration plan). The **Admin** section of Looker lists the features for which the legacy feature option can be turned on. 

Lexp
    
_see also_ **Looker expression** 

Liquid parameter
    
In Looker, a Liquid parameter is a LookML parameter field that has been created using elements of the Liquid templating language. 

Liquid variable
    
A Liquid variable is an element of the Liquid templating language that can be used with LookML to create dynamic content. 

Look (_n._)
    
A Look is a single query table or visualization that is saved. Looks can be added to dashboards, scheduled, shared, and made public. Any changes made to a Look will be reflected in any dashboards that contain it. 

Looker-hosted
    
When Looker hosts your deployment, Looker manages all necessary IT functions that are related to the Looker application on your behalf, based on resource utilization and business requirements, greatly reducing the effort required to install, configure, and maintain the Looker application. To learn more about the comparative advantages of each hosting option, see the Choosing a hosting option for a Looker (original) instance documentation page.
All Looker (Google Cloud core) instances are Looker hosted.
_see also_ **customer-hosted** 

Looker API
    
The Looker API is a secure, "RESTful" application programming interface for managing your Looker instance and fetching data through the Looker data platform. You can write applications or automation scripts to provision new Looker user accounts, run queries, schedule data deliveries, etc. Just about anything you can do in the Looker application you can do through the Looker API. 

Looker Cloud
    
**Looker Cloud** means the product is installed and provisioned to a customer on a web-connected platform that is run in a third-party hosting facility designated by Looker. For more information, see the **Cloud Security Architecture** section of Looker's security webpage. 

Looker connector
    
The **Looker connector** is an integration between Looker and Looker Studio that allows you to access data from your Looker Explores within Looker Studio by adding an Explore as a data source in a Looker Studio report. 

Looker Data Dictionary
    
The Looker Data Dictionary is an extension — a web application built using Looker components — developed using the Looker extension framework and deployed through the Looker Marketplace. The Looker Data Dictionary extension provides a dedicated, centralized interface for searching through all Looker fields and descriptions in an Explore. To use the Looker Data Dictionary, Looker admins must enable the Extension Framework and Marketplace features.
_see also_ **extension,** **Looker extension framework** 

Looker expression
    
Table calculations, custom fields, and custom filters rely on Looker expressions (Lexp) to perform calculations. A Looker expression is built from a combination of functions, operators, and fields, and possibly constants or variables. 

Looker extension framework
    
The Looker extension framework is a development framework that significantly reduces the effort and complexity of building custom JavaScript data applications and tools. To use the Looker extension framework, Looker admins must enable the Extension Framework feature.
_see also_ **extension** 

Looker (Google Cloud core)
    
Looker (Google Cloud core) instances are Looker instances with deeper Google Cloud integration, including the ability to provision and administer instances from the Google Cloud console. 

Looker Marketplace
    
The Looker Marketplace is a central location for finding, deploying, and managing many types of Looker content, such as Looker Blocks (or "Models"), applications (or "extensions"), and visualizations (or "Plug-ins"). The Looker Marketplace can be accessed directly from a Looker instance or from `marketplace.looker.com`. The `marketplace.looker.com` director also lists the actions (or integrations) that are available from the Looker Action Hub. 

Looker (original)
    
Looker (original) instances are Looker instances that are not provisioned by the Google Cloud console, in contrast with Looker (Google Cloud core) instances. Usually, these instances are referred to simply as _Looker_ instances.  

LookML
    
LookML is a language for describing dimensions, aggregates, calculations and data relationships in a SQL database. The Looker app uses a model written in LookML to construct SQL queries against a particular database. 

LookML-based derived table
    
More often referred to as native derived tables, a LookML-based derived table is a derived table whose query is defined in LookML terms, referring to LookML dimensions and measures in your model. Native derived tables can be temporary or persistent.
_see also_ **derived table**, **persistent native derived table**, **temporary derived table** 

LookML dashboard
    
A LookML dashboard is written entirely using LookML (as opposed to a user-defined dashboard, which is created by using the visualization editor).
_see also_ **user-defined dashboard** 

LookML Diagram
    
The LookML Diagram is an entity relationship diagram of a LookML model that visually depicts relationships between its LookML objects. It is an extension — a web application built using Looker components — developed using the Looker extension framework and deployed through the Looker Marketplace.
_see also_ **extension**, **Looker extension framework**, **Looker Marketplace**, **LookML object** 

LookML object
    
LookML objects are the models, Explores, views, and fields that have been defined, in LookML, in a project, including files imported from another project. You can view LookML object relationships in the object browser or the LookML Diagram extension.
## M 

manifest, manifest file
    
A manifest (or project manifest) file is where you set project-level settings, such as those for specifying other projects to import into the current project, defining LookML constants, specifying model localization settings, and adding extensions and custom visualizations to your project. 

Markdown tile
    
A type of dashboard text tile that lets you use some HTML and a subset of the Markdown markup language to format the tile. 

Marketplace
    
see **Looker Marketplace** 

materialized view
    
A materialized view is a type of persistent derived table (PDT) that leverages your database's persistence functionality. This functionality is available for database dialects that support materialized views. Depending on your dialect, a materialized view can consume large resources, so it is important that you understand your dialect's implementation of materialized views. 

measure
    
A measure is a field in an Explore that represents measurable information about your data, such as sums, counts, and so forth. A measure is declared in a view file and can be of an aggregate or non-aggregate type. 

Merged Results
    
The Merged Results feature lets you combine data from different Explores (even from different models, projects, or connections). Using the Merged Results feature, you can create a query from an Explore, then add queries from other Explores to display the merged results in a single table. The Merged Results feature performs similarly to a left join in SQL: it's as if the added query is being left-joined into the primary query. 

metadata, IDE metadata
    
The metadata panel in the Looker IDE shows contextually relevant information for a LookML object. For example, if your cursor is on a `view` parameter in the IDE, the metadata panel will show you which Explores have that view joined in and other views that are extensions of that view. 

model
    
A model is the semantic layer in Looker that controls logic and gates data access for users. This is created by developers as a model file within the LookML project, and contains information about which tables to use and how they should be joined together. Multiple models can exist for the same database connection in a single LookML project, and each model can expose different data to different users.  

model file
    
Inside a LookML project, a model file specifies a single database connection, the set of Explores that use that connection, and the Explores themselves, as well as how they should be joined together. 

model set
    
A model set defines what data and LookML fields a user or group can see. An admin can select a combination of LookML models to which a user or group should have access. It must be used as part of a role to have any effect.
_see also_ **role**
## N 

native derived table
    
Sometimes referred to as LookML-based derived tables, native derived tables are derived tables that have queries defined in LookML terms, referring to LookML dimensions and measures in your model. Native derived tables can be temporary or persistent.
_see also_ **derived table**, **persistent native derived table**, **temporary derived table** 

northbound traffic
    
In networking, northbound traffic is traffic from a lower-level network component to a higher-level network component. In the context of Looker (Google Cloud core), northbound traffic is, for example, traffic from a client to a Looker (Google Cloud core) instance that allows users to access a Looker (Google Cloud core) instance.
## O 

Object browser
    
The object browser panel in the Looker IDE lets users view all the objects in a project in one place, along with the hierarchical relationships between them. 

Object
    
_see_ **LookML object**
## P 

parameter
     A parameter defines or modifies LookML elements such as models, views, Explores, and fields. See the LookML quick reference for a list of all available parameters.  

permission
    
Admins can manage permissions to determine which users and groups can access content, data, and features. Permissions can be model-specific or instance-wide. Permission sets must be used as part of a role to have any effect. 

permission set
    
Permission sets are combined with model sets in a role.
_see also_ **role** 

persistent derived table
    
A persistent derived table (PDT) is a derived table that is stored in the scratch schema of a database and can be regenerated on a schedule of your choosing. It can be referenced in a query without running the underlying SQL each time it is called. A PDT can be a native derived table or a SQL-based derived table.
_see also_ **derived table** 

persistent native derived table
    
A persistent native derived table is a LookML-based derived table that is persistent, meaning it is stored in the scratch schema of a database and can be regenerated on a schedule of your choosing. It can be referenced in a query without running the underlying SQL each time it is called. 
_see also_ **derived table**, **native derived table** 

persistent SQL-based derived table
    
A persistent SQL-based derived table is a SQL-based derived table that is persistent, meaning it is stored in the scratch schema of a database and can be regenerated on a schedule of your choosing. It can be referenced in a query without running the underlying SQL each time it is called. 
_see also_ **derived table**, **SQL-based derived table** 

primary key
    
The primary key is the dimension that has exactly one unique value for each row of data. When data tables are joined together in a one-to-many relationship, the primary key must be defined correctly in order to avoid a fanout. 

primary query
    
A primary query is a single query created from a single Explore. When working with merged results, the primary query is a similar concept to the primary ID when joining multiple tables in SQL. 

Production Mode
    
In Production Mode, changes that have been made in Development Mode (but not pushed to production) are not yet reflected in the data model shared by all users. In Production Mode, LookML files are treated as read-only. A developer can enter Development Mode to make changes to LookML files and push those changes for others to see in Production. 

project, LookML project
    
In Looker, a project is a set of related models and other files (like Explores, views, and LookML dashboards) that you will use to define your data model. In general, a project corresponds to a single Git repository.
## Q 

Query Time Zone
    
Query Time Zone is an admin setting for the time zone in which to show dates and times when querying.
_see also_ **Database Time Zone**, **time zone settings**
## R 

report
    
A [Looker report](/looker/docs/studio-in-looker) is a type of Looker content with which you can visualize and analyze data. Unlike a dashboard, a report requires no underlying modeling. You can share reports with other people and let them just view the data, or give them edit access so they can change the report structure. Reports can consist of multiple pages, charts, and other components, such as controls, text areas, shapes, and images. A Looker admin can enable access to reports by turning on **Enable reports** in the **Reports** section of the **Admin** panel. 

role
    
A role defines the privileges that a user or group will have for a specific set of models in Looker. Create a role by combining one model set with one permission set.
_see also_ **model set**, **permission set**
## S 

scratch schema
    
A scratch schema is a schema in the underlying database that is designated to store Looker PDTs.
_see also_ **persistent derived table** 

Slug
    
A slug is a securely generated random string that takes the place of the content ID value in a URL. For example, this URL points to a dashboard: `https://docserver.cloud.looker.com/dashboards/CQ1fu99Z9Y1ggq2wcHDfMm`. In this example, the string `CQ1fu99Z9Y1ggq2wcHDfMm` is the slug. To view a dashboard slug, select **Get link** from the dashboard's three-dot menu. To view an Explore slug, select **Share** from the Explore action gear menu. You can then view the slug in — or copy the slug from — the **Short URL** field. 

southbound traffic
    
In networking, southbound traffic is traffic from a higher-level network component to a lower-level network component. In the context of Looker (Google Cloud core), southbound traffic is, for example, traffic from a Looker (Google Cloud core) instance to a backend target service, such as a database. 

Space
    
A Space is a folder where dashboards, Looks, and other Spaces (subspaces) are stored. Each user has a personal Space, and a Looker instance can also have a variety of shared Spaces. Access to content in Looker is allocated at the Space level. Spaces have been renamed **folders** as of Looker 6.20.
_see also_ **folder** 

SQL-based derived table
    
A SQL-based derived table is a derived table that has a query defined with a SQL query, referring to columns in your database. SQL-based derived tables can be temporary or persistent.
_see also_ **derived table**, **persistent SQL-based derived table**, **temporary derived table** 

SQL Runner
    
Accessible through the **Develop** menu or from an Explore (with the appropriate permissions), SQL Runner lets users run raw SQL against their allowed connections. SQL Runner can be used to perform database functions, create and add derived tables to projects, to leverage the `EXPLAIN` function, among other uses. 

Standard edition
    
A **Standard** edition is a Looker (Google Cloud core) edition type that is tailored for small teams and small or medium-sized businesses with up to 50 internal platform users. In addition to many existing Looker features, the **Standard** edition brings new functionality including Google Cloud identity access management and simplified BigQuery connectivity. 

subfolder
    
A subfolder is a folder that is stored within another folder. Folders were called **Spaces** prior to Looker 6.20. 

subparameter
    
A subparameter is a parameter that can be used under another (parent) parameter in order to further define, refine, or specify how that parameter functions. 

subspace
    
A subspace is a Space that is stored within another Space. Spaces have been renamed **folders** as of Looker 6.20. 

substitution operator
    
The dollar sign () is a substitution operator in Looker, and helps to make LookML code more reusable and modular. You can use this syntax to reference LookML objects that have already been defined. 

symmetric aggregates
    
Symmetric aggregates are functions in Looker that successfully return results for aggregations or measures. They help define the correct relationship between tables, thereby avoiding fanouts. 

system time zone
    
The system time zone is the time zone for which the server running Looker is configured.
_see also_ **time zone settings**
## T 

table calculation
    
Table calculations are similar to spreadsheet formulas and are performed on the results of a query, after the query has executed. 

temporary derived table
    
A temporary derived table — sometimes called an "ephemeral" derived table — is temporary and not written to your database. A temporary derived table can be either a LookML-based (native) derived table, or an  SQL-based derived table.
_see also_ **derived table**, **native derived table**, **SQL-based derived table** 

Text tile
    
A type of dashboard text tile that provides a visual editing experience. 

theme
    
Themes are a way to customize the appearance of your embedded Looker dashboards and Explores. You can use themes to customize font family, text color, background color, tile color, and other visual elements. 

tile
    
Tiles are visualizations that are added to a dashboard from an Explore or a Look. Tiles can be query-based or Look-linked. Query tiles differ from Look-linked tiles because they are stored only on dashboards. 

time zone settings
    
Looker admins and users have a variety of options to convert and display time-based data in specific time zones.
_see also_ **Application Time Zone**, **Database Time Zone**, **Query Time Zone**, **system time zone**, **User Specific Time Zones** 

transpile
    
The process of taking source code written in one language and transforming it into another language that has a similar level of abstraction. An example is TypeScript to JavaScript. 

trigger-persisted table
    
A trigger-persisted table is a derived table that has a trigger as a persistence strategy, using either the `datagroup_trigger` parameter, the `sql_trigger_value` parameter, or the `interval_trigger` parameter. With trigger-persisted tables, Looker maintains the PDT in the database until the PDT is triggered for rebuild. When the PDT is triggered, Looker rebuilds the PDT to replace the previous version. See the Derived tables in Looker documentation page for more information.
## U 

Unsubscribe (for alerts and scheduled content deliveries)
    
By unsubscribing, users can choose to stop receiving scheduled content deliveries and alert notifications. The consequences for unsubscribing differ depending on how the delivery is set up.
For scheduled email deliveries and alert notifications that are sent by email, any user who unsubscribes on behalf of a group email distribution will terminate email deliveries and alert notifications for all users in that group. When recipients are listed separately, when the last remaining recipient unsubscribes from a scheduled content delivery, the schedule is deleted from Looker and deliveries will no longer be sent.
When any user unsubscribes to alert notifications to Slack through either the Slack or Slack Attachment (API Token) integration, the alert is disabled in Looker and notifications will no longer be sent. 

User Specific Time Zones
    
User Specific Time Zones is an admin option that, when enabled, lets users choose their own time zones. Queries will be created with the time zones of the users who created them.
_see also_ **Application Time Zone**, **Database Time Zone**, **Query Time Zone**, **time zone settings** 

user-defined dashboard, UDD
    
User-defined dashboards are created by adding content through Looker's user interface, rather than using LookML. This is the most common type of dashboard.
## V 

view
    
In Looker, a view can represent an underlying database table or a derived table. Views are the building blocks for Explores, which make the information in a view available for querying with the field picker in the Explore UI. By convention, a view is defined in a view file. 

view file
    
A view file is where you define the dimensions, measures, and other fields that are used in your LookML model.
_see also_ **model** 

visual drilling
    
Visual drilling is not supported by dashboards. To enable visual drilling, LookML developers customize a drill visualization using the `link` parameter. Look or Explore viewers can select whether to view the custom visualization or a data table by clicking buttons at the top of the drill window.
_see also_ **model** 

visualization
    
Looker offers several types of visualizations: the built-in chart visualizations that appear in Looker content and the custom visualizations that can be created with a `visualization` parameter or from the **Visualizations** page in the **Admin** section of the Looker instance, or installed as visualizations or "plug-ins" from the Looker Marketplace. 

visualization components
    
Visualization components are React-based, prebuilt pieces of Looker's application that can be used to render and modify visualizations for custom-built data applications and customized embedded Looker dashboards.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


