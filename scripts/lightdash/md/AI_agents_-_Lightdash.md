# AI agents - Lightdash

**Source:** https://docs.lightdash.com/guides/ai-agents

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
AI agents
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
    * Interacting with your dashboards
    * Using the Slack integration
    * Scheduled deliveries
    * Chart Version History
    * Formatting your fields
    * How to promote content
    * Table calculation SQL templates
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Creating your first AI agent
  * What it can do
  * Core capabilities
  * Using AI agents in Slack
  * Best practices
  * Think specialized, not general
  * Document your data thoroughly
  * Using AI hints
  * Writing effective instructions
  * What to include
  * What to avoid
  * Set up multiple agents
  * Limiting access to specific explores/fields
  * Adding tags at the model level
  * Adding tags to individual metrics & dimensions


## Cloud Pro
## Cloud Enterprise
AI agents transform the way you interact with your data by allowing you to ask questions in natural language and get answers back. Whether you’re exploring data in Lightdash or collaborating with your team in Slack, AI agents make data analysis as simple as having a conversation. AI agents automatically select the most relevant data models and metrics to answer your questions, build and execute queries with appropriate dimensions, metrics, and filters, and present results in the most insightful format.
AI Agents in the Lightdash app will follow row-level, column-level, and table-level data access based on user attributes.In Slack, the AI will have the user attributes of the user who set up the agent. We plan to respect user attributes based on Slack user email in the future, reach out if you need that feature!
##  Get started
Getting started with AI agents is simple - you can begin using them right away on any project in your Lightdash instance.
###  Creating your first AI agent
  1. **Find the “Ask AI” button** in your project - this will be your entry point to AI agents
  2. **Create a new agent** (only admins and developers can create new AI agents)
  3. **Configure your agent:**
     * **Name and image** - Give your agent a memorable name and visual identity
     * **Instructions (optional)** - Provide context about your models, tables, or specific use cases to help the AI give more relevant responses
     * **Tags (optional)** - Use tags to control which metrics and dimensions the agent can access

Once set up, you can start asking questions immediately! Try asking “What kind of data can you access?” to get started.
##  What it can do
###  Core capabilities
AI agents in Lightdash allow you to:
  * **Ask questions in natural language** - Simply type what you want to know about your data, like “What’s our total revenue by region?” or “Show me user growth over the last 6 months”
  * **Get instant visualizations** - Receive bar charts, time series, and tables automatically generated based on your questions
  * **Explore interactively** - Follow up with additional questions, drill down into specific data points, or request different chart types
  * **Maintain conversation context** - AI agents remember your conversation history, so you can build on previous questions and refine your analysis
  * **Provide text-only responses** - Get answers in natural language when visualizations aren’t needed
  * **Guide you to the right data** - Direct you to the most relevant explores or tables for your questions


###  Using AI agents in Slack
Connect your AI agents to Slack for collaborative data analysis and team-wide insights sharing, here’s how:
  1. Select or create an AI agent in your Lightdash instance
  2. Add the Slack integration in your organization settings
  3. Under ‘Integrations’, add the channel you want to use 
  4. Tag your **Slack App** in the channel you want to use
  5. Start asking questions like “What kind of data can you access?” or “Show me total order amount over time”
  6. Get instant results directly in Slack

You can also summon the bot on a thread to continue the conversation. In order for the bot to be able to respond, you need enable this context sharing in your Lightdash Integrations settings.
####  Demo
Watch this comprehensive demo to see AI agents in action:
##  Best practices
To get the most accurate and useful answers from your AI agents, follow these best practices for preparing your data and configuring your agents.
###  Think specialized, not general
Think of AI agents as your specialized analysts - each one can be configured to focus on specific areas of your business. For example, you might create a “Marketing Assistant” that only has access to marketing data like campaign performance, lead generation, and customer acquisition metrics. This focused approach ensures more accurate, relevant responses and prevents sensitive data from being accessible to the wrong teams. To find out more about how to configure specific access, see Limiting access to specific explores/fields.
###  Document your data thoroughly
Good documentation is crucial for AI to understand your data models and provide meaningful insights. The quality of the results depend on the quality of your metadata and documentation.
  * **Write clear, descriptive names** for metrics and dimensions
  * **Add detailed descriptions** to all metrics and dimensions explaining what they represent
  * **Include example questions** in descriptions that AI could answer with the metric
  * **Use AI hints** to provide additional context specifically for AI agents

Remember: If your colleague wouldn’t understand your documentation, neither will the AI agent. The more context you provide, the better the AI can interpret and analyze your data.
####  Using AI hints
AI hints are specialized metadata fields that provide additional context specifically for AI agents. These hints help the AI better understand your data models, business logic, and how to interpret your metrics and dimensions.
AI hints are internal metadata used only by AI agents and are not displayed to users in the Lightdash interface. When both AI hints and descriptions are present, AI hints take precedence for AI agent prompts.
AI hints support both string and array of strings formats. The array format allows you to organize multiple distinct pieces of information as separate hints, making them easier to read and maintain. You can add AI hints at three levels: **Model-level hints** - Provide context about the entire table:
dbt 1.10+
dbt <=1.9
Copy
Ask AI
```
models:
name: customers
    config:
      meta:
        ai_hint: 
This is a customers table containing customer information and derived facts
Use this for customer demographics, behavior analysis, and segmentation

```

String format:
dbt 1.10+
dbt <=1.9
Copy
Ask AI
```
models:
name: customers
    config:
      meta:
        ai_hint: |
          This is a customers table containing customer information and derived facts.
          Use this for customer demographics, behavior analysis, and segmentation.

```

**Dimension-level hints** - Explain individual columns:
dbt 1.10+
dbt <=1.9
Copy
Ask AI
```
columns:
name: last_name
    config:
      meta:
        dimension:
          ai_hint: 
Customer's last name
Contains PII data - use for identification but be mindful of privacy

```

**Metric-level hints** - Clarify what metrics measure:
dbt 1.10+
dbt <=1.9
Copy
Ask AI
```
columns:
name: customer_id
    config:
      meta:
        metrics:
          unique_customer_count:
            type: count_distinct
            ai_hint: 
Unique customer count for business reporting
Use this for customer acquisition and retention analysis

```

###  Writing effective instructions
Think of your instructions as teaching your AI agent about your world. The better you explain your business context and preferences, the more useful and relevant your agent’s responses will be. Focus on four key areas: what your agent should know about your industry, your team’s goals and constraints, how you like data analyzed, and how results should be communicated.
####  What to include
  * **Industry terminology and key metrics** including acronyms your team uses regularly (e.g., “CPM means Cost Per Mille, not cost per mile” or “Our ARR calculations exclude one-time setup fees”)
  * **Communication style** for how results should be presented to your team (e.g., “Keep explanations simple for non-technical stakeholders” or “Always include actionable next steps”)
  * **Business constraints** like regulatory requirements or budget limitations that affect decision-making
  * **Analysis preferences** your team relies on (e.g., “Always compare month-over-month growth” or “Flag any churn rates above 5% as concerning”)
  * **Context for interpreting your data** (e.g., “Our Q4 always shows higher sales due to holiday promotions” or “Weekend traffic is typically 40% lower”)


**Good example - Sales Team Agent:** You analyze sales performance for our SaaS company. Focus on MRR, churn, and pipeline health. When MRR growth drops below 10% month-over-month, flag it as concerning. Present insights in simple terms that our sales managers can act on immediately. Always include trend explanations and next steps.
####  What to avoid
  * **Contradictory instructions** that create confusion about priorities
  * **Overly complex rules** that are hard to follow consistently
  * **Vague guidance** like “be helpful” without explaining what that means for your situation
  * **Too many different focus areas** in one agent, remember to keep each agent focused, there are no limits on the number of agents you can create!
  * **Restating basic features** , don’t tell the AI to “create charts” since it already does that


**Poor example - Too vague:** Be helpful and analyze data well. Create good charts and explain things clearly.
##  Set up multiple agents
You can create multiple AI agents, each configured for different tasks, tones, languages, or teams. Each agent can have access to different datasets to focus results and give more accurate answers.
###  Limiting access to specific explores/fields
For each AI agent, you can configure which fields are used to answer questions using the tags you’ve defined in your YAML files. You can add one or many tags - fields with **any** of the tags in the list will be considered by the AI agent. Use tags to control which metrics and dimensions each AI agent can access. This helps focus the AI on the most relevant data for analysis and ensures agents only work with appropriate datasets. You can add tags at the model level to give access to entire explores, or at the individual metric and dimension level for more granular control.
####  Adding tags at the model level
Tag entire models to give your AI agent access to all metrics and dimensions within that explore:
dbt 1.10+
dbt <=1.9
Copy
Ask AI
```
models:
name: marketing_campaigns
    config:
      meta:
        tags: ['marketing', 'ai'#    <--------- tagging the entire model
    columns:
name: campaign_name
        config:
          meta:
            dimension:
              type: string
name: impressions
        config:
          meta:
            metrics:
              total_impressions:
                type: sum

```

####  Adding tags to individual metrics & dimensions
For more granular control, tag specific metrics and dimensions:
dbt 1.10+
dbt <=1.9
Copy
Ask AI
```
models:
name: orders
    columns:
name: status
        config:
          meta:
            dimension:
              tags: ['ai', 'sales'# <--------- tagging the dimension
name: location
        config:
          meta:
            dimension:
              tags: ['ai', 'operations'# <--------- taggint the dimension
name: amount
        description: Total amount of the order
        config:
          meta:
            metrics:
              total_order_amount:
                type: sum
                format: usd
                round: 2
                tags: ['ai', 'finance'# <--------- tagging the metric

```

##  FAQs
  1. Does Lightdash store the query data?

Lightdash only stores simple one-line answers so you can look back at your conversation history. We also save the basic query info to recreate these when needed. The actual data and detailed results stays in your warehouse and gets pulled fresh when the results are revisited.
  1. Why can’t I set multiple Agents for the same Slack channel?

Since you have to mention the Slack App for your organization, and to avoid unexpected results, we don’t allow multiple agents for the same slack channel. To align with best practices, we recommend one slack channel per project, so you prompt with confidence.
Creating DashboardsSpotlight
Assistant
Responses are generated using AI and may contain mistakes.


