# Conversational Analytics in Looker  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/conversational-analytics-looker

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Supported data sources
  * Before you begin
  * Navigate to Conversational Analytics
  * Start a conversation
  * Ask questions
    * Ask questions about a data source
    * Manage queries within a conversation
  * Understand query results and calculations
    * Determine how an answer was calculated
    * Get additional insights
  * Manage conversations
    * Name a conversation
    * Delete a conversation
    * Restore or permanently delete a conversation
  * Connect to data
    * Best practices for setting up a data source
    * Connect to Looker data
  * Additional resources




Was this helpful?
Send feedback 
#  Conversational Analytics in Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Supported data sources
  * Before you begin
  * Navigate to Conversational Analytics
  * Start a conversation
  * Ask questions
    * Ask questions about a data source
    * Manage queries within a conversation
  * Understand query results and calculations
    * Determine how an answer was calculated
    * Get additional insights
  * Manage conversations
    * Name a conversation
    * Delete a conversation
    * Restore or permanently delete a conversation
  * Connect to data
    * Best practices for setting up a data source
    * Connect to Looker data
  * Additional resources


Conversational Analytics is a chat with your data feature powered by Gemini for Google Cloud. Conversational Analytics empowers users with no expertise in business intelligence to ask data-related questions in regular, natural (conversational) language, and go beyond static dashboards. Conversational Analytics is available in Looker (Google Cloud core) and Looker (original) instances.
Learn how and when Gemini for Google Cloud uses your data.
## Supported data sources
The following data sources are supported for using Conversational Analytics with Looker Studio in Looker:
  * Looker Explores


## Before you begin
To use Conversational Analytics within a Looker instance, you and your Looker instance must meet the following requirements:
  1. A Looker admin must enable Gemini in Looker for the Looker instance. To learn more about how to manage Gemini in Looker enablement, see the documentation for Looker (original) or for Looker (Google Cloud core). 
     * The Trusted Tester capabilities must be enabled to use Conversational Analytics during the preview period.
  2. A Looker admin must grant you a role that contains the `gemini_in_looker` permission in the Looker instance. You must also have a role that contains the `access_data` permission for the model that you are querying.


We recommend that customers participating in Lookers Extended support release program update to Looker 25.6 or later to use Conversational Analytics.
For known limitations and a list of key features, see the Conversational Analytics landing page.
## Navigate to Conversational Analytics
You can access Conversational Analytics in the following ways:
  * From the main navigation menu, select **Conversations**.
  * From the **Create** menu, select **Conversation**.
  * From a Looker Explore, select **Start a conversation**.


## Start a conversation
Sets of questions that you ask about a dataset are organized by conversation. Splitting work into multiple conversations can be useful for organizing lines of inquiry. To create a new conversation, follow these steps:
  1. Navigate to Conversational Analytics.
  2. Click **+ Create conversation**.
  3. Select the source of your conversation:
     * **Explores** : To start a conversation based on a Looker Explore, select the **Explore** panel. The project name is listed beside the Explore name.
     * **Agents** : Data agents are customized with context and instructions that are specific to your data. To start a conversation with an existing data agent, select **Agents** , and then select a data agent. To create a new data agent, select **+ Create agent**.
  4. To start the conversation, enter your question and press return (Mac) or Enter (PC).


You can return to the conversation from the schedule **Recent** section.
## Ask questions
You can ask questions to get insights from your data. When you're beginning a new conversation, Conversational Analytics suggests some starting questions to ask.
### Ask questions about a data source
Once you have created a conversation, you can ask questions about the data in the send_spark **Ask a question** field within the conversation.
The questions don't need to be in a specific format or use a specific syntax. However, they do need to relate to the data source that you've selected. Conversational Analytics may rephrase your question after you've written a query, and the rephrased question will be displayed in the conversation window following your original question. For example, Conversational Analytics might rephrase the question "What is the mean of user ages?" to "What is the average user age?"
Conversational Analytics will take previous questions and answers into account as you continue the conversation. You can take previous answers and build on them by further refining results or changing the visualization type.
For more guidance on creating questions, see Limitations on questions.
### Manage queries within a conversation
When you converse with data, you can manage the conversation by stopping an active query response while it is running or by deleting the most recent question and its response.
#### Stop a query response
To stop running a query after you've sent a message, click stop **Stop response**. Conversational Analytics stops running the query and displays the following message: `The query was cancelled.`
#### Delete the most recent question
To delete the most recent question and its response, follow these steps:
  1. Hold your cursor over the most recent question, and then click delete **Delete message**.
  2. In the **Permanently delete message?** dialog, click **Delete** to permanently delete the question and its response.


## Understand query results and calculations
When you ask questions about your data in Conversational Analytics, the response might include a visualization, a data table, or other details, depending on your specific query and the connected data.
In addition to this query response, Conversational Analytics provides the following options for understanding query results and calculations:
  * Details about how the answer was calculated
  * If available, the option to view additional insights about the response


### Determine how an answer was calculated
To see how Conversational Analytics arrived at an answer or created a visualization, click keyboard_arrow_down **How was this calculated?** within the query results.
When you click **How was this calculated?** , Conversational Analytics displays a **Text** section. The **Text** section provides a plain text explanation of the steps that were taken by Conversational Analytics to arrive at the given answer. This explanation includes the raw field names that were used, the calculations that were done, the filters that were applied, the sort order, and other details.
### Get additional insights
When Conversational Analytics is able to provide additional data insights about a response, an **Insights** keyboard_arrow_down button will appear below the response. Click **Insights** keyboard_arrow_down to see additional information about your query. **Insights** only analyzes the data that was returned by your prompt and won't run additional queries to fetch additional data. **Insights** can be a useful source for ideas for follow-up questions to continue the conversation.
The following is an example of some insights that might be returned by the prompt "How many users are in each state?":
  * A general summary of high and low data volume areas. For example: 
    * "California, Texas, and Ohio are key states for business operations based on the data provided."
    * "England and specific regions in China, namely Anhui and Guangdong, show significant business activity."
    * "Some states, including Mie, Akita, and Iwate, have minimal presence based on the data."
  * An assessment of the variability of the dataset. For example, "The data indicates varying operational scales across different locations."


## Manage conversations
You can change the names of conversations, delete conversations, or restore them from the trash folder.
### Name a conversation
Conversational Analytics automatically generates a conversation title that is based on your first question and response. To change the generated name, follow these steps:
  1. Click the title at the top of the conversation page.
  2. Enter a new conversation name.
  3. To save your changes, click elsewhere on the page, or press return (Mac) or Enter (PC).


### Delete a conversation
To move a conversation to the trash, open the conversation and click delete **Move to trash**.
### Restore or permanently delete a conversation
To restore or permanently delete a conversation from the trash, follow these steps:
  1. Within Conversational Analytics, select delete **Trash** in the left navigation panel to view the list of conversations that have been moved to the trash.
  2. In the **Trash** section, click the name of the conversation that you want to restore or permanently delete.
  3. In the **Are you sure?** dialog, select one of the following options: 
     * **Cancel** : Cancels the action.
     * **Restore** : Restores the conversation. The conversation can be accessed from the schedule **Recent** section of the left navigation menu within Conversational Analytics.
     * **Delete forever** : Permanently deletes the conversation.


## Connect to data
You can connect to new Looker Explores within your instance to use with Conversational Analytics.
### Best practices for setting up a data source
Setting up a data source in the ideal manner can help Conversational Analytics provide the most helpful answers. Consider following these best practices when creating a data source:
  * Only include fields in the data source that should be used for analysis by end users.
  * Give each field a clear and concise name.
  * Give each field a clear description, including sample values where relevant. These field descriptions are included in the prompt that is sent to Conversational Analytics, and they can be helpful for providing context. Sample values are especially helpful for string fields.


See Best practices for rolling out Conversational Analytics with Looker for strategies and best practices to help Looker administrators and LookML developers successfully configure, deploy, and optimize Conversational Analytics.
### Connect to Looker data
You start a conversation directly with a Looker Explore or with a data agent that is built with a Looker Explore.
#### Before you begin
To use a Looker Explore with Conversational Analytics, the Looker connector must be enabled for the Looker instance that you are connecting to within Conversational Analytics. To enable the Looker connector, your Looker instance must meet the prerequisites that are described in Connecting to Looker Studio.
#### Use a Looker Explore as a data source
Looker Explores appear in the list of available Explores on the **Chat with your data** page. To use a new Looker Explore as a data source in Conversational Analytics, follow these steps:
  1. In Conversational Analytics, on the **Chat with your data** page, select the **Explores** tab.
  2. Select an Explore from the list, or search for a specific Explore.
  3. Click **Connect** to start a conversation.


#### Converse with a Looker data source
Once you've connected to a Looker Explore, you can ask questions about your Looker data.
When you converse with your data, the collapsible storage **Data** panel shows the name of the Looker Explore that is being used by the conversation. The storage **Data** panel also provides the following options:
  * open_in_new **View fields** : View the Explore in a new browser window by clicking open_in_new **View fields**.
  * chat_spark **New conversation** : Start a new conversation with the Looker Explore that the current conversation is using.


#### Open in a Looker Explore
To open the query results as an Explore, click explore **Open in Explore** within the query results.
## Additional resources
  * **Conversational Analytics: Query your data in natural language** : The landing page for Conversational Analytics contains setup requirements, known limitations, supported question types, and more.
  * **Create and converse with data agents** : With data agents, you can customize the AI-powered data querying agent by providing context and instructions that are specific to your data, which helps Conversational Analytics generate more accurate and contextually relevant responses.
  * **Best practices for rolling out Conversational Analytics with Looker** : Strategies and best practices to help Looker administrators and LookML developers successfully configure, deploy, and optimize Conversational Analytics.
  * **Enable advanced analytics with the Code Interpreter** : The Code Interpreter within Conversational Analytics translates your natural language questions into Python code and executes that code. Compared to standard SQL-based queries, the Code Interpreter's use of Python enables more complex analysis and visualizations.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


