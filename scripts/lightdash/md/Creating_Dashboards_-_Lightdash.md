# Creating Dashboards - Lightdash

**Source:** https://docs.lightdash.com/get-started/exploring-data/dashboards

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Quickstart
Creating Dashboards
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
    * Exploring your content
    * Metrics and dimensions
    * Sharing with your team
    * Creating Dashboards
  * Guides
  * Reference
    * Creating Dashboards
    * Filters reference
    * Using custom fields


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
  * 1. Create a new empty dashboard
  * 2. Choose a chart to add to your dashboard
  * How to create a chart from within your dashboard.
  * How to add an existing chart to your dashboard.
  * 3. Add markdown or other content
  * Markdown tiles
  * 4. Save your dashboard
  * 5. Add filters to your dashboards
  * Leaving filters empty
  * Adding an empty-value filter
  * Marking a filter as required for the dashboard to run
  * 6. Add tabs to your dashboard
  * Editing and Removing
  * Embedding Dashboard Tabs
  * 7. Share your dashboard


Dashboards allow you to arrange multiple charts that are related to each other into a single view. Checkout this tutorial on how to create your first dashboard:
##  1. Create a new empty dashboard
On the nav bar, click “New” to create a new dashboard. Fill out the details of your new dashboard and hit ‘Create’. Once done, you will be redirected to your new Dashboard page: Next, you’ll want to add some tiles to your dashboard by clicking on the `add tile` button.
##  2. Choose a chart to add to your dashboard
You can either create a new chart from within your dashboard, or you can add an existing chart.
###  How to create a chart from within your dashboard.
Creating charts from within a dashboard helps to keep your spaces and projects clutter-free from charts that are used only once in a dashboard. Charts that are created from within your dashboard are exclusive to the dashboard. This means that they can’t be reused in other dashboards in your project. Click “Add tile” and then “New chart” to create a chart that is exclusive to the dashboard. You will be taken to the chart builder. Once you save the chart it will appear at the bottom of your dashboard. Note: These charts can’t be used in other dashboards and won’t be shown in the global search or in any space. If you want to make these charts reusable in other dashboards, you can detatch them from the dashboard and save them to a space so they’re permanent using the `move to space` option from the chart’s three-dot-menu.
###  How to add an existing chart to your dashboard.
You can add an existing chart to your dashboard by clicking “Add tile” and then “Saved chart”. Clicking any chart will add it at the bottom of your dashboard. You can resize charts by dragging the lower-right corner. You can position your chart by dragging the center of the chart.
##  3. Add markdown or other content
In addition to charts, you can also add markdown tiles or embedded Loom videos to explain the dashboard to people who will be using it.
###  Markdown tiles
These tiles are very flexible and allow you to enter text with headers, formatting, etc. You can even include code blocks and images within markdown tiles. The built-in editor provides most formatting you’ll need. One option that isn’t available in the editor is text centering. That can be achieved like this:
Copy
Ask AI
```
h2 style="text-align:center"This is my centered title</h2

```

Other HTML markdown tile options
There are a number of other inline HTML options available. Below are some examples - Copy and paste them into a markdown tile to check them out!
Copy
Ask AI
```
Check out this bbold</b word.
You can also do iitalics</i.
And even uunderline</u.
Or maybe you want to sstrikethrough</s.
Show code snippets like codeHello World!</code.
Or markhighlight</mark something important.
Add links like a href="https://docs.lightdash.com/"this!</a
Use subsubscript</sub or supsuperscript</sup
p style="color:red"Easily colour your text.</p
p style="font-size:20px"Or change the size.</p
p style="text-align:center"Center your text.</p
p style="text-align:right"Or align it to the right.</p
p style="text-align:justify"You can even justify a line of text if you are trying to communicate a point that is particularly long, perhaps something like this example sentence?</p
p style="word-spacing:5px"Change the word spacing. 👏</p
p style="font-style:italic;font-weight:bold;color:blue"
    Or combine a whole bunch of styles together.

h1We also support headings</h1
h2 style="color:red"Here's an H2 heading in red</h2
You can also include images and apply different alt options and styles. Here's one I centered earlier:
img src="https://placehold.co/300x200" alt="Centered Image" style="display:block;margin:0 auto" />

```

###  Loom videos
All you need to do for embedding Loom videos is click on the Loom video option and enter a URL and title for the tile.
##  4. Save your dashboard
When you’re happy with the layout, hit “Save”. You can also see all of the saved dashboards in your project by clicking on `Browse` —> `All Dashboards`.
##  5. Add filters to your dashboards
Now let’s add some filters to your dashboard. First, start by editing your dashboard by clicking on the `Edit dashboard` button. Click on the `Add filter` button to add a new filter to your dashboard by selecting a field and a value to filter by. Select a value to filter by and hit `Apply`. You can add as many filters as you like. Now that you’ve added a filter, you can see the filter applied to your dashboard. Hit `Save` to save your dashboard with the new filter.
###  Leaving filters empty
You might want to add an empty-value filter so that your dashboard viewers can choose their own value and explore the data based on their own criteria. Your dashboard viewers might also want to add their own filters to your dashboard.
####  Adding an empty-value filter
Just edit your filter and ensure that you don’t provide a default value.
####  Marking a filter as required for the dashboard to run
You can mark a filter as required for the dashboard to run. This means that the dashboard will not run unless a value is selected for the filter. Just edit your filter and check the “Require value for dashboard to run” checkbox. Until viewers have set a value for the filter, the dashboard will not run. To learn more about adding filters to your dashboards, check out our guide on using filters.
##  6. Add tabs to your dashboard
As your dashboard grows you may find it supporting different teams and varied use-cases or domains. Lets add tabs to your dashboard for better organization! While editing, click “Add tile” and then “Add tab”. Give your new tab a unique name. Once created, you can add content to your tab just like any other dashboard. You now have a new canvas to add content to your dashboard.
###  Editing and Removing
To edit a tab, click on the edit icon to the right of your tab name while in dashboard edit mode. You can either rename or remove the tab from your dashboard. If you have content in a tab, you’ll have an option to safely remove that tab. This gives you an opportunity to transfer tab content to another tab. From there, choose which tab you’d like to transfer the content. This way, you can keep your content while removing the actual tab.
###  Sharing
You can share tab content just like you would a regular dashboard. Sharable links will navigate right to the tab that was active when you created the shareable link.
###  Embedding Dashboard Tabs
Embeddings with tabs work slightly differently. When embedding a dashboard with tabs, all the tabs will be appended to the dashboard. In this case, the embeddeding will be one dashboard with all content from all tabs.
##  7. Share your dashboard
You might want to share your dashboard with other people in your organisation. You can do this by copying the URL (or by pressing on the 🔗 button).
Sharing with your teamAI agents
Assistant
Responses are generated using AI and may contain mistakes.


