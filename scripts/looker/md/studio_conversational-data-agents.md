# Conversational Analytics: Data agents  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/conversational-data-agents

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Create and edit data agents
    * Write agent instructions
    * Edit an existing data agent
  * Start a conversation with an agent
  * Share data agents
    * Share a data agent
    * Revoke access to a data agent
  * Delete a data agent




Was this helpful?
Send feedback 
#  Conversational Analytics: Data agents
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Create and edit data agents
    * Write agent instructions
    * Edit an existing data agent
  * Start a conversation with an agent
  * Share data agents
    * Share a data agent
    * Revoke access to a data agent
  * Delete a data agent


Data agents let you curate the Conversational Analytics experience for your data. With agents, you can provide Conversational Analytics with context and instructions to enable it to answer questions more effectively for specific use cases. Agents empower analysts to map business terms to specific fields, specify the best fields for filtering, and define custom calculations.
This page guides you through the following processes:
  * Create and edit data agents
  * Start a conversation with an agent
  * Share data agents and conversations


Learn how and when Gemini for Google Cloud uses your data.
## Create and edit data agents
To create a new data agent, follow these steps:
  1. Navigate to Conversational Analytics in Looker Studio or Looker.
  2. Select **+ Create agent** in the **+ Create Conversation** section. Or, in the left navigation panel, select **Manage agents** , and then select **+ Create agent**.
  3. On the **New agent** page, provide the following information about your data agent.
     * **Agent Name** : Enter a name for the agent. The name should be unique and descriptive.
     * **Description** : Briefly describe what this agent can do and the data that it uses. Users will see this description when they select the agent to start a conversation or when you share the agent with them, so make sure it clearly explains the agent's purpose and how it can be helpful.
     * **Data** : Connect to a new or existing data source by following these steps:
       1. In the **Data** field, click **Select data**.
       2. In the **Select data for Agent** window, under **Name** , click the name of a data source.
       3. Click **Select** to add the selected data source to the data agent.
Alternatively, you can select **Connect to data** in the **Select data for agent** window to create a new data source.
  4. **Instructions** : Provide context to help Conversational Analytics understand how to interact with your data and provide accurate and relevant responses. For examples of the types of context that you can provide, see Writing agent instructions.
  5. To save your new data agent, click **Save**.


After you save the data agent, you can share the agent with other users and start a conversation with the agent.
### Write agent instructions
When you create a data agent, you can provide the following types of context in the **Instructions** field:
  * **Synonyms** : Alternative terms for key fields
  * **Key fields** : The most important fields for analysis
  * **Excluded fields** : Fields that the data agent should avoid
  * **Filtering and grouping** : Fields that the agent should use to filter and group data


Here are some sample instructions to adjust and test with your agent:
  * Unless stated otherwise, always filter the data on `Order Items Created Year = 2024`
  * We consider "loyal" customers to be those with `Order Items Count > 5`
  * If someone says anything about "Location," that means User City
  * If the question mentions "Seniors", those are users with `User Age > 65`
  * If a question is about Revenue, use Total Sales
  * When someone says "by product", unless they specifically say "name", group by `product category`
  * "Successful" orders means that Order Items status = "Complete"
  * Whenever there is a question of a timeline, or over time, always use `Order Item Created Date` as the field to group by


### Test an agent
When you're creating or editing an agent, the agent details page includes the **Preview your agent** pane. You can test agent settings and instructions by starting a conversation with the agent.
### Edit an existing data agent
To edit an existing data agent, follow these steps:
  1. In Conversational Analytics, click **Manage agents**.
  2. On the **Manage agents** page, select the data agent that you want to edit.
  3. Update the details about the agent as needed. You can modify the details that you specified when you created the agent, including the **Agent Name** , **Description** , and **Instructions** fields.
  4. To save your changes, click **Update**.


## Start a conversation with an agent
You can start a conversation with a data agent that you created or that another user has shared with you. To start a conversation with an agent, follow these steps:
  1. In the left navigation panel, click **+ Create conversation**.
  2. In the **Agents** tab, select the agent that you want to start a conversation with.
  3. Type in your question and press return (Mac) or Enter (PC) to start the conversation.


You can return to the conversation from the **schedule Recent** section.
## Share data agents
Only the owner of a data agent can share an agent. The recipients of a shared data agent can see the agent's description but cannot edit the agent. Once an agent is created, it may take a few minutes for it to become shareable.
### Share a data agent
To share a data agent, follow these steps:
  1. In Conversational Analytics, click **Manage agents**.
  2. Hold your cursor over the data agent and select person_add **Share data agent** , or select **person_add Share** while editing an existing data agent.
  3. You can invite specific people or Google Groups to share the agent. You can also share more broadly by turning on link sharing for a report.
  4. Once you have added the individuals or groups to the **People with Access** section, click **Done**.


The recipient will receive an email with a link to the data agent. When a user selects Create conversation, agents that have been shared with them will appear under **Agents**. After an agent is initially shared, users won't be able to view the instructions for that agent. Include any relevant information in the agent description.
### Revoke access to a data agent
To revoke access to an agent, remove the person or group from the list of **People with access** in the **Share** menu of the agent. If the removed user has an ongoing conversation, they will still have access for a minute or two while the changes propagate.
If a user tries to ask more questions once access to an agent is removed, then that user will see the message `The agent in this conversation may not be shared with you, or may have been deleted. You can view any past conversations with the agent, but can't ask new questions.`
## Delete a data agent
To delete a data agent, follow these steps:
  1. In Conversational Analytics, click **Manage agents**.
  2. On the **Manage agents** page, hold your cursor over the data agent that you want to delete.
  3. Click more_vert **More options**.
  4. Select delete **Delete**.
  5. In the **Move to trash** window, click **Move to trash** to delete the data agent.


Agents that are moved to the trash will be permanently deleted after 30 days. You can permanently delete a data agent manually, or you can restore a data agent from the trash before it is permanently deleted.
#### Permanently delete a data agent
To permanently delete a data agent, follow these steps:
  1. Navigate to Conversational Analytics.
  2. In the left navigation panel, expand the **Trash** section.
  3. Select the data agent that you want to delete.
  4. In the **Are you sure?** window, click **Delete forever**.


#### Restore a data agent from the trash
To restore a data agent from the trash, follow these steps:
  1. Navigate to Conversational Analytics.
  2. In the left navigation panel, expand the **Trash** section.
  3. Select the data agent that you want to restore.
  4. In the **Are you sure?** window, click **Restore**.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


